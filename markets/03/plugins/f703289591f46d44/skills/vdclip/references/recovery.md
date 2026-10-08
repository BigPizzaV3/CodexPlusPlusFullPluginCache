# Safe recovery contract

Every connector error carries a stable `code` you can branch on, plus a human `message`.
Some also carry `retryable`, `retry_after`, `required_scope` or `feature`.

## Error codes

| `code` | Root cause | Safe next step | Stop condition |
| --- | --- | --- | --- |
| `unauthorized` | Not authenticated, or the token expired | Ask the user to reconnect the connector | Reconnect fails |
| `forbidden` | Missing OAuth scope or not the owner | Name `required_scope`; ask to grant it or pick an owned resource | Access remains absent |
| `not_found` | Id does not exist, or belongs to someone else | Re-read from `list_projects` / `list_clips`; never guess an id | Resource is genuinely gone |
| `insufficient_credits` | Balance below the job cost | Report the shortfall and stop | Always — do not retry |
| `plan_gated` | Feature not in the user's tier | Name the feature and the tier that unlocks it | Always — do not work around it |
| `quota_exceeded` | Daily/monthly posting limit hit | Show used/limit from `list_calendar`; offer a later date | Always — do not retry now |
| `invalid_input` | A field failed validation | Fix the named field (`param`) and call again | Correct value cannot be determined |
| `conflict` | State changed under you | Re-read current state, then decide with the user | Intent no longer maps cleanly |
| `rate_limited` | Request budget exhausted | Wait `retry_after`, then retry once | Wait exceeds the user's goal |
| `upstream_error` | Backend or platform failed | Read status before retrying any write | Completion stays unknown |
| `upstream_unavailable` | Backend temporarily down | Retry once after a pause | Still down on retry |
| `upstream_timeout` | Backend did not answer in time | **Read state first**, then decide | Completion stays unknown |
| `conflict_retry_exhausted` | Repeated conflicts on the same write | Stop and report; do not loop | Always |
| `feature_paused` | Chat-driven editing is off | Give the editor link from the message | Always — it is not retryable |

## Write uncertainty

After a timeout or transport loss, **never assume the write failed**. Read first:

| Uncertain write | Read this before deciding |
| --- | --- |
| `create_project` | `list_projects`, then `get_project_status` |
| `render_clip` | `get_clip` — check `render_status` |
| `publish_clip` / `schedule_clips_bulk` | `list_calendar` for the target window |
| `reschedule_post` / `cancel_post` | `list_calendar` for that `post_id` |

Retry only when the read proves the operation did not complete. A blind retry double-posts
or double-charges.

## Paused editing

`apply_edits`, `save_project` and `compose_scenes` are not advertised in `tools/list`. If
one is called from memory, the answer is `feature_paused` with a link:

```
Chat-based editing is temporarily paused.
Open the full editor to keep editing: https://editor.vdclip.com/edit/<result_id>
```

Do not retry, do not look for another tool that does the same thing, and do not promise the
edit for later. Hand over the link. See [editing.md](editing.md).

## Empty or no-op results

A tool that succeeds without changing anything is not a failure — but reporting it as a
change is. `get_transcript` on a project with no captions says so explicitly rather than
returning an empty list. `schedule_clips_bulk` returns `skipped_clips` when a clip was not
rendered. Surface both.
