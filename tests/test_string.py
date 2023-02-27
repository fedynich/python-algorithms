from algorithms.strings import *

import unittest


class TestString(unittest.TestCase):

    INPUT_V1 = 'Hello, World'
    OUTPUT_V1 = 'dlroW ,olleH'

    INPUT_V2 = ''
    OUTPUT_V2 = ''

    def test_pythonic(self):
        self.assertEqual(slicing(self.INPUT_V1), self.OUTPUT_V1)
        self.assertEqual(slicing(self.INPUT_V2), self.OUTPUT_V2)

    def test_built_in_reversed(self):
        self.assertEqual(built_in_reversed(self.INPUT_V1), self.OUTPUT_V1)
        self.assertEqual(built_in_reversed(self.INPUT_V2), self.OUTPUT_V2)

    def test_built_in_reverse(self):
        self.assertEqual(built_in_reverse(self.INPUT_V1), self.OUTPUT_V1)
        self.assertEqual(built_in_reverse(self.INPUT_V2), self.OUTPUT_V2)

    def test_iterative(self):
        self.assertEqual(iterative(self.INPUT_V1), self.OUTPUT_V1)
        self.assertEqual(iterative(self.INPUT_V2), self.OUTPUT_V2)

    def test_list_comprehension(self):
        self.assertEqual(list_comprehension(self.INPUT_V1), self.OUTPUT_V1)
        self.assertEqual(list_comprehension(self.INPUT_V2), self.OUTPUT_V2)

    def test_recursive(self):
        self.assertEqual(recursive(self.INPUT_V1), self.OUTPUT_V1)
        self.assertEqual(recursive(self.INPUT_V2), self.OUTPUT_V2)

