import functions
from error import catch_error
import ctypes

_all_functions = {}
SC2Lib = ctypes.windll.LoadLibrary("SC2_Cam.dll")
for key,val in functions._all_functions.iteritems():
    cfunc = getattr(SC2Lib, "PCO_"+key)
    cfunc.argtypes = val.argtypes
    func = catch_error(cfunc, val, val.__doc__)







val=functions._all_functions.get("GetRecordingStruct")
cfunc = getattr(SC2Lib, "PCO_GetRecordingStruct")
cfunc.argtypes = val.argtypes
func = catch_error(cfunc, val, val.__doc__)
_all_functions["GetRecordingStruct"] = func
GetRecordingStruct = func


val=functions._all_functions.get("SetTimestampMode")
cfunc = getattr(SC2Lib, "PCO_SetTimestampMode")
cfunc.argtypes = val.argtypes
func = catch_error(cfunc, val, val.__doc__)
_all_functions["SetTimestampMode"] = func
SetTimestampMode = func


val=functions._all_functions.get("GetCOCRuntime")
cfunc = getattr(SC2Lib, "PCO_GetCOCRuntime")
cfunc.argtypes = val.argtypes
func = catch_error(cfunc, val, val.__doc__)
_all_functions["GetCOCRuntime"] = func
GetCOCRuntime = func


val=functions._all_functions.get("GetActiveRamSegment")
cfunc = getattr(SC2Lib, "PCO_GetActiveRamSegment")
cfunc.argtypes = val.argtypes
func = catch_error(cfunc, val, val.__doc__)
_all_functions["GetActiveRamSegment"] = func
GetActiveRamSegment = func


val=functions._all_functions.get("GetCameraHealthStatus")
cfunc = getattr(SC2Lib, "PCO_GetCameraHealthStatus")
cfunc.argtypes = val.argtypes
func = catch_error(cfunc, val, val.__doc__)
_all_functions["GetCameraHealthStatus"] = func
GetCameraHealthStatus = func


val=functions._all_functions.get("GetRecordingState")
cfunc = getattr(SC2Lib, "PCO_GetRecordingState")
cfunc.argtypes = val.argtypes
func = catch_error(cfunc, val, val.__doc__)
_all_functions["GetRecordingState"] = func
GetRecordingState = func


val=functions._all_functions.get("SetTimingStruct")
cfunc = getattr(SC2Lib, "PCO_SetTimingStruct")
cfunc.argtypes = val.argtypes
func = catch_error(cfunc, val, val.__doc__)
_all_functions["SetTimingStruct"] = func
SetTimingStruct = func


val=functions._all_functions.get("GetDoubleImageMode")
cfunc = getattr(SC2Lib, "PCO_GetDoubleImageMode")
cfunc.argtypes = val.argtypes
func = catch_error(cfunc, val, val.__doc__)
_all_functions["GetDoubleImageMode"] = func
GetDoubleImageMode = func


val=functions._all_functions.get("GetPendingBuffer")
cfunc = getattr(SC2Lib, "PCO_GetPendingBuffer")
cfunc.argtypes = val.argtypes
func = catch_error(cfunc, val, val.__doc__)
_all_functions["GetPendingBuffer"] = func
GetPendingBuffer = func


val=functions._all_functions.get("GetNumberOfImagesInSegment")
cfunc = getattr(SC2Lib, "PCO_GetNumberOfImagesInSegment")
cfunc.argtypes = val.argtypes
func = catch_error(cfunc, val, val.__doc__)
_all_functions["GetNumberOfImagesInSegment"] = func
GetNumberOfImagesInSegment = func


val=functions._all_functions.get("GetAcquireMode")
cfunc = getattr(SC2Lib, "PCO_GetAcquireMode")
cfunc.argtypes = val.argtypes
func = catch_error(cfunc, val, val.__doc__)
_all_functions["GetAcquireMode"] = func
GetAcquireMode = func


val=functions._all_functions.get("InitiateSelftestProcedure")
cfunc = getattr(SC2Lib, "PCO_InitiateSelftestProcedure")
cfunc.argtypes = val.argtypes
func = catch_error(cfunc, val, val.__doc__)
_all_functions["InitiateSelftestProcedure"] = func
InitiateSelftestProcedure = func


val=functions._all_functions.get("GetConversionFactor")
cfunc = getattr(SC2Lib, "PCO_GetConversionFactor")
cfunc.argtypes = val.argtypes
func = catch_error(cfunc, val, val.__doc__)
_all_functions["GetConversionFactor"] = func
GetConversionFactor = func


