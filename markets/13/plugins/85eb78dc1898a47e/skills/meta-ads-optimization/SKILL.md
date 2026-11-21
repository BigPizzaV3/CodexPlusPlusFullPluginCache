---
name: meta-ads-optimization
description: Improve Meta Ads with Toffu: creative testing, audiences, budget optimization and placements. Use when the user asks how to test creatives, structure Meta campaigns or ad sets, or why Meta results changed.
---

Use the Toffu tools. Never apply a change the user has not confirmed.

1. Call `get_account_context`. If a platform has several accounts, ask which one. Pass the ids as `account_ids` to `query_campaign_performance`, and as `account_id` to the other tools.
2. Read data with `query_campaign_performance` (daily rows: `time_increment` "1"), `list_campaigns`, `list_ad_sets` and `list_ads`.
3. To change something, call `propose_update_campaign`, `propose_update_ad_set` or `propose_update_ad`, and show the preview. Call `apply_change` only after the user confirms that change.

# Meta Ads Optimization Framework

## Creative Testing Methodology
- **Dynamic Creative Testing (DCT)**: provide 5 headlines, 5 images/videos, 5 primary text variants. Meta tests combinations.
- **Manual A/B testing**: isolate one variable (image, headline, CTA). Run with equal budget splits.
- Test creative concepts (humor vs authority vs UGC) before optimizing copy within a concept.
- Kill underperformers at 2x CPA or after 1,000 impressions with no conversions. Don't let losers drain budget.

## Audience Segmentation
- **Broad targeting**: let Meta's algorithm find converters. Works best with 50+ conversions/week.
- **Lookalike audiences**: 1% for precision, 3-5% for scale. Source from purchasers, not just site visitors.
- **Retargeting**: segment by recency (1-3 days, 4-14 days, 15-30 days). Increase urgency as recency fades.
- Avoid audience overlap between ad sets — use the Audience Overlap tool to check.

## Campaign Budget Optimization (CBO)
- CBO distributes budget to top-performing ad sets automatically.
- Set minimum spend limits on ad sets you want to protect from getting zero spend.
- CBO works best with 3-5 ad sets of similar audience size.

## Ad Fatigue Detection
- Monitor **frequency** and **CTR trend**. CTR dropping while frequency rises = fatigue.
- Refresh creative every 2-4 weeks for retargeting, every 4-8 weeks for prospecting.
- Rotate creative formats: static -> carousel -> video -> UGC. Don't just swap colors.

## Placement Optimization
- Start with **Advantage+ placements** (all placements). Let Meta optimize.
- Review placement breakdown after 500+ impressions per placement.
- Create placement-specific assets: 9:16 for Stories/Reels, 1:1 for Feed, 16:9 for in-stream.

## Conversion API (CAPI)
- Server-side tracking is mandatory for accurate attribution post-iOS 14.5.
- Implement via partner integration (Shopify, GTM server-side) or direct API.
- Deduplicate events between pixel and CAPI using event_id parameter.
- Monitor Event Match Quality score — aim for "Good" or above.

## Attribution Windows
- Default: 7-day click, 1-day view. Suitable for most e-commerce.
- Longer consideration cycles (B2B, high-ticket): test 28-day click attribution.
- Compare attribution windows to understand the true conversion lag of your funnel.
