# Tool Return Fields

Reference-image-to-video and image-to-video **share the same set of `i2v_*` tools**, distinguished by the
`kind` parameter:

- `kind="image"` (default): single-image-to-video / fixed first-end-frame video
- `kind="reference"`: reference-image-to-video (this skill)

**Every call in this skill except `i2v_get_task` must explicitly pass `kind="reference"`**. The two modes'
model lists come from different upstream fields and are not interchangeable.

All tools parse `userId` from the access token; they **do not accept and do not need the caller to pass a
user identifier**. The billing credential `example` is selected internally by the server according to the
parameter combination and passed through; **it never appears in any return value**.

## `i2v_list_models(kind="reference")`

```jsonc
{
  "kind": "reference",
  "end_frame_only": false,
  "count": 2,
  "models": [
    {
      "model": "Model identifier; use it in all later calls",
      "model_name": "Display name",
      "model_desc": "Capability description",
      "model_type": 2,
      "unlock_type": 0,
      "supports_fixed_end_frame": false,
      "qualities": [{ "value": 2, "display": "720P", "is_default": true }],
      "durations_sec": [4, 8],
      "modes": [{ "value": "fast", "display": "Fast", "is_default": true }],
      "ratios": ["9:16", "16:9"],
      "default_ratio": "9:16",
      "movement_amplitudes": [{ "value": "auto", "display": "Auto", "is_default": true }],
      "supports_audio": false,
      "required_image_count": 2,
      "optional_image_count": 1,
      "min_image_count": 2,
      "max_image_count": 3,
      "prompt_limit_length": 1200,
      "prompt_hint": "Upstream prompt-writing hint",
      "prompt_guide_url": "Upstream prompt guide page; you may paraphrase it for the user",
      "combinations": [
        { "mode": "fast", "quality": 2, "quality_display": "720P",
          "duration": 4, "audio": false, "credit": 45 }
      ]
    }
  ]
}
```

- `min_image_count` / `max_image_count` is the **reference-image count range actually validated by the
  server**, derived from upstream `requiredCount` + `optionalCount`, with an upper limit of 3 images.
- `combinations` is the **only trustworthy source of parameter combinations**: combinations not in the list
  will definitely fail on submission.
- Passing `end_frame=true` with `kind="reference"` will error--reference-image-to-video has no fixed
  first/end frame mode.

## `i2v_get_options(model, kind="reference", quality?, duration?, mode?, audio?, ratio?)`

```jsonc
{
  "model": "...",
  "kind": "reference",
  "quality": 2,
  "duration_sec": 4,
  "mode": "fast",
  "audio": false,
  "ratio": "9:16",
  "credit_cost": 45,
  "image_count": { "min": 2, "max": 3 },
  "image_role": ["Reference image 1", "Reference image 2", "Reference image 3"],
  "crop": {
    "ratio": "9:16",
    "crop_required": true,
    "target_width": 720,
    "target_height": 1280,
    "strategy": "First center-crop to the target aspect ratio, then scale to target_width x target_height",
    "hint": "Local cropping command example"
  },
  "prompt_required": true,
  "prompt_limit_length": 1200,
  "prompt_hint": "...",
  "prompt_guide_url": "...",
  "next_step": "..."
}
```

Note that with `kind="reference"`, `image_count` is a **range object** (`{min, max}`), while with
`kind="image"` it is an integer--their structures differ; do not reuse parsing logic between them.

When parameters are `null` / omitted, they fall back to the model defaults. The returned values are the
**final effective values**, and both quoting and submission must use them.

When `crop.crop_required` is `false` (ratio is `free`), no cropping is needed; upload the original images
directly. **The same batch of reference images must all be cropped to the same ratio**.

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

The form field name is fixed as `file`, and one file is uploaded per request. **Call it once for each
reference image**, and collect the returned URLs in order.

## `i2v_create_task(model, kind="reference", image_urls, prompt, ...)`

```jsonc
{
  "task_id": "Task ID; use it for later polling",
  "task_status": "Initial status at submission time",
  "model": "...",
  "kind": "reference",
  "end_frame": false,
  "image_count": 2,
  "quality": 2,
  "duration_sec": 4,
  "mode": "fast",
  "ratio": "9:16",
  "credit_cost": 45,
  "next_step": "..."
}
```

Under `kind="reference"`, `end_frame` is **always `false`**: two reference images are not treated as first
and end frames; image count validation uses the `min_image_count`~`max_image_count` range.

Before submission, the server validates: the model exists in the reference-image-to-video list, the ratio is
supported, the parameter combination matches a billing template, the reference image count is within range,
`prompt` is non-empty, and the prompt is not too long. If any condition is not met, the request is rejected
directly and **no credits are charged**.

## `i2v_get_task(task_id)`

```jsonc
{
  "task_id": "...",
  "task_status": "success | fail | other (queued/generating)",
  "task_reason": "Failure reason; null on success",
  "video_url": "Finished video URL; null before completion",
  "finished": true,
  "status_legend": "success-success, fail-failure, other values mean queued or generating and require continued polling"
}
```

The query interface is fully shared by both modes and **does not require `kind`**. When `finished` is
`false`, continue polling; when `finished` is `true`, branch according to `task_status`.

## Relationship Between Parameters and Billing Templates

`quality` / `duration` / `mode` / `audio` **do not directly enter the upstream request body**. Their only
purpose is to locate a template in the model's billing template list and extract the billing credential to send
with the request. Therefore:

- The four dimensions must form a combination that exists in `combinations`; otherwise the server reports
  "unsupported parameter combination"
- Changing any dimension may change the credit cost; after changing it, run `i2v_get_options` again for a quote

## Relationship Between Reference Images and the Prompt

The **order** of `image_urls` is the numbering of reference images 1/2/3. The upstream service does not
accept any role-label field and does not support reference syntax such as `@1` / `{img1}`. The combination
relationship among reference images **can only be made clear through natural language in `prompt`**.
Therefore:

- Before submission, understand what each image is and write it into the prompt
- Changing the image order changes the semantics, so the prompt must be updated at the same time
- Replacing images without changing the prompt usually will not produce the expected result
