import unittest
import os

from day3_p1 import get_duplicate_item, get_priority, get_triples

class Day3Tests(unittest.TestCase):
    def setUp(self):
        self.base_file_path = os.path.dirname(__file__) + '/test_files/'

    ##### Part 1 Tests #####
    def test_example_p1(self):
        """ Test to ensure the example solution matches for Part 1. """
        dupes = get_duplicate_item(self.base_file_path + 'example.txt')
        self.assertEqual(dupes, ['p', 'L', 'P', 'v', 't', 's'])

        self.assertEqual(get_priority(dupes), 157)

    def test_puzzle_input_p1(self):
        """ Test to ensure the solution is correct for Part 1. """
        dupes = get_duplicate_item(self.base_file_path + 'puzzle_input.txt')
        self.assertEqual(dupes, ['l', 'j', 'q', 'j', 'Z', 'w', 'g', 'l', 'b', 'n', 's', 'j', 'H',
                                 'b', 'T', 'Z', 'W', 'N', 'z', 's', 'J', 'm', 'V', 'j', 'S', 'm',
                                 'p', 'N', 'g', 'J', 'P', 'm', 'Z', 'L', 'J', 'v', 'V', 'm', 'l',
                                 'l', 'F', 'L', 'G', 'f', 'g', 'n', 'c', 'f', 'n', 'd', 'F', 'H',
                                 'd', 'W', 'H', 'P', 'D', 'L', 'W', 'S', 'v', 'H', 'q', 'h', 'p',
                                 'l', 'N', 'r', 'g', 'g', 'S', 'N', 'S', 's', 'C', 'Q', 'v', 'm',
                                 'H', 'M', 'j', 'r', 'g', 'm', 'C', 'w', 't', 'S', 'M', 'B', 'V',
                                 'q', 'd', 'F', 'R', 'L', 'g', 'V', 'n', 'P', 'C', 'F', 'L', 'N',
                                 'T', 'C', 's', 'm', 'L', 'G', 'S', 'm', 'Z', 'F', 's', 'Q', 'l',
                                 'm', 't', 'j', 'w', 'h', 'j', 'N', 'C', 'J', 'N', 'Z', 's', 'z',
                                 'f', 't', 'H', 'L', 'G', 'n', 'h', 'm', 'F', 'p', 's', 'n', 'H',
                                 'M', 'G', 'q', 'M', 'l', 'j', 'J', 'W', 'l', 'P', 's', 'l', 'j',
                                 'G', 'g', 'M', 'd', 'l', 'z', 'L', 'M', 't', 'p', 'r', 'C', 't',
                                 'd', 'l', 'G', 'H', 'n', 'T', 'Q', 'L', 'Z', 'F', 'j', 'R', 'C',
                                 'S', 'R', 'm', 'c', 'T', 'f', 's', 'n', 'c', 'm', 'G', 'T', 'd',
                                 'h', 'N', 'Q', 'g', 'S', 'V', 'H', 'G', 'l', 'z', 'j', 'F', 'b',
                                 'G', 'p', 'P', 'W', 'd', 'S', 'G', 'z', 'D', 'V', 'G', 'g', 'm',
                                 'Z', 'h', 'V', 'v', 'J', 'Q', 'h', 'W', 'j', 'H', 'G', 'D', 'P',
                                 'm', 'v', 'd', 'v', 'w', 'n', 'l', 'G', 'g', 'm', 'd', 'Z', 'Q',
                                 'g', 'p', 'd', 'b', 'M', 'n', 'z', 'V', 'j', 'D', 'G', 'q', 'c',
                                 'b', 'Q', 'W', 'N', 'Z', 'z', 'V', 'M', 'C', 'g', 's', 'd', 'L',
                                 'q', 'z', 'V', 'z', 'Q', 's', 'G', 'd', 'J', 'W', 'g', 'Z', 'H',
                                 'D', 'N', 't', 'R', 'n', 'c', 'd', 'R', 'J', 'l', 'T', 'Q', 'j',
                                 'c'])

        self.assertEqual(get_priority(dupes), 7793)

    ##### Part 2 Tests #####
    def test_example_p2(self):
        """ Test to ensure the example solution matches for Part 2. """
        dupes = get_triples(self.base_file_path + 'example.txt')
        self.assertEqual(dupes, ['r', 'Z'])

        self.assertEqual(get_priority(dupes), 70)

    def test_puzzle_input_p2(self):
        """ Test to ensure the solution is correct for Part 2. """
        dupes = get_triples(self.base_file_path + 'puzzle_input.txt')
        self.assertEqual(len(dupes), 100)

        self.assertEqual(get_priority(dupes), 2499)
