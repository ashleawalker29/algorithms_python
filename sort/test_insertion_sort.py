import unittest

from insertion import insertion_sort


class InsertionSortTests(unittest.TestCase):

    def test_insertion_sort_none(self):
        self.assertEqual(insertion_sort(None), 'Nothing to sort.')

    def test_insertion_sort_empty(self):
        self.assertEqual(insertion_sort([]), 'Nothing to sort.')

    def test_insertion_sort_not_nums(self):
        self.assertEqual(insertion_sort([0, 'a', 3]), 'Can only sort lists of just numbers.')
        self.assertEqual(insertion_sort(['a', 'b', 'c']), 'Can only sort lists of just numbers.')

    def test_insertion_sort_single_value(self):
        self.assertEqual(insertion_sort([5]), [5])

    def test_insertion_sort_nums_positive_even(self):
        self.assertEqual(insertion_sort([20, 12, 45, 19, 91, 55]), [12, 19, 20, 45, 55, 91])

    def test_insertion_sort_nums_positive_odd(self):
        self.assertEqual(insertion_sort([20, 12, 45, 19, 91]), [12, 19, 20, 45, 91])

    def test_insertion_sort_nums_negative_even(self):
        self.assertEqual(
            insertion_sort([-20, -12, -45, -19, -91, -55]), [-91, -55, -45, -20, -19, -12])

    def test_insertion_sort_nums_negative_odd(self):
        self.assertEqual(
            insertion_sort([-20, -12, -45, -19, -91]), [-91, -45, -20, -19, -12])

    def test_insertion_sort_nums_positive_and_negative_even(self):
        self.assertEqual(insertion_sort([-12, -19, -20, 45, 91, 55]), [-20, -19, -12, 45, 55, 91])

    def test_insertion_sort_nums_positive_and_negative_odd(self):
        self.assertEqual(insertion_sort([-12, -19, -20, 45, 91]), [-20, -19, -12, 45, 91])
