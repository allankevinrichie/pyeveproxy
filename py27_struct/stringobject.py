# https://github.com/python/cpython/blob/362ede2232107fc54d406bb9de7711ff7574e1d4/Include/stringobject.h
import ctypes
from .object import PyObject_VAR_HEAD


class PyStringObject(ctypes.Structure):
    _fields_ = PyObject_VAR_HEAD + [
        ('ob_shash', ctypes.c_long),
        ('ob_sstate', ctypes.c_int),
        ('ob_sval', ctypes.c_char * 1)
    ]
