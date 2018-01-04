#!/usr/bin/python3

import unittest
import lca

class TestEuler(unittest.TestCase):

    def test_min_tree_size_one(self):
        t = lca.Tree([-1])
        t.build_euler_tour()
        self.assertEqual(t.euler_tour, [(0, 0)])

    def test_min_tree_size_two(self):
        t = lca.Tree([-1, 0])
        t.build_euler_tour()
        self.assertEqual(t.euler_tour, [(0, 0), (1, 1), (0, 0)])

    def test_small_tree(self):
        t = lca.Tree([-1, 0, 1, 1])
        t.build_euler_tour()
        self.assertEqual(t.euler_tour, [(0, 0), (1, 1), (2, 2), (1, 1), (3, 2), (1, 1), (0, 0)])

    def test_bamboo(self):
        t = lca.Tree([-1, 0, 1, 2, 3, 4, 5])
        t.build_euler_tour()
        self.assertEqual(t.euler_tour, [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (5, 5), (4, 4), (3, 3), (2, 2), (1, 1), (0, 0)])
