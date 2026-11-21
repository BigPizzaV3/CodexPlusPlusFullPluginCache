# Error handling

## MCP connection layer

| Symptom | Cause | Handling |
| --- | --- | --- |
| No `mcp__enkio` namespace in the tool list | **Most often OAuth login has not been completed** (a server that is not logged in does not register its entire namespace); in fewer cases, the plugin is not enabled | Run `codex mcp login enkio` yourself (not the user), read the plain `https://` authorization URL it prints, and give the user only that URL as a plain clickable link -- do not lead with the unreliable `codex://mcp/login?server=enkio` deep link; then **open a new conversation** and retry; see `references/auth.md` |
| `mcp__enkio` exists, but it has no `mv_*` tools | Server version is too old | Confirm the gx-mcp service has been upgraded to a version containing this play; use `codex mcp get` to see which deployment the url points to |
| Call returns 401 / says not logged in | Token expired or revoked | Run `codex mcp logout enkio` then `codex mcp login enkio` yourself, relay the newly printed `https://` login URL to the user the same way (not the `codex://` deep link), then open a new conversation and retry |
| Connection refused / timeout | The service pointed to by the url in `.mcp.json` is not started | Run `python -m gx_mcp --port 8000` locally, or change the url to the production domain |

## Upstream business error codes

When a tool throws an error, the error message usually includes the upstream code and traceId.

| code | Meaning | Handling |
| --- | --- | --- |
| `1001` | Missing request header | Server configuration issue (`GX_ALGO_SIGN_KEY` / `GX_CLIENT_*` not fully configured); report to the service maintainer |
| `1009` | Signature is invalid or expired | Server `GX_ALGO_SIGN_KEY` does not match `GX_CLIENT_CP` / `GX_CLIENT_PLATFORM` / `GX_CLIENT_VERSION`, or the machine time drift is too large |
| `1013` | Task does not exist | Wrong `task_id` or expired task; confirm with the user and start again |
| `10001` | Not logged in | Run OAuth login again |
| Other | Business failure (insufficient credits, non-compliant material, etc.) | Relay the upstream `m` field to the user as-is |

If `mv_create_story` fails with a message saying the operation `requires an active membership`, the
user is not a member. Nothing was created and no credits were charged. Give the user the
`pricing_url` contained in the error message (or call `get_pricing_url` to fetch it) to open in a
browser, signed in with the same Wondershare account used to authorize this MCP, and purchase a
membership. Retry only after the user confirms the purchase and `get_user_profile()` reports
`is_member: true`. If the membership lookup itself fails, relay the upstream error; do not retry the
create call in a loop.

When credits are insufficient, use the `credit` field from `get_user_profile()` to confirm the
balance, and prompt the user to recharge: call `get_pricing_url` and give the user the returned
`pricing_url` to open in a browser, signed in with the same Wondershare account used to authorize
this MCP, to top up credits or upgrade the plan. Do not construct the pricing link yourself.

When reporting an error, include the `traceId` as well so the server can investigate.

## Task-level failures

- Stage one item `*_status == "fail"`: other items are usually still usable. If role image / cover image fails, use `mv_regenerate_asset` to regenerate that item separately;
  if the outline or storyline fails, usually the task must be started again. Restarting
  re-bills story creation at the normal price--failed credits are refunded automatically, and
  since this is disclosed up front, no fresh price confirmation is needed; just tell the user
  it failed and ask whether to restart or abandon.
- Stage two shot `image_status == 3` or `video_status == 3`: use `mv_regenerate_segment` to regenerate only that shot,
  then run `mv_submit_production(compose_only=true)` to compose again after it completes.
- Polling exceeds the upper limit and still has not completed: do not wait forever. Tell the user the current progress and `task_id`, and let them continue querying later with
  `mv_get_story` / `mv_get_production`.

## Material-related issues

- Upload API returns `c != 200`: relay `m` to the user. Common causes are files that are too large or unsupported formats.
- File URL expires (temporary storage cleaned up): re-upload is required before starting the task again.
- Audio duration outside the `min/max_audio_duration_sec` range from `mv_get_options` will be rejected upstream. Self-check before submission.

## Preview download failures

Generated images/videos are Enkio temporary remote URLs. Codex cannot embed previews, so they must first be downloaded locally with `curl` and then displayed
(see "Showing artifacts" in SKILL.md). Downloads may fail for the following reasons:

| Symptom | Handling |
| --- | --- |
| curl returns non-0 or file size is 0 | Retry once; if it still fails, give the remote URL to the user, state that preview download failed, and do not pretend it was shown |
| HTTP 403 / 404 | URL has expired or been cleaned up; call `mv_get_story` / `mv_get_production` again to get the latest URL |
| Display shows a gray placeholder box | This means a remote URL was pasted instead of a local path; use the downloaded local absolute path instead |
| Image did not change after regeneration | The URL was updated but the old local file was reused; download again with a different file name |
