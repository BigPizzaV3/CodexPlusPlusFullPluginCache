---
name: meta-ads-creative-fatigue
description: Find tired Meta ads with Toffu, from frequency, CTR decline and CPA drift. Use when the user asks which ads to refresh, kill or keep, why Meta performance is dropping, or wants a creative fatigue audit.
---

Use the Toffu tools. Never apply a change the user has not confirmed.

1. Call `get_account_context`. If a platform has several accounts, ask which one. Pass the ids as `account_ids` to `query_campaign_performance`, and as `account_id` to the other tools.
2. Read data with `query_campaign_performance` (daily rows: `time_increment` "1"), `list_campaigns`, `list_ad_sets` and `list_ads`.
3. To change something, call `propose_update_campaign`, `propose_update_ad_set` or `propose_update_ad`, and show the preview. Call `apply_change` only after the user confirms that change.

Pull ad rows with `query_campaign_performance` `level` "ad" and `platforms` ["meta_ads"], once for the last 7 days and once for the last 30. CTR = clicks / impressions; CPA = spend / conversions. Read each ad's status from `list_ads`.

# Meta Ads Creative Fatigue Detection

Use when the user asks "which ads are tired", "what should we refresh", "why is performance dropping", "creative fatigue audit", or wants a kill/keep/refresh recommendation per ad.

## Signal stack (all three must be checked, not just frequency)

1. **Frequency**: lifetime impressions per unique reached user. Pull `frequency` from the ad-level insights. Flag at >= 3.0 for prospecting, >= 5.0 for retargeting.
2. **CTR decay**: compare last-7-day CTR to trailing-30-day CTR. Decay >= 25% is a fatigue signal even when frequency is fine.
3. **CPA drift**: last-7-day CPA vs trailing-30-day CPA. Drift >= 30% upward, with conversions > 0 in both windows, confirms fatigue. Drift on a base of 0 conversions is noise.

A single signal is suggestive. Two signals = confirmed fatigue. Three = act today.

## Procedure

1. Pull ad-level insights for the date range with fields: `ad_id`, `ad_name`, `impressions`, `reach`, `frequency`, `clicks`, `ctr`, `spend`, `actions`, `cost_per_action_type`. Group by ad.
2. Compute the three signals per ad. Use date_preset=last_7d and last_30d in two calls.
3. Cross-reference with `effective_status` — exclude PAUSED/ARCHIVED ads from the "act today" list.
4. Output one row per ad with: name, lifetime spend, last-7d CTR, 30d CTR, % CTR change, last-7d CPA, 30d CPA, % CPA change, frequency, signal count (0-3), recommendation.

## Recommendations vocabulary

- **Keep**: 0 signals, performance flat or improving.
- **Watch**: 1 signal, frequency under threshold. Re-audit in 7 days.
- **Refresh creative**: 2 signals. Same offer/audience, new hook/visual. Don't pause yet — duplicate first.
- **Kill**: 3 signals OR spend > 2x target CPA in last 7 days with no conversions. Pause and reallocate budget.

## Pitfalls

- Don't act on frequency alone for retargeting. High frequency on a tight retargeting pool is expected.
- Don't compare CTR across placements. Reels CTR is structurally lower than Feed; use placement-stratified breakdowns when the ad is mixed-placement.
- Don't kill an ad with high frequency and stable CTR/CPA. Saturation, not fatigue, is the diagnosis. Expand audience instead.
- Always present the data as a sortable table, sorted by signal count descending then spend descending.
