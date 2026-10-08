---
name: omneky-creative
description: >-
  Generate, edit, or resize Omneky paid-media image and video ads, grounded
  in the brand product catalogue when the brief is product-specific. Use
  when the user wants a new image ad, a multi-scene product video, an edit
  of an existing creative, or another aspect ratio (9:16, 4:5, Stories,
  Reels). Intent keywords: turn this product URL into video ads, generate
  image ads for this product, image ad, product video, creative, catalogue,
  edit ad, resize ad, Meta creative, TikTok video, Reels, credits.
---

# Omneky creative

## Activation analytics

If the host exposes a skill-activation / analytics hook, call it once per new user request with this skill name; otherwise skip silently. Never invent a tracking tool. Omneky MCP does **not** expose `track_skill_activation`.

## Purpose

Paid-media image and multi-scene product video generation plus sync edit /
resize on `https://mcp.omneky.com/mcp`. Ground product-specific briefs in the
catalogue. Never claim success without a completed status or sync result URL.

## When to use

- New static image ads or multi-scene product video commercials
- Edit copy, layout, or style on an existing finished ad
- Resize a paid-media creative into another placement (9:16, 4:5, 16:9)
- Product-specific briefs that need the brand catalogue first

## When not to use

- Launching the finished creative → `omneky-launch-manage` after
  `register_creative_for_launch` (Approve before launch)
- ROAS / CTR → `omneky-analytics`
- Creating / updating catalogue products → `omneky-catalogue`
- Central-only names (`trigger_ac_ad_generation`,
  `trigger_multi_scene_product_video`, sibling video triggers, UGC,
  `edit_video`, `trigger_product_video_v2`) — clients use public aliases below
- Thin single-path asks may use `omneky-image-ads` /
  `omneky-product-video` / `omneky-edit-resize` instead

## OpenAI runtime contract

- Use only tools from the current OpenAI host + Omneky MCP (`https://mcp.omneky.com/mcp`). Never invent tools.
- Prefer native ChatGPT / host widgets and question UI for decisions. Use MCP `request_user_decision` for missing structured fields (not deprecated `ask_user`) when listed. Else follow `omneky-failure-modes` § Approval / plain-chat fallback.
- When intake is incomplete, ask **one** concise chat question. Never invent a question tool.
- Generate / Cancel / Approve turns: end the turn after the choice UI (or plain chat); mutate only after affirmative Generate / Approve.
- Never invent tokens; OAuth is host-managed.
- Prefer runtime `tools/list` when it differs from skill hardcoding.

## Non-negotiable output / safety contract

- **Credit callout before paid generation**: image ads typically **~5**
  credits; multi-scene product videos typically **~30**, charged when the job
  is submitted. Show Generate / Cancel (host UI preferred; else plain chat).
  Billing gating: `omneky-failure-modes` § Billing tools absent —
  call balance only when listed; if absent, state operational cost, proceed
  after user confirms, rely on `credit_insufficient` as the hard gate.
- `credit_insufficient` ⇒ render **did not start** — relay that; do not retry;
  upgrade path via billing skill **when those tools are listed**.
- Never claim success without `get_generation_status` completion (async) or a
  sync tool’s returned URL (`edit_image` / `resize_ad` / `resize_image`).
- On hosts with MCP Apps widgets (ChatGPT): the widget owns
  `poll_image_generation` / `poll_video_generation` / `sync_generation_group`
  — do **not** call those as the agent and do not loop
  `get_generation_status` in one turn. On text-only hosts: stop after
  submit; on the next user message call `get_generation_status(job_id,
  kind=…)` **once**.
- Ask whether the creative is for a **specific product** or the **brand in
  general**. Product-specific: catalogue grounding. Brand-general:
  `get_brand_details` assets only.
- Unique `gpt_ad_gen_id` per image job (`<short-slug>-<uuid4>`), never reused.
  Ambiguous submit recovery: `omneky-failure-modes` § Ambiguous paid submit
  recovery (status with that key as `job_id`; on `not_found` wait/ask —
  do **not** auto-mint a new key).
