---
name: hotel-research
description: Compare Google Hotels or Booking.com hotel offers for dates and travelers, or inspect a supplied Booking property with HasData. Use for hotel research, not flights, homes for sale or making reservations.
---

# Compare hotels for the supplied stay

Read `../hasdata-research/SKILL.md` and the Travel section of `../hasdata-research/references/tool-catalog.md`.

Use `hasdata_google_travel_hotels_getGoogleHotels` with q, checkInDate and checkOutDate for Google Hotels. Booking discovery uses `hasdata_booking_search_getBookingSearchResults` with keyword; a supplied Booking property URL uses `hasdata_booking_place_getBookingPlaceDetails` without an unnecessary area search. Preserve the requested source; when unspecified, choose a suitable available source and state it rather than asking the user to select an API.

If the user has not named a source or room count, prefer Google Hotels, whose schema does not require rooms. For an explicitly requested Booking stay with a complete party but no room count, a one-room comparison may be used only as a clearly stated assumption when that party reasonably fits one room; ask when multiple rooms or occupancy would materially change the result. Preserve any supplied room count and never present an assumption as user-provided.

Collect materially missing dates and party details before a priced-stay query. Booking search and details both require rooms, adults and children. When children > 0, get every child's age and pass childrenAges as a comma-separated list, one age 0-17 per child. Google Hotels also has childrenAges; use its own live schema. Never silently switch to an adults-only stay.

Encode zero children by source. Booking requires children:0 for a supplied adults-only party. Google Hotels rejects explicit children:0; omit children and childrenAges when there are no children, but preserve any positive child count and supplied ages. Google Hotels has no rooms input in the checked schema; do not pass it or claim that a requested room count was applied. State that limitation when room count matters to the comparison.

Apply only source-specific actual filters and returned tokens. Keep names, dates, occupancy, currency and rate basis with offers. Distinguish nightly from whole-stay prices and show excluded taxes/fees when returned; unknown charges are not zero. No stock or cancellation guarantee from a snapshot, and no reservation/payment actions.

For explicitly requested Airbnb rentals use `../airbnb-research/SKILL.md`; homes for sale or long-term housing use `../property-research/SKILL.md`.
