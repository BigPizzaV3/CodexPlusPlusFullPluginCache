---
name: find-best-snow
description: Find and compare European ski resorts with the best snow. Use when the user asks where to ski, where the most snow is or will be, which resort to pick for a trip, or wants two or more resorts compared, in Europe or a specific country or region.
---

# Find the best snow

Uses the Powder Union connector. All values are centimetres of modelled snowfall.

1. **Pick the metric from the user's timing:**
   - Going in the next few days or "this weekend": `next7d`
   - Going in about 1–2 weeks: `10d`, and say forecasts that far out are uncertain
   - "Where has it snowed" / fresh snow now: `7d` (or `24h` for today)
   - Overall snow-sureness this winter: `season`
2. **Narrow the area.** For a region, call `list_regions` once if you need the region id. For a country, use `get_country_snow` with the ISO code (AT, CH, FR, IT, ...).
3. **Get candidates.** Call `get_top_snowfall` with the metric, `limit` 10 and the region id if there is one. For a country, rank its resorts from `get_country_snow` instead.
4. **Check the top 3–5.** Call `get_resort_snow` on each shortlisted slug. Prefer resorts that do well on both the forecast and the season to date, and mention `bestDayToGo`.
5. **Answer with a short table** (resort, region, next 7 days, season vs normal, best day), then a 2–3 sentence recommendation. When comparing resorts the user named, use the same table for just those resorts.
6. **Link** each resort's `citationUrl`. For off-piste or touring plans, point to each resort's `avalancheBulletin`.

Size matters to many skiers: include `pisteKm` when picking between similar options. Don't claim lift or piste status, prices or opening dates; the connector doesn't provide them.
