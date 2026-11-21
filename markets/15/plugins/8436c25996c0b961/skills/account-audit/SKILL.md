---
name: account-audit
description: Audit a Meta Ads account with Toffu. Use when the user asks to audit, review or health-check their Facebook or Instagram ads, or asks what to fix or improve. Ranks campaigns, ad sets and creatives by spend and ROAS, flags waste, fatigue and budget limits, and proposes fixes the user confirms.
---

# Meta Ads account audit

Use the Toffu tools only. Never apply a change the user has not confirmed.

## Steps

1. Call `get_account_context`. If several Meta ad accounts are connected, ask which one. Pass its id as `account_ids` `{"meta_ads": "<id>"}` to `query_campaign_performance`, and as `account_id` to the other tools. Follow any conversion events or targets in `custom_instructions`.
2. Ask for the target CPA or ROAS, unless the user gave one. Without a target, use the account average.
3. Call `query_campaign_performance` for the last 30 full days (end date = yesterday). Read `conversions_by_action` in the rows. If the account has no purchases but has leads or another event, call it again with that event in `conversion_events` (for example `["lead"]`) and say which event you used.
4. Call `query_campaign_performance` for the 30 days before, for the trend.
5. Call `list_campaigns` and `list_ad_sets` for status, objective and daily budget. Meta budgets in these lists are in minor units: divide `daily_budget` by 100. A campaign without a daily budget has its budget on its ad sets.
6. Call `creative_report` for the last 30 full days, for the creatives and their frequency.
7. For each campaign with spend in either period, compute ROAS = conversion_value / spend, CPA = spend / conversions, share of account spend, average daily spend = spend / 30, and the change against the previous 30 days.
8. Flag these findings, worst first:
   - **Off target:** CPA above the target CPA, or ROAS below the target ROAS.
   - **No conversions:** 0 conversions, and spend above 2x the account CPA.
   - **Budget-limited winner:** ROAS above the account ROAS, and average daily spend is 90% or more of the daily budget.
   - **Sharp drop:** conversions down 30% or more, with spend flat or up.
   - **Tired creative:** an active ad with frequency 3 or more and ROAS below the account ROAS.
   - **Paused winner:** a paused campaign that had ROAS above the account ROAS in the previous period.
9. Report:
   - Account totals: spend, purchases (or the event used), conversion value, ROAS, CPA, against the previous period.
   - One table: campaign, status, spend, conversions, ROAS, CPA, finding.
   - The 3 best and 3 worst creatives by ROAS, with title and thumbnail link.
   - At most 3 recommended actions, each with the numbers that support it.
10. Offer each action as a change: `propose_update_campaign` or `propose_update_ad_set` (`status`, `daily_budget_amount` in the account currency) or `propose_update_ad` (`status`). Show the preview. Call `apply_change` only after the user confirms that change.

## Rules

- Use the account currency. Never add totals in different currencies.
- Say "no data" when a metric is missing. Never estimate it.
- Do not recommend a change from fewer than 7 days of data or fewer than 10 conversions without saying that the sample is small.
