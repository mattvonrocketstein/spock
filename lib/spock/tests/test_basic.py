""" spock.tests.test_basic
"""
import unittest2 as unittest
from types import GeneratorType

from spock.aima import Expr
from spock.simplex import Expression
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
        return self.assertTrue(any([isinstance(other, Expr),
                                    isinstance(other, Expression)]))
    def assertOpEqual(self, expr, name):
        return self.assertEqual(expr.op, name)

class BasicTests(Common):

    def setUp(self):
        super(Common, self).setUp()
        self.s1 = predicate.f(symbol.x, symbol.y)
        self.complex_sentence = self.s1 | symbol.y

    def test_simple(self):
        self.assertTrue(predicate.F.simple)
        self.assertTrue(symbol.x.simple)
        self.assertTrue(not predicate.F(symbol.x).simple)

    def test_solutions(self):
        self.assertEqual(symbol.x.solution,
                         [{'x':True}])
        x,y = symbol.x, symbol.y
        sol = (x|y).solution
        self.assertTrue(sol in
                        [ {x:True,y:False},
                          {y:True,x:False},
                           {x:True,y:True},] )

    def test_simple_decompose(self):
        sentence = self.complex_sentence
        components = sentence.decompose()
        self.assertEqual(components, [ self.s1, symbol.y ])

    def test_complex_decompose(self):
        blam = predicate.foo(symbol.a, symbol.b)
        sentence = self.complex_sentence | blam
        components = sentence.decompose()
        self.assertEqual(components,
                         [self.s1, symbol.y, blam])

    def test_implication_basic(self):
        z = ( is_farmer(Mac) & is_rabbit(Pete) >> \
              does_hate(Mac, Pete) )
        self.assertExpression(z)
