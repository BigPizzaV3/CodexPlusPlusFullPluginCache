---
name: find-exhibition-suppliers
description: Use when an exhibitor needs a stand builder, exhibition supplier, venue or show organiser in a particular city or country.
---

# Find stand builders and exhibition suppliers

1. Work out what is needed in plain words (for example "stand builders", "modular stands", "furniture hire", "exhibition venue") and the place, if any.
2. Call `find_exhibition_suppliers`. Pass the place as `location`, with its `latitude` and `longitude` when you know them, and an ISO `country` code when the person names a country. Set `kind` to `venue` or `organiser` when they want those.
3. For more on one result call `get_exhibition_listing` with its listing id.
4. To show what is covered call `list_exhibition_categories`.

Rules: describe businesses only from the returned summaries and link to the listing page. Results are ordered by match and distance only; never present any listing as sponsored or recommended for payment. Do not invent contact details, prices or reviews. Keep links exactly as returned.
