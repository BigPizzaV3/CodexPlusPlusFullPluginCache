---
name: get-started
description: Introduce Powder Union and show what it can do. Use when the user first adds Powder Union, asks what it does, or asks how to check snow conditions at European ski resorts.
---

# Get started with Powder Union

Powder Union gives snow reports for more than 650 European ski resorts, using modelled snowfall from Open-Meteo (refreshed every 6 hours) and observed snow depth from Swiss SLF stations. All values are in centimetres.

When the user is new, explain briefly what they can ask, then offer to run one example:

- **One resort:** "How's the snow in Val Thorens?" (uses the snow-check skill: recent snowfall, 7–10 day forecast, best day to go, season vs normal).
- **Where to ski:** "Where in Austria will it snow most this week?" (uses find-best-snow: ranks resorts and compares the top picks).
- **Weekly roundup:** "Give me this week's European snow briefing." (uses weekly-snow-briefing).

If the user names a resort straight away, skip the introduction: call `search_resorts`, then `get_resort_snow`, and answer.

Always link the resort's page on powderunion.eu from the result. Powder Union doesn't provide lift status, opening dates, prices or avalanche advice; for off-piste plans, point to the local avalanche bulletin included in each resort report.
