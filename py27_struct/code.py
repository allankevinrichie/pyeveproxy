# https://github.com/python/cpython/blob/362ede2232107fc54d406bb9de7711ff7574e1d4/Include/code.h
import ctypes
from .object import PyObject_HEAD, PyObject


class PyCodeObject(ctypes.Structure):
    _fields_ = [
        ('PyObject_HEAD', ctypes.c_byte * PyObject_HEAD),
        ('co_argcount', ctypes.c_int),
        ('co_nlocals', ctypes.c_int),
        ('co_stacksize', ctypes.c_int),
        ('co_flags', ctypes.c_int),
        ('co_code', ctypes.POINTER(PyObject)),
        ('co_consts', ctypes.POINTER(PyObject)),
        ('co_names', ctypes.POINTER(PyObject)),
        ('co_varnames', ctypes.POINTER(PyObject)),
        ('co_freevars', ctypes.POINTER(PyObject)),
        ('co_cellvars', ctypes.POINTER(PyObject)),
        ('co_filename', ctypes.POINTER(PyObject)),
        ('co_name', ctypes.POINTER(PyObject)),
        ('co_firstlineno', ctypes.c_int),
        ('co_lnotab', ctypes.POINTER(PyObject)),
        ('co_zombieframe', ctypes.c_void_p),
        ('co_weakreflist', ctypes.POINTER(PyObject))
    ]
