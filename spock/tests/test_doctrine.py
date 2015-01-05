""" spock.tests.test_doctrine
"""
import unittest2 as unittest
from types import GeneratorType
from spock import (predicate, symbol, Doctrine,)
from spock.doctrine import TemporalDoctrine
from spock.obligations import Obligation, Always

# (1) base classes, (2) rules, and symbols (3) predicates
from spock.tests.test_basic import Common
from spock.tests.test_basic import RABBIT_LOGIC, Mac, Pete
from spock.tests.test_basic import does_hate, is_wife, is_rabbit

class DoctrineTests(Common):
    def setUp(self):
        super(DoctrineTests, self).setUp()
        self.kb0 = Doctrine( RABBIT_LOGIC )

    def test_disallow_duplicate_sentences(self):
        self.kb0.tell(predicate.is_sandwich(symbol.panini))
        try:
            self.kb0.tell(predicate.is_sandwich(symbol.panini))
        except self.kb0.DuplicateSentence:
            pass
        else:
            self.fail("should have raised duplicate sentence error")

    def test_ask_with_one_result(self):
        someone_Mac_hates = self.kb0.ask(does_hate(Mac, symbol.x))[symbol.x]
        self.assertEqual(someone_Mac_hates, symbol.Pete)
        self.assertOpEqual(someone_Mac_hates, 'Pete')

    def test_ask_with_empty_results(self):
        empty = self.kb0.ask(is_wife(Pete, symbol.x))
        self.assertEqual(False, empty)

    def test_consider_with_several_results(self):
        self.kb0.tell(is_rabbit(symbol.Flopsie))
        all_solutions = self.kb0.consider(does_hate(Mac, symbol.x), symbol.x)
        self.assertTrue(isinstance(all_solutions, GeneratorType))
        all_solutions = [ z for z in all_solutions ]
        [ self.assertExpression(z) for z in all_solutions ]
        names = set([z.op for z in all_solutions ])
        self.assertEqual(set('Pete Flopsie'.split()), names)

class TemporalDoctrineTests(Common):
    def setUp(self):
        super(TemporalDoctrineTests, self).setUp()
        self.z = TemporalDoctrine()

    #def test_basic(self):
        #from IPython import Shell; Shell.IPShellEmbed(argv=['-noconfirm_exit'])()
