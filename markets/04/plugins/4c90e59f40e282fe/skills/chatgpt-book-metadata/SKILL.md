---
name: chatgpt-book-metadata
description: Search non-transactional ebook and audiobook bibliographic metadata on EbooksDepository by title, author, publisher, or language, and retrieve one public catalog record by slug.
---

# Search ebook and audiobook metadata

Use the EbooksDepository OpenAI connector for public bibliographic research.

## Workflow

1. Call `search_book_metadata` with a title, author, or publisher. Add a two-letter language filter only when the user specifies one.
2. Present a small set of close matches with title, authors, publisher, formats, language, ISBN when available, and the canonical EbooksDepository URL.
3. Call `get_book_metadata` with a returned slug when the user needs the complete catalog record.
4. Preserve titles and names as returned while answering in the user's language.

## Boundaries

- Do not use this connector for shopping, store comparison, ordering, payment, publishing, or account actions.
- Do not infer fields that are absent from the catalog record.
- Do not read or edit uploaded manuscripts.
- Cite canonical URLs returned by the connector.
