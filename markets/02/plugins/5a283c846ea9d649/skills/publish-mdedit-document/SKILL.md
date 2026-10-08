---
name: publish-mdedit-document
description: Check or change Public Document Publishing for an existing mdedit Markdown Document. Use when the user explicitly asks to publish, unpublish, inspect publication status, or create or update a public mded.it link. Do not use for private editor links, local files, or generic sharing advice.
compatibility: Requires the mdedit MCP server with publishing tools and explicit confirmation fields.
---

# Manage Public Document Publishing

Public visibility is a separate, explicit action. Never treat saving or editing as permission to publish.

1. Resolve the workspace and document using `list_workspaces`, `list_articles`, and `read_article`. Ask the user to choose when a returned match is ambiguous.
2. Call `get_publish_status` before proposing a mutation.
3. For a status-only request, report only the returned state and exact returned URL fields, then stop without mutating.
4. Before publishing or updating a public link, warn that anyone with the link can view the document and ask for explicit confirmation. Do not infer confirmation from an earlier save or edit request.
5. After confirmation, call `publish_article` with `confirmPublic: true`. Include a custom slug or SEO metadata only when the user supplied or approved it.
6. Treat publication as successful only when the tool returns `publishId`, `shortUrl`, `fullUrl`, and `publishedAt`. Return the exact tool-provided public URL; prefer `shortUrl` for sharing.
7. Before disabling a public link, identify the current returned link and ask for explicit confirmation. After confirmation, call `unpublish_article` with `confirmUnpublish: true`.

Never construct an `mded.it` URL, expose an editor URL as a public link, or claim publication from a requested slug. On denied permission, failure, or missing result fields, report the bounded error and leave visibility unchanged.
