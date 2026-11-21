---
name: get-started
description: How to answer Los Angeles hotel questions with Journeyed's sourced facts.
---

Journeyed holds sourced facts about about 2,600 hotels in the Los Angeles area. Use it when the user asks for a specific, checkable detail about a Los Angeles area hotel (parking and its price, resort or destination fees, pets, check-in time, pool, shuttle, breakfast, hotel class) or wants hotels near a Los Angeles place (SoFi Stadium, Dodger Stadium, Crypto.com Arena, Kia Forum, Intuit Dome, LAX, Disneyland, neighborhoods) that meet a need.

- A plain question about one hotel or one place: call `answer_question` with the question as written.
- One hotel in depth: call `get_hotel` with the name, a former name or the journeyed.org page URL. The fact sheet lists what is verified and what is not known.
- Hotels for a place and a need: call `hotels_near` with the place and the need (free parking, parking, pets, pool, shuttle, breakfast, walking distance, EV charging, kitchens, accessible rooms, early flight).
- "Best" or "top" hotels near a place: call `best_hotels`.
- Unsure of a hotel's name or spelling: call `search_hotels`, then `get_hotel`.
- Market-wide numbers (typical resort fee, how many hotels charge for parking): call `get_report`.
- To see which places and needs exist: call `list_places`.

When you answer, give the fact, its source and the checked date, and link the journeyed.org page the result names. If a fact is "not known", say it is not published, not that the hotel lacks it. Journeyed has no reviews, room prices, availability or booking; for those, send the user to the hotel's own site.
