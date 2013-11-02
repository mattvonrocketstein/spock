""" spock.ambients.util
"""

class arg_types(object):
    """ A decorator which enforces the rule that all arguments must be
        of type "Ambient".  All keyword arguments are ignored.
    """
    def __init__(self, fxn, types):
        self.fxn = fxn
        self.types = types if isinstance(types, (list, tuple)) else [types]

    def __call__(self, *args, **kargs):
        assert all(
            [ any([ isinstance(a, x) for x in self.types]) for a in args ] )
        return self.fxn(*args, **kargs)

from .abstract import AbstractAmbient

ambient_args = lambda fxn: arg_types(fxn, [AbstractAmbient])
