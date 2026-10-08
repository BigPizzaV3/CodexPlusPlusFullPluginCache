---
name: find-mdedit-document
description: Find and read an existing Markdown Document stored in mdedit. Use when the user asks to locate, open, retrieve, quote, summarize, or inspect a saved mdedit document. Do not use for local files, web pages, or generic Markdown questions unrelated to mdedit storage.
compatibility: Requires the mdedit MCP server with workspace and article read tools.
---

# Find and read a document in mdedit

Resolve a real saved document before describing its content.

1. Resolve the workspace with `list_workspaces` unless a `workspaceId` from an earlier mdedit tool result is already established.
   - If several workspaces could match, ask the user to choose by returned name.
   - If no workspace matches, stop without guessing.
2. Call `list_articles` for the resolved workspace.
3. Match the user's title or description against returned document metadata.
   - If there is one clear match, continue.
   - If several documents plausibly match, present only their returned titles and ask the user to choose.
   - If there is no match, say so and stop.
4. Call `read_article` with the returned `workspaceId` and `articleId`.
5. Answer from the returned saved `content`, `contentRevision`, and `contentHash`. Distinguish exact saved content from any summary or interpretation.

This workflow is read-only. Do not call create, edit, publish, or unpublish tools. Never infer document content, identifiers, revisions, publication status, or URLs from titles or conversation memory.
