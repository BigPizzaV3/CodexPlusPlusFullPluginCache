---
name: tours
description: Find, explain and compare bookable tours and activities with Adónde, checked against the operator's published schedule. Use when the traveller asks what tours or activities run in a city or on a date, asks about one tour (start times, pickup, ages, languages, cancellation), or wants tours side by side.
---

# Tours with Adónde

## Searching

- Call `search_tours` with the city and a date. With a date, only tours whose operator runs them that day come back, with their departure times. Ask for the date if the traveller has one in mind; a trip's dates come from the trip.
- Pass the traveller's interest as `query` ("food", "boat", "Douro wine").
- The default is 8. For more, page with `limit` and `offset`, and say only as many exist as the result returned.
- Inside a trip, offer tours only after stays, for the same dates.

## One tour in depth

Call `get_tour_details` with its product code (from `search_tours` or a menu id): photos, what is included, meeting point, pickup, start times on the day, price per adult and child, ages, languages and the cancellation policy.

## Comparing

Call `compare_tours` with two to four product codes: price per adult and child, rating, duration, whether each runs on the first day and its start times, pickup, meeting point, group size, languages and cancellation. Present the rows that matter.

## Answering questions

- Answer only from the returned fields and name the tour each answer is about.
- "Does it run on the 14th?" is answered from the schedule the tool returns, never assumed. A tour that runs on none of the traveller's days is not offered.
- Tours carry a score and review counts but no review text; do not describe what reviewers said.
- If a field is absent, say it is not stated and suggest asking the operator.

## Booking

Hand over the result's own `book_link` on getadonde.com. Booking happens there, not in the chat.
