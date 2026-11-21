---
name: vaiz-documents
description: Read, create, and edit Vaiz documents and comments — standalone documents in personal, project, or space trees, task and milestone descriptions, fragment edits, Markdown with mentions, renaming, moving, archiving, followers, threaded comments, and document history.
---

# Vaiz documents and comments

Every task and milestone in Vaiz carries a document (its description). Standalone documents live in a tree that is personal, per project, or shared across the space. All content is written in Markdown.

## Prerequisite

The Vaiz MCP server (`https://api.vaiz.com/mcp`) must be available through the installed Vaiz plugin and authorized with OAuth (open the Vaiz connection and complete OAuth sign-in).

Vaiz tools can appear under different names depending on how Vaiz is connected: `mcp__Vaiz__query_tasks` for a directly configured MCP server, or `mcp__codex_apps__vaiz_query_tasks` (sometimes with a longer app prefix such as `vaiz_testing_`) when Vaiz is installed as an app. Match tool names case-insensitively and by the tool suffix (`query_tasks`, `show_tasks`, …), not by an exact `Vaiz` prefix. Tools may also be loaded lazily: a Vaiz tool that is not in the current tool list is not missing — load it through tool search (for example `Vaiz query_tasks`) before concluding it is unavailable. Work with Vaiz only through these tools: do not open app.vaiz.com in a browser or drive the Vaiz desktop app with Computer Use, even if the user's `@Vaiz` mention also resolves to that app.

## Two kinds of "documents"

- **User documents** — content your team wrote: standalone docs, task and milestone descriptions. Tools: `get_document`, `create_document`, `replace_document_fragment`, `edit_document_content`.
- **System help** — Vaiz's own knowledge base. Do not use `get_document` for it; use `search_knowledge_base` or `read_resource` (see the `vaiz-help` skill).

Task and milestone descriptions belong to their entity: their title comes from `edit_task` / `edit_milestone`, and they cannot be moved, archived, or deleted on their own.

## Reading

- `get_document(documentId)` — a user document as Markdown, with its parent chain and child documents. Find ids with `search_space(entityType: "document")`.
- Task and milestone descriptions: the document id is in `get_task` (`document`) or `get_milestone` (`documentId`).
- `get_document_comments` — comments on a standalone document; `get_task_comments` for tasks.
- `get_document_history` — change history of a document.
- Files referenced inside a document can be read with `read_file` (see `vaiz-files`).

## Creating a standalone document

`create_document` takes a `data` object:

- `title` (required)
- `container`: `"personal"` (default, private to you), `"project"` (requires `projectId`), or `"space"` (shared)
- `description` — initial Markdown content; do not start it with a heading that repeats the title
- `parentDocumentId` — nest under an existing document

Ask where the document should live when the user did not say: a team-facing spec rarely belongs in personal documents. Do not use `create_document` for task or milestone descriptions; those documents already exist.

## Editing content

Read the document with `get_document` first, then pick the smallest edit:

| Goal | Tool |
| --- | --- |
| Fix a sentence, update a section, insert after a heading, remove a file or image | `replace_document_fragment` |
| Append to the end | `edit_document_content` (`replace: false`, the default) |
| Rewrite everything | `edit_document_content` with `replace: true` — only when the user asked for a full rewrite |

`replace_document_fragment` takes `documentId`, `find`, `text`, and `mode` (`replace` by default, `insert_before`, or `insert_after`):

- `find` must be copied verbatim from the `get_document` Markdown, formatting marks included, and must occur exactly once. If it is missing or ambiguous, nothing changes — extend it with neighbouring text and retry.
- An empty `text` with `replace` deletes the fragment; this is also how you remove a file, image, or video block.
- Several lines, or a line starting with `#`, `-`, `1.`, `>`, a code fence, or `|`, become separate blocks. A single plain line goes inline; start it with a blank line for `insert_after` to make a new paragraph.
- Only touched blocks are rebuilt; formatting that Markdown cannot express (colors, alignment) is lost only there. A full `replace: true` loses it everywhere.

`edit_document_content` takes a `data` object with `documentId`, `description` (Markdown), and `replace`.

## Markdown and mentions

Headings, lists, code blocks, and tables are supported. Mention entities with `@[label](kind:id)` where `kind` is `user`, `task`, `document`, `milestone`, `project`, or `board`, for example `@[Anna](user:64f1…)`. Use database ids, not HRIDs, inside mentions; get member ids from `query_members`. In `find`, the label of a mention does not matter — it matches by kind and id.

## Organizing the tree

- `edit_document` — rename a standalone document or change its icon.
- `move_document` — move a document with its subtree within its tree or to another tree (`container` + `projectId`). Omit `parentDocumentId` for the top level and `index` to append at the end.
- `set_document_archived` — archive (`true`) or restore (`false`); sub-documents go and come back with it. Prefer it over `delete_document`, which is permanent (see `vaiz-safe-changes`).
- `set_followers` with `entityType: "document"` — subscribe or unsubscribe members; works for standalone documents only.

## Comments

- `create_comment` with `entityType` (`"task"`, `"milestone"`, `"document"`) and `entityId` (task HRID or id; 24-char id for the others). `content` is Markdown. `replyTo` posts a threaded reply. `fileIds` attaches files already uploaded to the same entity (see `vaiz-files`); content may be omitted when files are provided.
- `edit_comment` — replace the text of your own comment and/or detach files with `removeFileIds`.
- `delete_comment` — delete your own comment; there is no archive for comments.

Mentioning an AI agent (`isAgent: true`) in a **task** comment starts an agent run. Confirm with the user first and report `agentInvocations` from the response (see `vaiz-agents`).

Use a comment for discussion, status, or questions. Use the description for the durable definition of the work.

## Good habits

- Search before creating a document; a similar one may already exist.
- Keep one topic per document and nest related documents with `parentDocumentId`.
- Decisions and conventions that should be searchable across the space belong in Space Memory (see `vaiz-memories`), possibly with a link back to the document.

Further reading: https://vaiz.com/help/tutorials/how-to-connect-vaiz-to-mcp · https://vaiz.com
