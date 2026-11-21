# Tool Return Fields

The `i2v_*` tools also have a `kind` parameter (default `"image"`). This skill uses `kind="image"`; **keep the default and do not pass this parameter**.

All tools derive `userId` from the access token. **They do not accept and do not require the caller to pass a user identifier**.
The billing credential `example` is internally selected and forwarded by the server according to the parameter combination;
**it does not appear in any return value**.

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
      "fixed_end_frame_prompt_hint": "Guidance for writing prompts in fixed first/end-frame scenarios",
      "combinations": [
        { "mode": "fast", "quality": 2, "quality_display": "720P",
          "duration": 4, "audio": false, "credit": 30 }
      ]
    }
  ]
}
```

`combinations` is the **only trustworthy source of parameter combinations**: submitting a combination that is not in
this list will inevitably error.

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
    "strategy": "Center-crop to the target aspect ratio first, then scale to target_width x target_height",
    "hint": "Example local crop command"
  },
  "prompt_limit_length": 1500,
  "prompt_hint": "...",
  "next_step": "..."
}
```

When parameters are passed as `null` / omitted, they fall back to the model defaults. The values returned are the
**final effective values**, and both quoting and submission must use them.

When `crop.crop_required` is `false` (ratio is `free`), no crop is required; upload the original image directly.

## `create_upload_url()`

```jsonc
{
  "upload_url": "...",
  "method": "POST",
  "content_type": "multipart/form-data",
  "form_field": "file",
  "headers": { "X-Client-Sn": "..." },
  "response_hint": "Upstream returns {c, m, d, traceId}: c=200 means success, d is the full file URL"
}
```

The form field name is fixed as `file`; upload one file at a time.

## `i2v_create_task(...)`

```jsonc
{
  "task_id": "Task ID, used for later polling",
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

`end_frame` is inferred by the server from the length of `image_urls`: 1 image means single-image generation,
2 images means fixed first/end frames.

Before submission, the server validates: model existence, supported ratio, whether the parameter combination matches
a billing template, and prompt length. Fixed first/end frames additionally validate that the model supports the capability,
the ratio is not `free`, and there are exactly two images.

## `i2v_get_task(task_id)`

```jsonc
{
  "task_id": "...",
  "task_status": "success | fail | other (queued/generating)",
  "task_reason": "Failure reason, null on success",
  "video_url": "Finished video URL, null before completion",
  "finished": true,
  "status_legend": "success-success, fail-failure, other values mean queued or generating and require continued polling"
}
```

When `finished` is `false`, continue polling; when it is `true`, branch according to `task_status`.

## Relationship Between Parameters and Billing Templates

`quality` / `duration` / `mode` / `audio` **do not directly enter the upstream request body**. Their only purpose
is to locate one template in the model's billing template list and send the billing credential from that template
with the request. Therefore:

- The four dimensions must form a combination that exists in `combinations`; otherwise the server reports
  "Unsupported parameter combination"
- Changing any dimension may change credit consumption, so after any change, run `i2v_get_options` again for a quote

## Extra Requirements for Fixed First/End Frames

Upstream uses **the same interface** for both single-image and first/end-frame generation. The only difference is the
length of `image_urls`:

| Mode | `image_urls` | `end_frame` returned by server |
| --- | --- | --- |
| Single-image video generation | `[first frame]` | `false` |
| Fixed first/end frames | `[first frame, end frame]` | `true` |

When two images are passed, the server additionally validates three things. If any one is not satisfied, it rejects
directly (no credits charged):

1. The model's `supports_fixed_end_frame` is `true`
2. `ratio` is not `free`
3. `image_urls` has exactly two elements

`i2v_list_models(end_frame=true)` prefilters unsupported models;
`i2v_get_options(..., end_frame=true)` prevalidates the ratio. Both are free before submission, so use them to block
problems before any credits are charged.

When `end_frame=true`, `i2v_get_options` returns `image_count` as 2 and `image_role` as
`["First frame", "End frame"]`, which can be used to confirm material order with the user.
