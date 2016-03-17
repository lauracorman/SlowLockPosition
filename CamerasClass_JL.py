# -*- coding: utf-8 -*-
"""
Created on Thu Jan 22 09:50:15 2015

:Author: Laura Corman

:Version: 2015-01-29

This file define the Camera class, where all the necessary functions to work with the camera GUI are written.
It has to be inherited to specific camera types.
The implementation is done for the Lumenera cameras (Davide) and the Princeton cameras.


"""

#from Lumenera_interface import Lucam
from Princeton_wrapper import Princeton,PrincetonForceClose
from masterHeader_wrapper import ShutterOpenMode 
import numpy as np
from PIL import Image
from matplotlib import pyplot
from time import sleep
import wx
import ExplicitAdvancedFunctions


class Camera(object):
    
#==============================================================================
#     Constructor
#==============================================================================
    
    def __init__(self,name = '',handle = 0):
        self._name = name
        self._camera = None
        self._handle = handle
        self._timeout = 100000
    
#==============================================================================
#     Basic checks
#==============================================================================
        
    def checkCameraOk(self):
        print 'Not implemented'
        return False
        
    def openCamera(self):
        print 'Not implemented'
        return 0
        
    def closeCamera(self):
        print 'Not implemented'
        return 0
        
#==============================================================================
#     Taking pictures in various modes
#==============================================================================
        
    def takeSinglePicture(self):
        print 'Not implemented'
        return 0
        
    def takeTriggedPicture(self,nPicture = 1):
        print 'Not implemented'
        return 0
        
    def abortTakeTriggedPicture(self,nPicture = 1):
        print 'Not implemented'
        return 0
        
    def startPreview(self):
        print 'Not implemented'
        return 0
        
    def stopPreview(self):
        print 'Not implemented'
        return 0
        
#==============================================================================
#     Properties
#==============================================================================
        
    def _setExposureTime(self,exposureTime):
        print 'Not implemented'
        
    def _getExposureTime(self):
        print 'Not implemented'
        return 0
        
    exposureTime = property(_getExposureTime,_setExposureTime)
        
    def _setGain(self,gain = 1):
        print 'Not implemented'
        
    def _getGain(self):
        print 'Not implemented'
        
    gain = property(_getGain,_setGain)
        
    def _getName(self):
        return self._name
        
    name = property(_getName)
        
    def _getID(self):
        return self._handle
        
    ID = property(_getID)
    
    def _getCameraInfo(self):
        print 'Not implemented'
        return 'Not implemented'
        
    def _setTimeout(self,timeout = 100000):
        self._timeout = timeout
        
    def _getTimeout(self):
        return self._timeout
        
    timeout = property(_setTimeout,_getTimeout)
        
