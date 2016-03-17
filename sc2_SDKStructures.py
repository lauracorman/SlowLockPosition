from PCO_Structures import *
import ctypes

BOOL = ctypes.c_bool
float = ctypes.c_float
int = ctypes.c_int
char = ctypes.c_char
BYTE = ctypes.c_byte
long = ctypes.c_long
#word = ctypes.c_ulong
word = ctypes.c_ushort
dword = ctypes.c_long
short = ctypes.c_short
DWORD = dword
WORD = word
QWORD = ctypes.c_int64
double = ctypes.c_double
HANDLE = ctypes.c_void_p
SHORT = short
LONG = long

void_etoile = ctypes.c_void_p
unsigned_char_etoile = ctypes.c_char_p


union = ctypes.Union
#struct = ctypes.Structure 

class struct(ctypes.Structure):
    pass
#    def __init__(self, *args, **kwd):
#        super(struct, self).__init__(*args, **kwd)
#        if self._fields_[0][0]=="wSize":
#            _pack_ = 1 # test internet
#            self.wSize = 300
#            self.wSize = ctypes.sizeof(self)

PCO_STRUCTREV = 102
PCO_BUFCNT = 16 #apparemment pas ca le max
PCO_MAXDELEXPTABLE = 16
PCO_RAMSEGCNT = 4
PCO_MAXVERSIONHW = 10
PCO_MAXVERSIONFW = 10
PCO_ARM_COMMAND_TIMEOUT = 10000
PCO_HPX_COMMAND_TIMEOUT = 10000
PCO_COMMAND_TIMEOUT = 400
PCO_INTERFACE_FW = 1
PCO_INTERFACE_CL_MTX = 2
PCO_INTERFACE_CL_ME3 = 3
PCO_INTERFACE_CL_NAT = 4
PCO_INTERFACE_GIGE = 5
PCO_INTERFACE_USB = 6
PCO_INTERFACE_CL_ME4 = 7
PCO_INTERFACE_USB3 = 8
PCO_INTERFACE_WLAN = 9
PCO_INTERFACE_HS_ME5 = 11
PCO_LASTINTERFACE = PCO_INTERFACE_HS_ME5
PCO_INTERFACE_CL_SER = 10
PCO_INTERFACE_GENERIC = 20
PCO_OPENFLAG_GENERIC_IS_CAMLINK = 0x0001
PCO_OPENFLAG_HIDE_PROGRESS = 0x0002
class PCO_Buflist(ctypes.Structure):
	_fields_=[("sBufNr",SHORT),
        ("ZZwAlignDummy",WORD),
        ("dwStatusDll",DWORD),
        ("dwStatusDrv",DWORD)]

class PCO_OpenStruct(ctypes.Structure):
	_fields_=[("wSize",WORD),
        ("wInterfaceType",WORD),
        ("wCameraNumber",WORD),
        ("wCameraNumAtInterface",WORD),
        ("wOpenFlags",WORD*10),
        ("dwOpenFlags",DWORD*5),
        ("wOpenPtr",void_etoile*6),
        ("zzwDummy",WORD*8)]

class PCO_SC2_Hardware_DESC(ctypes.Structure):
	_fields_=[("szName",char*16),
        ("wBatchNo",WORD),
        ("wRevision",WORD),
        ("wVariant",WORD),
        ("ZZwDummy",WORD*20)]

class PCO_SC2_Firmware_DESC(ctypes.Structure):
	_fields_=[("szName",char*16),
        ("bMinorRev",BYTE),
        ("bMajorRev",BYTE),
        ("wVariant",WORD),
        ("ZZwDummy",WORD*22)]

class PCO_HW_Vers(ctypes.Structure):
	_fields_=[("BoardNum",WORD),
        ("Board",PCO_SC2_Hardware_DESC*PCO_MAXVERSIONHW)]

class PCO_FW_Vers(ctypes.Structure):
	_fields_=[("DeviceNum",WORD),
        ("Device",PCO_SC2_Firmware_DESC*PCO_MAXVERSIONFW)]

class PCO_CameraType(ctypes.Structure):
	_pack_ = 0 
	_fields_=[("wSize",WORD),
        ("wCamType",WORD),
        ("wCamSubType",WORD),
        ("ZZwAlignDummy1",WORD),
        ("dwSerialNumber",DWORD),
        ("dwHWVersion",DWORD),
        ("dwFWVersion",DWORD),
        ("wInterfaceType",WORD),
        ("strHardwareVersion",PCO_HW_Vers),
        ("strFirmwareVersion",PCO_FW_Vers),
        ("ZZwDummy",WORD*39)]

