---
name: studio
description: Direct image, video and music generation, plus your asset library and credit balance, for requests no other ImagineArt skill covers. Use only as a last resort — fashion, products, ads, effects, social, motion, retouching, branding and interiors all have dedicated skills that handle those requests better.
---

# Studio

**This is the fallback.** It does not participate in automatic routing
(`allow_implicit_invocation: false`). Before using it, check whether a specific skill owns
the request — it almost always does.

| If the request is about | Use instead |
|---|---|
| A photo that should move | Effects |
| Clothing, models, lookbooks, runway | Fashion |
| A customer's own garment on a person | Try-On |
| A product with a presenter | UGC Ads |
| Product stills, listings, jewelry | Product Studio |
| Instagram, carousels, thumbnails, captions | Social Studio |
| Camera moves, drone, food video | Motion |
| Editing an existing image | Retoucher |
| Logos and identity | Brand Studio |
| Rooms and staging | Spaces |
| Music | Sound |
| Editable After Effects compositions or motion titles | After Effects |
| Premiere Pro timelines and exports | Premiere |
| Editable Blender scenes, materials, lighting or 3D animation | Blender |

## Tokens

| Token | What it does |
|---|---|
| `/assets` `/creations` | Browse past work |
| `/credits` `/balance` | Credit balance |
| *(none)* | Raw generation |

## Generation

- `generate_image` — text-to-image, or image-to-image when `image_url` is set
- `generate_video` — text-to-video, or image-to-video when `image_url` holds exactly one URL
- `generate_music` — audio

**Never guess a valid value** — but use the right source.

- **`generate_video` / `generate_image` durations and resolutions are per-model
  allow-lists**, documented on the tool itself and summarised in `references/models.md`.
- **`list_durations` and `list_resolutions` describe ad generation only.** They are inputs
  for `generate_ad`, not universal validators — do not use them to check a video model.
- `list_aspect_ratios`, `list_camera_angles`, `list_camera_movements` are general.

Model names must be passed exactly as written; a near-miss fails.

**Never omit `resolution`** — it defaults to the model's lowest tier.

## Library

| Request | Tool |
|---|---|
| Visual grid | `show_assets` with `org_id` |
| Rows to reason over | `list_assets` |
| Past generations | `list_user_creations` |
| Credit balance | `get_balance` |

`list_assets` takes `service`: `user` for uploads, `image,video` for generations, omitted
for everything including music and project assets. When a full page comes back there is a
next-page cursor — use it rather than saying that's all there is.

**The most common real reason to be here:** another skill needs an `asset_id`. Find it,
hand it over, continue. Never make the user copy a uuid.

## Finishing a generation

Where a widget renders, it polls itself. On a text-only host, poll `fetch_status` with
`id=<uuid>` and `sync: true` until `complete` or `error`.

## Paywall

Free organizations can only run `generate_image` on the default model. Relay refusals
verbatim; they carry the upgrade link.

## Conventions

Never print `org_id`, `folder_id`, or raw uuids — refer to assets by what they are and
when they were made.

## When something fails

Read `references/errors.md`. Identify the kind of failure before responding: pending jobs
are waited on, technical errors retried at most twice, unsupported capabilities stated
plainly, safety refusals never routed around, and every material change disclosed.

## QA before delivery

Run `references/qa.md` before calling this finished. Inspect the actual output — never
claim quality you have not observed, and say plainly what you could not verify.
