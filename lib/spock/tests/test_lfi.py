"""
"""
from unittest2 import TestCase

def xcombinations(items, n):
    if n==0: yield []
    else:
        for i in xrange(len(items)):
            for cc in xcombinations(items[:i]+items[i+1:],n-1):
                yield [items[i]]+cc

def xuniqueCombinations(items, n):
    if n==0: yield []
    else:
        for i in xrange(len(items)):
            for cc in xuniqueCombinations(items[i+1:],n-1):
                yield [items[i]]+cc

def xselections(items, n):
    if n==0: yield []
    else:
        for i in xrange(len(items)):
            for ss in xselections(items, n-1):
                yield [items[i]]+ss

def xpermutations(items):
    return xcombinations(items, len(items))

class Test(TestCase):
    def setUp(self):
        self.data = xcombinations(list('tifu'), 2)

    def test_arriw(self):
        [ _arrow(*x) for x in self.data ]

    def test_and(self):
        [ _and(*x) for x in self.data ]

    def test_or(self):
        [ _or(*x) for x in self.data ]
