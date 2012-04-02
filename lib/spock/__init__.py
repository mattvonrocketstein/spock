""" spock: logic programming for python
"""

from spock.simplex import Expression, predicate, symbol, s
from spock.doctrine import Doctrine

class Time(object): pass
class Now(Time): pass
class Always(Time): pass

class theta(object):
    """ an expression true at a time """
    def __init__(self, expression=None, time=None):
        self.expression = expression
        self.time = time

    def __str__(self):
        return "({code} @ {t})".format(code=str(self.expression), t=self.time)

class Obligation(theta):
    """ Following Shoham:'94, an obligation is a 4-tuple
        representing a directed commitment from alfa to beta
        about gamma at theta.  Typical conceptions about these
        data structures follows, but, for flexibility, not much
        along these lines is actually enforced.

           * Theta is a specific time or a value like "always" or "never"
           * Gamma is usually an "action"
           * Alfa and beta are usually "agents",
    """
    def __init__(self, alfa, beta, theta, gamma):
        self.expression = predicate.Obligation(s[alfa], s[beta], s[gamma])
        self.expression.alfa = alfa
        self.expression.beta = beta
        self.expression.gamma = gamma
        self.alfa, self.beta, self.gamma = alfa, beta, gamma
        super(Obligation,self).__init__(expression=self.expression, time=theta)

class Decision(Obligation):
    """ Following Shoham:'94, a decision is an obligation to onself """
    def __init__(self, myself, theta, gamma):
        super(Obligation,self).__init__(myself, myself, theta, gamma)
