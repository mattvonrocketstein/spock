""" spock.ambients

    implements a subset of the Ambient Calculus

    see also:
      http://lucacardelli.name/Papers/Ambient%20Logic.A4.pdf
      http://en.wikipedia.org/wiki/Ambient_calculus
"""

from .abstract import AbstractAmbient
from .util import ambient_args

class Ambient(AbstractAmbient):
    """  Communication within (i.e. local to) an ambient is anonymous and
         asynchronous. Output actions release names or capabilities into
         the surrounding ambient. Input actions capture a value from the
         ambient, and bind it to a variable. Non-local I/O can be represented
         in terms of these local communications actions by a variety of means.
         One approach is to use mobile "messenger" agents that carry a message
         from one ambient to another (using the capabilities described above).
         Another approach is to emulate channel-based communications by modeling
         a channel in terms of ambients and operations on those ambients.[1] The
         three basic ambient primitives, namely in, out, and open are expressive
         enough to simulate name-passing channels in the pi-calculus.

         http://en.wikipedia.org/wiki/Ambient_calculus
    """
    def __init__(self, content={}, parent=None):
        self.parent = parent
        self.content=content
    @arg_types()
    def _set_content(self, content):
    self.content = content

    def _set_parent(self, parent):
        self._parent = parent
    def _get_parent(self):
        return self._parent
    parent = property(_get_parent, _set_parent)

    @ambient_args
    def adjacent(self, other):
        """ ambient adjacency: a very naive default topology """
        return self.parent==other.parent
    sibling = adjacent

    @ambient_args
    def enter(self, other, continuation=None):
        """ in(m,P) instructs the surrounding ambient to enter
            some sibling ambient m, and then proceed as P
        """
        assert self.is_sibling(other), 'Can only enter a sibling ambient'
        self.parent = other
        if continuation is not None:
            continuation()

    @ambient_args
    def exit(self, other, continuation=None):
        """ out(m,P) instructs the surrounding ambient
            to exit its parent ambient m.
        """
        p = self.parent
        assert p is not None, 'Cannot exist the uppermost ambient'
        if continuation is not None:
            continuation()

    @ambient_args
    def open(self, other, continuation=None):
        """open(m, P) instructs the surrounding ambient to
           dissolve the boundary of an ambient m located at
           the same level
        """

    @ambient_args
    def copy(self, other):
        """ copy(m) makes any number of copy of something m """
