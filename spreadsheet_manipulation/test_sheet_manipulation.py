import unittest

from sheet_manipulation import get_all_keys, get_worksheet_names, open_worksheet


class SheetManipulationTests(unittest.TestCase):

    def setUp(self):
        self.worksheet_names = get_worksheet_names()

    def test_get_worksheet_names(self):
        self.assertEqual(len(self.worksheet_names), 10)

        for worksheet_name in self.worksheet_names:
            self.assertIsInstance(worksheet_name, str)

    def test_open_worksheets(self):
        for worksheet_name in self.worksheet_names:
            self.assertTrue(open_worksheet(worksheet_name))

    def test_get_all_keys(self):
        for worksheet_name in self.worksheet_names:
            opened_worksheet = open_worksheet(worksheet_name)
            self.assertTrue(get_all_keys(opened_worksheet))
