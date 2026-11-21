---
name: wasted-spend
description: Find Meta Ads spend that brings no return. Use when the user asks where they waste money on Facebook or Instagram, what to pause or cut, or which campaigns, ad sets or ads do not convert. Finds spend with no or weak conversions at every level and proposes pauses or budget cuts the user confirms.
---

# Meta Ads wasted spend

Use the Toffu tools only. Never apply a change the user has not confirmed.

## Steps

1. Call `get_account_context`. If several Meta ad accounts are connected, ask which one. Pass its id as `account_ids` `{"meta_ads": "<id>"}` to `query_campaign_performance`, and as `account_id` to the other tools.
2. Call `query_campaign_performance` for the last 30 full days (end date = yesterday). Compute the account CPA (spend / conversions) and ROAS (conversion_value / spend). If purchases are 0 but `conversions_by_action` shows leads or another event, use that event in `conversion_events` and say so.
3. Call `query_campaign_performance` again with `level` "adset", then with `level` "ad", for the same dates.
4. Mark a row as waste when it is active and one of these is true:
   - It has 0 conversions, and spent more than 2x the account CPA. If the account has no conversions, use more than 10% of account spend.
   - Its ROAS is below 60% of the account ROAS, and it has at least 10% of account spend. If conversion value is missing, use CPA: its CPA is more than 1.7x the account CPA.
5. Work from the top down: if a whole campaign is waste, report the campaign, not each of its ads.
6. Call `list_campaigns` and `list_ad_sets` for the status and daily budget of each waste item. Budgets there are in minor units: divide `daily_budget` by 100.
7. Report:
   - Total wasted spend and its share of account spend.
   - One table: level, name, spend, conversions, ROAS, the reason.
   - The amount the user saves per month for each one (average daily spend x 30).
8. For each waste item, propose one action:
   - **Pause** with `propose_update_campaign`, `propose_update_ad_set` or `propose_update_ad` `{"status": "PAUSED"}` when it has 0 conversions.
   - **Cut the budget** with `propose_update_campaign` or `propose_update_ad_set` `{"daily_budget_amount": <new amount>}` when it converts at a low ROAS. Cut by 20% to 50%.
   Show each preview. Call `apply_change` only after the user confirms that change.

## Rules

- Never pause the account's only converting campaign.
- Retargeting ad sets often have a high CPA on few conversions. Tell the user before you propose to pause one.
- An ad set or ad in Meta's learning phase (launched in the last 7 days) is not waste yet. Say so instead of pausing it.
