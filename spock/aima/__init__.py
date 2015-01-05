""" spock.aima

    This package spock.aima includes various improvements on the AI:MA source code,
    primarily along the lines of

     1) implementing  things that were left as an exercise to the reader,
     2) updating idioms from the original code that are now old style
     3) moves doctests and examples to a proper test suite,
     4) provides a more pythonic interface whenever possible,
     5) and fixes bugs.

    The modules at spock.aima.* are more or less the original source code, but I
    tried to ensure that changes per file are always documented at the top of
    that file.

"""
from spock.aima.logic import *
from spock.aima.csp import CSP, backtracking_search
