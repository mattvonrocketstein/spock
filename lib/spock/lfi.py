""" spock.lfi

    Implementing logics for formal inconsistency.

    http://sqig.math.ist.utl.pt/pub/MarcosJ/01-CM-tableaux.pdf
"""

class Operator(object):
    def __init__(self, table):
        self.table = {}
        for args, result in table:
            self.table[tuple(args)]=result

    @property
    def arity(self):
        return len(self.table[0][0])

    def __call__(self, *args):
        return self.table[args]

class CommutingOperator(Operator):
    def __call__(self, *args):
        sooper = super(CommutingOperator, self).__call__
        try:
            return sooper(*args)
        except KeyError:
            args = list(args)
            args.reverse()
            return sooper(*args)

negative_by_default = Operator([
    [['t'],'f'],
    [['i'],'f'],
    [['f'],'t'],
    [['u'],'u'],
    ])

_and = CommutingOperator([
    [['t', 't'], 't'],
    [['t', 'i'], 'i'],
    [['t', 'f'], 'f'],
    [['i', 'i'], 'i'],
    [['u', 'u'], 'u'],
    [['u', 't'], 'u'],
    [['u', 'i'], 'u'],
    [['u', 'f'], 'f'],
    [['f', 'f'], 'f'],
    [['f', 'i'], 'f'], ])

_arrow = Operator([
    [ ['t','t'], 't'],
    [ ['t','i'], 'f'],
    [ ['t','u'], 'f'],
    [ ['t','f'], 'f'],
    [ ['i','t'], 'i'],
    [ ['i','i'], 'i'],
    [ ['i','u'], 'f'],
    [ ['i','f'], 'f'],
    [ ['u','t'], 't'],
    [ ['u','i'], 't'],
    [ ['u','u'], 't'],
    [ ['u','f'], 'f'],
    [ ['f','t'], 't'],
    [ ['f','i'], 't'],
    [ ['f','u'], 't'],
    [ ['f','f'], 't'],
    ])
_or = CommutingOperator([
    [['t', 't'], 't'],
    [['t', 'u'], 't'],
    [['i', 'i'], 'i'],
    [['u', 'i'], 'i'],
    [['u', 'f'], 'u'],
    [['t', 'f'], 't'],
    [['t', 'i'], 't'],
    [['f', 'f'], 'f'],
    [['f', 'i'], 'i'], ])
