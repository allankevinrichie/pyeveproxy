# https://github.com/python/cpython/blob/362ede2232107fc54d406bb9de7711ff7574e1d4/Include/funcobject.h
import ctypes
from .object import PyObject_HEAD, PyObject


# /* Function objects and code objects should not be confused with each other:
#  *
#  * Function objects are created by the execution of the 'def' statement.
#  * They reference a code object in their func_code attribute, which is a
#  * purely syntactic object, i.e. nothing more than a compiled version of some
#  * source code lines.  There is one code object per source code "fragment",
#  * but each code object can be referenced by zero or many function objects
#  * depending only on how many times the 'def' statement in the source was
#  * executed so far.
#  */
class PyFunctionObject(ctypes.Structure):
    _fields_ = PyObject_HEAD + [
        ('func_code', ctypes.POINTER(PyObject)),  # A code object
        ('func_globals', ctypes.POINTER(PyObject)),  # A dictionary (other mappings won't do)
        ('func_defaults', ctypes.POINTER(PyObject)),  # NULL or a tuple
        ('func_closure', ctypes.POINTER(PyObject)),  # NULL or a tuple of cell objects
        ('func_doc', ctypes.POINTER(PyObject)),  # The __doc__ attribute, can be anything
        ('func_name', ctypes.POINTER(PyObject)),  # The __name__ attribute, a string object
        ('func_dict', ctypes.POINTER(PyObject)),  # The __dict__ attribute, a dict or NULL
        ('func_weakreflist', ctypes.POINTER(PyObject)),  # List of weak references
        ('func_module', ctypes.POINTER(PyObject))  # The __module__ attribute, can be anything

        #     /* Invariant:
        #      *     func_closure contains the bindings for func_code->co_freevars, so
        #      *     PyTuple_Size(func_closure) == PyCode_GetNumFree(func_code)
        #      *     (func_closure may be NULL if PyCode_GetNumFree(func_code) == 0).
        #      */
    ]
