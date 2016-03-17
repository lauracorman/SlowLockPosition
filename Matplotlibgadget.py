# -*- coding: utf-8 -*-
"""
Created on Mon Jan 26 13:27:41 2015

:Author: Laura Corman

:Version: 2015-01-29

This class provides the definition of a matplotlib widget for a qt GUI that has a function to plot an image

"""
from PyQt4 import QtGui, QtCore

from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as Canvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

class MatplotlibWidget(Canvas):        
    def __init__(self, parent=None, title='Title', xlabel='', ylabel='', dpi=100, hold=False):
        super(MatplotlibWidget, self).__init__(Figure())

        self.setParent(parent)
        self.figure = Figure(dpi=dpi)
        self.figure.set_frameon(False)
        self.canvas = Canvas(self.figure)
        self.theplot = self.figure.add_subplot(111)        

#        self.theplot.set_title(title)
#        self.theplot.set_xlabel(xlabel)
#        self.theplot.set_ylabel(ylabel)

    def plotDataPoints(self, im,CLim = 4):
        self.theplot.imshow(im,vmin = 0, vmax = CLim, cmap=plt.cm.PuRd)
#        if type(CLim) == float or type(CLim) == int or type(CLim) == long:
#            self.theplot.imshow(im,vmin = 0, vmax = CLim)
#        else:
#            self.theplot.imshow(im)
        self.draw() 
        im = None