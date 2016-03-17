# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 14:57:56 2015

@author: BEC
"""

#!/usr/bin/env python
from pylab import *
from PIL import Image
from scipy import optimize
from scipy import signal
import tifffile as tiff


#image_with = 1.*array(Image.open('WithAtoms.tif'))
#image_noatoms = 1.*array(Image.open('NoAtoms.tif'))
#image_background = 1.*array(Image.open('Background.tif'))
#
#Transmission = (image_with-image_background)/(image_noatoms-image_background)
#Optical_Thickness = nan_to_num(-log(Transmission))
#Optical_Thickness[Optical_Thickness<0]=0
#Optical_Thickness[Optical_Thickness>6]=0

####### GAUSSIAN FIT ######

def gaussian(height, center_x, center_y, width_x, width_y,offset):
	"""Returns a gaussian function with the given parameters"""
	width_x = float(width_x)
	width_y = float(width_y)
	return lambda x,y: offset + height*exp(-(((center_x-x)/width_x)**2+((center_y-y)/width_y)**2)/2)

def moments(dataa):
    """Returns (height, x, y, width_x, width_y) the gaussian parameters of a 2D distribution by calculating its moments """
    offset = dataa.min()
    data = dataa - offset
    total = data.sum()
    X, Y = indices(data.shape)
    x = (X*data).sum()/total
    y = (Y*data).sum()/total	
    col = data[:, int(y)]
    width_x = sqrt(abs((arange(col.size)-y)**2*col).sum()/col.sum())
    row = data[int(x), :]
    width_y = sqrt(abs((arange(row.size)-x)**2*row).sum()/row.sum())
    height = data.max()
    return height, x, y, width_x, width_y,offset

def fitgaussian(data):
	"""Returns (height, x, y, width_x, width_y) the gaussian parameters of a 2D distribution found by a fit"""
	params = moments(data)
	errorfunction = lambda p: ravel(gaussian(*p)(*indices(data.shape)) - data)
	p, success = optimize.leastsq(errorfunction, params)
	return p

######## END GAUSSIAN FIT ######


im = tiff.imread('test.tif')
im = signal.convolve2d(im,np.ones((15,15)),mode='same')
params = fitgaussian(im)
fit = gaussian(*params)

subplot(1,2,1)
imshow(im)
colorbar()

subplot(1,2,2)
imshow(fit(*indices(im.shape)))
colorbar()

show()
