---
name: team-performance
description: Show how the Vixiees sales team is performing — leaderboard, activity, and progress against sales goals. Use when the user asks who is performing best, how the team is doing against target, or for a team activity report.
---

# Team performance

## Steps

1. Pick the playbook with `list_playbooks_tool` (ask if there are several and the user didn't name one).
2. Call `get_dashboard_leaderboard_tool` for the team ranking over the requested period (default `last_7_days`).
3. If the user asks about one agent, resolve them with `list_users_tool` and call `get_sales_dashboard_performance_tool` with their `user_id` for won, conversion rate, tasks and contacted. This tool covers one agent per call — don't loop it over the whole team.
4. If the user asks about targets, call `get_sales_dashboard_sales_goals_tool` with `start_date` and `end_date` (both required, ISO 8601) matching the period.
5. Use `list_teams_tool` only to resolve team names the user mentions.

## Output

- A compact table from the leaderboard: agent and results, plus goal progress when requested.
- One or two sentences on what stands out, e.g. an agent with high activity but few results, or a team behind its goal pace.
- Answer in the language the user wrote in.

## Rules

- Tasks are assigned automatically by Vixiees. Never suggest reassigning tasks or contacts between agents.
- Speed of first response to new leads matters most. Highlight it when the data shows it.
- Report what the data shows. Don't speculate about individual people's motives.
