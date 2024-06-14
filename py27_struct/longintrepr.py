# https://github.com/python/cpython/blob/362ede2232107fc54d406bb9de7711ff7574e1d4/Include/longobject.h
import ctypes
from .object import PyObject_VAR_HEAD


# constants for Win64
SIZEOF_VOID_P = 8
PYLONG_BITS_IN_DIGIT = 30
PY_UINT32_T = ctypes.c_uint32
PY_INT32_T = ctypes.c_int32
PY_UINT64_T = ctypes.c_uint64
PY_INT64_T = ctypes.c_int64
digit = PY_UINT32_T
sdigit = PY_INT32_T
twodigits = PY_UINT64_T
stwodigits = PY_INT64_T
PyLong_SHIFT = 30
_PyLong_DECIMAL_SHIFT = 9
_PyLong_DECIMAL_BASE = 1000000000


class LongObject(ctypes.Structure):
    # /* Long integer representation.
    #    The absolute value of a number is equal to
    #    	SUM(for i=0 through abs(ob_size)-1) ob_digit[i] * 2**(SHIFT*i)
    #    Negative numbers are represented with ob_size < 0;
    #    zero is represented by ob_size == 0.
    #    In a normalized number, ob_digit[abs(ob_size)-1] (the most significant
    #    digit) is never zero.  Also, in all cases, for all valid i,
    #    	0 <= ob_digit[i] <= MASK.
    #    The allocation function takes care of allocating extra memory
    #    so that ob_digit[0] ... ob_digit[abs(ob_size)-1] are actually available.
    #
    #    CAUTION:  Generic code manipulating subtypes of PyVarObject has to
    #    aware that longs abuse  ob_size's sign bit.
    # */
    _fields_ = [
        ('PyObject_VAR_HEAD', ctypes.c_byte * PyObject_VAR_HEAD),
        ('ob_digit', digit * 1)
    ]
