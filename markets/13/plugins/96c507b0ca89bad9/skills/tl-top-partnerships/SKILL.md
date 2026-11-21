---
name: tl-top-partnerships
description: Analyze a brand user's published sponsorship performance using available ThoughtLeaders records, such as actual views and eCPM when required fields are exposed. Use for best-performing partnerships, realized CPM, ROI, or over/under-delivery questions.
---

# Sponsorship performance analysis (MCP)

Use only data visible to the authenticated caller. This plugin can return an analysis in chat; it does not create the CLI skill's Google Sheet.

## Workflow

1. Call tl_whoami, then tl_skill_track with skill="tl-top-partnerships" and stage="started"; retain its run_id. If the caller has no accessible brand-side profile, explain the limitation. If multiple brands are available and the user did not identify one, ask which brand.
2. Clarify the reporting period when ambiguous. Use calendar YTD only when the user asks for the current-year view; state exact dates.
3. Read tl_schema_pg, tl_schema_fb, and tl_describe to confirm which sponsorship dates, live views, and sold-date projections are exposed to this role. Use only documented fields. Check tl_balance and run pricing=true before large queries.
4. Compute live eCPM as price / live_views × 1000 only when both values are present and positive. Compute sold-date eCPM only if the projection captured at sale is actually available; do not substitute current projected views. For channel rollups, divide total price by total live views rather than averaging per-deal CPMs.
5. Exclude or separately label unpublished deals and rows without enough data. State counts, period, ranking basis, and missing-data count. Do not claim completeness if query limits apply.

Do not expose contact details, private notes, or fields beyond caller access. Do not invent future bookings or projections. No spreadsheet is created; return a concise table or summary in chat.

Before the final response, call tl_skill_track with skill="tl-top-partnerships", stage="completed", the retained run_id, and outcome="completed", "no_results", "failed", or "cancelled". Never include user content, queries, or results in that tracking call.

