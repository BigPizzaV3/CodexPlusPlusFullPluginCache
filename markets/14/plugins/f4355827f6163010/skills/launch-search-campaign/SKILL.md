---
name: launch-search-campaign
description: Build a new Google Ads search campaign with Toffu. Use when the user asks to launch, create or set up a search campaign. Plans the campaign, ad group, keywords and ad with the user, then stages each part as a paused proposal the user confirms.
---

# Google Ads search campaign launch

Use the Toffu tools only. Never apply a change the user has not confirmed. Everything is created PAUSED.

## Steps

1. Call `get_account_context`. If several Google Ads accounts are connected, ask which one. Pass its id as `account_ids` `{"google_ads": "<id>"}` to `query_campaign_performance`, and as `account_id` to the other tools.
2. Ask for what you do not have: the product or service, the landing page URL, the daily budget, the goal (sales or leads) and the target CPA or ROAS, if any.
3. Write a plan and get the user's approval before you stage anything:
   - Campaign: name, daily budget, bidding (MAXIMIZE_CONVERSIONS for leads, MAXIMIZE_CONVERSION_VALUE for sales).
   - One ad group per theme, at most 3.
   - 5 to 20 keywords per ad group, in PHRASE or EXACT match. Use BROAD only if the user asks.
   - One responsive search ad per ad group: 8 to 15 headlines of 30 characters or fewer, 2 to 4 descriptions of 90 characters or fewer.
4. Call `propose_create_campaign` with fields `name`, `daily_budget_micros` (budget x 1,000,000), `campaign_type` "SEARCH", `bidding_strategy`, `status` "PAUSED". Show the preview, and call `apply_change` after the user confirms. Keep the campaign id from the result.
5. For each ad group, call `propose_create_ad_set` with `campaign_id` and fields `name`, `status` "ENABLED". Apply after the user confirms. Call `list_ad_sets` to get its `adGroup.resourceName`.
6. For each ad group, call `propose_create_keyword` with fields `ad_group_resource_name`, `ad_group_name` and `keywords` `[{"text": "...", "match_type": "PHRASE"}]`. Apply after the user confirms.
7. For each ad group, call `propose_create_ad` with fields `ad_group_resource_name`, `ad_group_name`, `headlines`, `descriptions`, `final_urls`. Apply after the user confirms.
8. Summarize what exists now. The campaign stays PAUSED. To start it, the user confirms `propose_update_campaign` `{"status": "ENABLED"}`.

## Rules

- The ad groups, keywords and ads only serve when the campaign is enabled. Say so.
- Never enable the campaign in the same step as you create it.
- Use the account currency for the budget.