val=functions._all_functions.get("GetBufferStatus")
cfunc = getattr(SC2Lib, "PCO_GetBufferStatus")
cfunc.argtypes = val.argtypes
func = catch_error(cfunc, val, val.__doc__)
_all_functions["GetBufferStatus"] = func
GetBufferStatus = func


val=functions._all_functions.get("SetRecordingStruct")
cfunc = getattr(SC2Lib, "PCO_SetRecordingStruct")
cfunc.argtypes = val.argtypes
func = catch_error(cfunc, val, val.__doc__)
_all_functions["SetRecordingStruct"] = func
SetRecordingStruct = func


val=functions._all_functions.get("GetImage")
cfunc = getattr(SC2Lib, "PCO_GetImage")
cfunc.argtypes = val.argtypes
func = catch_error(cfunc, val, val.__doc__)
_all_functions["GetImage"] = func
GetImage = func


val=functions._all_functions.get("GetSizes")
cfunc = getattr(SC2Lib, "PCO_GetSizes")
cfunc.argtypes = val.argtypes
func = catch_error(cfunc, val, val.__doc__)
_all_functions["GetSizes"] = func
GetSizes = func


val=functions._all_functions.get("GetBinning")
cfunc = getattr(SC2Lib, "PCO_GetBinning")
cfunc.argtypes = val.argtypes
func = catch_error(cfunc, val, val.__doc__)
_all_functions["GetBinning"] = func
GetBinning = func


val=functions._all_functions.get("GetStorageStruct")
cfunc = getattr(SC2Lib, "PCO_GetStorageStruct")
cfunc.argtypes = val.argtypes
func = catch_error(cfunc, val, val.__doc__)
_all_functions["GetStorageStruct"] = func
GetStorageStruct = func


val=functions._all_functions.get("GetCameraDescription")
cfunc = getattr(SC2Lib, "PCO_GetCameraDescription")
cfunc.argtypes = val.argtypes
func = catch_error(cfunc, val, val.__doc__)
_all_functions["GetCameraDescription"] = func
GetCameraDescription = func


val=functions._all_functions.get("AddBuffer")
cfunc = getattr(SC2Lib, "PCO_AddBuffer")
cfunc.argtypes = val.argtypes
func = catch_error(cfunc, val, val.__doc__)
_all_functions["AddBuffer"] = func
AddBuffer = func


val=functions._all_functions.get("ClearRamSegment")
cfunc = getattr(SC2Lib, "PCO_ClearRamSegment")
cfunc.argtypes = val.argtypes
func = catch_error(cfunc, val, val.__doc__)
_all_functions["ClearRamSegment"] = func
ClearRamSegment = func


val=functions._all_functions.get("GetSensorFormat")
cfunc = getattr(SC2Lib, "PCO_GetSensorFormat")
cfunc.argtypes = val.argtypes
func = catch_error(cfunc, val, val.__doc__)
_all_functions["GetSensorFormat"] = func
GetSensorFormat = func


val=functions._all_functions.get("ResetSettingsToDefault")
cfunc = getattr(SC2Lib, "PCO_ResetSettingsToDefault")
cfunc.argtypes = val.argtypes
func = catch_error(cfunc, val, val.__doc__)
_all_functions["ResetSettingsToDefault"] = func
ResetSettingsToDefault = func


val=functions._all_functions.get("GetStorageMode")
cfunc = getattr(SC2Lib, "PCO_GetStorageMode")
cfunc.argtypes = val.argtypes
func = catch_error(cfunc, val, val.__doc__)
_all_functions["GetStorageMode"] = func
GetStorageMode = func


val=functions._all_functions.get("SetUserPowerDownTime")
cfunc = getattr(SC2Lib, "PCO_SetUserPowerDownTime")
cfunc.argtypes = val.argtypes
func = catch_error(cfunc, val, val.__doc__)
_all_functions["SetUserPowerDownTime"] = func
SetUserPowerDownTime = func


val=functions._all_functions.get("SetStorageStruct")
cfunc = getattr(SC2Lib, "PCO_SetStorageStruct")
cfunc.argtypes = val.argtypes
func = catch_error(cfunc, val, val.__doc__)
_all_functions["SetStorageStruct"] = func
SetStorageStruct = func


val=functions._all_functions.get("SetPowerDownMode")
cfunc = getattr(SC2Lib, "PCO_SetPowerDownMode")
cfunc.argtypes = val.argtypes
func = catch_error(cfunc, val, val.__doc__)
_all_functions["SetPowerDownMode"] = func
SetPowerDownMode = func


