---
name: letter-document-authoring
description: Use when the user wants to create, find, open, read, or revise a Letter.md document. Guides safe document selection, creation, editor opening, and reviewable suggestions with Letter.md MCP tools.
---

# Letter.md document authoring

Use Letter.md as the source of truth for document identity and current content. Keep reads and writes separate so the user can understand what will change.

## Choose the document

- Use an explicit "documentId" when the user supplied one.
- Use "list_documents" when the title is ambiguous or the user wants to browse. Use "search_workspace_documents" when the user describes document content instead of its title.
- Use "render_letter_editor" without a document ID only when the user explicitly asks for their latest document.
- If multiple documents remain plausible, present the short candidates and ask the user to choose instead of guessing.

## Create a document

1. Draft complete Markdown before saving.
2. Call "create_document" only when the user asked to create or save a new Letter.md document. Supply a useful title and the finished Markdown. Omit "idempotencyKey" for normal retries.
3. Use the returned document ID with "render_letter_editor" so the user can continue in the collaborative editor.

Creating a new document never means overwriting an existing document. Do not use "create_document_from_ai" outside an active in-editor derivative workflow.

## Read or revise an existing document

1. Call "get_document" before quoting, summarizing, or proposing changes so the response uses the latest Markdown and block IDs.
2. For requested edits, call "create_suggestion" with narrow operations anchored to exact current block IDs and text. Prefer "replace_text" for a local edit and include prefix or suffix context when the same text can occur more than once.
3. Explain that a suggestion is reviewable and does not change the document until the user accepts it.
4. Call "render_letter_editor" when the user asks to open the document or when visual review and acceptance are the natural next step.

Do not claim that a suggestion was accepted or that document content changed unless a later tool result confirms it.
