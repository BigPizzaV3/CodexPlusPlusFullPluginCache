---
name: ad-copy-refresh
description: Write new Google Ads responsive search ads with Toffu. Use when the user asks for new ad copy, an ad refresh, a test of new headlines, or to replace a tired ad. Reads the current ads, writes a new ad for the ad group, and proposes to pause the old one after the user confirms.
---

# Google Ads ad copy refresh

Use the Toffu tools only. Never apply a change the user has not confirmed.

## Steps

1. Call `get_account_context`. If several Google Ads accounts are connected, ask which one. Pass its id as `account_ids` `{"google_ads": "<id>"}` to `query_campaign_performance`, and as `account_id` to the other tools.
2. Ask which campaign or ad group, unless the user said it. Call `list_ad_sets` (it lists the whole account; keep the rows of that campaign) for the ad group's `adGroup.resourceName` and `adGroup.name`.
3. Call `list_ads` and keep the ads of that ad group. Read their headlines, descriptions and final URL.
4. Call `query_campaign_performance` for the last 30 full days for the campaign's results, so the copy fits what works.
5. Write one new responsive search ad:
   - 8 to 15 headlines, each 30 characters or fewer. Include the brand, the main product words, a benefit, an offer or proof, and a call to action.
   - 2 to 4 descriptions, each 90 characters or fewer.
   - The same final URL as the current ad, unless the user gives a new one.
   - No claim the user has not given (prices, discounts, awards).
6. Show the copy with the character count of each line. Change it until the user approves it.
7. Call `propose_create_ad` with fields `ad_group_resource_name`, `ad_group_name`, `headlines`, `descriptions`, `final_urls`. Show the preview. Call `apply_change` only after the user confirms.
8. Offer to pause the old ad with `propose_update_ad` `{"status": "PAUSED"}` (entity id `<ad_group_id>~<ad_id>`). Recommend to keep both running for 2 to 4 weeks first, to compare them.

## Rules

- Ad text cannot be edited in Google Ads. A change is always a new ad.
- Count characters exactly. Google refuses a headline over 30 or a description over 90 characters.
