""" spock.simplex
"""

from .aima import Expr, FolKB, expr, is_definite_clause

class Expression(Expr):
    """

    small improvements, extensions, and syntactic sugar for aima.logic
    expressions, including working with fewer strings, and fewer calls
    to Expr(), so it's more pythonic.

      e.g. this
        >>> is_definite_clause(expr('(Farmer(f) & Rabbit(r)) ==> Hates(f, r)'))

      becomes something more like this:
        >>> Farmer = predicate.Farmer; Rabbit=predicate.Rabbit; Hates = predicate.Hates
        >>> f = symbol.f; r = symbol.r
        >>> is_definite_clause(farmer(f) & Rabbit(r) >> Hates(f,r))

    """
    def decompose(self):
        """ TODO: use literals() """
        if self.simple:
            return [self]
        elif self.op.isalpha():
            return [self]
        else:
            out = []
            for x in self.args:
                out += x.decompose()
            return out

    @property
    def solution(self):
        """ NB: nondeterministic! no guarantee you get the same solution each time """
        # TODO: caching
        if self.simple:
            return [ {self.op : True} ]
        else:
            from spock.aima.logic import WalkSAT
            return WalkSAT([self])

    @property
    def simple(self):
        # TODO: use is_literal() instead?
        # TODO: increasingly bad module name
        return not self.args

class _tmp(object):
    """ dumb helper to work with fewer strings"""
    def __getattr__(self, name):
        return Expression(name)

class symbol(_tmp):
    def __getitem__(self, x):
        '''convert x into a symbol'''
        # TODO: better docs
        return id(x)
class predicate(_tmp): pass

predicate = predicate()
symbol    = symbol()
p = P = predicate
s = S = symbol
