# https://github.com/python/cpython/blob/362ede2232107fc54d406bb9de7711ff7574e1d4/Include/listobject.h
import ctypes
from .object import PyObject_VAR_HEAD, PyObject


class PyListObject(ctypes.Structure):
    _fields_ = PyObject_VAR_HEAD + [
        # /* Vector of pointers to list elements.  list[0] is ob_item[0], etc. */
        ('ob_item', ctypes.POINTER(ctypes.POINTER(PyObject))),
        # /* ob_item contains space for 'allocated' elements.  The number
        #  * currently in use is ob_size.
        #  * Invariants:
        #  *     0 <= ob_size <= allocated
        #  *     len(list) == ob_size
        #  *     ob_item == NULL implies ob_size == allocated == 0
        #  * list.sort() temporarily sets allocated to -1 to detect mutations.
        #  *
        #  * Items must normally not be NULL, except during construction when
        #  * the list is not yet visible outside the function that builds it.
        #  */
        ('allocated', ctypes.c_ssize_t)
    ]
