---
name: find-pet-trade-suppliers
description: Use when a pet business needs a trade supplier, wholesaler or manufacturer, optionally near a place or limited to trade-only sellers.
---

# Find pet trade suppliers

1. Work out what is needed in plain words (for example "dog treats", "grooming tables", "aquatics wholesale", "kennels") and the place, if any.
2. Call `find_pet_trade_suppliers`. Pass the place as `location`, with its `latitude` and `longitude` when you know them, and an ISO `country` code when the person names a country. Set `sells_to` to `trade_only` when they want trade-only suppliers.
3. For more on one result call `get_pet_trade_listing` with its listing id.
4. To show what is covered call `list_pet_trade_categories`.

Rules: describe businesses only from the returned summaries and link to the listing page. Results are ordered by match and distance only; never present any listing as sponsored or recommended for payment. Do not invent contact details, prices or reviews. Keep links exactly as returned.
