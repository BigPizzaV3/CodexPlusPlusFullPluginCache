---
name: bluerails
description: Find DACH hotels near a place and, when dates and party details are available, retrieve live rooms, whole-stay EUR prices, cancellation terms, breakfast details, and booking links through the Bluerails MCP server. Use for hotel discovery or availability searches in Germany, Austria, and Switzerland; do not use it for booking or payment.
---

# Bluerails

Use the connected Bluerails MCP server at `https://402.bluerails.com/mcp`. It is public and exposes a single tool, `list_hotels`. It never books anything and never charges anyone. Read the parameter list, defaults and limits from the live `tools/list` and trust it over this document; what follows is how to use the answer, not a copy of the schema.

## Search hotels

One call does the whole search — there is no second tool to fan out to. Pass everything the user supplied at once.

- `city` is the place to search around: any DACH place name, of any size. Pass the name alone — `Waren`, never `20 km from Waren`; distance goes in `radius`. Prefer the English name where one exists (`Munich`, not `München`), because accents are folded before lookup and can collide with a smaller place of the same folded name.
- Prefer `city` over `query` for anything geographic. `city` resolves a real place and returns neighbouring towns; `query` only matches words in a name or description and knows nothing about location.
- `radius` is a value and its unit — `{"value": 10, "unit": "mi"}` — so state the unit the user used and never convert it yourself.
- `country` and `starRating` narrow the set when the user asked for that.
- Do not use `limit` to shape the answer. A small `limit` also shrinks how many properties get priced at all, and the ones priced are the *nearest*, not the cheapest — so asking for `limit: 5` to answer "the five cheapest near Munich" prices five nearby hotels and hides the cheaper ones further out. Request the full set and trim in your own presentation.

For live rates, pass all three stay fields in the same call:

- `checkIn` and `checkOut` in `YYYY-MM-DD` format.
- `adults`.
- `childrenAges`, when applicable: one integer per child, never a child count. Never invent an age.
- `maxPricePerNight`, when the user gave a budget. It FILTERS rather than labels: `priced` comes back holding only the hotels at or under it, each carrying only its rooms at or under it. A kept room keeps all of its rate plans, including one dearer than the budget, so a breakfast rate is still there to offer. The comparison is the stay average, not a rate charged every night.

If dates or party details are missing, search without them, and ask only for what the user's actual request needs. Never invent stay parameters.

## Interpret results

Results come back nearest first, each with `distanceKm` — say how far a property is from the place the user named, and treat `distanceApproximate: true` as "about". A dated result splits into groups. Present `priced` first.

**`priced`** — hotels whose live rates were read, on page 1 only. At most the nearest ten, drawn from the whole filter set rather than from this page. So a budget verdict is only ever about those: "of the nearest hotels I could price, none is under [budget]" — never "nothing is available".

- `rooms` is one entry per room *and* rate plan. Show the bookable ones with `eurPrice` (the total for the whole stay), breakfast inclusion and cancellation terms.
- An entry with `soldOut: true` or `eurPrice: null` cannot be booked. Leave it out, or name it as unavailable — never print a null price and never hand over a link to it.
- A room's own `bookingUrl` opens the engine on that room and rate, but it is optional. When it is absent, use the hotel's `bookingUrl`.
- `stayTotalEur` is the cheapest bookable offer for the whole stay. `pricePerNightEur` is that total divided by the nights — describe it as an average per night, not the charge for each night.

**`aboveBudget`** — only when a `maxPricePerNight` was given and *not one* hotel fits it. These are hotels whose real prices were read and are over the budget, in the same shape as `priced`. It is never a second page to offer alongside `priced`: it answers "then what does the nearest thing cost". The honest sentence is "none of the ones I could price are under X, the cheapest is Y". It is nearest-first, not cheapest-first, so read the prices rather than taking the first row.

**`unpriced`** — every other match: engines that cannot be read, engines that did not answer, and properties past the read ceiling. These are all the same thing to the user, and their price is *unknown*, never sold out. It is paged, and no count of the whole match is returned — narrow with filters rather than paging to find out how many there are.

- Give each one its `bookingUrl`. If `datesApplied` or `partyApplied` is false, say the user will have to enter those details on the hotel's site.
- A `bookingUrl` of `null` means no *booking* link is held. Say so and offer nothing to book — but `websiteUrl` is the property's own site, so offer that as its website, never as a way to book or check rates. An empty `websiteUrl` is the opposite case: we know where to book but never found a site of its own. Offer the `bookingUrl` and say nothing about a website.

A dateless result puts every match in `unpriced` with no `priced` at all. That is expected, and says nothing about availability.

An empty `priced` on a dated call does NOT mean the rates were unreadable. Under a budget it means every hotel that could be priced costs more, and those are in `aboveBudget` with real prices — quote them. Only when `aboveBudget` is empty too does it mean no rates could be read; say exactly that and hand over the links. A reader returns the same empty answer for a network failure, a party the engine will not sell to, and a genuinely full hotel, and never says which.

Read `hint`. It is the one part of the answer that reports what the rows cannot: why a search came back empty, what the budget left out, and how many properties were dropped because their engine stated they are full for this stay. Those dropped properties are the single exception to "no row can tell you a hotel has no space" — they are not in any group, and only `hint` counts them. Read the whole string; a budget sentence and a sold-out sentence can arrive together, and it describes the hotels this call priced, never the whole area.

If the response has `placeNotRecognised`, the *name* was not understood — not that the place has no hotels. Try the English name, or ask for a nearby larger town.

If the search found nothing at all, the response carries `nearestBeyondRadiusKm`: how far the nearest property lies outside the radius searched, with `nearestSearchedToKm` saying how far that look went. Report the number and offer to widen to it, rather than guessing a bigger radius. A `null` there means there is nothing even at the outer limit of the search — unless you set a `query`, which stays applied to that second look, so a null with a query set does not mean the area is empty. Read the `hint`.

## Answering the user

- Answer the dates, place and budget that were asked for. If they cannot be met, say so plainly. Never substitute different dates, a different town or a higher budget and present the result as the answer.
- A requested number of hotels is a ceiling, not a target. If the search the user asked for yields one property, the answer is one property.
- Widening the radius is a separate step. Give the real answer first, then offer it — and say the radius changed.
- Never drop a property because its price could not be read. Surface it in its own labelled group, with its link.
- Never fabricate a hotel, room, price, availability status, or booking link. Every one of those must come from a tool response.
- Booking and payment are not part of this tool surface. Hand over the returned link so the user completes the booking on the hotel's own site. Offer to book or pay only if the `tools/list` you actually received contains a tool that does it, and confirm with the user before any consequential action.
- Publishers, ecommerce stores, and SaaS companies in the Bluerails registry are served over the REST API, not as MCP tools. Do not imply that `list_hotels` searches those verticals.
