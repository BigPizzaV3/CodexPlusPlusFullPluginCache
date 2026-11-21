# Error Handling

## MCP connection layer

| Symptom | Cause | Handling |
| --- | --- | --- |
| The tool list has no `mcp__selfyz_ai` namespace | **Most often OAuth login has not been completed** (a server that is not logged in does not register its entire namespace); less commonly, the plugin is not enabled | Run `codex mcp login selfyz-ai` yourself (not the user), read the plain `https://` authorization URL it prints, and give the user only that URL as a plain clickable link -- do not lead with the unreliable `codex://mcp/login?server=selfyz-ai` deep link; then **open a new conversation** and retry; see `references/auth.md` |
| `mcp__selfyz_ai` exists, but it has no `any2i_*` tools | Server version is too old | Confirm the gx-mcp service has been updated to a version containing this workflow; use `codex mcp get` to see which deployment the url points to |
| Call returns 401 / says not logged in | Token expired or revoked | Run `codex mcp logout selfyz-ai` then `codex mcp login selfyz-ai` yourself, relay the newly printed `https://` login URL to the user the same way (not the `codex://` deep link), then open a new conversation and retry |
| Connection refused / timeout | The service pointed to by the url in `.mcp.json` is not running | Run `python -m gx_mcp --port 8000` locally, or change the url to the online domain |

## Wrong tool group (most common)

Image generation and video generation use different tool groups with different identifiers and
result fields:

| Error / Symptom | Cause | Handling |
| --- | --- | --- |
| `any2i_get_task` says parameter `job_id` is missing | You passed `task_id` instead | The input parameter name for image generation is `job_id` |
| Calling `i2v_get_task` / `t2v_get_task` with a `job_id` returns no `image_urls` | Wrong tool group | Image-generation tasks can only be queried with `any2i_get_task` |
| Calling `any2i_get_task` with a video `task_id` returns no `video_url` | Same issue, opposite direction | Video tasks use `i2v_get_task` / `t2v_get_task` |
| Expected `video_url` but got `image_urls` | You used the image-generation tool | Image generation outputs images; use the corresponding video skill if you need video |

## Parameter validation errors (rejected directly by the server, no charge)

| Error | Cause | Handling |
| --- | --- | --- |
| `Nonexistent image-generation model X` | The `model` is wrong, **or a video model name was used with `any2i_*`** | Use `any2i_list_models` to get the exact `model`; image-generation and video models are not interchangeable |
| `Image generation must provide prompt` | `prompt` is empty or only whitespace | Align with the user on what to draw, then write a complete prompt before submitting |
| `Model X requires N~M input images, currently K were provided` | The count is outside the interval | Add or remove images according to `image_count` from `any2i_get_options`; only `min=0` allows no image, and `max=0` means the model accepts no images |
| `Model X requires 0~0 input images` | `image_urls` was passed to a pure text-to-image model | Remove `image_urls`; if the user really wants to modify an image, switch to a model with `accepts_images=true` |
| `Unsupported aspect ratio X` | `ratio` is not in the model's `ratios` | Use a ratio supported by the model, and re-crop **all** input images to the new ratio |
| `Unsupported parameter combination` | `quality` is not in the model's billing template | Use only quality values that appear in `credits[].quality` |
| `Prompt too long` | Exceeds `prompt_limit_length` | Shorten the prompt and retry |

## Upstream business error codes

When a tool throws an error, the message usually includes the upstream code and traceId.

| code | Meaning | Handling |
| --- | --- | --- |
| `1001` | Missing request header | Server configuration problem (`GX_ALGO_SIGN_KEY` / `GX_CLIENT_*` not fully configured); report to the service maintainers |
| `1009` | Signature is invalid or expired | Server `GX_ALGO_SIGN_KEY` does not match `GX_CLIENT_CP` / `GX_CLIENT_PLATFORM` / `GX_CLIENT_VERSION`, or the machine clock drift is too large |
| `Task X was not found` | Task does not exist or was deleted | `job_id` is wrong or the task has expired; confirm with the user and start again |
| `10001` | Not logged in | Run OAuth login again |
| `4011` | Confirmed credits no longer match the server price (pricing changed after the quote) | Nothing was charged; run `any2i_get_options` again, tell the user the new `credit_cost`, and resubmit only after confirmation |
| Other | Business failure (insufficient credits, material or prompt non-compliance, etc.) | Pass the upstream `message` field to the user verbatim |

