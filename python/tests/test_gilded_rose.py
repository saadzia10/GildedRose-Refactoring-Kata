import pytest
from gilded_rose import Item, GildedRose

def run_item_days(item, days):
    gilded_rose = GildedRose([item])
    for day in range(days):
        gilded_rose.update_quality()
    return gilded_rose.items[0]


# General Constraints Test

def test_below_zero_quality_standard():
    item = Item("foo", sell_in=5, quality=0)
    result = run_item_days(item, 10)
    assert result.quality == 0
    assert result.sell_in == -5

def test_below_zero_quality_aged_brie():
    item = Item("Aged Brie", sell_in=5, quality=0)
    result = run_item_days(item, 10)
    assert result.quality == 15
    assert result.sell_in == -5

def test_below_zero_quality_backstage_passes():
    item = Item("Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=0)
    result = run_item_days(item, 10)
    assert result.quality == 0
    assert result.sell_in == -5

def test_fixed_quality_sulfuras():
    item = Item("Sulfuras, Hand of Ragnaros", sell_in=5, quality=80)
    result = run_item_days(item, 10)
    assert result.quality == 80
    assert result.sell_in == 5

# Quality never above 50

def test_quality_above_50_aged_brie():
    item = Item("Aged Brie", sell_in=5, quality=50)
    result = run_item_days(item, 10)
    assert result.quality == 50
    assert result.sell_in == -5

def test_quality_above_50_backstage_passes():
    item = Item("Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=50)
    result = run_item_days(item, 10)
    assert result.quality == 0
    assert result.sell_in == -5

# Test for sell_in decreases by 1
def test_sell_in_decreases_by_1_standard():
    item = Item("foo", sell_in=5, quality=30)
    result = run_item_days(item, 10)
    assert result.sell_in == -5

def test_sell_in_decreases_by_1_aged_brie():
    item = Item("Aged Brie", sell_in=5, quality=30)
    result = run_item_days(item, 10)
    assert result.sell_in == -5

def test_sell_in_decreases_by_1_backstage_passes():
    item = Item("Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=30)
    result = run_item_days(item, 10)
    assert result.sell_in == -5

# Item Rules Test

# Standard Items

def test_standard_before_expiry_degrades_by_1():
    it = Item("+5 Dexterity Vest", sell_in=10, quality=20)
    it = run_item_days(it, 1)
    assert it.quality == 19

def test_standard_after_expiry_degrades_by_2():
    it = Item("Elixir of the Mongoose", sell_in=0, quality=10)
    it = run_item_days(it, 1)
    assert it.quality == 8

# Aged Brie

def test_brie_before_expiry_increases_by_1():
    it = Item("Aged Brie", sell_in=2, quality=0)
    it = run_item_days(it, 1)
    assert it.quality == 1

def test_brie_after_expiry_increases_by_2():
    it = Item("Aged Brie", sell_in=0, quality=0)
    it = run_item_days(it, 1)
    assert it.quality == 2

# Backstage Passes

@pytest.mark.parametrize("sell_in, expected_inc", [
    (15, 1),  # >10
    (10, 2),  # 6..10
    (7, 2),
    (5, 3),   # 1..5
    (1, 3),
])
def test_backstage_increments_tiers(sell_in, expected_inc):
    start_q = 10
    item = Item("Backstage passes to a TAFKAL80ETC concert", sell_in, start_q)
    item = run_item_days(item, 1)
    assert item.quality == start_q + expected_inc

# Conjured Items

def test_conjured_degrades_by_2_before_expiry():
    item = Item("Conjured Mana Cake", sell_in=3, quality=10)
    item = run_item_days(item, 1)
    assert item.quality == 8

def test_conjured_degrades_by_4_after_expiry():
    item = Item("Conjured Mana Cake", sell_in=0, quality=10)
    item = run_item_days(item, 1)
    assert item.quality == 6

def test_conjured_zero_quality():
    item = Item("Conjured Mana Cake", sell_in=-1, quality=3)
    item = run_item_days(item, 1)
    assert item.quality == 0
