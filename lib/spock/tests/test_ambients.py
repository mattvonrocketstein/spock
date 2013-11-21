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

class PacketTestCase(unittest.TestCase):
    """ taken from papers/AmbientLogic.pdf

        For example the process:

          a[p[out a. in b. <m>]] | b[open p. (n). n[]]

        represents a packet p that travels out of host a and
        into host b, where it is opened, and its contents m
        are read and used to create a new ambient. The process
        reduces in four steps (illustrating each of the four
        reduction rules) to the residual process:

          a[] | b[m[]].
    """
    def setUp(self):
        self.a = Ambient()
        self.b = Ambient()


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
