---
name: tiktok-ads
description: TikTok Ads with Opus Growth - campaigns, ad groups, ads, Spark ads from existing posts, video and image uploads, identities, pixels and events, lead forms, direct message and WhatsApp ads, Smart+, audiences, search negatives and reporting. Use for any TikTok Ads Manager question or change. Covers the objectives TikTok retires on 1 January 2027, identity and cover-image requirements, and fields TikTok silently ignores.
---

# TikTok Ads

Follow the `opus-growth` skill for preview, confirm, dates and budgets. Structure: campaign
(objective, optional budget) → ad group (targeting, placements, budget, optimization, bidding)
→ ad (identity + creative). A campaign alone never spends; ad groups are created disabled and
ads paused.

## Which tool

| Need | Tool |
|---|---|
| One-call picture | `account_snapshot` (platform tiktok) |
| Performance | `tiktok_campaign_report`, `get_report`; custom metrics and dimensions `tiktok_report_query` |
| What changed | `tiktok_change_history` |
| TikTok's own suggestions | `tiktok_recommendations` |
| Locations | `tiktok_region_search` |
| Interests, behaviours | `tiktok_targeting_search` |
| Account standing, business verification | `tiktok_advertiser_qualification` |

## Before building: objective and flow

- TikTok stops accepting new manual campaigns, ad groups and ads for PRODUCT_SALES,
  WEB_CONVERSIONS, APP_PROMOTION and LEAD_GENERATION on 1 January 2027. Existing campaigns keep
  running and can still be edited. For new conversion, lead or app work use Smart+
  (`automation=SMART_PLUS` on `create_tiktok_campaign`), which needs a campaign budget above
  TikTok's per-account minimum. TRAFFIC, REACH, VIDEO_VIEWS and ENGAGEMENT are not affected.
- TikTok Shop sales run only as GMV Max since 2026 (`list_tiktok_gmv_max_stores`); manual shop
  ads can no longer be created or edited.
- Conversion optimization (CONVERT) needs a pixel and an optimization event that already fires
  (`list_tiktok_pixels`). Without events, optimize for clicks or landing page views first.
- Each ad group has a daily budget minimum per currency (about 20 USD converted); TikTok's error
  states the exact minimum for the account.

## Building

1. `create_tiktok_campaign` with objective and budget mode.
2. `create_tiktok_adgroup`: `location_ids` from `tiktok_region_search` (required), age groups,
   genders, optimization goal, billing event, promotion type (what is advertised: website, app,
   instant form, direct message, WhatsApp...). Pacing FAST works only with a manual bid; automatic
   bidding needs SMOOTH.
3. Creative:
   - Spark ad: `tiktok_item_id` of an existing post (`list_tiktok_posts`); the identity must own
     the post. Usually the strongest option because the post keeps its likes and comments.
   - Uploaded video: `upload_tiktok_video`. TikTok also requires a cover image; when none is
     given, `create_tiktok_ad` uploads the video's own cover frame. If TikTok still asks for an
     image, take the video's `cover_url` from `list_tiktok_videos` right away (the URL expires),
     upload it with `upload_tiktok_image` and pass the image id.
   - Identity: the ad runs under a real TikTok account identity (`list_tiktok_identities`).
     Custom brand-name identities are retired by TikTok and cannot run ads.
   - TikTok requires an AI-generated content disclosure; set `ai_generated=yes` when the media
     came from an AI tool.
4. `create_tiktok_ad`, read back with `list_tiktok_ads`, enable on request.

## Messaging ads

- Direct message ad groups (`optimization_goal=CONVERSATION`) need an approved auto message
  template (`list_tiktok_auto_messages`, `create_tiktok_auto_message`; status must be PASS).
- Click-to-WhatsApp ads take `whatsapp_number` with the country code.

## Editing without losing learning

- `update_tiktok_adgroup` changes targeting, bid and schedule in place. Never delete and rebuild
  an ad group to change targeting: that resets learning and loses history.
- A bid only applies with manual bidding (the tool sets BID_TYPE_CUSTOM when you pass a bid);
  read the ad group back to confirm the bid stuck.
- TikTok's learning phase wants about 50 conversions per ad group in 7 days; frequent edits and
  very small budgets keep it learning.

## Locations

TikTok returns place names without Turkish or other accents ("Izmir", "Sehzadeler"), down to
district level in many countries. Match accent-insensitively and check the parent region before
choosing an id; many city names repeat across countries.

## Leads and audiences

Leads from instant forms: `download_tiktok_leads` (fields via `get_tiktok_lead_form_fields`).
Audiences: customer files (`create_tiktok_customer_file_audience`), lookalikes
(`create_tiktok_lookalike_audience`), sharing across accounts (`share_tiktok_audience`). Search
ads negatives: `manage_tiktok_search_negative_keywords`.

## Policy review

`list_tiktok_ads` returns `delivery_status`. When that status is in audit or rejected, the same
row includes `review` with TikTok's reason text. `tiktok_ad_review` reads that text again for
specific ad ids. Quote the reason. Do not treat the status code as the policy explanation.

## Reporting notes

TikTok's default attribution is 7-day click and 1-day view, so recent days fill in later. Video
metrics (2-second and 6-second views, average watch time) tell whether the first seconds hold
attention; low watch time with good targeting is a creative problem, not an audience problem.

## Every operation

The complete list of this area's operations, what each is for and the tool that runs it: `references/operations.md`.