#class PrincetonCam(Camera):
#    
##==============================================================================
##     Constructor
##==============================================================================
#    
#    def __init__(self,handle = 0,name = ''):
#        self._name = name
#        self._camera = None
#        self._handle = handle
#    
##==============================================================================
##     Basic checks
##==============================================================================
#        
#    def checkCameraOk(self):
#        return self._camera.checkCameraOK()
#        
#    def openCamera(self,number = 0):
#        try:
#            self._camera = Princeton(number)
#        except:
#            PrincetonForceClose(number)
#            print 'Try force closing princeton camera with handle ' + str(number)
#            self._camera = Princeton(number)
#        self._name = 'Princeton camera ' + str(number+1)
#        
#    def closeCamera(self):
#        self._camera.close()
#        return 
#        
##==============================================================================
##     Taking pictures in various modes
##==============================================================================
#        
#    def takeSinglePicture(self):
#        if self._camera.kineticsEnabled:
#            self._camera.disableKineticsMode()
##        self._camera.shutterOpenMode = ShutterOpenMode.preexposure
#        (image,infos) = self._camera.takePicture()
#        return image[0][0]
#        
#    def takeTriggedPicture(self,nPicture = 1,kineticsWindowSize = 256):
##        Takes the picture in kinetics mode
#        if not self._camera.kineticsEnabled:
#            self._camera.enableKineticsMode(kineticsWindowSize)
##        self._camera.shutterOpenMode = ShutterOpenMode.preexposure
#        print 'Princeton cam taking picture starting'
#        (ims,infos) = self._camera.takeTriggedPicture()
#        print 'Princeton cam taking picture done'
#        
##        Converts it into 3 pictures given the kinetics window size
#        ims = ims[0][0]
#        if not self._camera.kineticsWindowSize == 256:
#            return ims
#        image = []
#        kwSize = 256
#        image.append(ims[kwSize:(2*kwSize),:])
#        image.append(ims[(2*kwSize):(3*kwSize),:])
#        image.append(ims[(3*kwSize):(4*kwSize),:])
#        
#        return image
#        
#    def abortTakeTriggedPicture(self,nPicture = 1):
#        print 'Not implemented'
#        return 0
#        
#    def startPreview(self):
#        try:
#            self._camera.disableKineticsMode()
#        except:
#            print 'Couldd not disable Kinetics mode of princeton camera'
#        self._camera.startContinuous()
#        SIZE = (1024, 1024)
#        
#        def get_image(xc,yc):
#        #    x = np.linspace(-320,320,640)
#        #    y = np.linspace(-240,240,480)
#        #    X,Y = np.meshgrid(x,y)
#        #    image = np.sqrt(X**2 + Y**2)<iteration
#        #    image = image.astype(int) * 256
#            statusString, statusNumber, byteCounted, bufferCounted = self._camera.exposureCheckContinuousStatus()
#            while not statusNumber == 3:
#                statusString, statusNumber, byteCounted, bufferCounted = self._camera.exposureCheckContinuousStatus()
#                sleep(0.1)
#            image = self._camera.retrieveContinuousFrame()
#            image = image/np.max(image[:])
#            # Put your code here to return a PIL image from the camera.
#            return Image.fromarray(np.uint8(pyplot.cm.jet(image)*255))
#        
#        def pil_to_wx(image):
#            width, height = image.size
#            buffer = image.convert('RGB').tostring()
#            bitmap = wx.BitmapFromBuffer(width, height, buffer)
#            return bitmap
#        
#        class Panel(wx.Panel):
#            xc = np.linspace(0,2*np.pi,500)
#            iteration = 0
#            def __init__(self, parent):
#                super(Panel, self).__init__(parent, -1)
#                self.SetSize(SIZE)
#                self.SetBackgroundStyle(wx.BG_STYLE_CUSTOM)
#                self.Bind(wx.EVT_PAINT, self.on_paint)
#                self.update()
#            def update(self):
#                self.Refresh()
#                self.Update()
#                wx.CallLater(15, self.update)
#            def create_bitmap(self):
#                index = np.mod(self.iteration,500)
#                rho = 0.7
#                shift = 0.1
#                image = get_image(rho*np.cos(self.xc[index])-shift,rho*np.sin(self.xc[index]))
#                self.iteration = self.iteration + 1
#                bitmap = pil_to_wx(image)
#                return bitmap
#            def on_paint(self, event):
#                bitmap = self.create_bitmap()
#                dc = wx.AutoBufferedPaintDC(self)
#                dc.DrawBitmap(bitmap, 0, 0)
#        
#        class Frame(wx.Frame):
#            def __init__(self):
#                style = wx.DEFAULT_FRAME_STYLE & ~wx.RESIZE_BORDER & ~wx.MAXIMIZE_BOX
#                super(Frame, self).__init__(None, -1, 'Camera Viewer', style=style)
#                panel = Panel(self)
#                self.Fit()
#        
#        app = wx.PySimpleApp()
#        frame = Frame()
#        frame.Center()
#        frame.Show()
#        app.MainLoop()
#        
#    def stopPreview(self):
#        self._camera.stopContinuous()
#        
##==============================================================================
##     Properties
##==============================================================================
#        
#    def _setExposureTime(self,exposureTime):
#        self._camera.expTime = int(exposureTime*1000) # in microseconds by default
#        
#    def _getExposureTime(self):
#        return self._camera.expTime/1000. # in microseconds by default
#        
#    exposureTime = property(_getExposureTime,_setExposureTime)
#        
#    def _setGain(self,gain = 1):
#        return
#        
#    def _getGain(self):
#        return 1
#        
#    gain = property(_getGain,_setGain)
#    
#    def _getCameraInfo(self):
#        print 'Not implemented'
#        return 'Not implemented'
#        
#class LumeneraCam(Camera):
#    
##==============================================================================
##     Constructor
##==============================================================================
#    
#    def __init__(self,handle = 0,name = ''):
#        self._name = name
#        self._camera = None
#        self._handle = handle
#        self._number = 0
#
#        #here all snapshot parameters
#        
#        self._width = 1392
#        self._heigh = 1040
#        self._pixel_depth = 1 # value of API.LUCAM_PF_16
#        self._xoffset = 0
#        self._yoffset = 0
#        self._xbin = 1
#        self._xbinflag = 0
#        self._ybin = 1
#        self._ybinflag = 0
#        self._framerate = 1000000
#        self._brightness = 1.0
#        self._contrast = 1.0
#        self._gamma = 1.0
#        self._exposure = 10.0
#        self._gain = 1.0
#        self._timeout = 100000
#    
##==============================================================================
##     Basic checks
##==============================================================================
#        
#    def checkCameraOk(self):
#        print 'Not implemented'
#        return True
#        
#    def openCamera(self,number = 0):
#        """
#
#        Find connected camera and create new Lucam class instance
#        See Lumenera_interface for more informations on this class
#        
#        Lucam indexed from 1 -> add one to the identifier
#
#        """
#        self._number = number
#        number = number + 1
#        self._camera = Lucam(number)
#        self._setup_camera()
#        self._name = 'Lumenera camera ' + str(number)
#
#    def _setup_camera(self):
#        """
#
#        Setup all camera parameters
#
#        """
#        self._camera.SetFormat(Lucam.FrameFormat(self._xoffset,
#                                               self._yoffset,
#                                               self._width,
#                                               self._heigh,
#                                               self._pixel_depth,
#                                               binningX = self._xbin,
#                                               flagsX = self._xbinflag,
#                                               binningY = self._ybin,
#                                               flagsY = self._ybinflag),
#                             framerate = self._framerate)
#
#        frameformat, framerate = self._camera.GetFormat()
#        
#        self.snapshot = Lucam.Snapshot(brightness = self._brightness,
#                                  contrast = self._contrast,
#                                  saturation = 1.0,
#                                  exposureDelay = 0.0,
#                                  hue = 0.0,
#                                  gamma = self._gamma,
#                                  exposure = self._exposure,
#                                  gain = self._gain, 
#                                  timeout = self._timeout,
#                                  format = frameformat)
#        
#        self._camera.SetTriggerMode(True)
#        
#    def closeCamera(self):
#        self._camera.CameraClose()
#        
##==============================================================================
##     Taking pictures in various modes
##==============================================================================
#        
#    def takeSinglePicture(self):
#        self._setup_camera()
#        image = self._camera.TakeSnapshot(snapshot=self.snapshot)
#        return image
#        
#    def takeTriggedPicture(self,nPicture = 1):
#        image=[]
#        try: 
#            self._camera.EnableFastFrames(self.snapshot)
#            self._camera.SetTriggerMode(True)
#            image.append(self._camera.TakeFastFrame())
#            image.append(self._camera.TakeFastFrame())
#            image.append(self._camera.TakeFastFrame())
#            sleep(0.25)
#            self._camera.DisableFastFrames()  
#        except:
#            self.closeCamera()
#            self.openCamera(self._number)
#        return image
#        
#    def abortTakeTriggedPicture(self,nPicture = 1):
#        self._camera.CancelTakeFastFrame()
#        
#    def startPreview(self):
#        self._setup_camera()
#        self._camera.CreateDisplayWindow("Preview",width=700, height=600)
#        self._camera.StreamVideoControl('start_display')
#        self._camera.AdjustDisplayWindow(width=700,
#                              height=600)
#        
#    def stopPreview(self):
#        self._camera.StreamVideoControl('stop_streaming')
#        self._camera.DestroyDisplayWindow()
#        
##==============================================================================
##     Properties
##==============================================================================
#        
#    def _setExposureTime(self,exposureTime):
#        self._exposure = exposureTime
#        
#    def _getExposureTime(self):
#        return self._exposure
#        
#    exposureTime = property(_getExposureTime,_setExposureTime)
#        
#    def _setGain(self,gain = 1):
#        self._gain = gain
#        
#    def _getGain(self):
#        return self._gain
#        
#    gain = property(_getGain,_setGain)
#    
#    def _getCameraInfo(self):
#        print 'Not implemented'
#        return 'Not implemented'
#        
#    def _setTimeout(self,timeout = 100000):
#        self._timeout = timeout        
#
#        frameformat, framerate = self._camera.GetFormat()
#        
#        self.snapshot = Lucam.Snapshot(brightness = self._brightness,
#                                  contrast = self._contrast,
#                                  saturation = 1.0,
#                                  exposureDelay = 0.0,
#                                  hue = 0.0,
#                                  gamma = self._gamma,
#                                  exposure = self._exposure,
#                                  gain = self._gain, 
#                                  timeout = self._timeout,
#                                  format = frameformat)
#        
#    def _getTimeout(self):
#        return self._timeout
#        
#    timeout = property(_getTimeout,_setTimeout)




