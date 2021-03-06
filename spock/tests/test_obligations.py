""" spock.tests.test_obligation

"""
from datetime import datetime, timedelta
import unittest2 as unittest
from types import GeneratorType
from spock import (predicate, symbol, Doctrine,)
from spock.doctrine import TemporalDoctrine
from spock.obligations import Obligation, Now, Always

from spock.tests.test_basic import Common
from spock.tests.test_basic import RABBIT_LOGIC, Mac, Pete

class John(object): pass
class Jane(object): pass

class ObligationTests(Common):
    def setUp(self):
        super(ObligationTests, self).setUp()
        # Whatever, actual expression doesnt matter
        self.expression = RABBIT_LOGIC[0]

    def test_alfa_beta(self):
        o = Obligation(John, Jane, self.expression)
        self.assertTrue(o.alfa, John)
        self.assertTrue(o.beta, Jane)

    def test_equality_positive(self):
        # different instances should be equal as long as the parts are equal
        o1 = Obligation(John, Jane, self.expression, Always)
        o2 = Obligation(John, Jane, self.expression, Always)
        self.assertTrue(o1 == o2)
        # .. but we don't cache instances
        self.assertTrue(id(o1) != id(o2))

    def test_equality_negative(self):
        # these instances should be unequal because times do not match exactly
        o1 = Obligation(John, Jane, self.expression, Now)
        o2 = Obligation(John, Jane, self.expression, Now)
        self.assertTrue(o1!=o2)

    def test_gamma(self):
        o = Obligation(John, Jane, self.expression)
        self.assertTrue(o.gamma, self.expression)

    def test_default_thetas(self):
        # when theta is not passed, or the pseudo value Now is used,
        # datetime.now() should be used.
        expression    = self.expression
        effective_min = timedelta(seconds=2)
        o1, now = Obligation(John, Jane, expression), datetime.now()
        self.assertTrue( (now-o1.theta) < effective_min )
        o2, now = Obligation(John, Jane, expression, Now), datetime.now()
        self.assertTrue( (now-o2.theta) < effective_min )
        o3, now = Obligation(John, Jane, expression, Now()), datetime.now()
        self.assertTrue( (now-o3.theta) < effective_min )


#def IDIntoObjectTransform(_id):
#    """ id into object transformer: idiot for short. """
#    import _ctypes
#    return _ctypes.PyObj_FromPtr(_id)
