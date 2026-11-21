---
name: meta-ads
description: Meta Ads (Facebook and Instagram) with Opus Growth - campaigns, ad sets, ads, Instagram post ads, click-to-WhatsApp, Messenger and Instagram Direct ads, lead forms, audiences, pixels and conversions, reporting and change history. Use for any Facebook, Instagram, WhatsApp-ad or Meta Ads Manager question or change. Covers learning-phase rules, messaging setup that silently breaks delivery, and why Meta's numbers can mislead.
---

# Meta Ads

Follow the `opus-growth` skill for preview, confirm, dates and budgets. Meta's structure is
campaign (objective, optional campaign budget) → ad set (audience, placements, optimization,
budget unless the campaign holds it) → ad (creative). Budgets are in the account currency's main
unit.

## Which tool

| Need | Tool |
|---|---|
| One-call picture | `account_snapshot` (platform meta) |
| Performance by campaign, ad set or ad | `meta_campaign_insights`, `get_report` |
| Breakdowns (age, gender, placement, region, hour) and custom metrics | `meta_insights_query` |
| Why an ad is not delivering | `list_meta_ads` (delivery state and Meta's issue text) |
| Who changed what | `meta_change_history` |
| Audience size before building | `meta_reach_estimate`; for an existing ad set `meta_delivery_estimate` |
| Interests, employers, job titles | `search_meta_interests` |
| Read an ad's creative | `get_meta_ad_creative` |

## Reading Meta numbers correctly

- Meta's `ctr` and `clicks` count every click (likes, comments, profile, "see more"). Compare ads
  on link clicks and link CTR (`inline_link_clicks`, `inline_link_click_ctr` via
  `meta_insights_query`), especially boosted posts against conversion ads.
- "Results" follow each ad set's optimization goal, so results of different ad sets are not the
  same thing. Name the result type.
- Each ad set counts conversions with its own attribution setting (`attribution_spec` in
  `list_meta_adsets`; Meta's default is 7-day click and 1-day view). Quote it with the numbers so
  they match Ads Manager. Conversions are reported on the impression date; recent days fill in
  later.
- **Messaging results can lag or undercount.** A click-to-message campaign showing 0
  conversations while it has link clicks does not prove no one wrote. Ask the user to check the
  Business Suite inbox for chats labelled with the ad before cutting budget or blaming targeting.
- Change history times are UTC while other Meta timestamps use the account time zone; convert
  before saying "it changed on day X". In the change log, an object type of CAMPAIGN is an ad
  set and CAMPAIGN_GROUP is a campaign (Meta's legacy names).

## 2026 changes that change advice

- Since 15 January 2026 (Andromeda) detailed targeting is a suggestion, not a limit: Meta
  expands beyond interests when it predicts better results, and interest or behaviour
  exclusions are no longer available. The creative now decides who sees the ad: several clearly
  different creatives per ad set matter more than narrow interests.
- Advantage+ is the default for sales, app and leads campaigns.
- 7-day-view and 28-day-view attribution were removed; since March 2026 click-through
  attribution counts link clicks only. Results before and after these dates are not directly
  comparable; say so when comparing periods across them.

## Learning phase

An ad set needs about 50 optimization events in a week to exit learning. Large budget changes,
targeting, creative, optimization event or bid strategy edits, and pauses longer than about a
week can restart it. So:
- Group changes; avoid daily tweaks on an ad set that is still learning.
- Prefer fewer ad sets with more budget each over many small ones (budget split too thin never
  exits learning).
- Replace a tired creative with `update_meta_ad_creative`, which keeps the ad, its history and
  social proof, instead of deleting and recreating.

## Building

1. `create_meta_campaign`: objective OUTCOME_SALES, OUTCOME_LEADS, OUTCOME_TRAFFIC,
   OUTCOME_ENGAGEMENT, OUTCOME_AWARENESS or OUTCOME_APP_PROMOTION. A campaign budget makes it
   budget-optimized: the ad sets then get no budget of their own. Housing, employment, credit,
   finance and political ads must declare `special_ad_categories`, which limits targeting.
2. `create_meta_adset`: optimization goal, audience, placements, schedule. A lifetime budget needs
   an end time. Check audience size with `meta_reach_estimate` first.
3. Ad: `create_meta_link_ad`, `create_meta_video_ad`, `create_meta_carousel_ad`,
   `create_meta_post_ad` (existing Page post), `create_meta_instagram_post_ad` (existing post or
   Reel: get its id with `find_instagram_media_id` from the link), `create_meta_dynamic_ad`
   (catalog). Images and videos first via `upload_meta_image` / `upload_meta_video`. A video ad
   needs a cover image, taken from the video automatically; a video still processing at Meta
   can fail this, so retry after a minute. `preview_meta_ad` shows the ad before publishing.
4. Everything is created paused and goes through Meta review. Read back with `list_meta_ads`.

Sales and leads campaigns need a working pixel or Conversions API events (`list_meta_pixels`
shows when each pixel last fired). Without them, optimize for landing page views, not
conversions. An ad account without a pixel gets one with `create_meta_pixel`; if the account
already has one, Meta creates no second pixel and the existing one comes back. The pixel records
nothing until its code is on every page of the site (see the `measurement` skill).

## Click-to-message ads (WhatsApp, Messenger, Instagram Direct)

- Campaign OUTCOME_ENGAGEMENT, ad set optimization CONVERSATIONS with destination WHATSAPP,
  MESSENGER or INSTAGRAM_DIRECT and the Page. WhatsApp needs a WhatsApp number connected to the
  Page.
- The ad's button must match the destination: WHATSAPP → WHATSAPP_MESSAGE, MESSENGER →
  MESSAGE_PAGE, INSTAGRAM_DIRECT → INSTAGRAM_MESSAGE. A mismatch (often after duplicating a
  campaign in Ads Manager) is accepted at creation and then stops delivery. For Instagram post ads
  leave the button empty; Meta derives it from the destination.
- Use a welcome message (pre-filled text, at most 300 characters); without it the chat opens
  empty and the business's auto-reply does not fire.
- Ad sets built the older way (lead generation optimization with a messaging destination) are
  fragile: Meta can block status edits on their ads, and budget or targeting edits have stopped
  all their ads ("update required"). Do not edit those; rebuild as Engagement + Conversations.
- Instant replies and away messages in the Business Suite inbox have no public API; they are set
  in Business Suite.

## Targeting traps

- **Location expansion** (Meta also reaches people outside the chosen places who it thinks are
  interested in them) is separate from Advantage+ audience. "We get messages from cities we do
  not target" → check it first and turn it off with `update_meta_adset` `location_expansion="off"`.
- Advantage+ audience rejects a minimum age above 25.
- Targeting edits are rate limited (about one every 30 seconds per ad set).
- Excluded cities cannot carry a radius. Ad sets saved that way in Ads Manager reject edits,
  even pausing; pause at campaign level instead.
- Relationship and education status are top-level fields; life events, industries and behaviors
  are catalog entries found with `search_meta_interests`.

## Account-level blockers

`list_meta_ad_accounts` and `account_snapshot` (`account_alerts`) show a disabled account with
its `disable_reason` and a reached account spending limit. Either one stops every ad while
campaigns still read active. A disapproved ad carries `review_feedback` with Meta's policy reason;
quote it and fix that exact point.

## Errors that look like something else

- Code 31 / subcode 3858385 "Please authenticate your account": a security re-check, not business
  verification. The user opens any ad or ad set in Ads Manager edit view and starts the
  verification shown in the right panel.
- Meta access tokens last 60 days without refresh: when they expire every call fails; reconnect
  with `connect_meta_ads`.
- A write that returns success is not proof. After changing creatives, welcome messages or
  Instagram identity, read back with `get_meta_ad_creative`.

## Audiences

Website visitors (`create_meta_website_audience`, needs a pixel), engagers
(`create_meta_engagement_audience`: video viewers 10s, ThruPlay, 25-100%; Page; Instagram; lead
forms), lookalikes from a seed (`create_meta_lookalike_audience`). New custom audiences take time
to fill; a very small audience will not deliver.

## Every operation

The complete list of this area's operations, what each is for and the tool that runs it: `references/operations.md`.
