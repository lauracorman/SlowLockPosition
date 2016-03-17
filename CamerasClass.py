# -*- coding: utf-8 -*-
"""
Created on Thu Jan 22 09:50:15 2015

:Author: Laura Corman

:Version: 2015-01-29

This file define the Camera class, where all the necessary functions to work with the camera GUI are written.
It has to be inherited to specific camera types.
The implementation is done for the Lumenera cameras (Davide) and the Princeton cameras.


"""

from Lumenera_interface import Lucam
from Princeton_wrapper import Princeton,PrincetonForceClose
from masterHeader_wrapper import ShutterOpenMode 
import ExplicitAdvancedFunctions as PCO
import numpy as np
from PIL import Image
from matplotlib import pyplot
from time import sleep
import wx
import time


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
        
    timeout = property(_getTimeout,_setTimeout)
        
    def _getTypeCamera(self):
        return 'None'
        
    typecam = property(_getTypeCamera)
        


#==============================================================================
#==============================================================================
#==============================================================================
#==============================================================================
# # # # 
#==============================================================================
#==============================================================================
#==============================================================================
#==============================================================================        
        
class PrincetonCam(Camera):
    
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
        self._camera.close()
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
        
    def _getTypeCamera(self):
        return 'Princeton'
        
    typecam = property(_getTypeCamera)
    


#==============================================================================
#==============================================================================
#==============================================================================
#==============================================================================
# # # # 
#==============================================================================
#==============================================================================
#==============================================================================
#==============================================================================
        
class LumeneraCam(Camera):
    
#==============================================================================
#     Constructor
#==============================================================================
    
    def __init__(self,handle = 0,name = ''):
        self._name = name
        self._camera = None
        self._handle = handle
        self._number = 0

        #here all snapshot parameters
        
        self._width = 1392
        self._heigh = 1040
        self._pixel_depth = 1 # value of API.LUCAM_PF_16
        self._xoffset = 0
        self._yoffset = 0
        self._xbin = 1
        self._xbinflag = 0
        self._ybin = 1
        self._ybinflag = 0
        self._framerate = 1000000
        self._brightness = 1.0
        self._contrast = 1.0
        self._gamma = 1.0
        self._exposure = 10.0
        self._gain = 1.0
        self._timeout = 100000
    
#==============================================================================
#     Basic checks
#==============================================================================
        
    def checkCameraOk(self):
        print 'Not implemented'
        return True
        
    def openCamera(self,number = 0):
        """

        Find connected camera and create new Lucam class instance
        See Lumenera_interface for more informations on this class
        
        Lucam indexed from 1 -> add one to the identifier

        """
        self._number = number
        number = number + 1
        self._camera = Lucam(number)
        self._setup_camera()
        self._name = 'Lumenera camera ' + str(number)

    def _setup_camera(self):
        """

        Setup all camera parameters

        """
        self._camera.SetFormat(Lucam.FrameFormat(self._xoffset,
                                               self._yoffset,
                                               self._width,
                                               self._heigh,
                                               self._pixel_depth,
                                               binningX = self._xbin,
                                               flagsX = self._xbinflag,
                                               binningY = self._ybin,
                                               flagsY = self._ybinflag),
                             framerate = self._framerate)

        frameformat, framerate = self._camera.GetFormat()
        
        self.snapshot = Lucam.Snapshot(brightness = self._brightness,
                                  contrast = self._contrast,
                                  saturation = 1.0,
                                  exposureDelay = 0.0,
                                  hue = 0.0,
                                  gamma = self._gamma,
                                  exposure = self._exposure,
                                  gain = self._gain, 
                                  timeout = self._timeout,
                                  format = frameformat)
        
        self._camera.SetTriggerMode(True)
        
    def closeCamera(self):
        self._camera.CameraClose()
        
#==============================================================================
#     Taking pictures in various modes
#==============================================================================
        
    def takeSinglePicture(self):
        self._setup_camera()
        image = self._camera.TakeSnapshot(snapshot=self.snapshot)
        return image
        
    def takeTriggedPicture(self,nPicture = 1):
        print 'Entering Trigged Picture'
        image=[]
        try: 
            print 'Entering try'
            self._camera.EnableFastFrames(self.snapshot)
            print 'Fast Frame Enabled'
            self._camera.SetTriggerMode(True)
            print 'Trigged Mode Enables - Taking pictures'
