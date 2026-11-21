---
name: paid-media-review
description: Review paid advertising performance across Google Ads, Meta Ads, LinkedIn Ads and Microsoft Ads in CitationLab. Use for questions about campaign results, spend, conversions, cost per result or which campaigns to cut or scale.
---

# Paid media review

All tools need `projectId` and read the performance data CitationLab has synced from each connected ad account. They never change an ad account.

- **Google Ads:** `list_gads_campaigns` for campaigns with spend, clicks and conversions (`yearMonth` as YYYY-MM, or `startMonth`/`endMonth`); `get_gads_metrics` with `entityType` (`campaign`, `ad_group`, `keyword`, `search_term`, …) for a breakdown.
- **Meta Ads:** `list_meta_ads_campaigns`, `get_meta_ads_metrics` (monthly) and `get_meta_ads_daily_metrics` (day by day, for week-over-week comparisons).
- **LinkedIn Ads:** `get_linkedin_ads_metrics`.
- **Microsoft Ads:** `get_bing_ads_metrics`.
- Use `get_integration_status` first if you are unsure which platforms are connected.

## How to report

- Lead with spend and conversions for the period per platform, then the largest inefficiencies by name with their cost, then recommended changes ranked by expected impact.
- Amounts are in the account currency; say which.
- Changes to campaigns are made in the ad platform or in the CitationLab app. Offer to record a recommended change as an action (see `actions-and-follow-up`).
