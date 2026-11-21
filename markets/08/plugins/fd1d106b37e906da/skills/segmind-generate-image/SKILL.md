---
name: segmind-generate-image
description: >
  Generate or edit a still image with Segmind. Use when the user wants a picture
  made from a prompt — a product shot, poster, logo, illustration, concept art,
  ad creative, thumbnail — or wants an existing image changed: restyled,
  relit, background swapped or removed, an object erased or added, text
  corrected, a face swapped, or upscaled. Also use for a series of related
  images (variations, a set of ad sizes, a storyboard's frames). Do not use for
  video or animation, for audio, or when the user only wants advice on which
  model to use.
---

# Generate an image with Segmind

Images are the fast path: one `run_inference` call, output inline, seconds not
minutes. Read [inference-contract](references/inference-contract.md) first —
especially rule 4 on inputs and rule 3 on cost.

## Workflow

### 1. Settle the model

If the user named a model, use it. Otherwise pick one — `segmind-pick-model` has
the routing table, or use the shortlist below and move on. Do not spend three
tool calls choosing a model for a $0.01 generation.

| The job | Start here | Why |
|---|---|---|
| Photoreal product / lifestyle shot | `nano-banana-2`, `seedream-5-pro` | Strong realism, fast |
| Anything with readable text in the image | `ideogram-4`, `qwen-image-3`, `gpt-image-2` | Text rendering is a distinct capability |
| Cheap / high-volume / drafts | `p-image`, `z-image-turbo` | ~$0.005, sub-10s |
| Editing an existing image | `p-image-edit`, `nano-banana-2`, `seedream-4.5` | Take an image list, preserve the untouched parts |
| Transparent cutout of one object | `bria-extract-object` | Returns a real alpha PNG |
| Resize one creative into many ad sizes | `smart-banner-resizer` | Recomposes rather than crops |

### 2. Read the spec, then call

`get_model_spec(slug)` for the model you settled on. Parameter names differ more
than you would expect — an edit model may want `image_urls` (a list),
`first_frame_url`, or `image` (a single string). Do not guess from another
model's schema.

```
run_inference(slug="p-image", params={"prompt": "..."})
```

Leave `timeout` alone unless the model's `latency` says otherwise. If the result
comes back `pending`, resume with `check_inference` — do not resubmit.

### 3. Write the prompt properly

The prompt is the parameter that decides quality, so spend the effort there
rather than on tuning seeds.

- Name the subject, the setting, the light, and the camera framing. "A red
  ceramic mug on a white studio backdrop, soft diffused light, straight-on
  product photo" beats "a mug".
- State what must **not** change on an edit: "change the mug to matte navy,
  keep the framing, lighting, and shadow identical."
- For in-image text, put the exact string in quotes and keep it short.
- Do not stuff quality tokens ("8k, masterpiece, trending on artstation") into
  modern models. They were a Stable-Diffusion-era habit and now mostly cost
  prompt budget.

Keep the `seed` fixed across a set when the user wants consistency, and vary it
when they asked for options.

### 4. Chain edits on the output URL

Every result carries an `https://images.segmind.com/...` URL. Feed it directly
into the next step's image parameter — generate, then edit, then upscale, all
without an upload. This is the supported composition pattern and it is why a
multi-step request does not need any local file handling.

### 5. Deliver

Hand back the hosted URL and, when the user is watching spend, the `cost` from
`metrics`. For a set, deliver them in a stable order and say which parameter you
varied.

## Rules

1. **Upload a local file, don't refuse it.** `upload_media` returns a hosted
   URL to pass as the input — see contract rule 4 for which of its two routes
   this host uses. Never tell a user their file cannot be
   used, and never downscale it into a `data:` URI to make a call fit. Note the
   uploaded URL is publicly fetchable — see contract rule 4.
2. **One image first, then the set.** When the user wants variations or multiple
   sizes, generate one, show it, and only fan out once the look is agreed.
   Fanning out first is how a $0.01 model becomes a $0.30 surprise.
3. **Never resubmit a `pending` job.** It is already running and already billed.
4. **On a 422, read the field name in the message**, fix that field, retry once.
   Never loop.
5. **Do not silently substitute a model.** If the chosen one errors, say which
   model failed and why before moving to the runner-up.
