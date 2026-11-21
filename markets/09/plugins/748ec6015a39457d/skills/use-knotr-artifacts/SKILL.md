---
name: use-knotr-artifacts
description: >-
  Create and manage Knotr Artifacts over MCP (list_artifact_types,
  create_or_update_artifact, collections). Use when saving Cursor canvases,
  markdown docs, or HTML/React rewrites as durable shareable outputs. Prefer
  knotr-save-artifact for an explicit save.
---

# Use Knotr artifacts (MCP)

Artifacts are durable, shareable outputs—not chat ephemera and not skills.

## After create or update

Always paste **`present_url`** from the MCP response in chat (handoff link).
Set link visibility when the user asks to share.

## Mapping

| Source | artifact_type | content_format | source_kind | Body |
|--------|---------------|----------------|-------------|------|
| Cursor `.canvas.tsx` | `page` | `tsx` | `cursor_canvas` | Paste TSX unchanged |
| Long-form markdown | `document` | `markdown` | `markdown` | Markdown source |
| Static HTML (no scripts) | `page` | `html` | `html_static` | HTML |
| Claude/Gemini interactive HTML/React | — | — | `html_interactive` | **Rewrite** to `page`+`tsx` |

## page + tsx rules

- Default-export one React component
- Import only `cursor/canvas` and `react`
- Inline data; no `fetch()` / network

## Tools

1. `list_artifact_types` if unsure of allowed formats.
2. `create_or_update_artifact` (`mcp_write`) with title, type, format, body.
3. Optional `collection_ids` or `create_or_update_artifact_collection`.
4. `list_artifacts` / `get_artifact` to reopen.

Prefer **knotr-save-artifact** when the user explicitly wants to persist.

## When not to use artifacts

- Reusable procedures → skills
- Source-of-truth notes/docs → knowledgebase
