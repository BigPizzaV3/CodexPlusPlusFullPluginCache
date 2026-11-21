---
name: performance-review
description: Review how ad accounts are performing with Opus Growth - one platform or all connected ones - with exact date ranges, period-over-period comparison, the few numbers that matter for the goal, and a short list of concrete next steps. Use when the user asks how campaigns are doing, for a weekly or monthly review, "what is working", or why results changed.
---

# Performance review

Follow the `opus-growth` skill for dates and reading results. A review answers three questions:
what happened, why, and what to do next. It changes nothing.

## 1. Scope

- `get_connection_status`, then one `account_snapshot` per connected ad platform (it returns every
  campaign with dates, lifetime and recent performance and account totals).
- Period: what the user asked; otherwise the last 30 full days compared with the 30 days before.
  For a "this week" question use the last 7 full days vs the 7 before.
- Know the goal before judging: sales (revenue, ROAS), leads (cost per lead, lead quality),
  calls or messages, traffic, awareness. If the account has no conversion tracking, say that the
  review can judge only traffic and cost (see the `measurement` skill).

## 2. Numbers

Pull them with `get_report` (same arguments for both periods), or the platform's own report for
detail (`google_ads_performance_report`, `meta_campaign_insights`, `tiktok_campaign_report`,
`linkedin_campaign_analytics`, `microsoft_performance_report`, `chatgpt_ads_insights`).

Report per platform, in the account currency:
- spend, conversions (name the conversion type), cost per conversion, conversion value / ROAS when
  tracked
- clicks, CTR, CPC as diagnosis, not as the headline
- change vs the previous period in % and absolute

Never add conversions across platforms as unique customers; each platform claims its own.
If analytics is connected, `marketing_overview` (Google sources) shows the site side.

## 3. Why it changed

Check in this order and stop when the cause is found:
1. **Tracking**: did conversions drop to zero on a day? That is usually a broken tag or a changed
   conversion setting, not performance (`google_ads_conversion_tracking_health`,
   `list_meta_pixels`, `list_tiktok_pixels`).
2. **Changes**: what changed in the account around that date
   (`google_ads_get_change_history`, `meta_change_history`, `tiktok_change_history`).
3. **Delivery**: budget-limited or rank-limited (`google_ads_impression_share_analysis`),
   disapproved ads (`google_ads_list_ad_policy_issues`, `list_meta_ads`), learning restarts,
   ended campaigns, account spending limit reached.
4. **Demand**: seasonality, fewer searches, a competitor (on Google, impression share and CPC
   rising together hint at competition).
5. **Mix**: one campaign growing while another shrinks can move the averages with no real change.

Do not call a campaign a loser while it is still learning, on fewer than about 100 clicks, or on
less spend than roughly three times the target cost per conversion.

## 4. Answer format

1. Two or three lines: the period, total spend, the main result and its change.
2. A short table per platform (campaign, spend, results, cost per result, change).
3. What drove the change, with the evidence.
4. Three concrete next steps, each one a specific request the user can approve (for example
   "add these 6 search terms as negatives in campaign X", "move 20% budget from A to B"). Load
   the `optimize` skill to carry them out.

Keep it short. Long dumps of every metric are not a review.
