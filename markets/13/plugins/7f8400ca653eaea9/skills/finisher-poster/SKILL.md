---
name: finisher-poster
description: Draw a Routeframe finisher poster of a marathon or half marathon the user ran, with the course traced from OpenStreetMap, the city, distance, year, the runner's name and finish time, then change the style, units or note in the card. Use when someone wants a marathon poster, half marathon poster, race map poster or course map of a race they ran, or asks which races Routeframe has.
---

Use this skill when the user wants a poster of a race they ran. The user's explicit instructions always come first.

## Flow

1. Ask for anything missing among the race, the year, the runner's name and the finish time. Routeframe has no race results, so the name and time come from the user exactly as given.
2. `find_race` identifies the race by name, city or country and returns the years available; with an empty query it lists the whole catalogue of marathons and half marathons.
3. `preview_poster` draws the poster and shows it in a card. The user can switch among six colour styles, miles or kilometres, the year and a short line of their own such as "First marathon", in the card or by asking.
4. The poster is its design and its preview in the card; there is no file to download.

## Scope

- Marathons and half marathons in Routeframe's catalogue only; if a race is missing, say so and offer `find_race` for nearby ones.
- Routeframe is not affiliated with any race or its organisers; posters name the city and distance, not a race's marks.
- `delete_my_data` only when the user asks to delete their Routeframe data.
- The tool results say what this user can do with the poster.
