from algorithms.arrays import (
    swap_positions_v1, swap_positions_v2, swap_positions_v3
)

import unittest


class TestSwapElements(unittest.TestCase):
    def test_swap_positions_v1(self):
        self.assertEqual(swap_positions_v1(
            [4, 5, 2, 6, 7, 8, 1], pos1=2, pos2=5),
            [4, 5, 8, 6, 7, 2, 1])

    def test_swap_positions_v2(self):
        self.assertEqual(swap_positions_v2(
            [4, 5, 2, 6, 7, 8, 1], pos1=2, pos2=5),
            [4, 5, 8, 6, 7, 2, 1])

    def test_swap_positions_v3(self):
        self.assertEqual(swap_positions_v3(
            [4, 5, 2, 6, 7, 8, 1], pos1=2, pos2=5),
            [4, 5, 8, 6, 7, 2, 1])
