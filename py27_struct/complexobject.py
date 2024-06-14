# https://github.com/python/cpython/blob/362ede2232107fc54d406bb9de7711ff7574e1d4/Include/complexobject.h
import ctypes
from .object import PyObject_HEAD


class Py_complex(ctypes.Structure):
    _fields_ = [
        ('real', ctypes.c_double),
        ('imag', ctypes.c_double)
    ]


class PyComplexObject(ctypes.Structure):
    _fields_ = PyObject_HEAD + [
        ('cval', Py_complex * 2)
    ]
