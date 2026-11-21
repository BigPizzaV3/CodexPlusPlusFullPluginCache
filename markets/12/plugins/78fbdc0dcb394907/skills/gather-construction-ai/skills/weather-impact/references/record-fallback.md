# Per-Record Weather Fallback

Load only when Step 2's `dashboardShiftTable` response has **no weather field** (verified per
Pattern 12), or the user explicitly asks for per-shift weather detail (narrative-level
conditions or photos) that the dashboard report does not carry.

Fall back to `getShiftRecords` (paginated, 25/page) to enumerate shifts in the period, then
`getShiftRecord` per shift for the weather/narrative fields. Both are limited to **2 requests
per second** — pace the loop and warn the user of the approximate wait per **Pattern 4
(Pagination and Rate Limits)** from `../../../shared/patterns/04-pagination-rate-limits.md`.
Quote only the fields you need (weather, narrative excerpt, shift start/end) into the
transcript — never the full record JSON.

Once records are collected, proceed to Step 3's classification rules using the per-record
weather and narrative fields in place of the dashboard's columns. `shift_analytics.py` expects
report-shaped rows (date, weather-derived duration fields); when working from raw
`getShiftRecord` fallback data, run the manual classification in Step 3 instead of the script,
or reshape the collected records into the same row shape before running it.
