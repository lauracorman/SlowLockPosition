import functions
#import ExplicitRawFunctions as raw_functions
import raw_functions
from collections import namedtuple

from class_definition import *
import ctypes

_all_functions = {}




def GetRecordingStruct(handle):
    _strRecording = PCO_Recording()

    _strRecording.wSize = ctypes.sizeof(_strRecording)

    strRecording = ctypes.byref(_strRecording)
    out_type = namedtuple('GetRecordingStructOutputTuple', ['strRecording'])
    raw_functions.GetRecordingStruct(handle, strRecording)
    return _strRecording


def SetTimestampMode(handle, TimeStampMode):
    raw_functions.SetTimestampMode(handle, TimeStampMode)


def GetCOCRuntime(handle):
    _Time_s = DWORD()

    Time_s = ctypes.byref(_Time_s)
    _Time_us = DWORD()

    Time_us = ctypes.byref(_Time_us)
    out_type = namedtuple('GetCOCRuntimeOutputTuple', ['Time_s', 'Time_us'])
    raw_functions.GetCOCRuntime(handle, Time_s, Time_us)
    return out_type(Time_s=_Time_s.value, Time_us=_Time_us.value)


def GetActiveRamSegment(handle):
    _ActSeg = WORD()

    ActSeg = ctypes.byref(_ActSeg)
    out_type = namedtuple('GetActiveRamSegmentOutputTuple', ['ActSeg'])
    raw_functions.GetActiveRamSegment(handle, ActSeg)
    return _ActSeg.value


def GetCameraHealthStatus(handle):
    _Warn = DWORD()
    
    Warn = ctypes.byref(_Warn)
    _Err = DWORD()
    
    Err = ctypes.byref(_Err)
    _Status = DWORD()
    
    Status = ctypes.byref(_Status)
    out_type = namedtuple('GetCameraHealthStatusOutputTuple', ['Warn', 'Err', 'Status'])
    raw_functions.GetCameraHealthStatus(handle, Warn, Err, Status)
    return out_type(Warn=_Warn.value, Err=_Err.value, Status=_Status.value)


def GetRecordingState(handle):
    _RecState = WORD()

    RecState = ctypes.byref(_RecState)
    out_type = namedtuple('GetRecordingStateOutputTuple', ['RecState'])
    raw_functions.GetRecordingState(handle, RecState)
    return _RecState.value


def SetTimingStruct(handle):
    _strTiming = PCO_Timing()

    _strTiming.wSize = ctypes.sizeof(_strTiming)

    strTiming = ctypes.byref(_strTiming)
    out_type = namedtuple('SetTimingStructOutputTuple', ['strTiming'])
    raw_functions.SetTimingStruct(handle, strTiming)
    return _strTiming


def GetDoubleImageMode(handle):
    _DoubleImage = WORD()

    DoubleImage = ctypes.byref(_DoubleImage)
    out_type = namedtuple('GetDoubleImageModeOutputTuple', ['DoubleImage'])
    raw_functions.GetDoubleImageMode(handle, DoubleImage)
    return _DoubleImage.value


def GetPendingBuffer(handle):
    _count = int()

    count = ctypes.byref(_count)
    out_type = namedtuple('GetPendingBufferOutputTuple', ['count'])
    raw_functions.GetPendingBuffer(handle, count)
    return _count.value


def GetNumberOfImagesInSegment(handle, Segment):
    _ValidImageCnt = DWORD()

    ValidImageCnt = ctypes.byref(_ValidImageCnt)
    _MaxImageCnt = DWORD()

    MaxImageCnt = ctypes.byref(_MaxImageCnt)
    out_type = namedtuple('GetNumberOfImagesInSegmentOutputTuple', ['ValidImageCnt', 'MaxImageCnt'])
    raw_functions.GetNumberOfImagesInSegment(handle, Segment, ValidImageCnt, MaxImageCnt)
    return out_type(ValidImageCnt=_ValidImageCnt.value, MaxImageCnt=_MaxImageCnt.value)


