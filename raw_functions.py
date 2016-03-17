import functions
from error import catch_error
import ctypes

#class _nothing():
#    def __getattr__(self, name):
#        return lambda *args:0
#SC2Lib = _nothing()

SC2Lib = ctypes.windll.LoadLibrary("SC2_Cam.dll")
#C:\Program Files\Digital Camera Toolbox\CamWare
#SC2Lib = ctypes.oledll.LoadLibrary("../pco.sdk/bin/SC2_Cam.dll")

_all_functions = {}

for key,val in functions._all_functions.iteritems():
    cfunc = getattr(SC2Lib, 'PCO_'+key)
    cfunc.argtypes = val.argtypes
    func = catch_error(cfunc, val, val.__doc__)
    _all_functions[key] = func
    exec('{key} = func'.format(key=key))


# t = (ctypes.c_ulong*10000000)()
# **WORD : POINTER(tt) avevc tt = (ctypes.c_ulong*10000000) pour argtypes
# byref(t) dans l'appelde la fonction