import _ctypes
def di(_id):
    """ invert id() muahaha """
    return _ctypes.PyObj_FromPtr(_id)


from spock import Obligation, Now
from spock.doctrine import TemporalDoctrine

alice = object()
bob   = object()
obl   = Obligation(alice, bob, Now, lambda:42)
t = TemporalDoctrine()
t.obligation(obl)
commitment = t.commitments[alice].items()[0]
_to, obligations = commitment
assert _to==bob,'obligation is to someone else?'
assert all([obligations,obligations[0]==obl]),'obligation is not the obligation?'

from IPython import Shell; Shell.IPShellEmbed(argv=['-noconfirm_exit'])()
