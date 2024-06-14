# https://github.com/python/cpython/blob/362ede2232107fc54d406bb9de7711ff7574e1d4/Include/intobject.h
import ctypes
from .object import PyObject_HEAD


class PyIntObject(ctypes.Structure):
    _fields_ = PyObject_HEAD + [
        ('ob_ival', ctypes.c_long)
    ]
