# Tool Return Fields

Image generation uses an **independent set of `any2i_*` tools** that is not shared with any video
workflow:

| Workflow | Tool group | Task identifier | Result field |
| --- | --- | --- | --- |
| Single-image-to-video / fixed first and last frames | `i2v_*` (`kind="image"`) | `task_id` | `video_url` |
| Reference-image-to-video | `i2v_*` (`kind="reference"`) | `task_id` | `video_url` |
| Text-to-video | `t2v_*` | `task_id` | `video_url` |
| Image generation (this skill) | `any2i_*` | **`job_id`** | **`image_urls[]`** |

Image generation and video generation share the same upstream task service, but their models, billing,
and result shapes differ: image tasks are identified by `job_id` and return `image_urls[]`. Always poll
an image task with `any2i_get_task`, and a video task with its own video query tool.

All tools derive `userId` from the access token; **they neither accept nor need the caller to pass a
user identifier**. The billing credential `example` is internally selected by the server according to
quality and passed through; **it does not appear in any return value**.

## `any2i_list_models()`

```jsonc
{
  "count": 2,
  "models": [
    {
      "model": "Model identifier; use it for all subsequent calls",
      "model_name": "Display name",
      "model_desc": "Capability description",
      "model_type": 7,
      "unlock_type": 0,
      "qualities": [{ "value": 1, "display": "1K", "is_default": true }],
      "ratios": ["9:16", "1:1", "free"],
      "default_ratio": "9:16",
      "min_image_count": 1,
      "max_image_count": 3,
      "accepts_images": true,
      "requires_images": true,
      "prompt_limit_length": 1500,
      "prompt_hint": "Upstream guidance on writing prompts",
      "prompt_guide_url": "Upstream prompt guide page; you may paraphrase it to the user",
      "credits": [
        { "quality": 1, "quality_display": "1K", "is_default": true, "credit": 10 },
        { "quality": 2, "quality_display": "2K", "credit": 25 }
      ]
    }
  ]
}
```

- `min_image_count` / `max_image_count` are the **input-image count interval actually validated by
  the server**:
  - `min == 0`: images may be omitted, i.e. text-to-image
  - `max == 0`: the model **does not accept any input images**; passing them will be rejected
  - Both > 0: images are required, i.e. image-to-image
- `credits` is the **only trustworthy pricing source**, and it is tiered only by quality--image
  generation does not have the video-style combined dimensions of "mode + duration + audio".
- The response **does not contain** `durations_sec` / `modes` / `supports_audio` /
  `movement_amplitudes`: the upstream model structure is shared with video and may carry these fields,
  but image generation does not use any of them; showing them only misleads users.

## `any2i_get_options(model, quality?, ratio?)`

```jsonc
{
  "model": "...",
  "model_name": "...",
  "quality": 2,
  "ratio": "9:16",
  "credit_cost": 25,
  "image_count": { "min": 1, "max": 3 },
  "accepts_images": true,
  "requires_images": true,
  "crop": {
    "ratio": "9:16",
    "crop_required": true,
    "target_width": 720,
    "target_height": 1280,
    "strategy": "First center-crop to the target aspect ratio, then scale to target_width × target_height",
    "hint": "Example local crop command"
  },
  "prompt_required": true,
  "prompt_limit_length": 1500,
  "prompt_hint": "...",
  "prompt_guide_url": "...",
  "next_step": "..."
}
```

When parameters are passed as `null` / omitted, they fall back to the model defaults. The values in
the response are the **final effective values**, and both quoting and submission should be based on
them.

When `crop.crop_required` is `false` (ratio is `free`), no cropping is required; upload the original
images directly. **The same batch of input images must be cropped to the same ratio**.

## `create_upload_url()`

```jsonc
{
  "upload_url": "...",
  "method": "POST",
  "content_type": "multipart/form-data",
  "form_field": "file",
  "headers": { "X-Client-Sn": "..." },
  "response_hint": "Upstream returns {c, m, d, traceId}: c=200 means success, and d is the full file URL"
}
```

The form field name is fixed as `file`, and one request uploads one file. **Call it once for each
input image**, and collect the returned URLs in order. Text-to-image does not use this tool at all.

## `any2i_create_task(model, prompt, image_urls?, quality?, ratio?)`

```jsonc
{
  "job_id": "Task ID for subsequent polling",
  "job_status": "Initial status at submission time",
  "model": "...",
  "image_count": 1,
  "quality": 2,
  "ratio": "9:16",
  "credit_cost": 25,
  "next_step": "Poll with any2i_get_task; after job_status=success, take image_urls"
}
```

Before submission, the server validates that: the model exists in the image-generation model list,
`prompt` is non-empty, the prompt is not too long, the ratio is supported, the input-image count falls
within the interval, and the quality matches a billing template. If any of these is not satisfied, the
server rejects the request directly and **does not charge credits**.

When `ratio` is `free`, the server **does not** send it upstream--`free` is only the convention for
"do not crop locally", not a real aspect ratio.

## `any2i_get_task(job_id)`

```jsonc
{
  "job_id": "...",
  "job_status": "success | fail | other (queued/generating)",
  "job_reason": "Failure reason; null on success",
  "image_urls": ["Finished image URL; possibly multiple; empty array until complete"],
  "image_count": 2,
  "mask_url": "Mask image returned by some workflows; usually null",
  "wait_time_sec": 0,
  "finished": true,
  "status_legend": "success-success, fail-failure, other values mean queued or generating and require continued polling"
}
```

The input parameter name is **`job_id`**. When `finished` is `false`, keep polling; when it is `true`,
branch according to `job_status`.

`image_urls` is an **array**, and on success it contains at least one image. During delivery, download
and show every image; do not take only the first one.

## Relationship between quality and billing templates

`quality` **does not go directly into the upstream request body**. Its purpose is to locate one
template in the model's billing-template list, then send the billing credential from that template
with the request. Therefore:

- `quality` must be a value that appears in `credits[].quality`, otherwise the server reports
  "Unsupported parameter combination"
- Changing quality changes credit consumption; after changing it, run `any2i_get_options` again for a
  quote
- Ratio, image count, and prompt length **do not participate** in template lookup, and therefore do
  not affect credits

## Boundary between text-to-image and image-to-image

These are not two tools, but two usages of the same tool set, determined by **model capability** rather
than by the caller:

- Model `min_image_count == 0` and no `image_urls` passed -> text-to-image
- `image_urls` passed -> image-to-image, and the count must fall within the interval

Before choosing a model, first confirm whether the user has images, so you do not choose a model that
requires images when no material is available, or a model that accepts no images when the user wants to
modify an image.
