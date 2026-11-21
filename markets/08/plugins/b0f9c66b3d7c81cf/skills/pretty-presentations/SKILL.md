---
name: pretty-presentations
description: Draft or edit PowerPoint presentations through the connected Pretty workspace, continue Pretty chats, and use its available files, skills, brand kits, assets, and slide pools. Also use when the user asks to save a personal Pretty skill or presentation preference.
---

# Work with Pretty

Pretty's MCP tools send requests to the same chats users can open in the Pretty editor. Creating and editing a presentation are messages in those chats. The remote Pretty assistant performs the work.

Use the tools advertised by the connected Pretty server and their actual input schemas. The deployed server can offer fewer tools than this package describes. Brand kits and slide pools also depend on workspace feature settings. Use optional tools only when they are available; if a requested capability is absent, explain that limitation and continue with the available workflow where possible.

## Start or continue a presentation

For a new task, call `start_chat` with the user's request. For a revision or answer in an existing Pretty chat, call `send_message` with that chat's `chatId`. Use `list_chats` to find an existing chat when its ID is unknown. Preserve a known chat ID across follow-ups.

Include the audience, purpose, requested length, source material, and style requirements the user has supplied. Send enough context for Pretty to do the task without relying on this conversation being visible there. Read a relevant workspace skill with `list_skills` and `read_skill` when the user requests that workflow, and include its reference or relevant guidance in the Pretty message.

Share the returned `url` as a clickable link as soon as the request has started. This opens the same chat in Pretty, where the user can inspect and continue the work.

After `start_chat` or `send_message`, use `wait_for_chat_status` if available. Each call waits for up to 50 seconds. If the result is `queued` or `working`, continue waiting while the task is active and give occasional progress updates. If this tool is unavailable, use `get_chat_status` to check progress without rapid polling.

Handle the returned status:

- `queued` or `working`: The task is still running. A successful message send is not a finished presentation.
- `waiting_for_you`: Relay the assistant's question and use `send_message` in the same chat when the user answers. Answer from context already supplied by the user when it resolves the question.
- `finished`: Summarize the returned result and share the Pretty chat link. Use `list_messages` if the latest message lacks needed context.
- `failed`: Report the public error and chat link. Do not repeatedly queue the same failed request without understanding the cause.

`send_message` defaults to `queued: true`, which waits for the current assistant turn to finish. Use `queued: false` when the user asks to interrupt or replace the work in progress; it stops that turn and leaves its partial reply in the chat.

## Files and source links

`list_files` without `path` returns the caller's organization and personal roots. Browse returned directory paths to locate existing files. Follow `nextCursor` using the same directory path when a folder has more results.

Attach an existing file using the exact path returned by `list_files`:

```json
{"type": "workspace", "path": "<returned workspace path>"}
```

Attach a user-supplied source link using:

```json
{"type": "link", "url": "<source URL>", "title": "<optional source title>"}
```

Pass these objects in the `attachments` array of `start_chat` or `send_message`. `list_files` returns metadata, not file contents. Let the Pretty assistant read attached sources when the task needs them. The Pretty assistant edits presentation files through chat requests. File transfer tools move source or result files when those tools are available.

## Upload and download files

A local path alone does not provide file access. Obtain the actual file bytes from a user attachment or another authorized source before uploading. Use `list_files` to choose a returned workspace root and an existing destination directory.

When `create_file_upload` is available, calculate the exact byte length and base64-encoded CRC32C checksum, then send `path`, `mimeType`, `size`, and `checksum`. PUT the same bytes to the returned `url` using every returned header and the returned method before `expiresAt`. Only after the upload succeeds, call `complete_file_upload` with the returned `operationId` and `rootId`. Report success only when completion succeeds. Attach the completed file using its returned workspace path. Never invent file bytes, checksums, upload identifiers, or completion results.

If the client cannot transfer bytes to the upload URL, explain that limitation and ask for an accessible source link or an upload through Pretty. Do not mark an untransferred file complete.

When `get_file` is available and the user requests a file, pass its exact returned workspace path and share the returned temporary download link or resource link. Treat signed upload and download links as temporary and avoid saving them as permanent file references.

## Brand kits, assets, and reusable slides

When `list_brand_kits` is available and the user requests a particular brand, resolve its ID and pass it as `brandKitId` to `start_chat`. Omit it to use the organization's default. Brand kit selection belongs to a new chat; `send_message` does not accept that field.

Use `list_asset_libraries` to discover available libraries, then `search_assets` with a returned library ID. Mention the selected asset's exact returned `ref` in the Pretty message so the assistant can use it. Respect `hasMore` and advance the search page when needed.

Use `list_slidepools` to find ready slide pools and `search_slidepool` to find matching slides. Send the chosen pool ID, slide ID, slide number, and intended use in the Pretty message. Returned slide IDs and slide numbers are distinct. The search returns descriptions and identifiers; the Pretty assistant does the reuse or adaptation.

## Personal skills and preferences

When available, `create_skill` saves a personal skill with `name`, `description`, and Markdown `instructions`. Use it when the user asks to save a reusable Pretty workflow. The result is private to that user. Organization skills are managed in Pretty. If the tool returns `duplicate`, report it and resolve the name rather than claiming the existing skill was overwritten.

When the user asks Pretty to remember a durable presentation preference, use `create_memory` if available. Its `memory` value must be one line of at most 500 characters. Pretty reads this preference across the user's organizations. Check the returned status; `memory_full` means the preference was not saved.

## Read the conversation

`list_chats` returns the caller's chats, most recently active first. `list_messages` defaults to newest first; use `order: "oldest"` to read a transcript chronologically. Follow `nextCursor` while keeping the same chat and order. Report the user-visible messages and returned links without inventing internal tool results or presentation download URLs.
