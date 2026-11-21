---
name: spend-anomaly-detection
description: Find spend anomalies across all connected ad platforms with Toffu: sudden spikes, drops to zero and slow drift. Use when the user asks if anything is wrong or unusual in spend, whether something spiked, or wants a morning check before standup.
---

Use the Toffu tools. Never apply a change the user has not confirmed.

1. Call `get_account_context`. If a platform has several accounts, ask which one. Pass the ids as `account_ids` to `query_campaign_performance`, and as `account_id` to the other tools.
2. Read data with `query_campaign_performance` (daily rows: `time_increment` "1"), `list_campaigns`, `list_ad_sets` and `list_ads`.
3. To change something, call `propose_update_campaign`, `propose_update_ad_set` or `propose_update_ad`, and show the preview. Call `apply_change` only after the user confirms that change.

`list_campaigns` gives the current status only, with no change history: say "paused now", without a time or a person.

# Cross-Channel Spend Anomaly Detection

Use when the user asks "anything weird in spend yesterday", "did anything spike", "is everything pacing", "anomalies", or wants a daily morning sanity check across Google Ads, Meta Ads, LinkedIn Ads, TikTok Ads. This is the first thing an agency lead checks before standup.

## What counts as an anomaly

Compare yesterday's spend per (account, campaign) to the trailing-14-day median for the same weekday slot:

1. **Spike**: yesterday > 1.5x median AND absolute delta > $100. Could be a budget bug, a runaway bid, a Smart Bidding excursion, or an unexpected promo.
2. **Drop-to-zero**: median > $20 AND yesterday == 0. Account suspended, payment failed, campaign accidentally paused, daily budget exhausted before midnight.
3. **Slow drift**: 7-day moving average up > 25% vs prior 7-day moving average. Less urgent but a brief should mention it.

Weekday-aware comparison matters. Saturday spend is structurally different from Tuesday. Don't use a single trailing-N-day mean.

## Procedure

1. Pull yesterday's per-campaign spend for every active account in scope. Same for the prior 14 days.
2. For each (account, campaign), compute the weekday-matched median (e.g., last 2 Tuesdays if yesterday was Tuesday).
3. Apply the three rules above.
4. Cross-reference against status changes: if `effective_status` flipped to PAUSED in the last 24h, the drop is operator-induced — note it as "paused yesterday at HH:MM by <user>" rather than as an anomaly.

## Output format

Three sections, in this order:

**Critical (act today)**: drops to zero on accounts spending > $200/day. Bullet per anomaly with the diagnostic ("budget exhausted at 14:32 — raise budget" / "ad account disapproved — check Business Manager").

**High (review today)**: spikes above 1.5x median, absolute delta > $500.

**Watch (mention in weekly)**: drift, smaller spikes.

Lead with the headline: "X critical, Y high, Z watch. Total unexpected spend yesterday: $N." If empty: "Nothing unusual."

## Pitfalls

- New campaigns don't have 14 days of history. Skip them or flag as "new — no baseline" — don't false-positive every launch.
- Account-level vs campaign-level: detect at campaign level so a budget shift between two campaigns in the same account isn't reported as both a spike AND a drop.
- Currency mixing kills the dollar-threshold logic. Convert everything to the agency's reporting currency before applying $100/$500 cutoffs.
- Don't alert on weekend spend dropping. Most accounts intentionally taper. Use weekday-matched medians.
