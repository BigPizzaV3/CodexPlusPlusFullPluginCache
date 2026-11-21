# Meta Ads: every operation

Generated from the tools' own descriptions. "Tool" is the platform tool that runs the operation on grouped connections (operation=<name>, params=<arguments>); on connections that list every operation as its own tool, call the operation name directly.

## Read (changes nothing)

| Operation | Tool | Use it when |
|---|---|---|
| `download_meta_leads` | meta_ads_read | Wants the leads submitted through Meta instant forms, with their answers. |
| `find_instagram_media_id` | meta_ads_read | Gives an Instagram post or Reel link and its media id is needed to advertise it. |
| `get_meta_ad_creative` | meta_ads_read | Wants to read an existing Meta ad's creative: text, media, button, link, Page and Instagram identity. |
| `list_meta_ad_accounts` | meta_ads_read | Wants their connected Meta ad accounts. |
| `list_meta_ads` | meta_ads_read | Wants the ads in a Meta ad account or ad set with their status and delivery state. |
| `list_meta_adsets` | meta_ads_read | Wants the ad sets of a Meta ad account or campaign. |
| `list_meta_audiences` | meta_ads_read | Wants the Meta custom, lookalike and website audiences with their IDs. |
| `list_meta_campaigns` | meta_ads_read | Wants the campaigns in a Meta ad account. |
| `list_meta_catalogs` | meta_ads_read | Wants the product catalogs available to a Meta ad account. |
| `list_meta_custom_conversions` | meta_ads_read | Wants the Meta custom conversions defined on pixels. |
| `list_meta_instagram_accounts` | meta_ads_read | Needs the Instagram accounts that a Meta ad account can advertise with. |
| `list_meta_instagram_posts` | meta_ads_read | Wants the posts and Reels of an Instagram business account, for example to advertise one. |
| `list_meta_lead_forms` | meta_ads_read | Wants the instant forms of a Facebook Page with their questions. |
| `list_meta_page_posts` | meta_ads_read | Wants a Facebook Page's posts and their media, for example to reuse them as ads. |
| `list_meta_pages` | meta_ads_read | Needs the Facebook Pages they manage, for example to choose the page_id of a new ad. |
| `list_meta_pixels` | meta_ads_read | Wants the Meta pixels of an ad account and when each last fired, for example to check Meta conversion tracking. |
| `list_meta_product_sets` | meta_ads_read | Wants the product sets inside a Meta catalog for dynamic ads. |
| `list_meta_saved_audiences` | meta_ads_read | Wants the saved targeting presets of a Meta ad account. |
| `meta_campaign_insights` | meta_ads_read | Wants Meta Ads performance (spend, reach, clicks, results) for campaigns, ad sets or ads. |
| `meta_change_history` | meta_ads_read | Asks who changed what in a Meta ad account, and when. |
| `meta_delivery_estimate` | meta_ads_read | Wants the estimated audience size and daily results of an existing Meta ad set. |
| `meta_insights_query` | meta_ads_read | Needs Meta Insights metrics, breakdowns or filters that the standard Meta report does not cover. |
| `meta_reach_estimate` | meta_ads_read | Wants the estimated Meta audience size for a targeting idea before creating an ad set. |
| `preview_meta_ad` | meta_ads_read | Wants to see how a Meta ad creative looks, without publishing it. |
| `search_meta_interests` | meta_ads_read | Needs Meta detailed-targeting IDs (interests, employers, job titles, schools) by name. |

## Add (preview, then confirm)

