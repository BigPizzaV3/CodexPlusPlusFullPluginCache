---
name: pipeline-review
description: Review the Minz.ai sales pipeline, including totals by stage, deals expected to close soon, and deals that look stalled or at risk, for a weekly sales meeting or a manager check-in. Use when the user asks about their pipeline, forecast, deals closing this month or quarter, or which deals need attention.
---

# Pipeline review

Give the user an honest picture of the pipeline and a short list of deals to act on.

## Data and its limits

- `crm_pipeline_summary` returns the complete aggregate for the workspace: deal count and value by stage, and the total. Closed Lost is excluded. This is the only complete view, so take totals from here, never from adding up search results.
- `crm_deals_search` returns at most 20 deals per call and reports the full count as `total`. Narrow it with `stage` (exact value), `pipelineName` (partial name) or `personName` (partial match on owner, assigned member, creator or contact) to cover the deals that matter. When `total` is larger than the rows returned, say how many you did not see.
- `crm_pipeline_health` reports stale, stuck and soon-to-close open deals. Counts cover every visible open deal; each list is capped at the 10 most urgent and `partial` is true when a list was truncated. Use it to pick deals for the "needs attention" list, and say when a list was cut.
- `crm_deals_history`, used for a few deals, shows recent movement. It is bounded and may be partial.
- `general_activities_search` with a `dealId` shows when a deal was last touched.

## What to report

1. **Totals by stage** from the summary, with currency as returned. Do not convert currencies.
2. **Closing soon:** deals whose close date falls in the period the user asked about (this month if they did not say), with stage, value and owner.
3. **Needs attention:** deals with a close date in the past but still open, deals in late stages with no recent activity, and large deals with no close date. Explain the reason for each one in a few words.
4. **Suggested next steps,** clearly marked as suggestions.

If the user is a manager asking about a person's deals, filter by `personName`. Reply in the user's language.
