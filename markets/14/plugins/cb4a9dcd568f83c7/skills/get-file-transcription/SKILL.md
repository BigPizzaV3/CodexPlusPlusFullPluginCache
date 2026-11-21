---
name: get-file-transcription
description: Retrieve an existing transcription for a single file accessible to the authenticated HiNoter user. Use when the user asks to view or read a HiNoter file transcription and provides a file_id or a clear file_id exists in context; do not use to initiate a new transcription.
---

# Get File Transcription

Use the `get_user_file_transcription` tool provided by the plugin MCP service to read an existing transcription.

1. Obtain a unique, explicit `file_id` from the user message or a trusted previous tool result. If there is no `file_id`, ask first; if the user only provides a file name, use `$browse-hinoter-files` to get a list first, then ask the user to confirm the single match. Never guess identifiers.
2. Call `get_user_file_transcription` exactly once using the `file_id`; do not pass `user_id`, access tokens, or any other identity information.
3. Present the returned `transcription` or `segments` as-is. Do not add content the tool did not return, and do not interpret empty content as a transcription failure.
4. If the tool returns `isError`, briefly restate the error and stop. Do not bypass permission checks by calling regular business APIs.

This skill only reads existing transcriptions. It never triggers new transcriptions, never reads summaries, images, todos, or storage paths, and never performs any write operation.
