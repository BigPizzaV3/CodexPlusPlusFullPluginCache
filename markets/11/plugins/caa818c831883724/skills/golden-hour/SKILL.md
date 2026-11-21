---
name: golden-hour
description: Calculate local sunrise, sunset, golden hour, blue hour, twilight and day length for cities; plan photography shoots with ICS and CSV files.
---

Use `find_sun_times` for a city and local date. Use `plan_golden_hour_shoot` for a start date, 1–31 days and morning/evening/both. Use `compare_day_length` with two dates, or a year for local equinox and solstice dates.

Pass dates as YYYY-MM-DD. Resolve cities by name, optionally country or US state; do not ask for coordinates. The largest matching city is selected and alternatives are reported. If no date is supplied, use the current date in America/New_York and explicitly state that assumption.

Give the matched city, IANA time zone, requested times and downloads. Golden hour uses altitude -4° to +6°; blue hour -6° to -4°. Missing polar events do not occur on that date. Times assume a flat sea-level horizon; hills, buildings and weather change the observed light. Accuracy is about one minute below 66° latitude. City table covers population 50,000+ and dates cover 1900–2100. Midnight-clipped windows are marked. Files do not modify a calendar.
