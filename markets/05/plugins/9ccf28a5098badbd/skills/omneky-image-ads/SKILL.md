---
name: omneky-image-ads
description: >-
  Generate branded still image ads for a product or brand brief. Use when
  the user wants image ads, static creatives, or Meta/feed stills.
  Keywords: image ad, branded ad, still creative, feed ad, generate image,
  gpt_ad_gen_id, 5 credits, ambiguous submit recovery.
---

# Image ads

## Activation analytics

If the host exposes a skill-activation / analytics hook, call it once per new user request with this skill name; otherwise skip silently. Never invent a tracking tool. Omneky MCP does **not** expose `track_skill_activation`.

## Purpose

Focused still-image generation path (subset of `omneky-creative`). Submit
async `generate_image_ad`, wait correctly for completion, then offer edit /
resize / launch handoff.

## When to use

- User wants static / feed / still image ads
- Product or brand-general image concepts

## When not to use

- Multi-scene product video → `omneky-product-video`
- Launch without confirmation → `omneky-launch-manage`
- Catalogue import → `omneky-product-import`

## OpenAI runtime contract

- Use only tools from the current OpenAI host + Omneky MCP (`https://mcp.omneky.com/mcp`). Never invent tools.
- Prefer native ChatGPT / host widgets and question UI for decisions. Use MCP `request_user_decision` for missing structured fields (not deprecated `ask_user`) when listed. Else `omneky-failure-modes` § Approval / plain-chat fallback.
- When intake is incomplete, ask **one** concise chat question. Never invent a question tool.
- Generate / Cancel turns: end the turn after the choice UI (or plain chat); mutate only after affirmative Generate.
- Never invent tokens; OAuth is host-managed.

## Non-negotiable output / safety contract

- Credit callout before generate (~**5** credits per image job when submitted).
  Generate / Cancel via host UI or plain chat.
- Credits / balance: follow `omneky-failure-modes` § Billing tools absent —
  call `get_account_credit_balance` only when listed; if absent, state ~5
  operational cost, proceed after user confirms intent, rely on
  `credit_insufficient` as the hard gate. Never invent balance.
- Unique `gpt_ad_gen_id` (`<short-slug>-<uuid4>`), never reused across
  variants. Required with `brand_id`, `brand_name`, `company_id`, `user_id`;
  prompt field is `ad_concept`.
- Ambiguous submission (timeout / transport / unknown after possible
  submit): follow `omneky-failure-modes` § Ambiguous paid submit recovery —
  status-check with `gpt_ad_gen_id` as `job_id` (kind=image). If
  `not_found` / queued+source not_found: **WAIT ~30–60s and/or ask user** —
  do **not** auto-mint a new key (commit lag can still mean charged). New
  key only after clear pre-accept failure, or explicit user OK after wait
  still shows never-started.
- Prefer one product library image in `user_assets`; do not generate with
  empty assets when product-specific and no imagery exists.
- Widget hosts own `poll_image_generation` / `sync_generation_group` — agent
  must not call them. Text hosts: one `get_generation_status(..., kind="image")`
  on a later turn.
- Never claim success without completed status / asset URL.
- Hand off launch only after user confirms (paused default).

## Staged workflow

### Stage 1 — Brand + brief

1. `list_brands` / picker / `get_brand_details`.
2. Product-specific: `list_brand_products` / `get_product_details` (or
   `identify_product_from_url` → import via `omneky-product-import` first).
3. Brand-general: brand assets only.
4. `get_current_user` when `user_id` is required.

### Stage 2 — Credits

1. If `get_account_credit_balance` is on `tools/list`, call when balance
   unknown.
2. Else: state ~5 credits operational cost (`omneky-failure-modes`
   § Billing tools absent).
3. Credit callout Generate / Cancel (host UI or plain chat); end turn if
   waiting.

### Stage 3 — Generate

1. Mint unique `gpt_ad_gen_id` (`<short-slug>-<uuid4>`).
2. `generate_image_ad` with `ad_concept` + that key + required brand /
   company / user fields + assets.
3. Remember the intended key for recovery.
4. Capture returned `job_id` when present.

### Stage 4 — Completion

1. Widget path: wait for widget / user follow-up.
2. Text path: `get_generation_status(job_id, kind="image")` once next turn.
3. Offer `edit_image` / `resize_ad` via `omneky-edit-resize` (resizes
   uncharged per live tool text — `omneky-failure-modes` § Resize / edit charge).

### Stage 5 — Launch handoff

1. `register_creative_for_launch` when attaching to a campaign later.
2. `omneky-launch-manage` / `omneky-meta-launch` with Approve + paused default.

## Failure boundaries

| Failure | Required response |
| --- | --- |
| `credit_insufficient` | No retry; billing path if tools present; else Omneky app. |
| Billing tools absent | `omneky-failure-modes` § Billing tools absent. |
| Clear failure before accept | New `gpt_ad_gen_id` OK for a new attempt. |
| Timeout / transport / unknown after possible submit | Status with `gpt_ad_gen_id` as `job_id`; on `not_found` wait/ask — never auto new key (`omneky-failure-modes` § Ambiguous paid submit recovery). |
| No product imagery | Stop; ask upload / other product / brand-general. |
| Poll loop in one turn | Forbidden. |
| Success claimed early | Forbidden until status/URL. |
