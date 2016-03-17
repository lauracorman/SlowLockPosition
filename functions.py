
from class_definition import Argument, ArgumentPointer, ArgumentDoublePointer, FunctionDef


class GetGeneral(FunctionDef):
    """

    """
    ph = Argument(arg_name="ph", type_name="HANDLE")
    strGeneral = ArgumentPointer(arg_name="strGeneral", type_name="PCO_General")
    _arg_list = [ph, strGeneral]
    _func_name = "GetGeneral"

class GetCameraType(FunctionDef):
    """

    """
    ph = Argument(arg_name="ph", type_name="HANDLE")
    strCamType = ArgumentPointer(arg_name="strCamType", type_name="PCO_CameraType")
    _arg_list = [ph, strCamType]
    _func_name = "GetCameraType"

class GetCameraHealthStatus(FunctionDef):
    """

    """
    ph = Argument(arg_name="ph", type_name="HANDLE")
    dwWarn = ArgumentPointer(arg_name="dwWarn", type_name="DWORD")
    dwErr = ArgumentPointer(arg_name="dwErr", type_name="DWORD")
    dwStatus = ArgumentPointer(arg_name="dwStatus", type_name="DWORD")
    _arg_list = [ph, dwWarn, dwErr, dwStatus]
    _func_name = "GetCameraHealthStatus"

class ResetSettingsToDefault(FunctionDef):
    """

    """
    ph = Argument(arg_name="ph", type_name="HANDLE")
    _arg_list = [ph]
    _func_name = "ResetSettingsToDefault"

class InitiateSelftestProcedure(FunctionDef):
    """

    """
    ph = Argument(arg_name="ph", type_name="HANDLE")
    _arg_list = [ph]
    _func_name = "InitiateSelftestProcedure"

class GetTemperature(FunctionDef):
    """

    """
    ph = Argument(arg_name="ph", type_name="HANDLE")
    sCCDTemp = ArgumentPointer(arg_name="sCCDTemp", type_name="SHORT")
    sCamTemp = ArgumentPointer(arg_name="sCamTemp", type_name="SHORT")
    sPowTemp = ArgumentPointer(arg_name="sPowTemp", type_name="SHORT")
    _arg_list = [ph, sCCDTemp, sCamTemp, sPowTemp]
    _func_name = "GetTemperature"

class GetSensorStruct(FunctionDef):
    """

    """
    ph = Argument(arg_name="ph", type_name="HANDLE")
    strSensor = ArgumentPointer(arg_name="strSensor", type_name="PCO_Sensor")
    _arg_list = [ph, strSensor]
    _func_name = "GetSensorStruct"

class SetSensorStruct(FunctionDef):
    """

    """
    ph = Argument(arg_name="ph", type_name="HANDLE")
    strSensor = ArgumentPointer(arg_name="strSensor", type_name="PCO_Sensor")
    _arg_list = [ph, strSensor]
    _func_name = "SetSensorStruct"

class GetCameraDescription(FunctionDef):
    """

    """
    ph = Argument(arg_name="ph", type_name="HANDLE")
    strDescription = ArgumentPointer(arg_name="strDescription", type_name="PCO_Description")
    _arg_list = [ph, strDescription]
    _func_name = "GetCameraDescription"

class GetSensorFormat(FunctionDef):
    """

    """
    ph = Argument(arg_name="ph", type_name="HANDLE")
    wSensor = ArgumentPointer(arg_name="wSensor", type_name="WORD")
    _arg_list = [ph, wSensor]
    _func_name = "GetSensorFormat"

class SetSensorFormat(FunctionDef):
    """

    """
    ph = Argument(arg_name="ph", type_name="HANDLE")
    wSensor = Argument(arg_name="wSensor", type_name="WORD")
    _arg_list = [ph, wSensor]
    _func_name = "SetSensorFormat"

class GetSizes(FunctionDef):
    """

    """
    ph = Argument(arg_name="ph", type_name="HANDLE")
    wXResAct = ArgumentPointer(arg_name="wXResAct", type_name="WORD")
    wYResAct = ArgumentPointer(arg_name="wYResAct", type_name="WORD")
    wXResMax = ArgumentPointer(arg_name="wXResMax", type_name="WORD")
    wYResMax = ArgumentPointer(arg_name="wYResMax", type_name="WORD")
    _arg_list = [ph, wXResAct, wYResAct, wXResMax, wYResMax]
    _func_name = "GetSizes"

