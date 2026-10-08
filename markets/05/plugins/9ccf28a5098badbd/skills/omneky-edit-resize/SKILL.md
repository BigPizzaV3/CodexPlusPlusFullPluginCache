---
name: omneky-edit-resize
description: >-
  Edit an existing Omneky creative or resize it for Stories, Reels, 9:16,
  4:5, or 16:9. Resizes are not charged (adapt an already-paid creative).
  Keywords: edit ad, resize ad, Stories, Reels, aspect ratio, outpaint,
  edit_image, resize_ad, uncharged resize.
---

# Edit and resize

## Activation analytics

If the host exposes a skill-activation / analytics hook, call it once per new user request with this skill name; otherwise skip silently. Never invent a tracking tool. Omneky MCP does **not** expose `track_skill_activation`.

## Purpose

Synchronous edit / resize of **existing** finished creatives. No async
`job_id` polling for these tools.

## When to use

- Change copy / layout / style on a finished image ad
- New placement aspect ratio for an already-paid creative

## When not to use

- Net-new concepts → `omneky-image-ads` / `omneky-creative`
- Product video generation → `omneky-product-video`
- Calling `get_generation_status` for these sync tools

## OpenAI runtime contract

- Use only tools from the current OpenAI host + Omneky MCP (`https://mcp.omneky.com/mcp`). Never invent tools.
- Prefer native ChatGPT / host widgets and question UI for decisions. Use MCP `request_user_decision` for missing structured fields (not deprecated `ask_user`) when listed. Else `omneky-failure-modes` § Approval / plain-chat fallback.
- When intake is incomplete, ask **one** concise chat question. Never invent a question tool.
- Never invent tokens; OAuth is host-managed.

## Non-negotiable output / safety contract

- `edit_image`, `resize_ad`, and `resize_image` are **synchronous** — they
  return URLs when done. Do **not** call `get_generation_status` for them.
- **Resizes are not charged** (live tool text): `resize_ad` / `resize_image`
  adapt an already-paid creative. Do **not** invent “premium resize tiers”
  or require balance-before-resize. Follow
  `omneky-failure-modes` § Resize / edit charge. If a future `tools/list`
  description changes, follow the live tool text over this skill.
- `edit_image` charge: follow live tool text for that tool only; gate with
  balance tools only when listed and the live text indicates a charge
  (`omneky-failure-modes` § Billing tools absent).
- Confirm the source asset id / URL with the user when ambiguous.
- Never invent Central-only enhance / variation / upscale tool names if they
  are not on `tools/list`.

## Staged workflow

### Stage 1 — Resolve asset + brand

1. Confirm brand if needed.
2. Confirm which finished creative to edit/resize.

### Stage 2 — Charge check (edit only when applicable)

1. Resize path: no credit gate — uncharged per live tool text.
2. Edit path: if live tool text indicates a charge and
   `get_account_credit_balance` is on `tools/list`, check balance; else skip
   inventing a balance. Optional Apply vs Cancel for paid edit.

### Stage 3 — Mutate (sync)

1. Edit: `edit_image` with natural-language instruction → edited image URL
   (often 30–120s).
2. Placement resize: `resize_ad` → `resized_ad_url` (often 30–180s).
3. Pixel resize: `resize_image` → `presigned_url` / `resized_image_url`.
   Prefer `resize_ad` for marketing placements.

### Stage 4 — Next

1. More variants, or `register_creative_for_launch` + launch-manage handoff
   (Approve, paused default — `omneky-failure-modes` § Approval / plain-chat
   fallback).

## Failure boundaries

| Failure | Required response |
| --- | --- |
| Agent starts status poll loop | Stop — sync tools do not use job polling. |
| “Premium resize” / balance-before-resize | Forbidden — resizes not charged; § Resize / edit charge. |
| `credit_insufficient` on edit | Billing path if tools present; no retry. |
| Missing source asset | Ask once; do not invent URLs. |
| Invented upscale / UGC tool | Refuse unless on `tools/list`. |
