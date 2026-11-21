# Tool response fields

Text-to-video uses **an independent set of `t2v_*` tools** that are not interchangeable with the
`i2v_*` tools for image-to-video / reference image-to-video:

| Mode | Tool group | Requires images |
| --- | --- | --- |
| Single-image video / fixed first and last frame | `i2v_*` (`kind="image"`) | Yes |
| Reference image-to-video | `i2v_*` (`kind="reference"`) | Yes |
| Text-to-video (this skill) | `t2v_*` | **No** |

The model lists for the three modes come from different fields in the upstream combined API. Model
identifiers cannot be reused across modes.

All tools parse `userId` from the access token and **do not accept or require callers to pass a user
identifier**. The billing credential `example` is selected internally by the server according to the
parameter combination and forwarded through; **it does not appear in any response**.

## `t2v_list_models()`

```jsonc
{
  "count": 2,
  "models": [
    {
      "model": "Model identifier; use it in all later calls",
      "model_name": "Display name",
      "model_desc": "Capability description",
      "model_type": 3,
      "unlock_type": 0,
      "qualities": [{ "value": 2, "display": "720P", "is_default": true }],
      "durations_sec": [5, 10],
      "modes": [{ "value": "fast", "display": "Fast", "is_default": true }],
      "ratios": ["16:9", "9:16", "1:1"],
      "default_ratio": "16:9",
      "movement_amplitudes": [{ "value": "auto", "display": "Auto", "is_default": true }],
      "supports_audio": false,
      "prompt_limit_length": 800,
      "prompt_hint": "Upstream prompt-writing hint",
      "prompt_guide_url": "Upstream prompt guide page; you may summarize it for the user",
      "combinations": [
        { "mode": "fast", "quality": 2, "quality_display": "720P",
          "duration": 5, "audio": false, "credit": 30 }
      ]
    }
  ]
}
```

- The response **does not contain any image-related fields** (`image_count` / `crop` /
  `supports_fixed_end_frame`, etc.). Text-to-video does not accept assets, so these concepts do not
  apply.
- `ratios` **will not contain `free`**: text-to-video must resolve to a concrete aspect ratio.
- `combinations` is the **only trustworthy source of parameter combinations**: submitting a
  combination that is not in the list will certainly error.

## `t2v_get_options(model, quality?, duration?, mode?, audio?, ratio?)`

```jsonc
{
  "model": "...",
  "model_name": "...",
  "quality": 2,
  "duration_sec": 10,
  "mode": "fast",
  "audio": false,
  "ratio": "9:16",
  "credit_cost": 60,
  "prompt_required": true,
  "prompt_limit_length": 800,
  "prompt_hint": "...",
  "prompt_guide_url": "...",
  "next_step": "After confirming credits, submit directly with t2v_create_task; no assets need to be uploaded"
}
```

When parameters are passed as `null` or omitted, they fall back to the model defaults. The values in
the response are the **final effective values**, and both the quote and submission are based on them.

`ratio` fallback order: explicit input -> model `default_ratio` (non-`free`) -> the first available
value in `ratios`. If all are missing, the error is "No available aspect ratio configuration", which
means the upstream configuration for that model has a problem.

The response has no `crop` field because there is no cropping step.

## `t2v_create_task(model, prompt, ratio?, quality?, duration?, mode?, audio?, movement_amplitude?)`

```jsonc
{
  "task_id": "Task ID; use it for later polling",
  "task_status": "Initial status at submission time",
  "model": "...",
  "quality": 2,
  "duration_sec": 10,
  "mode": "fast",
  "ratio": "9:16",
  "credit_cost": 60,
  "next_step": "Poll with t2v_get_task; after task_status=success, retrieve video_url"
}
```

There is **no `image_urls` parameter**, and there are no `kind` / `end_frame` / `image_count` fields.

Before submission, the server validates that: the model exists in the text-to-video list, `prompt` is
not empty, the prompt is not too long, the aspect ratio is supported and not `free`, and the parameter
combination matches a billing template. If any of these conditions is not met, the request is rejected
directly and **no credits are charged**.

## `t2v_get_task(task_id)`

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

`quality` / `mode` / `audio` **do not directly enter the upstream request body**. Their role is to
locate one template in the model's billing template list, then extract the billing credential and
send it with the request. Therefore:

- The four dimensions must form a combination that exists in `combinations`; otherwise the server
  reports "Unsupported parameter combination".
- Changing any dimension may change the credit cost, so after changing one, call
  `t2v_get_options` again for a quote.

`duration` differs from image-to-video: it both participates in locating the billing template and is
**explicitly sent to the upstream service in the request body**, because there is no input image to
determine video length. Therefore, if `duration` is wrong, not only will the quote be inaccurate, the
finished video length will also be wrong.

## The prompt is the only input

In image-to-video, the prompt is "additional instructions"; in text-to-video, it is **everything**.
The upstream service receives no visual reference at all. Therefore:

- The more specific the prompt is (subject / action / scene / camera / lighting), the more
  controllable the result will be.
- Multiple generations from the same prompt will differ; this is a model characteristic, not a fault.
- If the user wants the video to match an existing image, this mode cannot do it; use
  `enkio:image-to-video` or `enkio:reference-to-video` instead.
