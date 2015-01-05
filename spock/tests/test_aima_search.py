""" spock.tests.test_aima_search
"""
import unittest2 as unittest

from spock.aima.search import UndirectedGraph, compare_searchers, GraphProblem, boggle_hill_climbing
from spock.aima.search import (
    breadth_first_graph_search, breadth_first_tree_search,
    depth_limited_search, depth_first_graph_search,
    depth_first_tree_search, iterative_deepening_search, astar_search)

romania = UndirectedGraph(dict(
        A=dict(Z=75, S=140, T=118),
        B=dict(U=85, P=101, G=90, F=211),
        C=dict(D=120, R=146, P=138),
        D=dict(M=75), E=dict(H=86),
        F=dict(S=99), H=dict(U=98),
        I=dict(V=92, N=87), L=dict(T=111, M=70),
        O=dict(Z=71, S=151), P=dict(R=97),
        R=dict(S=80), U=dict(V=142)))

romania.locations = dict(
    A=( 91, 492),    B=(400, 327),    C=(253, 288),   D=(165, 299),
    E=(562, 293),    F=(305, 449),    G=(375, 270),   H=(534, 350),
    I=(473, 506),    L=(165, 379),    M=(168, 339),   N=(406, 537),
    O=(131, 571),    P=(320, 368),    R=(233, 410),   S=(207, 457),
    T=( 94, 410),    U=(456, 350),    V=(509, 444),   Z=(108, 531))

australia = UndirectedGraph(dict(
    T=dict(), SA=dict(WA=1, NT=1, Q=1, NSW=1, V=1),
    NT=dict(WA=1, Q=1), NSW=dict(Q=1, V=1)))

australia.locations = dict(WA=(120, 24), NT=(135, 20), SA=(135, 30),
                           Q=(145, 20), NSW=(145, 32), T=(145, 42), V=(145, 37))


def compare_graph_searchers():
    """Prints a table of results like this:
Searcher                     Romania(A,B)         Romania(O, N)        Australia
breadth_first_tree_search    <  21/  22/  59/B>   <1158/1159/3288/N>   <   7/   8/  22/WA>
breadth_first_graph_search   <  10/  19/  26/B>   <  19/  45/  45/N>   <   5/   8/  16/WA>
depth_first_graph_search     <   9/  15/  23/B>   <  16/  27/  39/N>   <   4/   7/  13/WA>
iterative_deepening_search   <  11/  33/  31/B>   < 656/1815/1812/N>   <   3/  11/  11/WA>
depth_limited_search         <  54/  65/ 185/B>   < 387/1012/1125/N>   <  50/  54/ 200/WA>
astar_search                 <   3/   4/   9/B>   <   8/  10/  22/N>   <   2/   3/   6/WA>  """
    compare_searchers(problems=[GraphProblem('A', 'B', romania),
                                GraphProblem('O', 'N', romania),
                                GraphProblem('Q', 'WA', australia)],
            header=['Searcher', 'Romania(A,B)', 'Romania(O, N)', 'Australia'])

class TestSearch(unittest.TestCase):
    def setUp(self):
        self.ab = GraphProblem('A', 'B', romania)

    def test_bfirst(self):
        self.assertEqual(breadth_first_graph_search(self.ab).state, 'B')

    def test_bfirst_tree(self):
        self.assertEqual(breadth_first_tree_search(self.ab).state, 'B')

    def test_dfirst(self):
        self.assertEqual(depth_first_graph_search(self.ab).state, 'B')

    def test_ideep(self):
        self.assertEqual(iterative_deepening_search(self.ab).state, 'B')

    def test_lsearch(self):
        self.assertEqual(depth_limited_search(self.ab).state, 'B')

    def test_astar(self):
        self.assertEqual(astar_search(self.ab).state, 'B')

    def test_astar_path(self):
        self.assertEqual(
            [node.state for node in astar_search(self.ab).path()],
            ['B', 'P', 'R', 'S', 'A'])

    def test_all(self):
        compare_graph_searchers()

    def broken_test_boggle_hill_climbing(self):
        x = boggle_hill_climbing('ABCDEFGHI', verbose=False)
        self.assertEqual(x, (['E', 'P', 'R', 'D', 'O', 'A', 'G', 'S', 'T'], 123))
