# Error Handling

## MCP Connection Layer

| Symptom | Cause | Remedy |
| --- | --- | --- |
| `i2v_list_models` does not recognize the `kind` parameter | Server version is too old (before reference-image-to-video launched) | Upgrade the gx-mcp server and retry |
| No `mcp__enkio` namespace in the tool list | **Usually OAuth login has not been completed** (a server that is not logged in does not register its entire namespace); less commonly the plugin is not enabled | Run `codex mcp login enkio` yourself (not the user), read the plain `https://` authorization URL it prints, and give the user only that URL as a plain clickable link -- do not lead with the unreliable `codex://mcp/login?server=enkio` deep link; then **open a new conversation** and retry; see `references/auth.md` |
| `mcp__enkio` exists, but it has no `i2v_*` tools | Server version is too old | Confirm the gx-mcp service has been upgraded to a version that includes this mode; use `codex mcp get` to see which deployment the url points to |
| Call returns 401 / says not logged in | Token expired or was revoked | Run `codex mcp logout enkio` then `codex mcp login enkio` yourself, relay the newly printed `https://` login URL to the user the same way (not the `codex://` deep link), then open a new conversation and retry |
| Connection refused / timeout | The service pointed to by the url in `.mcp.json` is not running | Run `python -m gx_mcp --port 8000` locally, or change the url to the online domain |

## Parameter Validation Errors (Server Rejects Directly, No Charge)

| Error | Cause | Remedy |
| --- | --- | --- |
| `nonexistent reference-image-to-video model X` | Wrong `model`, **or you used a reference model but forgot `kind="reference"`** | First confirm every call includes `kind="reference"`, then use `i2v_list_models(kind="reference")` to get the exact `model` |
| `nonexistent image-to-video model X` | A reference model was passed while `kind` is the default `image` | Add `kind="reference"` |
| `model X requires N~M reference images, currently K were provided` | Reference image count is outside the allowed range | Add or remove images according to `image_count` from `i2v_get_options`; if insufficient, do not pad with unrelated images |
| `reference-image-to-video must provide prompt` | `prompt` is empty or whitespace-only | Confirm what each reference image represents with the user, write a complete prompt, then retry |
| `reference-image-to-video does not have fixed first/end frame mode` | `end_frame=true` was passed | Remove the parameter; if the user really wants first/end frame transition, use the `enkio:first-end-frame-video` skill instead |
| `unsupported parameter combination` | mode/quality/duration/audio combination is not in the templates | Check `combinations` and use only combinations that appear there |
| `unsupported aspect ratio X` | `ratio` is not in the model's `ratios` | Use a ratio supported by the model, and recrop **all** reference images to the new ratio |
| `prompt too long` | Exceeds `prompt_limit_length` | Shorten the prompt and retry |
| `image_urls cannot be empty` | Images were not uploaded first | First use `create_upload_url` + curl to upload each image |

## Upstream Business Error Codes

When a tool throws, the error message usually includes the upstream code and traceId.

| code | Meaning | Remedy |
| --- | --- | --- |
| `1001` | Missing request header | Server configuration issue (`GX_ALGO_SIGN_KEY` / `GX_CLIENT_*` not fully configured); report to the service maintainer |
| `1009` | Signature invalid or expired | Server `GX_ALGO_SIGN_KEY` does not match `GX_CLIENT_CP` / `GX_CLIENT_PLATFORM` / `GX_CLIENT_VERSION`, or the machine time differs too much |
| `Task X was not found` | Task does not exist or was deleted | `task_id` is wrong or the task has expired; confirm with the user and start again |
| `10001` | Not logged in | Run OAuth login again |
| `4011` | Confirmed credits no longer match the server price (pricing changed after the quote) | Nothing was charged; run `i2v_get_options` again, tell the user the new `credit_cost`, and resubmit only after confirmation |
| Other | Business failure (insufficient credits, non-compliant material, etc.) | Relay the upstream `message` field to the user as-is |

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

When reporting an error, include `traceId` as well to help server-side investigation.

## Task-Level Failure

- `task_status == "fail"`: relay `task_reason` exactly. Common causes include non-compliant content in a
  reference image, unclear face, or a policy-violating prompt. Retrying re-submits at the
  normal price--failed credits are refunded automatically, and since this is disclosed up
  front, no fresh price confirmation is needed; just suggest replacing the problematic
  reference image or adjusting the prompt before trying again.
- Polling still not complete after the upper limit (about 15 minutes): do not wait forever. Tell the user the
  current status and `task_id`, and have them continue querying later with `i2v_get_task`. The task is still
  running on the server and does not need to be resubmitted.

## Result Does Not Match Expectations

These situations are **not errors**. The task returns `success`; the finished video just differs from what
the user imagined:

| Symptom | Remedy |
| --- | --- |
| An element from one reference image does not appear at all | The prompt did not clearly state that image's role; add the description and retry (this re-bills at the normal price; no need to reconfirm since it was disclosed up front) |
| The combination relationship between reference images is wrong | Check whether the `image_urls` order corresponds to the prompt description; change both together |
| The finished video differs significantly from the reference images | This mode is "reference", not "reproduction", and this is normal; if the user wants to stay close to the original image, use `enkio:image-to-video` |
| The prompt used references such as `@1` | The upstream service does not support this syntax and treats it as ordinary text; change to natural-language references and retry |

## Material-Related Issues

- Upload interface returns `c != 200`: relay `m` to the user. Common causes are file too large or unsupported format.
- File URL expired (temporary storage was cleaned): upload again before starting the task.
- Cropped dimensions are wrong: recheck with `sips -g pixelWidth -g pixelHeight <file>`, and confirm the
  width/height order in the command was not reversed (`sips --cropToHeightWidth` takes **height before width**).
- Only some reference images were cropped: all reference images must be cropped to **the same** target size;
  an uncropped image will skew the composition.

## Preview Download Failed

The finished video is an Enkio temporary remote URL. Codex cannot embed-preview it; it must first `curl`
the video locally before delivery (see "Displaying the Artifact" in SKILL.md). Download may fail for the
following reasons:

| Symptom | Remedy |
| --- | --- |
| curl returns non-0 or file size is 0 | Retry once; if it still fails, give the remote URL to the user, state that preview download failed, and do not pretend it was delivered |
| HTTP 403 / 404 | URL expired or was cleaned; call `i2v_get_task` again to get the latest URL |
| File downloads but cannot play | Check whether it downloaded an HTML error page (use the `file` command to inspect the type); if so, retrieve the URL again |
