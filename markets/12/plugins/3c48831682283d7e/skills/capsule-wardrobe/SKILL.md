---
name: capsule-wardrobe
description: Plan a small mix-and-match capsule wardrobe from Tailor's shops, for a trip, a new season, a new job or a wardrobe refresh. Use when someone asks what to pack, wants a set of pieces that all work together, or wants as many outfits as possible from a few items.
---

# Plan a capsule wardrobe with Tailor

A capsule is a few pieces in which nearly every top works with nearly every bottom.
The value of the answer is the combinations, so plan the set as a whole before
searching.

## 1. Get the brief

Infer what you can and ask only for what's missing, in one short question:

- **Country** (`za`, `us` or `gb`) and **department** (`women`, `men`, `kids`, `baby`)
- **What it's for**: trip length, destination and season, or the new job or season
- **Activities**: work, sightseeing, evenings out, beach, hiking
- **Budget** for everything they need to buy
- **What they already own** that should be part of the capsule. Count those pieces in
  the plan, but don't search for them.

## 2. Plan the set

Start from this shape and adjust it to the brief:

| Slot | Count |
| --- | --- |
| Bottoms (trousers, jeans, skirts) | 2 |
| Tops (tees, shirts, knits) | 3 to 4 |
| Layer (cardigan, blazer, overshirt) | 1 |
| Outerwear, if the weather needs it | 1 |
| Shoes | 2 (one comfortable pair for the day, one smarter) |
| Optional: one dress or one evening piece | 1 |

Choose a palette of two neutrals and one accent colour, and keep every top compatible
with every bottom. For a trip, use fabrics that suit the climate and travel well.

## 3. Search slot by slot

Split the budget across the slots and pass each share as `price_max` in the country's
currency. Call `search_products` once per piece, with `country`, `department`, a
product-page description and `colour_family` for the palette colours. Pass `exclude_ids`
for items you've already picked, so that two tops in the same slot differ.

## 4. Present the capsule

Call `show_products` once with every chosen `product_id`, grouped by slot, with a
`title` such as "Your 5-day New York capsule". Don't re-list the products in text.
Then give:

- 4 to 6 named outfits from the set, each as a short line of piece names ("Day 1:
  cream knit, dark jeans, white sneakers")
- how many outfits the set makes in total
- the total price in the shop's currency, and which owned pieces it builds on

Offer to swap any piece, to stretch or cut the budget, or to add one piece that
unlocks more outfits.