##            first take image to discharge the CCD
#            data = self._camera.TakeFastFrame()
#            then take the right pictures
            test = self._camera.TakeFastFrame()
            image.append(test)
#            print '1'
#            test = self._camera.TakeFastFrame()
#            image.append(test)
#            print '2'
#            test = self._camera.TakeFastFrame()
#            image.append(test)
#            print '3'
#            print 'Exiting takeTriggedPIctures'
#            sleep(0.25)
            self._camera.DisableFastFrames()  
        except:
            print 'entering except'
            self.closeCamera()
            self.openCamera(self._number)
        print 'Exiting takeTriggedPIctures'
        return image
        
    def abortTakeTriggedPicture(self,nPicture = 1):
        self._camera.CancelTakeFastFrame()
        
    def startPreview(self):
        self._setup_camera()
        self._camera.CreateDisplayWindow("Preview",width=700, height=600)
        self._camera.StreamVideoControl('start_display')
        self._camera.AdjustDisplayWindow(width=700,
                              height=600)
        
    def stopPreview(self):
        self._camera.StreamVideoControl('stop_streaming')
        self._camera.DestroyDisplayWindow()
        
#==============================================================================
#     Properties
#==============================================================================
        
    def _setExposureTime(self,exposureTime):
        self._exposure = exposureTime
        self._setup_camera()
        
    def _getExposureTime(self):
        return self._exposure
        
    exposureTime = property(_getExposureTime,_setExposureTime)
        
    def _setGain(self,gain = 1):
        self._gain = gain
        self._setup_camera()
        
    def _getGain(self):
        return self._gain
        
    gain = property(_getGain,_setGain)
    
    def _getCameraInfo(self):
        print 'Not implemented'
        return 'Not implemented'
        
    def _setTimeout(self,timeout = 100000):
        self._timeout = timeout        

        frameformat, framerate = self._camera.GetFormat()
        
        self.snapshot = Lucam.Snapshot(brightness = self._brightness,
                                  contrast = self._contrast,
                                  saturation = 1.0,
                                  exposureDelay = 0.0,
                                  hue = 0.0,
                                  gamma = self._gamma,
                                  exposure = self._exposure,
                                  gain = self._gain, 
                                  timeout = self._timeout,
                                  format = frameformat)
        
    def _getTimeout(self):
        return self._timeout
        
    timeout = property(_getTimeout,_setTimeout)
        
    def _getTypeCamera(self):
        return 'Lumenera'
        
    typecam = property(_getTypeCamera)

#==============================================================================
#==============================================================================
#==============================================================================
#==============================================================================
# # # # 
#==============================================================================
#==============================================================================
#==============================================================================
#==============================================================================

class PCOCam(Camera):
    
#==============================================================================
#     Constructor
#==============================================================================
    
    def __init__(self,name = '',handle = 0):
        self._name = name
        self._camera = None
        self._handle = handle
        self._timeout = 100000
        self._listBuffers = []
        self._exposure = 300 # in us
        return
    
#==============================================================================
#     Basic checks
#==============================================================================
        
    def checkCameraOk(self):
        k = PCO.GetCameraHealthStatus(self._camera).Status
        returnString = 'Status of camera :\n'
        if k&1>0:
            returnString = returnString + '\t- Camera is in default state, no settings were changed'
        else:
            returnString = returnString + '\t- Camera is not default state, settings were changed since power up or reset'
        if k&2>0:
            returnString = returnString + '\t- Settings are valid (last "Arm Camera" was successful and no settings were changed appart from exposure time")'
        else:
            returnString = returnString + '\t- Settings were changed but not yet checked and accepted by an "Arm Camera" command'
        if k&4>0:
            returnString = returnString + '\t- Recording state is on'
        else:
            returnString = returnString + '\t- Recording state is off'
        if k&16>0:
            returnString = returnString + '\t- Framerate setting is on'
        else:
            returnString = returnString + '\t- Framerate setting is off'
        return returnString
        
    def openCamera(self,number=0):
        self._camera = PCO.OpenCamera(number)
        self._setupCamera()
        return 
        
    def _setupCamera(self):
        self._description = PCO.GetCameraDescription(self._camera)
        self._sizes = PCO.GetSizes(self._camera)
