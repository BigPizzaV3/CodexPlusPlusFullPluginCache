---
name: social
description: Content for feeds and channels — Instagram posts, multi-slide carousels, stories, YouTube thumbnails, video covers, and burned-in captions or subtitles. Use when the destination is a social platform or a video needs captions. Not for marketplace listing images (use Product Studio).
---

# Social Studio

Read `references/recipes.md` for the prompt library and destination sizing.

## Tokens

| Token | What it does |
|---|---|
| `/instagram` `/post` | Single feed post |
| `/carousel` | Multi-slide deck |
| `/story` | Vertical story graphic |
| `/thumbnail` `/cover` | YouTube thumbnail (16:9 only) |
| `/captions` `/subtitles` | Burn captions into an existing video |

## Truth gate — claims

- **The claims the user supplies are the complete allowlist.** Preserve each as written.
  Never strengthen, combine, or infer a new claim from them.
- **With no claims supplied**, write only about what is directly observable — materials,
  controls, how it is used, what is included.
- **No superlatives you cannot support** — "best", "revolutionary", "#1". They read as
  advertising and fail on review.
- **No comparison to a named competitor.**

## Posts and carousels

- Single post → `generate_instagram_post`
- Multi-slide → `generate_carousel`. The `prompt` is the **topic**, not a per-slide prompt
  — upstream plans each slide with an LLM. Pass `slides` for the count.
- A carousel about a specific product → pass `product_id`; it resolves the product photo
  itself. Don't hunt for a URL.

**Carousels bill per requested slide up front, and a partial failure is not refunded.** If
fewer slides come back than requested, say so plainly.

## Thumbnails

`generate_youtube_thumbnail` takes `title`, plus optional `channel_style` and
`subject_description`. **Know its real shape before promising anything:**

- **It is 16:9 only.** There is no aspect-ratio argument. **It cannot produce a vertical
  Shorts cover.** If the user asks for one, say so and offer a 16:9 thumbnail or a
  `generate_image` route at `9:16`.
- **It takes no reference image.** You cannot feed it the user's face. `subject_description`
  is *text*. If the user needs their own face preserved, this tool is the wrong route —
  use `generate_image` with their photo as `image_url`.
- **It deliberately renders no text**, because image models render letterforms poorly. It
  returns a striking image *plus text-overlay guidance*: 2–3 overlay options of 3–5 bold
  words, where to place them, and font suggestions.

**So a thumbnail from this tool is not finished.** Deliver the image and the overlay
guidance together, and say plainly that the text still needs adding. For a finished
thumbnail with exact text, hand off to the **Canva** skill, which adds it as editable
elements — that is the completion path this tool was designed for.

What makes a thumbnail work, for the prompt you write:

- **Readable at 120px wide.** Big subject, few elements, hard contrast.
- **Faces beat objects**, and a clear expression beats a neutral one.
- Keep suggested overlay copy to 3–4 words.


## Captions

1. **Identify the video.** `asset_id` must be a finished video **this server hosts** — from
   `list_assets`, or the last path segment of an `asset.imagine.art/processed/<uuid>` URL
   already in the conversation. **A link from anywhere else cannot be captioned.** Say so
   plainly rather than trying.
2. **Style.** Named one ("whisper captions") → straight to `generate_video_captions`.
   Named none → `select_caption_preset`, which also collects language, position and shadow.
3. Pass `preset` **verbatim** — the upstream match is exact, so recapitalising fails.

**Cost, said while they choose, not after:** animated ("dynamic") presets cost twice static
ones; cost scales per started minute and doubles again for 2K/4K sources.

Use region-qualified locales — `en-US`, not `en`. `translation_language` adds a surcharge.

## Defaults

`4:5` feed, `9:16` stories, `1:1` if they say square. Thumbnails are `16:9` only —
the tool has no other option.
5 slides for a carousel.

## Conventions

Never print `org_id`, `folder_id`, or raw asset uuids.

## When something fails

Read `references/errors.md`. Identify the kind of failure before responding: pending jobs
are waited on, technical errors retried at most twice, unsupported capabilities stated
plainly, safety refusals never routed around, and every material change disclosed.

## Inspect before generating

A request to change something that already exists is an **edit**, not a build. Find the
existing asset and modify it. Generate only what the requested change actually requires.

## QA before delivery

Run `references/qa.md` before calling this finished. Inspect the actual output — never
claim quality you have not observed, and say plainly what you could not verify.
