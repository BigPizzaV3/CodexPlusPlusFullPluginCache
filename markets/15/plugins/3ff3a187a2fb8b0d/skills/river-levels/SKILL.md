---
name: river-levels
description: Check current USGS river flow and gage height with find_river_gauges and get_river_conditions, compare with past years for the same date, and download a PDF condition sheet and CSV of readings.
---

# Zovo River Level Check

Use `find_river_gauges` when the user does not know the USGS site number. Pass `state` (two-letter code, e.g. `CO`) with optional `name` words from the river (e.g. `Arkansas`), or a US `place` such as `Boulder` with optional `state` and `radius_miles` (1 to 50, default 15). Coordinates are not accepted. Say which city was matched.

Use `get_river_conditions` with `site_ids` (1 to 10 USGS site numbers such as `01646500`) and optional `days` (1 to 7, default 7). Report for each gauge the latest discharge (ft3/s) and gage height (ft) with the local time, the 24-hour trend, and the percentile band and percent of median for this calendar day. Give both download links and say they expire in about one hour.

Say that recent readings are provisional and that the percentile band compares an instantaneous reading with daily-mean statistics. When a gauge shows "source unavailable", say that USGS did not answer and do not estimate values. This is not a flood warning or a forecast: point users to National Weather Service warnings for safety decisions.
