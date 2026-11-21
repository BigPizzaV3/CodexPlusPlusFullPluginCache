---
name: ga4-analysis
description: Use this plugin for read-only Google Analytics 4 discovery, historical and realtime reporting, funnels, aggregate conversion acquisition views, and scope comparisons. Do not use it for configuration changes, advertising changes, email, calendar, or unrelated tasks.
---

# GA4 analysis workflow

Use only the GA4 MCP server bundled with this plugin for GA4 work. Do not substitute another HYPD server.

## Routing boundary

- Invoke this plugin only for read-only GA4 discovery, reporting, investigation, troubleshooting, or planning.
- For a request whose requested outcome is only a GA4 configuration change, Google Ads write, permission change, email, calendar action, or other unsupported action, do not call any plugin tool, including `init` or discovery tools. State the relevant limitation directly.
- Suggestions and plans are allowed, but never imply that a write occurred.

## Property and date handling

1. Call `init` for supported analytics work.
2. Discover accessible accounts and properties. Reuse only an exact returned `property_id`.
3. If exactly one property is available, continue with it. If multiple properties are available and the user has not identified one, ask the user to choose before running property-specific reports.
4. Read property details when its time zone, currency, industry category, or linked Google Ads context affects interpretation.
5. Resolve relative periods such as “last 30 complete days” in the selected property's time zone. State the explicit inclusive start and end dates used.

## Reporting accuracy

- Check metadata and compatibility before flexible historical reports when the requested dimension/metric combination has not already been validated.
- Keep historical and realtime fields separate. Do not send historical date ranges or unsupported historical metrics to the realtime report.
- For every tabular result, state the number of rows returned, the total row count if supplied, the requested limit or page size, and whether the result is complete, paginated, truncated, or of unknown completeness.
- When pagination is supported and the user asks for all results, fetch subsequent pages until complete. Otherwise rank and summarize only the rows actually returned and say so.
- Compare totals only when property, inclusive dates, filters, attribution scope, and metric definitions align. Show the arithmetic. If figures differ, report each value and the exact difference; do not invent a cause.
- Treat missing fields and empty results as unavailable or empty, not zero, unless the API explicitly returns zero.
- Do not claim ad spend, ROAS, transaction counts, assisted conversions, or joined Google Ads records unless the selected tool actually returns the required fields.

## Purpose-specific tools

- Despite its legacy name, `ga4_get_conversion_paths` returns aggregate conversions, total revenue, and sessions grouped by session default channel group and campaign. Do not describe it as ordered multi-step paths or assisted-conversion credit.
- Despite its legacy name, `ga4_compare_attribution` jointly groups results by first-user and session default channel groups. Describe it as a comparison of acquisition scopes, not a last-click versus data-driven attribution-model comparison.
- Keep these two aggregate views distinct and clearly state their actual grouping dimensions.

## Response quality

Report the exact property, date window, important filters, returned data scope, limitations, and any unresolved discrepancy. Never fabricate identifiers, rows, totals, explanations, or successful changes.
