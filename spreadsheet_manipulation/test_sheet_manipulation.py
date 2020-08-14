import unittest

from sheet_manipulation import get_all_keys, get_worksheet_names, open_worksheet


class SheetManipulationTests(unittest.TestCase):

    def test_get_worksheet_names(self):
        worksheet_names = get_worksheet_names()

        self.assertEqual(len(worksheet_names), 10)

        for worksheet_name in worksheet_names:
            self.assertIsInstance(worksheet_name, str)

    def test_open_worksheets(self):
        worksheet_names = get_worksheet_names()

        for worksheet_name in worksheet_names:
            self.assertTrue(open_worksheet(worksheet_name))

    def test_get_all_keys(self):
        worksheet_names = get_worksheet_names()

        for worksheet_name in worksheet_names:
            opened_worksheet = open_worksheet(worksheet_name)
            self.assertTrue(get_all_keys(opened_worksheet))
