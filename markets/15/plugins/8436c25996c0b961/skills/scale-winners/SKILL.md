---
name: scale-winners
description: Scale the best Meta Ads campaigns and ad sets with Toffu. Use when the user asks where to put more budget, what to scale, or how to grow results on Facebook and Instagram without losing efficiency. Finds the campaigns and ad sets with the best ROAS and room to spend, and proposes step-by-step budget increases the user confirms.
---

# Meta Ads scale winners

Use the Toffu tools only. Never apply a change the user has not confirmed.

## Steps

1. Call `get_account_context`. If several Meta ad accounts are connected, ask which one. Pass its id as `account_ids` `{"meta_ads": "<id>"}` to `query_campaign_performance`, and as `account_id` to the other tools.
2. Ask for the target CPA or ROAS and how much more the user wants to spend, unless the user said it.
3. Call `query_campaign_performance` for the last 14 full days with `level` "adset", and once with `time_increment` "7" for the last 28 full days, for the trend.
4. Call `list_campaigns` and `list_ad_sets` for status and daily budget (minor units: divide `daily_budget` by 100).
5. Call `creative_report` for the last 14 full days, for the frequency of each winner's ads.
6. Mark a campaign or ad set as a winner when all of these are true:
   - ROAS above the target ROAS (or CPA below the target CPA), or above the account ROAS without a target.
   - At least 10 conversions in the 14 days.
   - ROAS in the last 7 days not more than 20% below the 7 days before.
   - Its ads have frequency below 3.
7. Report the winners with spend, conversions, ROAS, CPA, budget use (average daily spend / daily budget) and frequency, and the ones you left out with the reason.
8. For each winner, propose a budget increase of 20% with `propose_update_campaign` (budget on the campaign) or `propose_update_ad_set` (budget on the ad set) `{"daily_budget_amount": <new amount>}`. If the user wants more, propose another step after 3 to 4 days, not now. Show each preview. Call `apply_change` only after the user confirms that change.

## Rules

- Use the account currency. `daily_budget_amount` is in whole currency units.
- Never raise a budget by more than 20% in one step. A larger change can restart Meta's learning phase.
- A winner with frequency 3 or more needs new creatives or a broader audience before more budget. Say so instead of raising its budget.
