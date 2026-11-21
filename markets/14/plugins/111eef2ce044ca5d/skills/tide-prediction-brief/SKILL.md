---
name: tide-prediction-brief
description: Prepare a NOAA astronomical tide prediction brief for a station and bounded dates, or compare its predictions with matching observations. Use when users need tide times, predicted levels and the meaning of the selected datum, units and local clock, with station capability and coverage limits.
---

# Tide prediction brief

Make a usable, dated tide table or a qualified observation comparison without turning astronomical predictions into a weather or flooding forecast.

1. Confirm station or public research point, dates, desired high/low table versus sampled series, units, datum and time zone. Use `find_tide_stations_near_point` with `station_type: tide_predictions` when station selection is needed. Explain distance and capability; do not substitute a nearby gauge silently or solicit a home address/device location.
2. Check `get_station_datums` and station capability metadata. Preserve station datum labels, units and published epoch; absent datum/epoch stays unknown. Known subordinate stations require high/low predictions and MLLW in this service. Do not force another interval or datum from an unsupported station.
3. Use `get_tide_predictions` with explicit arguments: `high_low` allows at most 31 calendar days, `hourly` seven, and `six_minute` two. State any narrowed window or product change. `local` follows station local/daylight-saving convention, `local_standard` does not adjust for daylight saving, and `gmt` is UTC. Keep the returned clock label next to times; do not invent missing UTC offsets or silently convert ambiguous DST times.
4. Present requested versus returned coverage, high/low type or sampling interval, predicted height and exact datum/units, station/source link and retrieval/cache provenance. Distinguish source dates and prediction period from fetch time. Null/failed/missing data are not zero tides. Do not label astronomical predictions as observations, water-level weather forecasts, storm-surge predictions or safety advice.
5. For a requested comparison, call `get_observed_water_levels` using the same station, datum, units, clock and compatible interval. Pair only matching timestamps with numeric values; give the number of pairs and unmatched/missing rows. Do not pair repeated local DST clock times ambiguously; use a compatible unambiguous time basis or leave the comparison unresolved. Explain observation quality flags and preliminary versus verified status. Label observed-minus-predicted differences with units and scope; do not call them an independently established storm surge, causal weather effect or site flood depth.

Conclude with what the table supports: station-level astronomical tide research on the requested dates. No transfer of station datum offsets to arbitrary inland ground, no property certification, flood-zone or insurance determination, and no guarantee of safe boating or flood-free conditions. For operational decisions, point to the responsible official service without inventing a live alert check.
