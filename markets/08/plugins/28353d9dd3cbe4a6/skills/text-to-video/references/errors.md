# Error handling

## MCP connection layer

| Symptom | Cause | Handling |
| --- | --- | --- |
| The tool list has no `mcp__enkio` namespace | **Most often OAuth login has not been completed** (a server that is not logged in does not register its entire namespace); less often the plugin is not enabled | Run `codex mcp login enkio` yourself (not the user), read the plain `https://` authorization URL it prints, and give the user only that URL as a plain clickable link -- do not lead with the unreliable `codex://mcp/login?server=enkio` deep link; then **open a new conversation** and retry; see `references/auth.md` |
| `mcp__enkio` exists, but it has no `t2v_*` tools | Server version is too old | Confirm gx-mcp has been upgraded to a version that includes this mode; use `codex mcp get` to see which deployment the url points to |
| Calls return 401 / say not logged in | Token expired or revoked | Run `codex mcp logout enkio` then `codex mcp login enkio` yourself, relay the newly printed `https://` login URL to the user the same way (not the `codex://` deep link), then open a new conversation and retry |
| Connection refused / timeout | The service pointed to by `url` in `.mcp.json` is not started | Run `python -m gx_mcp --port 8000` locally, or change the url to the online domain |

## Parameter validation errors (rejected directly by the server; no credits charged)

| Error | Cause | Handling |
| --- | --- | --- |
| `Nonexistent text-to-video model X` | `model` is wrong, **or an image-to-video / reference-to-video model name was used with `t2v_*`** | Use `t2v_list_models` to get the accurate `model`; the three modes' models are not interchangeable |
| `Nonexistent image-to-video model X` | The reverse: a text-to-video model was passed to `i2v_*` | If the task is text-to-video, switch to the `t2v_*` tool group |
| `Text-to-video must provide prompt` | `prompt` is empty or only whitespace | Align on the visual content with the user, then write a complete prompt before submitting |
| `Text-to-video must specify a concrete aspect ratio; free cannot be used` | `ratio` was set to `free` | Choose a concrete ratio from the model's `ratios` (such as `16:9` / `9:16`) and confirm landscape/portrait with the user |
| `Unsupported aspect ratio X` | `ratio` is not in the model's `ratios` | Use an aspect ratio supported by the model |
| `No available aspect ratio configuration` | The upstream configuration for this model only provided the `free` ratio | Switch models; also report to the service maintainer so the upstream configuration can be checked |
| `Unsupported parameter combination` | The mode/quality/duration/audio combination is not in the template list | Check `combinations` and use only combinations that appear there |
| `Prompt is too long` | The prompt exceeds `prompt_limit_length` | Shorten the prompt and retry |
| Message says `image_urls` is not a valid parameter | Image-to-video inputs were mistakenly used with `t2v_create_task` | Remove that parameter; if images are truly required, switch to the `enkio:image-to-video` / `enkio:reference-to-video` skill |

## Upstream business error codes

When a tool throws, the error message usually includes the upstream code and traceId.

| code | Meaning | Handling |
| --- | --- | --- |
| `1001` | Missing request headers | Server configuration problem (`GX_ALGO_SIGN_KEY` / `GX_CLIENT_*` not fully configured); report it to the service maintainer |
| `1009` | Signature is invalid or expired | Server `GX_ALGO_SIGN_KEY` does not match `GX_CLIENT_CP` / `GX_CLIENT_PLATFORM` / `GX_CLIENT_VERSION`, or the machine clock is too far off |
| `Task X was not found` | Task does not exist or was deleted | `task_id` is wrong or the task has expired; confirm with the user and start again |
| `10001` | Not logged in | Run OAuth login again |
| `4011` | Confirmed credits no longer match the server price (pricing changed after the quote) | Nothing was charged; run `t2v_get_options` again, tell the user the new `credit_cost`, and resubmit only after confirmation |
| Other | Business failure (insufficient credits, prompt non-compliance, etc.) | Relay the upstream `message` field to the user as-is |

If `t2v_create_task` fails with a message saying the operation `requires an active membership`, the
user is not a member. Nothing was created and no credits were charged. Give the user the
`pricing_url` contained in the error message (or call `get_pricing_url` to fetch it) to open in a
browser, signed in with the same Wondershare account used to authorize this MCP, and purchase a
membership. Retry only after the user confirms the purchase and `get_user_profile()` reports
`is_member: true`. If the membership lookup itself fails, relay the upstream error; do not retry the
create call in a loop.

When credits are insufficient, use the `credit` field from `get_user_profile()` to confirm the
balance and tell the user to recharge: call `get_pricing_url` and give the user the returned
`pricing_url` to open in a browser, signed in with the same Wondershare account used to authorize
this MCP, to top up credits or upgrade the plan. Do not construct the pricing link yourself.

When reporting an error, include the `traceId` as well so the server can investigate.

## Task-level failures

- `task_status == "fail"`: relay `task_reason` as-is. The most common cause of text-to-video failure
  is **the prompt triggering content moderation** (real people, violence, adult content, etc.).
  Retrying re-submits at the normal price--failed credits are refunded automatically, and since
  this is disclosed up front, no fresh price confirmation is needed; just recommend rewriting
  the prompt to avoid sensitive wording before trying again.
- Polling still has not completed after the upper limit (about 15 minutes): do not wait forever. Tell
  the user the current status and `task_id`, and let them continue querying later with
  `t2v_get_task`. The task is still running on the server and does not need to be submitted again.

## Output not as expected

These cases are **not errors**. The task returns `success` normally, but the video differs from what
the user imagined:

| Symptom | Handling |
| --- | --- |
| Subject is wrong / elements are missing | The prompt lacks information; add subject, action, and scene details, then retry (this re-bills at the normal price; no need to reconfirm since it was disclosed up front) |
| The camera is static / there is no motion | The prompt did not specify camera movement; add phrases such as "slowly push in", "track sideways", or "aerial flyover", and you may also adjust `movement_amplitude` |
| Style or mood is wrong | Add lighting and style descriptions (cool tones, backlight, cinematic feel, animation style, etc.) |
| Composition is cropped strangely | The ratio was chosen incorrectly, such as using `9:16` for landscape content (or the reverse); retry with a different `ratio` |
| The same prompt produces completely different results twice | This is a model characteristic, not a fault; use `enkio:image-to-video` if the scene must be stable and controllable |
| User wants to reproduce the scene of an existing image | Text-to-video cannot do this; use `enkio:image-to-video` or `enkio:reference-to-video` |

## Preview download failed

The finished video is an Enkio temporary remote URL. Codex cannot embed-preview it; it must first be
downloaded locally with `curl` and then delivered (see "Showing artifacts" in SKILL.md). Downloads
may fail for these reasons:

| Symptom | Handling |
| --- | --- |
| curl returns non-zero or file size is 0 | Retry once; if it still fails, give the remote URL to the user, state that the preview download failed, and do not pretend it was delivered |
| HTTP 403 / 404 | The URL has expired or been cleaned up; call `t2v_get_task` again to get the latest URL |
| The file downloads but cannot be played | Check whether an HTML error page was downloaded instead (use the `file` command to inspect the type); if so, retrieve the URL again |
