---
name: compare-listings
description: Compare several UAE property listings from Listint side by side on price, price per sqft, size, bedrooms, location, developer and completion status, and explain which suits a stated priority such as budget, space or move-in readiness. Use after a Listint search when someone asks to compare, rank, shortlist or choose between listings, or asks which is better value. Do not use to compare properties that did not come from Listint, or to give investment, mortgage or valuation advice.
---

# Comparing Listint listings

Use this once `search_listings` has returned results the user wants weighed
against each other. Compare only listings actually returned by Listint.

## Build the comparison from real fields

Put the listings in a table, one row each, with the columns that matter for the
question asked. Useful columns, all straight from the result:

`price_label` · `category` · `bedrooms` · `bathrooms` · `area` · `location` ·
`property_type` · `agency` · `developer` · `completion_status` ·
`completion_percentage`

Derive **price per sqft** as `price / area`, rounded to the nearest dirham, and
label it in AED/sqft. It is usually the single most useful column, because it
separates "cheap" from "good value".

Only compute it when both `price` and `area` are present. Where either is
missing, write "n/a" — never estimate a price or a size, and never carry a
figure over from a similar listing.

## Say what the numbers mean

After the table, give a short read of it against whatever the user actually
cares about:

- **Budget** — lowest total price, and separately the best price per sqft; these
  are often different listings, which is worth pointing out.
- **Space** — largest `area`, and bedrooms relative to size, since a large
  bedroom count in a small area means small rooms.
- **Move-in readiness** — `completion_status` of `Ready` beats `Off Plan`; for
  off-plan, `completion_percentage` shows how far along it is.
- **Location** — group by `location` so the comparison is like-for-like; a
  cheaper listing in a different community is not really a cheaper equivalent.

Keep it to a few sentences. State the trade-off rather than declaring a single
winner, unless the user gave one clear priority.

## Boundaries

- **Never put a sale price and a rent in the same comparison.** Check `category`
  on every listing first: `Sale` is a purchase price and `Rent` is an annual
  rent, so comparing them, or deriving one price-per-sqft column across both,
  produces a meaningless answer. Compare within one category and say why if the
  user's shortlist mixed them.
- A missing price means it is not published. Say "price on request"; do not
  treat it as the cheapest option or leave it out silently.
- `completion_percentage` is construction progress. It is not a score, a
  discount, or a measure of quality.
- Comparing listings is not valuation. Do not project appreciation, rental
  yield, or return on investment, and do not advise on financing.
- Link each listing by its `url` so the user can open any of them.
