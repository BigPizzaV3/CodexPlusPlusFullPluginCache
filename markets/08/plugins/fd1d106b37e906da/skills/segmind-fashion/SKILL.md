---
name: segmind-fashion
description: >
  Produce fashion and apparel imagery with Segmind — virtual try-on, flat-lay
  and packshot photography, mannequin-to-model, model or fabric swaps, lookbook
  and e-commerce product shots, and fashion showcase video. Use when the subject
  is clothing, accessories, or a person wearing them for a catalogue, storefront,
  lookbook, or ad. Do not use for general product photography of non-apparel
  goods, for portrait retouching unrelated to garments, or for face swapping
  (that is segmind-faceswap).
---

# Fashion imagery with Segmind

Read [pixelflow-contract](references/pixelflow-contract.md) and
[inference-contract](references/inference-contract.md) first.

Fashion is the densest corner of the Pixelflow catalogue — and one of the most
broken. **Verify a flow's chain before offering it** (contract rule 4); several
of the most obviously-named flows are dead.

## Verified working

| Flow | Inputs | Output | Notes |
|---|---|---|---|
| `flat-lay-studio` | `garment`, `prompt` | `image_out` | Our packaged flow. Single node, so the fewest failure points. **The safe default.** |
| `ai-flat-lay-tryon` | `cloth_image`, `prompt` | `image_output` | The public flow it is based on. **Measured working** — returned a 1.9MB PNG. |
| `ai-flat-lay-clothing-photography` | — | — | Same single-node shape; run `get_pixelflow_spec` for its keys. |

Single-node flows are the reliable ones here: fewer links, less to have rotted.

## Known broken — do not offer

| Flow | Why |
|---|---|
| `ai-virtual-try-on` | Chains `furniture-staging`, which no longer exists. |
| `qwen-image-edit-virtual-try-on` | **Measured failing** — its `llama4-scout-instruct-basic` node returns 400, even though every model in the chain is still listed in the catalogue. |
| `segfit-fashion-video-generator` | Chains `segfit`, retired. |
| `fashion-video-generator-seedance1lite-segfit` | Chains `seedance-v1-lite-image-to-video`, retired. |

The second row is the important one: **every model being listed is not proof the
flow runs.** Listing membership is a floor, not a guarantee.

## Worth checking before use

`ai-fashion-model-swap`, `ai-mannequin-to-model`, `wan2.2-fashion-video-generator`,
`professional-fashion-photoshoot-headshot-ai`, `ai-rotating-fashion-showcase-video-maker`
all pass the chain check but are unverified by a real run. Run
`get_pixelflow_spec`, tell the user it is untested, and try it on one image
before committing to a set.

## Direct models when no flow fits

A flow is a convenience, not a requirement. For garment edits on an existing
photo, `nano-banana-2`, `seedream-5-pro` or `qwen-image-edit-plus-*` via
`run_inference` are faster and cheaper than a multi-node flow, and they fail
more legibly.

## Workflow

1. **Get a URL** for the garment or model photo — a local file goes through
   `upload_media` first (contract rule 4).
2. **Pick a verified flow**, or a direct model. If the user names a broken one,
   say it is broken and offer the working alternative.
3. **`get_pixelflow_spec`** — fashion flows have the least guessable input names
   in the catalogue (`Model_Image`, `select_clothing_in_reference_image`,
   `cloth_image`).
4. **One image first**, then the set. Fashion requests are almost always "and
   now the other twelve SKUs"; get the look agreed on one before fanning out.
5. **Submit, then poll in this turn** until it finishes, and deliver the
   `images.segmind.com` URL in the same reply.

## Rules

1. **Never offer a flow without checking its chain.** ~10% of the published
   catalogue chains a model that no longer exists.
2. **One garment first.** Then batch.
3. **Prefer single-node flows** for anything client-facing — fewer failure points.
4. **Do not photograph a real person into clothing they did not wear** and
   present it as a real photo. Catalogue and mockup use is fine; a real named
   individual needs their consent.
5. **Segmind models only** — no local image tooling, no other services.
