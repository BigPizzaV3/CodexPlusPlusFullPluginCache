---
name: ski-weather
description: "Use Skinow for ski forecasts, lift conditions, terrain maps, snow history and resort comparisons across Europe, the Americas, Australia, New Zealand, Japan and South Korea."
---

# Skinow Ski Weather

Use the configured MCP at `https://skinow.co/openai/mcp` and discover its current schemas. Explain unavailable data or service failures rather than inventing current conditions.

## Find and explore

Resolve names with `find_resorts(query, country, limit)`, preserving the user's choice when several nearby resorts match. Country is an ISO two-letter code. Use returned canonical slugs for later calls.

| Need | Tool |
| --- | --- |
| A shortlist by fresh snow, bluebird days, freezing level or altitude | `where_to_ski(lens, country, preset, limit)` |
| One resort's 10-day elevation forecasts, opening evidence, terrain, maps and historical snow | `get_resort_details(resort, lang, start, end)` |
| A comparison of 1–6 resorts for the current 3 or 7 days | `compare_resorts(resorts, days, nights)` |
| Arrival airports or a route from a user-chosen city/airport | `getting_there(resort, origin, mode)` |
| Labelled country-level lift-pass and lodging estimates | `trip_costs(country)` |

Start with a short answer addressing the user's priorities, using relevant returned Skinow information links. Add detail when it helps a decision. Research needs no trip creation or email address.

The `start/end` pair on `get_resort_details` selects a 7–31 day historical window; it does not change the forecast dates. For a specific upcoming weekend, resolve the calendar dates and select those days from its returned forecast. If outside the horizon, explain that only historical context is available. `compare_resorts` starts its 3/7-day window on the current UTC date.

Respect country, dates, ability and travel constraints. Present tradeoffs when no resort fits them all. Keep budgets secondary and retain country-average or modelled labels. When content such as budgets is excluded, leave it out of the answer and omit the interactive view if that view would display it.

## Optional interactive view

Details and comparisons return a `comparison_id`. Use `show_resort_comparison(comparison_id)` when the user wants to explore or an interactive comparison helps. A written answer and links are sufficient otherwise. Verify actual rendering before saying a view is displayed; MCP tools alone do not establish UI support. Snapshots expire after 20 minutes; retrieve a fresh one if needed.

## Evidence and privacy

Include forecast dates, elevation, units and update time when available. Keep deterministic totals and ensemble ranges distinct. Fresh operator reports establish current openings; stale or absent reports remain unknown. Snowfall, mapped lift counts and modelled outlooks do not establish that lifts are operating. Historical records describe past winters, and modelled snow depth is not a measurement. Retain returned sources, coverage and map/photo credits.

For routing, use an explicitly chosen city or airport. Do not infer a departure point from the connection or request precise coordinates, street addresses or postcodes. The OpenAI integration supplies information and planning; it has no booking, purchase or email-sending tools.