- **Video:** `fetch_product_video_narratives` returns **slim cards** with a
  minted `narrative_id` (may also echo `id`); full narrative is persisted
  server-side. On pick, prefer `generate_product_video` with
  **`narrative_id`** (server hydrates segments). Full `narrative` with
  `video_gen.segments` is still OK if available — prefer the id. Do not
  invent partial narratives or fake ids.
- Thin/string picks without a resolvable id → `narrative_unresolved` (no
  job, no credits) — re-fetch; never invent; never silent Generate Now.
- Generate Now: **omit both** `narrative_id` and `narrative`; pass
  `target_duration` 10–30 (default **12**). Optional `hook` for Generate
  Now only.
- Prefer runtime `tools/list` over skill hardcoding when schemas differ.
- `environment_setting` / `location_url` is optional **HTTPS image URL** only
  — never scene prose; omit if no URL; never invent a URL.
- Resizes are **not charged** (adapt already-paid creative) — follow
  `omneky-failure-modes` § Resize / edit charge. No “premium resize tiers”.
- Prefer pause-ready launch handoff; never auto-launch after gen.

## Staged workflow

### Stage 1 — Brand + credits + brief type

1. Resolve brand: `list_brands` / picker / `get_brand_details`.
2. `get_current_user` when `user_id` is required.
3. If `get_account_credit_balance` is on `tools/list` and balance unknown,
   call it. Else follow `omneky-failure-modes` § Billing tools absent.
4. Credit callout (image ~5 / video ~30) with Generate / Cancel (host UI or
   plain chat). End turn after Cancel or while waiting for Generate.
5. Ask product-specific vs brand-general if unclear.

### Stage 2 — Catalogue grounding (product-specific)

1. `list_brand_products` / `get_product_details`.
2. For image gens, pass **one** product library image URL in `user_assets`
   when possible. Quality drops with more than two assets per ad — send more
   only when the user explicitly asks.
3. If the product has **no library images** and the user did not supply
   imagery: **do not** call `generate_image_ad` — ask for another product,
   an upload, or a brand-general brief (empty-asset jobs often fail).

### Stage 3 — Image ads

1. `generate_image_ad` with `ad_concept` (full prompt — no separate `prompt`
   arg), required `gpt_ad_gen_id` / `brand_id` / `brand_name` / `company_id` /
   `user_id`, and unique `gpt_ad_gen_id` (`<short-slug>-<uuid4>`).
2. Remember the intended key. Tool returns `job_id` immediately — not a
   finished image.
3. Widget host: let widget poll. Text host: one
   `get_generation_status(job_id, kind="image")` on a later turn.
4. Ambiguous timeout after possible submit: `omneky-failure-modes`
   § Ambiguous paid submit recovery (status with `gpt_ad_gen_id` as
   `job_id`; on `not_found` wait ~30–60s and/or ask user — do not auto
   mint a new key).
5. Variants: `omneky-edit-resize` (`edit_image`, `resize_ad`,
   `resize_image`).

### Stage 4 — Video ads (narrative select → generate)

1. `fetch_product_video_narratives` when you need narrative options.
   Present **slim cards** (`narrative_id` / `id`, title, hook, duration,
   description). Do **not** auto-trigger video.
2. Wait for the user to pick a card (host UI / plain chat / one question);
   end turn. Keep the chosen **`narrative_id`**.
3. `generate_product_video` with that **`narrative_id`** and orientation:
   `9:16` → `portrait`, `16:9` → `landscape`, `1:1` → `square`.
   Server hydrates `video_gen.segments`. Prefer omitting the fat
   `narrative` blob when the id is available. A full `narrative` with
   non-empty `video_gen.segments` is still OK if you have it — prefer id.
   Also pass required top-level: `product_image_urls`, `product_name`,
   `product_description`, `orientation`, `brand_id`, `company_id`.