class GetROI(FunctionDef):
    """

    """
    ph = Argument(arg_name="ph", type_name="HANDLE")
    wRoiX0 = ArgumentPointer(arg_name="wRoiX0", type_name="WORD")
    wRoiY0 = ArgumentPointer(arg_name="wRoiY0", type_name="WORD")
    wRoiX1 = ArgumentPointer(arg_name="wRoiX1", type_name="WORD")
    wRoiY1 = ArgumentPointer(arg_name="wRoiY1", type_name="WORD")
    _arg_list = [ph, wRoiX0, wRoiY0, wRoiX1, wRoiY1]
    _func_name = "GetROI"

class SetROI(FunctionDef):
    """

    """
    ph = Argument(arg_name="ph", type_name="HANDLE")
    wRoiX0 = Argument(arg_name="wRoiX0", type_name="WORD")
    wRoiY0 = Argument(arg_name="wRoiY0", type_name="WORD")
    wRoiX1 = Argument(arg_name="wRoiX1", type_name="WORD")
    wRoiY1 = Argument(arg_name="wRoiY1", type_name="WORD")
    _arg_list = [ph, wRoiX0, wRoiY0, wRoiX1, wRoiY1]
    _func_name = "SetROI"

class GetBinning(FunctionDef):
    """

    """
    ph = Argument(arg_name="ph", type_name="HANDLE")
    wBinHorz = ArgumentPointer(arg_name="wBinHorz", type_name="WORD")
    wBinVert = ArgumentPointer(arg_name="wBinVert", type_name="WORD")
    _arg_list = [ph, wBinHorz, wBinVert]
    _func_name = "GetBinning"

class SetBinning(FunctionDef):
    """

    """
    ph = Argument(arg_name="ph", type_name="HANDLE")
    wBinHorz = Argument(arg_name="wBinHorz", type_name="WORD")
    wBinVert = Argument(arg_name="wBinVert", type_name="WORD")
    _arg_list = [ph, wBinHorz, wBinVert]
    _func_name = "SetBinning"

class GetPixelRate(FunctionDef):
    """

    """
    ph = Argument(arg_name="ph", type_name="HANDLE")
    dwPixelRate = ArgumentPointer(arg_name="dwPixelRate", type_name="DWORD")
    _arg_list = [ph, dwPixelRate]
    _func_name = "GetPixelRate"

class SetPixelRate(FunctionDef):
    """

    """
    ph = Argument(arg_name="ph", type_name="HANDLE")
    dwPixelRate = Argument(arg_name="dwPixelRate", type_name="DWORD")
    _arg_list = [ph, dwPixelRate]
    _func_name = "SetPixelRate"

class GetConversionFactor(FunctionDef):
    """

    """
    ph = Argument(arg_name="ph", type_name="HANDLE")
    wConvFact = ArgumentPointer(arg_name="wConvFact", type_name="WORD")
    _arg_list = [ph, wConvFact]
    _func_name = "GetConversionFactor"

class SetConversionFactor(FunctionDef):
    """

    """
    ph = Argument(arg_name="ph", type_name="HANDLE")
    wConvFact = Argument(arg_name="wConvFact", type_name="WORD")
    _arg_list = [ph, wConvFact]
    _func_name = "SetConversionFactor"

class GetDoubleImageMode(FunctionDef):
    """

    """
    ph = Argument(arg_name="ph", type_name="HANDLE")
    wDoubleImage = ArgumentPointer(arg_name="wDoubleImage", type_name="WORD")
    _arg_list = [ph, wDoubleImage]
    _func_name = "GetDoubleImageMode"

class SetDoubleImageMode(FunctionDef):
    """

    """
    ph = Argument(arg_name="ph", type_name="HANDLE")
    wDoubleImage = Argument(arg_name="wDoubleImage", type_name="WORD")
    _arg_list = [ph, wDoubleImage]
    _func_name = "SetDoubleImageMode"

class GetADCOperation(FunctionDef):
    """

    """
    ph = Argument(arg_name="ph", type_name="HANDLE")
    wADCOperation = ArgumentPointer(arg_name="wADCOperation", type_name="WORD")
    _arg_list = [ph, wADCOperation]
    _func_name = "GetADCOperation"

class SetADCOperation(FunctionDef):
    """

    """
    ph = Argument(arg_name="ph", type_name="HANDLE")
    wADCOperation = Argument(arg_name="wADCOperation", type_name="WORD")
    _arg_list = [ph, wADCOperation]
    _func_name = "SetADCOperation"

class GetIRSensitivity(FunctionDef):
    """

    """
    ph = Argument(arg_name="ph", type_name="HANDLE")
    wIR = ArgumentPointer(arg_name="wIR", type_name="WORD")
    _arg_list = [ph, wIR]
    _func_name = "GetIRSensitivity"

