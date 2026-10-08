---
name: omneky-meta-launch
description: >-
  Prepare and launch Meta/Facebook/Instagram ads (sales, traffic, leads,
  awareness, video views) after user confirmation. Keywords: Meta launch,
  Facebook ads, Instagram ads, launch campaign, PAUSED, sales, leads,
  ThruPlay, lead_gen_form_id.
---

# Meta launch

## Activation analytics

If the host exposes a skill-activation / analytics hook, call it once per new user request with this skill name; otherwise skip silently. Never invent a tracking tool. Omneky MCP does **not** expose `track_skill_activation`.

## Purpose

Meta-first launch path using `launch_facebook_*` tools. Same Approve-before-
mutate and paused-default rules as `omneky-launch-manage`, narrowed to
Facebook / Instagram.

## When to use

- User wants Meta / Facebook / Instagram paid launch
- Sales / conversions, traffic, leads, awareness, or video views objectives

## When not to use

- Google / TikTok / LinkedIn / Reddit / Pinterest / X → `omneky-launch-manage`
- Creative generation → `omneky-creative` first
- Analytics-only → `omneky-analytics`

## OpenAI runtime contract

- Use only tools from the current OpenAI host + Omneky MCP (`https://mcp.omneky.com/mcp`). Never invent tools.
- Prefer native ChatGPT / host widgets and question UI for decisions. Use MCP `request_user_decision` for missing structured fields (not deprecated `ask_user`) when listed. Else `omneky-failure-modes` § Approval / plain-chat fallback.
- When intake is incomplete, ask **one** concise chat question. Never invent a question tool.
- Approval turns: end the turn after Approve / Deny / Edit (host UI or plain chat); mutate only next turn after Approve. Never invent a fake summary-widget tool.
- Never invent tokens; OAuth is host-managed.

## Non-negotiable output / safety contract

- Confirm brand, creative, objective, budget, targeting, CTA, landing URL.
- Approve / Deny / Edit one-card summary **before** any `launch_facebook_*`
  (host-native confirmation / MCP Apps / `request_user_decision` when
  available; else plain-chat fallback — `omneky-failure-modes` § Approval /
  plain-chat fallback). End turn; launch only next turn after affirmative
  Approve.
- Default paused / disabled unless user clearly asks to go live.
- Prefer pause over delete (`omneky-pause-budget` /
  `set_ad_entity_status`).
- If a preflight / validate tool appears on this session’s `tools/list`, use
  it before create — never invent a preflight tool name that is absent.
- Facebook lead ads: set `lead_gen_form_id` on ad specs for native forms.
- Inline targeting example shape: countries + age_min / age_max — do not
  invent unsupported facets.
- No `launch_openai_*` / managed-Meta launch names on public `/mcp`.

## Staged workflow

### Stage 1 — Brand + connection

1. `list_brands` / picker / `get_brand_details`.
2. `get_channel_connection_status` for Facebook. If disconnected →
   `omneky-self-connect` (`get_channel_connect_url` →
   `list_authorized_ad_accounts` / `list_authorized_facebook_pages` →
   `link_ad_channel_account`).
3. `get_channel_budget` / `minimum_budget_for_objective`.

### Stage 2 — Creative + catalogue

1. Product: `list_brand_products` / `get_product_details` when relevant.
2. Generate if needed via `omneky-creative` (credits first).
3. `register_creative_for_launch` when attaching a chat creative.

### Stage 3 — Objective + specs

1. Map user intent → tool:
   - Sales / purchases / ROAS → `launch_facebook_sales_ad`
   - Leads → `launch_facebook_leads_ad` (+ `lead_gen_form_id` when native form)
   - Traffic → `launch_facebook_traffic_ad`
   - Awareness / reach → `launch_facebook_awareness_ad`
   - Video views / ThruPlay → `launch_facebook_video_views_ad`
2. New vs existing: `campaign_spec={"id": …}` / `ad_group_spec={"id": …}`
   when extending.
3. Optional `get_ad_custom_properties` / `reach_estimate`.

### Stage 4 — Approve then launch

1. Summary Approve / Deny / Edit (host UI or plain chat); end turn.
2. After Approve: call the chosen `launch_facebook_*` with paused default.
3. Post-launch next steps → status / 7d metrics (`omneky-analytics`) / Done.

### Stage 5 — Manage after

Pause / budget / retarget via `omneky-pause-budget` or
`set_ad_entity_status` / `set_ad_budget` / `update_ad_targeting`
(Facebook-only targeting updates) after Approve.

## Failure boundaries

| Failure | Required response |
| --- | --- |
| Launch without Approve | Forbidden. |
| Invented summary-widget tool | Forbidden — plain-chat fallback OK. |
| Disconnected Meta | Self-connect; re-check status. |
| Missing countries / targeting | Ask once / `request_user_decision`; do not guess. |
| Lead form missing when required | Ask for `lead_gen_form_id` or switch objective. |
| Invented preflight tool | Skip if not on `tools/list`. |
| User wants ACTIVE casually | Confirm explicitly; still prefer stating spend risk. |
| `needs_user_decision` | `request_user_decision` if listed; else plain chat; no JSON dump; no auto-retry. |
