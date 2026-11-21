---
name: weekly-report
description: Weekly Meta Ads performance report with Toffu. Use when the user asks for a weekly report, a week-over-week comparison, or how last week went on Facebook and Instagram. Compares the last 7 days with the 7 days before, highlights the best and worst campaigns and creatives, and changes over 20%.
---

# Meta Ads weekly report

Use the Toffu tools only. This skill changes nothing unless the user asks for a change.

## Steps

1. Call `get_account_context`. If several Meta ad accounts are connected, ask which one. Pass its id as `account_ids` `{"meta_ads": "<id>"}` to `query_campaign_performance`, and as `account_id` to the other tools.
2. Call `query_campaign_performance` for the last 7 full days (end date = yesterday), then for the 7 days before.
3. Call `creative_report` for the last 7 full days.
4. For the account and for each campaign, compute for both weeks: spend, impressions, reach, clicks, CTR = clicks / impressions, conversions, CPA = spend / conversions, ROAS = conversion_value / spend. When the denominator is 0, show "n/a", never 0 or infinity.
5. Report:
   - Account totals for both weeks, with the change in percent.
   - The 3 best campaigns by ROAS and the 3 worst by CPA (campaigns with spend only).
   - Every campaign whose CPA, ROAS, conversions or spend changed by more than 20%, marked as better or worse. Percent change = (this week - last week) / last week. When last week is 0 or n/a, show "new".
   - The top 3 creatives of the week by ROAS, with title, thumbnail link, spend and frequency, and any active creative with frequency 3 or more.
6. End with at most 3 recommended next steps. If the user wants a change, use the matching `propose_update_campaign`, `propose_update_ad_set` or `propose_update_ad` call, show the preview, and call `apply_change` only after the user confirms.

## Rules

- Use the account currency.
- A change on fewer than 10 conversions is noise. Say so instead of calling it a trend.
- Meta reports conversions by attribution date, so the last 1 to 3 days can still rise. Say so when last week looks worse only at its end.