val=functions._all_functions.get("GetPixelRate")
cfunc = getattr(SC2Lib, "PCO_GetPixelRate")
cfunc.argtypes = val.argtypes
func = catch_error(cfunc, val, val.__doc__)
_all_functions["GetPixelRate"] = func
GetPixelRate = func


val=functions._all_functions.get("GetAcqEnblSignalStatus")
cfunc = getattr(SC2Lib, "PCO_GetAcqEnblSignalStatus")
cfunc.argtypes = val.argtypes
func = catch_error(cfunc, val, val.__doc__)
_all_functions["GetAcqEnblSignalStatus"] = func
GetAcqEnblSignalStatus = func


val=functions._all_functions.get("SetIRSensitivity")
cfunc = getattr(SC2Lib, "PCO_SetIRSensitivity")
cfunc.argtypes = val.argtypes
func = catch_error(cfunc, val, val.__doc__)
_all_functions["SetIRSensitivity"] = func
SetIRSensitivity = func


val=functions._all_functions.get("GetImageStruct")
cfunc = getattr(SC2Lib, "PCO_GetImageStruct")
cfunc.argtypes = val.argtypes
func = catch_error(cfunc, val, val.__doc__)
_all_functions["GetImageStruct"] = func
GetImageStruct = func


val=functions._all_functions.get("SetRecordingState")
cfunc = getattr(SC2Lib, "PCO_SetRecordingState")
cfunc.argtypes = val.argtypes
func = catch_error(cfunc, val, val.__doc__)
_all_functions["SetRecordingState"] = func
SetRecordingState = func


val=functions._all_functions.get("GetGeneral")
cfunc = getattr(SC2Lib, "PCO_GetGeneral")
cfunc.argtypes = val.argtypes
func = catch_error(cfunc, val, val.__doc__)
_all_functions["GetGeneral"] = func
GetGeneral = func


val=functions._all_functions.get("OpenCamera")
cfunc = getattr(SC2Lib, "PCO_OpenCamera")
cfunc.argtypes = val.argtypes
func = catch_error(cfunc, val, val.__doc__)
_all_functions["OpenCamera"] = func
OpenCamera = func


val=functions._all_functions.get("SetTriggerMode")
cfunc = getattr(SC2Lib, "PCO_SetTriggerMode")
cfunc.argtypes = val.argtypes
func = catch_error(cfunc, val, val.__doc__)
_all_functions["SetTriggerMode"] = func
SetTriggerMode = func


val=functions._all_functions.get("GetCameraType")
cfunc = getattr(SC2Lib, "PCO_GetCameraType")
cfunc.argtypes = val.argtypes
func = catch_error(cfunc, val, val.__doc__)
_all_functions["GetCameraType"] = func
GetCameraType = func


val=functions._all_functions.get("GetDelayExposureTime")
cfunc = getattr(SC2Lib, "PCO_GetDelayExposureTime")
cfunc.argtypes = val.argtypes
func = catch_error(cfunc, val, val.__doc__)
_all_functions["GetDelayExposureTime"] = func
GetDelayExposureTime = func


val=functions._all_functions.get("GetTimingStruct")
cfunc = getattr(SC2Lib, "PCO_GetTimingStruct")
cfunc.argtypes = val.argtypes
func = catch_error(cfunc, val, val.__doc__)
_all_functions["GetTimingStruct"] = func
GetTimingStruct = func


val=functions._all_functions.get("GetSegmentStruct")
cfunc = getattr(SC2Lib, "PCO_GetSegmentStruct")
cfunc.argtypes = val.argtypes
func = catch_error(cfunc, val, val.__doc__)
_all_functions["GetSegmentStruct"] = func
GetSegmentStruct = func


val=functions._all_functions.get("SetADCOperation")
cfunc = getattr(SC2Lib, "PCO_SetADCOperation")
cfunc.argtypes = val.argtypes
func = catch_error(cfunc, val, val.__doc__)
_all_functions["SetADCOperation"] = func
SetADCOperation = func


val=functions._all_functions.get("SetBinning")
cfunc = getattr(SC2Lib, "PCO_SetBinning")
cfunc.argtypes = val.argtypes
func = catch_error(cfunc, val, val.__doc__)
_all_functions["SetBinning"] = func
SetBinning = func


