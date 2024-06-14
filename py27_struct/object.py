# https://github.com/python/cpython/blob/362ede2232107fc54d406bb9de7711ff7574e1d4/Include/object.h
import ctypes

# /*
# Objects are structures allocated on the heap.  Special rules apply to
# the use of objects to ensure they are properly garbage-collected.
# Objects are never allocated statically or on the stack; they must be
# accessed through special macros and functions only.  (Type objects are
# exceptions to the first rule; the standard types are represented by
# statically initialized type objects, although work on type/class unification
# for Python 2.2 made it possible to have heap-allocated type objects too).
#
# An object has a 'reference count' that is increased or decreased when a
# pointer to the object is copied or deleted; when the reference count
# reaches zero there are no references to the object left and it can be
# removed from the heap.
#
# An object has a 'type' that determines what it represents and what kind
# of data it contains.  An object's type is fixed when it is created.
# Types themselves are represented as objects; an object contains a
# pointer to the corresponding type object.  The type itself has a type
# pointer pointing to the object representing the type 'type', which
# contains a pointer to itself!).
#
# Objects do not float around in memory; once allocated an object keeps
# the same size and address.  Objects that must hold variable-size data
# can contain pointers to variable-size parts of the object.  Not all
# objects of the same type have the same size; but the size cannot change
# after allocation.  (These restrictions are made so a reference to an
# object can be simply a pointer -- moving an object would require
# updating all the pointers, and changing an object's size would require
# moving it if there was another object right next to it.)
#
# Objects are always accessed through pointers of the type 'PyObject *'.
# The type 'PyObject' is a structure that only contains the reference count
# and the type pointer.  The actual memory allocated for an object
# contains other data that can only be accessed after casting the pointer
# to a pointer to a longer structure type.  This longer type must start
# with the reference count and type fields; the macro PyObject_HEAD should be
# used for this (to accommodate for future changes).  The implementation
# of a particular object type can cast the object pointer to the proper
# type and back.
#
# A standard interface exists for objects that contain an array of items
# whose size is determined when the object is allocated.
# */


class PyObject(ctypes.Structure):
    pass


class PyTypeObject(ctypes.Structure):
    pass


_PyObject_HEAD_EXTRA = [
    ("_ob_next", ctypes.POINTER(PyObject)),
    ("_ob_prev", ctypes.POINTER(PyObject))
]

PyObject_HEAD = _PyObject_HEAD_EXTRA + [
    ("ob_refcnt", ctypes.c_ssize_t),
    ("ob_type", ctypes.POINTER(PyTypeObject))
]

PyObject_VAR_HEAD = PyObject_HEAD + [
    ("ob_size", ctypes.c_ssize_t)
]


PyObject._fields_ = PyObject_HEAD


class PyVarObject(ctypes.Structure):
    _fields_ = PyObject_VAR_HEAD


PyTypeObject._fields_ = PyObject_VAR_HEAD + [
        ('tp_name', ctypes.c_char_p),
        ('tp_basicsize', ctypes.c_ssize_t),
        ('tp_itemsize', ctypes.c_ssize_t),
        ('tp_dealloc', ctypes.c_void_p),
        ('tp_print', ctypes.c_void_p),
        ('tp_getattr', ctypes.c_void_p),
        ('tp_setattr', ctypes.c_void_p),
        ('tp_compare', ctypes.c_void_p),
        ('tp_repr', ctypes.c_void_p),
        ('tp_as_number', ctypes.c_void_p),
        ('tp_as_sequence', ctypes.c_void_p),
        ('tp_as_mapping', ctypes.c_void_p),
        ('tp_hash', ctypes.c_void_p),
        ('tp_call', ctypes.c_void_p),
        ('tp_str', ctypes.c_void_p),
        ('tp_getattro', ctypes.c_void_p),
        ('tp_setattro', ctypes.c_void_p),
        ('tp_as_buffer', ctypes.c_void_p),
        ('tp_flags', ctypes.c_long),
        ('tp_doc', ctypes.c_char_p),
        ('tp_traverse', ctypes.c_void_p),
        ('tp_clear', ctypes.c_void_p),
        ('tp_richcompare', ctypes.c_void_p),
        ('tp_weaklistoffset', ctypes.c_ssize_t),
        ('tp_iter', ctypes.c_void_p),
        ('tp_iternext', ctypes.c_void_p),
        ('tp_methods', ctypes.c_void_p),
        ('tp_members', ctypes.c_void_p),
        ('tp_getset', ctypes.c_void_p),
        ('tp_base', ctypes.c_void_p),
        ('tp_dict', ctypes.POINTER(PyObject)),
        ('tp_descr_get', ctypes.c_void_p),
        ('tp_descr_set', ctypes.c_void_p),
        ('tp_dictoffset', ctypes.c_ssize_t),
        ('tp_init', ctypes.c_void_p),
        ('tp_alloc', ctypes.c_void_p),
        ('tp_new', ctypes.c_void_p),
        ('tp_free', ctypes.c_void_p),
        ('tp_is_gc', ctypes.c_void_p),
        ('tp_bases', ctypes.POINTER(PyObject)),
        ('tp_mro', ctypes.POINTER(PyObject)),
        ('tp_cache', ctypes.POINTER(PyObject)),
        ('tp_subclasses', ctypes.POINTER(PyObject)),
        ('tp_weaklist', ctypes.POINTER(PyObject)),
        ('tp_del', ctypes.c_void_p),
        ('tp_version_tag', ctypes.c_uint),
        ('tp_allocs', ctypes.c_ssize_t),
        ('tp_frees', ctypes.c_ssize_t),
        ('tp_maxalloc', ctypes.c_ssize_t),
        ('tp_prev', ctypes.c_void_p),
        ('tp_next', ctypes.c_void_p)
    ]
