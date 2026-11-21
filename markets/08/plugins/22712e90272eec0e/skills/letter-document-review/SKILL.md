---
name: letter-document-review
description: Use when the user wants to review, comment on, improve, or check publication readiness for a Letter.md document. Guides evidence-based review, comment reconciliation, and reviewable suggestions without silently editing the document.
---

# Letter.md document review

Review the current Letter.md document with evidence from its latest Markdown and block structure. Keep findings concise, non-overlapping, and actionable.

## Review workflow

1. Resolve the target document from an explicit ID, "list_documents", or "search_workspace_documents". Do not guess between similarly named documents.
2. Call "get_review_context" when comments are part of the request. Otherwise call "get_document" for the latest Markdown and block IDs.
3. Check structure, clarity, consistency, duplication, unsupported claims, and the user's stated goal. Quote only short exact excerpts and identify the relevant block IDs.
4. If the user requested changes, create one or more focused "create_suggestion" calls. Link comment-driven suggestions with "sourceCommentIds" and preserve exact anchors.
5. Open "render_letter_editor" when the user wants to inspect or accept the results.

## Publication readiness and publishing

- Use "get_publication_context" for title, slug, description, excerpt, indexing, current revisions, site state, and readiness recommendations.
- Treat publication preparation as read-only analysis. Never publish unless the user explicitly asks to make the document public or update its public version.
- For an unpublished document, call "publish_document" with the current document revision. Use a site handle only when the Workspace owner is creating the first public site.
- For an existing public version, call "update_document_publication" with both revisions returned by "get_publication_context". Never use the first-publish tool to overwrite a public version.
- If either tool reports that the document or public version changed, read the context again and show the user what changed before retrying.

## Safety and output

- Separate observations from proposed edits.
- Do not manufacture comments, citations, versions, or acceptance state.
- If no useful issue remains, say so instead of creating a cosmetic suggestion.
- Existing document edits remain reviewable suggestions until the user accepts them in Letter.md.
