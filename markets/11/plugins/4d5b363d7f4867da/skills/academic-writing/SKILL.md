---
name: academic-writing
description: Draft, revise or export source-cited academic writing in Paperguide AI Writer, including literature reviews, introductions, related-work sections and research reports. Use when the user wants a manuscript or document; not for standalone paper discovery or citation formatting alone.
---

# Academic writing in Paperguide AI Writer

Respect the user's requested genre, audience, scope, sources, length, and citation style. Ground factual claims in genuine paper records; never invent a citation target or use a citation to support unrelated prose.

## Choose the operation

- **Paperguide does research and writes a new cited draft:** use `generate_document` with a precise prompt, word count, `sources` (`public`, `library`, or `both`), optional `reference_ids` (up to 50, for library/both), citation style, language, folder and `workspace_id`. Check `get_usage` when credit expense is material. This is an asynchronous *Paperguide server-side job*: return its document URL and `generating` status immediately; never claim the finished manuscript exists yet. Do not repeatedly poll while the job is running.
- **Save already-written/pasted material:** use `create_document`, not `generate_document`. For supported live citations, first identify genuine paper IDs or DOIs via `search`/`fetch` or library lookup. Use exact `[Author et al., year](cite:ID)` or `cite:doi:10.x/...` targets. The display text is not the bibliographic key. Check returned `citations.unmatched` and report/fix unmatched sources; do not silently claim successful citation linking.
- **Read/edit an existing document:** find it with `list_documents` (and `list_document_folders` if useful), then `get_document`. For long/truncated text, retrieve relevant sections. Use `update_document` with `replace_section`, `append`, or `replace` as explicitly requested. Preserve existing `cite:` links and factual meaning. Editing fails while the document is open in the editor; ask the user to close it if this error occurs. Replacing text may dislocate comments, even though an editor version is saved.
- **Export a document:** use `export_document` for `docx` or `pdf` and requested citation style, relay the returned link and **exact expiration**. Use `cite_papers` for a standalone reference list, not to rebuild the citations that are already formatted on document export.

## Writing and verification

1. Decide whether the request is a synthesized literature review, critical essay, structured report, or rewrite. A review should compare themes and disagreements, not paraphrase abstracts sequentially. If using only a named folder, resolve its reference IDs first and constrain the document sources accordingly.
2. When manually constructing prose, read relevant paper details with `fetch`, `search_reference_manager_full_text` or `get_reference_full_text` when warranted. Differentiate direct full-text support from abstract summaries; do not invent quotes, page numbers, effects or methods.
3. Keep the distinction between findings, interpretations and suggestions; maintain qualifications and confounding/limitations. Never treat a generated draft as publication-ready without expert checking.
4. For the exact tool limits and failure behavior, read `references/writer-operations.md` before performing large operations or modifying documents.

## Output

Return a useful outline or completed text as requested, cite grounded material, and give the **Paperguide document link/status**, citation-linking issues or credit limitations. On server-side generation, make clear that the content is in progress and accessible at the returned link; do not imply completion.

Only take write actions when the user requests creation or edits; user instructions and safety policies override stylistic defaults here.
