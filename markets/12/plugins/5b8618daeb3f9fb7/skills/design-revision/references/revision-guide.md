# Revise an existing design

Identify the actual source before writing: a room/artifact returned in this conversation, or an accessible uploaded image. If several images are plausible, ask which one to change. Record what must stay and what must change, including exact replacement text or target dimensions.

For a known accessible Designkit room, use `designkit_update_task` with the same `room_id`, a new idempotency key, and a brief identifying the artifact/page and selected revision. Preserve pending task context. Reopening previews or checking progress is read-only.

For an uploaded external design with no existing room, prepare the actual upload and create one task using the source as a reference. Explain that a new task is needed in this case. Do not invent a source room or claim the backend can access another user's room.

For exact text replacement, preserve punctuation, language and case. For resizing, specify all requested sizes and reflow the composition instead of stretching it. For reference-guided changes, capture the reference's role separately from the user's product or logo.

Follow [the MCP workflow](mcp-workflow.md). Present real revised previews and links; distinguish any remaining mismatch or failed output. Do not promise vector/source editing, perfect preservation of pixels, image layers, or a downloadable format that has not been returned. Do not trigger further revisions without the user's request.
