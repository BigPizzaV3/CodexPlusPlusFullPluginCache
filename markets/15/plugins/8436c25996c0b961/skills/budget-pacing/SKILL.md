---
name: budget-pacing
description: Check Meta Ads budget pacing for the month with Toffu. Use when the user asks if they are on track, over or under budget, or how much they will spend on Facebook and Instagram this month. Projects month-end spend per campaign against the daily budgets or a monthly target, and proposes budget changes the user confirms.
---

# Meta Ads budget pacing

Use the Toffu tools only. Never apply a change the user has not confirmed.

## Steps

1. Call `get_account_context`. If several Meta ad accounts are connected, ask which one. Pass its id as `account_ids` `{"meta_ads": "<id>"}` to `query_campaign_performance`, and as `account_id` to the other tools.
2. Ask for the monthly budget target, unless the user gave one. If there is no target, use the sum of the daily budgets x the days in the month.
3. Call `query_campaign_performance` with `time_increment` "1" (daily rows), from the earlier of the first day of this month and 7 days ago, to yesterday.
4. Call `list_campaigns` for each campaign's status and daily budget. For campaigns without a daily budget, call `list_ad_sets`: their budget is on the ad sets. Budgets in these lists are in minor units: divide `daily_budget` by 100.
5. For each campaign, compute:
   - Spend so far this month, from the rows dated in this month. Include paused campaigns: their spend counts.
   - Average daily spend over the last 7 days. Use 0 for a campaign that is paused now.
   - Projected month-end spend = spend so far + (average daily spend x days left, today included).
6. Report:
   - Account spend so far, projected month-end spend and the target, with the difference in amount and percent.
   - One table: campaign, daily budget, average daily spend, spend so far, projected spend.
   - The status: on track (projection 95% to 105% of the target), over or under.
   - Daily budget use for each active campaign: 7-day average daily spend / daily budget. Flag 95% or more (limited by budget) and below 70% (budget not used: often a narrow audience or a low bid cap).
7. If the projection is below 95% or above 105% of the target, propose new daily budgets with `propose_update_campaign` (or `propose_update_ad_set` where the budget is on the ad set) `{"daily_budget_amount": <amount in the account currency>}`. Move budget to the campaigns with the highest ROAS first. Show each preview. Call `apply_change` only after the user confirms that change.

## Rules

- Use the account currency. `daily_budget_amount` is in whole currency units, not minor units.
- Change a budget by 20% or less at a time. A larger change can restart Meta's learning phase.
- Meta can spend up to 75% more than the daily budget on one day. Use the 7-day average, not one day.
- In the first days of a month, say that the projection rests on the last 7 days.
