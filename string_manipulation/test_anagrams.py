import unittest

from .anagrams import is_anagram


class AnagramsTests(unittest.TestCase):

    def test_anagrams_none(self):
        self.assertEqual(is_anagram(None, 'Example'),
                         'Cannot find an anagram from an empty string.')
        self.assertEqual(is_anagram('Example', None),
                         'Cannot find an anagram from an empty string.')
        self.assertEqual(is_anagram(None, None),
                         'Cannot find an anagram from an empty string.')

    def test_anagrams_partial(self):
        self.assertEqual(is_anagram('The army', 'Mary'), 'Partial anagram.')

    def test_anagrams_full(self):
        self.assertEqual(is_anagram('Oh, lame saint.', 'The Mona Lisa'), 'Full anagram.')
