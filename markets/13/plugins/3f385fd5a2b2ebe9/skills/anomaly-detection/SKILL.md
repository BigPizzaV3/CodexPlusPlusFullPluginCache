---
name: anomaly-detection
description: "Scans the ad accounts of a workspace for anomalies through the Pilot MCP server: data gaps, spend spikes or drops, campaigns spending without results, budgets capped or idle, account issues and sudden changes in site traffic, and returns a short alert list ranked by urgency. Use when the user asks if anything looks wrong, for a daily check, or for alerts. Triggers: anomaly detection, anything unusual, daily check, alerts. Déclencheurs : détection d'anomalies, quelque chose d'anormal, contrôle du jour, alertes, vérification quotidienne."
compatibility: "Requires the Pilot MCP server (https://app.pilot.braike.com/mcp) connected in the client and authorized on a workspace with at least one ad platform attached."
metadata:
  pilot-mcp-server: "https://app.pilot.braike.com/mcp"
  pilot-mcp-tools: "pilot_data_freshness pilot_diagnose_wasted_spend pilot_budget_pacing google_list_accounts google_get_campaign_performance google_get_account_spend_today meta_list_accounts meta_get_daily_spend_breakdown meta_check_account_issues google_analytics_run_report"
  pilot-mcp-read-only: "true"
---

# Anomaly detection

Run a quick check of the workspace and return only what looks wrong, ranked by urgency. If nothing is wrong, say so in one line. Answer in the user's language.

## Requirements

- **Required MCP server:** Pilot MCP (`https://app.pilot.braike.com/mcp`), authorized on the workspace to check.
- **Optional MCP servers:** a team messaging server to post the alerts, a note-taking server to log them. None is needed.
- **Read-only:** never pause a campaign or change a budget, even for an urgent alert. Alerts are for a person to act on.

## Tools

- `pilot_data_freshness`: collection gaps, and accounts that stopped delivering.
- `pilot_diagnose_wasted_spend`: spend without conversions and outlier costs per acquisition.
- `pilot_budget_pacing`: capped and idle budgets.
- `google_list_accounts`: the Google Ads accounts attached to the workspace.
- `google_get_campaign_performance`: recent Google Ads results, day by day when needed.
- `google_get_account_spend_today`: spend today, in micros (divide by 1,000,000).
- `meta_list_accounts`: the Meta ad accounts attached to the workspace.
- `meta_get_daily_spend_breakdown`: daily Meta spend.
- `meta_check_account_issues`: Meta account limits, rejections and restrictions.
- `google_analytics_run_report`: daily sessions and key events, to catch a site or tracking break.

## Steps

1. Call `pilot_data_freshness`. A collection gap or an account that stopped delivering is the first alert.
2. Call `pilot_diagnose_wasted_spend` with `days: 7` and `pilot_budget_pacing` with `days: 7`.
3. Google Ads: `google_list_accounts`, then `google_get_account_spend_today` and `google_get_campaign_performance` on the last 7 days against the 7 before (`start_date`, `end_date`).
4. Meta Ads: `meta_list_accounts`, then `meta_get_daily_spend_breakdown` with `date_preset: "last_14d"` and `meta_check_account_issues`.
5. GA4, if attached: `google_analytics_run_report` with `dimensions: ["date"]` and `metrics: ["sessions", "keyEvents"]` over the last 14 days. A day near zero points to tracking.
6. Flag a change only when it is large against the usual day-to-day variation of the account; mention the threshold you used.

## Output

A list of alerts, most urgent first. Each alert gives what happened, where (platform, account, campaign), since when, the figure against its usual level, and the first thing to check. End with "Nothing else unusual" when the rest is normal.

## Rules

- Rule out a data gap before raising a performance alert.
- Never report a weekend or holiday dip as an anomaly without comparing with the same days before.
- Keep the list short: five alerts at most, the rest in one line.

## Examples

- "Anything unusual in my accounts today?"
- "Fais le contrôle quotidien de l'espace et dis-moi seulement ce qui cloche."
- "Y a-t-il une dépense anormale sur Meta cette semaine ?"
