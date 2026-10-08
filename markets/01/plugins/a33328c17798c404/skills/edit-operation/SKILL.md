---
name: edit-operation
description: Poll fetch after edit_form until the background form build finishes. Use whenever edit_form returns url "in_progress".
---

# Edit operation

After `edit_form` returns `url: "in_progress"`:

1. Do NOT call `edit_form` again to check progress.
2. Call `fetch` with the returned form id from `related_asset.asset_id`.
3. If `metadata.build_status` is `processing`, wait `metadata.poll_after_seconds`, then call `fetch` again with the same form id.
4. When `metadata.build_status` is `completed`, `awaiting_confirmation`, or `failed`, use `fetch.text` as the final reply to the user.

If `fetch.text` already contains a "Tell the user:" instruction, follow it exactly.

When `metadata.build_status` is `awaiting_confirmation`, ask the follow-up question described in `fetch.text` using the choices in `metadata.confirmation.choices`, then wait for the user's answer before calling `edit_form` again.