val=functions._all_functions.get("SetROI")
cfunc = getattr(SC2Lib, "PCO_SetROI")
cfunc.argtypes = val.argtypes
func = catch_error(cfunc, val, val.__doc__)
_all_functions["SetROI"] = func
SetROI = func


val=functions._all_functions.get("SetSensorStruct")
cfunc = getattr(SC2Lib, "PCO_SetSensorStruct")
cfunc.argtypes = val.argtypes
func = catch_error(cfunc, val, val.__doc__)
_all_functions["SetSensorStruct"] = func
SetSensorStruct = func


val=functions._all_functions.get("GetIRSensitivity")
cfunc = getattr(SC2Lib, "PCO_GetIRSensitivity")
cfunc.argtypes = val.argtypes
func = catch_error(cfunc, val, val.__doc__)
_all_functions["GetIRSensitivity"] = func
GetIRSensitivity = func


val=functions._all_functions.get("SetDoubleImageMode")
cfunc = getattr(SC2Lib, "PCO_SetDoubleImageMode")
cfunc.argtypes = val.argtypes
func = catch_error(cfunc, val, val.__doc__)
_all_functions["SetDoubleImageMode"] = func
SetDoubleImageMode = func


val=functions._all_functions.get("GetCameraRamSize")
cfunc = getattr(SC2Lib, "PCO_GetCameraRamSize")
cfunc.argtypes = val.argtypes
func = catch_error(cfunc, val, val.__doc__)
_all_functions["GetCameraRamSize"] = func
GetCameraRamSize = func


val=functions._all_functions.get("SetAcquireMode")
cfunc = getattr(SC2Lib, "PCO_SetAcquireMode")
cfunc.argtypes = val.argtypes
func = catch_error(cfunc, val, val.__doc__)
_all_functions["SetAcquireMode"] = func
SetAcquireMode = func


val=functions._all_functions.get("CloseCamera")
cfunc = getattr(SC2Lib, "PCO_CloseCamera")
cfunc.argtypes = val.argtypes
func = catch_error(cfunc, val, val.__doc__)
_all_functions["CloseCamera"] = func
CloseCamera = func


val=functions._all_functions.get("GetTemperature")
cfunc = getattr(SC2Lib, "PCO_GetTemperature")
cfunc.argtypes = val.argtypes
func = catch_error(cfunc, val, val.__doc__)
_all_functions["GetTemperature"] = func
GetTemperature = func


val=functions._all_functions.get("SetActiveRamSegment")
cfunc = getattr(SC2Lib, "PCO_SetActiveRamSegment")
cfunc.argtypes = val.argtypes
func = catch_error(cfunc, val, val.__doc__)
_all_functions["SetActiveRamSegment"] = func
SetActiveRamSegment = func


val=functions._all_functions.get("GetTriggerMode")
cfunc = getattr(SC2Lib, "PCO_GetTriggerMode")
cfunc.argtypes = val.argtypes
func = catch_error(cfunc, val, val.__doc__)
_all_functions["GetTriggerMode"] = func
GetTriggerMode = func


val=functions._all_functions.get("SetSensorFormat")
cfunc = getattr(SC2Lib, "PCO_SetSensorFormat")
cfunc.argtypes = val.argtypes
func = catch_error(cfunc, val, val.__doc__)
_all_functions["SetSensorFormat"] = func
SetSensorFormat = func


val=functions._all_functions.get("GetRecorderSubmode")
cfunc = getattr(SC2Lib, "PCO_GetRecorderSubmode")
cfunc.argtypes = val.argtypes
func = catch_error(cfunc, val, val.__doc__)
_all_functions["GetRecorderSubmode"] = func
GetRecorderSubmode = func


val=functions._all_functions.get("SetCameraRamSegmentSize")
cfunc = getattr(SC2Lib, "PCO_SetCameraRamSegmentSize")
cfunc.argtypes = val.argtypes
func = catch_error(cfunc, val, val.__doc__)
_all_functions["SetCameraRamSegmentSize"] = func
SetCameraRamSegmentSize = func


val=functions._all_functions.get("GetSegmentImageSettings")
cfunc = getattr(SC2Lib, "PCO_GetSegmentImageSettings")
cfunc.argtypes = val.argtypes
func = catch_error(cfunc, val, val.__doc__)
_all_functions["GetSegmentImageSettings"] = func
GetSegmentImageSettings = func


val=functions._all_functions.get("AddBufferEx")
cfunc = getattr(SC2Lib, "PCO_AddBufferEx")
cfunc.argtypes = val.argtypes
func = catch_error(cfunc, val, val.__doc__)
_all_functions["AddBufferEx"] = func
AddBufferEx = func


