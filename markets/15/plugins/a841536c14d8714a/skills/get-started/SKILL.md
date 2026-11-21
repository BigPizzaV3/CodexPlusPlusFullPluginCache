---
name: get-started
description: What the four Bluesun tools return, which prices are live, and where a stay is booked.
---

Bluesun has 14 properties on the Croatian Adriatic: eleven hotels, two holiday villages and Camping Paklenica (pitches and mobile homes), in Tučepi and Brela (Makarska Riviera), Bol (Brač) and Starigrad-Paklenica. All four tools are read-only.

- `find_hotels` lists the brand's hotels by destination, stars, budget, party size or a free-text wish, with photos, a nightly from-price and the current brand offers.
- `get_hotel` returns one hotel's profile, amenities, photos and room types with their occupancy. It takes the hotel's name, so a hotel the guest names needs no search first.
- `get_availability` reads the brand's live booking system for one hotel: with a check-in date, the rooms and rate plans free for that stay and party with exact totals; without one, the cheapest dates and monthly minimum prices over the months ahead.
- `get_price_quote` returns the exact total, board and cancellation policy for a room and rate plan taken from `get_availability`.

The from-price in `find_hotels` is the hotel's year-round lowest nightly starting price: it is not tied to any dates and does not rank hotels for a stay. Prices from `get_availability` and `get_price_quote` are live for the dates and party asked about, as are `find_hotels` totals with `price_for_stay` and a check-in date.

Booking is completed on the official Bluesun website, www.bluesunhotels.com, through the link the results return. No tool takes payment details or makes a reservation.

Starter prompts:
- Which Bluesun hotel on the Makarska Riviera is best for a family with young children?
- When is the cheapest week to stay at Bluesun Hotel Elaphusa on Brač?
- Tell me about Maestral Adults Exclusive Hotel and its rooms.
