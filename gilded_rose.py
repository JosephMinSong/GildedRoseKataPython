# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod

class Item(ABC):
    """ DO NOT CHANGE THIS CLASS!!!"""
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = self.validateQuality(quality)
    
    def validateQuality(self, quality):
        if self.name != "Sulfuras, Hand of Ragnaros":
            if quality > 50:
                raise ValueError
        return quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
    
    @abstractmethod
    def updateQuality(self):
        pass

class AgedBrie(Item):
    def __init__(self, sell_in, quality):
        super().__init__("Aged Brie", sell_in, quality)
    
    def updateQuality(self):
        # "Aged Brie" actually increases in Quality the older it gets
        if self.quality < 50:
            self.quality += 1
        self.sell_in -= 1

class Sulfuras(Item):
    def __init__(self, sell_in):
        super().__init__("Sulfuras, Hand of Ragnaros", sell_in, 80)
    
    def updateQuality(self):
        # "Sulfuras", being a legendary item, never has to be sold or decreases in Quality
        pass

class BackstagePasses(Item):
    def __init__(self, sell_in, quality):
        super().__init__("Backstage passes to a TAFKAL80ETC concert", sell_in, quality)
    
    def updateQuality(self):
        """
        "Backstage passes", like aged brie, increases in Quality as its SellIn value approaches;
        Quality increases by 2 when there are 10 days or less and by 3 when there are 5 days or less but
        Quality drops to 0 after the concert
        """
        if self.sell_in < 0:
            self.quality = 0
        elif self.sell_in <= 5:
            self.quality += 3
        elif self.sell_in <= 10:
            self.quality += 2
        else:
            self.quality += 1
        self.sell_in -= 1

class ConjuredItem(Item):
    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)
    
    def updateQuality(self):
        # "Conjured" items degrade in Quality twice as fast as normal items
        if self.quality > 0:
            if self.sell_in > 0:
                self.quality -= 2
            else:
                self.quality -= 4
        self.sell_in -= 1

class NormalItem(Item):
    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)
    
    def updateQuality(self):
        if self.quality > 0:
            if self.sell_in > 0:
                self.quality -= 1
            else:
                self.quality -= 2
        self.sell_in -= 1


class GildedRose(object):

    def __init__(self, items: list[Item]):
        # DO NOT CHANGE THIS ATTRIBUTE!!!
        self.items = items
    
    def get_items(self):
        return [str(item) for item in self.items]

    def update_quality(self):
        for item in self.items:
            item.updateQuality()
