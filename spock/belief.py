""" spock.belief
"""
from datetime import datetime
from spock.simplex import symbol

ALWAYS = always = symbol._belief_always
NEVER = never = symbol._belief_never

class BadBelief(ValueError):
    pass
class Belief(object):
    """ a belief is a artifact in temporal logic.  see Shoham:1993
        for more information.  In his description, both `at` and `about`
        are time-valued, and `context` is potentially recursive.  That
        is to say, beliefs can be nested to represent a belief about a
        belief.  A `context` should essentially function as a predicate,
        but for flexibility this is left as an implementation detail.
    """
    def __init__(self, at=None, about=None, ctx=None, starting=None, ending=None):
        """ see Belief.__doc__ """
        if at in [always, never]:
            self.at = at
        else:
            if at is None:
                if starting is None or ending is None:
                    raise BadBelief("when at=None, must provide starting/ending kwargs")
                at = [starting, ending]
            self.at = at
            if not isinstance(at, list):
                raise BadBelief(
                    ("at={0} but it should be a time interval,"
                     " or always/never symbol").format(self.at))
            if len(at)!=2:
                raise BadBelief(
                    ("at={0} but it should be a time interval like [start, end]").format(
                        self.at))
            assert all([isinstance(x, datetime) for x in self.at])
            starting,ending=self.at
            if starting >= ending:
                raise BadBelief("`starting` value cannot be before `ending`")

        assert at is not None

        self.about = about
        self.ctx = ctx
        assert about is not None
        assert ctx is not None

    def holds_when(self, t):
        """ check whether belief applies at time `t`"""
        if self.at == always:
            return True
        elif self.at== never:
            return False
        if self.at[0] < t < self.at[1]:
            return True

    def holds(self):
        """ check whether belief holds now """
        return self.holds_when(datetime.now())

    def __call__(self, obj):
        """ tests belief against object at the present time"""
        if obj==self.about and self.holds():
            return self.ctx
        return False