def GetAcquireMode(handle):
    _AcquMode = WORD()

    AcquMode = ctypes.byref(_AcquMode)
    out_type = namedtuple('GetAcquireModeOutputTuple', ['AcquMode'])
    raw_functions.GetAcquireMode(handle, AcquMode)
    return _AcquMode.value


def InitiateSelftestProcedure(handle):
    raw_functions.InitiateSelftestProcedure(handle)


def GetConversionFactor(handle):
    _ConvFact = WORD()

    ConvFact = ctypes.byref(_ConvFact)
    out_type = namedtuple('GetConversionFactorOutputTuple', ['ConvFact'])
    raw_functions.GetConversionFactor(handle, ConvFact)
    return _ConvFact.value


def GetBufferStatus(handle, BufNr):
    _StatusDll = DWORD()

    StatusDll = ctypes.byref(_StatusDll)
    _StatusDrv = DWORD()

    StatusDrv = ctypes.byref(_StatusDrv)
    out_type = namedtuple('GetBufferStatusOutputTuple', ['StatusDll', 'StatusDrv'])
    raw_functions.GetBufferStatus(handle, BufNr, StatusDll, StatusDrv)
    return out_type(StatusDll=_StatusDll.value, StatusDrv=_StatusDrv.value)


def SetRecordingStruct(handle):
    _strRecording = PCO_Recording()

    _strRecording.wSize = ctypes.sizeof(_strRecording)

    strRecording = ctypes.byref(_strRecording)
    out_type = namedtuple('SetRecordingStructOutputTuple', ['strRecording'])
    raw_functions.SetRecordingStruct(handle, strRecording)
    return _strRecording


def GetImage(handle, dwSegment, firststImage, LastImage, BufNr):
    raw_functions.GetImage(handle, dwSegment, firststImage, LastImage, BufNr)


def GetSizes(handle):
    _XResAct = WORD()

    XResAct = ctypes.byref(_XResAct)
    _YResAct = WORD()

    YResAct = ctypes.byref(_YResAct)
    _XResMax = WORD()

    XResMax = ctypes.byref(_XResMax)
    _YResMax = WORD()

    YResMax = ctypes.byref(_YResMax)
    out_type = namedtuple('GetSizesOutputTuple', ['XResAct', 'YResAct', 'XResMax', 'YResMax'])
    raw_functions.GetSizes(handle, XResAct, YResAct, XResMax, YResMax)
    return out_type(XResAct=_XResAct.value, YResAct=_YResAct.value, XResMax=_XResMax.value, YResMax=_YResMax.value)


def GetBinning(handle):
    _BinHorz = WORD()

    BinHorz = ctypes.byref(_BinHorz)
    _BinVert = WORD()

    BinVert = ctypes.byref(_BinVert)
    out_type = namedtuple('GetBinningOutputTuple', ['BinHorz', 'BinVert'])
    raw_functions.GetBinning(handle, BinHorz, BinVert)
    return out_type(BinHorz=_BinHorz.value, BinVert=_BinVert.value)


def GetStorageStruct(handle):
    _strStorage = PCO_Storage()

    _strStorage.wSize = ctypes.sizeof(_strStorage)

    strStorage = ctypes.byref(_strStorage)
    out_type = namedtuple('GetStorageStructOutputTuple', ['strStorage'])
    raw_functions.GetStorageStruct(handle, strStorage)
    return _strStorage


def GetCameraDescription(handle):
    _strDescription = PCO_Description()

    _strDescription.wSize = ctypes.sizeof(_strDescription)

    strDescription = ctypes.byref(_strDescription)
    out_type = namedtuple('GetCameraDescriptionOutputTuple', ['strDescription'])
    raw_functions.GetCameraDescription(handle, strDescription)
    return _strDescription


def AddBuffer(handle, firststImage, LastImage, BufNr):
    raw_functions.AddBuffer(handle, firststImage, LastImage, BufNr)


def ClearRamSegment(handle):
    raw_functions.ClearRamSegment(handle)


