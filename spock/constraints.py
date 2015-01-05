""" spock.constraints
"""
from spock.aima.logic import *
from spock.aima import CSP, backtracking_search

class InconsistentConstraints(Exception): pass

class BootOrderProblem(object):
    """ solves the "boot order" problem, aka dependency consistency, etc.
        this class is just a more convenient interface aima's CSP
    """
    InconsistentConstraints = InconsistentConstraints

    def __init__(self, constraint_table, csp_algorithm=None):
        self.table=constraint_table
        self.csp_algorithm = csp_algorithm or backtracking_search

    def _boot_order_constraint(self, s1, boot_order1, s2, boot_order2):
        """ returns True iff (s1, s2) satisfy the constraint when they
            have boot-orders boot_order1 and boot_order2 respectively
        """
        # because all boot orders should be unique
        if boot_order1==boot_order2:
            return False

        # figure out which service is first
        first, second = (s1, s2) if (boot_order1 < boot_order2) else (s2, s1)

        # ensure the second isn't in the first's  table of dependancies
        return (second not in self.table[first])

    @property
    def neighbors(self):
        """ every service participates in the
            constraints of the other selfs except
            itself
        """
        return dict([ [service, [service2 for service2 in self.vars if \
                                 service2!=service] ] for service in self.vars ])

    @property
    def vars(self):
        """ variables this csp solves over """
        return self.table.keys()

    @property
    def domains(self):
        """ every service could potentially be booted in any order """
        return dict([ [service, range(len(self.vars))] for service in self.vars])

    def __call__(self):
        """ computes problem solution """
        # compute solution
        self.csp_problem = CSP(self.vars, self.domains,
                               self.neighbors, self._boot_order_constraint)
        answer         = self.csp_algorithm(self.csp_problem)
        if answer is None:
            raise InconsistentConstraints(self.table)
        else:
            # clean up the answer before we return it.  by default
            # it will be a dictionary of {service_name : boot_order},
            # but boot_order's may be duplicated, and it may not be
            # in order.  we simply return a list of variable names
            # that is guaranteed to be consistent.
            answer = answer.items()
            answer.sort(lambda x,y: cmp(x[1], y[1]))
            return [ x[0] for x in answer ]

if __name__=='__main__':
    print BootOrderProblem({1:[2,3],2:[1],3:[]},)()
    from IPython import Shell; Shell.IPShellEmbed(argv=['-noconfirm_exit'])()
