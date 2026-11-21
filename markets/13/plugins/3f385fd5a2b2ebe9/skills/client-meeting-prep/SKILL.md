---
name: client-meeting-prep
description: "Prepares a client meeting brief through the Pilot MCP server: results for the period across Google Ads, Meta Ads and Google Analytics 4, what worked and what did not, budget status, concentration risk and the recommendations to discuss, written for an account manager to present. Use when the user asks to prepare a client meeting, a client review or talking points. Triggers: prepare client meeting, client review deck notes, talking points. Déclencheurs : préparer un point client, préparer un rendez-vous client, bilan client, points à aborder."
compatibility: "Requires the Pilot MCP server (https://app.pilot.braike.com/mcp) connected in the client and authorized on the client's workspace."
metadata:
  pilot-mcp-server: "https://app.pilot.braike.com/mcp"
  pilot-mcp-tools: "pilot_data_freshness pilot_cross_platform_overview pilot_budget_pacing pilot_account_concentration google_list_accounts google_get_campaign_performance google_get_recommendations meta_list_accounts meta_get_account_performance_summary google_analytics_run_report"
  pilot-mcp-read-only: "true"
---

# Client meeting prep

Write the brief an account manager reads before a client meeting: the results, the story behind them, and the decisions to ask the client for. Answer in the user's language.

## Requirements

- **Required MCP server:** Pilot MCP (`https://app.pilot.braike.com/mcp`), authorized on the client's workspace.
- **Optional MCP servers:** a file storage server to save the brief, a note-taking server to keep meeting notes, a team messaging server to share it with the team. None is needed.
- **Read-only:** never change anything in the accounts. Recommendations are for the meeting.

## Tools

- `pilot_data_freshness`: whether the figures are complete.
- `pilot_cross_platform_overview`: consolidated spend and results.
- `pilot_budget_pacing`: budget status.
- `pilot_account_concentration`: how many campaigns carry most of the spend.
- `google_list_accounts`: the Google Ads accounts of the client.
- `google_get_campaign_performance`: Google Ads campaigns over the period.
- `google_get_recommendations`: Google's recommendations to discuss.
- `meta_list_accounts`: the Meta ad accounts of the client.
- `meta_get_account_performance_summary`: Meta account KPIs.
- `google_analytics_run_report`: site traffic and key events by channel.

## Steps

1. Ask for the period if the user did not give one; by default, the last full month.
2. Call `pilot_data_freshness`, then `pilot_cross_platform_overview` over the period.
3. Google Ads: `google_list_accounts`, `google_get_campaign_performance` with `start_date` and `end_date`, and `google_get_recommendations`.
4. Meta Ads: `meta_list_accounts`, then `meta_get_account_performance_summary` with the matching preset (for example `last_month`).
5. GA4, if attached: `google_analytics_run_report` by `sessionDefaultChannelGroup` with `sessions` and `keyEvents`.
6. Call `pilot_budget_pacing` and `pilot_account_concentration` for the risks to raise.
7. Write the brief in plain language for a client, with the numbers that support each point.

## Output

1. **The period in three lines**: spend, results and the trend.
2. **What worked**: two or three points with figures.
3. **What did not**: two or three points with figures and the reason when known.
4. **Budget and risks**: pacing, concentration, anything fragile.
5. **To decide with the client**: the recommendations, each with its expected effect.
6. **Likely questions**: questions the client may ask, with short answers.

## Rules

- Write for a client: no tool names, no jargon without a short explanation.
- State the period and the currency.
- Keep Google's recommendations apart from your own, and present them as suggestions.

## Examples

- "Prepare my meeting with the client tomorrow, last month's results."
- "Prépare le point client de jeudi : résultats d'octobre et recommandations."
- "Quels sont les points à aborder avec ce client sur le mois dernier ?"
