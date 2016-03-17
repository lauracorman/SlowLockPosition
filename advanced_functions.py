import functions
import raw_functions
from collections import namedtuple

from class_definition import *
import ctypes


""" This module automatically creates the output variable passed as references 
The output of the function is either nothing, or one value or a namedtupple
"""

idf = open('explicitAdvancedFunctionsNext.py','w')

idf.writelines(['import functions\n',
                'import raw_functions\n',
                'from collections import namedtuple\n',
                '\n',
                'from class_definition import *\n',
                'import ctypes\n',
                '\n',
                '_all_functions = {}\n',
                '\n',
                '\n',
                '\n',
                '\n'])

_all_functions = {}


for key,val in functions._all_functions.iteritems():
    idf.write('def '+key+val.advanced_function_string)
    raw_func = raw_functions._all_functions[key]
    #print val.advanced_function_string
#    exec(val.advanced_function_string)
#    func.__name__ =  raw_func.__name__
#    func.__doc__ = raw_func.__doc__ + '\n' + val.output_doc
#    _all_functions[key] = func
#    exec('{key} = func'.format(key=key))
    idf.writelines(['\n', '\n'])


#_all_functions = {}
#
#
#for key,val in functions._all_functions.iteritems():
#    raw_func = raw_functions._all_functions[key]
#    #print val.advanced_function_string
#    exec(val.advanced_function_string)
#    func.__name__ =  raw_func.__name__
#    func.__doc__ = raw_func.__doc__ + '\n' + val.output_doc
#    _all_functions[key] = func
#    exec('{key} = func'.format(key=key))



