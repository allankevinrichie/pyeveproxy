# https://github.com/python/cpython/blob/362ede2232107fc54d406bb9de7711ff7574e1d4/Include/classobject.h
import ctypes
from .object import PyObject_HEAD, PyObject


class PyClassObject(ctypes.Structure):
    _fields_ = PyObject_HEAD + [
        ('cl_bases', ctypes.POINTER(PyObject)),  # A tuple of class objects
        ('cl_dict', ctypes.POINTER(PyObject)),  # A dictionary
        ('cl_name', ctypes.POINTER(PyObject)),  # A string
        # The following three are functions or NULL
        ('cl_getattr', ctypes.POINTER(PyObject)),
        ('cl_setattr', ctypes.POINTER(PyObject)),
        ('cl_delattr', ctypes.POINTER(PyObject)),
        ('cl_weakreflist', ctypes.POINTER(PyObject))  # List of weak references
    ]


class PyInstanceObject(ctypes.Structure):
    _fields_ = PyObject_HEAD + [
        ('in_class', ctypes.POINTER(PyClassObject)),  # The class object
        ('in_dict', ctypes.POINTER(PyObject)),  # A dictionary
        ('in_weakreflist', ctypes.POINTER(PyObject))  # List of weak references
    ]


class PyMethodObject(ctypes.Structure):
    _fields_ = PyObject_HEAD + [
        ('im_func', ctypes.POINTER(PyObject)),
        ('im_self', ctypes.POINTER(PyObject)),
        ('im_class', ctypes.POINTER(PyObject)),
        ('im_weakreflist', ctypes.POINTER(PyObject))
    ]
