---
name: fixture-time-planner
description: Convert Cricket Explorer fixture start times into one or more local time zones and produce a copyable agenda when the user asks when matches start where they live, across cities, or after a date change. Require trustworthy GMT timestamps and resolved time zones; do not create calendar events, reminders, or guessed start or finish times.
---

# Fixture Time Planner

Turn returned fixture start timestamps into an agenda with explicit dates, time zones, and day changes.

## Inputs and retrieval

1. Reuse the requested match rows from tool results or `widgetState.modelContent.selectedMatch`. For a series, use returned `structuredContent.selectedSeries.matches`; the selected series in widget state contains no fixture list.
2. If details are missing but an ID is known, call `open-cricket-explorer` with `reason` and either `initialPanel: "matches"` plus `matchId`, or `initialPanel: "series"` plus `seriesId`. Check the returned selection rather than assuming the lookup succeeded.
3. If no ID is known, open the appropriate panel with `reason` and `initialPanel`, ask the user to select the entity, and use its next model-visible ID. Do not invent IDs or call the widget-only `get-cricket-data` tool.
4. Resolve the destination time zone or zones from the request. Use IANA names such as `Europe/London` and `Australia/Sydney`. Ask about ambiguous cities or abbreviations such as CST; language, country, and current device offsets do not establish a time zone for a future fixture.

## Convert the timestamps

1. Use `dateTimeGmt` as the source instant. Interpret an offset-free timestamp in that field as UTC; honor an explicit offset when supplied. Require a full calendar date and time. Never manufacture midnight from `date` or infer a missing year.
2. Use the bundled [scripts/convert_fixtures.py](scripts/convert_fixtures.py) when local Python execution is available. It uses Python 3.9 or later and the system's IANA time-zone database through `zoneinfo`, with no third-party Python packages.
3. Extract the returned rows into a temporary JSON array containing their `id`, `name`, `date`, and `dateTimeGmt`. Resolve the helper path from this skill directory. For example, run from this directory:

   ```bash
   python3 scripts/convert_fixtures.py --input /tmp/cricket-fixtures.json --timezone Europe/London --timezone Australia/Sydney
   ```

4. Read the helper's JSON result. Use `utcStart` and each `localStarts` entry's `dateTime`, `timeZone`, `abbreviation`, and `dateShiftDays`. Keep rows marked `missing` or `invalid` unresolved. Invalid destination zones fail the command instead of silently substituting another zone.
5. If the helper cannot run, use another available standard time-zone facility with date-specific IANA rules. If no reliable conversion facility is available, retain the source timestamps and explain that local conversion is unresolved. Do not guess daylight-saving offsets.
6. Sort valid instants chronologically, deduplicate match IDs, and preserve each local calendar date. Show the numeric offset alongside the zone name when a repeated clock time could be ambiguous.

## Deliverable

Provide a copyable table of fixture, UTC start, and a dated local start for each requested time zone. Highlight local day changes and list unresolved fixtures separately, preserving a trustworthy source date only as an unconverted date.

Label times as reported starts from data potentially cached for up to 24 hours. A conversion establishes neither a fresh schedule nor a confirmed future start if status and timing conflict. Keep start times distinct from match duration or daily sessions; the app supplies no finish times or calendar-writing capability.