class SetIRSensitivity(FunctionDef):
    """

    """
    ph = Argument(arg_name="ph", type_name="HANDLE")
    wIR = Argument(arg_name="wIR", type_name="WORD")
    _arg_list = [ph, wIR]
    _func_name = "SetIRSensitivity"

class GetCoolingSetpointTemperature(FunctionDef):
    """

    """
    ph = Argument(arg_name="ph", type_name="HANDLE")
    sCoolSet = ArgumentPointer(arg_name="sCoolSet", type_name="SHORT")
    _arg_list = [ph, sCoolSet]
    _func_name = "GetCoolingSetpointTemperature"

class SetCoolingSetpointTemperature(FunctionDef):
    """

    """
    ph = Argument(arg_name="ph", type_name="HANDLE")
    sCoolSet = Argument(arg_name="sCoolSet", type_name="SHORT")
    _arg_list = [ph, sCoolSet]
    _func_name = "SetCoolingSetpointTemperature"

class GetOffsetMode(FunctionDef):
    """

    """
    ph = Argument(arg_name="ph", type_name="HANDLE")
    wOffsetRegulation = ArgumentPointer(arg_name="wOffsetRegulation", type_name="WORD")
    _arg_list = [ph, wOffsetRegulation]
    _func_name = "GetOffsetMode"

class SetOffsetMode(FunctionDef):
    """

    """
    ph = Argument(arg_name="ph", type_name="HANDLE")
    wOffsetRegulation = Argument(arg_name="wOffsetRegulation", type_name="WORD")
    _arg_list = [ph, wOffsetRegulation]
    _func_name = "SetOffsetMode"

class GetTimingStruct(FunctionDef):
    """

    """
    ph = Argument(arg_name="ph", type_name="HANDLE")
    strTiming = ArgumentPointer(arg_name="strTiming", type_name="PCO_Timing")
    _arg_list = [ph, strTiming]
    _func_name = "GetTimingStruct"

class SetTimingStruct(FunctionDef):
    """

    """
    ph = Argument(arg_name="ph", type_name="HANDLE")
    strTiming = ArgumentPointer(arg_name="strTiming", type_name="PCO_Timing")
    _arg_list = [ph, strTiming]
    _func_name = "SetTimingStruct"

class GetDelayExposureTime(FunctionDef):
    """

    """
    ph = Argument(arg_name="ph", type_name="HANDLE")
    dwDelay = ArgumentPointer(arg_name="dwDelay", type_name="DWORD")
    dwExposure = ArgumentPointer(arg_name="dwExposure", type_name="DWORD")
    wTimeBaseDelay = ArgumentPointer(arg_name="wTimeBaseDelay", type_name="WORD")
    wTimeBaseExposure = ArgumentPointer(arg_name="wTimeBaseExposure", type_name="WORD")
    _arg_list = [ph, dwDelay, dwExposure, wTimeBaseDelay, wTimeBaseExposure]
    _func_name = "GetDelayExposureTime"

class SetDelayExposureTime(FunctionDef):
    """

    """
    ph = Argument(arg_name="ph", type_name="HANDLE")
    dwDelay = Argument(arg_name="dwDelay", type_name="DWORD")
    dwExposure = Argument(arg_name="dwExposure", type_name="DWORD")
    wTimeBaseDelay = Argument(arg_name="wTimeBaseDelay", type_name="WORD")
    wTimeBaseExposure = Argument(arg_name="wTimeBaseExposure", type_name="WORD")
    _arg_list = [ph, dwDelay, dwExposure, wTimeBaseDelay, wTimeBaseExposure]
    _func_name = "SetDelayExposureTime"

class GetDelayExposureTimeTable(FunctionDef):
    """

    """
    ph = Argument(arg_name="ph", type_name="HANDLE")
    dwDelay = ArgumentPointer(arg_name="dwDelay", type_name="DWORD")
    dwExposure = ArgumentPointer(arg_name="dwExposure", type_name="DWORD")
    wTimeBaseDelay = ArgumentPointer(arg_name="wTimeBaseDelay", type_name="WORD")
    wTimeBaseExposure = ArgumentPointer(arg_name="wTimeBaseExposure", type_name="WORD")
    wCount = Argument(arg_name="wCount", type_name="WORD")
    _arg_list = [ph, dwDelay, dwExposure, wTimeBaseDelay, wTimeBaseExposure, wCount]
    _func_name = "GetDelayExposureTimeTable"