| Operation | Tool | Use it when |
|---|---|---|
| `connect_meta_ads` | meta_ads_create | Wants to connect a Meta (Facebook and Instagram) ad account, or reconnect after Meta's 60-day access expires. |
| `copy_meta_entity` | meta_ads_create | Wants a paused copy of a Meta campaign, ad set or ad. |
| `create_meta_ab_test` | meta_ads_create | Wants a Meta A/B split test that compares two existing campaigns. |
| `create_meta_adset` | meta_ads_create | Wants a new Meta ad set with targeting, placements, budget, schedule and optimization; it is created paused unless the user asks to launch it. |
| `create_meta_campaign` | meta_ads_create | Wants a new Meta campaign with its objective, budget and special ad category; it is created paused unless the user asks to launch it. |
| `create_meta_carousel_ad` | meta_ads_create | Wants a Meta carousel ad with 2 to 10 cards. |
| `create_meta_custom_conversion` | meta_ads_create | Wants a Meta custom conversion on a pixel, based on a URL rule or an event. |
| `create_meta_dynamic_ad` | meta_ads_create | Wants a Meta dynamic product ad that pulls products from a catalog. |
| `create_meta_engagement_audience` | meta_ads_create | Wants a Meta retargeting audience of people who engaged with videos, a Page, Instagram, lead forms or events. |
| `create_meta_instagram_post_ad` | meta_ads_create | Wants to turn an existing Instagram post or Reel into a Meta ad. |
| `create_meta_lead_form` | meta_ads_create | Wants a Meta instant form (lead form) on a Facebook Page for lead ads. |
| `create_meta_link_ad` | meta_ads_create | Wants a Meta single image or link ad, created with its creative in one step. |
| `create_meta_lookalike_audience` | meta_ads_create | Wants a Meta lookalike audience from an existing custom audience. |
| `create_meta_pixel` | meta_ads_create | Wants a new Meta pixel in an ad account to track website conversions; if the account already has one, the existing pixel is returned. |
| `create_meta_post_ad` | meta_ads_create | Wants to promote an existing Facebook Page post as a Meta ad. |
| `create_meta_video_ad` | meta_ads_create | Wants a Meta video ad from an uploaded video or a video URL. |
| `create_meta_website_audience` | meta_ads_create | Wants a Meta retargeting audience of website visitors tracked by a pixel. |
| `instagram_follower_growth` | meta_ads_create | Asks how many Instagram followers an account gained per day, for example to measure a follower campaign. |
| `upload_meta_image` | meta_ads_create | Wants to upload an image to Meta and get a reusable image hash for ads. |
| `upload_meta_video` | meta_ads_create | Wants to upload a video to Meta for video ads. |

## Change, pause or delete (preview, then confirm)

| Operation | Tool | Use it when |
|---|---|---|
| `delete_meta_ad` | meta_ads_edit | Wants to permanently delete a Meta ad. |
| `delete_meta_adset` | meta_ads_edit | Wants to permanently delete a Meta ad set. |
| `delete_meta_audience` | meta_ads_edit | Wants to delete a Meta custom or lookalike audience. |
| `delete_meta_campaign` | meta_ads_edit | Wants to permanently delete a Meta campaign. |
| `send_meta_conversion_event` | meta_ads_edit | Wants to send a server-side conversion event to Meta through the Conversions API. |
| `update_meta_ad` | meta_ads_edit | Wants to pause, resume, archive or rename one Meta ad. |
| `update_meta_ad_creative` | meta_ads_edit | Wants to replace an existing Meta ad's creative while keeping the ad, its learning and its history. |
| `update_meta_adset` | meta_ads_edit | Wants to change a Meta ad set's status, budget, bid, optimization, placements or targeting. Budget increases are capped at +50% per change and +100% within 24 hours. |
| `update_meta_campaign` | meta_ads_edit | Wants to pause, resume, archive, rename or change the budget of a Meta campaign. Budget increases are capped at +50% per change and +100% within 24 hours. |
| `update_meta_custom_conversion` | meta_ads_edit | Wants to rename a Meta custom conversion or set its description or default value. |
| `update_meta_instagram_post_ad` | meta_ads_edit | Wants to add or change the pre-filled WhatsApp or Messenger message, button or Advantage+ settings of an existing Instagram post ad. |
