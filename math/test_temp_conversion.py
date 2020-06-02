import unittest

from .temp_conversion import celsius_to_fahrenheit, fahrenheit_to_celsius, round_traditional


class TempConversionTests(unittest.TestCase):

    def test_celsius_to_fahrenheit_conversion(self):
        self.assertEqual(celsius_to_fahrenheit(20.0), 68)
        self.assertEqual(celsius_to_fahrenheit('Not a temperature'), 'Not a valid temperature.')

    def test_fahrenheit_to_celsius_conversion(self):
        self.assertEqual(fahrenheit_to_celsius(70.0), 21.11)
        self.assertEqual(fahrenheit_to_celsius('Not a temperature'), 'Not a valid temperature.')

    def test_traditional_rounding(self):
        self.assertEqual(round_traditional(1.004, 2), 1.00)
        self.assertEqual(round_traditional(1.005, 2), 1.01)