class SetDelayExposureTimeTable(FunctionDef):
    """

    """
    ph = Argument(arg_name="ph", type_name="HANDLE")
    dwDelay = ArgumentPointer(arg_name="dwDelay", type_name="DWORD")
    dwExposure = ArgumentPointer(arg_name="dwExposure", type_name="DWORD")
    wTimeBaseDelay = Argument(arg_name="wTimeBaseDelay", type_name="WORD")
    wTimeBaseExposure = Argument(arg_name="wTimeBaseExposure", type_name="WORD")
    wCount = Argument(arg_name="wCount", type_name="WORD")
    _arg_list = [ph, dwDelay, dwExposure, wTimeBaseDelay, wTimeBaseExposure, wCount]
    _func_name = "SetDelayExposureTimeTable"

class GetTriggerMode(FunctionDef):
    """

    """
    ph = Argument(arg_name="ph", type_name="HANDLE")
    wTriggerMode = ArgumentPointer(arg_name="wTriggerMode", type_name="WORD")
    _arg_list = [ph, wTriggerMode]
    _func_name = "GetTriggerMode"

class SetTriggerMode(FunctionDef):
    """

    """
    ph = Argument(arg_name="ph", type_name="HANDLE")
    wTriggerMode = Argument(arg_name="wTriggerMode", type_name="WORD")
    _arg_list = [ph, wTriggerMode]
    _func_name = "SetTriggerMode"

class ForceTrigger(FunctionDef):
    """

    """
    ph = Argument(arg_name="ph", type_name="HANDLE")
    wTriggered = ArgumentPointer(arg_name="wTriggered", type_name="WORD")
    _arg_list = [ph, wTriggered]
    _func_name = "ForceTrigger"

class GetCameraBusyStatus(FunctionDef):
    """

    """
    ph = Argument(arg_name="ph", type_name="HANDLE")
    wCameraBusyState = ArgumentPointer(arg_name="wCameraBusyState", type_name="WORD")
    _arg_list = [ph, wCameraBusyState]
    _func_name = "GetCameraBusyStatus"

class GetPowerDownMode(FunctionDef):
    """

    """
    ph = Argument(arg_name="ph", type_name="HANDLE")
    wPowerDownMode = ArgumentPointer(arg_name="wPowerDownMode", type_name="WORD")
    _arg_list = [ph, wPowerDownMode]
    _func_name = "GetPowerDownMode"

class SetPowerDownMode(FunctionDef):
    """

    """
    ph = Argument(arg_name="ph", type_name="HANDLE")
    wPowerDownMode = Argument(arg_name="wPowerDownMode", type_name="WORD")
    _arg_list = [ph, wPowerDownMode]
    _func_name = "SetPowerDownMode"

class GetUserPowerDownTime(FunctionDef):
    """

    """
    ph = Argument(arg_name="ph", type_name="HANDLE")
    dwPowerDownTime = ArgumentPointer(arg_name="dwPowerDownTime", type_name="DWORD")
    _arg_list = [ph, dwPowerDownTime]
    _func_name = "GetUserPowerDownTime"

class SetUserPowerDownTime(FunctionDef):
    """

    """
    ph = Argument(arg_name="ph", type_name="HANDLE")
    dwPowerDownTime = Argument(arg_name="dwPowerDownTime", type_name="DWORD")
    _arg_list = [ph, dwPowerDownTime]
    _func_name = "SetUserPowerDownTime"

class GetExpTrigSignalStatus(FunctionDef):
    """

    """
    ph = Argument(arg_name="ph", type_name="HANDLE")
    wExpTrgSignal = ArgumentPointer(arg_name="wExpTrgSignal", type_name="WORD")
    _arg_list = [ph, wExpTrgSignal]
    _func_name = "GetExpTrigSignalStatus"

class GetCOCRuntime(FunctionDef):
    """

    """
    ph = Argument(arg_name="ph", type_name="HANDLE")
    dwTime_s = ArgumentPointer(arg_name="dwTime_s", type_name="DWORD")
    dwTime_us = ArgumentPointer(arg_name="dwTime_us", type_name="DWORD")
    _arg_list = [ph, dwTime_s, dwTime_us]
    _func_name = "GetCOCRuntime"

class GetStorageStruct(FunctionDef):
    """

    """
    ph = Argument(arg_name="ph", type_name="HANDLE")
    strStorage = ArgumentPointer(arg_name="strStorage", type_name="PCO_Storage")
    _arg_list = [ph, strStorage]
    _func_name = "GetStorageStruct"

class SetStorageStruct(FunctionDef):
    """

    """
    ph = Argument(arg_name="ph", type_name="HANDLE")
    strStorage = ArgumentPointer(arg_name="strStorage", type_name="PCO_Storage")
    _arg_list = [ph, strStorage]
    _func_name = "SetStorageStruct"

