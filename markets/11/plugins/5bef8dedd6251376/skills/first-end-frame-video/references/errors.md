# Error Handling

## MCP Connection Layer

| Symptom | Cause | Handling |
| --- | --- | --- |
| No `mcp__selfyz_ai` namespace in the tool list | **Most often OAuth login has not been completed** (a server that is not logged in does not register its entire namespace); rarely, the plugin is not enabled | Run `codex mcp login selfyz-ai` yourself (not the user), read the plain `https://` authorization URL it prints, and give the user only that URL as a plain clickable link -- do not lead with the unreliable `codex://mcp/login?server=selfyz-ai` deep link; then **open a new conversation** and retry; see `references/auth.md` |
| `mcp__selfyz_ai` exists, but it has no `i2v_*` tools | Server version is too old | Confirm that the gx-mcp service has been updated to a version containing this mode; use `codex mcp get` to see which deployment the url points to |
| Call returns 401 / says not logged in | Token expired or revoked | Run `codex mcp logout selfyz-ai` then `codex mcp login selfyz-ai` yourself, relay the newly printed `https://` login URL to the user the same way (not the `codex://` deep link), then open a new conversation and retry |
| Connection refused / timeout | The service pointed to by the url in `.mcp.json` is not running | Run `python -m gx_mcp --port 8000` locally, or change the url to the online domain |

## Parameter Validation Errors (Server Rejects Directly, No Credits Charged)

| Error | Cause | Handling |
| --- | --- | --- |
| `Nonexistent image-to-video model X` | `model` was passed incorrectly | Call `i2v_list_models` again and use the exact `model` value |
| `Unsupported parameter combination` | The mode/quality/duration/audio combination is not in the template | Check `combinations` from `i2v_list_models` and use only combinations that appear there |
| `Unsupported aspect ratio X` | `ratio` is not in the model's `ratios` | Switch to a ratio supported by the model and recrop the images using the new ratio |
| `Prompt too long` | Exceeds `prompt_limit_length` | Shorten the prompt and retry |
| `image_urls cannot be empty` | Forgot to upload images first | Run `create_upload_url` + curl upload first |
| `Model X does not support fixed first/end frames` | Two images were passed but the model does not support them | Switch to a model from `i2v_list_models(end_frame=true)`, or pass only one image |
| `free ratio is not supported in fixed first/end-frame mode` | Two images + `ratio=free` | Use a fixed ratio (such as `9:16`) and crop both images to the same ratio |
| `image_urls supports at most two images` | Passed 3 or more images | Pass 1 image for single-image generation, and 2 images for first/end-frame generation |

## Upstream Business Error Codes

When a tool throws an error, the error message usually includes the upstream code and traceId.

| code | Meaning | Handling |
| --- | --- | --- |
| `1001` | Missing request header | Server configuration issue (`GX_ALGO_SIGN_KEY` / `GX_CLIENT_*` not fully configured); report to the service maintainer |
| `1009` | Signature invalid or expired | Server `GX_ALGO_SIGN_KEY` does not match `GX_CLIENT_CP` / `GX_CLIENT_PLATFORM` / `GX_CLIENT_VERSION`, or machine time drift is too large |
| `Task X was not found` | Task does not exist or was deleted | `task_id` is wrong or the task has expired; confirm with the user and start again |
| `10001` | Not logged in | Run OAuth login again |
| `4011` | Confirmed credits no longer match the server price (pricing changed after the quote) | Nothing was charged; run `i2v_get_options` again, tell the user the new `credit_cost`, and resubmit only after confirmation |
| Other | Business failure (insufficient credits, non-compliant material, etc.) | Relay the upstream `message` field verbatim to the user |

If `i2v_create_task` fails with a message saying the feature `is available to accounts with an
active` membership, the account is not a member. Nothing was created and no credits were charged.
Tell the user this feature is not included in their current account. Only if the user asks about
plans, share the informational `pricing_url` contained in the error message (or call `get_pricing_url`, when that tool is available, to fetch it). Retry only after the user says their account status has changed
and `get_user_profile()` reports `is_member: true`. If the membership lookup itself fails, relay the upstream error; do not retry the
create call in a loop.

When credits are insufficient, use the `credit` field from `get_user_profile()` to confirm the
balance, and tell the user the required credits and the current balance. No task was created and
no credits were charged. If the user asks about plans or credit options, call `get_pricing_url` (when that tool is
available) and share the returned informational `pricing_url`; do not construct the link yourself.

When reporting an error, include the `traceId` as well to help server-side troubleshooting.

## Task-Level Failures

- `task_status == "fail"`: relay `task_reason` verbatim. Common causes are non-compliant image content,
  unclear faces, or prompt violations. Retrying re-submits at the normal price--failed credits
  are refunded automatically, and since this is disclosed up front, no fresh price
  confirmation is needed; just suggest adjusting the images or prompt before trying again.
- Still incomplete after the polling limit (about 15 minutes): do not wait forever. Tell the user the current status
  and `task_id`, and let them continue querying later with `i2v_get_task`. The task is still running on the server;
  there is no need to resubmit.

## Material-Related Issues

- Upload API returns `c != 200`: relay `m` to the user. Common causes are oversized files or unsupported formats.
- File URL expired (temporary storage was cleaned up): upload again before starting the task.
- Incorrect size after cropping: verify with `sips -g pixelWidth -g pixelHeight <file>`, and confirm the width/height
  order in the command was not reversed (`sips --cropToHeightWidth` is **height first, then width**).

## Pitfalls Specific to First/End Frames

| Symptom | Cause | Handling |
| --- | --- | --- |
| The finished video direction is reversed (changes from end frame to first frame) | `image_urls` order was reversed | The order must be `[first frame, end frame]`; resubmit (this re-bills at the normal price; no need to reconfirm since it was disclosed up front) |
| Returned `end_frame` is `false` | Only one image was passed | Check whether the end-frame URL was omitted, or whether one image upload failed and produced an empty value |
| The transition jumps or composition changes abruptly | The two images do not have the same crop ratio or size | Redo both images with the same crop parameters, verify pixel dimensions are exactly identical, then upload again |
| The transition is stiff or does not look like the same scene | The first and end frames differ too much | This is a material issue. Suggest that the user use two more similar images, or specify the transition method in the prompt |
| A prompt was written but the effect is not obvious | The prompt only describes a single-frame image | Change it to describe "how the first frame changes into the end frame", referencing the model's `fixed_end_frame_prompt_hint` |

## Preview Download Failure

The finished video is an SelfyzAI temporary remote URL. Codex cannot embed-preview it; it must first `curl` the file
locally before delivery (see "Showing the Artifact" in SKILL.md). Downloads may fail for the following reasons:

| Symptom | Handling |
| --- | --- |
| curl returns non-0 or file size is 0 | Retry once; if it still fails, give the remote URL to the user, state that preview download failed, and do not pretend it was delivered |
| HTTP 403 / 404 | URL has expired or been cleaned up; call `i2v_get_task` again to obtain the latest URL |
| File downloads but cannot play | Check whether it downloaded an HTML error page (`file` command shows the type); if so, obtain the URL again |
