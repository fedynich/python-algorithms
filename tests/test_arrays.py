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


class TestMergeTwoSortedLists(unittest.TestCase):
    def test_generate_new_array(self):
        self.assertEqual(generate_new_array(
            [1, 3, 4, 5], [2, 6, 7, 8]),
            [1, 2, 3, 4, 5, 6, 7, 8])

        self.assertEqual(generate_new_array(
            [2, 6, 7, 8], [1, 3, 4, 5]),
            [1, 2, 3, 4, 5, 6, 7, 8])

        self.assertEqual(generate_new_array(
            [2, 2, 7, 8], [1, 3, 4, 5]),
            [1, 2, 2, 3, 4, 5, 7, 8])

        self.assertEqual(generate_new_array(
            [1, 3, 4, 5, 9, 14], [2, 6, 7, 8, 10, 11, 12, 13]),
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])