class PCO_General(ctypes.Structure):
	_fields_=[("wSize",WORD),
        ("ZZwAlignDummy1",WORD),
        ("strCamType",PCO_CameraType),
        ("dwCamHealthWarnings",DWORD),
        ("dwCamHealthErrors",DWORD),
        ("dwCamHealthStatus",DWORD),
        ("sCCDTemperature",SHORT),
        ("sCamTemperature",SHORT),
        ("sPowerSupplyTemperature",SHORT),
        ("ZZwDummy",WORD*37)]

class PCO_Description(ctypes.Structure):
	_fields_=[("wSize",WORD),
        ("wSensorTypeDESC",WORD),
        ("wSensorSubTypeDESC",WORD),
        ("wMaxHorzResStdDESC",WORD),
        ("wMaxVertResStdDESC",WORD),
        ("wMaxHorzResExtDESC",WORD),
        ("wMaxVertResExtDESC",WORD),
        ("wDynResDESC",WORD),
        ("wMaxBinHorzDESC",WORD),
        ("wBinHorzSteppingDESC",WORD),
        ("wMaxBinVertDESC",WORD),
        ("wBinVertSteppingDESC",WORD),
        ("wRoiHorStepsDESC",WORD),
        ("wRoiVertStepsDESC",WORD),
        ("wNumADCsDESC",WORD),
        ("wMinSizeHorzDESC",WORD),
        ("dwPixelRateDESC",DWORD*4),
        ("ZZdwDummypr",DWORD*20),
        ("wConvFactDESC",WORD*4),
        ("sCoolingSetpoints",SHORT*10),
        ("ZZdwDummycv",WORD*8),
        ("wSoftRoiHorStepsDESC",WORD),
        ("wSoftRoiVertStepsDESC",WORD),
        ("wIRDESC",WORD),
        ("wMinSizeVertDESC",WORD),
        ("dwMinDelayDESC",DWORD),
        ("dwMaxDelayDESC",DWORD),
        ("dwMinDelayStepDESC",DWORD),
        ("dwMinExposureDESC",DWORD),
        ("dwMaxExposureDESC",DWORD),
        ("dwMinExposureStepDESC",DWORD),
        ("dwMinDelayIRDESC",DWORD),
        ("dwMaxDelayIRDESC",DWORD),
        ("dwMinExposureIRDESC",DWORD),
        ("dwMaxExposureIRDESC",DWORD),
        ("wTimeTableDESC",WORD),
        ("wDoubleImageDESC",WORD),
        ("sMinCoolSetDESC",SHORT),
        ("sMaxCoolSetDESC",SHORT),
        ("sDefaultCoolSetDESC",SHORT),
        ("wPowerDownModeDESC",WORD),
        ("wOffsetRegulationDESC",WORD),
        ("wColorPatternDESC",WORD),
        ("wPatternTypeDESC",WORD),
        ("wDummy1",WORD),
        ("wDummy2",WORD),
        ("wNumCoolingSetpoints",WORD),
        ("dwGeneralCapsDESC1",DWORD),
        ("dwGeneralCapsDESC2",DWORD),
        ("dwExtSyncFrequency",DWORD*2),
        ("dwReservedDESC",DWORD*4),
        ("ZZdwDummy",DWORD*40)]

class PCO_Description2(ctypes.Structure):
	_fields_=[("wSize",WORD),
        ("ZZwAlignDummy1",WORD),
        ("dwMinPeriodicalTimeDESC2",DWORD),
        ("dwMaxPeriodicalTimeDESC2",DWORD),
        ("dwMinPeriodicalConditionDESC2",DWORD),
        ("dwMaxNumberOfExposuresDESC2",DWORD),
        ("lMinMonitorSignalOffsetDESC2",LONG),
        ("dwMaxMonitorSignalOffsetDESC2",DWORD),
        ("dwMinPeriodicalStepDESC2",DWORD),
        ("dwStartTimeDelayDESC2",DWORD),
        ("dwMinMonitorStepDESC2",DWORD),
        ("dwMinDelayModDESC2",DWORD),
        ("dwMaxDelayModDESC2",DWORD),
        ("dwMinDelayStepModDESC2",DWORD),
        ("dwMinExposureModDESC2",DWORD),
        ("dwMaxExposureModDESC2",DWORD),
        ("dwMinExposureStepModDESC2",DWORD),
        ("dwModulateCapsDESC2",DWORD),
        ("dwReserved",DWORD*16),
        ("ZZdwDummy",DWORD*41)]

