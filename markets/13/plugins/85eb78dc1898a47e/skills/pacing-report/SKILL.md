---
name: pacing-report
description: Report month-to-date budget pacing across all connected ad platforms with Toffu. Use when the user asks how they are pacing, whether they are on budget, or what they will spend by month end. Projects month-end spend per account against the monthly budgets and lists the moves to make this week.
---

Use the Toffu tools. Never apply a change the user has not confirmed.

1. Call `get_account_context`. If a platform has several accounts, ask which one. Pass the ids as `account_ids` to `query_campaign_performance`, and as `account_id` to the other tools.
2. Read data with `query_campaign_performance` (daily rows: `time_increment` "1"), `list_campaigns`, `list_ad_sets` and `list_ads`.
3. To change something, call `propose_update_campaign`, `propose_update_ad_set` or `propose_update_ad`, and show the preview. Call `apply_change` only after the user confirms that change.

There is no budgets sheet here: ask the user for the monthly budget per account or platform, once.

# Mid-Month Pacing Report

Use when the user asks "how are we pacing", "are we on budget", "month-to-date pacing", "will we hit budget", or wants a report to send a client mid-month. Agency clients ask this every two weeks. Automating it is a recurring time saver.

## Inputs

- The monthly budget per account or per channel (the user supplies; if missing, ask once or pull from a stored budgets sheet).
- Today's date and the month-to-date (MTD) actual spend per account or channel.
- The number of days elapsed and the number of days remaining in the month.

## The math (no surprises)

- `expected_pace = (days_elapsed / days_in_month) * monthly_budget`
- `pacing_delta_pct = (mtd_spend - expected_pace) / expected_pace`
- `projected_eom = mtd_spend * (days_in_month / days_elapsed)`
- `projected_vs_budget_pct = (projected_eom - monthly_budget) / monthly_budget`

## Classification

- **On track**: |pacing_delta_pct| <= 5%. No action.
- **Underpacing**: pacing_delta_pct < -10%. Budget will be left on the table. Recommend: raise budgets, expand audiences, or unpause held inventory.
- **Overpacing**: pacing_delta_pct > 10%. Will overspend without intervention. Recommend: reduce daily caps, pause lowest-ROAS campaigns, or move budget to under-pacing accounts.
- **Severe**: |pacing_delta_pct| > 25%. Lead with this.

Round all percentages to whole numbers in the output. The CMO does not need 3 decimal places.

## Output format

One executive line: "X of N accounts pacing on target. $A overspend / $B underspend projected at month-end."

Then a table — Account/Channel | Monthly budget | MTD spend | Days elapsed/total | Expected pace | Pacing delta | Projected EOM | Action. Sort by absolute pacing delta descending.

End with a 3-line "what to do this week" section listing concrete moves (raise X budget by $Y, pause campaign Z).

## Pitfalls

- Calendar months have different lengths. Always use the actual `days_in_month` for the month being reported, not 30.
- A campaign launched on the 10th has different "expected pace" than one running since the 1st. If launch dates differ from month-start, use `days_since_campaign_start` instead of `days_elapsed`. Note this on the row.
- Weekend tapering: most accounts spend less on Sat-Sun. A simple linear pace will read "underpacing" Friday morning and "overpacing" Monday morning. State the projection as "linear" so the reader knows it's not seasonality-aware.
- If the budget is "as much as profitable" rather than a fixed cap, pacing is the wrong report — use ROAS-vs-target instead.
- Currency: convert MTD spend to the budget's currency, not the other way around. Otherwise the budget moves between reports.
