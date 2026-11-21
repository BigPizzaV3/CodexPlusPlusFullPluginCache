---
name: weather-history
description: Find reporting US weather stations and generate daily historical weather logs with Excel and CSV downloads for cities, ZIP codes, addresses or station IDs.
---

# Zovo Weather History

Use `find_weather_stations` to find stations near a US city and state, ZIP code or street address for a date range. Dates are YYYY-MM-DD. Without dates it uses the thirty days ending five days before today UTC. Show coverage, distance and reporting elements.

Use `generate_weather_log` with `sites`, `start_date` and `end_date` for daily observations and Excel and CSV files. The sites may also be US station IDs such as USW00094728. Up to five sites and 366 calendar days per call; start dates must be on or after 1900-01-01. Threshold defaults: rain 0.10 inch, snow 1.0 inch, heat 90 F, freeze 32 F, peak gust 40 mph. A weather day meets any selected rule, default rain or snow. Preserve user thresholds.

Present one summary per site, per-site errors, the source URL and UTC retrieval time, and both download links (expire in about an hour). Observations are at a station; say its distance from the matched place. Missing or QC-failed data does not count in totals or thresholds. T denotes trace, contributes zero, and does not count as a rain or snow day. Keep QC flags visible. Some stations lack wind and gusts. Cooperative observation days may end at 7 a.m.; read the Source sheet note. Recent days can be not yet published, typically with a two to seven day delay. These are observations, not a certified weather report.

Do not use these tools for forecasts, current conditions or places outside the US.
