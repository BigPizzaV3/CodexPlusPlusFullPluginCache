---
name: pipeline-review
description: Review the IRM365 sales pipeline. Use when the user asks about their pipeline, forecast, deals or opportunities closing soon, stalled deals, or expected revenue.
---

# Pipeline review

## Decide the scope first

- **Open deals only.** The open stages are `discovery`, `viewing`, `proposal`, `negotiation` and `commitment`. Won, lost and cancelled deals are closed. Never count them in pipeline totals.
- **Period.** If the user named one ("this month", "this quarter"), work out its last day in the user's timezone (from `get_workspace_context`) and pass it as `closing_before`. If they named none, review all open deals and say so.

## Fetch

1. Call `search_opportunities` once for each open stage, using `status`, plus `closing_before` when there is a period.
2. Page through each call while `has_more` is true, up to 200 opportunities in total.
3. If you stop with `has_more` still true, the totals are **partial**. Say so plainly at the top of the answer, with how many deals were read. Never present partial totals as the pipeline.
4. For a deal that looks stalled, call `get_opportunity` for its detail. Stalled means its close date has passed, or it has no next follow-up.

## Report

- **Totals by stage:** for each open stage, the count and expected value in AED, plus a probability-weighted total (expected value × win probability).
- **Closing soon:** deals due in the next 30 days, or within the period, soonest first, with owner and probability.
- **At risk:** deals past their close date and deals without a next follow-up, each with one suggested next step.

Show amounts as AED with thousands separators. Say that the figures cover only the opportunities this person can see in IRM365, which may not be the whole company. Don't round probabilities into certainty, and don't forecast beyond what the data shows.
