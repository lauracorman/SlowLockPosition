import ctypes

BOOL = ctypes.c_bool
float = ctypes.c_float
int = ctypes.c_int
char = ctypes.c_char
BYTE = ctypes.c_byte
long = ctypes.c_long
word = ctypes.c_ulong
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
struct = ctypes.Structure 

class SRGBCOLCORRCOEFF(struct):
	_fields_=[("da11",double),
        ("da12",double),
        ("da13",double),
        ("da21",double),
        ("da22",double),
        ("da23",double),
        ("da31",double),
        ("da32",double),
        ("da33",double)]

