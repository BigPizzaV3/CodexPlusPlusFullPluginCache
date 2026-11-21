---
name: tikita-creator-mcp
description: Create, inspect, and edit the user's Tikita interactive story drafts, characters, episodes, dialogue, variables, lorebook, and image links through Tikita Creator MCP. Use when the user mentions Tikita or provides a tikita.ai/create URL.
---

# Tikita Creator

Use the connected Tikita MCP tools. The production endpoint is `https://mcp.tikita.ai/mcp`. Preserve an explicitly requested environment and account. A supplied Tikita `/create/<short_id>` or `/story/<short_id>` URL identifies an existing story; pass it in the `short_id` field and inspect that workspace instead of creating another story.

## Connect

In ChatGPT, use the installed plugin's Connect/Sign in interface. ChatGPT handles OAuth; the user signs in to Tikita and grants consent. Do not run Codex commands in ChatGPT or ask the user to reveal credentials or callback codes. If tools are unavailable, describe the missing connection instead of claiming success.

In Codex CLI, first inspect the existing Tikita server registration. Reuse a matching registration and test an existing authenticated connection before reauthorizing. If missing, register the exact endpoint. For a registration named `tikita`, login with `codex mcp login tikita --scopes email,profile`. A differently named registration needs its own name in that command. The client may append `offline_access` to obtain refresh tokens. Keep the callback listener running while the user approves; an approval page alone is not a completed token exchange.

Call `get_capabilities` to verify the connection. A health response or a tool transport completion with `ok: false` does not establish success. If a Codex login without explicit scopes fails, retry once with `email,profile`. For ChatGPT token-exchange failures, report the error and stop reauthorization loops; clients and publishers control OAuth settings, not the conversation.

## Work on a draft

1. Read the Story Creator Guide resource, or the bundled [creator guide](references/creator-guide.md), and inspect the actual available tool schemas. Use the category reference for exact category labels.
2. For an existing story, use its `/create/<short_id>` or `/story/<short_id>` URL, or call `story_list_my_stories` with `query` for a title/short ID and `offset` if `has_more` is true. The list omits full workspace text by default. `workspace_list_items` lists saved opening, episode, character, variable, dialog, and lorebook ids without sending all text; `workspace_get_item` returns one exact saved item. Use `story_get_creation_context` or `workspace_get_draft` with selected `sections` when broader context is needed. Ask for missing creative direction only when it prevents the task.
3. Edit only the named story. Use `workspace_patch_item` for one opening, character, episode, variable, or example dialog: send its id and changed fields, preferably with the `updated_at` from `workspace_get_item`. Use `workspace_update_story_metadata` with `return_mode: "summary"` for one story field. If `workspace_changed_retry` occurs, re-read and reconcile. `workspace_patch_draft` shallow-merges objects but replaces arrays; set `return_mode: "summary"` for bulk writes unless full text is needed. It rejects omitted existing episode or lorebook ids unless `confirm_array_drop: true`, while other arrays have no omission guard. Reserve array replacement for deliberate bulk edits and set deletion confirmation only when explicitly requested. Avoid simultaneous Studio edits.
   For a small wording change inside a long field such as `introHtml`, `detailMd`, an opening body, or a character secret, use `workspace_replace_text` with a unique literal `find` string and a short `replace` string. If no text or multiple matches are found, re-read the field and give more surrounding context. Do not resend the entire long field.
4. Use `lorebook_list_library` with `summary_only: true` to find an id, then `lorebook_get_entry` and `lorebook_patch_entry` to change only the requested fields of a reusable library entry. Library changes affect reusable account entries, so do not replace or delete a shared entry merely to change one story. Workspace lorebook copies reach live conversations only after the creator saves in Studio.
5. Use only owned, completed image assets with terminal moderation. An image attachment, image-group assignment, cover, character avatar, and cinema sprite are separate references. Read back each reference that changed. If only an image URL is available and no library-list tool exists, explain the missing ID; do not invent an ID, scrape private storage, or silently import another copy.
6. Check tool results for `ok: false`, errors, limits, and missing resources. After a timeout or ambiguous write, read the target before deciding whether another write is necessary. Do not blindly repeat creates.
7. Verify a small change with `workspace_get_item` or `lorebook_get_entry`; use `workspace_get_draft` only for sections that need broad verification. Summarize changed fields and link back to Studio. A workspace update changes a draft; applying it to the story and publishing require the creator's Studio save/publish flow.

Before a large edit, use `workspace_get_content_budget` to see available room without loading the draft text. If a tool returns `story_total_length_exceeded`, Tikita rejected that edit without saving it. Report its `total`, `max`, and `sections` and reduce the relevant content before retrying; do not call it a ChatGPT request block.

## Long conversations and exports

ChatGPT may no longer supply earlier turns verbatim in a long conversation. Tikita MCP can retrieve content saved in the creator's Tikita draft even when ChatGPT's earlier context is unavailable. Before asking the creator to paste an episode or lorebook entry again, look up the owned story and read that saved item with the tools above. A ChatGPT share link does not give this plugin access to the host's original transcript.

The plugin cannot read or export the full ChatGPT conversation. If asked for a Markdown file, never call a summary or partial history the complete transcript. State which Tikita fields were retrieved and which chat messages are unavailable; only export exact content actually retrieved or supplied by the user.

## Scope and data handling

Never print passwords, access/refresh tokens, authorization codes, signed upload URLs, or raw authentication material. Creator-only story fields may be read and edited for their owner when the request requires it; keep them out of public descriptions and comments.

Public comment creation is a separate action and requires an explicit user request. Do not send comments as a connectivity test. Lorebook deletion removes library data and links across stories; explain its scope before executing an explicit deletion request. Ordinary authorized draft edits can proceed without repeated approval requests.

This plugin does not sell subscriptions, credits, digital goods, or paid image generation. Do not introduce purchase links or claim a paid generator exists. Use only the capabilities actually returned by the MCP server.
