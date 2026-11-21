# Error handling

## MCP connection layer

| Symptom | Cause | Handling |
| --- | --- | --- |
| The tool list has no `mcp__enkio` namespace | **Most often OAuth login has not been completed** (an unauthenticated server does not register the entire namespace); less often, the plugin is not enabled | Run `codex mcp login enkio` yourself (not the user), read the plain `https://` authorization URL it prints, and give the user only that URL as a plain clickable link -- do not lead with the unreliable `codex://mcp/login?server=enkio` deep link; then **open a new conversation** and retry; see `references/auth.md` |
| `mcp__enkio` exists, but it has no `i2v_*` tools | Server version is too old | Confirm the gx-mcp service has been upgraded to a version that includes this workflow; use `codex mcp get` to see which deployment the url points to |
| Call returns 401 / says not logged in | Token has expired or been revoked | Run `codex mcp logout enkio` then `codex mcp login enkio` yourself, relay the newly printed `https://` login URL to the user the same way (not the `codex://` deep link), then open a new conversation and retry |
| Connection refused / timeout | The service pointed to by the url in `.mcp.json` has not started | Run `python -m gx_mcp --port 8000` locally, or change the url to the online domain |

## Parameter validation errors (server rejects directly; no credits charged)

| Error | Cause | Handling |
| --- | --- | --- |
| `Nonexistent image-to-video model X` | Wrong `model` value | Call `i2v_list_models` again and use the exact `model` value |
| `Unsupported parameter combination` | The mode/quality/duration/audio combination is not in the template list | Check `combinations` from `i2v_list_models`; use only combinations that appear there |
| `Unsupported aspect ratio X` | `ratio` is not in the model's `ratios` | Switch to a ratio supported by the model, and crop the image again to the new ratio |
| `Prompt too long` | Exceeds `prompt_limit_length` | Shorten the prompt and retry |
| `image_urls cannot be empty` | Forgot to upload the image first | Run `create_upload_url` + curl upload first |
| `Model X does not support fixed first and end frames` | Two images were passed but the model does not support it | Switch to a model from `i2v_list_models(end_frame=true)`, or pass only one image |
| `free ratio is not supported in fixed first/end-frame mode` | Two images + `ratio=free` | Use a fixed ratio (such as `9:16`) and crop both images to the same ratio |
| `image_urls supports at most two images` | Three or more images were passed | Pass 1 image for the single-image workflow, or 2 images for the first/end-frame workflow |

## Upstream business error codes

When a tool throws an error, the error message usually includes the upstream code and traceId.

| code | Meaning | Handling |
| --- | --- | --- |
| `1001` | Missing request header | Server configuration issue (`GX_ALGO_SIGN_KEY` / `GX_CLIENT_*` not fully configured); report it to the service maintainer |
| `1009` | Signature is invalid or expired | Server `GX_ALGO_SIGN_KEY` does not match `GX_CLIENT_CP` / `GX_CLIENT_PLATFORM` / `GX_CLIENT_VERSION`, or the machine time is significantly off |
| `Task X was not found` | Task does not exist or was deleted | `task_id` is wrong or the task has expired; confirm with the user and start again |
| `10001` | Not logged in | Re-run OAuth login |
| `4011` | Confirmed credits no longer match the server price (pricing changed after the quote) | Nothing was charged; run `i2v_get_options` again, tell the user the new `credit_cost`, and resubmit only after confirmation |
| Other | Business failure (insufficient credits, non-compliant material, etc.) | Relay the upstream `message` field verbatim to the user |

If `i2v_create_task` fails with a message saying the operation `requires an active membership`, the
user is not a member. Nothing was created and no credits were charged. Give the user the
`pricing_url` contained in the error message (or call `get_pricing_url` to fetch it) to open in a
browser, signed in with the same Wondershare account used to authorize this MCP, and purchase a
membership. Retry only after the user confirms the purchase and `get_user_profile()` reports
`is_member: true`. If the membership lookup itself fails, relay the upstream error; do not retry the
create call in a loop.

When credits are insufficient, use the `credit` field from `get_user_profile()` to confirm the
balance and prompt the user to recharge: call `get_pricing_url` and give the user the returned
`pricing_url` to open in a browser, signed in with the same Wondershare account used to authorize
this MCP, to top up credits or upgrade the plan. Do not construct the pricing link yourself.

When reporting an error, include the `traceId` as well so the server side can investigate.

## Task-level failures

- `task_status == "fail"`: relay `task_reason` verbatim. Common causes include non-compliant image
  content, unclear faces, and policy-violating prompts. Retrying re-submits at the normal
  price--failed credits are refunded automatically, and since this is disclosed up front, no
  fresh price confirmation is needed; just suggest adjusting the image or prompt before
  trying again.
- Polling exceeds the upper limit (about 15 minutes) and is still not complete: do not wait
  forever. Tell the user the current status and `task_id`, and let them continue querying later with
  `i2v_get_task`. The task is still running on the server; no need to submit it again.

## Material-related issues

- Upload API returns `c != 200`: relay `m` to the user. Common causes are oversized files or
  unsupported formats.
- File URL expires (temporary storage was cleaned up): upload again before starting the task.
- Dimensions after cropping are wrong: recheck with `sips -g pixelWidth -g pixelHeight <file>`, and
  confirm that width and height in the command were not swapped (`sips --cropToHeightWidth` is
  **height first, width second**).

## Preview download failure

The finished video is an Enkio temporary remote URL. Codex cannot embed a preview, so you must first download it locally with `curl` before delivery (see "Displaying the
output" in SKILL.md). Downloads may fail for the following reasons:

| Symptom | Handling |
| --- | --- |
| curl returns non-0 or file size is 0 | Retry once; if it still fails, give the remote URL to the user, state that preview download failed, and do not pretend it was delivered |
| HTTP 403 / 404 | The URL has expired or been cleaned up; call `i2v_get_task` again to get the latest URL |
| File downloads but cannot play | Check whether an HTML error page was downloaded instead (use the `file` command to inspect type); if so, retrieve the URL again |
