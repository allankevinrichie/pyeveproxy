# https://github.com/python/cpython/blob/362ede2232107fc54d406bb9de7711ff7574e1d4/Include/floatobject.h
import ctypes
from .object import PyObject_HEAD


class PyFloatObject(ctypes.Structure):
    _fields_ = PyObject_HEAD + [
        ('ob_fval', ctypes.c_double)
    ]