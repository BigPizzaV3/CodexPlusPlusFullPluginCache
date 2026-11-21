---
name: attribution-modeling
description: Explain marketing attribution with Toffu: attribution models, windows, incrementality tests and media mix models. Use when the user asks why platforms report different conversions, which attribution model to trust, or how to measure a channel's real impact.
---

Use the Toffu tools. Never apply a change the user has not confirmed.

1. Call `get_account_context`. If a platform has several accounts, ask which one. Pass the ids as `account_ids` to `query_campaign_performance`, and as `account_id` to the other tools.
2. Read data with `query_campaign_performance` (daily rows: `time_increment` "1"), `list_campaigns`, `list_ad_sets` and `list_ads`.
3. To change something, call `propose_update_campaign`, `propose_update_ad_set` or `propose_update_ad`, and show the preview. Call `apply_change` only after the user confirms that change.

# Marketing Attribution Methodology

## Attribution Model Comparison

### Rule-Based Models
- **Last-click**: all credit to the final touchpoint. Simple but biases toward bottom-funnel channels.
- **First-click**: all credit to the first touchpoint. Highlights acquisition channels but ignores nurturing.
- **Linear**: equal credit to all touchpoints. Fair but undifferentiating.
- **Time-decay**: more credit to touchpoints closer to conversion. Good for short sales cycles.
- **Position-based (U-shaped)**: 40% first, 40% last, 20% distributed across middle. Balances acquisition and closing.

### Algorithmic Models
- **Data-driven attribution** (GA4, Google Ads): uses machine learning on your data to distribute credit.
- Requires sufficient conversion volume (typically 300+ conversions/month for reliability).
- More accurate than rule-based but less transparent — treat as a black box.

## Incrementality Testing
- Attribution models measure correlation. Incrementality measures causation.
- **Geo-holdout tests**: suppress a channel in test markets. Compare conversion rates to control markets.
- **Ghost ads / PSA tests**: serve a public service ad to the control group instead of your ad.
- **Conversion lift studies**: platform-native (Meta, Google). Randomized control/exposed groups.
- Run incrementality tests quarterly on your largest spend channels.

## Media Mix Modeling (MMM)
- Regression-based approach using aggregate data (spend, impressions, external factors like seasonality).
- Doesn't require user-level tracking — works in a cookieless world.
- Best for budget allocation decisions across channels at the strategic level.
- Limitations: needs 2+ years of data, slow to reflect rapid changes, expensive to build in-house.

## Cross-Device Tracking
- Users convert across devices. Mobile discovery -> desktop purchase is common.
- Use Google Signals (GA4) for cross-device reporting — requires users to be signed into Google.
- Supplement with CRM data: email-based identity resolution across touchpoints.

## Offline Conversion Import
- Close the loop between online clicks and offline outcomes (phone calls, in-store purchases, closed deals).
- Import offline conversions to Google Ads and Meta via their respective APIs.
- Match on GCLID (Google) or FBCLID (Meta). Automate the upload pipeline.
- Offline data dramatically improves algorithmic bidding for lead-gen businesses.

## Attribution Window Selection
- Shorter windows (7-day click) are more conservative but may undercount longer journeys.
- Longer windows (28-day click) capture more conversions but include more noise.
- Match the window to your typical sales cycle. B2C impulse: 7-day. B2B consideration: 28-90 day.
