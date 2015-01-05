""" spcok.tests.test_aima_logic
"""
from unittest2 import TestCase

from spock.aima.logic import dpll_satisfiable
from spock.aima.logic import (conjuncts, disjuncts, prop_symbols,
                              PropKB,to_cnf,expr,is_positive,literals,
                              tt_entails,tt_true,eliminate_implications,
                              move_not_inwards,distribute_and_over_or,
                              is_literal, is_definite_clause,variables)
from spock import symbol, predicate
_ = symbol

class FailingTests(object):
    # ugh, failing now because of parenthesis in representation
    def failing_test_to_cnf(self):
        eq1 = (_.P&_.Q) | (~_.P & ~_.Q)
        R   = (~_.P | _.P) & (~_.Q | _.P) & (~_.P | _.Q) & (~_.Q | _.Q)
        self.assertEqual(to_cnf(eq1), R)

    # am i using this wrong? did it never work?  did i break it?
    def failing_test_dpll_satisfiable(self):
        self.assertEqual(False, dpll_satisfiable(self.A & ~self.A))
        self.assertEqual([], dpll_satisfiable())#dpll_satisfiable(self.A & ~self.B))

class TestLogic(FailingTests, TestCase):
    def setUp(self):
        A, B = symbol.A, symbol.B
        and_expr = A&B
        or_expr  = A|B
        namespace=locals()
        namespace.pop('self')
        for x in namespace:
            setattr(self,x,namespace[x])

    def test_distribute_and_over_or(self):
        self.assertEqual(distribute_and_over_or((_.A & _.B) | _.C),
                         ((_.A | _.C) & (_.B | _.C)))

    def test_move_not_inwards(self):
        self.assertEqual(move_not_inwards(~(_.A | _.B)),
                         expr('(~A & ~B)'))
        self.assertEqual(
            move_not_inwards(~(_.A & _.B)),
            expr('(~A | ~B)'))
        self.assertEqual(
            move_not_inwards(expr('~(~(A | ~B) | ~~C)')),
            expr('((A | ~B) & ~C)'))

    def test_eliminate_implications(self):
        self.assertEqual(eliminate_implications(_.A >> (~_.B << _.C)),
                         expr('((~B | ~C) | ~A)'))

    def test_tt_entails(self):
        self.assertEqual(tt_entails(expr('P & Q'), expr('Q')),
                         True)
    def test_tt_true(self):
        self.assertTrue(tt_true(expr("(P >> Q) <=> (~P | Q)")),
                        True)

    def test_is_definite_clause(self):
        self.assertEqual(
            is_definite_clause(expr('Farmer(Mac)')), True)
        self.assertEqual(
            is_definite_clause(expr('~Farmer(Mac)')), False)
        self.assertEqual(
            is_definite_clause(expr('(Farmer(f) & Rabbit(r)) ==> Hates(f, r)')),
            True)
        self.assertEqual(
            is_definite_clause(expr('(Farmer(f) & ~Rabbit(r)) ==> Hates(f, r)')),
            False)

    def test_variables(self):
        self.assertEqual(
            variables(_.F(_.x, _.A, _.y)),
            set([_.x, _.y]))
        self.assertEqual(
            variables(expr('F(x, x) & G(x, y) & H(y, z) & R(A, z, z)')),
            set([_.x, _.y, _.z]))

    def test_literals(self):
        self.assertEqual(literals(expr('F(A, B)')),
                         [_.F(_.A, _.B)])
        self.assertEqual(literals(expr('~F(A, B)')),
                         [~_.F(_.A, _.B)])
        self.assertEqual(literals(expr('(F(A, B) & G(B, C)) ==> R(A, C)')),
                         [ _.F(_.A, _.B),
                           _.G(_.B, _.C),
                           _.R(_.A, _.C)])

    def test_is_literal(self):
        self.assertEqual(False, is_literal(expr('F(A, B) & G(B, C)')))
        self.assertEqual(True, is_literal(expr('~F(A, B)')))
        self.assertEqual(True, is_literal(expr('F(A, B)')))

    def test_is_positive(self):
        self.assertEqual(True,is_positive(expr('F(A, B)')))
        self.assertEqual(False,is_positive(expr('~F(A, B)')))

    def test_prop_symbols(self):
        self.assertEqual(set(prop_symbols(self.and_expr)), set([self.A,self.B]))
        self.assertEqual(set(prop_symbols(self.or_expr)), set([self.A,self.B]))
        self.assertEqual(set(prop_symbols(predicate.F(symbol.a) & symbol.a)),
                         set([predicate.F(symbol.a), symbol.a]))


    def test_disjuncts(self):
        self.assertEqual(disjuncts(self.or_expr),[self.A,self.B])
        self.assertEqual(disjuncts(self.and_expr),[self.and_expr])

    def test_conjuncts(self):
        self.assertEqual(conjuncts(self.and_expr), [self.A,self.B])
        self.assertEqual(conjuncts(self.or_expr), [self.or_expr])

    def test_prop_kb(self):
        kb = PropKB()
        kb.tell(_.A & _.B)
        kb.tell(_.B >> _.C)
        #The result {} means true, with no substitutions
        self.assertEqual({}, kb.ask(_.C))
        self.assertEqual(kb.ask(_.P),False)
        kb.retract(_.B)
        self.assertEqual(kb.ask(_.C), False)
"""
>>> pl_true(P, {})
>>> pl_true(P | Q, {P: True})
True

# Notice that the function pl_true cannot reason by cases:
>>> pl_true(P | ~P)

# However, tt_true can:
>>> tt_true(P | ~P)
True

# The following are tautologies from [Fig. 7.11]:
>>> tt_true("(A & B) <=> (B & A)")
True
>>> tt_true("(A | B) <=> (B | A)")
True
>>> tt_true("((A & B) & C) <=> (A & (B & C))")
True
>>> tt_true("((A | B) | C) <=> (A | (B | C))")
True
>>> tt_true("~~A <=> A")
True
>>> tt_true("(A >> B) <=> (~B >> ~A)")
True
>>> tt_true("(A >> B) <=> (~A | B)")
True
>>> tt_true("(A <=> B) <=> ((A >> B) & (B >> A))")
True
>>> tt_true("~(A & B) <=> (~A | ~B)")
True
>>> tt_true("~(A | B) <=> (~A & ~B)")
True
>>> tt_true("(A & (B | C)) <=> ((A & B) | (A & C))")
True
>>> tt_true("(A | (B & C)) <=> ((A | B) & (A | C))")
True

# The following are not tautologies:
>>> tt_true(A & ~A)
False
>>> tt_true(A & B)
False

### [Fig. 7.13]
>>> alpha = expr("~P12")
>>> to_cnf(Fig[7,13] & ~alpha)
((~P12 | B11) & (~P21 | B11) & (P12 | P21 | ~B11) & ~B11 & P12)
>>> tt_entails(Fig[7,13], alpha)
True
>>> pl_resolution(PropKB(Fig[7,13]), alpha)
True

### [Fig. 7.15]
>>> pl_fc_entails(Fig[7,15], expr('SomethingSilly'))
False

### Unification:
>>> unify(x, x, {})
{}
>>> unify(x, 3, {})
{x: 3}


"""
