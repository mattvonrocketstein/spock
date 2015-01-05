""" spock.test.test_belief
"""
import time
import unittest2 as unittest
from datetime import datetime
from spock.belief import always, never, Belief, BadBelief

class TestBelief(unittest.TestCase):
    def setUp(self):
        obj = self.obj = object()
        self.always = Belief(ctx=True, at=always, about=obj)
        self.never = Belief(ctx=True, at=never, about=obj)

    def test_always(self):
        self.assertTrue(self.always.holds())
        self.assertTrue(self.always.holds_when(datetime.now()))

    def test_never(self):
        self.assertFalse(self.never.holds())
        self.assertFalse(self.never.holds_when(datetime.now()))

    def test_bad_declaration_empty_interval(self):
        bad1 = lambda: Belief(ctx=True, at=[], about=self.obj)
        self.assertRaises(BadBelief,bad1 )

    def test_bad_declaration_nil_interval(self):
        bad1 = lambda: Belief(ctx=True, at=None, about=self.obj)
        self.assertRaises(BadBelief, bad1)

    def test_bad_declaration_nonsense_interval(self):
        t1 = datetime.now()
        time.sleep(.25)
        t2 = datetime.now()
        #wrong because t2 comes after t2
        bad1 = lambda: Belief(ctx=True, at=[t2, t1], about=self.obj)
        bad2 = lambda: Belief(ctx=True, starting=t2, ending=t1, about=self.obj)
        self.assertRaises(BadBelief, bad1)
        # but.. this should work
        Belief(ctx=True, at=[t1, t2], about=self.obj)
        Belief(ctx=True, starting=t1, ending=t2, about=self.obj)
