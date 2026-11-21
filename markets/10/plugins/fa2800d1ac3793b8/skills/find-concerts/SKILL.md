---
name: find-concerts
description: Find upcoming concerts and gigs in Belgium or the Netherlands with the Concertje tools. Use when the user asks what's on in a Belgian or Dutch city or venue, whether an artist plays there, or about ticket status, prices, on-sale or presale dates for such a show.
---

# Find concerts in Belgium and the Netherlands

Explicit user instructions take priority over this skill.

## 1. Pick the country

- Dutch city or venue (Amsterdam, Rotterdam, Utrecht, Paradiso, Melkweg…): pass `country: 'NL'`.
- Belgian, or no place given: pass `country: 'BE'` (the default).
- A place outside Belgium and the Netherlands: say Concertje only covers those two countries. Don't call a tool.
- City names work in English, Dutch or French ("Ghent", "Gent", "Gand").

## 2. Call the right tool

- Concerts on a date or in a period: `concertje_search_concerts` with `when` (`today`, `tomorrow`,
  `weekend`, `week`, `month`) or `dateFrom` and `dateTo` (YYYY-MM-DD).
- Every search shows its results to the user as cards, so ask in one call: put all the cities in
  `cities` and all the genres in `genres` ("post-punk", "techno", as the user wrote them) instead of
  one search per city or genre, or fetching everything and filtering yourself. An unknown genre is an
  error: try a broader one.
- A venue: `concertje_list_venues` for its ID (match on `name` or `aliases`), then
  `concertje_search_concerts` with `venueId`.
- Artists: `concertje_search_concerts` with every name in `searches`; without `country` it covers both
  countries. For genres, bio or related artists, call `concertje_get_artist` with an artist `id` from
  those results.
- Price, on-sale or presale details for one show: `concertje_get_concert` with its `id`.
- `pagination.total` larger than the results: page with `offset` only when the user wants more. The
  `countries` in a result are the ones it searched; don't search those again.

## 3. Answer

- The cards already list the concerts, so don't repeat them all. Highlight the best few, one line each:
  date, artists, venue and city, ticket status, price, and the `url` link. Say how many more there are.
- Ticket status in words: `announced` (not on sale yet), `available`, `limited` (few left), `waitlist`, `sold_out`, `cancelled`, `unknown`.
- State only prices, dates and statuses a tool returned. A missing price or on-sale date is unknown, not free.
- No results: say so plainly and suggest a wider date range or a nearby city.

## Out of scope

- Buying, reserving or saving tickets: Concertje is read-only. Give the concert page link; tickets are sold
  by the venue or ticket seller.
- Concerts the tools didn't return: don't add them from memory.
