---
name: get-started
description: What the four Sunčani Hvar tools return, which prices are live, and where a stay is booked.
---

Sunčani Hvar has seven hotels on the Croatian island of Hvar. All four tools are read-only.

- `find_hotels` lists the brand's hotels by stars, budget, party size or a free-text wish, with photos, a nightly from-price and the current brand offers.
- `get_hotel` returns one hotel's profile, photos and room types with their occupancy. It takes the hotel's name, so a hotel the guest names needs no search first.
- `get_availability` reads the brand's live booking system for one hotel: with a check-in date, the rooms and rate plans free for that stay and party with exact totals; without one, the cheapest dates and monthly minimum prices over the months ahead.
- `get_price_quote` returns the exact total, board and cancellation policy for a room and rate plan taken from `get_availability`.

The from-price in `find_hotels` is the hotel's year-round lowest nightly starting price: it is not tied to any dates and does not rank hotels for a stay. Prices from `get_availability` and `get_price_quote` are live for the dates and party asked about, as are `find_hotels` totals with `price_for_stay` and a check-in date.

Booking is completed on the official Sunčani Hvar website, www.suncanihvar.com, through the link the results return. No tool takes payment details or makes a reservation.

Starter prompts:
- Which Sunčani Hvar hotel is best for a couple wanting a quiet stay?
- When is the cheapest week to stay at Amfora?
- Tell me about Palace Elisabeth and its rooms.
