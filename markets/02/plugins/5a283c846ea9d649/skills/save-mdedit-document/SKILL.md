---
name: save-mdedit-document
description: Create and durably save a private Markdown Document in mdedit. Use when the user explicitly asks to save, persist, archive, or turn conversation content into a document in mdedit. Do not use for generic Markdown writing, formatting, or local-file creation that does not require mdedit storage.
compatibility: Requires the mdedit MCP server with list_workspaces and create_article tools.
---

# Save a document to mdedit

Create one durable private document from content the user supplied or asked you to draft.

1. Determine the intended title and Markdown content. Ask a focused question if the source material or document boundary is unclear.
2. Resolve the destination workspace:
   - Use an established `workspaceId` only when it came from an earlier mdedit tool result.
   - Otherwise call `list_workspaces`.
   - If exactly one workspace is returned, use it. If several are returned, ask the user which returned workspace name to use. If none are returned, stop.
3. Call `create_article` once with the returned `workspaceId`, title, complete Markdown content, and `collaborative: false` unless the user explicitly asks for live collaboration.
4. Treat the save as successful only when the tool returns `workspaceId`, `articleId`, `contentRevision`, `contentHash`, and `editorUrl`.
5. Report the saved title and exact returned `editorUrl`. State that the document remains private.

Never invent or reconstruct a workspace ID, document ID, revision, hash, or editor URL. Never call a publishing tool as part of this workflow. If creation fails or reports retained partial state, report that bounded failure and do not claim the document was saved.
