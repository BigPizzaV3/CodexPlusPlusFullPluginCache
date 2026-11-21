---
name: find-hotels
description: "Search and compare live TravelYalla hotel prices by city or hotel name, filter by stars, guest score, price or distance, and give travelyalla.com booking links. Use for any request for hotels, stays, accommodation or a hotel's details, in English or Arabic (فنادق، فندق، حجز فندق، إقامة، أرخص فندق), especially in Egypt, Saudi Arabia (including Makkah and Madinah) and the Gulf."
---

# Find hotels

Tools: `search-destinations`, then `search-hotels`, then `get-hotel-details` for a hotel the user wants to know more about.

Explicit user instructions take priority over the defaults here.

## 1. Collect the stay

You need these before searching:

- **Destination.** A city, area or hotel name.
- **Check-in and check-out dates.** Resolve relative dates against today's date. Never use past dates. "Next weekend" means Friday to Sunday unless the user's region suggests Thursday to Saturday. State which dates you used.
- **Guests per room.** If the user doesn't say, assume 2 adults in 1 room and tell them so. Children need their ages, from 0 to 17.

If the destination or the dates are missing, ask for them in one short question.

## 2. Resolve the destination

Call `search-destinations` with what the user said.

- Take a hit with `type: "city"`. Use its `code` as `city` and its `country.code` as `country_code`.
- If the user named a hotel, take the hotel hit's city code and country, and remember the hotel's name so you can find it in the results.
- If several cities share the name, for example London in GB and London in US, pick the one the context points to. Ask if it's unclear.

## 3. Search

Call `search-hotels` with:

- `city`, `country_code`.
- `check_in`, `check_out` as `DDMMMYYYY` in upper case, for example `16OCT2026`.
- `rooms`: one entry per room, for example `[{"adults": 2, "children": [7]}]`.
- `nationality`: the guest's own country as ISO-2, not the destination's. Rates and the default currency depend on it. Use it if known. Otherwise search anyway and offer to re-run.
- `currency`: only if the user asked for one. Never default to the destination's currency.
- `language`: `ar` when the user writes in Arabic.
- `sort_by` and `sort_dir`:
  - `price` / `asc` for "cheap" or "budget"
  - `stars` / `desc` for "luxury" or a star level
  - `rated` / `desc` for "best" or "top-rated" (also the default)
  - `distance` / `asc` for "central" or "near the centre".
- `limit`: 10. Raise it when filters leave too few results.

The search takes about 20–30 seconds, so tell the user once.

If the search fails (for example "no provider answered"), retry once. If it still fails, say so and suggest other dates. Never invent hotels or prices.

## 4. Present the results

Show the 3–6 best matches. For each one, give:

- `name` and `stars`
- guest score as `review_score` from `review_count` reviews, when present
- `distance_to_center_km`, when present
- price per night (`night`) and the stay total (`total` for `nights` nights) in `currency`.

Apply the user's filters to the returned data, such as stars, maximum price or minimum score, and say how many hotels matched. Prices are live and can change until booked.

For a landmark such as "near the British Museum", `distance_to_center_km` measures distance from the city centre, not from the landmark. Use `get-hotel-details` coordinates for the top few candidates and describe nearness only approximately.

## 5. Details

Call `get-hotel-details` with a hotel's `code` when the user asks about it. Report its address, check-in and check-out times, and facilities.

Room types, board and cancellation terms are not available here. Send the user to the hotel's page for those.

## 6. Booking link

Give each hotel you recommend a travelyalla.com link built as described in [references/booking-links.md](references/booking-links.md). The user books and pays on the website. Never collect payment details in the chat.