def GetSensorFormat(handle):
    _Sensor = WORD()

    Sensor = ctypes.byref(_Sensor)
    out_type = namedtuple('GetSensorFormatOutputTuple', ['Sensor'])
    raw_functions.GetSensorFormat(handle, Sensor)
    return _Sensor.value


def ResetSettingsToDefault(handle):
    raw_functions.ResetSettingsToDefault(handle)


def GetStorageMode(handle):
    _StorageMode = WORD()

    StorageMode = ctypes.byref(_StorageMode)
    out_type = namedtuple('GetStorageModeOutputTuple', ['StorageMode'])
    raw_functions.GetStorageMode(handle, StorageMode)
    return _StorageMode.value


def SetUserPowerDownTime(handle, PowerDownTime):
    raw_functions.SetUserPowerDownTime(handle, PowerDownTime)


def SetStorageStruct(handle):
    _strStorage = PCO_Storage()

    _strStorage.wSize = ctypes.sizeof(_strStorage)

    strStorage = ctypes.byref(_strStorage)
    out_type = namedtuple('SetStorageStructOutputTuple', ['strStorage'])
    raw_functions.SetStorageStruct(handle, strStorage)
    return _strStorage


def SetPowerDownMode(handle, PowerDownMode):
    raw_functions.SetPowerDownMode(handle, PowerDownMode)


def GetPixelRate(handle):
    _PixelRate = DWORD()

    PixelRate = ctypes.byref(_PixelRate)
    out_type = namedtuple('GetPixelRateOutputTuple', ['PixelRate'])
    raw_functions.GetPixelRate(handle, PixelRate)
    return _PixelRate.value


def GetAcqEnblSignalStatus(handle):
    _AcquEnableState = WORD()

    AcquEnableState = ctypes.byref(_AcquEnableState)
    out_type = namedtuple('GetAcqEnblSignalStatusOutputTuple', ['AcquEnableState'])
    raw_functions.GetAcqEnblSignalStatus(handle, AcquEnableState)
    return _AcquEnableState.value


def SetIRSensitivity(handle, IR):
    raw_functions.SetIRSensitivity(handle, IR)


def GetImageStruct(handle):
    _strImage = PCO_Image()

    _strImage.wSize = ctypes.sizeof(_strImage)

    strImage = ctypes.byref(_strImage)
    out_type = namedtuple('GetImageStructOutputTuple', ['strImage'])
    raw_functions.GetImageStruct(handle, strImage)
    return _strImage


def SetRecordingState(handle, RecState):
    raw_functions.SetRecordingState(handle, RecState)


def GetGeneral(handle):
    _strGeneral = PCO_General()

    _strGeneral.wSize = ctypes.sizeof(_strGeneral)

    strGeneral = ctypes.byref(_strGeneral)
    out_type = namedtuple('GetGeneralOutputTuple', ['strGeneral'])
    raw_functions.GetGeneral(handle, strGeneral)
    return _strGeneral


def OpenCamera(CamNum):
    _handle = HANDLE()

    handle = ctypes.byref(_handle)
    out_type = namedtuple('OpenCameraOutputTuple', ['handle'])
    raw_functions.OpenCamera(handle, CamNum)
    return _handle.value


def SetTriggerMode(handle, TriggerMode):
    raw_functions.SetTriggerMode(handle, TriggerMode)


def GetCameraType(handle):
    _strCamType = PCO_CameraType()

    _strCamType.wSize = ctypes.sizeof(_strCamType)

    strCamType = ctypes.byref(_strCamType)
    out_type = namedtuple('GetCameraTypeOutputTuple', ['strCamType'])
    raw_functions.GetCameraType(handle, strCamType)
    return _strCamType


