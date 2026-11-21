---
name: weekly-snow-briefing
description: Write a short European ski snow briefing for the week. Use when the user asks for a snow roundup, this week's snow news, a ski conditions summary for Europe, or content for a newsletter or social post about snow.
---

# Weekly snow briefing

Uses the Powder Union connector.

1. Call `get_weekly_summary`.
2. If the user cares about specific regions, call `get_region_snow` for each one.
3. Write the briefing in this shape, about 150–250 words unless asked otherwise:
   - **Headline:** the single biggest story (biggest dump, standout forecast, or "quiet week").
   - **Last 7 days:** the leaders, with cm and region.
   - **Next 7–10 days:** where snow is forecast and roughly how much.
   - **Region by region:** one line each for the regions in the summary's outlooks.
   - **Best bet:** one resort or region to watch, with its best day.
4. Use centimetres, name the resorts, and link `https://powderunion.eu/this-week` as the source.
5. Early or late in the season (October–November, April–May), say plainly when most resorts are closed and the numbers are pre-season snowfall.
