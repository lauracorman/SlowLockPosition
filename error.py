from functools import wraps
import re
import ctypes
from sc2_SDKStructures import DWORD

SC2Lib = ctypes.cdll.LoadLibrary("SC2_Cam.dll")
#C:\Program Files\Digital Camera Toolbox\CamWare
#SC2Lib = ctypes.oledll.LoadLibrary("../pco.sdk/bin/SC2_Cam.dll")

def GetErrorText(errorCode):
    lengthCharacterArray = 2048
    characterBuffer = ctypes.create_string_buffer(lengthCharacterArray)
    getErrorText = SC2Lib.PCO_GetErrorText
    getErrorText.argtypes = (DWORD, ctypes.POINTER(ctypes.c_char), DWORD)
    getErrorText(DWORD(errorCode),characterBuffer,DWORD(lengthCharacterArray))
    return characterBuffer.value


def add_keywords(arg_name):
    """ This function is used to create a decorator that add arg_name keywords to a function"""
    s = """def add_keywords_decorator(f):
    def function({0}):return f({0})
    return function"""
    exec(s.format(', '.join(arg_name)))
    return locals()['add_keywords_decorator']

def catch_error(f, cls, doc):
    @wraps(f)
    @add_keywords(cls.python_argnames)
    def catched_func(*args):
#        print args
        a = f(*args)
        if a!=0:
            
            fich = open("PCO_err.h", "r") #to pick significations of errors
            line=fich.readlines() #list of lines of fich
            list=[] 
            for i in range(len(line)):
                if re.match(r"#define\s+(\w*)\s*(\w*)\s*// (.*)\n",line[i]):
                    list.append(re.match(r"#define\s+(\w*)\s*(\w*)\s*// (.*)\n",line[i])) #creates a list of the important lines with stuff saved in 3 entries
            
            b=hex(a+2**32)  
            errorText = GetErrorText(a+2**32)       
            b='0x'+ b[2:10].upper() #so that it has the same form as in PCO_err.h
            print 'Raw error message hexadecimal :', b   
            print errorText
            raise Exception(errorText)
#            #now find the good error
#            c=0
#            
#            #find layer
#            layer_hex='0x0000'+b[6]+'000'
#            for i in range(len(list)):
#                if layer_hex==list[i].group(2):
#                    layer=list[i].group(3)
#            #find error sources / devices
#            device_hex='0x00'+b[4]+b[5]+'0000'
#            for i in range(len(list)):
#                if device_hex==list[i].group(2):
#                    device=list[i].group(3)        
#                    
#            #find error
#            for i in range(len(list)):
#                if b==list[i].group(2):
#                    raise Exception('Error Message : "{a}", corresponding to layer "{layer}" and devices/sources "{device}" (no error means numbers were "00")'.format(a=list[i].group(3), device=device, layer=layer))
#                    c=1
#            if c==0:
#                #device = 'tada' #faire avec comme fonction P Clade et line qu'il faut b[4 et 5]
#                d=b[0:4]+'00'+b[6:10]           
#                for i in range(len(list)):
#                    if d==list[i].group(2):
#                        raise Exception('Error Message : "{a}", corresponding to layer "{layer}" and devices/sources "{device}" (no error means numbers were "00")'.format(a=list[i].group(3), device=device, layer=layer))
#                        c=1
#            if c==0:
#                #layer = b[6] #faire avec comme fonction P Clade et line qu'il faut b[6] // Je la mets plus haut en fait pour voir si renvoie tjrs le layer. Voir si pose pbs. -> surtout pour errors giGe
#                d=b[0:4]+'000'+b[7:10]           
#                for i in range(len(list)):
#                    if d==list[i].group(2):
#                        raise Exception('Error Message : "{a}", corresponding to layer "{layer}" and devices/sources "{device}" (no error means numbers were "00")'.format(a=list[i].group(3), device=device, layer=layer))
#                        c=1
#            if c==0:
#                raise Exception('no error matches...  layer "{layer}" and devices/sources "{device}" (no error means numbers were "00")'.format(a=list[i].group(3), device=device, layer=layer))
        
        #restent les erreurs avec les 4.6 Error codes for GigE, car un caractere hexadecimal en plus, mais directement bons si pas besoin d'ajouter device

        return a
    catched_func.__doc__ = doc
    catched_func.__name__ = cls._func_name
    return catched_func