def GetDelayExposureTime(handle):
    _Delay = DWORD()

    Delay = ctypes.byref(_Delay)
    _Exposure = DWORD()

    Exposure = ctypes.byref(_Exposure)
    _TimeBaseDelay = WORD()

    TimeBaseDelay = ctypes.byref(_TimeBaseDelay)
    _TimeBaseExposure = WORD()

    TimeBaseExposure = ctypes.byref(_TimeBaseExposure)
    out_type = namedtuple('GetDelayExposureTimeOutputTuple', ['Delay', 'Exposure', 'TimeBaseDelay', 'TimeBaseExposure'])
    raw_functions.GetDelayExposureTime(handle, Delay, Exposure, TimeBaseDelay, TimeBaseExposure)
    return out_type(Delay=_Delay.value, Exposure=_Exposure.value, TimeBaseDelay=_TimeBaseDelay.value, TimeBaseExposure=_TimeBaseExposure.value)


def GetTimingStruct(handle):
    _strTiming = PCO_Timing()

    _strTiming.wSize = ctypes.sizeof(_strTiming)

    strTiming = ctypes.byref(_strTiming)
    out_type = namedtuple('GetTimingStructOutputTuple', ['strTiming'])
    raw_functions.GetTimingStruct(handle, strTiming)
    return _strTiming


def GetSegmentStruct(handle, Segment):
    _strSegment = PCO_Segment()

    _strSegment.wSize = ctypes.sizeof(_strSegment)

    strSegment = ctypes.byref(_strSegment)
    out_type = namedtuple('GetSegmentStructOutputTuple', ['strSegment'])
    raw_functions.GetSegmentStruct(handle, Segment, strSegment)
    return _strSegment


def SetADCOperation(handle, ADCOperation):
    raw_functions.SetADCOperation(handle, ADCOperation)


def SetBinning(handle, BinHorz, BinVert):
    raw_functions.SetBinning(handle, BinHorz, BinVert)


def SetROI(handle, RoiX0, RoiY0, RoiX1, RoiY1):
    raw_functions.SetROI(handle, RoiX0, RoiY0, RoiX1, RoiY1)


def SetSensorStruct(handle):
    _strSensor = PCO_Sensor()

    _strSensor.wSize = ctypes.sizeof(_strSensor)

    strSensor = ctypes.byref(_strSensor)
    out_type = namedtuple('SetSensorStructOutputTuple', ['strSensor'])
    raw_functions.SetSensorStruct(handle, strSensor)
    return _strSensor


def GetIRSensitivity(handle):
    _IR = WORD()

    IR = ctypes.byref(_IR)
    out_type = namedtuple('GetIRSensitivityOutputTuple', ['IR'])
    raw_functions.GetIRSensitivity(handle, IR)
    return _IR.value


def SetDoubleImageMode(handle, DoubleImage):
    raw_functions.SetDoubleImageMode(handle, DoubleImage)


def GetCameraRamSize(handle):
    _RamSize = DWORD()

    RamSize = ctypes.byref(_RamSize)
    _PageSize = WORD()

    PageSize = ctypes.byref(_PageSize)
    out_type = namedtuple('GetCameraRamSizeOutputTuple', ['RamSize', 'PageSize'])
    raw_functions.GetCameraRamSize(handle, RamSize, PageSize)
    return out_type(RamSize=_RamSize.value, PageSize=_PageSize.value)


def SetAcquireMode(handle, AcquMode):
    raw_functions.SetAcquireMode(handle, AcquMode)


def CloseCamera(handle):
    raw_functions.CloseCamera(handle)


def GetTemperature(handle):
    _CCDTemp = SHORT()

    CCDTemp = ctypes.byref(_CCDTemp)
    _CamTemp = SHORT()

    CamTemp = ctypes.byref(_CamTemp)
    _PowTemp = SHORT()

    PowTemp = ctypes.byref(_PowTemp)
    out_type = namedtuple('GetTemperatureOutputTuple', ['CCDTemp', 'CamTemp', 'PowTemp'])
    raw_functions.GetTemperature(handle, CCDTemp, CamTemp, PowTemp)
    return out_type(CCDTemp=_CCDTemp.value, CamTemp=_CamTemp.value, PowTemp=_PowTemp.value)


def SetActiveRamSegment(handle, ActSeg):
    raw_functions.SetActiveRamSegment(handle, ActSeg)


