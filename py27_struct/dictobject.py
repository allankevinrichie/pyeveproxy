# https://github.com/python/cpython/blob/362ede2232107fc54d406bb9de7711ff7574e1d4/Include/dictobject.h
import ctypes
from .object import PyObject, PyObject_HEAD

PyDict_MINSIZE = 8


class PyDictEntry(ctypes.Structure):
    _fields_ = [
        #     /* Cached hash code of me_key.  Note that hash codes are C longs.
        #      * We have to use Py_ssize_t instead because dict_popitem() abuses
        #      * me_hash to hold a search finger.
        #      */
        ('me_hash', ctypes.c_ssize_t),
        ('me_key', ctypes.POINTER(PyObject)),
        ('me_value', ctypes.POINTER(PyObject))
    ]


class PyDictObject(ctypes.Structure):
    _fields_ = PyObject_HEAD + [
        ('ma_fill', ctypes.c_ssize_t),
        ('ma_used', ctypes.c_ssize_t),
        #     /* The table contains ma_mask + 1 slots, and that's a power of 2.
        #      * We store the mask instead of the size because the mask is more
        #      * frequently needed.
        #      */
        ('ma_mask', ctypes.c_ssize_t),
        #     /* ma_table points to ma_smalltable for small tables, else to
        #      * additional malloc'ed memory.  ma_table is never NULL!  This rule
        #      * saves repeated runtime null-tests in the workhorse getitem and
        #      * setitem calls.
        #      */
        ('ma_table', ctypes.POINTER(PyDictEntry)),
        ('ma_lookup', ctypes.POINTER(ctypes.CFUNCTYPE(ctypes.POINTER(PyDictEntry), ctypes.c_void_p, ctypes.POINTER(PyObject), ctypes.c_long))),
        ('ma_smalltable', PyDictEntry * PyDict_MINSIZE)
    ]
