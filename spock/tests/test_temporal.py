""" spock.tests.test_temporal
"""
import datetime
import unittest2 as unittest
from types import GeneratorType

from spock.aima import Expr
from spock import (predicate, symbol, Obligation)
from spock.doctrine import TemporalDoctrine

s = symbol
now = datetime.datetime.now()


def obligation(time=now):
    """ `alice` promises `bob` a thing called `dinner` at time `t` """
    alice, bob, action = 'alice', 'bob', 'dinner'
    return Obligation(alice, bob, action, time)

class TestObligationSimple(unittest.TestCase):
    def setUp(self):
        self.o1 = obligation()
        self.o2 = obligation()
        self.o3 = obligation(datetime.datetime.now())

    def test_obligation_equality(self):
        self.assertTrue(self.o1 == self.o2)
        self.assertFalse(self.o1 == self.o3)

    def test_obligation_basic(self):
        self.assertTrue(self.o1.expression.alfa == 'alice' == self.o1._from)
        self.assertTrue(self.o1.expression.beta == 'bob' == self.o1._to)
        self.assertTrue(self.o1.theta == now)
        self.assertTrue(self.o1.gamma=='dinner')


class TemporalTests(unittest.TestCase):

    def setUp(self):
        self.kb = TemporalDoctrine()

    def test_commitments(self):
        obl = obligation()
        alice, bob = obl.alfa, obl.beta
        self.kb.obligation(obl)
        alice_commitments = self.kb.commitments[alice]
        self.assertTrue(bob in alice_commitments.keys())
        self.assertTrue(obl in alice_commitments[bob])