class PixelflyCam(Camera):
    
#==============================================================================
#     Constructor
#==============================================================================
    
    def __init__(self,handle = 0,name = ''):
        self._name = name
        self._camera = None
        self._handle = handle
    
#==============================================================================
#     Basic checks
#==============================================================================
        
    def checkCameraOk(self):
        return self._camera.checkCameraOK()
        
    def openCamera(self,number = 0):
        try:
            self._camera = Princeton(number)
        except:
            PrincetonForceClose(number)
            print 'Try force closing princeton camera with handle ' + str(number)
            self._camera = Princeton(number)
        self._name = 'Princeton camera ' + str(number+1)
        
    def closeCamera(self):
        CloseCamera(self._handle)
        return 
        
#==============================================================================
#     Taking pictures in various modes
#==============================================================================
        
    def takeSinglePicture(self):
        if self._camera.kineticsEnabled:
            self._camera.disableKineticsMode()
#        self._camera.shutterOpenMode = ShutterOpenMode.preexposure
        (image,infos) = self._camera.takePicture()
        return image[0][0]
        
    def takeTriggedPicture(self,nPicture = 1,kineticsWindowSize = 256):
#        Takes the picture in kinetics mode
        if not self._camera.kineticsEnabled:
            self._camera.enableKineticsMode(kineticsWindowSize)
