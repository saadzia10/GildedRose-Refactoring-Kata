# -*- coding: utf-8 -*-
from updaters import StandardUpdater, AgedBrieUpdater, BackstagePassesUpdater, SulfurasUpdater

SULFURAS = "Sulfuras, Hand of Ragnaros"
AGED_BRIE = "Aged Brie"
BACKSTAGE_PASSES = "Backstage passes to a TAFKAL80ETC concert"

UPDATERS = {
    SULFURAS: SulfurasUpdater(),
    AGED_BRIE: AgedBrieUpdater(),
    BACKSTAGE_PASSES: BackstagePassesUpdater(),
}

def get_updater(item):
    return UPDATERS.get(item.name, StandardUpdater())


class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            get_updater(item).update(item)


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
