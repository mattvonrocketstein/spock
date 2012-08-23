""" spock.tests.test_basic
"""
import unittest2 as unittest
from types import GeneratorType

from spock.aima import Expr
from spock import (predicate, symbol,
                   Obligation, Doctrine,)

# declare predicates, symbols, and simple rules
is_farmer = predicate.Farmer
is_rabbit = predicate.Rabbit
does_hate = predicate.Hates
is_wife   = predicate.Wife
Mac       = symbol.Mac
Pete      = symbol.Pete

RABBIT_LOGIC = [
    is_farmer(Mac),  # declare symbol `mac` is a farmer
    is_rabbit(Pete), # declare symbol `pete` is a rabbit

    # if `r` is a rabbit & `f` is a farmer, that implies `f` hates `r`
    ( is_rabbit(symbol.r) & is_farmer(symbol.f) ) >> does_hate(symbol.f, symbol.r)
    ]


class Common(unittest.TestCase):
    """ """
    def assertExpression(self,other):
        return self.assertTrue(isinstance(other, Expr))

    def assertOpEqual(self, expr, name):
        return self.assertEqual(expr.op, name)

class BasicTests(Common):
    def test_implication_basic(self):
        z = ( is_farmer(Mac) & is_rabbit(Pete) >> \
              does_hate(Mac, Pete) )
        self.assertExpression(z)
