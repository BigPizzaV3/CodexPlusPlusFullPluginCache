---
name: omneky-channel-connect
description: >-
  Connect Meta, Google, TikTok, LinkedIn, Reddit, Pinterest, or X ad
  accounts for a brand via OAuth URL and link_ad_channel_account. Keywords:
  connect ads, link ad account, Facebook page, channel OAuth, Pinterest,
  twitter, TikTok ads connect.
---

# Connect ad channels

## Activation analytics

If the host exposes a skill-activation / analytics hook, call it once per new user request with this skill name; otherwise skip silently. Never invent a tracking tool. Omneky MCP does **not** expose `track_skill_activation`.

## Purpose

Focused paid-media channel attachment (OAuth URL → authorized accounts →
link). Prefer `omneky-self-connect` when OpenAI Ads / PostHog / Drive are
also in scope.

## When to use

- User asks to connect Meta / Google / TikTok / LinkedIn / Reddit /
  Pinterest / X Ads only
- Launch blocked by disconnected channel

## When not to use

- OpenAI Ads / PostHog / Drive → `omneky-self-connect`
- HubSpot / Semrush / Ahrefs / GSC connect (not on this surface)
- Launch / pause / budget mutations → launch-manage / pause-budget skills

## OpenAI runtime contract

- Use only tools from the current OpenAI host + Omneky MCP (`https://mcp.omneky.com/mcp`). Never invent tools.
- Prefer native ChatGPT / host widgets and question UI for decisions. Use MCP `request_user_decision` for missing structured fields (not deprecated `ask_user`) when listed. Else follow `omneky-failure-modes` § Approval / plain-chat fallback.
- When intake is incomplete, ask **one** concise chat question. Never invent a question tool.
- Approval / Generate turns: end the turn after Approve / Deny (or Generate / Cancel) via host UI or plain chat; mutate only after affirmative Approve / Generate. Never invent a fake widget tool.
- Never invent tokens; OAuth is host-managed. Never ask the user to paste a JWT or API key into chat.

## Non-negotiable output / safety contract

- X Ads wire name is `twitter`, never `x`.
- Do not claim connected until status re-check succeeds.
- Never invent API keys for paid-media channels — use
  `get_channel_connect_url` OAuth.

## Staged workflow

### Stage 1 — Brand + status

1. Resolve brand (`list_brands` / picker) if needed.
2. `get_channel_connection_status` (and `get_pinterest_connection_status`
   when Pinterest). Optional snapshot: `list_connector_statuses`.

### Stage 2 — OAuth

1. `get_channel_connect_url` for the channel.
2. Hand URL to user; end turn while they complete browser OAuth.

### Stage 3 — Link

1. `list_authorized_ad_accounts`.
2. Meta: also `list_authorized_facebook_pages` when needed.
3. Confirm selection → `link_ad_channel_account`.
4. Re-check status.

### Stage 4 — Next

Offer launch via `omneky-launch-manage` (paused by default) or Meta path
`omneky-meta-launch`.

## Failure boundaries

| Failure | Required response |
| --- | --- |
| Still disconnected after OAuth | Re-check once; ask user to retry OAuth; do not invent tokens. |
| Wrong wire name `x` | Use `twitter`. |
| Multiple accounts | Confirm before `link_ad_channel_account`. |
| Non–paid-media connector | Hand off to `omneky-self-connect` or analytics (reads-only). |