class PCO_DescriptionEx(ctypes.Structure):
	_fields_=[("wSize",WORD)]

NUM_MAX_SIGNALS = 20
NUM_SIGNALS = 4
NUM_SIGNAL_NAMES = 4
class PCO_Single_Signal_Desc(ctypes.Structure):
	_fields_=[("wSize",WORD),
        ("ZZwAlignDummy1",WORD),
        ("strSignalName",char*NUM_SIGNAL_NAMES),
        ("wSignalDefinitions",WORD),
        ("wSignalTypes",WORD),
        ("wSignalPolarity",WORD),
        ("wSignalFilter",WORD),
        ("dwDummy",DWORD*22)]

class PCO_Signal_Description(ctypes.Structure):
	_fields_=[("wSize",WORD),
        ("wNumOfSignals",WORD),
        ("strSingeSignalDesc",PCO_Single_Signal_Desc*NUM_MAX_SIGNALS),
        ("dwDummy",DWORD*524)]

PCO_SENSORDUMMY = 7
class PCO_Sensor(ctypes.Structure):
	_fields_=[("wSize",WORD),
        ("ZZwAlignDummy1",WORD),
        ("strDescription",PCO_Description),
        ("strDescription2",PCO_Description2),
        ("ZZdwDummy2",DWORD*256),
        ("wSensorformat",WORD),
        ("wRoiX0",WORD),
        ("wRoiY0",WORD),
        ("wRoiX1",WORD),
        ("wRoiY1",WORD),
        ("wBinHorz",WORD),
        ("wBinVert",WORD),
        ("ZZwAlignDummy2",WORD),
        ("dwPixelRate",DWORD),
        ("wConvFact",WORD),
        ("wDoubleImage",WORD),
        ("wADCOperation",WORD),
        ("wIR",WORD),
        ("sCoolSet",SHORT),
        ("wOffsetRegulation",WORD),
        ("wNoiseFilterMode",WORD),
        ("wFastReadoutMode",WORD),
        ("wDSNUAdjustMode",WORD),
        ("wCDIMode",WORD),
        ("ZZwDummy",WORD*36),
        ("strSignalDesc",PCO_Signal_Description),
        ("ZZdwDummy",DWORD*PCO_SENSORDUMMY)]

class PCO_Signal(ctypes.Structure):
	_fields_=[("wSize",WORD),
        ("wSignalNum",WORD),
        ("wEnabled",WORD),
        ("wType",WORD),
        ("wPolarity",WORD),
        ("wFilterSetting",WORD),
        ("wSelected",WORD),
        ("ZZwReserved",WORD),
        ("dwParameter",DWORD*4),
        ("dwSignalFunctionality",DWORD*4),
        ("ZZdwReserved",DWORD*3)]

class PCO_ImageTiming(ctypes.Structure):
	_fields_=[("wSize",WORD),
        ("wDummy",WORD),
        ("FrameTime_ns",DWORD),
        ("FrameTime_s",DWORD),
        ("ExposureTime_ns",DWORD),
        ("ExposureTime_s",DWORD),
        ("TriggerSystemDelay_ns",DWORD),
        ("TriggerSystemJitter_ns",DWORD),
        ("TriggerDelay_ns",DWORD),
        ("TriggerDelay_s",DWORD),
        ("ZZdwDummy",DWORD*11)]

PCO_TIMINGDUMMY = 24
class PCO_Timing(ctypes.Structure):
	_fields_=[("wSize",WORD),
        ("wTimeBaseDelay",WORD),
        ("wTimeBaseExposure",WORD),
        ("ZZwAlignDummy1",WORD),
        ("ZZdwDummy0",DWORD*2),
        ("dwDelayTable",DWORD*PCO_MAXDELEXPTABLE),
        ("ZZdwDummy1",DWORD*114),
        ("dwExposureTable",DWORD*PCO_MAXDELEXPTABLE),
        ("ZZdwDummy2",DWORD*112),
        ("wTriggerMode",WORD),
        ("wForceTrigger",WORD),
        ("wCameraBusyStatus",WORD),
        ("wPowerDownMode",WORD),
        ("dwPowerDownTime",DWORD),
        ("wExpTrgSignal",WORD),
        ("wFPSExposureMode",WORD),
        ("dwFPSExposureTime",DWORD),
        ("wModulationMode",WORD),
        ("wCameraSynchMode",WORD),
        ("dwPeriodicalTime",DWORD),
        ("wTimeBasePeriodical",WORD),
        ("ZZwAlignDummy3",WORD),
        ("dwNumberOfExposures",DWORD),
        ("lMonitorOffset",LONG),
        ("strSignal",PCO_Signal*NUM_MAX_SIGNALS),
        ("wStatusFrameRate",WORD),
        ("wFrameRateMode",WORD),
        ("dwFrameRate",DWORD),
        ("dwFrameRateExposure",DWORD),
        ("wTimingControlMode",WORD),
        ("wFastTimingMode",WORD),
        ("ZZwDummy",WORD*PCO_TIMINGDUMMY)]

