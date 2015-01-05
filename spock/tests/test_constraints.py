""" spock.tests.test_constraints
"""
import unittest2 as unittest
from spock.constraints import BootOrderProblem
from spock.aima.csp import backtracking_search, CSP, parse_neighbors

class TestConstraints(unittest.TestCase):
    """ tests for the unique spock code """
    def test_solvable_boot_order_problem(self):
        # 2 must boot before 1 must boot before 3.  3 has no dependency
        self.assertEqual([3,2,1],BootOrderProblem({1:[2], 2:[3], 3:[]})())

    def test_unsolvable_boot_order_problem(self):
        # no solution: 2 must boot before 1, but 1 must boot before 2.
        self.assertRaises(BootOrderProblem.InconsistentConstraints,
                          BootOrderProblem({1:[2], 2:[1]}),)

class TestAIMA(unittest.TestCase):
    ZEBRA_SOLUTION = {'Blue': 2, 'Chesterfields': 2, 'Coffee': 5,
                      'Dog': 4, 'Englishman': 3, 'Fox': 1,
                      'Green': 5, 'Horse': 2, 'Ivory': 4,
                      'Japanese': 5, 'Kools': 1, 'LuckyStrike': 4,
                      'Milk': 3, 'Norwegian': 1, 'OJ': 4,
                      'Parliaments': 5, 'Red': 3, 'Snails': 3,
                      'Spaniard': 4, 'Tea': 2, 'Ukranian': 2,
                      'Water': 1, 'Winston': 3, 'Yellow': 1,
                      'Zebra': 5}

    def test_zebra(self):
        # this problem is not easy and the test may take several seconds.
        self.assertEqual(backtracking_search(Zebra()),
                         self.ZEBRA_SOLUTION)
def Zebra():
    "Return an instance of the Zebra Puzzle."
    Colors = 'Red Yellow Blue Green Ivory'.split()
    Pets = 'Dog Fox Snails Horse Zebra'.split()
    Drinks = 'OJ Tea Coffee Milk Water'.split()
    Countries = 'Englishman Spaniard Norwegian Ukranian Japanese'.split()
    Smokes = 'Kools Chesterfields Winston LuckyStrike Parliaments'.split()
    vars = Colors + Pets + Drinks + Countries + Smokes
    domains = {}
    for var in vars:
        domains[var] = range(1, 6)
    domains['Norwegian'] = [1]
    domains['Milk'] = [3]
    neighbors = parse_neighbors("""Englishman: Red;
                Spaniard: Dog; Kools: Yellow; Chesterfields: Fox;
                Norwegian: Blue; Winston: Snails; LuckyStrike: OJ;
                Ukranian: Tea; Japanese: Parliaments; Kools: Horse;
                Coffee: Green; Green: Ivory""", vars)
    for type in [Colors, Pets, Drinks, Countries, Smokes]:
        for A in type:
            for B in type:
                if A != B:
                    if B not in neighbors[A]: neighbors[A].append(B)
                    if A not in neighbors[B]: neighbors[B].append(A)
    def zebra_constraint(A, a, B, b, recurse=0):
        same = (a == b)
        next_to = abs(a - b) == 1
        if A == 'Englishman' and B == 'Red': return same
        if A == 'Spaniard' and B == 'Dog': return same
        if A == 'Chesterfields' and B == 'Fox': return next_to
        if A == 'Norwegian' and B == 'Blue': return next_to
        if A == 'Kools' and B == 'Yellow': return same
        if A == 'Winston' and B == 'Snails': return same
        if A == 'LuckyStrike' and B == 'OJ': return same
        if A == 'Ukranian' and B == 'Tea': return same
        if A == 'Japanese' and B == 'Parliaments': return same
        if A == 'Kools' and B == 'Horse': return next_to
        if A == 'Coffee' and B == 'Green': return same
        if A == 'Green' and B == 'Ivory': return (a - 1) == b
        if recurse == 0: return zebra_constraint(B, b, A, a, 1)
        if ((A in Colors and B in Colors) or
            (A in Pets and B in Pets) or
            (A in Drinks and B in Drinks) or
            (A in Countries and B in Countries) or
            (A in Smokes and B in Smokes)): return not same
        raise 'error'
    return CSP(vars, domains, neighbors, zebra_constraint)
{'Blue': 2,
 'Chesterfields': 2,
 'Coffee': 5,
 'Dog': 4,
 'Englishman': 3,
 'Fox': 1,
 'Green': 5,
 'Horse': 2,
 'Ivory': 4,
 'Japanese': 5,
 'Kools': 1,
 'LuckyStrike': 4,
 'Milk': 3,
 'Norwegian': 1,
 'OJ': 4,
 'Parliaments': 5,
 'Red': 3,
 'Snails': 3,
 'Spaniard': 4,
 'Tea': 2,
 'Ukranian': 2,
 'Water': 1,
 'Winston': 3,
 'Yellow': 1,
 'Zebra': 5}
