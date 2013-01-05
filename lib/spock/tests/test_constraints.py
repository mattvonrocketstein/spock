""" spock.tests.test_constraints
"""
import unittest2 as unittest
from spock.aima import BootOrderProblem

class TestConstraints(unittest.TestCase):
    def test_solvable_boot_order_problem(self):
        # 2 must boot before 1 must boot before 3.  3 has no dependency
        self.assertEqual([3,2,1],BootOrderProblem({1:[2], 2:[3], 3:[]})())

    def test_unsolvable_boot_order_problem(self):
        # no solution: 2 must boot before 1, but 1 must boot before 2.
        self.assertRaises(BootOrderProblem.InconsistentConstraints,
                          BootOrderProblem({1:[2], 2:[1]}),)
