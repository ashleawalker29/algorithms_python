import unittest

from Wedding_Items import WeddingItem


class WeddingItemsTests(unittest.TestCase):

    def test_wedding_items_attributes(self):
        item = WeddingItem(
            name='Example Item',
            hcr=30,
            sell_price=25000)
        self.assertEqual(item.name, 'Example Item')
        self.assertEqual(item.hcr, 30)
        self.assertEqual(item.sell_price, 25000)
        self.assertEqual(round(item.ratio, 2), 8.33)
