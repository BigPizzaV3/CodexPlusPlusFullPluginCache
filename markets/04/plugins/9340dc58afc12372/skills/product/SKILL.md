---
name: product
description: Product imagery without a presenter — clean cutouts, white-background shots, lifestyle scenes, oversized hero showcases, jewelry video, and full marketplace listing sets for Amazon or Shopify. Use for any still or video of a physical product on its own. Not for a person presenting it (use UGC Ads) and not for retouching an existing photo (use Retoucher).
---

# Product Studio

Read `references/recipes.md` for the prompt library and `references/models.md` before any
video call.

## Tokens

| Token | What it does |
|---|---|
| `/product-shot` | A generated scene around the product |
| `/white-bg` | Product cut out and placed on white |
| `/lifestyle` | Product in a real-world scene |
| `/giant` | Oversized, monumental hero |
| `/jewelry` `/watch` | Macro jewelry video |
| `/amazon-main` `/a-plus` `/listing` | Marketplace listing set |

## Truth gate — claims

- **The claims the user supplies are the complete allowlist.** Preserve each as written.
  Never strengthen, combine, or infer a new claim from them.
- **With no claims supplied**, write only about what is directly observable — materials,
  controls, how it is used, what is included.
- **No superlatives you cannot support** — "best", "revolutionary", "#1". They read as
  advertising and fail on review.
- **No comparison to a named competitor.**

## Getting the source

`request_image_upload` renders the upload widget and places URLs into context. Attached
files are never handed to this server — never call `user_upload` directly.

## Stills

| Request | Tool |
|---|---|
| Transparent cutout | `remove_background` |
| **White-background main image** | `remove_background`, **then** `generate_image` with that cutout as `image_url` and an explicit pure-white prompt — see `references/recipes.md`. `remove_background` alone returns **transparency, not white**. |
| One product into a described scene | `generate_image` with the product as `image_url` (image-to-image) |
| **Two or more** images reconciled into one frame | `composite_shoot` — `image_urls` requires **2+**, and a paid organization. Never for a single product. |
| Oversized hero | `generate_giant_product_showcase` |

## Jewelry

`generate_jewelry_video`. This category lives on **macro detail and controlled reflection**
— metal and stone read by how light moves across them, so motion matters more than
composition. Close beats wide. Gold tone, metal type and stone colour must match the real
piece; buyers return items that don't match the video.

## Marketplace listings

A listing is a **set**, not one image. Produce the whole set without checking in between.

1. **Main image** — product on pure white, filling most of the frame, **no props, no text,
   no badges**. Two steps: `remove_background` for the cutout, then `generate_image` with
   that cutout as `image_url` and the white-background prompt from `references/recipes.md`.
   The cutout alone is transparent, which is not a compliant main image.
2. **Secondaries** — 3–5 shots: angles, scale, detail, in-use. `generate_image` with the
   product as `image_url`. Use `composite_shoot` only when genuinely merging 2+ images.
3. **A+ modules** — `generate_carousel` for multi-panel story blocks.

Ask which marketplace only if unstated; main-image rules differ. If the user wants text on
the main image, say it risks rejection and put it on a secondary instead.

**Carousels bill per requested slide up front and a partial failure is not refunded.** If
fewer slides come back than asked, say so plainly rather than presenting a short deck.

## The rule that matters most

**Never alter the product.** Colour, shape, finish and included accessories must match what
actually ships. Restyle the scene, never the product. A shot that flatters but
misrepresents gets sellers suspended — it is a failure, not a success.

## Defaults

`1:1` for catalogue and marketplace, `4:5` for social, `16:9` for banners.

## Conventions

Never print `org_id`, `folder_id`, or raw asset uuids.

## When something fails

Read `references/errors.md`. Identify the kind of failure before responding: pending jobs
are waited on, technical errors retried at most twice, unsupported capabilities stated
plainly, safety refusals never routed around, and every material change disclosed.

## QA before delivery

Run `references/qa.md` before calling this finished. Inspect the actual output — never
claim quality you have not observed, and say plainly what you could not verify.
