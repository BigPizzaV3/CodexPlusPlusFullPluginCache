---
name: omneky-self-connect
description: >-
  Connect a missing Omneky ad channel or OpenAI Ads / PostHog / Google Drive
  for the signed-in brand. Use when get_channel_connection_status is
  disconnected or the user asks to link an ad account, Facebook Page,
  Pinterest, X Ads (twitter), PostHog, or Drive. Intent keywords: connect
  ads, OAuth URL, link ad account, Facebook page, Pinterest, Twitter, X Ads,
  OpenAI Ads, PostHog, Google Drive, disconnect Drive.
---

# Omneky self-connect

## Activation analytics

If the host exposes a skill-activation / analytics hook, call it once per new user request with this skill name; otherwise skip silently. Never invent a tracking tool. Omneky MCP does **not** expose `track_skill_activation`.

## Purpose

Attach authorized ad accounts and optional brand connectors so later
`launch_*` / asset flows can succeed. Browser OAuth (or one-shot API key
forward for OpenAI Ads / PostHog) is user-completed; this skill never
collects secrets into free chat beyond what the tool schema requires, and
never invents disconnect tools that are not on `tools/list`.

## When to use

- Channel is disconnected and the user wants to launch or manage ads
- User asks to connect Meta / Google / TikTok / LinkedIn / Reddit /
  Pinterest / X Ads (`twitter`), OpenAI Ads, PostHog, or Google Drive
- After `get_channel_connection_status` or `list_connector_statuses` shows
  a gap blocking a requested workflow

## When not to use

- Not HubSpot / Semrush / Ahrefs / GSC **connect** — those are status +
  reads only on this surface (see `omneky-analytics`). Users connect them
  in brand settings.
- Not OpenAI Ads / managed-Meta **launches** — connect ≠ launch. There is
  no `launch_openai_*` / `launch_omneky_managed_*` on public `/mcp`.
- Not Datadog / Shopify / GTM / invented connectors
- Not for pausing / budgeting (→ `omneky-pause-budget`) or launching
  (→ `omneky-launch-manage`)

## OpenAI runtime contract

- Use only tools from the current OpenAI host + Omneky MCP (`https://mcp.omneky.com/mcp`). Never invent tools.
- Prefer native ChatGPT / host widgets and question UI for decisions. Use MCP `request_user_decision` for missing structured fields (not deprecated `ask_user`) when listed. Else follow `omneky-failure-modes` § Approval / plain-chat fallback.
- When intake is incomplete, ask **one** concise chat question. Never invent a question tool.
- Approval / Generate turns: end the turn after Approve / Deny (or Generate / Cancel) via host UI or plain chat; mutate only after affirmative Approve / Generate. Never invent a fake widget tool.
- Never invent tokens; OAuth is host-managed. Never ask the user to paste a JWT or API key into chat.

## Non-negotiable output / safety contract

- Wire name for X Ads is **`twitter`**, never `x`.
- Hand the user the OAuth / connect URL; they finish in the browser. Do not
  claim the channel is connected until a status re-check says so.
- OpenAI Ads / PostHog keys are forwarded **once** by the tool and never
  logged back — do not echo keys into chat.
- Destructive disconnects (`disconnect_posthog`, `disconnect_google_drive`)
  need an Approve widget / explicit confirm; prefer leave-connected unless
  the user asked to disconnect.
- Never invent Pinterest / Twitter disconnect tools if absent from
  `tools/list`.
- After connect, offer next step: launch (`omneky-launch-manage`) or
  verify with a read-only list (`get_campaigns`).

## Staged workflow

### Stage 1 — Resolve brand

1. If `brand_id` unknown: `list_brands` → brand picker → `get_brand_details`.
2. Snapshot: `list_connector_statuses`.

### Stage 2 — Paid-media channel connect (Meta / Google / TikTok / LinkedIn / Reddit / Pinterest / X)

1. `get_channel_connection_status` with the correct `channel`
   (`facebook` / `google` / `tiktok` / `linkedin` / `reddit` /
   `pinterest` / `twitter`). Pinterest also has
   `get_pinterest_connection_status`.
2. If disconnected: `get_channel_connect_url` — show the URL; end turn if
   waiting on the user.
3. After the user says they finished OAuth: `list_authorized_ad_accounts`.
   For Meta also `list_authorized_facebook_pages` when a Page is required.
4. Confirm which account (and Page) to attach via widget / one question.
5. `link_ad_channel_account` with the chosen ids.
6. Re-check `get_channel_connection_status` / `list_connector_statuses`.

### Stage 3 — OpenAI Ads

1. `get_openai_ads_connection_status`.
2. If connecting: `connect_openai_ads` with the user-provided API key
   (schema-required; do not store or reprint).
3. Re-check status. Remind: connect ≠ launch.

### Stage 4 — PostHog

1. `get_posthog_connection_status`.
2. Connect: `connect_posthog` with personal `phx_…` key (not `phc_…`) and
   host `us.posthog.com` or `eu.posthog.com`.
3. Disconnect only on explicit Approve: `disconnect_posthog`.

### Stage 5 — Google Drive

1. `get_google_drive_connection_status`.
2. Connect: `get_google_drive_connect_url` → user OAuth → re-check.
3. Disconnect only on explicit Approve: `disconnect_google_drive`.

### Stage 6 — Hand off

- Ready to launch → `omneky-launch-manage` / `omneky-meta-launch`
- Channel-only questions → `omneky-channel-connect` (thin channel path)
- Failures → `omneky-failure-modes`

## Failure boundaries

| Failure | Required response |
| --- | --- |
| 401 / unauthorized | Host re-OAuth; never paste JWT. |
| OAuth URL opened but status still disconnected | Wait; re-check status once; do not re-link blindly with stale ids. |
| User has multiple authorized accounts | Picker / one question; do not pick silently. |
| Meta missing Page | `list_authorized_facebook_pages` then include page on `link_ad_channel_account`. |
| User said `channel=x` | Correct to `twitter` and proceed. |
| HubSpot/Semrush/Ahrefs/GSC “connect” request | Explain status+read only; point to brand settings; use analytics skill for queries. |
| Disconnect without confirm | Show Approve / Deny; do not call disconnect yet. |
| Invented disconnect / launch tool missing | Refuse; stay on `tools/list` names. |