#        self._camera.shutterOpenMode = ShutterOpenMode.preexposure
        print 'Princeton cam taking picture starting'
        (ims,infos) = self._camera.takeTriggedPicture()
        print 'Princeton cam taking picture done'
        
#        Converts it into 3 pictures given the kinetics window size
        ims = ims[0][0]
        if not self._camera.kineticsWindowSize == 256:
            return ims
        image = []
        kwSize = 256
        image.append(ims[kwSize:(2*kwSize),:])
        image.append(ims[(2*kwSize):(3*kwSize),:])
        image.append(ims[(3*kwSize):(4*kwSize),:])
        
        return image
        
    def abortTakeTriggedPicture(self,nPicture = 1):
        print 'Not implemented'
        return 0
        
    def startPreview(self):
        try:
            self._camera.disableKineticsMode()
        except:
            print 'Couldd not disable Kinetics mode of princeton camera'
        self._camera.startContinuous()
        SIZE = (1024, 1024)
        
        def get_image(xc,yc):
        #    x = np.linspace(-320,320,640)
        #    y = np.linspace(-240,240,480)
        #    X,Y = np.meshgrid(x,y)
        #    image = np.sqrt(X**2 + Y**2)<iteration
        #    image = image.astype(int) * 256
            statusString, statusNumber, byteCounted, bufferCounted = self._camera.exposureCheckContinuousStatus()
            while not statusNumber == 3:
                statusString, statusNumber, byteCounted, bufferCounted = self._camera.exposureCheckContinuousStatus()
                sleep(0.1)
            image = self._camera.retrieveContinuousFrame()
            image = image/np.max(image[:])
            # Put your code here to return a PIL image from the camera.
            return Image.fromarray(np.uint8(pyplot.cm.jet(image)*255))
        
        def pil_to_wx(image):
            width, height = image.size
            buffer = image.convert('RGB').tostring()
            bitmap = wx.BitmapFromBuffer(width, height, buffer)
            return bitmap
        
        class Panel(wx.Panel):
            xc = np.linspace(0,2*np.pi,500)
            iteration = 0
            def __init__(self, parent):
                super(Panel, self).__init__(parent, -1)
                self.SetSize(SIZE)
                self.SetBackgroundStyle(wx.BG_STYLE_CUSTOM)
                self.Bind(wx.EVT_PAINT, self.on_paint)
                self.update()
            def update(self):
                self.Refresh()
                self.Update()
                wx.CallLater(15, self.update)
            def create_bitmap(self):
                index = np.mod(self.iteration,500)
                rho = 0.7
                shift = 0.1
                image = get_image(rho*np.cos(self.xc[index])-shift,rho*np.sin(self.xc[index]))
                self.iteration = self.iteration + 1
                bitmap = pil_to_wx(image)
                return bitmap
            def on_paint(self, event):
                bitmap = self.create_bitmap()
                dc = wx.AutoBufferedPaintDC(self)
                dc.DrawBitmap(bitmap, 0, 0)
        
        class Frame(wx.Frame):
            def __init__(self):
                style = wx.DEFAULT_FRAME_STYLE & ~wx.RESIZE_BORDER & ~wx.MAXIMIZE_BOX
                super(Frame, self).__init__(None, -1, 'Camera Viewer', style=style)
                panel = Panel(self)
                self.Fit()
        
        app = wx.PySimpleApp()
        frame = Frame()
        frame.Center()
        frame.Show()
        app.MainLoop()
        
    def stopPreview(self):
        self._camera.stopContinuous()
        
#==============================================================================
#     Properties
#==============================================================================
        
    def _setExposureTime(self,exposureTime):
        self._camera.expTime = int(exposureTime*1000) # in microseconds by default
        
    def _getExposureTime(self):
        return self._camera.expTime/1000. # in microseconds by default
        
    exposureTime = property(_getExposureTime,_setExposureTime)
        
    def _setGain(self,gain = 1):
        return
        
    def _getGain(self):
        return 1
        
    gain = property(_getGain,_setGain)
    
    def _getCameraInfo(self):
        print 'Not implemented'
        return 'Not implemented'
        