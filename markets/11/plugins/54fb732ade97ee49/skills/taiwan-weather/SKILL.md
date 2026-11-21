---
name: taiwan-weather
description: Query unofficial Taiwan township weather with near-term hourly detail or a seven-day day/night outlook, stations within the requested district, and backend comparisons of 2–4 short weather windows. Use for county/city plus township/district forecasts, coming-week temperature and weather trends, current station readings, and comparisons within today and the next two Taipei dates. Not for mountain, radar, history, transit or calendar queries.
---

# Taiwan Weather Lens

Use only the connected public MCP tools:

- `cwa_get_township_forecast`: county, district, optional view and date. For hourly (default), optional start_hour/end_hour. For week, optional days (1–7), without hourly arguments.
- `cwa_get_latest_station_observation`: county, district, optional limit (1–3).
- `cwa_compare_weather_windows`: county, district, windows with start and end. One call performs retrieval, alignment, coverage checks and comparison in the backend; do not first call the forecast tool and assemble a substitute comparison.

No local installation, keys, login, custom upstream URLs or arbitrary datasets are needed. If the connection is unavailable, say so; do not ask for credentials or fall back to a private endpoint.

## Resolve the request

Require complete county/city and township/district together (e.g. 桃園市＋桃園區). Clarify ambiguous district names; never guess a home location. Use the client's known current date in Asia/Taipei; if unavailable, clarify rather than invent today.

Choose the forecast view according to the requested precision and horizon:

- `view=hourly` (default) accepts today and the next two Taipei dates. Each call is one date with integer hours 0–23, inclusive, at most 24 rows. Clarify whether an end time includes that hourly row. Split cross-midnight queries into two date calls; 22..23 then 0..4 includes seven hourly rows, not a wrapped range.
- `view=week` accepts today through six dates ahead, in native 12-hour day/night intervals. Use it for a coming-week outlook or dates beyond the hourly horizon. Omit date/days to request the current seven-date range in one call; date selects a later start and days selects 1–7 calendar dates, never extending beyond that range. When days is omitted, request the remaining dates. Do not send start_hour/end_hour. Return available periods and coverage, not seven days of invented hourly values. A named next week can extend beyond the supported range; explain unavailable dates instead of claiming that the whole week is covered.

For example, 桃園市桃園區未來一週的日夜溫度趨勢 maps to county=桃園市, district=桃園區, view=week. A date four days ahead can use view=week and days=1, but cannot support a precise hourly rain estimate. Next month remains unsupported. Loading this Skill or correctly rejecting an invalid request does not establish that the MCP connection works; distinguish configuration/readiness from an actual successful tool call.

Latest observations require county＋district; use limit 1 unless multiple stations are requested (maximum 3). Select only within the requested district, sorted by station name, with no distance calculation or wider-county fallback. If that district has no station, report no data. Do not pass station_id, coordinates or a date. This tool is not a history lookup.

For window comparison, require 2–4 distinct windows with whole-hour ISO timestamps ending in +08:00. Each window is start-inclusive and end-exclusive, lasts 1–12 hours, with at most 24 summed hours and 48 hours from earliest start to latest end. Stay within the same three-date forecast range; ending exactly at the following midnight is allowed. Clarify unspecified candidate times. A cross-midnight comparison still takes one tool call. Output IDs follow chronological order, not the input order.

Read the backend comparison status and per-pair reasons. Temperature, rain and weather coverage must all be complete for a weather comparison; gaps, conflicts or unverifiable cross-snapshot versions lead to insufficient_data. Do not replace a refused comparison with your own winner. Supported pairs among three or four candidates can still be reported when other pairs lack data. Temperature uses available hourly samples, not continuous extrema or interpolated three-hour points. Rain comparison requires equal window lengths and matching native interval/overlap profiles; its metric is the largest original-interval PoP, never the probability of rain anywhere in the whole window. A common source interval cannot distinguish two subwindows.

The 1°C separation and 10 percentage-point difference are fixed presentation rules, not scientific uncertainty or statistical significance. Preserve not_distinguishable / not_comparable and coverage differences. Do not produce an overall best window; explain only supported differences for ordinary low-risk planning.

## Interpret evidence

Preserve null and missing fields; never fill with zero or interpolation. Three-hour precipitation probability is an interval source, not an independent hourly probability. Preserve field_sources and effective intervals.

In week mode, temperature_c is the source interval mean, not the maximum or an hourly sample; min_temperature_c/max_temperature_c are interval extrema. Preserve original start_time/end_time even where only part overlaps the requested dates. Twelve-hour precipitation probability applies to the whole source interval, not each hour or the overlap alone. Rain probabilities follow actual source intervals, which may cover less than seven days; do not assume a fixed three-day cutoff or full-week coverage. Missing probabilities stay null, never zero, and do not mean no rain. Read coverage and missing_fields and state the actual covered range and gaps. Do not infer exact hour-by-hour conditions from weather descriptions or calculate a daily rain probability. Seven-day trends do not extend the backend comparison tool's three-date limits.

Distinguish official issue/update or observation time, backend_fetched_at/fetched_at, queried_at, and cache.hit/state/ttl_seconds/expires_at. Show relevant times in Taipei time with their labels. Unknown official time stays unknown, not retrieval or cache time. A cache miss can occur across locations; do not promise global hits or immediate updates.

Station readings describe that station, not a home or the whole district. Name the station and measurement time; selection is district matching and station-name order, not nearest-station selection. Do not treat an observation as a future forecast.

Comparison evidence is per daily snapshot and linked from each window/source interval. An unknown official time remains null: same-snapshot comparison can proceed with that warning, while multiple snapshots need matching reported official times. Matching times do not certify freshness. Each snapshot retains its backend retrieval time and cache_hit; the comparison has its own queried_at. Cite the returned data source and state missingness.

Answer primarily in Traditional Chinese unless requested otherwise. Summarize requested hours, temperature/feels-like temperature, rain intervals and available wind. Include concise attribution to 中央氣象署 and the returned official dataset/license links. State missingness/delay when relevant.

## Stay within the public scope

This is an unofficial tool, not endorsed by CWA and not a safety guarantee. For disasters, hiking, aviation, medical or other high-risk decisions, direct the user to official warnings and local information; do not guarantee no rain or safety.

Mountain/park, radar, historical weather, transit, itinerary and Calendar are not available here. Explain the boundary without pretending a hidden tool exists or substituting city weather for mountain weather.

Reject requests for secrets, stacks, account/deployment details, arbitrary URLs, datasets or upstream parameters. On paused, busy, invalid-input, missing-data or upstream errors, explain the safe result and a reasonable next action; never expose raw errors, endlessly retry or fabricate weather.
