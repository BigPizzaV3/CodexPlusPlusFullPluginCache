---
name: weekly-report
description: Weekly Google Ads performance report with Toffu. Use when the user asks for a weekly report, a week-over-week comparison, or how last week went. Compares the last 7 days with the 7 days before and highlights the best and worst campaigns and changes over 20%.
---

# Google Ads weekly report

Use the Toffu tools only. This skill changes nothing.

## Steps

1. Call `get_account_context`. If several Google Ads accounts are connected, ask which one. Pass its id as `account_ids` `{"google_ads": "<id>"}` to `query_campaign_performance`, and as `account_id` to the other tools.
2. Call `query_campaign_performance` for the last 7 full days (end date = yesterday), then for the 7 days before.
3. For the account and for each campaign, compute for both weeks: spend, impressions, clicks, CTR = clicks / impressions, conversions, CPA = spend / conversions, ROAS = conversion_value / spend. When the denominator is 0, show "n/a" (no impressions, no conversions or no spend), never 0 or infinity.
4. Report:
   - Account totals for both weeks, with the change in percent.
   - The 3 best campaigns by ROAS and the 3 worst by CPA (campaigns with spend only).
   - Every campaign whose CPA, ROAS, conversions or spend changed by more than 20%, marked as better or worse. Percent change = (this week - last week) / last week. When last week is 0 or n/a, show "new" instead of a percent.
5. End with at most 3 recommended next steps. If the user wants a change, use the matching `propose_update_campaign` call, show the preview, and call `apply_change` only after the user confirms.

## Rules

- Use the account currency.
- A change on fewer than 10 conversions is noise. Say so instead of calling it a trend.
- Say "no data" when conversion value is missing, and leave ROAS out.
