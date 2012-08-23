What is this?
-------------

Python library for logic.  This is not intended to be a complete implementation and
at this point it is certainly not written to be very fast.  It's mainly an experiment
and might be useful to someone as a reference.  The code for first order logic is stolen
directly from Norvig's "AI: A Modern Approach", with a few improvements to make it more
pythonic.

Supports:

  - First Order Logic [via AI:MA]
  - Agent logic (obligations, decisions) [following Shoham '94]
  - Temporal logic (very crude, very in-progress)

Wishlist:

  - Paraconsistent Logic [maybe following LFI1: A 3-valued Logic for Formal Inconsistency]

Examples
--------

  TODO: adapt from http://staff.washington.edu/jon/flip/www/witch.html


Running tests
-------------

after cloning the repository, simply run::

  $ python lib/spock/tests

Related Reading and Software
----------------------------
LFI1: http://www.deamo.prof.ufu.br/arquivos/FLAIRS05AmoS.pdf

FLIP: a logic framework in python
http://staff.washington.edu/jon/flip/

theorem prover example:
http://www.blog.everythings-beta.com/?p=57
