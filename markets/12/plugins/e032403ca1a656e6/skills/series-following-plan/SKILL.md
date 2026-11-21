---
name: series-following-plan
description: Build a practical shortlist of fixtures to follow from a Cricket Explorer series when the user wants a viewing plan around preferred teams, formats, dates, or available time. Use returned fixtures and stated preferences; do not promise streaming availability, complete coverage, reminders, or a match fitting wholly within a time window.
---

# Series Following Plan

Turn the available fixtures for one series into a small, prioritized plan based on the user's interests and availability.

## Inputs and retrieval

1. Identify the requested series and reuse stated team, format, date-window, and availability preferences. Ask for missing preferences only when they materially affect the shortlist; an unfiltered fixture overview needs no availability interview.
2. Obtain an actual fixture list from returned `structuredContent.selectedSeries.matches`. The selected series in `widgetState.modelContent` is a summary and does not include matches.
3. If only a series summary or its ID is available, call `open-cricket-explorer` with `reason`, `initialPanel: "series"`, and the observed or supplied `seriesId`. Check that the returned `selectedSeries` matches the intended series and contains usable fixtures.
4. If no ID is known, open the Series panel with `reason` and `initialPanel: "series"`, ask the user to select the series, and use its next model-visible ID to retrieve details. Never turn a name into an invented ID.
5. Leave `get-cricket-data` calls and Load more actions to the widget. Do not assume its local fixture cache or all loaded list pages are visible to the model.

## Build the plan

1. Scope the plan to the returned series and fixture rows. Deduplicate by match ID. Compare the number of returned rows with `matchCount` when available, and disclose a mismatch; a matching count alone does not prove complete coverage.
2. Apply explicit team and format preferences to actual `teams`, `name`, and `matchType` fields. Treat missing or `unknown` values as unresolved, not as matches for a preference.
3. Assess timing from trustworthy `dateTimeGmt` values. Interpret offset-free timestamps in that GMT field as UTC. Resolve the user's time zone before assessing local availability, and use a reliable time-zone conversion facility. Keep date-only or malformed timing outside exact time-window decisions.
4. Check `matchStarted`, `matchEnded`, and status before describing a fixture as upcoming. Treat contradictory or stale-looking timing and status as uncertain. Responses may be cached for up to 24 hours.
5. Rank eligible fixtures by the user's expressed preferences. Explain each choice using supported facts such as team, format, date, or start-time fit. Avoid invented stakes, team form, rivalries, or broadcast access.
6. Describe a start time falling within a window as a start-time fit. The app provides no duration, finish time, daily Test schedule, weather forecast, or streaming schedule.

## Deliverable

Provide a compact shortlist with fixture, format, reported start time and time zone, and a reason for inclusion. Keep fixtures with unresolved timing in a separate brief note. Explain the scope and cache limitation once.

If no fixtures satisfy the constraints, show the nearest supported alternatives and which constraint each misses. Leave reminders, calendar events, subscriptions, and streaming arrangements uncreated; this workflow produces a plan in chat.