If `any2i_create_task` fails with a message saying the feature `is available to accounts with an
active` membership, the account is not a member. Nothing was created and no credits were charged.
Tell the user this feature is not included in their current account. Only if the user asks about
plans, share the informational `pricing_url` contained in the error message (or call `get_pricing_url`, when that tool is available, to fetch it). Retry only after the user says their account status has changed
and `get_user_profile()` reports `is_member: true`. If the membership lookup itself fails, relay the upstream error; do not retry the
create call in a loop.

When credits are insufficient, use the `credit` field from `get_user_profile()` to confirm the
balance, and tell the user the required credits and the current balance. No task was created and
no credits were charged. If the user asks about plans or credit options, call `get_pricing_url` (when that tool is
available) and share the returned informational `pricing_url`; do not construct the link yourself.

When reporting an error, include the `traceId` as well to make server-side troubleshooting easier.

## Task-level failures

- `job_status == "fail"`: pass `job_reason` through verbatim. The most common image-generation
  failure is **content review triggered by the prompt or input images** (real people, nudity,
  violence, etc.). Retrying re-submits at the normal price--failed credits are refunded
  automatically, and since this is disclosed up front, no fresh price confirmation is needed;
  just suggest rewriting the prompt or replacing the input images before trying again.
- Polling still has not completed after the limit (about 5 minutes): do not wait forever. Tell the
  user the current status and `job_id`, and let them continue querying later with `any2i_get_task`.
  The task is still running on the server; there is no need to submit again.

## Result does not meet expectations

These cases are **not errors**. The task returns `success` normally; the finished image simply differs
from what the user imagined:

| Symptom | Handling |
| --- | --- |
| Elements are missing in text-to-image output | The prompt lacks information; complete the subject, scene, composition, and style before retrying (this re-bills at the normal price; no need to reconfirm since it was disclosed up front) |
| Image-to-image changes the original image beyond recognition | The prompt was written as a "redraw"; rewrite it in the form "keep X, only change Y" and try again |
| Image-to-image barely changes anything | The prompt is too conservative; state the part to change more explicitly and strongly |
| Elements from multiple input images were not used | The prompt did not explain the role of each image; describe them in natural language by order and retry |
| The prompt contains references such as `@1` | Upstream does not support that syntax and treats it as plain text; replace it with natural-language references |
| Output resolution is insufficient | Increase `quality` (more expensive), and go through `any2i_get_options` again for a quote |
| Composition is cropped strangely | The ratio is wrong; change `ratio` and **re-crop all input images** before retrying |
| The same prompt gives different results twice | This is a model characteristic, not a failure |

## Material-related issues

- Upload endpoint returns `c != 200`: pass `m` to the user. Common causes are oversized files or
  unsupported formats.
- File URL expired (temporary storage was cleaned up): upload again before starting the task.
- Cropped dimensions are wrong: verify with `sips -g pixelWidth -g pixelHeight <file>`, and confirm
  that the width/height order in the command was not reversed (`sips --cropToHeightWidth` is
  **height first, then width**).
- Only some input images were cropped: all input images must be cropped to the **same** target size;
  the omitted image will skew the composition.

## Preview download failed

Finished images are SelfyzAI temporary remote URLs. Codex cannot embed-preview them; they must be
`curl`ed locally before delivery (see "Displaying artifacts" in SKILL.md). Downloads may fail for
the following reasons:

| Symptom | Handling |
| --- | --- |
| curl returns non-0 or file size is 0 | Retry once; if it still fails, give the user the remote URL and say preview download failed. Do not pretend it was delivered |
| HTTP 403 / 404 | The URL has expired or been cleaned up; call `any2i_get_task` again to fetch the latest URL |
| File downloads but cannot be opened | Check whether it downloaded an HTML error page (use the `file` command to inspect type); if so, fetch the URL again |
| `image_urls` has multiple images but only one was downloaded | Download and show every image; do not take only the first one |
