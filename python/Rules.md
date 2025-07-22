# Gilded Rose Rules

## Global Constraints
- Quality is never negative.
- Quality is never more than 50 (except **Sulfuras**, which is 80 and immutable).
- At the end of each day, `SellIn` decreases by 1 (except **Sulfuras**).

## Standard Items
- Before the `SellIn` date passes: Quality decreases by **1** per day.
- After the `SellIn` date: Quality decreases by **2** per day.

## Aged Brie
- Quality increases instead of decreasing.
- After the `SellIn` date, it increases twice as fast (**+2** per day), still capped at 50.

## Sulfuras, Hand of Ragnaros
- Legendary: `Quality` and `SellIn` never change.

## Backstage Passes (to a TAFKAL80ETC concert)
- Quality increases by:
  - **+1** when `SellIn` > 10
  - **+2** when 6 ≤ `SellIn` ≤ 10
  - **+3** when 1 ≤ `SellIn` ≤ 5
- After the concert (`SellIn` < 0): Quality drops to **0**.

## Conjured Items (Extension)
- Degrade in Quality twice as fast as the corresponding standard rule:
  - Before `SellIn` passes: **–2** per day
  - After `SellIn` passes: **–4** per day