#        T = PCO.GetTemperature(self._camera)
        PCO.SetBinning(self._camera,1,1)
        PCO.SetStorageMode(self._camera,0)
        PCO.SetRecorderSubmode(self._camera,1)
        PCO.SetAcquireMode(self._camera,0)
        PCO.SetDelayExposureTime(self._camera,0,self._exposure,1,1)
        PCO.SetPixelRate(self._camera,12000000)
        
#        PCO.SetRecordingState(self._camera,0)
#        r = PCO.GetActiveRamSegment(self._camera)
        return
        
    def closeCamera(self):
        try:
            for i in range(len(self._listBuffers)):
                PCO.FreeBuffer(self._camera,self._listBuffers[i])
        except:
            print 'Could not free buffers'
        try:
            PCO.SetRecordingState(self._camera,0)
        except:
            a = PCO.GetRecordingState(self._camera)
            if not a==0:
                print 'Problem setting recording state to zero'
        PCO.CloseCamera(self._camera)
        return 
        
#==============================================================================
#     Taking pictures in various modes
#==============================================================================
        
    def takeSinglePicture(self):
#        Set right parameters (trigger mode, interlacing mode)
        PCO.SetDelayExposureTime(self._camera,0,self._exposure,1,1)
        PCO.SetTriggerMode(self._camera,0)
#        PCO.SetDoubleImageMode(self._camera,0)
#        Initialize a new buffer
        imsize = self._sizes.XResAct * self._sizes.YResAct * 2
        bufsize = imsize
        buf = PCO.AllocateBuffer(self._camera,bufsize,-1)
        bufnr = buf.BufNr
        self._listBuffers.append(bufnr)
#        Arm the camera to validate the settings
        PCO.ArmCamera(self._camera)
#        Set recording state to 1
        PCO.SetRecordingState(self._camera,1)
#        Add the buffer to the list of active buffer
        PCO.AddBufferEx(self._camera,0,0,buf.BufNr,self._sizes.XResAct,self._sizes.YResAct,self._description.wDynResDESC)
#        Wait until the buffer event is set in order to be able to read the picture
        v = 0
        while (v&32768)==0:
            bufStat = PCO.GetBufferStatus(self._camera,buf.BufNr)
            v = (bufStat.StatusDll+2**32)
            time.sleep(0.1)
#        Once the event is set, read the buffer
        im = buf.Buf[:bufsize]
        im = np.array(im)
        im = np.reshape(im[:self._sizes.XResAct*self._sizes.YResAct],(self._sizes.YResAct,self._sizes.XResAct))
#        Remove the buffer from the queue, set recording state to 0 and free the buffer
        PCO.CancelImages(self._camera)
        PCO.SetRecordingState(self._camera,0)
        PCO.FreeBuffer(self._camera,buf.BufNr)
        self._listBuffers.remove(bufnr)
        
        return im
        
    def takeTriggedPicture(self,nPicture = 1):
#        Set right parameters (trigger mode, interlacing mode)
        unit = 1
        PCO.SetDelayExposureTime(self._camera,0,self._exposure,unit,unit)
        unitStr = ''
        if unit==0:
            unitStr = 'ns'
        elif unit == 1:
            unitStr = 'us'
        elif unit == 2:
            unitStr = 'ms'
        PCO.SetTriggerMode(self._camera,2)
        PCO.SetDoubleImageMode(self._camera,1)
        time.sleep(0.1)
#        Initialize two new buffers
        imsize = self._sizes.XResAct * self._sizes.YResAct 
        print 'XResAct = ', self._sizes.XResAct,' ; YResAct = ', self._sizes.YResAct
#        print 'XResAct',self._sizes.XResAct
#        print 'YResAct',self._sizes.YResAct
        bufsize = int(1.2 * imsize)
        print 'Before initialize buffer'
        buf = PCO.AllocateBuffer(self._camera,bufsize,-1)
        bufBgd = PCO.AllocateBuffer(self._camera,bufsize,-1)
        print 'After initialize buffer'
        bufnr = buf.BufNr
        self._listBuffers.append(bufnr)
        bufnrbg = bufBgd.BufNr
        self._listBuffers.append(bufnrbg)
        print 'list of buffers', self._listBuffers
