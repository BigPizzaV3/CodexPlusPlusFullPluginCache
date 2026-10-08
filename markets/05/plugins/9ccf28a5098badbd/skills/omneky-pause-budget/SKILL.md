---
name: omneky-pause-budget
description: >-
  Pause or enable ads and change budgets on connected channels after user
  confirmation. Keywords: pause ad, enable ad, resume ad, change budget,
  set budget, set_ad_entity_status, set_ad_budget, prefer pause over delete.
---

# Pause and budget

## Activation analytics

If the host exposes a skill-activation / analytics hook, call it once per new user request with this skill name; otherwise skip silently. Never invent a tracking tool. Omneky MCP does **not** expose `track_skill_activation`.

## Purpose

Safe mutations for status and budget on live entities. Pause-first culture;
never delete from this skill unless the user explicitly insisted and completed
dual confirm (prefer redirecting deletes through `omneky-launch-manage`).

## When to use

- Pause / enable / resume campaign, ad set, or ad
- Change daily or lifetime budget on Meta / Google (and channel-supported sets)
- Pinterest status via `set_pinterest_entity_status`

## When not to use

- Creating new campaigns → `omneky-launch-manage` / `omneky-meta-launch`
- Reporting-only → `omneky-analytics`
- Creative generation → `omneky-creative`

## OpenAI runtime contract

- Use only tools from the current OpenAI host + Omneky MCP (`https://mcp.omneky.com/mcp`). Never invent tools.
- Prefer native ChatGPT / host widgets and question UI for decisions. Use MCP `request_user_decision` for missing structured fields (not deprecated `ask_user`) when listed. Else `omneky-failure-modes` § Approval / plain-chat fallback.
- When intake is incomplete, ask **one** concise chat question. Never invent a question tool.
- Approval turns: end the turn after Approve / Deny (host UI or plain chat); mutate only next turn after Approve. Never invent a fake widget tool.
- Never invent tokens; OAuth is host-managed.

## Non-negotiable output / safety contract

- Confirm brand, entity (campaign / ad set / ad ids), channel, and action
  with Approve / Deny before writes (host UI or plain-chat summary —
  `omneky-failure-modes` § Approval / plain-chat fallback). End turn after
  showing the choice.
- Prefer `set_ad_entity_status` (not deprecated `set_ad_status`).
- Prefer **pause** over **delete**. If user asks to delete, offer pause
  first; dual confirm before `delete_*` (or hand off to launch-manage).
- Facebook CBO vs ABO: accepted budget level depends on campaign
  configuration — do not invent hierarchy overrides.
- X Ads: `channel="twitter"`.
- Unscoped entity lists can time out — pass `campaign_id` into
  `get_ad_groups` when inspecting.

## Staged workflow

### Stage 1 — Resolve entities

1. Brand: `list_brands` / picker if needed.
2. `get_channel_connection_status`.
3. Inspect: `get_campaigns` → `get_ad_groups(campaign_id=…)` → `get_ads`.
   Pinterest helpers: `get_pinterest_campaigns` /
   `get_pinterest_ad_groups` / `get_pinterest_ads`.
4. Optional name resolve: `get_campaign_ad_group_names` /
   `search_reporting_values`.

### Stage 2 — Budget context

1. `get_channel_budget` / `minimum_budget_for_objective` before raising spend.
2. Confirm currency / daily vs lifetime with the user when ambiguous.

### Stage 3 — Approve

1. One-card summary: Brand · Channel · Entity · Action (Pause|Enable|Budget) ·
   Amount — host UI when available; else plain chat with Approve / Deny /
   Edit.
2. End turn.

### Stage 4 — Mutate (next turn)

1. Status: `set_ad_entity_status` (Pinterest: `set_pinterest_entity_status`).
2. Budget: `set_ad_budget`.
3. Meta retarget only when asked: `update_ad_targeting` (Facebook-only).

### Stage 5 — Verify

1. Re-read entity via `get_ads` / `get_ad_groups` / `get_campaigns` as needed.
2. Offer metrics via `omneky-analytics` / `omneky-performance-movers`.

## Failure boundaries

| Failure | Required response |
| --- | --- |
| Write without Approve | Forbidden — host UI or plain-chat summary first. |
| Invented approval widget tool | Forbidden — `omneky-failure-modes` § Approval / plain-chat fallback. |
| Delete-first request | Offer pause; dual confirm or hand off. |
| Timeout listing ad groups | Scope with `campaign_id`. |
| Budget below minimum | Show `minimum_budget_for_objective`; do not submit invalid. |
| Wrong channel wire `x` | Use `twitter`. |
| Disconnected channel | Self-connect before mutate. |
