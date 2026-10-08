---
name: omneky-launch-manage
description: >-
  Launch and manage Omneky paid-media ads on Meta/Facebook, Google Ads,
  TikTok, LinkedIn, Reddit, Pinterest, and X Ads (Twitter). Use when the
  user wants to create, pause, budget, retarget, or delete campaigns, or
  attach a catalogue/creative to a live ad account. Intent keywords: paid
  media, Meta ads, Facebook ads, Instagram, Google PMax, Demand Gen,
  TikTok ads, LinkedIn ads, Reddit ads, Pinterest ads, X Ads, Twitter ads,
  launch Meta sales ads, ROAS, launch campaign, pause ad, budget,
  targeting, product catalogue, Approve launch.
---

# Omneky launch and manage

## Activation analytics

If the host exposes a skill-activation / analytics hook, call it once per new user request with this skill name; otherwise skip silently. Never invent a tracking tool. Omneky MCP does **not** expose `track_skill_activation`.

## Purpose

Create and operate paid-media campaigns across connected channels with
**Approve-before-mutate** discipline. Default new launches to **PAUSED**.
Prefer pause over delete. X Ads wire name is **`twitter`**, never `x`.

## When to use

- Launch, pause, resume, budget, or retarget paid-media campaigns
- Meta / Facebook / Instagram, Google Ads, TikTok, LinkedIn, Reddit,
  Pinterest, or X Ads
- Attach a catalogue product or chat-generated creative to an existing
  campaign or ad set
- Connect a missing ad account (delegate detail to `omneky-self-connect`)

## When not to use

- ROAS / CTR / spend reporting → `omneky-analytics`
- Generating or editing creatives → `omneky-creative` (then return here)
- Catalogue SKU writes → `omneky-catalogue`
- Inventing Central-only or OpenAI Ads **launch** names (`launch_openai_*`,
  managed-Meta launch tools)

## OpenAI runtime contract

- Use only tools from the current OpenAI host + Omneky MCP (`https://mcp.omneky.com/mcp`). Never invent tools.
- Prefer native ChatGPT / host widgets and question UI for decisions. Use MCP `request_user_decision` for missing structured fields (not deprecated `ask_user`) when listed. Else follow `omneky-failure-modes` § Approval / plain-chat fallback.
- When intake is incomplete, ask **one** concise chat question. Never invent a question tool.
- Approval turns: end the turn after Approve / Deny / Edit (host UI or plain chat); mutate only next turn after Approve. Never invent a fake summary-widget tool; never stall for a widget that did not appear.
- Never invent tokens; OAuth is host-managed.

## Non-negotiable output / safety contract

- Before any `launch_*`, `set_ad_entity_status` / `set_ad_budget` /
  `update_ad_targeting` / `delete_*`: show a one-card summary
  (`Brand · Channel · Objective · Budget · Paused|Live · Creative`) with
  **Approve / Deny / Edit** via host-native confirmation / MCP Apps /
  `request_user_decision` when available; otherwise **plain-chat fallback**
  (`omneky-failure-modes` § Approval / plain-chat fallback). End the turn.
  Mutate only next turn after affirmative Approve (or clear yes).
- Default `status_on_launch` / `configured_status` to **`PAUSED`** unless the
  user explicitly asked to go live.
- Prefer **pause** over **delete**. Deletes: first offer Pause instead /
  Delete permanently / Cancel; then a **second** Approve confirm.
- Prefer `set_ad_entity_status` over deprecated `set_ad_status`.
- Prefer `request_user_decision` over deprecated `ask_user` when that tool
  is on `tools/list` and fields are missing / `needs_user_decision`. Else
  plain-chat questions. Never dump `clarification_needed` JSON; never
  auto-retry failed writes same turn.
- Hierarchy: Campaign → Ad Set (`ad_group`) → Ad. Creative is an asset on
  the Ad (`ad_specs`), never on the campaign. Status/budget tools do not
  add ads.
- Confirm channel connected before launch; else `omneky-self-connect`.
- After success: post-launch next steps (host UI or plain chat) — Check
  status / Pull 7d metrics / Done (metrics via `omneky-analytics`).
- Keep decision options to ≤3 when possible.

## Staged workflow

### Stage 1 — Brand + intent

1. Resolve brand (`list_brands` / picker) → `get_brand_details`.
2. Confirm live launch vs creative-only. Creative-only → `omneky-creative`
   first (credit callouts image ~5 / video ~30).
3. Catalogue product when relevant: `list_brand_products` /
   `get_product_details`.

### Stage 2 — Channel readiness

1. `get_channel_connection_status` (X: `channel="twitter"`; Pinterest also
   `get_pinterest_connection_status`).
2. `get_channel_budget` / `minimum_budget_for_objective`.
3. Optional: `reach_estimate` for targeting size questions.
4. Optional: `get_ad_custom_properties` for custom conversion definitions.
5. Disconnected → `get_channel_connect_url` path via `omneky-self-connect` /
   `omneky-channel-connect`.

### Stage 3 — Targeting pre-calls

| Channel | Required pre-call | Notes |
| --- | --- | --- |
| Meta / Facebook | none | Inline `targeting`: countries / age_min / age_max |
| Google PMax | none | Set `link_url`; Google places automatically |
| Google Demand Gen | `search_google_countries` | Pass values as `targeting_fragments` |
| LinkedIn | `search_ad_targeting` `types=["locations"]` | Must include `urn:li:adTargetingFacet:locations`; `start_date` on new group |
| TikTok | `get_tiktok_location_ids` | `location_ids` required on ad group |
| Reddit | none | Inline `targeting`; `bid_value` microcurrency (dollars × 1e6) |
| X Ads | none | Wire name `twitter` |
| Pinterest | none | `get_pinterest_*` list helpers |

