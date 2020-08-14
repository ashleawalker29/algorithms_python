import unittest

from sheet_manipulation import get_all_collection_cards, get_worksheet_names, open_worksheet


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

    def test_get_all_collection_cards(self):
        CARD_KEYS = ['Card Number', 'Card Character', 'Have', 'Need']

        collection_cards = get_all_collection_cards()

        self.assertEqual(len(collection_cards), 450)
        self.assertFalse([card for card in collection_cards if list(card.keys()) != CARD_KEYS])