class GetCameraRamSize(FunctionDef):
    """

    """
    ph = Argument(arg_name="ph", type_name="HANDLE")
    dwRamSize = ArgumentPointer(arg_name="dwRamSize", type_name="DWORD")
    wPageSize = ArgumentPointer(arg_name="wPageSize", type_name="WORD")
    _arg_list = [ph, dwRamSize, wPageSize]
    _func_name = "GetCameraRamSize"

class GetCameraRamSegmentSize(FunctionDef):
    """

    """
    ph = Argument(arg_name="ph", type_name="HANDLE")
    dwRamSegSize = ArgumentPointer(arg_name="dwRamSegSize", type_name="DWORD")
    _arg_list = [ph, dwRamSegSize]
    _func_name = "GetCameraRamSegmentSize"

class SetCameraRamSegmentSize(FunctionDef):
    """

    """
    ph = Argument(arg_name="ph", type_name="HANDLE")
    dwRamSegSize = ArgumentPointer(arg_name="dwRamSegSize", type_name="DWORD")
    _arg_list = [ph, dwRamSegSize]
    _func_name = "SetCameraRamSegmentSize"

class ClearRamSegment(FunctionDef):
    """

    """
    ph = Argument(arg_name="ph", type_name="HANDLE")
    _arg_list = [ph]
    _func_name = "ClearRamSegment"

class GetActiveRamSegment(FunctionDef):
    """

    """
    ph = Argument(arg_name="ph", type_name="HANDLE")
    wActSeg = ArgumentPointer(arg_name="wActSeg", type_name="WORD")
    _arg_list = [ph, wActSeg]
    _func_name = "GetActiveRamSegment"

class SetActiveRamSegment(FunctionDef):
    """

    """
    ph = Argument(arg_name="ph", type_name="HANDLE")
    wActSeg = Argument(arg_name="wActSeg", type_name="WORD")
    _arg_list = [ph, wActSeg]
    _func_name = "SetActiveRamSegment"

class GetRecordingStruct(FunctionDef):
    """

    """
    ph = Argument(arg_name="ph", type_name="HANDLE")
    strRecording = ArgumentPointer(arg_name="strRecording", type_name="PCO_Recording")
    _arg_list = [ph, strRecording]
    _func_name = "GetRecordingStruct"

class SetRecordingStruct(FunctionDef):
    """

    """
    ph = Argument(arg_name="ph", type_name="HANDLE")
    strRecording = ArgumentPointer(arg_name="strRecording", type_name="PCO_Recording")
    _arg_list = [ph, strRecording]
    _func_name = "SetRecordingStruct"

class GetStorageMode(FunctionDef):
    """

    """
    ph = Argument(arg_name="ph", type_name="HANDLE")
    wStorageMode = ArgumentPointer(arg_name="wStorageMode", type_name="WORD")
    _arg_list = [ph, wStorageMode]
    _func_name = "GetStorageMode"

class SetStorageMode(FunctionDef):
    """

    """
    ph = Argument(arg_name="ph", type_name="HANDLE")
    wStorageMode = Argument(arg_name="wStorageMode", type_name="WORD")
    _arg_list = [ph, wStorageMode]
    _func_name = "SetStorageMode"

class GetRecorderSubmode(FunctionDef):
    """

    """
    ph = Argument(arg_name="ph", type_name="HANDLE")
    wRecSubmode = ArgumentPointer(arg_name="wRecSubmode", type_name="WORD")
    _arg_list = [ph, wRecSubmode]
    _func_name = "GetRecorderSubmode"

class SetRecorderSubmode(FunctionDef):
    """

    """
    ph = Argument(arg_name="ph", type_name="HANDLE")
    wRecSubmode = Argument(arg_name="wRecSubmode", type_name="WORD")
    _arg_list = [ph, wRecSubmode]
    _func_name = "SetRecorderSubmode"

class GetRecordingState(FunctionDef):
    """

    """
    ph = Argument(arg_name="ph", type_name="HANDLE")
    wRecState = ArgumentPointer(arg_name="wRecState", type_name="WORD")
    _arg_list = [ph, wRecState]
    _func_name = "GetRecordingState"

class SetRecordingState(FunctionDef):
    """

    """
    ph = Argument(arg_name="ph", type_name="HANDLE")
    wRecState = Argument(arg_name="wRecState", type_name="WORD")
    _arg_list = [ph, wRecState]
    _func_name = "SetRecordingState"

class ArmCamera(FunctionDef):
    """

    """
    ph = Argument(arg_name="ph", type_name="HANDLE")
    _arg_list = [ph]
    _func_name = "ArmCamera"

