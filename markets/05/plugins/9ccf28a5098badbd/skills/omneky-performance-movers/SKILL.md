---
name: omneky-performance-movers
description: >-
  Find which ads to make more of: performance movers, ROAS/CTR leaders, and
  creative recommendations. Keywords: which ads, ROAS, CTR, movers,
  recommendations, leaderboard, what rose, what fell, make more of.
---

# Performance movers

## Activation analytics

If the host exposes a skill-activation / analytics hook, call it once per new user request with this skill name; otherwise skip silently. Never invent a tracking tool. Omneky MCP does **not** expose `track_skill_activation`.

## Purpose

Fast read-only path for “what rose / fell?” and “which creatives should I
make more of?” grounded in movers + recommendations + optional drill-downs.

## When to use

- Which ads / campaigns / creatives improved or declined vs the prior period
- Leaderboard / “what should I scale?” questions
- Follow-on from a thin analytics ask that is clearly mover-centric

## When not to use

- Full multi-connector / GSC / HubSpot deep dives → `omneky-analytics`
- Mutations (pause / budget / launch) → launch-manage / pause-budget
- Inventing causal “lift” scores without tool support

## OpenAI runtime contract

- Use only tools from the current OpenAI host + Omneky MCP (`https://mcp.omneky.com/mcp`). Never invent tools.
- Prefer native ChatGPT / host widgets and question UI for decisions. Use MCP `request_user_decision` for missing structured fields (not deprecated `ask_user`) when listed. Else follow `omneky-failure-modes` § Approval / plain-chat fallback.
- When intake is incomplete, ask **one** concise chat question. Never invent a question tool.
- Approval / Generate turns: end the turn after Approve / Deny (or Generate / Cancel) via host UI or plain chat; mutate only after affirmative Approve / Generate. Never invent a fake widget tool.
- Never invent tokens; OAuth is host-managed.

## Non-negotiable output / safety contract

- Brand-scoped and read-only.
- Coverage first: `check_reporting_data_available` before treating empty as zero.
- Prefer `get_performance_movers` (not deprecated `get_trending`).
- Prefer `get_performance_breakdown` for ranked drill-down (not deprecated
  `get_dimension_summary`).
- Never invent metrics; never sum `selected_conversion_metric_value` across channels.
- Summarize winners and losers with evidence.

## Staged workflow

### Stage 1 — Brand + coverage

1. Resolve brand (`list_brands` / picker) if needed; `get_current_user` when required.
2. Confirm date window.
3. `check_reporting_data_available`.

### Stage 2 — Movers

1. `get_performance_movers` for up / down vs prior period.
2. Present a short leaderboard (top gains / top drops) with channel labels.

### Stage 3 — Drill / recommend

1. Optional: `get_daily_metrics` for a nominated entity’s trend.
2. Optional: `get_performance_breakdown` for creative / campaign ranks.
3. Optional: `search_reporting_values` to resolve names → ids.
4. When they ask what to change or test next: `get_recommendations`
   (tight window; timeout → narrow, no identical retry).

### Stage 4 — Hand off

- “Make more like winner X” → `omneky-creative` / `omneky-image-ads` /
  `omneky-product-video`
- “Pause the losers” → `omneky-pause-budget` (Approve before mutate)
- Broader reporting → `omneky-analytics`

## Failure boundaries

| Failure | Required response |
| --- | --- |
| Empty movers | Coverage check; explain gap; do not invent ranks. |
| Recommendations timeout | Narrow window; stop identical retry. |
| Cross-channel conversion sum | Refuse; channel-group. |
| User requests pause mid-read | Hand off; Approve widget required. |