4. If `error=narrative_unresolved`: re-fetch and pick again. No job started,
   no credits. Do not invent segments; do not silent Generate Now.
5. Generate Now (no picked story): **omit both** `narrative_id` and
   `narrative`. Pass `target_duration` 10–30 (default **12**; 10–15 short
   invent, 16–30 longform). Optional `hook`. Generate Now invents a
   commercial; it is **not** animation.
6. Same poll rule as images with `kind="video"`.

### Stage 5 — Edit and resize (sync — no poll)

1. `edit_image` — change an existing finished ad (natural language). Returns
   edited URL when done (often 30–120s). **No** `job_id` / status poll.
2. `resize_ad` — marketing aspect-ratio outpaint; returns `resized_ad_url`.
   **Not charged** (adapt already-paid creative).
3. `resize_image` — explicit pixel dimensions; prefer `resize_ad` for
   placements. **Not charged.**
4. Follow `omneky-failure-modes` § Resize / edit charge. Do not invent
   premium resize tiers or balance-before-resize. If live `tools/list` text
   changes later, follow the live tool text.

### Stage 6 — Register + launch handoff

1. Persist chat creative when launching later:
   `register_creative_for_launch` (also accepted:
   `register_ad_instance_item`).
2. Hand off to `omneky-launch-manage` / `omneky-meta-launch` with Approve
   before any `launch_*` (`omneky-failure-modes` § Approval / plain-chat
   fallback). Default paused.

## Failure boundaries

| Failure | Required response |
| --- | --- |
| `credit_insufficient` | Did not start; billing / upgrade if tools present; else Omneky app; no retry. |
| Billing tools absent | `omneky-failure-modes` § Billing tools absent. |
| Ambiguous paid submit | `omneky-failure-modes` § Ambiguous paid submit recovery. |
| Empty product imagery | Do not generate; ask for assets / other product / brand-general. |
| Agent called widget poll tools | Stop; leave polling to widget / one status peek next turn. |
| Looping `get_generation_status` in one turn | Forbidden; one peek per follow-up. |
| Thin / invented narrative without resolvable id | Forbidden — prefer `narrative_id` from fetch (or full object with segments). |
| `narrative_unresolved` | Re-fetch narratives; no credit charge. Never invent; never silent Generate Now. |
| Live `tools/list` schema differs | Prefer live schema over skill hardcoding. |
| Prose in `environment_setting` | Omit or pass HTTPS URL only. |
| Invented Central trigger names | Refuse; use public `generate_*` / `fetch_product_video_narratives`. |
| Premium resize / balance-before-resize | Forbidden — § Resize / edit charge. |
| Auto-launch after gen | Forbidden; Approve + paused default via launch-manage. |
| Claim success without URL / completed status | Forbidden. |

## Batching and media limits

- Prefer **one** strong product image in `user_assets` per image ad. More than
  two assets per ad usually hurts quality unless the user explicitly wants a
  multi-image collage.
- For multiple image concepts, submit separate `generate_image_ad` jobs with
  **distinct** `gpt_ad_gen_id` values. Do not reuse ids.
- Do not start a large unpaid speculative batch — credit callout must reflect
  the count (≈5 × image jobs, ≈30 × multi-scene video jobs).
- On widget hosts, `sync_generation_group` is widget-owned so one iframe can
  track siblings — the agent must not call it.
- Never mix sync edit/resize polling with async gen polling rules.

## Sibling map

| Need | Skill |
| --- | --- |
| Image-only | `omneky-image-ads` |
| Video-only | `omneky-product-video` |
| Edit / resize only | `omneky-edit-resize` |
| Credits | `omneky-credit-balance` / `omneky-billing` |
| Launch after gen | `omneky-launch-manage` / `omneky-meta-launch` |
| Catalogue grounding | `omneky-catalogue` / `omneky-product-import` |
| Shared recoveries | `omneky-failure-modes` |
