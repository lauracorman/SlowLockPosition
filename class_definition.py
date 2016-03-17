
import ctypes
from ctypes import *

from sc2_SDKStructures import PCO_Sensor, PCO_Timing, SHORT, WORD, int, PCO_Recording, PCO_Image, PCO_CameraType, PCO_Segment, PCO_General, PCO_Description, DWORD, HANDLE, BYTE, PCO_Storage


class Argument(object):
    def __init__(self, type_name, arg_name, is_output=None):
        self.type_name = type_name
        self.arg_name = arg_name
        self._ctypes = eval(self.type_name)
        if is_output is not None:
            self.is_output = is_output
    @property
    def _python_arg_name(self):
        """ Name without the C type prefix """
        name = self.arg_name
        if self.type_name=='WORD' and name.startswith('w'):
            return name[1:]
        if self.type_name=='SHORT' and name.startswith('s'):
            return name[1:]
        if self.type_name=='DWORD' and name.startswith('dw'):
            return name[2:]
        if self.type_name=='BYTE' and name.startswith('uc'):
            return name[2:]
        if self.type_name=='HANDLE' and name.startswith('h'):
            return name[1:]
        if self.type_name=='HANDLE' and name=="ph":
            return 'handle'
        return name

    @property
    def python_arg_name(self):
        out = self._python_arg_name
        if out[0]=='1':
            return 'first'+out[1:]
        return out

    @property
    def output_string(self):
        if hasattr(self._ctypes, 'value'):
            return self.python_arg_name+'.value'
        else:
            return self.python_arg_name

    _is_output = False

    @property
    def ctypes(self):
        return self._ctypes

    @property
    def is_output(self):
        return self._is_output

    def __repr__(self):
        return '{name}(arg_name="{self.arg_name}", type_name="{self.type_name}")'.format(name=type(self).__name__, self=self) 

class ArgumentPointer(Argument):
    _is_output = True
    
    @property
    def ctypes(self):
        return ctypes.POINTER(self._ctypes)


class ArgumentDoublePointer(ArgumentPointer):
    @property
    def ctypes(self):
        return ctypes.POINTER(ctypes.POINTER(self._ctypes))


#adv_func_output="""
#def func({val.advanced_declaration_string}):
#{val.advanced_output_initialisation_string}
#{val.named_tuple_string}
#    raw_functions.{key}({val.python_argnames_string})
#{val.advanced_return_string}
#"""    

adv_func_output="""({val.advanced_declaration_string}):
{val.advanced_output_initialisation_string}
{val.named_tuple_string}
    raw_functions.{key}({val.python_argnames_string})
{val.advanced_return_string}
"""    

#adv_func="""
#def func({val.advanced_declaration_string}):
#    raw_functions.{key}({val.python_argnames_string})
#"""  

adv_func="""({val.advanced_declaration_string}):
    raw_functions.{key}({val.python_argnames_string})
"""    

types_with_wSize = ["PCO_OpenStruct","PCO_CameraType","PCO_General","PCO_Description",
                    "PCO_Description2","PCO_DescriptionEx","PCO_Single_Signal_Desc",
                    "PCO_Signal_Description","PCO_Sensor","PCO_Signal","PCO_ImageTiming",
                    "PCO_Timing","PCO_Storage","PCO_Recording","PCO_Segment",
                    "PCO_Image_ColorSet","PCO_Image"]

class FunctionDefMetaclass(type):
    @property
    def argtypes(self):
        return [elm.ctypes for elm in self._arg_list]

    @property
    def argnames(self):
        return [elm.arg_name for elm in self._arg_list]

    @property
    def python_argnames(self):
        return [elm.python_arg_name for elm in self._arg_list]

    @property
    def python_argnames_string(self):
        return ', '.join(self.python_argnames)

    @property
    def input_args(self):
        return [elm for elm in self._arg_list if not elm.is_output]

    @property
    def output_args(self):
        return [elm for elm in self._arg_list if elm.is_output]

    @property
    def advanced_declaration_string(self):
        out = ", ".join([elm.python_arg_name for elm in self.input_args])
#        out += ", " + ", ".join([elm.python_arg_name+" = None" for elm in self.intput_args])
        return out

    @property
    def advanced_output_initialisation_string(self):
        out = []
        for elm in self.output_args:
            thisTypeName = elm.type_name
            thisArgName = elm.python_arg_name
            out.append("    _" + thisArgName + " = " + thisTypeName + "()\n")
            if any(typeName in thisTypeName for typeName in types_with_wSize):
                out.append("    _" + thisArgName + ".wSize = ctypes.sizeof(_" + thisArgName + ")\n")
#                out.append("    print _" + thisArgName + ".wSize\n")
#                out.append("    _" + thisArgName + ".wSize = 1364\n")
#                out.append('    print _' + thisArgName + ".wSize")
            out.append("    {elm.python_arg_name} = ctypes.byref(_{elm.python_arg_name})".format(elm=elm))
        return '\n'.join(out)

#    @property
#    def advanced_output_initialisation_string(self):
#        out = []
#        for elm in self.output_args:
#            out.append("    _{elm.python_arg_name} = {elm.type_name}()\n    {elm.python_arg_name} = ctypes.byref(_{elm.python_arg_name})".format(elm=elm))
#        return '\n'.join(out)

    @property
    def named_tuple_string(self):
        out = "    out_type = namedtuple('{self._func_name}OutputTuple', [{names}])".format(self=self, names= ", ".join(["'"+elm.python_arg_name+"'" for elm in self.output_args]))
        return out

    @property
    def advanced_return_string(self):
        if len(self.output_args)==1:
            out = "    return _{names}".format(names= ", ".join([elm.output_string for elm in self.output_args]))
        else:
            out = "    return out_type({names})".format(names= ", ".join([elm.python_arg_name+"=_" + elm.output_string for elm in self.output_args]))
        return out

    @property
    def output_doc(self):
        if len(self.output_args)==0:
            return "No output"
        return "Output : {names}".format(names= ", ".join([elm.python_arg_name for elm in self.output_args]))

    @property
    def advanced_function_string(self):
        if self.output_args:
            cmd = adv_func_output.format(key=self._func_name, val=self)
        else:
            cmd = adv_func.format(key=self._func_name, val=self)
        return cmd

    @property
    def is_method(self):
        arg0 = self._arg_list[0]
        if isinstance(arg0, Argument) and arg0.type_name=='HANDLE' and not isinstance(arg0, ArgumentPointer):
            return True
        return False

class FunctionDef(object):
    __metaclass__ = FunctionDefMetaclass


