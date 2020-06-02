import unittest

from palindrome import is_palindrome


class PalindromeTests(unittest.TestCase):

    def test_palindrome_punctuation(self):
        self.assertTrue(is_palindrome('Madam, I\'m Adam.'))
        self.assertFalse(is_palindrome('This is, in fact, not a palindrome.'))

    def test_palindrome_capitalization(self):
        self.assertTrue(is_palindrome('Never Odd Or Even'))
        self.assertFalse(is_palindrome('This Is Not A Palindrome'))

    def test_palindrome_whitespace(self):
        self.assertTrue(is_palindrome('race car'))
        self.assertFalse(is_palindrome('not a palindrome'))

    def test_palindrome_numerics(self):
        self.assertTrue(is_palindrome('12321'))
        self.assertFalse(is_palindrome('12345'))
