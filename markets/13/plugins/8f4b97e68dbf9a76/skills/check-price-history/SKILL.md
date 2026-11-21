---
name: check-price-history
description: Check a South African product's price history on PriceCheck to see whether today's price is a good deal. Use when the user asks if a price is good, whether to buy now or wait, whether something has been cheaper, or how a price has changed.
---

# Check whether a price is a good deal

1. Find the product with `search-products-tool` (brand in `brands`, model in `search`). Take the product ID from the Product URL: the number after `/offers/`.
2. Call `price-history-tool` with the product ID. It covers 90 days by default; use `days: 180` or `365` if the user asks about a longer period or the 90 days show no change.
3. Work out from the daily `MinPrice` values:
   - today's lowest price
   - the lowest and highest price in the period, with the dates
   - the average price in the period
4. Tell the user in plain words whether today's price is low, average or high for the period, and give the lowest price seen and when.
5. If the price has been flat the whole time, say so; it means waiting is unlikely to help based on history alone.

Don't predict future prices or promise that a sale is coming. Past prices don't guarantee future ones. Prices are in ZAR.
