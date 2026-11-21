# Shared workflows

## Resolve names and recover

Inspect the full live tool declaration, including input schema; a truncated tool summary is not a missing capability. For `compact-v1`, find a person or agent with `list_members({"request":{"kind":"workspace","query":"Chief Approval"}})` and a channel/DM with `list_conversations({"request":{"kind":"list","q":"pr-approvals"}})`. Replace example names with the requested target. Never infer a separate search mode from the user's word “search.” Use `conversation_kind` only if the live schema offers it.

For an invalid mode, use the returned supported modes. For an invalid field, correct it against the full declaration. Refresh tools only when it disagrees with the server, and reconnect only for actual authentication or identity recovery. Resume the original authorized task after recovery; finding a recipient does not complete a requested send. Use `markdown_content` for the message body where the declaration requires it.

For complete reads, follow `next_page.tool` and `next_page.arguments` when returned, including on empty pages. Otherwise follow the tool's existing cursor contract while preserving filters. A failed Jam query is unavailable evidence, never “no Jams.” Report incomplete coverage when a server has no continuation.

# Shared workflows

These are workflow hints for the compact catalog, not an allowlist or frozen schema. If the active connection exposes legacy tools, use the current exposed equivalents and their schemas. Never assume the compact rollout is active.

## Decisions and follow-ups

Resolve channel IDs using permitted discovery. `search_messages` finds candidates; `read_thread` recovers the discussion. `read_conversation` has context, messages, threads, and time-range modes: select the smallest mode that covers the request. Follow cursors until the requested range is covered, and recover replies before calling an item open or resolved. Use source timestamps to order proposals and decisions; do not choose a launch day from the question's wording.

For a cross-channel update, give a concise decision, remaining follow-ups, stated owners, and direct source links. An absent owner is “not stated,” not the message author's inferred responsibility. If access is partial, qualify the scope instead of claiming completeness.

## Sending

`send_message` can address a conversation, thread, or direct-message recipients in the compact catalog. Use the exact schema; do not assume a legacy flat payload still works. Preserve the intended thread root and destination. `save_message_draft` is an explicit save action, not a required step for drafting in chat. Do not create reminders, reactions, channels, or memberships unless requested.

When sending a previously approved draft, ensure the principal and destination still match the authorization. If a principal switch changes the author, resolve the changed authorship before sending. An error or timeout is not proof a message was not sent; reconcile before retrying.

## Knowledge and jams

Use discovery/read/update interfaces while retaining resource type, audience, ID, and revision. Read the current resource before editing; preserve unrelated content and handle revision conflicts by rereading. `answer_from_knowledge`, when exposed, synthesizes cited knowledge. Read the cited sources for exact quotations. A `no_answer` result can lead to message search; `in_progress` calls for bounded waiting rather than duplicate jobs. Jams may expose details and transcripts separately; use the transcript for claims about what was said.

## Files and tasks

`read_file` returns metadata/download access or upload readiness; it does not itself extract contents. Download/read only the permitted file needed for the task. `upload_file` may accept small inline bytes or prepare a signed upload. In the latter case, PUT the bytes using the returned contract and confirm readiness before attaching. Do not claim the prepare response uploaded the file.

Use `read_tasks` and the currently advertised typed task action, such as `create_task`, `report_task_progress`, or `change_task_status`. Older catalogs may expose `update_task`; follow its actual schema. Respect target-conversation access and the current revision. Do not invoke task inspection repeatedly after access denial. Missing task access does not establish that no tasks exist.
