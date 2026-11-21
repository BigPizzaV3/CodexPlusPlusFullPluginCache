---
name: plan-a-trip-map
description: Build or extend an Ikuzo map of real places for a trip, a city or a theme. Use when the user asks to make a map, add places to a map, or turn a list or an article into spots.
---

# Building a map of real places

1. Find the map: call `maps_list`. Use the map the user names; if they want a new one, call `maps_create` with a short, clear title.
2. Call `schema` once to know the valid types and statuses.
3. For every place, call `places_search` with the place name and a location near it, and use the returned coordinates and placeId. Never invent coordinates.
4. Add the places with `spots_create_bulk` (up to 10 at a time). Give each spot a fitting type, and the status the user asked for (To visit by default). Keep descriptions to one short sentence; Ikuzo shows text as is, without Markdown.
5. Finish with `maps_show`, so the user sees the map in the chat, and add at most one short sentence. Do not repeat the map, an image or the link.

Prefer fewer, well chosen places over long lists, and ask before adding more than 30 at once.
