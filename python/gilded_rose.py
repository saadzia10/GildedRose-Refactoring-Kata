# -*- coding: utf-8 -*-

MAX_QUALITY = 50
MIN_QUALITY = 0
SULFURAS = "Sulfuras, Hand of Ragnaros"
AGED_BRIE = "Aged Brie"
BACKSTAGE_PASSES = "Backstage passes to a TAFKAL80ETC concert"

def clamp_quality(quality):
    return max(MIN_QUALITY, min(quality, MAX_QUALITY))

def increment_quality(item, amount=1):
    item.quality = clamp_quality(item.quality + amount)

def decrement_quality(item, amount=1):
    item.quality = clamp_quality(item.quality - amount)

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def _update_standard_item(self, item, expired):
        decrement_quality(item, 2 if expired else 1)

    def _update_aged_brie(self, item, expired):
        increment_quality(item, 2 if expired else 1)
    
    def _update_backstage_passes(self, item, expired):
        
        if expired:
            item.quality = 0
        else:
            if item.sell_in < 6:
                increment_quality(item, 3)
            elif item.sell_in < 11:
                increment_quality(item, 2)
            else:
                increment_quality(item, 1)

    def update_quality(self):
        for item in self.items:
            if item.name == SULFURAS:
                continue
            elif item.name == AGED_BRIE:
                self._update_aged_brie(item, item.sell_in <= 0)
            elif item.name == BACKSTAGE_PASSES:
                self._update_backstage_passes(item, item.sell_in <= 0)
            else:
                self._update_standard_item(item, item.sell_in <= 0)

            item.sell_in -= 1


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
