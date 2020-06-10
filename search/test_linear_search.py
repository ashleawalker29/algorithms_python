import unittest

from linear import linear_search


class LinearSearchTests(unittest.TestCase):

    def test_linear_search_none(self):
        self.assertEqual(linear_search(None, 1), 'Nothing to search through.')

    def test_linear_search_empty(self):
        self.assertEqual(linear_search([], 1), 'Nothing to search through.')

    def test_linear_search_not_nums(self):
        self.assertEqual(linear_search([0, 'a', 3], 3),
                         'Can only search through lists of just numbers.')
        self.assertEqual(linear_search(['a', 'b', 'c'], 'a'),
                         'Can only search through lists of just numbers.')

    def test_linear_search_single_value(self):
        self.assertEqual(linear_search([1], 1), 'Value was found within the list.')
        self.assertEqual(linear_search([1], 2), 'Value was not found within the list.')

    def test_linear_search_nums_positive_sorted(self):
        self.assertEqual(linear_search([12, 19, 20, 45, 55, 91], 20),
                         'Value was found within the list.')
        self.assertEqual(linear_search([12, 19, 20, 45, 55, 91], 72),
                         'Value was not found within the list.')

    def test_linear_search_nums_positive_unsorted(self):
        self.assertEqual(linear_search([20, 12, 45, 19, 91, 55], 20),
                         'Value was found within the list.')
        self.assertEqual(linear_search([20, 12, 45, 19, 91, 55], 72),
                         'Value was not found within the list.')

    def test_linear_search_nums_negative_sorted(self):
        self.assertEqual(linear_search([-91, -55, -45, -20, -19, -12], -45),
                         'Value was found within the list.')
        self.assertEqual(linear_search([-91, -55, -45, -20, -19, -12], -72),
                         'Value was not found within the list.')

    def test_linear_search_nums_negative_unsorted(self):
        self.assertEqual(linear_search([-20, -12, -45, -19, -91, -55], -45),
                         'Value was found within the list.')
        self.assertEqual(linear_search([-20, -12, -45, -19, -91, -55], -72),
                         'Value was not found within the list.')

    def test_linear_search_nums_positive_and_negative_sorted(self):
        self.assertEqual(linear_search([-20, -19, -12, 45, 55, 91], 45),
                         'Value was found within the list.')
        self.assertEqual(linear_search([-20, -19, -12, 45, 55, 91], 72),
                         'Value was not found within the list.')
        self.assertEqual(linear_search([-20, -19, -12, 45, 55, 91], -12),
                         'Value was found within the list.')
        self.assertEqual(linear_search([-20, -19, -12, 45, 55, 91], -72),
                         'Value was not found within the list.')

    def test_linear_search_nums_positive_and_negative_unsorted(self):
        self.assertEqual(linear_search([-12, -19, -20, 45, 91, 55], 45),
                         'Value was found within the list.')
        self.assertEqual(linear_search([-12, -19, -20, 45, 91, 55], 72),
                         'Value was not found within the list.')
        self.assertEqual(linear_search([-12, -19, -20, 45, 91, 55], -12),
                         'Value was found within the list.')
        self.assertEqual(linear_search([-12, -19, -20, 45, 91, 55], -72),
                         'Value was not found within the list.')
