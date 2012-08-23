""" spock.doctrine: extensions for aima's first order logic knowledge base
"""

from collections import defaultdict

from spock.aima import FolKB

class Doctrine(FolKB):
    """  a Doctrine is a collection of beliefs.

         tell(sentence)::
           stores a sentence in the knowledgebase.
           any duplicates will raise an exception.

         ask(sentence)::
           returns the first answer or False.

         ask_generator(sentence)::
           yields all solutions with all symbols/values
           combinations in their own dictionary.

         consider(q, [with-respect-to])::
           yields all solutions as a flattened value,
           with respect to variable specified by  `wrt`
    """

    class DuplicateSentence(ValueError):
        pass

    def tell(self, sentence):
        # by default, FolKB allows duplicate sentences.
        if sentence in self.clauses:
            raise self.DuplicateSentence(str(sentence))
        else:
            return FolKB.tell(self, sentence)

    def consider(self, proposition, wrt=None):
        """ see Doctirne.__doc__ """
        results = self.ask_generator(proposition)
        if wrt is not None:
            for x in results:
                yield x[wrt]

class TemporalDoctrine(defaultdict):
    """ very crude temporal logic: we store multiple subdoctrines for
        every single time that is referenced.

        TODO: how best to make this work simultaneously in a way that is
              similar to a Doctrine subclass?  make tell() work with `Always`
              as a default?  etc.
    """
    @property
    def commitments(self):
        class TMP:
            """ """
            def __getitem__(himself, x):
                """ returns { beta : obligation }
                    actually obligation here is an expression representing that
                    obligation, and not an obligation
                """
                from spock import Obligation
                results = defaultdict(lambda:[])
                for t,doctrine in self.items():
                    clauses = filter(lambda clause: \
                                     all([clause.op=='Obligation',
                                          getattr(clause,'alfa', None)==x]),
                                     doctrine.clauses)
                    for clause in clauses:
                        obl = Obligation(alfa=clause.alfa, beta=clause.beta,
                                   theta=clause.theta, gamma=clause.gamma)
                        #clause.time = t
                        results[clause.beta].append(obl)
                return dict(results)
        return TMP()

    def __init__(self):
        super(TemporalDoctrine,self).__init__(lambda:Doctrine())

    def obligation(self, obl):
        self[obl.time].tell(obl.expression)
        print 'stored'
