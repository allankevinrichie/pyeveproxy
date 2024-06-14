# https://github.com/python/cpython/blob/362ede2232107fc54d406bb9de7711ff7574e1d4/Include/bytearrayobject.h
import ctypes
from .object import PyObject_VAR_HEAD


class PyByteArrayObject(ctypes.Structure):
    _fields_ = PyObject_VAR_HEAD + [
        ('ob_exports', ctypes.c_int),
        ('ob_alloc', ctypes.c_ssize_t),
        ('ob_bytes', ctypes.POINTER(ctypes.c_char))
    ]
