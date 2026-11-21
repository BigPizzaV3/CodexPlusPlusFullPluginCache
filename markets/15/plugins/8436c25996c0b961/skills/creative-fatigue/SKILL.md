---
name: creative-fatigue
description: Find tired Meta ad creatives with Toffu. Use when the user asks which ads are fatigued, what to refresh, why results drop, or for a creative audit. Compares each creative's frequency, CTR and CPA in the last 7 days against the 3 weeks before, and gives a keep, watch, refresh or pause call per ad.
---

# Meta Ads creative fatigue

Use the Toffu tools only. Never apply a change the user has not confirmed.

## Steps

1. Call `get_account_context`. If several Meta ad accounts are connected, ask which one, and pass its id as `account_id`.
2. Call `creative_report` for the last 7 full days (end date = yesterday). Then call it for the 21 days before. Each row is one ad, with its creative title, text, thumbnail and metrics.
3. Match the rows by `ad_id`. For each ad with spend in both windows, compute:
   - CTR change = (CTR last 7 days - CTR before) / CTR before
   - CPA change = (CPA last 7 days - CPA before) / CPA before, only when both windows have conversions
   - Frequency in the last 7 days
4. Count the fatigue signals:
   - **Frequency:** 3.0 or more for prospecting, 5.0 or more for retargeting (campaign or ad set name with "retargeting", "remarketing" or "DPA").
   - **CTR decay:** CTR down 25% or more.
   - **CPA drift:** CPA up 30% or more.
5. Give each ad one call:
   - **Keep:** 0 signals.
   - **Watch:** 1 signal. Check again in 7 days.
   - **Refresh:** 2 signals. Keep the offer and audience, change the hook or visual.
   - **Pause:** 3 signals, or spend in the last 7 days above 2x the account CPA with 0 conversions.
6. Report one table, sorted by signal count and then spend: ad, campaign, thumbnail link, spend, frequency, CTR and CPA in both windows, signals, call. Under it, say what the best creatives have in common (format, hook, offer), from their title and text.
7. For each ad marked Pause, offer `propose_update_ad` `{"status": "PAUSED"}`. Show the preview. Call `apply_change` only after the user confirms. Before pausing the last active ad of an ad set, tell the user that the ad set stops delivering.

## Rules

- High frequency with steady CTR and CPA is saturation, not fatigue. Recommend a broader audience, not a pause.
- A change on fewer than 10 conversions is noise. Say so.
- Toffu cannot upload new images or videos here. For a refresh, describe the new creative so the user can make it.