def GetTriggerMode(handle):
    _TriggerMode = WORD()

    TriggerMode = ctypes.byref(_TriggerMode)
    out_type = namedtuple('GetTriggerModeOutputTuple', ['TriggerMode'])
    raw_functions.GetTriggerMode(handle, TriggerMode)
    return _TriggerMode.value


def SetSensorFormat(handle, Sensor):
    raw_functions.SetSensorFormat(handle, Sensor)


def GetRecorderSubmode(handle):
    _RecSubmode = WORD()

    RecSubmode = ctypes.byref(_RecSubmode)
    out_type = namedtuple('GetRecorderSubmodeOutputTuple', ['RecSubmode'])
    raw_functions.GetRecorderSubmode(handle, RecSubmode)
    return _RecSubmode.value


def SetCameraRamSegmentSize(handle):
    _RamSegSize = DWORD()

    RamSegSize = ctypes.byref(_RamSegSize)
    out_type = namedtuple('SetCameraRamSegmentSizeOutputTuple', ['RamSegSize'])
    raw_functions.SetCameraRamSegmentSize(handle, RamSegSize)
    return _RamSegSize.value


def GetSegmentImageSettings(handle, Segment):
    _XRes = WORD()

    XRes = ctypes.byref(_XRes)
    _YRes = WORD()

    YRes = ctypes.byref(_YRes)
    _BinHorz = WORD()

    BinHorz = ctypes.byref(_BinHorz)
    _BinVert = WORD()

    BinVert = ctypes.byref(_BinVert)
    _RoiX0 = WORD()

    RoiX0 = ctypes.byref(_RoiX0)
    _RoiY0 = WORD()

    RoiY0 = ctypes.byref(_RoiY0)
    _RoiX1 = WORD()

    RoiX1 = ctypes.byref(_RoiX1)
    _RoiY1 = WORD()

    RoiY1 = ctypes.byref(_RoiY1)
    out_type = namedtuple('GetSegmentImageSettingsOutputTuple', ['XRes', 'YRes', 'BinHorz', 'BinVert', 'RoiX0', 'RoiY0', 'RoiX1', 'RoiY1'])
    raw_functions.GetSegmentImageSettings(handle, Segment, XRes, YRes, BinHorz, BinVert, RoiX0, RoiY0, RoiX1, RoiY1)
    return out_type(XRes=_XRes.value, YRes=_YRes.value, BinHorz=_BinHorz.value, BinVert=_BinVert.value, RoiX0=_RoiX0.value, RoiY0=_RoiY0.value, RoiX1=_RoiX1.value, RoiY1=_RoiY1.value)


def AddBufferEx(handle, firststImage, LastImage, BufNr, XRes, YRes, BitRes):
    raw_functions.AddBufferEx(handle, firststImage, LastImage, BufNr, XRes, YRes, BitRes)


def CamLinkSetImageParameters(handle, XResAct, YResAct):
    raw_functions.CamLinkSetImageParameters(handle, XResAct, YResAct)


def SetDelayExposureTimeTable(handle, TimeBaseDelay, TimeBaseExposure, Count):
    _Delay = DWORD()

    Delay = ctypes.byref(_Delay)
    _Exposure = DWORD()

    Exposure = ctypes.byref(_Exposure)
    out_type = namedtuple('SetDelayExposureTimeTableOutputTuple', ['Delay', 'Exposure'])
    raw_functions.SetDelayExposureTimeTable(handle, Delay, Exposure, TimeBaseDelay, TimeBaseExposure, Count)
    return out_type(Delay=_Delay.value, Exposure=_Exposure.value)


def CancelImages(handle):
    raw_functions.CancelImages(handle)


def SetRecorderSubmode(handle, RecSubmode):
    raw_functions.SetRecorderSubmode(handle, RecSubmode)


def GetTimestampMode(handle):
    _TimeStampMode = WORD()

    TimeStampMode = ctypes.byref(_TimeStampMode)
    out_type = namedtuple('GetTimestampModeOutputTuple', ['TimeStampMode'])
    raw_functions.GetTimestampMode(handle, TimeStampMode)
    return _TimeStampMode.value