#        Arm the camera to validate the settings
        PCO.ArmCamera(self._camera)
#        Set recording state to 1
        PCO.SetRecordingState(self._camera,1)
#        Add the buffers to the list of active buffers
        PCO.AddBufferEx(self._camera,0,0,buf.BufNr,self._sizes.XResAct,self._sizes.YResAct,self._description.wDynResDESC)
        PCO.AddBufferEx(self._camera,0,0,bufBgd.BufNr,self._sizes.XResAct,self._sizes.YResAct,self._description.wDynResDESC)
#        Wait until the buffer event is set in order to be able to read the picture
        v = 0
        vBgd = 0
        vOld = 0
        vBgdOld = 0
        print 'start waiting'
        while (v&32768)==0 or (vBgd&32768)==0:
#        while (v&32768)==0:
            vOld = v
            vBgdOld = vBgd
            bufStat = PCO.GetBufferStatus(self._camera,buf.BufNr)
            v = (bufStat.StatusDll+2**32)
            bufStat = PCO.GetBufferStatus(self._camera,bufBgd.BufNr)
            vBgd = (bufStat.StatusDll+2**32)
            time.sleep(0.1)
            if not (v&32768)==(vOld&32768):
                print 'event 1 set'
            if not (vBgd&32768)==(vBgdOld&32768):
                print 'event 2 set'
#        Once the event is set, read the buffer 
        print 'try to read first buffer of size ', bufsize, ' up to ', imsize
        im = buf.Buf[:imsize]
        print 'try to read second buffer of size ', bufsize, ' up to ', imsize
        bgd = bufBgd.Buf[:imsize]
        print 'buffer saved as list'
        #im1 = np.zeros((len(im),),dtype = np.int32)
        #bgd1 = np.zeros((len(bgd),),dtype = np.int32)
        #im1[:] = im
        #bgd1[:] = bgd
#        Remove the buffer from the queue, set recording state to 0 and free the buffer
        print 'start emptying buffers' 
        PCO.SetRecordingState(self._camera,0)      
        PCO.CancelImages(self._camera)
        PCO.FreeBuffer(self._camera,buf.BufNr)
        PCO.FreeBuffer(self._camera,bufBgd.BufNr)
        self._listBuffers.remove(bufnr)
        self._listBuffers.remove(bufnrbg)
        print 'list of buffers', self._listBuffers
#        Process the pictures
        im1,im2 = self.transformListToArray(im)
        bgd1,bgd2 = self.transformListToArray(bgd)
        image = []
        image.append(im1)
        image.append(im2)
        image.append(bgd1)
        image.append(bgd2)
        return image
    
    def transformListToArray(self,im):
        lenghtOnePicture = int(len(im)/2)
        ymax = int(self._sizes.YResAct/2)
        im0 = np.asarray(im,dtype = np.int16)
        im1 = im0[0:lenghtOnePicture]
        im1 = np.reshape(im1,(ymax,self._sizes.XResAct))
        print len(im)
        im2 = im0[lenghtOnePicture:len(im)]
        im2 = np.reshape(im2,(ymax,self._sizes.XResAct))
        return im1, im2
        
    def abortTakeTriggedPicture(self,nPicture = 1):
        try:
            PCO.CancelImages(self._camera)
        except:
            print 'Could not cancel image'
        try:
            PCO.SetRecordingState(self._camera,0)
        except:
            print 'Could not set recording state to zero' 
        try:
            for i in range(len(self._listBuffers)):
                PCO.FreeBuffer(self._camera,self._listBuffers[i])
        except:
            print 'Could not free buffers'
        return self.checkCameraOk()
        
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
        self._exposure = int(exposureTime*1000) #in ms in the GUI, in us in the program 
        
    def _getExposureTime(self):
        return self._exposure/1000.
        
    exposureTime = property(_getExposureTime,_setExposureTime)
        
    def _setGain(self,gain = 1):
        return
        
    def _getGain(self):
        return 1
        
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
        
    def _getTypeCamera(self):
        return 'Pixelfly'
        
    typecam = property(_getTypeCamera)