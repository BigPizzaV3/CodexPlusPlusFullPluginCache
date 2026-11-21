# ChatGPT Ads: every operation

Generated from the tools' own descriptions. "Tool" is the platform tool that runs the operation on grouped connections (operation=<name>, params=<arguments>); on connections that list every operation as its own tool, call the operation name directly.

## Read (changes nothing)

| Operation | Tool | Use it when |
|---|---|---|
| `chatgpt_ads_ad_preview` | chatgpt_ads_read | Wants to see how a ChatGPT Ads ad looks and what blocks its delivery. |
| `chatgpt_ads_conversion_setup` | chatgpt_ads_read | Wants to check ChatGPT Ads conversion tracking: pixels and event settings. |
| `chatgpt_ads_details` | chatgpt_ads_read | Wants the full details of one ChatGPT Ads campaign, ad group or ad. |
| `chatgpt_ads_geo_lookup` | chatgpt_ads_read | Needs ChatGPT Ads location IDs. |
| `chatgpt_ads_insights` | chatgpt_ads_read | Wants ChatGPT Ads delivery and performance with time buckets or breakdowns. |
| `chatgpt_ads_spend_limits` | chatgpt_ads_read | Wants the ChatGPT Ads account spending limits. |
| `diagnose_chatgpt_ads_delivery` | chatgpt_ads_read | Asks why their ChatGPT Ads get no impressions. |

## Add (preview, then confirm)

| Operation | Tool | Use it when |
|---|---|---|
| `create_chatgpt_ads_ad` | chatgpt_ads_create | Wants a new ChatGPT Ads ad (chat card) in an ad group. |
| `create_chatgpt_ads_ad_group` | chatgpt_ads_create | Wants a new ChatGPT Ads ad group with its maximum bid and context hints. |
| `create_chatgpt_ads_campaign` | chatgpt_ads_create | Wants a new ChatGPT Ads campaign; it is created paused unless the user asks to launch it. |
| `create_chatgpt_ads_event_setting` | chatgpt_ads_create | Wants a ChatGPT Ads conversion event setting. |

## Change, pause or delete (preview, then confirm)

| Operation | Tool | Use it when |
|---|---|---|
| `chatgpt_ads_status` | chatgpt_ads_edit | Wants to change the status of a ChatGPT Ads campaign, ad group or ad, for example to pause or activate it. |
| `connect_chatgpt_ads` | chatgpt_ads_edit | Wants to connect a ChatGPT Ads account with its Ads API key. The preview only checks which ad account the key belongs to; saving replaces a key already stored for that account. |
| `manage_chatgpt_ads_accounts` | chatgpt_ads_edit | Wants to list, re-check, disconnect or change the default connected ChatGPT Ads account. |
| `manage_chatgpt_ads_spend_limit` | chatgpt_ads_edit | Wants to create, change or remove a ChatGPT Ads account spending limit. |
| `update_chatgpt_ads_ad` | chatgpt_ads_edit | Wants to change a ChatGPT Ads ad's copy, destination or image. |
| `update_chatgpt_ads_ad_group` | chatgpt_ads_edit | Wants to change a ChatGPT Ads ad group's name, bid, bid strategy or context hints. |
| `update_chatgpt_ads_campaign` | chatgpt_ads_edit | Wants to change a ChatGPT Ads campaign's name, budget, locations, platforms, schedule or conversion settings. Budget increases are capped at +50% per change and +100% within 24 hours. |
