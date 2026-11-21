---
name: performance-report
description: Use when the user asks for a marketing performance report, recap, overview, health check or client-ready summary across their connected platforms, for example "summarize last month", "build a client report for Acme", "how did all my channels do this quarter" or "give me a weekly marketing update".
---

# Cross-channel performance report

Build a clear, accurate report from the user's Power My Analytics data. Follow the data and accuracy rules in the `analyze-marketing-data` skill throughout.

## 1. Scope the report

- **Period.** Use the period the user names. If none is given, default to the last full calendar month and say so at the top of the report. Compare against the previous period of the same length; use year over year when the user asks or when the business is clearly seasonal.
- **Client or account.** For an agency report about one client, resolve the client with `pma_list_data_sources` and `name_filter`, then scope every query to that client's accounts or sub-accounts.
- **Platforms.** Include every connected platform with data for the period unless the user narrows it.

## 2. Gather the numbers

1. `pma_list_data_sources` to get connector types, accounts and `data_through` dates. If the period ends after `data_through`, note that the latest days are not loaded yet.
2. `pma_get_account_summary` across the in-scope platforms for spend, conversions, revenue and ROAS.
3. `pma_compare_sources` on the headline metric (usually spend, then conversions or revenue) to rank channels.
4. `pma_get_date_range_comparison` in `custom` mode for each key platform and metric, to get the change vs the comparison period. Run these calls in parallel.
5. `pma_query_custom` on each ad platform's insights report with `dimensions=["campaign_name"]`, ordered by spend, for the top campaigns. Add conversions and conversion value so efficiency can be computed.
6. For any metric that moved by more than about 15%, run `pma_analyze_drivers` to find which campaigns or segments caused it.
7. Optionally, `pma_detect_significant_anomalies` on spend and conversions to flag unusual days.

## 3. Structure the report

1. **Headline.** Two or three sentences: the main result, the biggest change, and the one thing to act on.
2. **Key metrics table.** Spend, conversions, revenue, ROAS or CPA for the period, the comparison period, and the change. Compute ROAS and CPA from totals.
3. **Channel breakdown.** One short paragraph or table row per platform: what it delivered and how it moved.
4. **What changed and why.** The main drivers, naming specific campaigns or segments.
5. **Watch list.** Anomalies, campaigns with rising cost and falling results, and connection or data gaps.
6. **Data notes.** Date range, platforms included, attribution caveat when ad-platform conversions are combined, and any days not yet loaded.

## 4. Style

- Write for a busy marketer or client: plain language, no internal connector codes, no tool names.
- Keep it to what fits on one or two screens unless the user asks for depth.
- Offer charts per channel when the user wants something to share.
- At the end, offer to save the report's sources as a Power My Analytics dataset so it can be refreshed in Google Sheets, Data Studio or Power BI.
