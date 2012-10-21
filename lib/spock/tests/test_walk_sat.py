""" spock.tests.test_walk_sat

    WalkSat exists in the original AIMA code but the implementation was incomplete
"""
import unittest2 as unittest
from spock import (predicate, symbol, Doctrine,)
from spock.doctrine import TemporalDoctrine
from spock.obligations import Obligation, Always

from spock.tests.test_basic import Common
from spock.tests.test_basic import RABBIT_LOGIC, Mac, Pete
from spock.tests.test_basic import does_hate, is_wife, is_rabbit
from spock.aima import WalkSAT

problems = {
    symbol.x & symbol.y: [ dict(x=True, y=True) ],
    symbol.x | symbol.y: [ dict(x=True, y=True),
                           dict(x=False, y=True),
                           dict(x=True, y=False), ],
    symbol.x & ~symbol.x : [None]

}

class WalkSATTests(unittest.TestCase):
    def test_all(self):
        for problem, solution_set in problems.items():
            computed = WalkSAT([problem])
            if computed: # answer might be None
                computed = dict( [ [ex.op, computed[ex]] for ex in computed ])
            self.assertTrue(computed in solution_set)
