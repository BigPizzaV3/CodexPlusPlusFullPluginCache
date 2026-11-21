---
name: explore-the-world
description: Discover radio from around the world with Spinn Radio, either by spinning the globe for a random live station or by opening the interactive station globe. Use for "surprise me", "somewhere new", "random station", "radio around the world", or "show me the globe".
---

Use this skill for open-ended discovery.

- "Surprise me", "random", "somewhere new", "spin the globe": call `spin_the_globe`. Pass `country` or `genre` only when the user narrows it ("a random station in Brazil", "random jazz").
  After it lands, give one or two sentences about the place or the station's style, without inventing facts about the station itself.
- "Show me the globe", "explore", "map of radio": call `open_globe`, optionally with `country` to centre it. The user can drag the globe, tap any dot to listen, and press Spin inside it.
- If the user wants several options from one region instead of one random pick, use `search_stations` with that `country` and then `show_station_cards`.

Keep the commentary short: the user came to listen.
