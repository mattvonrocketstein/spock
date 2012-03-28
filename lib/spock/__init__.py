""" spock:

     logic for python
"""
from spock.aima import FolKB
from spock.simplex import Expression, predicate, symbol, s


class theta(object):
    """ an expression true at a time """
    def __init__(self, expression=None, time=None):
        self.ex = expression
        self.time = time
    def __str__(self):
        return "({code} @ {t})".format(code=str(self.ex), t=self.time)

class Obligation(theta):
    def __init__(self, a,b,t,j):
        " a is committed to b about j at time t "
        ex = predicate.Obligation(s[a], s[b], s[j])
        super(Obligation,self).__init__(ex, t)
class Doctrine(FolKB):
    """  a Doctrine is a collection of beliefs.

         ask(q)::
           returns the first answer or False

         ask_generator(q)::
           yields all solutions with all symbols/values
           combinations in their own dictionary.

         consider(q, [with-respect-to])::
           yields all solutions as a flattened value,
           with respect to variable specified by  `wrt`
    """

    def consider(self, proposition, wrt=None):
        """ see Doctirne.__doc__ """

        results = self.ask_generator(proposition)
        if wrt is not None:
            for x in results:
                yield x[wrt]
