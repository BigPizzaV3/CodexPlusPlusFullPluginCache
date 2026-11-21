---
name: find-golf-suppliers
description: Use when a golf course, driving range, pro shop or indoor golf venue needs a trade supplier or contractor, optionally near a place.
---

# Find golf trade suppliers

1. Work out what is needed in plain words (for example "turf equipment", "golf carts", "range ball dispensers", "simulator installers") and the place, if any.
2. Call `find_golf_suppliers`. Pass the place as `location`, with its `latitude` and `longitude` when you know them, and an ISO `country` code when the person names a country. A US state, Canadian province or Australian state can go in `location` on its own.
3. For more on one result call `get_golf_supplier_listing` with its listing id.
4. To show what is covered call `list_golf_supplier_categories`.

Rules: describe businesses only from the returned summaries and link to the listing page. Results are ordered by match and distance only; never present any listing as sponsored or recommended for payment. Do not invent contact details, prices or reviews. Keep links exactly as returned.