val=functions._all_functions.get("CamLinkSetImageParameters")
cfunc = getattr(SC2Lib, "PCO_CamLinkSetImageParameters")
cfunc.argtypes = val.argtypes
func = catch_error(cfunc, val, val.__doc__)
_all_functions["CamLinkSetImageParameters"] = func
CamLinkSetImageParameters = func


val=functions._all_functions.get("SetDelayExposureTimeTable")
cfunc = getattr(SC2Lib, "PCO_SetDelayExposureTimeTable")
cfunc.argtypes = val.argtypes
func = catch_error(cfunc, val, val.__doc__)
_all_functions["SetDelayExposureTimeTable"] = func
SetDelayExposureTimeTable = func


val=functions._all_functions.get("CancelImages")
cfunc = getattr(SC2Lib, "PCO_CancelImages")
cfunc.argtypes = val.argtypes
func = catch_error(cfunc, val, val.__doc__)
_all_functions["CancelImages"] = func
CancelImages = func


val=functions._all_functions.get("SetRecorderSubmode")
cfunc = getattr(SC2Lib, "PCO_SetRecorderSubmode")
cfunc.argtypes = val.argtypes
func = catch_error(cfunc, val, val.__doc__)
_all_functions["SetRecorderSubmode"] = func
SetRecorderSubmode = func


val=functions._all_functions.get("GetTimestampMode")
cfunc = getattr(SC2Lib, "PCO_GetTimestampMode")
cfunc.argtypes = val.argtypes
func = catch_error(cfunc, val, val.__doc__)
_all_functions["GetTimestampMode"] = func
GetTimestampMode = func


val=functions._all_functions.get("GetROI")
cfunc = getattr(SC2Lib, "PCO_GetROI")
cfunc.argtypes = val.argtypes
func = catch_error(cfunc, val, val.__doc__)
_all_functions["GetROI"] = func
GetROI = func


val=functions._all_functions.get("SetPixelRate")
cfunc = getattr(SC2Lib, "PCO_SetPixelRate")
cfunc.argtypes = val.argtypes
func = catch_error(cfunc, val, val.__doc__)
_all_functions["SetPixelRate"] = func
SetPixelRate = func


val=functions._all_functions.get("GetExpTrigSignalStatus")
cfunc = getattr(SC2Lib, "PCO_GetExpTrigSignalStatus")
cfunc.argtypes = val.argtypes
func = catch_error(cfunc, val, val.__doc__)
_all_functions["GetExpTrigSignalStatus"] = func
GetExpTrigSignalStatus = func


val=functions._all_functions.get("SetStorageMode")
cfunc = getattr(SC2Lib, "PCO_SetStorageMode")
cfunc.argtypes = val.argtypes
func = catch_error(cfunc, val, val.__doc__)
_all_functions["SetStorageMode"] = func
SetStorageMode = func


val=functions._all_functions.get("GetDelayExposureTimeTable")
cfunc = getattr(SC2Lib, "PCO_GetDelayExposureTimeTable")
cfunc.argtypes = val.argtypes
func = catch_error(cfunc, val, val.__doc__)
_all_functions["GetDelayExposureTimeTable"] = func
GetDelayExposureTimeTable = func


val=functions._all_functions.get("SetCoolingSetpointTemperature")
cfunc = getattr(SC2Lib, "PCO_SetCoolingSetpointTemperature")
cfunc.argtypes = val.argtypes
func = catch_error(cfunc, val, val.__doc__)
_all_functions["SetCoolingSetpointTemperature"] = func
SetCoolingSetpointTemperature = func


val=functions._all_functions.get("AllocateBuffer")
cfunc = getattr(SC2Lib, "PCO_AllocateBuffer")
cfunc.argtypes = val.argtypes
func = catch_error(cfunc, val, val.__doc__)
_all_functions["AllocateBuffer"] = func
AllocateBuffer = func


val=functions._all_functions.get("SetDelayExposureTime")
cfunc = getattr(SC2Lib, "PCO_SetDelayExposureTime")
cfunc.argtypes = val.argtypes
func = catch_error(cfunc, val, val.__doc__)
_all_functions["SetDelayExposureTime"] = func
SetDelayExposureTime = func


val=functions._all_functions.get("GetCoolingSetpointTemperature")
cfunc = getattr(SC2Lib, "PCO_GetCoolingSetpointTemperature")
cfunc.argtypes = val.argtypes
func = catch_error(cfunc, val, val.__doc__)
_all_functions["GetCoolingSetpointTemperature"] = func
GetCoolingSetpointTemperature = func


