import unittest

import os

from day1_p1 import get_calories
from day1_p2 import get_top3_calories


class Day1Tests(unittest.TestCase):
    def setUp(self):
        self.base_file_path = os.path.dirname(__file__) + '/test_files/'

    ##### Part 1 Tests #####
    def test_file_none_p1(self):
        """ Test when a file is empty for Part 1. """
        self.assertEqual(get_calories(self.base_file_path + '/empty.txt'), 0)

    def test_no_calories_p1(self):
        """ Test when a file is filled with just zeroes for Part 1. """
        self.assertEqual(get_calories(self.base_file_path + 'no_calories.txt'), 0)

    def test_example_p1(self):
        """ Test to ensure the example solution matches for Part 1. """
        calories = get_calories(self.base_file_path + '/example.txt')

        self.assertEqual(calories, 24000)

    def test_puzzle_input_p1(self):
        """ Test to ensure the solution is correct for Part 2. """
        calories = get_calories(self.base_file_path + '/puzzle_input.txt')

        self.assertEqual(calories, 66616)

    ##### Part 2 Tests #####
    def test_file_none_p2(self):
        """ Test when a file is empty for Part 1. """
        self.assertEqual(get_top3_calories(self.base_file_path + '/empty.txt'), 0)

    def test_no_calories_p2(self):
        """ Test when a file is filled with just zeroes for Part 2. """
        self.assertEqual(get_top3_calories(self.base_file_path + '/no_calories.txt'), 0)

    def test_example_p2(self):
        """ Test to ensure the example solution matches for Part 2. """
        calories = get_top3_calories(self.base_file_path + '/example.txt')

        self.assertEqual(calories, 45000)

    def test_puzzle_input_p2(self):
        """ Test to ensure the solution is correct for Part 2. """
        calories = get_top3_calories(self.base_file_path + '/puzzle_input.txt')

        self.assertEqual(calories, 199172)
