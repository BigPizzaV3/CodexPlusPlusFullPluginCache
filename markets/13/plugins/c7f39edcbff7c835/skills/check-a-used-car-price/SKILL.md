---
name: check-a-used-car-price
description: Judge whether a used car's asking price in Dubai is fair, using Dubai Car Index's modelled fair range for the model year and mileage. Use when the user shares a used-car listing, an asking price, or asks what a used car is worth.
---

# Check a used car's asking price

Explicit user instructions take priority over this workflow.

1. Identify brand, model, model year, mileage and asking price. If the brand or
   model slug is unclear, call `search` with the user's words.
2. With an asking price, call `check_asking_price`. Without one, call
   `get_used_value` with the year (and `km` if known).
3. If a result says `found: false`, use one of its `suggestions`; never guess.

Report:

- The verdict and the fair range (low, fair, high) at the stated mileage. If
  `kmAssumed` is true, say the range uses typical mileage for the year.
- That the range is modelled from the entry trim's list price and a
  depreciation curve, in average condition. A higher trim, low mileage or a
  full dealer history can justify more; an accident record or missing history
  justifies less.
- The page `url`, and the advice to inspect the car and check its RTA history
  before paying.

Do not present the fair value as a market price, an offer or a valuation of
this specific car.
