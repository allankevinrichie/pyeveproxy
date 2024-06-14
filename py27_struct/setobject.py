# https://github.com/python/cpython/blob/362ede2232107fc54d406bb9de7711ff7574e1d4/Include/setobject.h
import ctypes
from .object import PyObject, PyObject_HEAD


PySet_MINSIZE = 8


class SetEntry(ctypes.Structure):
    _fields_ = [
        ('hash', ctypes.c_long),  # /* cached hash code for the entry key */
        ('key', ctypes.POINTER(PyObject))
    ]


class SetObject(ctypes.Structure):
    _fields_ = PyObject_HEAD + [
        ('fill', ctypes.c_ssize_t),  # N Active + N Dummy
        ('used', ctypes.c_ssize_t),  # Active
        #     /* The table contains mask + 1 slots, and that's a power of 2.
        #      * We store the mask instead of the size because the mask is more
        #      * frequently needed.
        #      */
        ('mask', ctypes.c_ssize_t),
        #     /* table points to smalltable for small tables, else to
        #      * additional malloc'ed memory.  table is never NULL!  This rule
        #      * saves repeated runtime null-tests.
        #      */
        ('table', ctypes.POINTER(SetEntry)),
        ('lookup', ctypes.POINTER(ctypes.CFUNCTYPE(ctypes.POINTER(SetEntry), ctypes.POINTER(SetObject), ctypes.POINTER(PyObject), ctypes.c_long))),
        ('smalltable', SetEntry * PySet_MINSIZE),
        ('hash', ctypes.c_long),  # /* only used by frozenset objects */
        ('weakreflist', ctypes.POINTER(PyObject))  # List of weak references
    ]
