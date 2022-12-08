import unittest

import os

from day2_p1 import eval_rounds
from day2_p2 import eval_rounds_p2


class Day2Tests(unittest.TestCase):
    def setUp(self):
        self.base_file_path = os.path.dirname(__file__) + '/test_files/'

    ##### Part 1 Tests #####
    def test_example_p1(self):
        """ Test to ensure the example solution matches for Part 1. """
        total_score = eval_rounds(self.base_file_path + '/example.txt')

        self.assertEqual(total_score, 15)

    def test_puzzle_input_p1(self):
        """ Test to ensure the solution is correct for Part 1. """
        total_score = eval_rounds(self.base_file_path + '/puzzle_input.txt')

        self.assertEqual(total_score, 11063)

    ##### Part 2 Tests #####
    def test_example_p2(self):
        """ Test to ensure the example solution matches for Part 2. """
        total_score = eval_rounds_p2(self.base_file_path + '/example.txt')

        self.assertEqual(total_score, 12)

    def test_puzzle_input_p2(self):
        """ Test to ensure the solution is correct for Part 2. """
        total_score = eval_rounds_p2(self.base_file_path + '/puzzle_input.txt')

        self.assertEqual(total_score, 10349)
