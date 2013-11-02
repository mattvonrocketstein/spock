""" spock.tests.test_ambients
"""
import unittest2 as unittest

from spock.ambients  import Ambient, ambient_args

class TestTestDecorators(unittest.TestCase):
    def setUp(self):
        self.ambient = Ambient()

    def test_with_ambients(self):
        tmp = ambient_args(lambda x: x)
        tmp(self.ambient)

    def test_with_non_ambients(self):
        tmp = ambient_args(lambda x: x)
        self.assertRaises(ambient_args.ArgTypeError, lambda: tmp(1))

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
