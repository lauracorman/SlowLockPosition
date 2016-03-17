# -*- coding: utf-8 -*-
"""
Created on Fri Jan 23 19:00:00 2015

@author: tempo
"""

from distutils.core import setup, Extension
import numpy
setup(name='_tifffile',ext_modules=[Extension('_tifffile', ['tifffile.c'],include_dirs=[numpy.get_include()])])