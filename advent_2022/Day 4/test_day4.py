import unittest
import os

from day4 import eval_file

class Day4Tests(unittest.TestCase):
    def setUp(self):
        self.base_file_path = os.path.dirname(__file__) + '/test_files/'

    ##### Part 1 Tests #####
    def test_example_p1(self):
        """ Test to ensure the example solution matches for Part 1. """
        self.assertEqual(eval_file(self.base_file_path + 'example.txt', 'subset'), 2)

    def test_puzzle_input_p1(self):
        """ Test to ensure the solution is correct for Part 1. """
        self.assertEqual(eval_file(self.base_file_path + 'puzzle_input.txt', 'subset'), 466)

    ##### Part 2 Tests #####
    def test_example_p2(self):
        """ Test to ensure the example solution matches for Part 2. """
        self.assertEqual(eval_file(self.base_file_path + 'example.txt', 'overlap'), 4)

    def test_puzzle_input_p2(self):
        """ Test to ensure the solution is correct for Part 2. """
        self.assertEqual(eval_file(self.base_file_path + 'puzzle_input.txt', 'overlap'), 865)
