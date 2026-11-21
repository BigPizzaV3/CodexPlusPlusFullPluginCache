---
name: budget-pacing-check
description: "Checks advertising budgets and spend pacing through the Pilot MCP server: campaigns capped by their budget, budgets left idle, spend so far this month, daily spend trends and the projected effect of a budget change, across Google Ads and Meta Ads. Use when the user asks whether the budget is on track, overspending or underspending. Triggers: budget pacing, are we on budget, monthly spend check. Déclencheurs : rythme du budget, suivi du budget, dépense du mois, budget plafonné, budget sous-utilisé."
compatibility: "Requires the Pilot MCP server (https://app.pilot.braike.com/mcp) connected in the client and authorized on a workspace with Google Ads or Meta Ads attached."
metadata:
  pilot-mcp-server: "https://app.pilot.braike.com/mcp"
  pilot-mcp-tools: "pilot_budget_pacing pilot_cross_platform_overview google_list_accounts google_get_account_budget_summary google_get_account_spend_today google_list_budgets google_simulate_budget_change meta_list_accounts meta_get_daily_spend_breakdown meta_get_minimum_budgets"
  pilot-mcp-read-only: "true"
---

# Budget pacing check

Tell the user whether spend is on track for the month, where budgets cap delivery and where they sit idle. Answer in the user's language.

## Requirements

- **Required MCP server:** Pilot MCP (`https://app.pilot.braike.com/mcp`), authorized on the workspace concerned.
- **Optional MCP servers:** a team messaging server to send the check, a spreadsheet or file storage server to keep a pacing log. None is needed.
- **Read-only:** never change a budget. Proposed changes are for a person to apply.

## Tools

- `pilot_budget_pacing`: capped, idle and undetermined budgets, with the reason.
- `pilot_cross_platform_overview`: spend so far across platforms.
- `google_list_accounts`: the Google Ads accounts attached to the workspace.
- `google_get_account_budget_summary`: account-level budget and spending limits.
- `google_get_account_spend_today`: spend today, in micros (divide by 1,000,000).
- `google_list_budgets`: campaign budgets and their amounts.
- `google_simulate_budget_change`: projected clicks, cost and conversions at other budget levels for one campaign.
- `meta_list_accounts`: the Meta ad accounts attached to the workspace.
- `meta_get_daily_spend_breakdown`: daily Meta spend.
- `meta_get_minimum_budgets`: Meta's minimum daily budgets.

## Steps

1. Ask for the monthly target if the user has one; otherwise judge pacing against the budgets set in the platforms.
2. Call `pilot_budget_pacing` (default window) to list capped, idle and undetermined budgets. Keep undetermined budgets apart: an unknown budget is not a zero budget.
3. Call `pilot_cross_platform_overview` with the number of days elapsed this month to get spend so far.
4. Google Ads: `google_list_accounts`, then `google_get_account_budget_summary`, `google_list_budgets` and `google_get_account_spend_today`. For a capped campaign that converts well, call `google_simulate_budget_change` to show what more budget would bring.
5. Meta Ads: `meta_list_accounts`, then `meta_get_daily_spend_breakdown` with `date_preset: "this_month"`, and `meta_get_minimum_budgets` when a budget looks too low to deliver.
6. Project month-end spend from the daily average of the days elapsed, and compare it with the target.

## Output

1. **Verdict**: on track, ahead or behind, with spend so far, projected month-end spend and the target.
2. **Capped budgets**: campaigns limited by budget, with their results and, when available, the simulated gain.
3. **Idle budgets**: budgets that are not spent, and why.
4. **Proposed moves**: budget shifts for a person to apply, with the expected effect.

## Rules

- Say which days the projection uses and which currency each amount is in.
- Never sum amounts in different currencies.
- Simulations are Google's estimates: present them as such.

## Examples

- "Are we on track with this month's budget?"
- "Quelles campagnes sont plafonnées par leur budget, et lesquelles dorment ?"
- "Mon budget Meta du mois est-il bien rythmé ?"
