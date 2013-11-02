""" spock.tests.test_ambients
"""
import unittest2 as unittest
from spock.ambients  import Ambient

class TestAmbient(unittest.TestCase):
    def test_init(self):
        Ambient()
        Ambient(parent=None)
        Ambient(parent=Ambient())

    def test_exit(self):
        pass

    def test_copy(self):
        self

    def test_open(self):
        pass

    def test_enter(self):
        pass
