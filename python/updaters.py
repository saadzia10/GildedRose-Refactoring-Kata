from abc import ABC, abstractmethod

MIN_QUALITY = 0
MAX_QUALITY = 50


class Updater(ABC):
    @abstractmethod
    def update(self, item):
        pass

    def _clamp(self, value, min_value, max_value):
        return max(min_value, min(value, max_value))

    def _inc(self, item, amount=1):
        item.quality = self._clamp(item.quality + amount, MIN_QUALITY, MAX_QUALITY)

    def _dec(self, item, amount=1):
        item.quality = self._clamp(item.quality - amount, MIN_QUALITY, MAX_QUALITY)

class StandardUpdater(Updater):
    def update(self, item):
        change = 2 if item.sell_in <= 0 else 1
        self._dec(item, change)
        item.sell_in -= 1


class SulfurasUpdater(Updater):
    def update(self, item):
        pass

class AgedBrieUpdater(Updater):
    def update(self, item):
        change = 2 if item.sell_in <= 0 else 1
        self._inc(item, change)
        item.sell_in -= 1

class BackstagePassesUpdater(Updater):
    def update(self, item):
        if item.sell_in <= 0:
            item.quality = 0
        else:
            if item.sell_in < 6:
                self._inc(item, 3)
            elif item.sell_in < 11:
                self._inc(item, 2)
            else:
                self._inc(item, 1)
        item.sell_in -= 1

class ConjuredUpdater(Updater):
    def update(self, item):
        change = 4 if item.sell_in <= 0 else 2
        self._dec(item, change)
        item.sell_in -= 1