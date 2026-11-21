# TikTok Ads: every operation

Generated from the tools' own descriptions. "Tool" is the platform tool that runs the operation on grouped connections (operation=<name>, params=<arguments>); on connections that list every operation as its own tool, call the operation name directly.

## Read (changes nothing)

| Operation | Tool | Use it when |
|---|---|---|
| `download_tiktok_leads` | tiktok_ads_read | Wants the leads collected by TikTok instant forms or direct messages. |
| `get_tiktok_lead_form_fields` | tiktok_ads_read | Needs the questions and field keys of a TikTok lead form to read its leads. |
| `list_tiktok_ad_accounts` | tiktok_ads_read | Wants their connected TikTok ad accounts. |
| `list_tiktok_adgroups` | tiktok_ads_read | Wants the TikTok ad groups of an account or campaign. |
| `list_tiktok_ads` | tiktok_ads_read | Wants the TikTok ads with their creative IDs and status. Rejected or in-audit ads include the review reason. |
| `tiktok_ad_review` | tiktok_ads_read | Wants TikTok's policy reason text for specific ad ids. |
| `list_tiktok_asset_groups` | tiktok_ads_read | Wants the asset groups of a TikTok Business Center. |
| `list_tiktok_audiences` | tiktok_ads_read | Wants the TikTok custom and lookalike audiences. |
| `list_tiktok_auto_messages` | tiktok_ads_read | Needs TikTok welcome-chat templates and their auto_message_id for messaging ads. |
| `list_tiktok_bc_advertisers` | tiktok_ads_read | Wants every ad account under a TikTok Business Center. |
| `list_tiktok_bc_pixels` | tiktok_ads_read | Wants the pixels across a TikTok Business Center. |
| `list_tiktok_business_centers` | tiktok_ads_read | Wants the TikTok Business Centers they can access. |
| `list_tiktok_campaigns` | tiktok_ads_read | Wants the campaigns in a TikTok ad account. |
| `list_tiktok_creative_portfolios` | tiktok_ads_read | Wants the creative portfolios of a TikTok ad account. |
| `list_tiktok_gmv_max_stores` | tiktok_ads_read | Wants the TikTok Shop stores linked to an ad account for GMV Max. |
| `list_tiktok_identities` | tiktok_ads_read | Needs the TikTok identities (identity_id) that ads can run under. |
| `list_tiktok_lead_forms` | tiktok_ads_read | Wants the TikTok lead-generation instant forms and their page_id. |
| `list_tiktok_pixels` | tiktok_ads_read | Wants the TikTok pixels of an ad account with their events and activity, for example to check TikTok conversion tracking. |
| `list_tiktok_posts` | tiktok_ads_read | Wants the organic TikTok posts of an identity that can become Spark Ads. |
| `list_tiktok_smart_plus` | tiktok_ads_read | Wants TikTok Smart+ campaigns, ad groups or ads, which the standard lists do not include. |
| `list_tiktok_videos` | tiktok_ads_read | Wants the videos in a TikTok ad account's video library with their video_id. |
| `tiktok_advertiser_qualification` | tiktok_ads_read | Asks about a TikTok advertiser's qualification or verification status in a Business Center. |
| `tiktok_campaign_report` | tiktok_ads_read | Wants TikTok Ads performance (spend, impressions, clicks, conversions) by campaign, ad group or ad. |
| `tiktok_change_history` | tiktok_ads_read | Asks who changed what in the TikTok ad accounts of a Business Center. |
| `tiktok_recommendations` | tiktok_ads_read | Wants TikTok's automatic optimization suggestions. |
| `tiktok_region_search` | tiktok_ads_read | Needs TikTok location IDs for targeting. |
| `tiktok_report_query` | tiktok_ads_read | Needs TikTok report metrics or dimensions that the standard TikTok report does not cover. |
| `tiktok_targeting_search` | tiktok_ads_read | Needs TikTok interest or behavior category IDs for targeting. |

## Add (preview, then confirm)

| Operation | Tool | Use it when |
|---|---|---|
| `connect_tiktok_ads` | tiktok_ads_create | Wants to connect a TikTok for Business ad account. |
| `create_tiktok_ad` | tiktok_ads_create | Wants a new ad in a TikTok ad group, from an uploaded video, images or an organic post (Spark Ads). |
| `create_tiktok_adgroup` | tiktok_ads_create | Wants a new TikTok ad group with targeting, budget and optimization; it is created disabled (paused). |
| `create_tiktok_auto_message` | tiktok_ads_create | Wants a TikTok welcome-chat (automated message) template for messaging ads. |
| `create_tiktok_campaign` | tiktok_ads_create | Wants a new TikTok campaign with its objective and budget; nothing spends until an ad group and an ad are enabled. |
| `create_tiktok_customer_file_audience` | tiktok_ads_create | Wants a TikTok custom audience from a customer list. |
| `create_tiktok_lookalike_audience` | tiktok_ads_create | Wants a TikTok lookalike audience from a source custom audience. |
| `create_tiktok_pixel` | tiktok_ads_create | Wants a new TikTok pixel for conversion tracking. |
| `upload_tiktok_image` | tiktok_ads_create | Wants to upload an image from a public URL to TikTok for ads. |
| `upload_tiktok_video` | tiktok_ads_create | Wants to upload a video from a public URL to TikTok for ads. |

## Change, pause or delete (preview, then confirm)

| Operation | Tool | Use it when |
|---|---|---|
| `manage_tiktok_search_negative_keywords` | tiktok_ads_edit | Wants to list, add or remove negative keywords on TikTok search ads. |
| `send_tiktok_conversion_event` | tiktok_ads_edit | Wants to send a server-side conversion event to TikTok through the Events API. |
| `share_tiktok_audience` | tiktok_ads_edit | Wants to share or unshare TikTok audiences with other ad accounts in the same Business Center. |
| `update_tiktok_ad` | tiktok_ads_edit | Wants to edit a TikTok ad's text, landing page, call to action or display name in place. |
| `update_tiktok_ad_status` | tiktok_ads_edit | Wants to enable, pause or delete TikTok ads. |
| `update_tiktok_adgroup` | tiktok_ads_edit | Wants to change a TikTok ad group's targeting, bid or schedule. |
| `update_tiktok_adgroup_budget` | tiktok_ads_edit | Wants to change a TikTok ad group budget. Budget increases are capped at +50% per change and +100% within 24 hours. |
| `update_tiktok_adgroup_status` | tiktok_ads_edit | Wants to enable, pause or delete TikTok ad groups. |
| `update_tiktok_campaign` | tiktok_ads_edit | Wants to rename a TikTok campaign. |
| `update_tiktok_campaign_budget` | tiktok_ads_edit | Wants to change a TikTok campaign budget. Budget increases are capped at +50% per change and +100% within 24 hours. |
| `update_tiktok_campaign_status` | tiktok_ads_edit | Wants to enable, pause or delete TikTok campaigns. |
