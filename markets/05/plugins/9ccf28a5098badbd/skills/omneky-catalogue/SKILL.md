---
name: omneky-catalogue
description: >-
  Maintain the Omneky brand product catalogue: list products, fetch details,
  create or update SKUs, and import a product-page URL. Use when the user
  wants to add, update, or inspect catalogue products before a paid-media
  launch or creative. Intent keywords: list my products, turn this product
  URL into, product catalogue, catalog, SKU, PDP, scrape product, import URL,
  product images, merchandise, upsert product.
---

# Omneky product catalogue

## Activation analytics

If the host exposes a skill-activation / analytics hook, call it once per new user request with this skill name; otherwise skip silently. Never invent a tracking tool. Omneky MCP does **not** expose `track_skill_activation`.

## Purpose

Read and write the brand product catalogue that grounds product-specific
creatives and launches. There is **no product-delete tool** on this public
surface.

## When to use

- List or inspect products for a brand before a launch or creative
- Add a product by hand (name, description, images, URL)
- Update an existing completed product or its PDP URL
- Import a single product page (identify → scrape → confirm → finalize)

## When not to use

- ROAS / CTR / spend → `omneky-analytics`
- Launching the product onto Meta / Google / TikTok →
  `omneky-launch-manage` after `product_id` + imagery exist
- Generating image/video from the product → `omneky-creative` /
  `omneky-image-ads` / `omneky-product-video`
- Listing / category URLs without classify — always
  `identify_product_from_url` first (see `omneky-product-import`)

## OpenAI runtime contract

- Use only tools from the current OpenAI host + Omneky MCP (`https://mcp.omneky.com/mcp`). Never invent tools.
- Prefer native ChatGPT / host widgets and question UI for decisions. Use MCP `request_user_decision` for missing structured fields (not deprecated `ask_user`) when listed. Else follow `omneky-failure-modes` § Approval / plain-chat fallback.
- When intake is incomplete, ask **one** concise chat question. Never invent a question tool.
- Approval / Generate turns: end the turn after Approve / Deny (or Generate / Cancel) via host UI or plain chat; mutate only after affirmative Approve / Generate. Never invent a fake widget tool.
- Never invent tokens; OAuth is host-managed.

## Non-negotiable output / safety contract

- Prefer numeric `brand_id` when thumbnails matter.
- Confirm create / update fields with the user before writes when they asked
  to confirm, or when fields are ambiguous — use `request_user_decision` or
  a host Approve widget; end turn after the widget.
- Scrape drafts: complete with `finalize_scraped_product`, **not**
  `upsert_brand_product`.
- `scrape_product_from_url` creates a **new draft** each successful start —
  do not spam scrapes.
- No public product-delete — say so if asked; do not invent one.
- Do not launch or charge creative credits from this skill.

## Staged workflow

### Stage 1 — Resolve brand

1. If `brand_id` unknown: `list_brands` → picker → `get_brand_details` when
   logo / colors / `company_id` are needed.

### Stage 2 — Read

1. List: `list_brand_products` (`brand_id`).
2. One product: `get_product_details` (also accepted: `fetch_product_details`)
   with `brand_id` + `product_id`.

### Stage 3 — Create or update (manual)

1. New product: `create_product` **or** `upsert_brand_product` /
   `update_brand_product` without `product_id`. Confirm fields first.
2. Update completed product: `upsert_brand_product` with `product_id`. Pass
   current `product_name` / `product_description` when leaving them unchanged.
3. URL only: `update_product_url`.

### Stage 4 — Import from URL (delegate detail)

Follow `omneky-product-import` stages, summarized:

1. `identify_product_from_url` — skip scrape on listing/category pages.
2. `scrape_product_from_url` — if `status=pending`, retry later same
   `brand_id` + url; no tight loop this turn.
3. Confirm fields + selected images with the user (widget / one question).
4. `finalize_scraped_product`.

### Stage 5 — Hand off

- Image ads → `omneky-image-ads` / `omneky-creative`
- Product video → `omneky-product-video`
- Launch → `omneky-launch-manage` (paused by default; Approve first)

## Failure boundaries

| Failure | Required response |
| --- | --- |
| Listing/category URL | Stop scrape; ask for a single PDP URL. |
| `status=pending` scrape | Later retry same args; no tight poll. |
| User asks to delete product | Explain no public delete tool. |
| Ambiguous update fields | `request_user_decision` / Approve; no silent overwrite. |
| Missing imagery for later gen | Tell user before creative handoff; do not pretend assets exist. |
| Auth / brand errors | `omneky-failure-modes` / `omneky-getting-started`. |

## Sibling map

| Need | Skill |
| --- | --- |
| URL import detail | `omneky-product-import` |
| Image/video from product | `omneky-creative` / `omneky-image-ads` / `omneky-product-video` |
| Launch product ads | `omneky-launch-manage` |
| Failures / pending scrape | `omneky-failure-modes` |

## Tool alias notes

Prefer canonical names when both appear on `tools/list`:

- `get_product_details` (also accepted: `fetch_product_details`)
- `upsert_brand_product` (also accepted: `update_brand_product`)
- `finalize_scraped_product` for scrape drafts (not upsert)
