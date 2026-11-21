---
name: wasted-spend
description: Find Google Ads spend that brings no return. Use when the user asks where they waste money, what to pause or cut, or which campaigns do not convert. Finds campaigns and ad groups with spend and no or weak conversions, and proposes pauses or budget cuts the user confirms.
---

# Google Ads wasted spend

Use the Toffu tools only. Never apply a change the user has not confirmed.

## Steps

1. Call `get_account_context`. If several Google Ads accounts are connected, ask which one. Pass its id as `account_ids` `{"google_ads": "<id>"}` to `query_campaign_performance`, and as `account_id` to the other tools.
2. Call `query_campaign_performance` for the last 30 full days (end date = yesterday). Compute the account CPA (spend / conversions) and ROAS (conversion_value / spend).
3. Call `list_campaigns` for each campaign's status and daily budget (`campaignBudget.amountMicros` / 1,000,000).
4. Mark a campaign as waste when it is ENABLED and one of these is true:
   - It has 0 conversions, and spent more than 2x the account CPA. If the account has no conversions, use more than 10% of account spend.
   - Its ROAS is below 60% of the account ROAS, and it has at least 10% of account spend. If conversion value is missing, use CPA instead: its CPA is more than 1.7x the account CPA.
5. Call `list_ad_sets` once. It lists the ad groups of the whole account; keep the rows whose `campaign.id` is a waste campaign, so the user sees what a pause stops.
6. Report:
   - Total wasted spend and its share of account spend.
   - One table: campaign, spend, conversions, ROAS, the reason.
   - The amount the user saves per month if they pause each one (average daily spend x 30).
7. For each waste campaign, propose one action:
   - **Pause** with `propose_update_campaign` `{"status": "PAUSED"}` when it has 0 conversions.
   - **Cut the budget by half** with `propose_update_campaign` `{"daily_budget": <new amount>}` when it converts but at a low ROAS.
   Show each preview. Call `apply_change` only after the user confirms that change.

## Rules

- Never pause the account's only converting campaign.
- Brand search campaigns often have low volume but protect the brand name. Tell the user before you propose to pause one.
- Say "no data" when conversion value is missing, and use the CPA rule in step 4.
