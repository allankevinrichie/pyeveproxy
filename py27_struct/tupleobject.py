# https://github.com/python/cpython/blob/362ede2232107fc54d406bb9de7711ff7574e1d4/Include/tupleobject.h
import ctypes
from .object import PyObject_VAR_HEAD, PyObject


class PyTupleObject(ctypes.Structure):
    _fields_ = PyObject_VAR_HEAD + [
        #     /* ob_item contains space for 'ob_size' elements.
        #      * Items must normally not be NULL, except during construction when
        #      * the tuple is not yet visible outside the function that builds it.
        #      */
        ('ob_item', ctypes.POINTER(PyObject) * 1)
    ]
