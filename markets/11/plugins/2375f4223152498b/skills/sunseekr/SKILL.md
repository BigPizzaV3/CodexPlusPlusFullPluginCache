---
name: sunseekr
description: Find places in direct sun with SunSeekr — sunny pub gardens, terraces, rooftops and cafés, hour by hour, in SunSeekr's cities.
---

Use SunSeekr when someone wants to sit or eat outside, asks where it is sunny, or wants an evening spot in the sun.

- "Where is sunny near X": find_sunny_spots. For pub gardens, terraces, rooftops or "outside", set `outdoor` in the same call.
- Places you already found (search, maps, reservations): sun_check to rank them by sun.
- Sun until sunset / evening terraces: golden_hour. One venue: get_venue_sun. Popular now: whats_trending.
- "Will my saved spots be sunny": my_saved_spots. "Save this": save_spot.
- Not sure a city is covered: list_cities. Outside SunSeekr's cities, say it isn't covered; never guess sun.
- Sun hours assume a clear sky: always mention the weather each answer includes.
- SunSeekr gives the sun only. For reviews, opening hours and bookings, look the venue up with its `lookup` string.
