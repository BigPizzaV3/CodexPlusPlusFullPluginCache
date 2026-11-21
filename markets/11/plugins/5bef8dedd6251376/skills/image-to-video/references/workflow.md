# Tool return fields

The `i2v_*` tools also have a `kind` parameter (default `"image"`). This skill uses `kind="image"`;
**keep the default and do not pass this parameter**.

All tools parse `userId` from the access token; **they neither accept nor need a caller-supplied user
identifier**. The billing credential `example` is selected internally by the server according to the
parameter combination and forwarded; **it does not appear in any return value**.

## `i2v_list_models(end_frame=false)`

```jsonc
{
  "end_frame_only": false,
  "count": 3,
  "models": [
    {
      "model": "Model identifier; use it in all later calls",
      "model_name": "Display name",
      "model_desc": "Capability description",
      "model_type": 1,
      "supports_fixed_end_frame": true,
      "qualities": [{ "value": 2, "display": "720P", "is_default": true }],
      "durations_sec": [4, 8],
      "modes": [{ "value": "fast", "display": "Fast", "is_default": true }],
      "ratios": ["free", "9:16", "16:9"],
      "default_ratio": "9:16",
      "movement_amplitudes": [{ "value": "auto", "display": "Auto", "is_default": true }],
      "supports_audio": false,
      "required_image_count": 1,
      "optional_image_count": 1,
      "prompt_limit_length": 1500,
      "prompt_hint": "Upstream guidance for writing prompts",
      "fixed_end_frame_prompt_hint": "Prompt-writing guidance for fixed first/end-frame scenarios",
      "combinations": [
        { "mode": "fast", "quality": 2, "quality_display": "720P",
          "duration": 4, "audio": false, "credit": 30 }
      ]
    }
  ]
}
```

`combinations` is the **only trusted source for parameter combinations**: submitting a combination
not in the list will certainly fail.

## `i2v_get_options(model, quality?, duration?, mode?, audio?, ratio?, end_frame?)`

```jsonc
{
  "model": "...",
  "quality": 2,
  "duration_sec": 4,
  "mode": "fast",
  "audio": false,
  "ratio": "9:16",
  "credit_cost": 30,
  "image_count": 1,
  "image_role": ["First frame"],
  "crop": {
    "ratio": "9:16",
    "crop_required": true,
    "target_width": 720,
    "target_height": 1280,
    "strategy": "First center-crop to the target aspect ratio, then scale to target_width x target_height",
    "hint": "Example local cropping command"
  },
  "prompt_limit_length": 1500,
  "prompt_hint": "...",
  "next_step": "..."
}
```

When parameters are passed as `null` / omitted, they fall back to model defaults. The returned values
are the **final effective values**, and both quote and submission must use them.

When `crop.crop_required` is `false` (ratio is `free`), no cropping is needed; upload the original
image directly.

## `create_upload_url()`

```jsonc
{
  "upload_url": "...",
  "method": "POST",
  "content_type": "multipart/form-data",
  "form_field": "file",
  "headers": { "X-Client-Sn": "..." },
  "response_hint": "Upstream returns {c, m, d, traceId}: c=200 means success, and d is the complete file URL"
}
```

The form field name is fixed as `file`; upload one file at a time.

## `i2v_create_task(...)`

```jsonc
{
  "task_id": "Task ID; use it for later polling",
  "task_status": "Initial status at submission time",
  "model": "...",
  "end_frame": false,
  "quality": 2,
  "duration_sec": 4,
  "mode": "fast",
  "ratio": "9:16",
  "credit_cost": 30,
  "next_step": "..."
}
```

`end_frame` is inferred by the server from the length of `image_urls`: 1 image means the single-image
workflow, and 2 images means fixed first/end-frame.

Before submission, the server validates that the model exists, the ratio is supported, the parameter
combination matches a billing template, and the prompt is not too long. Fixed first/end-frame also
adds validations that the model supports the capability, the ratio is not `free`, and exactly two
images were provided.

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

When `finished` is `false`, continue polling; when it is `true`, branch according to `task_status`.

## Relationship between parameters and billing templates

`quality` / `duration` / `mode` / `audio` **do not directly enter the upstream request body**. Their
only role is to locate a template in the model's billing-template list and extract the billing
credential to send with the request. Therefore:

- The four dimensions must form a combination that exists in `combinations`; otherwise the server
  reports "Unsupported parameter combination"
- Changing any dimension may change the credit cost, so after changing one you must run
  `i2v_get_options` again for a quote
