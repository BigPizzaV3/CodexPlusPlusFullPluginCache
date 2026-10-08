---
name: omneky-product-import
description: >-
  Import a product page URL into the Omneky brand catalogue or update a SKU
  after scrape confirmation. Keywords: import product, product URL, scrape
  product, catalogue, SKU, identify product, finalize scraped product, PDP.
---

# Product import

## Activation analytics

If the host exposes a skill-activation / analytics hook, call it once per new user request with this skill name; otherwise skip silently. Never invent a tracking tool. Omneky MCP does **not** expose `track_skill_activation`.

## Purpose

URL → catalogue draft → user confirm → finalize. Specialized path of
`omneky-catalogue` for PDP imports.

## When to use

- User pastes a product URL to import
- Re-scrape / refresh an existing PDP into a new draft then finalize

## When not to use

- Manual field entry without URL → `omneky-catalogue` (`create_product` /
  `upsert_brand_product`)
- Generating creatives from the product before finalize completes
- Category / collection listing URLs (classify first; usually skip scrape)

## OpenAI runtime contract

- Use only tools from the current OpenAI host + Omneky MCP (`https://mcp.omneky.com/mcp`). Never invent tools.
- Prefer native ChatGPT / host widgets and question UI for decisions. Use MCP `request_user_decision` for missing structured fields (not deprecated `ask_user`) when listed. Else follow `omneky-failure-modes` § Approval / plain-chat fallback.
- When intake is incomplete, ask **one** concise chat question. Never invent a question tool.
- Approval / Generate turns: end the turn after Approve / Deny (or Generate / Cancel) via host UI or plain chat; mutate only after affirmative Approve / Generate. Never invent a fake widget tool.
- Never invent tokens; OAuth is host-managed.

## Non-negotiable output / safety contract

- Always `identify_product_from_url` before scrape.
- Finalize with `finalize_scraped_product` — never treat scrape draft as
  completed via `upsert_brand_product`.
- Confirm selected images + fields before finalize (Approve widget preferred).
- No public product-delete tool.
- Pending scrapes: no tight-loop polling in one turn.

## Staged workflow

### Stage 1 — Brand

1. Resolve `brand_id` (`list_brands` / picker). Prefer numeric id.

### Stage 2 — Identify

1. `identify_product_from_url`.
2. If listing/category: tell the user; ask for a single product PDP. Stop.

### Stage 3 — Scrape

1. `scrape_product_from_url`.
2. If `status=pending`: explain; retry later with the same `brand_id` + url.
3. Do not start multiple parallel scrapes for the same URL in one turn.

### Stage 4 — Confirm

1. Present name, description, images, URL.
2. Host Approve / Deny / Edit (or plain-chat fallback / `request_user_decision` when listed) — `omneky-failure-modes` § Approval / plain-chat fallback.
3. End turn after the widget.

### Stage 5 — Finalize

1. On Approve: `finalize_scraped_product` with chosen fields / images.
2. Optionally `update_product_url` if only the URL should change later.
3. Hand off to creative or launch skills with the new `product_id`.

### Stage 6 — Re-import

1. Optional `update_product_url` first.
2. Scrape again → confirm → finalize.

## Failure boundaries

| Failure | Required response |
| --- | --- |
| Listing URL | No scrape; request PDP. |
| Pending | Later retry; no tight loop. |
| User denies finalize | Leave draft; do not upsert as completed. |
| Wrong brand | Re-resolve brand; do not finalize onto guessed id. |
| Delete request | No public delete; explain. |
