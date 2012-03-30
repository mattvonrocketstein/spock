""" spock.doctrine: extensions for aima's first order logic knowledge base
"""

from collections import defaultdict

from spock.aima import FolKB

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

class TemporalDoctrine(defaultdict):
    """ crude temporal logic: store multiple subdoctrines for any
        times that are referenced.
    """
    @property
    def commitments(self):
        class TMP:
            def __getitem__(himself, x):
                """ returns { beta : obligation } """
                results = defaultdict(lambda:[])
                for t,doctrine in self.items():
                    clauses = filter(lambda clause: \
                                     all([clause.op=='Obligation',
                                          getattr(clause,'alfa')==x]),
                                     doctrine.clauses)
                    for clause in clauses:
                        clause.time = t
                        results[clause.beta].append(clause)
                return dict(results)
        return TMP()

    def __init__(self):
        super(TemporalDoctrine,self).__init__(lambda:Doctrine())

    def obligation(self, obl):
        self[obl.time].tell(obl.expression)
        print 'stored'
