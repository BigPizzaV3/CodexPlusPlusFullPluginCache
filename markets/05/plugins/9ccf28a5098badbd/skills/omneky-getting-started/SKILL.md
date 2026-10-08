---
name: omneky-getting-started
description: >-
  Start any Omneky ChatGPT plugin session: host OAuth, health_check,
  get_current_user, list_brands / brand picker, get_brand_details, and
  list_connector_statuses. Use when the user is new, auth failed, brand_id
  is unknown, or they ask what Omneky can do. Intent keywords: sign in,
  OAuth, who am I, list brands, brand picker, connector status, getting
  started, first run, reconnect, capability summary.
---

# Omneky — getting started

## Activation analytics

If the host exposes a skill-activation / analytics hook, call it once per new user request with this skill name; otherwise skip silently. Never invent a tracking tool. Omneky MCP does **not** expose `track_skill_activation`.

## Purpose

Bootstrap a signed-in Omneky session before brand-scoped analytics, catalogue,
creative, or launch work. Prove the connector is up, resolve identity and
`brand_id`, summarize connected channels, and route to the right sibling
skill — without inventing keys, charging credits, or launching spend.

Omneky helps with paid-media on Meta/Facebook, Google (Performance Max and
Demand Gen), TikTok, LinkedIn, Reddit, Pinterest, and X Ads (`twitter`):
catalogue, image/video creatives, paused-by-default launches, and ROAS/CTR
reporting.

## When to use

- First turn on a new host / plugin session
- Auth / JWT / 401 errors (re-run host OAuth)
- Need `user_id`, `brand_id`, company context, or a capability snapshot
- User asks “what can Omneky do?” or “which brands do I have?”

## When not to use

- ROAS / CTR reporting → `omneky-analytics` / `omneky-performance-movers`
- Launches, pause, budget, delete → `omneky-launch-manage` /
  `omneky-meta-launch` / `omneky-pause-budget`
- Image/video generation → `omneky-creative` / `omneky-image-ads` /
  `omneky-product-video`
- Catalogue writes → `omneky-catalogue` / `omneky-product-import`
- Plan upgrade / Stripe portal as the primary goal → `omneky-billing`
- Do not treat `health_check` as a data source — reachability only

## OpenAI runtime contract

- Use only tools from the current OpenAI host + Omneky MCP (`https://mcp.omneky.com/mcp`). Never invent tools.
- Prefer native ChatGPT / host widgets and question UI for decisions. Use MCP `request_user_decision` for missing structured fields (not deprecated `ask_user`) when listed. Else follow `omneky-failure-modes` § Approval / plain-chat fallback.
- When intake is incomplete, ask **one** concise chat question. Never invent a question tool.
- Approval / Generate turns: end the turn after Approve / Deny (or Generate / Cancel) via host UI or plain chat; mutate only after affirmative Approve / Generate. Never invent a fake widget tool.
- Never invent tokens; OAuth is host-managed.

## Non-negotiable output / safety contract

- Never ask the user to paste a JWT, Nexus token, or API key into chat.
- Prefer a **brand-picker** host widget when multiple brands exist (≤3 options
  + custom when the host allows). Confirm before guessing `brand_id`.
- Prefer a **numeric** `brand_id` when thumbnails / catalogue imagery matter.
- Do not launch, delete, pause, enable, change budget, or submit paid
  generation from this skill — hand off with a clear next skill name.
- Safety defaults to mention when orienting: launches paused by default;
  pause > delete; credit callout before paid gen (image ~5 / video ~30);
  never invent metrics; `check_reporting_data_available` before empty=zero.
- ChatGPT-safe: omit Cursor-only / Grok-Bot-only avatar / profile-picture
  steps unless the host explicitly supports avatar update; if unsupported,
  skip silently.
- Cross-link siblings by name. Recovery detail → `omneky-failure-modes`.

## Staged workflow

### Stage 1 — Session / auth

1. If the host has no Omneky login, tell the user to complete the plugin
   connector OAuth for Omneky. On JWT / 401 / unauthorized, ask them to
   re-OAuth in the host. Never paste a token.
2. Optionally call `health_check` when diagnosing connect failures. Skip on
   every happy-path turn.

### Stage 2 — Identity

1. Call `get_current_user`. Capture `user_id` (needed later for movers / some
   creative args). Do not ask the user for a numeric user id.
2. If company context is needed: `get_company` (identity / plan fields only —
   not prepaid credit snapshot).

### Stage 3 — Brand resolution

1. Call `list_brands`.
2. If more than one brand: present a brand-picker widget or one concise chat
   question. Wait for the choice. End the turn after the widget when the host
   requires exclusive-tool turns.
3. Call `get_brand` and/or `get_brand_details` for the chosen id (logo,
   colors, copy, `company_id`, creative assets).

### Stage 4 — Connector snapshot

1. Call `list_connector_statuses` for paid-media channels (including
   `pinterest` / `twitter`) plus HubSpot, Ahrefs, GSC, OpenAI Ads, PostHog,
   Drive.
2. Semrush is **not** in that fanout — if the user cares about Semrush, call
   `get_semrush_connection_status` directly (see `omneky-analytics`).
3. Disconnected ad channel the user wants to use → `omneky-self-connect` /
   `omneky-channel-connect` (`get_channel_connect_url` /
   `link_ad_channel_account`).

### Stage 5 — Orient and hand off

Summarize in one short beat what is ready (brand, connected channels) and
offer next asks:

| User intent | Skill |
| --- | --- |
| Performance / ROAS | `omneky-analytics` / `omneky-performance-movers` |
| Catalogue / import URL | `omneky-catalogue` / `omneky-product-import` |
| Image / video creatives | `omneky-creative` (+ `omneky-credit-balance`) |
| Launch / pause | `omneky-launch-manage` (paused by default) |
| Meta-only launch | `omneky-meta-launch` |
| Plan / credits | `omneky-billing` / `omneky-credit-balance` |
| Something failed | `omneky-failure-modes` |

Example next asks to offer:

- “Show ROAS by creative last 7 days”
- “Import this product URL into the catalogue”
- “Generate a 1:1 Meta image ad for [product]”
- “Prepare a paused Meta sales launch for [brand]”

Support: support@omneky.com · Privacy: https://www.omneky.com/privacy-policy

## Failure boundaries

| Failure | Required response |
| --- | --- |
| 401 / unauthorized / invalid token | Re-run **host** Omneky OAuth. Never ask for a pasted JWT. |
| `health_check` fails / unreachable | Tell user the connector is down; retry later; do not invent alternate endpoints. |
| `list_brands` empty | Explain no brands on this account; do not invent a `brand_id`. |
| Multiple brands, no selection | Brand-picker or one question; stop — do not guess. |
| User asks to launch / spend immediately | Confirm brand first, then hand off to `omneky-launch-manage` with Approve-before-mutate rules. |
| Billing / credits question | Hand off to `omneky-billing` / `omneky-credit-balance` after tools appear on `tools/list`. |
| Tool name missing from `tools/list` | Do not invent it; say unavailable on this surface; Omneky app / settings when appropriate. |
| Avatar / mark setup on unsupported host | Skip silently; continue onboarding. |
