---
name: campaign-health
description: Daily Google Ads health check with Toffu. Use when the user asks if anything is broken, why a campaign stopped, or for a status check. Finds campaigns that are enabled but do not serve, campaigns with no impressions yesterday, budget-limited campaigns and sudden conversion drops.
---

# Google Ads campaign health

Use the Toffu tools only. Never apply a change the user has not confirmed.

## Steps

1. Call `get_account_context`. If several Google Ads accounts are connected, ask which one. Pass its id as `account_ids` `{"google_ads": "<id>"}` to `query_campaign_performance`, and as `account_id` to the other tools.
2. Call `list_campaigns` for status, serving status, channel type and daily budget (`campaignBudget.amountMicros` / 1,000,000).
3. Call `query_campaign_performance` with `time_increment` "1" for the last 8 full days (end date = yesterday).
4. Flag these problems, worst first:
   - **Not serving:** status ENABLED, but the serving status is not SERVING (for example ENDED, SUSPENDED, PENDING).
   - **No impressions:** status ENABLED and SERVING, with 0 impressions yesterday but impressions in the 7 days before.
   - **Budget-limited:** status ENABLED, and yesterday's spend is 90% or more of the daily budget.
   - **Underused budget:** status ENABLED, and the 7-day average daily spend is below 70% of the daily budget.
   - **Conversion drop:** yesterday's conversions are more than 30% below the daily average of the 7 days before, while spend is flat or up. Tell the user to check conversion tracking, because a drop with steady clicks often means a tracking problem.
5. Call `list_ads` and list ads with status PAUSED in the campaigns that have a problem, so the user sees what is stopped.
6. Report each problem with its campaign, the numbers and one fix. If there is no problem, say that all enabled campaigns serve.
7. For a fix the user wants (enable, pause, new daily budget), use `propose_update_campaign`. Show the preview, and call `apply_change` only after the user confirms.

## Rules

- This check uses daily data up to yesterday. It cannot see hourly spend or today.
- It cannot see ad disapprovals or policy reasons. Tell the user to check them in Google Ads when a campaign does not serve.