class GetAcquireMode(FunctionDef):
    """

    """
    ph = Argument(arg_name="ph", type_name="HANDLE")
    wAcquMode = ArgumentPointer(arg_name="wAcquMode", type_name="WORD")
    _arg_list = [ph, wAcquMode]
    _func_name = "GetAcquireMode"

class SetAcquireMode(FunctionDef):
    """

    """
    ph = Argument(arg_name="ph", type_name="HANDLE")
    wAcquMode = Argument(arg_name="wAcquMode", type_name="WORD")
    _arg_list = [ph, wAcquMode]
    _func_name = "SetAcquireMode"

class GetAcqEnblSignalStatus(FunctionDef):
    """

    """
    ph = Argument(arg_name="ph", type_name="HANDLE")
    wAcquEnableState = ArgumentPointer(arg_name="wAcquEnableState", type_name="WORD")
    _arg_list = [ph, wAcquEnableState]
    _func_name = "GetAcqEnblSignalStatus"

class SetDateTime(FunctionDef):
    """

    """
    ph = Argument(arg_name="ph", type_name="HANDLE")
    ucDay = Argument(arg_name="ucDay", type_name="BYTE")
    ucMonth = Argument(arg_name="ucMonth", type_name="BYTE")
    wYear = Argument(arg_name="wYear", type_name="WORD")
    wHour = Argument(arg_name="wHour", type_name="WORD")
    ucMin = Argument(arg_name="ucMin", type_name="BYTE")
    ucSec = Argument(arg_name="ucSec", type_name="BYTE")
    _arg_list = [ph, ucDay, ucMonth, wYear, wHour, ucMin, ucSec]
    _func_name = "SetDateTime"

class GetTimestampMode(FunctionDef):
    """

    """
    ph = Argument(arg_name="ph", type_name="HANDLE")
    wTimeStampMode = ArgumentPointer(arg_name="wTimeStampMode", type_name="WORD")
    _arg_list = [ph, wTimeStampMode]
    _func_name = "GetTimestampMode"

class SetTimestampMode(FunctionDef):
    """

    """
    ph = Argument(arg_name="ph", type_name="HANDLE")
    wTimeStampMode = Argument(arg_name="wTimeStampMode", type_name="WORD")
    _arg_list = [ph, wTimeStampMode]
    _func_name = "SetTimestampMode"

class GetImageStruct(FunctionDef):
    """

    """
    ph = Argument(arg_name="ph", type_name="HANDLE")
    strImage = ArgumentPointer(arg_name="strImage", type_name="PCO_Image")
    _arg_list = [ph, strImage]
    _func_name = "GetImageStruct"

class GetSegmentStruct(FunctionDef):
    """

    """
    ph = Argument(arg_name="ph", type_name="HANDLE")
    wSegment = Argument(arg_name="wSegment", type_name="WORD")
    strSegment = ArgumentPointer(arg_name="strSegment", type_name="PCO_Segment")
    _arg_list = [ph, wSegment, strSegment]
    _func_name = "GetSegmentStruct"

class GetSegmentImageSettings(FunctionDef):
    """

    """
    ph = Argument(arg_name="ph", type_name="HANDLE")
    wSegment = Argument(arg_name="wSegment", type_name="WORD")
    wXRes = ArgumentPointer(arg_name="wXRes", type_name="WORD")
    wYRes = ArgumentPointer(arg_name="wYRes", type_name="WORD")
    wBinHorz = ArgumentPointer(arg_name="wBinHorz", type_name="WORD")
    wBinVert = ArgumentPointer(arg_name="wBinVert", type_name="WORD")
    wRoiX0 = ArgumentPointer(arg_name="wRoiX0", type_name="WORD")
    wRoiY0 = ArgumentPointer(arg_name="wRoiY0", type_name="WORD")
    wRoiX1 = ArgumentPointer(arg_name="wRoiX1", type_name="WORD")
    wRoiY1 = ArgumentPointer(arg_name="wRoiY1", type_name="WORD")
    _arg_list = [ph, wSegment, wXRes, wYRes, wBinHorz, wBinVert, wRoiX0, wRoiY0, wRoiX1, wRoiY1]
    _func_name = "GetSegmentImageSettings"

class GetNumberOfImagesInSegment(FunctionDef):
    """

    """
    ph = Argument(arg_name="ph", type_name="HANDLE")
    wSegment = Argument(arg_name="wSegment", type_name="WORD")
    dwValidImageCnt = ArgumentPointer(arg_name="dwValidImageCnt", type_name="DWORD")
    dwMaxImageCnt = ArgumentPointer(arg_name="dwMaxImageCnt", type_name="DWORD")
    _arg_list = [ph, wSegment, dwValidImageCnt, dwMaxImageCnt]
    _func_name = "GetNumberOfImagesInSegment"

