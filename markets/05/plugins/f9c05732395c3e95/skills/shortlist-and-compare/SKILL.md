---
name: shortlist-and-compare
description: Build a shortlist of Dubai buildings from registered prices, yields and evidence thresholds, then compare the finalists side by side, using the Dubai Wealth Index tools. Use when the user asks which Dubai buildings or areas meet a budget, yield or rent target, wants the best buildings in an area for rental yield, or wants two to four named buildings compared.
---

# Shortlist and compare Dubai buildings

Explicit user instructions take priority over this workflow.

## Shortlist

- Thresholds the user states (budget, minimum gross yield, bedroom type,
  minimum number of sales, areas) go to `screen_buildings`. Set `minEvidence`
  to at least 10 when the user wants robust figures, and say what you used.
- "Best yields in <area>" without thresholds: `get_area` sorted by yield, or a
  published ranking (`list_rankings`, then `get_ranking` with the area).
  A ranking lists outliers and needs ten qualifying buildings; say so.
- Say plainly that thresholds apply to **registered medians**, not to
  apartments currently for sale, and that buildings below the publication gate
  cannot appear.

## Compare

- Two to four apartment buildings: `compare_buildings` on one bedroom type.
  It returns only the unit sizes every building publishes — keep that grain,
  and never compare one building's 1-bed with another's 2-bed.
- Villa communities: call `get_villa_community` once per community, same
  purpose and bedroom count.
- Areas: `get_area` per area on the same purpose and bedroom type.

## Optional market context

When the question calls for activity or supply context, use `get_market_activity`
on matching bedroom and ready/off-plan cohorts, or `get_supply_pipeline` for
pending projects. Keep source dates and both growth windows. Activity is not
sale probability or days on market; planned dates are not forecasts. Show a
brief summary first and offer detailed evidence only when useful.

## Report

A table works best: building, area, median price, price per sq ft, median rent,
gross yield, sales and contracts behind them, data date. A difference between
yields is in percentage points. Link each building's `canonicalUrl`.
