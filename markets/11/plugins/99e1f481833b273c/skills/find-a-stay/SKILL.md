---
name: find-a-stay
description: Find and price a Smart City Stays serviced apartment in Cape Town (Century City or the V&A Waterfront) for given dates, using live availability and direct rates, and hand the user a link to book on smartcitystays.com. Use when someone asks for a short-stay, corporate or family apartment in Cape Town, or asks what a named Smart City Stays apartment costs.
---

# Find a Smart City Stays apartment

Explicit instructions from the user take priority over this guidance.

## Tools

- `search_stays` (Smart City Stays server): live availability and prices across the portfolio.
  Inputs: `checkin`, `checkout` (YYYY-MM-DD), optional `area` (`waterfront`, `century-city` or `any`),
  optional `bedrooms` (0 = studio, up to 3), optional `guests`.
- `get_quote`: live price and every available rate for one named apartment.
  Inputs: `area`, `roomTypeId`, `checkin`, `checkout`. Look up `area` and `roomTypeId` in
  `references/apartments.md` (ids repeat across areas, so always pass both).

Both tools only read availability and prices. Neither books, holds or charges anything.

## Workflow

1. Get the dates. If the user gave no check-in or check-out date, ask for them before calling a tool.
   Resolve relative dates ("next weekend", "3 nights from 10 March") to YYYY-MM-DD in Cape Town time.
   Check-in must not be in the past and check-out must be after check-in.
2. Map the request to filters:
   - "Waterfront", "V&A", "Marina" means `area: waterfront`. "Century City" means `area: century-city`.
     Anywhere else in Cape Town, or no area given, means `area: any`.
   - "Studio" means `bedrooms: 0`. A named bedroom count maps directly.
   - If only a group size is given, pass `guests` and let the tool choose a sensible bedroom count.
3. If the user names a specific apartment, find it in `references/apartments.md` and call `get_quote`.
   If the name is ambiguous or not in the table, call `search_stays` with the matching area and bedrooms instead.
   Otherwise call `search_stays`.
4. Present results clearly: apartment name, area, total for the stay and nightly rate in ZAR, and the book link
   exactly as returned. Keep the tool's order (cheapest first). Do not invent prices, amenities or availability.
5. If nothing is available, say so plainly and suggest nearby dates, another area, or a different size.

## Limits

- Only Smart City Stays apartments in Cape Town are covered. For other cities or other hotels, say this
  app cannot help.
- The app cannot book, cancel, change or pay for a stay. Bookings are completed on smartcitystays.com
  through the book link. For existing bookings, point the user to https://www.smartcitystays.com/contact.
- Never ask for or accept card details in the chat.