class OpenCamera(FunctionDef):
    """

    """
    ph = ArgumentPointer(arg_name="ph", type_name="HANDLE")
    wCamNum = Argument(arg_name="wCamNum", type_name="WORD")
    _arg_list = [ph, wCamNum]
    _func_name = "OpenCamera"

class CloseCamera(FunctionDef):
    """

    """
    ph = Argument(arg_name="ph", type_name="HANDLE")
    _arg_list = [ph]
    _func_name = "CloseCamera"

class AllocateBuffer(FunctionDef):
    """

    """
    ph = Argument(arg_name="ph", type_name="HANDLE")
    sBufNr = ArgumentPointer(arg_name="sBufNr", type_name="SHORT")
    size = Argument(arg_name="size", type_name="DWORD")
    wBuf = ArgumentDoublePointer(arg_name="wBuf", type_name="WORD")
    hEvent = ArgumentPointer(arg_name="hEvent", type_name="HANDLE")
    _arg_list = [ph, sBufNr, size, wBuf, hEvent]
    _func_name = "AllocateBuffer"

class FreeBuffer(FunctionDef):
    """

    """
    ph = Argument(arg_name="ph", type_name="HANDLE")
    sBufNr = Argument(arg_name="sBufNr", type_name="SHORT")
    _arg_list = [ph, sBufNr]
    _func_name = "FreeBuffer"

class AddBuffer(FunctionDef):
    """

    """
    ph = Argument(arg_name="ph", type_name="HANDLE")
    dw1stImage = Argument(arg_name="dw1stImage", type_name="DWORD")
    dwLastImage = Argument(arg_name="dwLastImage", type_name="DWORD")
    sBufNr = Argument(arg_name="sBufNr", type_name="SHORT")
    _arg_list = [ph, dw1stImage, dwLastImage, sBufNr]
    _func_name = "AddBuffer"

class AddBufferEx(FunctionDef):
    """

    """
    ph = Argument(arg_name="ph", type_name="HANDLE")
    dw1stImage = Argument(arg_name="dw1stImage", type_name="DWORD")
    dwLastImage = Argument(arg_name="dwLastImage", type_name="DWORD")
    sBufNr = Argument(arg_name="sBufNr", type_name="SHORT")
    wXRes = Argument(arg_name="wXRes", type_name="WORD")
    wYRes = Argument(arg_name="wYRes", type_name="WORD")
    wBitRes = Argument(arg_name="wBitRes", type_name="WORD")
    _arg_list = [ph, dw1stImage, dwLastImage, sBufNr, wXRes, wYRes, wBitRes]
    _func_name = "AddBufferEx"

class GetBufferStatus(FunctionDef):
    """

    """
    ph = Argument(arg_name="ph", type_name="HANDLE")
    sBufNr = Argument(arg_name="sBufNr", type_name="SHORT")
    dwStatusDll = ArgumentPointer(arg_name="dwStatusDll", type_name="DWORD")
    dwStatusDrv = ArgumentPointer(arg_name="dwStatusDrv", type_name="DWORD")
    _arg_list = [ph, sBufNr, dwStatusDll, dwStatusDrv]
    _func_name = "GetBufferStatus"

class GetImage(FunctionDef):
    """

    """
    ph = Argument(arg_name="ph", type_name="HANDLE")
    dwSegment = Argument(arg_name="dwSegment", type_name="WORD")
    dw1stImage = Argument(arg_name="dw1stImage", type_name="DWORD")
    dwLastImage = Argument(arg_name="dwLastImage", type_name="DWORD")
    sBufNr = Argument(arg_name="sBufNr", type_name="SHORT")
    _arg_list = [ph, dwSegment, dw1stImage, dwLastImage, sBufNr]
    _func_name = "GetImage"

class GetPendingBuffer(FunctionDef):
    """

    """
    ph = Argument(arg_name="ph", type_name="HANDLE")
    count = ArgumentPointer(arg_name="count", type_name="int")
    _arg_list = [ph, count]
    _func_name = "GetPendingBuffer"

class CancelImages(FunctionDef):
    """

    """
    ph = Argument(arg_name="ph", type_name="HANDLE")
    _arg_list = [ph]
    _func_name = "CancelImages"

class CheckDeviceAvailability(FunctionDef):
    """

    """
    ph = Argument(arg_name="ph", type_name="HANDLE")
    wNum = Argument(arg_name="wNum", type_name="WORD")
    _arg_list = [ph, wNum]
    _func_name = "CheckDeviceAvailability"

