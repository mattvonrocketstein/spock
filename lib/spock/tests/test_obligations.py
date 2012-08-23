def IDIntoObjectTransform(_id):
    """ id into object transformer: idiot for short. """
    import _ctypes
    return _ctypes.PyObj_FromPtr(_id)
