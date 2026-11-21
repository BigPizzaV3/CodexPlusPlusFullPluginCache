---
name: hotels
description: Find, explain and compare hotels with Adónde. Use for any question about hotels, stays, where to sleep, resorts or neighbourhoods to stay in, with or without dates, for questions about one hotel (parking, breakfast, pets, check-in, children), and for "which is better, cheaper, closer or quieter".
---

# Hotels with Adónde

Every hotel question goes to `search_stays`, not a web or map search. Adónde shows real hotels with a Book link on getadonde.com.

## Searching

- **With dates:** call `search_stays` with the city (and `area`, `max_per_night`, adults) and the dates.
- **Without dates:** call it anyway. It returns real hotels for a labelled sample window and `needs: ["dates"]`. Show them, say the dates are a sample, and ask for the traveller's dates. A card's Set dates line ("Show me stays in ...", ending in a code) runs `search_stays` with that `intent_ref`.
- **Inside a trip:** after the days are built, read `next` in the `build_trip` or `get_trip` result, offer the first stop's stays with the budget and the recommended areas, and ask which area or "anywhere central".
- **Described stays:** pass the traveller's own words as `describe` ("quiet boutique with a rooftop pool, near the old town").
- **Filters:** `min_stars`, `min_guest_rating`, `min_per_night`, `max_per_night`, `refundable_only`, `breakfast_included`, `amenities`, `property_type`, `sort`. When nothing matches, the result shows the closest hotels and which filter each misses; say that.
- **More:** the default is 10. For N, pass `limit` N (up to 50). For "more", call again with `offset` set to the previous offset plus limit. Say only as many exist as the result returned (`total_available`, `has_more`).
- If `areas` is empty, offer "central" and the price bands (budget, mid, luxury) instead of inventing neighbourhoods.

## One hotel in depth

Call `get_stay_details` with its `hotel_id` and the same dates: photos, amenities, rooms and rates, and what the hotel states about check-in and check-out, pets, parking, children and extra beds, accessibility, payment and deposits, room sizes, and what guests say.

## Comparing

Call `compare_stays` with two to four `hotel_ids` from the search, the same dates and adults (and `distance_km` in the same order). Present the summary and the rows that matter to the traveller.

## Answering questions

- Answer only from the returned fields and name the hotel each answer is about.
- If the fields do not say (an amenity or policy is absent, a cell reads Not stated), say it is not known and suggest asking the hotel. Never guess an amenity, a policy, a room size or a review.
- For "quietest" and similar, use `review_highlights` and say it comes from guest reviews.

## Booking

Hand over each result's own `book_link`. Booking and payment happen on getadonde.com, never in the chat. Never substitute links from other booking sites.
