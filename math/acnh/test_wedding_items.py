import unittest
from unittest.mock import patch

from best_wedding_items import get_best_wedding_items
from WeddingItems import WeddingItem, wedding_items


class WeddingItemsTests(unittest.TestCase):

    def test_weddingitem_attributes(self):
        item = WeddingItem(
            name='Example Item',
            hcr=30,
            sell_price=25000)
        self.assertEqual(item.name, 'Example Item')
        self.assertEqual(item.hcr, 30)
        self.assertEqual(item.sell_price, 25000)
        self.assertEqual(item.ratio, 8.33)

    def test_wedding_items_attributes(self):
        for wedding_item in wedding_items:
            self.assertTrue(isinstance(wedding_item, WeddingItem))
            self.assertTrue(wedding_item.name)
            self.assertTrue(wedding_item.hcr > 0)
            self.assertTrue(wedding_item.sell_price > 0)
            self.assertTrue(wedding_item.ratio > 0)

    @patch('best_wedding_items.get_input', return_value=0)
    def test_0_heart_crystals(self, input):
        self.assertEqual(get_best_wedding_items(), {})
