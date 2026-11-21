---
name: google-ads
description: Google Ads with Opus Growth - Search, Performance Max, Demand Gen, Display and App campaigns, keywords, negatives, search terms, ads and extensions, bidding, audiences, conversion tracking, experiments and recommendations. Use for any Google Ads or AdWords question or change. Covers the traps where Google reports "active" while nothing serves, and the changes Google's API does not allow.
---

# Google Ads

Follow the `opus-growth` skill for preview, confirm, dates and budgets. Google Ads tools take
`customer_id` (digits, hyphens optional); empty uses the connected default account. Agencies:
`list_google_ads_accounts` lists every reachable account, `google_ads_portfolio_report` covers
many accounts in one report.

## Which tool

| Need | Tool |
|---|---|
| One-call picture of the account | `account_snapshot` (platform google_ads) |
| Metrics by campaign, ad group, ad, keyword, device, geo, hour, conversion action | `google_ads_performance_report` or `get_report` |
| Fast first audit (wasted search terms, rank loss, tracking problems) | `google_ads_instant_audit` |
| Keyword hygiene and Quality Score | `google_ads_account_audit`, `google_ads_keyword_report`, `google_ads_keyword_quality_report` |
| What people actually searched | `google_ads_search_terms_report` |
| Negative candidates ranked by waste | `google_ads_negative_keyword_suggestions` |
| Lost impression share (budget vs rank) | `google_ads_impression_share_analysis` |
| Month pacing | `google_ads_budget_pacing_alerts` |
| Disapproved or limited ads | `google_ads_list_ad_policy_issues` |
| Who changed what (last 30 days) | `google_ads_get_change_history` |
| Anything no report returns | `google_ads_query` (read-only GAQL SELECT) |

## Status: what "active" really means

- A campaign's `status` (ENABLED/PAUSED/REMOVED) is not what the Google Ads interface shows. The
  interface shows the primary status. An ENABLED campaign past its end date is ENDED and serves
  nothing. `list_entities` returns `is_serving` and `serving_status`; use those when the user asks
  what is running.
- Serving means primary status ELIGIBLE, LIMITED or LEARNING. PENDING, ENDED, PAUSED,
  NOT_ELIGIBLE and MISCONFIGURED do not serve.
- **Enabled, approved, eligible, and zero impressions?** Before discussing bids or keywords, check
  the account-level spending limit:
  `google_ads_query` with `SELECT account_budget.status, account_budget.amount_served_micros,
  account_budget.adjusted_spending_limit_micros FROM account_budget`. When served equals the
  limit, the account is stopped and every campaign status still looks fine. A limit can never be
  set below what was already spent; Google rounds it up to the spent amount and the account stops
  for good. Report it; the user changes billing in Google Ads.
- An ad's own status is independent of its campaign. Ads created paused stay paused when the
  campaign is enabled.

## Building a campaign

1. **Type.** Search for people searching for the offer; Performance Max when there is conversion
   tracking, a feed or good images and the user accepts less control; Demand Gen for YouTube,
   Discover and Gmail visuals; Display mostly for remarketing; App for app installs. New Smart
   campaigns can no longer be created (Google stopped it).
2. **Inputs.** Daily budget, final URL, locations, languages, conversion goal. Resolve places with
   `google_ads_geo_target_search`. A Search campaign without locations targets the whole world.
   `presence_only=true` limits it to people in the area (Google's default also includes people
   interested in it).
3. **Create** (`google_ads_create_search_campaign`, `google_ads_create_pmax_campaign`,
   `google_ads_create_demand_gen_campaign`, `google_ads_create_display_campaign`,
   `google_ads_create_app_campaign`). Campaigns are created paused.
4. **Search build-out.** `google_ads_create_ad_group`, `google_ads_add_keywords` (per-item match
   type with `text|EXACT`), `google_ads_create_responsive_search_ad` with at least 8-10 distinct
   headlines and 3-4 descriptions, real display paths (path1/path2) and status ENABLED (the paused
   campaign already prevents spend; paused ads would block the launch later).
5. **Extensions are not optional for Search.** `google_ads_add_extension_assets`: at least 4
   sitelinks, 4 callouts, a structured snippet, and a call asset when calls matter. Brand name and
   logo: `business_name` / `logo_asset_id` at creation, later `google_ads_set_business_name` /
   `google_ads_set_business_logo` (one logo per campaign; the tool swaps it in one step).
6. **Performance Max** needs everything at once: 3+ headlines (≤30), 1+ long headline (≤90),
   2+ descriptions (≤90), a landscape image (1.91:1), a square image (1:1) and a square logo,
   uploaded first with `google_ads_upload_image_asset`. Images must be at least 300x300 for image
   extensions.
7. **Read it back** with `list_entities` and `google_ads_get_campaign_targeting`, then ask before
   enabling with `google_ads_update_campaign_status`.

## Bidding

- Since 17 August 2026 Google bids toward the set target even when a campaign is limited by
  budget. A campaign beating its target (for example 350% ROAS against a 200% target) drifts down
  toward the target. Before lowering a target or raising budget, compare the target with actual
  performance; set the target near what the campaign really achieves.
