---
name: property-search
description: Search UAE real-estate listings on Listint — apartments, villas, townhouses, buildings, land and developer projects — by area, budget, bedrooms, size, amenities or developer. Use when someone wants to find, browse, filter or price-check property to buy or rent in the UAE, or asks what is available in a specific community. Do not use for mortgages, legal or tax advice, or property valuation.
---

# Searching Listint

Listint indexes live UAE property listings. `search_listings` finds them;
`get_listing_details` returns one record by id. Both are read-only.

## Pick the right collection

`collection` is the first decision and the tools behave differently per value.

| Value | Holds | Use when |
|---|---|---|
| `unit` | Individual homes: apartments, villas, townhouses | Almost every buyer question. The **only** collection with bedroom, bathroom, property-type and amenity data |
| `property` | Standalone assets: whole buildings, compounds, land, warehouses | "building", "plot", "land", "compound", commercial assets |
| `project` | Developer developments | A named development, a launch, or a developer's portfolio |

Never send `bedrooms`, `bathrooms`, `property_type` or `amenities` with
`collection: "project"` — projects hold none of that data. The response will
say so in `unsupported_filters`, and the constraint the user asked for will not
have been applied.

## Only filter on what was actually said

Set a filter when the user stated it. Do not infer a budget, a bedroom count, a
location or a property type from context, and do not carry filters over from an
earlier search unless the user is clearly refining that same search. An
unfiltered search that returns something is more useful than a guessed filter
that returns nothing.

## Counts are lists, so ranges work

`bedrooms` and `bathrooms` take arrays. Expand ranges rather than dropping them:

- "3 bedroom" → `[3]`
- "2 or 3 beds" → `[2, 3]`
- "at least 4 beds" → `[4, 5, 6, 7, 8, 9]`
- "up to 2 beds" → `[0, 1, 2]`
- "studio" → `[0]`

## Locations

`locations` is an array, so "Al Reem Island or Saadiyat" is one search. Pass the
place names as the user said them, in **English** — Arabic place names do not
currently match and will be dropped from the filter. `locations` is the area
being searched, never the user's own position.

## Sorting

Map the user's wording: "cheap", "cheapest", "affordable", "lowest price" →
`price_asc`. "expensive", "most expensive", "luxury", "highest price" →
`price_desc`. Otherwise leave it alone.

## Reading the response honestly

Two fields change what you must tell the user:

- **`relaxed_filters`** — the exact search found nothing, so these constraints
  were dropped to return something. Say plainly that these are not exact
  matches and name what was relaxed, before listing anything.
- **`unsupported_filters`** — this collection has no data for that filter, so it
  was ignored. Say which constraint could not be applied and suggest searching
  `unit` instead if that would help.
- **`uncovered_location`** — Listint indexes nothing in the place that was
  asked for. Say so plainly. Do not offer listings from anywhere else as
  substitutes, and do not re-run the search with the location removed.

Other things worth knowing when you summarise results:

- Prices are **AED**; sizes are **sqft**.
- A missing `price` means the price is not published — say "price on request"
  rather than implying it is free or cheap.
- `bedrooms: 0` on a unit means **studio**. A bedroom count also restricts the
  search to homes, so a studio search will not return shops or warehouses.
- `category` is `Sale` or `Rent`. A rent price is the **annual** rent, so say
  "per year" rather than quoting it like a purchase price.
- `completion_percentage` is construction progress, not a discount or a rating.
- `agency` is who listed it; `developer` is who built it. They differ.
- Every listing carries a `url`; link to it rather than describing where to look.

## Coverage

Coverage is concentrated in the **United Arab Emirates** — principally Abu Dhabi
and Dubai, with some listings in Ras Al Khaimah — plus a smaller selection of
buildings and projects in Egypt, the United Kingdom, Oman, Morocco, Latvia and
Ethiopia. It is uneven and it changes: a community that has rentals may have
nothing for sale, and vice versa.

Do not pre-judge what exists from this paragraph — run the search and read what
comes back. When the search finds nothing in the requested place it returns
`uncovered_location`; say that Listint has no listings there and stop, rather
than offering somewhere else as though it matched.

`category` separates the two markets: `Sale` to buy, `Rent` to rent. Set it only
when the user made the intent explicit, and never swap one for the other — a
rental is not an answer to someone who wants to buy.

## Following up on a result

`get_listing_details` takes the `collection` and the `id` from a previous
search result. Use it when the user asks about one specific listing rather than
running the same search again.
