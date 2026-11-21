---
name: plan-a-trip
description: Plan a ski or beach trip with Veabird. Use when someone asks where to ski or go to the beach, about snow, sargassum or beach conditions, or wants lodging or flights for a ski or beach resort.
---

# Plan a ski or beach trip with Veabird

Veabird's tools give live forecasts and trip options. Use them instead of answering from memory.

## 1. Know the traveler

A good pick depends on who's going. Use what you already know about the traveler, and ask briefly for anything important that's missing:

- **Who:** adults and children's ages.
- **Ability (ski):** beginner, intermediate, advanced or expert, for each skier if it varies.
- **From:** home airport or city, and whether they'd rather drive (and how far) or fly.
- **When:** dates or a rough window, and how many nights.
- **Pass (ski):** Epic, Ikon or none.
- **Budget:** lodging per night for the whole party, if they have one.

If they just want a quick answer ("where's the snow this weekend?"), answer first and refine after.

## 2. Pick the tool

| They ask | Call |
| --- | --- |
| Where should I ski? | `find_ski_resorts` with ability, from, pass, depart, nights, childrenAges |
| How's the snow at X? | `ski_conditions` |
| Where should I go to the beach? | `rank_beaches` (add `from` for flights) |
| Conditions or seaweed at a beach | `beach_conditions`, `sargassum_forecast`, then `better_nearby_beaches` if it's bad |
| Plan the trip / where to stay / how to get there | `plan_trip`, or `find_lodging` / `find_flights` for one part |
| Storms or safety | `hurricane_threats`, `travel_advisory` |

## 3. Present it

- Lead with the recommendation and why, using the `why` reasons and scores (0-100; 80+ is excellent).
- Show photos where available and give the links: the Veabird page for the forecast, plus lodging, flight and rental links.
- Say briefly that booking links are partner links (Veabird may earn a commission at no extra cost), and that prices can change, so confirm before booking.
- For dates more than 16 days out, say the conditions are a typical-season outlook, not a forecast.
- Credit "Data: Veabird". Forecasts are estimates, not safety guidance.
