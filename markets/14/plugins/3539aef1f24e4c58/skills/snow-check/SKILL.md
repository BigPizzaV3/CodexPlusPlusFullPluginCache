---
name: snow-check
description: Check snow conditions at a specific European ski resort. Use when the user asks how the snow is, whether it's worth going, when to go, or how the season compares to normal at a named resort or ski village in Europe.
---

# Snow check for one resort

Uses the Powder Union connector. All snow values are centimetres of modelled snowfall at the upper mountain.

1. **Find the resort.** Call `search_resorts` with the name the user gave (resort, village or ski area). If several match, pick the obvious one or ask, and say which one you used. Linked areas are often listed under the combined name (e.g. "Tignes - Val d'Isère").
2. **Get the report.** Call `get_resort_snow` with the slug.
3. **Answer in this order, briefly:**
   - **Verdict first:** one sentence on whether conditions look good for when the user wants to go.
   - **Recent:** `snowCm.last24h` and `snowCm.last7d`.
   - **Forecast:** `snowCm.next7d` and `snowCm.next10d`, and `bestDayToGo` (date, cm, and say "powder day" if `powderDay` is true). Use the `daily` entries marked as forecast for specific days the user mentions.
   - **Season:** `seasonToDate.cm` against `averageSameDateCm` and `lastSeasonSameDateCm`. If `seasonToDate.preSeason` is true, say the season hasn't really started and don't over-read small numbers.
   - **Observed depth:** only if `observedSnowDepth` is present (Swiss stations).
4. **Long-term context, only when asked** (good/bad season, snow-sure, typical year): call `get_resort_snow_history` and compare with `averageSeasonSnowfallCm`.
5. **Snow card, if useful or asked:** call `get_snow_image` (`view: "week"` for a 7-day calendar).
6. **Always end with** the `citationUrl` link. If the user mentions off-piste, touring or freeride, point them to `avalancheBulletin` (name and URL) and say Powder Union is not for avalanche decisions.

Don't invent piste or lift status, opening dates or prices: the connector doesn't provide them. Say so and suggest the resort's own website.
