---
name: use-knotr-knowledge
description: >-
  Search and read Knotr knowledgebases over MCP (list_knowledgebases,
  search_knowledgebase, list_documents, get_document) and know when to write
  notes with create_or_update_document. Use when the user wants trusted docs,
  notes, or semantic search from their profile KB.
---

# Use Knotr knowledgebases (MCP)

## Discover

1. `list_knowledgebases` (optional `query`) or `knotr-ai://manifests/knowledgebases`.
2. Prefer **active** KBs for search and document tools.

## Read / search

1. `search_knowledgebase` with a natural-language `query` (and KB scope when
   the tool requires it).
2. Or `list_documents` on an active KB, then `get_document`:
   - `return_type: metadata` (default) — same fields as a list row
   - `contents` — text_note body / extracted file text
   - `file` — signed download URL for file documents
3. Use `knotr-ai://manifests/document-mime-types` before creating files/notes
   with unfamiliar MIME types.

## Write

Use `create_or_update_document` (`mcp_write`) when the user wants durable notes
or uploads in a KB—not for reusable task procedures (skills) or shareable
finished canvases (artifacts).

1. Confirm target `knowledgebase_id` (active).
2. Omit `document_id` to create (`name`, `content_type` required).
3. For `text_note`, store markdown/plain content verbatim.
4. On update, `tags: []` leaves tags unchanged; include `""` in `tags` to
   clear entries.

## When not to use KB

- Reusable how-to → `use-knotr-skills` / `create_or_update_skill`
- Shareable canvas / page / long deliverable link → `use-knotr-artifacts`