### Stage 4 — Creative attach

1. Chat creative → `register_creative_for_launch` (alias
   `register_ad_instance_item`) before launch when required.
2. Confirm copy, CTA, landing URL.

### Stage 5 — Approve (exclusive-tool turn)

1. Show summary Approve / Deny / Edit (host UI when available; else
   plain-chat card — `omneky-failure-modes` § Approval / plain-chat
   fallback).
2. **End the turn.** Do not call `launch_*` yet.

### Stage 6 — Launch (next turn after Approve)

Call the matching tool with paused default. Existing campaign:
`campaign_spec={"id": …}`. Existing ad set: `ad_group_spec={"id": …}`.

**Meta / Facebook:** `launch_facebook_sales_ad`,
`launch_facebook_leads_ad`, `launch_facebook_awareness_ad`,
`launch_facebook_traffic_ad`, `launch_facebook_video_views_ad`
(Meta-focused detail also in `omneky-meta-launch`).

**Google:** `launch_google_performance_max_ad`,
`launch_google_demand_gen_ad`.

**LinkedIn:** `launch_linkedin_brand_awareness_ad`,
`launch_linkedin_website_visits_ad`, `launch_linkedin_conversions_ad`,
`launch_linkedin_engagement_ad`.

**Reddit:** `launch_reddit_awareness_ad`, `launch_reddit_traffic_ad`,
`launch_reddit_conversions_ad`, `launch_reddit_leads_ad`,
`launch_reddit_video_views_ad`.

**TikTok:** `launch_tiktok_traffic_ad`, `launch_tiktok_video_views_ad`,
`launch_tiktok_conversions_ad`, `launch_tiktok_leads_ad`.

**X Ads (`twitter`):** `launch_twitter_awareness_ad`,
`launch_twitter_traffic_ad`, `launch_twitter_engagements_ad`,
`launch_twitter_followers_ad`, `launch_twitter_video_views_ad`.

**Pinterest:** `launch_pinterest_awareness_ad`,
`launch_pinterest_traffic_ad`, `launch_pinterest_sales_ad`,
`launch_pinterest_leads_ad`, `launch_pinterest_video_views_ad`.

No Omneky-managed Meta / OpenAI **launch** tools. OpenAI Ads can be
*connected* (`connect_openai_ads`); do not invent `launch_openai_*`.

### Stage 7 — Manage existing

**Inspect:** `get_campaigns`, `get_ad_groups` (pass `campaign_id` — unscoped
brand-wide lists can time out), `get_ads`, `get_channel_budget`,
`minimum_budget_for_objective`, `get_campaign_ad_group_names`.
Pinterest: `get_pinterest_campaigns` / `get_pinterest_ad_groups` /
`get_pinterest_ads`.

**Mutate (after Approve):** `set_ad_entity_status`, `set_ad_budget`,
`update_ad_targeting` (Facebook-only retarget),
`set_pinterest_entity_status`.

**Delete (dual confirm):** `delete_campaign`, `delete_ad_group`,
`delete_ads`.

Specialized pause/budget path: `omneky-pause-budget`.

### Stage 8 — Post-launch

Next-steps (host UI or plain chat): Check status / Pull 7d metrics
(`omneky-analytics`) / Done.

## Failure boundaries

| Failure | Required response |
| --- | --- |
| Mutate without Approve | Forbidden — show summary (host UI or plain chat) and end turn. |
| Invented summary-widget tool | Forbidden — `omneky-failure-modes` § Approval / plain-chat fallback. |
| Disconnected channel | Self-connect / channel-connect; do not invent launch. |
| LinkedIn / TikTok / Google DG 400 | Run required targeting pre-call; see `omneky-failure-modes`. |
| `needs_user_decision` | `request_user_decision` if listed; else plain chat; no auto-retry. |
| Unscoped `get_ad_groups` timeout | Pass `campaign_id`; narrow. |
| User said go live but widget still paused | Confirm explicitly before ACTIVE. |
| Delete request | Pause-first offer; dual Approve for delete. |
| `channel=x` | Correct to `twitter`. |
| Reddit $ budgets entered as dollars in `bid_value` | Convert to microcurrency. |
| OpenAI Ads launch request | Connect only; no public launch tool. |

## Channel gotchas

- Reddit `bid_value` is microcurrency (dollars × 1,000,000). $5/day = `5000000`.
- LinkedIn `start_date` is required when creating a new campaign group.
- Facebook lead ads: set `lead_gen_form_id` on ad specs for native forms.
- Google Demand Gen needs `search_google_countries` → `targeting_fragments`.
- TikTok needs `get_tiktok_location_ids` → `location_ids`.
- Pinterest list/status helpers exist alongside generic getters.
- OpenAI Ads: `connect_openai_ads` / `get_openai_ads_connection_status` only —
  connect ≠ launch.
- Drive assets: `get_google_drive_connect_url` via `omneky-self-connect`.

## Sibling map

| Need | Skill |
| --- | --- |
| Meta-only | `omneky-meta-launch` |
| Pause / budget only | `omneky-pause-budget` |
| Connect channel | `omneky-self-connect` / `omneky-channel-connect` |
| Creatives | `omneky-creative` |
| Metrics after launch | `omneky-analytics` |
| Failures | `omneky-failure-modes` |
