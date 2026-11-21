---
name: segmind-pick-model
description: >
  Choose a Segmind model, or answer a question about the catalog, before running
  anything. Use when the user asks which model to use, what a generation will
  cost, what is cheapest or fastest for a task, how many models exist, what
  Segmind supports for some modality, or names a capability without naming a
  model ("something that does virtual try-on"). Also use as the first step of any
  generation request where no model is pinned. Do not use when the user already
  named a slug and just wants it run.
---

# Pick a Segmind model

The catalog runs to 500-plus models across a dozen modalities and moves weekly —
read the live count off `total_catalog` rather than quoting a number from here.
Picking well is most of the value; the generation itself is one call. Read
[inference-contract](references/inference-contract.md) before any tool call.

## The shape of a good answer

One recommendation, one runner-up, and the reason — cost, speed, or a capability
the other one lacks. Not a table of nine models. The user asked what to use, not
for the catalog.

## Workflow

### 1. Narrow with one `list_models` call

Pass `category` whenever the modality is clear from the request, and `search`
for a capability word. Leave `sort` at its default (`popularity`) unless the
user's own words point elsewhere — "cheap" → `sort="cost"`, "fast" / "quick"
→ `sort="latency"`.

```
list_models(category="imageToVideo", limit=15)
```

Map the request to a category before searching. Getting this wrong is the most
common failure — a "make my photo move" request is `imageToVideo`, not
`textToVideo`.

| The user says | Category |
|---|---|
| make / draw / generate an image, poster, logo | `textToImage` **and** `imageToImage` — see below |
| edit, restyle, remove, replace, swap, upscale, try-on this image | `imageToImage` |
| animate this photo, make this image move | `imageToVideo` |
| make a video of / about | `textToVideo` |
| edit, extend, restyle, subtitle, or clean up this video | `videoToVideo` |
| voiceover, narration, TTS, music, sound effects | `textToAudio` |
| transcribe, caption, align | `audioToText` |
| 3D model / mesh from a photo | `imageTo3d` |

⚠️ **`textToImage` alone does not contain the best text-to-image models.** The
category records a model's *primary* listing, and several of the strongest
generators — `nano-banana-2`, `nano-banana-2.1`, `seedream-4.5` — are filed under
`imageToImage` because they also edit, even though their image input is optional
and they generate from a bare prompt perfectly well. A from-scratch image request
filtered to `textToImage` silently hides them. Search both, or search by
capability (`search="photoreal"`) and read each row's category rather than
filtering on it.

Answer "how many models…" questions from `total_catalog`, `total_matching` and
`by_category` — never by counting the returned page, which is capped and
`truncated` will say so.

### 2. Shortlist two or three, then `compare_models`

Cut the page to the two or three that plausibly fit, then:

```
compare_models(slugs=["seedance-1.5-pro", "wan-2.2-i2v-fast"])
```

This is the only source of real prices. If the user asked *anything* about cost,
this call is mandatory before you answer — a listing row's `average_cost` is
observed spend, not a price.

Watch `price_drivers` on the listing row. When it names a parameter
(`duration`, `generate_audio`, `resolution`), the price moves with the user's
own choices, and the comparison has to be read at the settings they want, not at
the default.

### 3. Recommend, then hand off

Name the model, give the price basis and the rough wait, and say what you would
run. Then continue into `segmind-generate-image` or `segmind-generate-video` —
do not stop and ask "shall I proceed?" when the user's original message already
asked for the output.

Call `get_model_spec` only for the model you are about to run.

## Rules

1. **`average_cost` is not a price.** It ranks candidates. `compare_models`
   prices them. This is the single easiest way to mislead a user about money.
2. **Recommend by fit, not by rank.** The most popular image model is not the
   right answer when the user needs legible in-image text (that is Ideogram /
   Qwen Image / Seedream territory) or a transparent cutout (`bria-extract-object`).
3. **Skip the internal plumbing.** Rows named "Utility node: …" (`timeline`,
   `video-split`) and the `utility-image-*` models are internal composition
   nodes, not products. Never recommend one.
4. **Do not read the whole catalog.** One filtered `list_models` call, then a
   shortlist. Fetching specs for every candidate is slow and buys nothing.
5. **Deprecated and coming-soon models are hidden by default.** Only pass
   `include_unavailable=True` when the user explicitly asks what was retired.