def GetROI(handle):
    _RoiX0 = WORD()

    RoiX0 = ctypes.byref(_RoiX0)
    _RoiY0 = WORD()

    RoiY0 = ctypes.byref(_RoiY0)
    _RoiX1 = WORD()

    RoiX1 = ctypes.byref(_RoiX1)
    _RoiY1 = WORD()

    RoiY1 = ctypes.byref(_RoiY1)
    out_type = namedtuple('GetROIOutputTuple', ['RoiX0', 'RoiY0', 'RoiX1', 'RoiY1'])
    raw_functions.GetROI(handle, RoiX0, RoiY0, RoiX1, RoiY1)
    return out_type(RoiX0=_RoiX0.value, RoiY0=_RoiY0.value, RoiX1=_RoiX1.value, RoiY1=_RoiY1.value)


def SetPixelRate(handle, PixelRate):
    raw_functions.SetPixelRate(handle, PixelRate)


def GetExpTrigSignalStatus(handle):
    _ExpTrgSignal = WORD()

    ExpTrgSignal = ctypes.byref(_ExpTrgSignal)
    out_type = namedtuple('GetExpTrigSignalStatusOutputTuple', ['ExpTrgSignal'])
    raw_functions.GetExpTrigSignalStatus(handle, ExpTrgSignal)
    return _ExpTrgSignal.value


def SetStorageMode(handle, StorageMode):
    raw_functions.SetStorageMode(handle, StorageMode)


def GetDelayExposureTimeTable(handle, Count):
    _Delay = DWORD()

    Delay = ctypes.byref(_Delay)
    _Exposure = DWORD()

    Exposure = ctypes.byref(_Exposure)
    _TimeBaseDelay = WORD()

    TimeBaseDelay = ctypes.byref(_TimeBaseDelay)
    _TimeBaseExposure = WORD()

    TimeBaseExposure = ctypes.byref(_TimeBaseExposure)
    out_type = namedtuple('GetDelayExposureTimeTableOutputTuple', ['Delay', 'Exposure', 'TimeBaseDelay', 'TimeBaseExposure'])
    raw_functions.GetDelayExposureTimeTable(handle, Delay, Exposure, TimeBaseDelay, TimeBaseExposure, Count)
    return out_type(Delay=_Delay.value, Exposure=_Exposure.value, TimeBaseDelay=_TimeBaseDelay.value, TimeBaseExposure=_TimeBaseExposure.value)


def SetCoolingSetpointTemperature(handle, CoolSet):
    raw_functions.SetCoolingSetpointTemperature(handle, CoolSet)


def AllocateBuffer(handle, size,bufNr):
    _BufNr = SHORT(bufNr)

    BufNr = ctypes.byref(_BufNr)
    _Buf = size*WORD
    _Buf = _Buf()
    _Buf = ctypes.cast(_Buf,ctypes.POINTER(WORD))
    Buf = ctypes.pointer(_Buf)

    _Event = HANDLE()

    Event = ctypes.byref(_Event)
    out_type = namedtuple('AllocateBufferOutputTuple', ['BufNr', 'Buf', 'Event'])
    raw_functions.AllocateBuffer(handle, BufNr, size, Buf, Event)
    return out_type(BufNr=_BufNr.value, Buf=_Buf, Event=_Event.value)
    
    
#def AllocateBuffer(handle, size):
#    _BufNr = SHORT()
#
#    BufNr = ctypes.byref(_BufNr)
#    _Buf = WORD()
#
#    Buf = ctypes.byref(_Buf)
#    _Event = HANDLE()
#
#    Event = ctypes.byref(_Event)
#    out_type = namedtuple('AllocateBufferOutputTuple', ['BufNr', 'Buf', 'Event'])
#    raw_functions.AllocateBuffer(handle, BufNr, size, Buf, Event)
#    return out_type(BufNr=_BufNr.value, Buf=_Buf.value, Event=_Event.value)


