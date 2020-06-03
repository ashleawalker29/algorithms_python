import unittest

from bubble import bubble_sort


class BubbleSortTests(unittest.TestCase):

    def test_bubble_sort_none(self):
        self.assertEqual(bubble_sort(None), 'Nothing to sort.')

    def test_bubble_sort_empty(self):
        self.assertEqual(bubble_sort([]), 'Nothing to sort.')

    def test_bubble_sort_not_nums(self):
        self.assertEqual(bubble_sort([0, 'a', 3]), 'Can only sort lists of just numbers.')
        self.assertEqual(bubble_sort(['a', 'b', 'c']), 'Can only sort lists of just numbers.')

    def test_bubble_sort_nums_positive(self):
        self.assertEqual(bubble_sort([20, 12, 45, 19, 91, 55]), [12, 19, 20, 45, 55, 91])

    def test_bubble_sort_nums_negative(self):
        self.assertEqual(
            bubble_sort([-20, -12, -45, -19, -91, -55]), [-91, -55, -45, -20, -19, -12])

    def test_bubble_sort_nums_positive_and_negative(self):
        self.assertEqual(
            bubble_sort([-12, -19, -20, 45, 91, 55]), [-20, -19, -12, 45, 55, 91])
