What is this?
-------------

``Spock`` is a python library for logic.  This is not intended to be a complete implementation
and at this point it is certainly not written to be very fast.  It's mainly an experiment
and might be useful to someone as a reference.

The backend codes for first order logic are mostly stolen from Russel & Norvig's
"AI: A Modern Approach", and even the approach there is only intended to be illustrative
rather than industrial strength.  That code illustrates logic pretty well, but illustrates
*logic in python* pretty poorly.  ``Spock`` includes some improvements that make it more
pythonic.  I've also fixed what bugs I found, and implemented stuff that the margins were
originally too narrow to contain (e.g. WalkSAT).

Spock Supports::

  - First Order Logic [via AI:MA]
  - Agent logic (obligations, decisions) [following Shoham '94]
  - Temporal logic (very crude, very in-progress)

Wishlist::

  - Paraconsistent Logic [maybe following LFI1: A 3-valued Logic for Formal Inconsistency]

Examples
--------


  TODO: adapt more from nice pythonic http://staff.washington.edu/jon/flip/www/witch.html ?


Installation
-------------

You'll need virtualenv and pip already installed, then run::

  $ git clone http://github.com/mattvonrocketstein/spock.git
  $ cd spock
  $ virtualenv spock_test
  $ source spock_test/bin/activate
  $ python setup.py develop

Running tests
-------------

Type this::

  $ cd spock
  $ virtualenv spock_test
  $ source spock_test/bin/activate
  $ pip install pytest
  $ pytest -v -t lib/spock/tests

Related Reading and Software
----------------------------
  * LFI1: http://www.deamo.prof.ufu.br/arquivos/FLAIRS05AmoS.pdf
  * FLIP: a logic framework in python http://staff.washington.edu/jon/flip/
  * logic.py: http://truxler.net/robgfx/images/logic/tech_report.pdf
  * theorem prover example: http://www.blog.everythings-beta.com/?p=57
  * python bindings for a STP (a fast constraint-solving library) http://security.dico.unimi.it/~roberto/pystp/
  * HigherOrderLogic, a classic, and a good collection of related links http://www.cl.cam.ac.uk/research/hvg/HOL/history.html
