""" spock

    logic programming for python
"""
from .version import __version__
from spock.simplex import Expression, predicate, symbol, s
from spock.doctrine import Doctrine
from spock.obligations import Obligation, Decision
from spock.constraints import BootOrderProblem