def SetDelayExposureTime(handle, Delay, Exposure, TimeBaseDelay, TimeBaseExposure):
    raw_functions.SetDelayExposureTime(handle, Delay, Exposure, TimeBaseDelay, TimeBaseExposure)


def GetCoolingSetpointTemperature(handle):
    _CoolSet = SHORT()

    CoolSet = ctypes.byref(_CoolSet)
    out_type = namedtuple('GetCoolingSetpointTemperatureOutputTuple', ['CoolSet'])
    raw_functions.GetCoolingSetpointTemperature(handle, CoolSet)
    return _CoolSet.value


def GetCameraBusyStatus(handle):
    _CameraBusyState = WORD()

    CameraBusyState = ctypes.byref(_CameraBusyState)
    out_type = namedtuple('GetCameraBusyStatusOutputTuple', ['CameraBusyState'])
    raw_functions.GetCameraBusyStatus(handle, CameraBusyState)
    return _CameraBusyState.value


def SetDateTime(handle, Day, Month, Year, Hour, Min, Sec):
    raw_functions.SetDateTime(handle, Day, Month, Year, Hour, Min, Sec)


def GetOffsetMode(handle):
    _OffsetRegulation = WORD()

    OffsetRegulation = ctypes.byref(_OffsetRegulation)
    out_type = namedtuple('GetOffsetModeOutputTuple', ['OffsetRegulation'])
    raw_functions.GetOffsetMode(handle, OffsetRegulation)
    return _OffsetRegulation.value


def GetCameraRamSegmentSize(handle):
    _RamSegSize = DWORD()

    RamSegSize = ctypes.byref(_RamSegSize)
    out_type = namedtuple('GetCameraRamSegmentSizeOutputTuple', ['RamSegSize'])
    raw_functions.GetCameraRamSegmentSize(handle, RamSegSize)
    return _RamSegSize.value


def FreeBuffer(handle, BufNr):
    raw_functions.FreeBuffer(handle, BufNr)


def CheckDeviceAvailability(handle, Num):
    raw_functions.CheckDeviceAvailability(handle, Num)


def GetSensorStruct(handle):
    _strSensor = PCO_Sensor()

    _strSensor.wSize = ctypes.sizeof(_strSensor)

    strSensor = ctypes.byref(_strSensor)
    out_type = namedtuple('GetSensorStructOutputTuple', ['strSensor'])
    raw_functions.GetSensorStruct(handle, strSensor)
    return _strSensor


def ForceTrigger(handle):
    _Triggered = WORD()

    Triggered = ctypes.byref(_Triggered)
    out_type = namedtuple('ForceTriggerOutputTuple', ['Triggered'])
    raw_functions.ForceTrigger(handle, Triggered)
    return _Triggered.value


def GetPowerDownMode(handle):
    _PowerDownMode = WORD()

    PowerDownMode = ctypes.byref(_PowerDownMode)
    out_type = namedtuple('GetPowerDownModeOutputTuple', ['PowerDownMode'])
    raw_functions.GetPowerDownMode(handle, PowerDownMode)
    return _PowerDownMode.value


def SetOffsetMode(handle, OffsetRegulation):
    raw_functions.SetOffsetMode(handle, OffsetRegulation)


def SetConversionFactor(handle, ConvFact):
    raw_functions.SetConversionFactor(handle, ConvFact)


def GetUserPowerDownTime(handle):
    _PowerDownTime = DWORD()

    PowerDownTime = ctypes.byref(_PowerDownTime)
    out_type = namedtuple('GetUserPowerDownTimeOutputTuple', ['PowerDownTime'])
    raw_functions.GetUserPowerDownTime(handle, PowerDownTime)
    return _PowerDownTime.value


def ArmCamera(handle):
    raw_functions.ArmCamera(handle)


def GetADCOperation(handle):
    _ADCOperation = WORD()

    ADCOperation = ctypes.byref(_ADCOperation)
    out_type = namedtuple('GetADCOperationOutputTuple', ['ADCOperation'])
    raw_functions.GetADCOperation(handle, ADCOperation)
    return _ADCOperation.value


