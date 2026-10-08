---
name: omneky-product-video
description: >-
  Generate multi-scene product video ads from catalogue or a product URL.
  Use for product video, narrative picks, or Generate Now commercials.
  Keywords: product video, video ad, narrative, narrative_id, multi-scene,
  slim cards, target_duration, 30 credits, portrait, landscape, square.
---

# Product video ads

## Activation analytics

If the host exposes a skill-activation / analytics hook, call it once per new user request with this skill name; otherwise skip silently. Never invent a tracking tool. Omneky MCP does **not** expose `track_skill_activation`.

## Purpose

Multi-scene product video commercials via
`fetch_product_video_narratives` → user pick → `generate_product_video`.
Fetch returns **slim cards** with a minted `narrative_id` (may also echo
`id`); the full narrative is persisted server-side. Prefer passing
**`narrative_id`** on generate so the server hydrates segments. Not a
substitute for launch.

## When to use

- Product video / multi-scene commercial requests
- Narrative card selection flows
- Generate Now (omit both `narrative_id` and `narrative`; pass `target_duration`)

## When not to use

- Still image ads → `omneky-image-ads`
- Treating Generate Now as “animation only” or as an auto-launch
- Central-only video triggers / UGC / `edit_video` (not public)
- Inventing segments, title-only `narrative` blobs, or fake `narrative_id`s

## OpenAI runtime contract

- Use only tools from the current OpenAI host + Omneky MCP (`https://mcp.omneky.com/mcp`). Never invent tools.
- Prefer native ChatGPT / host widgets and question UI for decisions. Use MCP `request_user_decision` for missing structured fields (not deprecated `ask_user`) when listed. Else follow `omneky-failure-modes` § Approval / plain-chat fallback.
- When intake is incomplete, ask **one** concise chat question. Never invent a question tool.
- Generate / Cancel turns: end the turn after showing the choice UI (or plain-chat Generate / Cancel); mutate only after affirmative Generate.
- Never invent tokens; OAuth is host-managed.
- **Prefer runtime `tools/list`:** if the live tool schema differs from this skill (e.g. `narrative_id` present/absent, `narrative` shape), follow the live schema over hardcoded skill copy.

## Non-negotiable output / safety contract

- Credit callout before generate (~**30** credits for multi-scene video when
  submitted). Generate / Cancel via host UI or plain chat. Billing tools
  gating: `omneky-failure-modes` § Billing tools absent.
- After narrative fetch, present **slim cards** for UI (`narrative_id` / `id`,
  title, hook, duration, description). On pick, prefer
  `generate_product_video` with **`narrative_id`** from the card (server
  hydrates `video_gen.segments`). Do **not** invent a partial narrative;
  do **not** invent an id.
- Full `narrative` object with non-empty `video_gen.segments` is still OK
  when available, but **prefer `narrative_id`**.
- Thin/string picks without a resolvable minted id → `narrative_unresolved`
  (no job, no credits) — re-fetch and re-pick; never invent segments or
  silently switch to Generate Now.
- Generate Now: **omit both** `narrative_id` and `narrative`; pass
  `target_duration` 10–30 (default **12** when omitted by server). 10–15
  short invent; 16–30 longform. Optional `hook` for Generate Now only.
- `environment_setting` / `location_url` = optional HTTPS image URL only.
- Widget owns `poll_video_generation`; agent uses one
  `get_generation_status(..., kind="video")` on text hosts next turn.
- Ambiguous submit after optional client `job_id`: follow
  `omneky-failure-modes` § Ambiguous paid submit recovery.
- Never claim success without completion.

## Staged workflow

### Stage 1 — Brand + product

1. Brand pick (`list_brands` / `get_brand_details`).
2. Product: `list_brand_products` / `get_product_details`, or import URL via
   `omneky-product-import` first.
3. Required generate args later: `product_image_urls`, `product_name`,
   `product_description`, `orientation` (`landscape`|`portrait`|`square`),
   `brand_id`, `company_id`.

### Stage 2 — Narratives (selected-story flow)

1. `fetch_product_video_narratives`.
2. Present slim cards from the fetch result (`narrative_id` / `id`, title,
   hook, duration, description).
3. Wait for pick; end turn after UI / plain-chat options.
4. Keep the chosen **`narrative_id`** (and card metadata) for Stage 3.

### Stage 3 — Credits + generate

1. Balance check if `get_account_credit_balance` is on `tools/list`; else
   operational ~30 callout (`omneky-failure-modes` § Billing tools absent).
2. Selected story: `generate_product_video` with **`narrative_id`** from the
   card + orientation mapping (`9:16` → `portrait`, `16:9` → `landscape`,
   `1:1` → `square`). Prefer omitting the fat `narrative` blob when the id
   is available. Still pass required product fields.
3. Generate Now (user skipped pick): omit both `narrative_id` and
   `narrative`; pass `target_duration` 10–30 (default 12); optional `hook`.

### Stage 4 — Completion + handoff

1. Poll rules as in `omneky-creative` / failure-modes Stage D.
2. Register + `omneky-launch-manage` only after Approve (paused default).

## Failure boundaries

| Failure | Required response |
| --- | --- |
| Thin / invented / title-only narrative without resolvable id | Forbidden — use `narrative_id` from fetch (or full object with segments); never invent. |
| `narrative_unresolved` | Re-fetch + re-pick; no credit charge. Do not invent; do not silent Generate Now. |
| `credit_insufficient` | Did not start; billing path if tools present; else Omneky app; no retry. |
| Billing tools absent | `omneky-failure-modes` § Billing tools absent. |
| Ambiguous paid submit | `omneky-failure-modes` § Ambiguous paid submit recovery. |
| Auto-picked narrative | Forbidden. |
| Prose in `environment_setting` | Omit / URL only. |
| Early success claim | Forbidden. |
| Live `tools/list` conflicts with skill copy | Prefer live schema. |
