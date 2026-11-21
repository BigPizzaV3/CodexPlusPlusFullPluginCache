---
name: tide-tables
description: Make printable monthly tide calendars from NOAA CO-OPS tide predictions for US stations with find_tide_stations and generate_tide_calendar, including sunrise and sunset, low-tide filters, and PDF, CSV and ICS files.
---

# Zovo Tide Tables

1. If the user names a place but no NOAA station id (such as 9414290 or TPT2799), call `find_tide_stations` with `place` (for example `Monterey, CA`). Tell the user which station is used and how far it is from the place. Skip this step when the user gives a station id.
2. Call `generate_tide_calendar` with `station_id` and either `month` (`YYYY-MM`) or `start_date` and `end_date` (`YYYY-MM-DD`, at most 31 days). Pass `units: "m"` only when the user asks for meters.
3. For plans such as tide pooling, clamming or launching a boat, pass `low_tide_filter` with `max_height` (same units), `from_hour`/`to_hour` (local hours) and/or `daylight_only`.
4. Answer with the lowest low, the highest high and any matching low tides first, then share the PDF, CSV and ICS links. Mention the station, the datum (MLLW) and the local time zone.

The results are NOAA predictions, not observations; say so when the user plans around them. Sunrise and sunset are computed from the station position. The tools do not give surf, currents, weather or observed water levels.