PCO_STORAGEDUMMY = 39
class PCO_Storage(ctypes.Structure):
	_fields_=[("wSize",WORD),
        ("ZZwAlignDummy1",WORD),
        ("dwRamSize",DWORD),
        ("wPageSize",WORD),
        ("ZZwAlignDummy4",WORD),
        ("dwRamSegSize",DWORD*PCO_RAMSEGCNT),
        ("ZZdwDummyrs",DWORD*20),
        ("wActSeg",WORD),
        ("ZZwDummy",WORD*PCO_STORAGEDUMMY)]

PCO_RECORDINGDUMMY = 22
class PCO_Recording(ctypes.Structure):
	_fields_=[("wSize",WORD),
        ("wStorageMode",WORD),
        ("wRecSubmode",WORD),
        ("wRecState",WORD),
        ("wAcquMode",WORD),
        ("wAcquEnableStatus",WORD),
        ("ucDay",BYTE),
        ("ucMonth",BYTE),
        ("wYear",WORD),
        ("wHour",WORD),
        ("ucMin",BYTE),
        ("ucSec",BYTE),
        ("wTimeStampMode",WORD),
        ("wRecordStopEventMode",WORD),
        ("dwRecordStopDelayImages",DWORD),
        ("wMetaDataMode",WORD),
        ("wMetaDataSize",WORD),
        ("wMetaDataVersion",WORD),
        ("ZZwDummy1",WORD),
        ("dwAcquModeExNumberImages",DWORD),
        ("dwAcquModeExReserved",DWORD*4),
        ("ZZwDummy",WORD*PCO_RECORDINGDUMMY)]

class PCO_Segment(ctypes.Structure):
	_fields_=[("wSize",WORD),
        ("wXRes",WORD),
        ("wYRes",WORD),
        ("wBinHorz",WORD),
        ("wBinVert",WORD),
        ("wRoiX0",WORD),
        ("wRoiY0",WORD),
        ("wRoiX1",WORD),
        ("wRoiY1",WORD),
        ("ZZwAlignDummy1",WORD),
        ("dwValidImageCnt",DWORD),
        ("dwMaxImageCnt",DWORD),
        ("wRoiSoftX0",WORD),
        ("wRoiSoftY0",WORD),
        ("wRoiSoftX1",WORD),
        ("wRoiSoftY1",WORD),
        ("wRoiSoftXRes",WORD),
        ("wRoiSoftYRes",WORD),
        ("wRoiSoftDouble",WORD),
        ("ZZwDummy",WORD*33)]

class PCO_Image_ColorSet(ctypes.Structure):
	_fields_=[("wSize",WORD),
        ("sSaturation",SHORT),
        ("sVibrance",SHORT),
        ("wColorTemp",WORD),
        ("sTint",SHORT),
        ("wMulNormR",WORD),
        ("wMulNormG",WORD),
        ("wMulNormB",WORD),
        ("sContrast",SHORT),
        ("wGamma",WORD),
        ("wSharpFixed",WORD),
        ("wSharpAdaptive",WORD),
        ("wScaleMin",WORD),
        ("wScaleMax",WORD),
        ("wProcOptions",WORD),
        ("ZZwDummy",WORD*93)]

class PCO_Image(ctypes.Structure):
	_fields_=[("wSize",WORD),
        ("ZZwAlignDummy1",WORD),
        ("strSegment",PCO_Segment*PCO_RAMSEGCNT),
        ("ZZstrDummySeg",PCO_Segment*14),
        ("strColorSet",PCO_Image_ColorSet),
        ("wBitAlignment",WORD),
        ("wHotPixelCorrectionMode",WORD),
        ("ZZwDummy",WORD*38)]

PCO_BUFFER_STATICS = 0xFFFF0000
PCO_BUFFER_ALLOCATED = 0x80000000
PCO_BUFFER_EVENTDLL = 0x40000000
PCO_BUFFER_ISEXTERN = 0x20000000
PCO_BUFFER_EVAUTORES = 0x10000000
PCO_BUFFER_EVENTSET = 0x00008000
