---
name: google-ads-account-audit
description: "Audits a Google Ads account in read-only mode through the Pilot MCP server: structure, spend without conversions, search terms, bidding, conversion tracking, ad strength, recommendations and recent changes, then returns a prioritized findings report. Use when the user asks to audit, review or health-check a Google Ads account. Triggers: audit Google Ads, review my Google Ads account, account health check. Déclencheurs : audit Google Ads, auditer un compte Google Ads, bilan de santé du compte, revue de compte Google Ads."
compatibility: "Requires the Pilot MCP server (https://app.pilot.braike.com/mcp) connected in the client and authorized on a workspace with a Google Ads account attached."
metadata:
  pilot-mcp-server: "https://app.pilot.braike.com/mcp"
  pilot-mcp-tools: "google_list_accounts google_get_account_summary google_list_campaigns google_get_campaign_performance google_list_bidding_strategies google_get_search_terms_report google_get_keyword_performance google_list_conversion_actions_detailed google_get_ad_strength google_get_recommendations google_get_optimization_score google_get_change_history pilot_diagnose_wasted_spend pilot_account_concentration pilot_data_freshness"
  pilot-mcp-read-only: "true"
---

# Google Ads account audit

Audit one Google Ads account and hand back a short, prioritized list of findings, each backed by numbers from the account. Answer in the user's language.

## Requirements

- **Required MCP server:** Pilot MCP (`https://app.pilot.braike.com/mcp`), authorized on the workspace that holds the account.
- **Optional MCP servers:** a file storage server to save the report, a team messaging server to share it, a note-taking server to keep the findings. None is needed to run the audit.
- **Read-only:** never call a tool that creates, updates, pauses or deletes anything, on Pilot or on any other server. Every recommendation is written for a person to apply.

## Tools

- `google_list_accounts`: the accounts attached to the workspace, with their IDs.
- `google_get_account_summary`: account totals for the period.
- `google_list_campaigns`: campaigns, status, channel type and budget.
- `google_get_campaign_performance`: cost, clicks, conversions and value per campaign.
- `google_list_bidding_strategies`: portfolio bidding strategies and their targets.
- `google_get_search_terms_report`: the queries that triggered the ads.
- `google_get_keyword_performance`: keyword metrics.
- `google_list_conversion_actions_detailed`: conversion actions, counting, attribution and status.
- `google_get_ad_strength`: ad strength of responsive search ads.
- `google_get_recommendations`: Google's own recommendations.
- `google_get_optimization_score`: the account optimization score.
- `google_get_change_history`: recent changes, to date any break.
- `pilot_diagnose_wasted_spend`: campaigns that spend without converting, or whose cost per acquisition is far above the account median.
- `pilot_account_concentration`: how many campaigns carry 80% of the spend.
- `pilot_data_freshness`: whether Pilot's collected data is current.

## Steps

1. Call `google_list_accounts`. If several accounts are attached, ask which one to audit, unless the user named it. Use its ID as `customer_id` in every Google Ads call.
2. Call `pilot_data_freshness` with `platform: "google"`. If the data is stale or missing, say so at the top of the report and rely on the live Google Ads tools.
3. Set the period: the last 30 days by default (`date_range: "LAST_30_DAYS"`), or the period the user gave.
4. Read the account: `google_get_account_summary`, `google_list_campaigns`, `google_get_campaign_performance`.
5. Read where money leaks: `pilot_diagnose_wasted_spend` with `platform: "google"`, then `google_get_search_terms_report` and `google_get_keyword_performance` on the campaigns that spend most.
6. Read the setup: `google_list_bidding_strategies`, `google_list_conversion_actions_detailed`, `google_get_ad_strength`.
7. Read the context: `pilot_account_concentration`, `google_get_optimization_score`, `google_get_recommendations`, `google_get_change_history`.
8. Write the report. Rank findings by money at stake. Quote the figure behind each finding, and the period.

## Output

A report with these sections, in the user's language:

1. **Summary**: three lines on the account's state and the top three priorities.
2. **Findings**: a table with the finding, the evidence (figure and period), the estimated stake, and the suggested action.
3. **Tracking**: what the conversion setup counts, and any doubt about it.
4. **Next steps**: the actions to take, in order, for a person to apply in Google Ads.

## Rules

- Never compute a ratio on an empty denominator: write that the value is not available, not zero.
- Do not judge a campaign on fewer conversions than the account usually needs to be stable; say the volume is too low.
- Keep Google's recommendations separate from your own findings, and treat them as suggestions.
- If a tool is refused because an account is not attached, show the list of usable accounts from the message and stop.

## Examples

- "Audit my Google Ads account for the last 30 days."
- "Fais l'audit de mon compte Google Ads, en priorisant ce qui coûte le plus."
- "Quels sont les trois chantiers prioritaires sur le compte Google Ads de la boutique ?"