val=functions._all_functions.get("GetCameraBusyStatus")
cfunc = getattr(SC2Lib, "PCO_GetCameraBusyStatus")
cfunc.argtypes = val.argtypes
func = catch_error(cfunc, val, val.__doc__)
_all_functions["GetCameraBusyStatus"] = func
GetCameraBusyStatus = func


val=functions._all_functions.get("SetDateTime")
cfunc = getattr(SC2Lib, "PCO_SetDateTime")
cfunc.argtypes = val.argtypes
func = catch_error(cfunc, val, val.__doc__)
_all_functions["SetDateTime"] = func
SetDateTime = func


val=functions._all_functions.get("GetOffsetMode")
cfunc = getattr(SC2Lib, "PCO_GetOffsetMode")
cfunc.argtypes = val.argtypes
func = catch_error(cfunc, val, val.__doc__)
_all_functions["GetOffsetMode"] = func
GetOffsetMode = func


val=functions._all_functions.get("GetCameraRamSegmentSize")
cfunc = getattr(SC2Lib, "PCO_GetCameraRamSegmentSize")
cfunc.argtypes = val.argtypes
func = catch_error(cfunc, val, val.__doc__)
_all_functions["GetCameraRamSegmentSize"] = func
GetCameraRamSegmentSize = func


val=functions._all_functions.get("FreeBuffer")
cfunc = getattr(SC2Lib, "PCO_FreeBuffer")
cfunc.argtypes = val.argtypes
func = catch_error(cfunc, val, val.__doc__)
_all_functions["FreeBuffer"] = func
FreeBuffer = func


val=functions._all_functions.get("CheckDeviceAvailability")
cfunc = getattr(SC2Lib, "PCO_CheckDeviceAvailability")
cfunc.argtypes = val.argtypes
func = catch_error(cfunc, val, val.__doc__)
_all_functions["CheckDeviceAvailability"] = func
CheckDeviceAvailability = func


val=functions._all_functions.get("GetSensorStruct")
cfunc = getattr(SC2Lib, "PCO_GetSensorStruct")
cfunc.argtypes = val.argtypes
func = catch_error(cfunc, val, val.__doc__)
_all_functions["GetSensorStruct"] = func
GetSensorStruct = func


val=functions._all_functions.get("ForceTrigger")
cfunc = getattr(SC2Lib, "PCO_ForceTrigger")
cfunc.argtypes = val.argtypes
func = catch_error(cfunc, val, val.__doc__)
_all_functions["ForceTrigger"] = func
ForceTrigger = func


val=functions._all_functions.get("GetPowerDownMode")
cfunc = getattr(SC2Lib, "PCO_GetPowerDownMode")
cfunc.argtypes = val.argtypes
func = catch_error(cfunc, val, val.__doc__)
_all_functions["GetPowerDownMode"] = func
GetPowerDownMode = func


val=functions._all_functions.get("SetOffsetMode")
cfunc = getattr(SC2Lib, "PCO_SetOffsetMode")
cfunc.argtypes = val.argtypes
func = catch_error(cfunc, val, val.__doc__)
_all_functions["SetOffsetMode"] = func
SetOffsetMode = func


val=functions._all_functions.get("SetConversionFactor")
cfunc = getattr(SC2Lib, "PCO_SetConversionFactor")
cfunc.argtypes = val.argtypes
func = catch_error(cfunc, val, val.__doc__)
_all_functions["SetConversionFactor"] = func
SetConversionFactor = func


val=functions._all_functions.get("GetUserPowerDownTime")
cfunc = getattr(SC2Lib, "PCO_GetUserPowerDownTime")
cfunc.argtypes = val.argtypes
func = catch_error(cfunc, val, val.__doc__)
_all_functions["GetUserPowerDownTime"] = func
GetUserPowerDownTime = func


val=functions._all_functions.get("ArmCamera")
cfunc = getattr(SC2Lib, "PCO_ArmCamera")
cfunc.argtypes = val.argtypes
func = catch_error(cfunc, val, val.__doc__)
_all_functions["ArmCamera"] = func
ArmCamera = func


val=functions._all_functions.get("GetADCOperation")
cfunc = getattr(SC2Lib, "PCO_GetADCOperation")
cfunc.argtypes = val.argtypes
func = catch_error(cfunc, val, val.__doc__)
_all_functions["GetADCOperation"] = func
GetADCOperation = func


