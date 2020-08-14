import unittest

from sheet_manipulation import (get_all_keys, get_all_needed_cards, get_worksheet_names,
                                open_worksheet)


class SheetManipulationTests(unittest.TestCase):

    def setUp(self):
        self.worksheet_names = get_worksheet_names()

    def test_get_worksheet_names(self):
        self.assertEqual(len(self.worksheet_names), 9)

        for worksheet_name in self.worksheet_names:
            self.assertIsInstance(worksheet_name, str)

    def test_open_worksheets(self):
        for worksheet_name in self.worksheet_names:
            self.assertTrue(open_worksheet(worksheet_name))

    def test_get_all_keys(self):
        for worksheet_name in self.worksheet_names:
            opened_worksheet = open_worksheet(worksheet_name)
            self.assertTrue(get_all_keys(opened_worksheet))

    def test_get_all_needed_cards(self):
        NEEDED_WORKSHEET_KEYS = ['Card Number', 'Card Character', 'Have', 'Need']

        needed_card_worksheets = [open_worksheet(worksheet_name) for worksheet_name in
                                  self.worksheet_names if 'Need' in worksheet_name]

        # 5 needed worksheets: S1 Need, S2 Need, S3 Need, S4 Need, and WA Need.
        self.assertEqual(len(needed_card_worksheets), 5)

        needed_cards = []
        for needed_card_worksheet in needed_card_worksheets:
            # Ensure that each worksheet has the same keys for consistent comparisons.
            self.assertEqual(get_all_keys(needed_card_worksheet), NEEDED_WORKSHEET_KEYS)

            needed_cards.extend(get_all_needed_cards(needed_card_worksheet))

        # This test only works if there are 3 needed cards. This test will need to be changed once
        # more/all cards have been obtained. See README for more information.
        self.assertEqual(len(needed_cards), 3)