- With no conversion history, start with Maximize Clicks (optionally capped) or Manual CPC; move
  to Maximize Conversions, then Target CPA or ROAS once conversions accumulate (Google's
  guidance: a steady flow of conversions over the last 30 days). A target set far below the
  current CPA throttles delivery.
- Every bid strategy or target change restarts learning (roughly a week). Do not stack changes;
  change one thing, wait, measure.
- A CPC ceiling exists only on Maximize Clicks and Target Impression Share at campaign level; on
  other strategies it needs a portfolio strategy (`google_ads_manage_portfolio_bid_strategy`).
- A campaign inside a running experiment rejects bid strategy changes. Check
  `list_google_ads_experiments` first; end or promote the experiment before changing bidding.
- Display campaigns reject Target CPM; use viewable CPM, manual CPC, Maximize Clicks or Maximize
  Conversions.

## Performance Max and AI Max checks

Common findings in 2026 audits, worth checking in every account:
- Where Performance Max spends (Search, YouTube, Display, Gmail, Discover, Maps):
  `google_ads_performance_report` with `segment=network`.
- Performance Max without a target CPA or ROAS bids with no cost limit.
- Final URL expansion sends traffic to pages the advertiser never chose; exclude URLs that should
  not receive ads (`google_ads_manage_campaign_settings` shows the AI Max and URL expansion
  settings).
- Many Primary conversion actions (often 5-10) make Smart Bidding treat a newsletter sign-up like
  a sale; keep Primary only what the business pays for (`measurement` skill).
- AI Max is replacing Dynamic Search Ads; its matched searches carry `match_source` AI_MAX_BROAD_MATCH or
  AI_MAX_KEYWORDLESS in `google_ads_search_terms_report`. Treat AI Max searches like broad match: review
  them before trusting the conversions.
- Call-only ads can no longer be created; use responsive search ads with a call asset.

## Keywords, search terms and negatives

Load the `keywords` skill for research and search-term mining. Google-specific rules:
- Search terms are reported per ad group and matched keyword; the same term can appear several
  times. Rows already blocked by a negative carry `already_negative`; do not add them again.
- Negative keywords do not match close variants or synonyms: add plurals and misspellings
  explicitly. A phrase negative blocks every search containing the phrase in order; an exact
  negative blocks only that search; broad negative blocks searches containing all its words.
- Shared negative lists (`google_ads_manage_shared_negative_list`) keep account-wide exclusions
  (jobs, free, competitors) in one place.
- Smart campaign search terms are themes: they have no conversion data and cannot take negative
  keywords.

## Conversions

- `google_ads_conversion_tracking_health` first. `include_in_conversions_metric` is the real
  Primary flag (what bidding uses); `primary_for_goal` can mislead.
- Which campaign produced which conversion action: `google_ads_performance_report` with the
  conversion action breakdown. Google returns no cost in that breakdown by design.
- Calls: when account call reporting is on (`google_ads_set_call_reporting`), calls from ads are
  already counted by Google's default "Calls from ads" action. Creating a new "calls from ads"
  conversion action through the API is currently rejected by Google; do not ask the user to
  create one by hand when reporting is already on.
- Enhanced conversions for leads cannot be switched on through the API; it is a Google Ads
  interface setting.
- Offline / CRM sales: try `google_ads_upload_offline_conversions` (needs the GCLID or enhanced
  identifiers and an import conversion action). Google refuses this upload through the Google Ads
  API for integrations it has moved to its Data Manager API; when the tool answers that Google
  requires the Data Manager API, the user uploads the file in the Google Ads interface instead.
  Refunds and value corrections still work with `google_ads_upload_conversion_adjustments`, and
  Microsoft offline upload works (`upload_microsoft_offline_conversions`).

## Things Google does not allow through the API

- Deleting library assets: assets can only be unlinked (`google_ads_remove_extension_assets`).
  Before any "clean up the asset library" request, run `google_ads_list_assets` with usage: most
  "unused" text assets are inside paused ads that would break if removed.
- Auction Insights (competitor overlap) is not available in the API; the user exports it from the
  Google Ads interface.
- Lost impression share due to budget exists only at campaign level.
- A new account's currency and time zone (`create_google_ads_account`) can never be changed;
  the new account serves only after billing is added in Google Ads.
- Older campaigns may need the EU political advertising declaration before targeting edits
  (`google_ads_manage_campaign_settings`).
- Price assets accept only some languages and currencies; Turkish and TRY were rejected in our
  tests. Say so before promising price assets on such an account.

## Recommendations

Google recommendations raise the optimization score, not necessarily results. Review each one
(`google_ads_list_recommendations`) against the account goal; broad match and budget raises in
particular need conversion tracking you trust. Auto-applied recommendation types can be turned
off with `google_ads_manage_recommendation_auto_apply`.

## Every operation

The complete list of this area's operations, what each is for and the tool that runs it: `references/operations.md`.
