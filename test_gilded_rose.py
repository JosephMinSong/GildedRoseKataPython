# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    # example of test that checks for logical errors
    def test_sulfuras_should_not_decrease_quality(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 5, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        sulfuras_item = items[0]
        self.assertEqual(80, sulfuras_item.quality)
        self.assertEqual("Sulfuras, Hand of Ragnaros", sulfuras_item.name)

    # example of test that checks for syntax errors
    def test_gilded_rose_list_all_items(self):
        items = [Item("Sulfuras", 5, 80)]
        gilded_rose = GildedRose(items)
        all_items = gilded_rose.get_items()
        self.assertEqual(["Sulfuras"], all_items)

    # test 1 - logical error: Sulfuras item should still decrease sell in 
    # but it has no impact on the item
    def test_sulfuras_sell_value_still_decreases(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 5, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        sulfuras_item = items[0]
        self.assertEqual(4, sulfuras_item.sell_in)

    # test 2 - logical error: conjured item should decrement twice as fast
    def test_conjured_item_quality_decrement_twice_as_fast(self):
        items = [Item("Conjured item", 10, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        conjured_item = items[0]
        self.assertEqual(18, conjured_item.quality)

    # test 3 - logical error: item should not be instantiated with a quality over 50
    def test_item_quality_over_50(self):
        with self.assertRaises(ValueError):
            Item("Item more than 50", 10, 100)

    # test 4 - syntax error: there is no conjured field for items
    def test_conjured_item_field(self):
        items = [Item("Conjured item", 10, 20), Item("Non conjured item", 10, 20)]
        conjured_item = items[0]
        non_conjured_item = items[1]
        self.assertEqual(True, conjured_item.is_conjured)
        self.assertEqual(False, non_conjured_item.is_conjured)


if __name__ == '__main__':
    unittest.main()
