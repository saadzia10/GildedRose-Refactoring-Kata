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

    def update_quality(self):
        for item in self.items:
            if item.name not in ["Aged Brie", "Backstage passes to a TAFKAL80ETC concert", "Sulfuras, Hand of Ragnaros"]:
                decrement_quality(item)
            else:
                if item.quality < 50:
                    increment_quality(item)
                    if item.name == "Backstage passes to a TAFKAL80ETC concert":
                        if item.sell_in < 11:
                            if item.quality < 50:
                                increment_quality(item)
                        if item.sell_in < 6:
                            if item.quality < 50:
                                increment_quality(item)
            if item.name != "Sulfuras, Hand of Ragnaros":
                item.sell_in = item.sell_in - 1
            if item.sell_in < 0:
                if item.name != "Aged Brie":
                    if item.name != "Backstage passes to a TAFKAL80ETC concert":
                        if item.quality > 0:
                            if item.name != "Sulfuras, Hand of Ragnaros":
                                decrement_quality(item)
                    else:
                        decrement_quality(item, item.quality)
                else:
                    if item.quality < 50:
                        increment_quality(item)


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
