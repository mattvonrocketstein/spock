""" spock.obligations
"""
import datetime

from spock.simplex import Expression, predicate, symbol, s

class Time(object): pass
class Now(Time): pass
class Always(Time): pass

class Theta(object):
    """ an expression true at a time """
    def __init__(self, expression=None, time=Time()):
        self.expression = expression
        self.time = time
        if not isinstance(time, (Time, datetime.datetime)):
            raise Exception,'Bad type for theta value'

    def __str__(self):
        return "({code} @ {t})".format(code=str(self.expression), t=self.time)

class Obligation(Theta):
    """
        Obligation(A,B,G,T) implies A is obligated to B re: G at T

        Following Shoham:'94, an obligation is a 4-tuple
        representing a directed commitment from alfa to beta
        about gamma at theta.  Typical conceptions about these
        data structures follows, but, for flexibility, not much
        along these lines is actually enforced.

           * Theta is a specific time or a value like "always" or "never"
           * Gamma is usually referred to as a "action"
           * Alfa and beta are usually "agents",

    """
    def __init__(self, alfa=None, beta=None, gamma=None, theta=None,):
        if any([theta is None,
                theta==Now,
                isinstance(theta, Now)]):
            theta = datetime.datetime.now()
        self.expression = predicate.Obligation(s[alfa], s[beta], s[gamma])
        self.alfa  = self.expression.alfa  = alfa
        self.beta  = self.expression.beta  = beta
        self.gamma = self.expression.gamma = gamma
        self.theta = self.expression.theta = theta
        super(Obligation, self).__init__(expression=self.expression, time=theta)

    def __eq__(self,other):
        #if isinstance(other, Obligation):
        components = 'alfa beta theta gamma'
        components = components.split()
        _a, _b, _t, _g = [ getattr(other, x, None) for x in components ]
        return all( [ self.alfa  == _a, self.beta  == _b,
                      self.gamma == _g, self.theta == _t ] )

    @property
    def _from(self):
        return self.alfa

    @property
    def _to(self):
        return self.beta


class Decision(Obligation):
    """ Following Shoham:'94, a decision is an obligation to onself """
    def __init__(self, myself, gamma, theta, ):
        super(Obligation,self).__init__(myself, myself, gamma, theta,)
