---
name: tune-in
description: Find and play a live radio station on Spinn Radio by station name, place, genre or mood. Use when the user asks to play, put on or listen to radio, a station, or music from somewhere. For podcasts use the podcasts skill; for books, the audiobooks skill.
---

Use this skill when the user wants to listen to live radio.

1. Turn the request into search terms:
   - A station name ("BBC Radio 6 Music", "WWOZ") goes in `query`.
   - A place goes in `city` and/or `country` (ISO 3166-1 alpha-2, e.g. `US`, `NG`, `JP`).
   - A genre goes in `genre` as a lowercase tag. Map moods to tags: chill → `chillout`, focus or study → `ambient` or `lofi`, workout → `dance`, sleep → `ambient`, party → `dance` or `pop`, news → `news`, talk → `talk`.
   - "Near me" or "local" → call `find_nearby_stations` instead.
2. Call `search_stations`. If nothing comes back, widen the search once (drop the city, keep the country; or drop the genre) before telling the user.
3. If one station clearly fits (the user named it, or one result is far better), call `play_station` with its id.
   If several fit, call `show_station_cards` with up to 6 ids, best first, and a short heading such as "Jazz in New Orleans".
4. After the player opens, say in one sentence what you chose and why. Playback starts when the user taps play; do not claim audio is already playing.
   If the result says the requested station is off air and a similar one was opened instead, tell the user which station is playing.

Don't invent stations or ids. Only use ids returned by Spinn tools.