class CamLinkSetImageParameters(FunctionDef):
    """

    """
    ph = Argument(arg_name="ph", type_name="HANDLE")
    wXResAct = Argument(arg_name="wXResAct", type_name="WORD")
    wYResAct = Argument(arg_name="wYResAct", type_name="WORD")
    _arg_list = [ph, wXResAct, wYResAct]
    _func_name = "CamLinkSetImageParameters"

_all_functions = {"GetGeneral":GetGeneral, "GetCameraType":GetCameraType, "GetCameraHealthStatus":GetCameraHealthStatus, "ResetSettingsToDefault":ResetSettingsToDefault, "InitiateSelftestProcedure":InitiateSelftestProcedure, "GetTemperature":GetTemperature, "GetSensorStruct":GetSensorStruct, "SetSensorStruct":SetSensorStruct, "GetCameraDescription":GetCameraDescription, "GetSensorFormat":GetSensorFormat, "SetSensorFormat":SetSensorFormat, "GetSizes":GetSizes, "GetROI":GetROI, "SetROI":SetROI, "GetBinning":GetBinning, "SetBinning":SetBinning, "GetPixelRate":GetPixelRate, "SetPixelRate":SetPixelRate, "GetConversionFactor":GetConversionFactor, "SetConversionFactor":SetConversionFactor, "GetDoubleImageMode":GetDoubleImageMode, "SetDoubleImageMode":SetDoubleImageMode, "GetADCOperation":GetADCOperation, "SetADCOperation":SetADCOperation, "GetIRSensitivity":GetIRSensitivity, "SetIRSensitivity":SetIRSensitivity, "GetCoolingSetpointTemperature":GetCoolingSetpointTemperature, "SetCoolingSetpointTemperature":SetCoolingSetpointTemperature, "GetOffsetMode":GetOffsetMode, "SetOffsetMode":SetOffsetMode, "GetTimingStruct":GetTimingStruct, "SetTimingStruct":SetTimingStruct, "GetDelayExposureTime":GetDelayExposureTime, "SetDelayExposureTime":SetDelayExposureTime, "GetDelayExposureTimeTable":GetDelayExposureTimeTable, "SetDelayExposureTimeTable":SetDelayExposureTimeTable, "GetTriggerMode":GetTriggerMode, "SetTriggerMode":SetTriggerMode, "ForceTrigger":ForceTrigger, "GetCameraBusyStatus":GetCameraBusyStatus, "GetPowerDownMode":GetPowerDownMode, "SetPowerDownMode":SetPowerDownMode, "GetUserPowerDownTime":GetUserPowerDownTime, "SetUserPowerDownTime":SetUserPowerDownTime, "GetExpTrigSignalStatus":GetExpTrigSignalStatus, "GetCOCRuntime":GetCOCRuntime, "GetStorageStruct":GetStorageStruct, "SetStorageStruct":SetStorageStruct, "GetCameraRamSize":GetCameraRamSize, "GetCameraRamSegmentSize":GetCameraRamSegmentSize, "SetCameraRamSegmentSize":SetCameraRamSegmentSize, "ClearRamSegment":ClearRamSegment, "GetActiveRamSegment":GetActiveRamSegment, "SetActiveRamSegment":SetActiveRamSegment, "GetRecordingStruct":GetRecordingStruct, "SetRecordingStruct":SetRecordingStruct, "GetStorageMode":GetStorageMode, "SetStorageMode":SetStorageMode, "GetRecorderSubmode":GetRecorderSubmode, "SetRecorderSubmode":SetRecorderSubmode, "GetRecordingState":GetRecordingState, "SetRecordingState":SetRecordingState, "ArmCamera":ArmCamera, "GetAcquireMode":GetAcquireMode, "SetAcquireMode":SetAcquireMode, "GetAcqEnblSignalStatus":GetAcqEnblSignalStatus, "SetDateTime":SetDateTime, "GetTimestampMode":GetTimestampMode, "SetTimestampMode":SetTimestampMode, "GetImageStruct":GetImageStruct, "GetSegmentStruct":GetSegmentStruct, "GetSegmentImageSettings":GetSegmentImageSettings, "GetNumberOfImagesInSegment":GetNumberOfImagesInSegment, "OpenCamera":OpenCamera, "CloseCamera":CloseCamera, "AllocateBuffer":AllocateBuffer, "FreeBuffer":FreeBuffer, "AddBuffer":AddBuffer, "AddBufferEx":AddBufferEx, "GetBufferStatus":GetBufferStatus, "GetImage":GetImage, "GetPendingBuffer":GetPendingBuffer, "CancelImages":CancelImages, "CheckDeviceAvailability":CheckDeviceAvailability, "CamLinkSetImageParameters":CamLinkSetImageParameters}