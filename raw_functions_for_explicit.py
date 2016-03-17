import functions
from error import catch_error
import ctypes

idf = open('ExplicitRawFunctions.py','w')

idf.writelines(['import functions\n',
                'from error import catch_error\n',
                'import ctypes\n',
                '\n',
                '_all_functions = {}\n',
                'SC2Lib = ctypes.windll.LoadLibrary("SC2_Cam.dll")',
                '\n',
                'for key,val in functions._all_functions.iteritems():\n',
                '    cfunc = getattr(SC2Lib, "PCO_"+key)\n',
                '    cfunc.argtypes = val.argtypes\n',
                '    func = catch_error(cfunc, val, val.__doc__)\n',
                '\n',
                '\n',
                '\n',
                '\n',
                '\n',
                '\n',
                '\n'])

_all_functions = {}

#class _nothing():
#    def __getattr__(self, name):
#        return lambda *args:0
#SC2Lib = _nothing()

SC2Lib = ctypes.windll.LoadLibrary("SC2_Cam.dll")
#C:\Program Files\Digital Camera Toolbox\CamWare
#SC2Lib = ctypes.oledll.LoadLibrary("../pco.sdk/bin/SC2_Cam.dll")

_all_functions = {}

for key,val in functions._all_functions.iteritems():
    idf.writelines(['val=functions._all_functions.get("'+key+'")\n',
                    'cfunc = getattr(SC2Lib, "PCO_'+key+'")\n',
                    'cfunc.argtypes = val.argtypes\n',
                    'func = catch_error(cfunc, val, val.__doc__)\n',
                    '_all_functions["'+key+'"] = func\n',
                    '{key} = func'.format(key=key),
                    '\n',
                    '\n',
                    '\n'])
#    cfunc = getattr(SC2Lib, 'PCO_'+key)
#    cfunc.argtypes = val.argtypes
#    func = catch_error(cfunc, val, val.__doc__)
#    _all_functions[key] = func
#    exec('{key} = func'.format(key=key))

idf.close()

# t = (ctypes.c_ulong*10000000)()
# **WORD : POINTER(tt) avevc tt = (ctypes.c_ulong*10000000) pour argtypes
# byref(t) dans l'appelde la fonction