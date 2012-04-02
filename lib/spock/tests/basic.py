""" spock.tests.stuff
"""
import unittest2 as unittest
from types import GeneratorType

from spock.aima import Expr
from spock import (predicate, symbol,
                   Obligation, Doctrine,)

s = symbol

class Common(unittest.TestCase):
    """ """
    def assertExpression(self,other):
        return self.assertTrue(isinstance(other, Expr))
    def assertOpEqual(self, expr, name):
        return self.assertEqual(expr.op, name)

    def setUp(self):
        self.Farmer = predicate.Farmer
        self.Rabbit = predicate.Rabbit
        self.Hates  = predicate.Hates
        self.Wife  = predicate.Wife
        self.Mac = symbol.Mac
        self.Pete = symbol.Pete

class BasicTests(Common):
    def test_implication_basic(self):
        z = ( self.Farmer(self.Mac) & self.Rabbit(self.Pete) >> \
              self.Hates(self.Mac, self.Pete) )
        self.assertExpression(z)

class DoctrineTests(Common):
    def test_doctrine_basic(self):
        kb0 = Doctrine( [ self.Farmer(self.Mac),
                          self.Rabbit(self.Pete),
                          ( self.Rabbit(s.r) &
                            self.Farmer(s.f) ) >>
                          self.Hates(s.f, s.r) ] )
        kb0.tell(self.Rabbit(s.Flopsie))

        result = kb0.ask(self.Hates(self.Mac, s.x))[s.x]
        self.assertOpEqual(result, 'Pete')

        result = kb0.ask(self.Wife(self.Pete, s.x))
        self.assertTrue(not result)

        all_solutions = kb0.consider(self.Hates(self.Mac, s.x), s.x)
        self.assertTrue(isinstance(all_solutions,GeneratorType))
        all_solutions = [z for z in all_solutions]
        [ self.assertExpression(z) for z in all_solutions ]
        names = set([z.op for z in all_solutions ])
        self.assertEqual(set('Pete Flopsie'.split()), names)
