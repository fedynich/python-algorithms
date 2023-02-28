from algorithms.arrays import *

import unittest


class TestSwapElements(unittest.TestCase):
    INPUT_V1 = [4, 5, 2, 6, 7, 8, 1]
    OUTPUT_V1 = [4, 5, 8, 6, 7, 2, 1]

    def test_swap_positions_v1(self):
        self.assertEqual(swap_positions_v1(
            self.INPUT_V1, pos1=2, pos2=5), self.INPUT_V1)

    def test_swap_positions_v2(self):
        self.assertEqual(swap_positions_v2(
            self.INPUT_V1, pos1=2, pos2=5), self.INPUT_V1)

    def test_swap_positions_v3(self):
        self.assertEqual(swap_positions_v3(
            self.INPUT_V1, pos1=2, pos2=5), self.INPUT_V1)


class TestRemoveEvenIntegers(unittest.TestCase):

    INPUT_V1 = [2, 7, 11, 15, 2, 6, 2, 15, 8]
    OUTPUT_V1 = [7, 11, 15, 15]

    def test_list_comprehension(self):
        self.assertEqual(list_comprehension(self.INPUT_V1), self.OUTPUT_V1)

    def test_built_in_remove(self):
        self.assertEqual(classic(self.INPUT_V1), self.OUTPUT_V1)

