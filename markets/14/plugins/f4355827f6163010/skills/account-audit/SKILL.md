---
name: account-audit
description: Audit a Google Ads account with Toffu. Use when the user asks to audit, review or health-check their Google Ads, or asks what to fix or improve. Ranks campaigns by spend and ROAS, flags waste and budget limits, and proposes fixes the user confirms.
---

# Google Ads account audit

Use the Toffu tools only. Never apply a change the user has not confirmed.

## Steps

1. Call `get_account_context`. If several Google Ads accounts are connected, ask which one. Pass its id as `account_ids` `{"google_ads": "<id>"}` to `query_campaign_performance`, and as `account_id` to the other tools.
2. Ask for the target CPA or ROAS, unless the user gave one. Without a target, use the account average.
3. Call `query_campaign_performance` for the last 30 full days (end date = yesterday). Then call it again for the 30 days before, for the trend.
4. Call `list_campaigns` for status, channel type, bidding strategy and daily budget (`campaignBudget.amountMicros` / 1,000,000, in the account currency).
5. For each campaign with spend in either period, compute:
   - ROAS = conversion_value / spend
   - CPA = spend / conversions
   - Share of account spend
   - Average daily spend = spend / 30
   - Change in spend and conversions against the previous 30 days
6. Flag these findings, worst first:
   - **Off target:** CPA above the target CPA, or ROAS below the target ROAS.
   - **No conversions:** 0 conversions, and spend above 2x the account CPA. If the account has no conversions, use spend above 10% of account spend.
   - **Low return:** ROAS below 60% of the account ROAS, with at least 10% of account spend.
   - **Budget-limited winner:** ROAS above the account ROAS, and its average daily spend is 90% or more of its daily budget.
   - **Room to scale:** ROAS 2x the account ROAS or more, with average daily spend below 80% of its daily budget.
   - **Sharp drop:** conversions down 30% or more, with spend flat or up.
   - **Paused winner:** a paused campaign that had ROAS above the account ROAS in the previous period.
7. Report:
   - Account totals: spend, conversions, conversion value, ROAS, CPA, against the previous period.
   - One table: campaign, status, spend, conversions, ROAS, CPA, finding.
   - At most 3 recommended actions, each with the numbers that support it.
8. Offer each action as a change. Use `propose_update_campaign` (`status`, `daily_budget` in account currency, `target_roas`, `target_cpa`). Show the preview. Call `apply_change` only after the user confirms that change.

## Rules

- Use the account currency. Never add totals in different currencies.
- Say "no data" when a metric is missing. Never estimate it.
- Do not recommend a change from fewer than 7 days of data or fewer than 10 conversions without saying that the sample is small.
