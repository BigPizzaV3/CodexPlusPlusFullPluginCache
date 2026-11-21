---
name: audience-breakdown
description: Break down Meta Ads results by age, gender and placement with Toffu. Use when the user asks who converts, which age group or gender to target, which placements (Facebook, Instagram, Reels, Stories) work, or how to structure ad sets. Finds the segments that waste or win and proposes targeting or budget changes the user confirms.
---

# Meta Ads audience and placement breakdown

Use the Toffu tools only. Never apply a change the user has not confirmed.

## Steps

1. Call `get_account_context`. If several Meta ad accounts are connected, ask which one. Pass its id as `account_ids` `{"meta_ads": "<id>"}` to `query_campaign_performance`, and as `account_id` to the other tools.
2. Call `query_campaign_performance` for the last 30 full days (end date = yesterday) three times, with `breakdowns` `["age"]`, then `["gender"]`, then `["publisher_platform", "platform_position"]`.
3. For each segment, compute spend share, conversions, CPA = spend / conversions and ROAS = conversion_value / spend. Compare with the account average.
4. Flag:
   - **Waste segment:** at least 10% of spend, and CPA above 1.5x the account CPA (or 0 conversions).
   - **Winning segment:** ROAS above 1.3x the account ROAS, with at least 10 conversions.
   - **Placement gap:** a placement with spend and CTR below half of the account CTR.
5. Call `list_ad_sets` with `filters` `{"fields": "id,name,status,campaign_id,daily_budget,optimization_goal,targeting,promoted_object"}` for the current targeting of the ad sets that carry the waste or winning segments.
6. Report one table per breakdown (segment, spend, share, conversions, CPA, ROAS, flag) and at most 3 recommendations.
7. Offer each recommendation as a change:
   - Narrow an age range or placements with `propose_update_ad_set` `{"targeting": {...}}`. Meta replaces the whole targeting, so send the ad set's current targeting from step 5 with only the changed keys edited. Check that the preview's `current` and `data` differ only in those keys.
   - Test a winning segment in a new paused ad set with `propose_create_ad_set` (`name`, `optimization_goal`, `targeting`, `promoted_object` copied from the current ad set).
   - Move budget to the ad set with the winning segment with `propose_update_ad_set` or `propose_update_campaign` `{"daily_budget_amount": <amount>}`.
   Show the preview. Call `apply_change` only after the user confirms that change.

## Rules

- Breakdowns are Meta's estimates and do not add up exactly to the campaign total. Say so when the gap is above 5%.
- Advantage+ audiences and placements often do better than manual exclusions. Recommend a test before an exclusion when the segment has fewer than 30 conversions.
- Do not narrow targeting under a special ad category (housing, employment, credit, politics).
