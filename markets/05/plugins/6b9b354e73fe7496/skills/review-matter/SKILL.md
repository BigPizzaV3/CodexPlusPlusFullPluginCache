---
name: review-matter
description: Build a concise, source-linked briefing for an in-house legal matter from Sandstone's people, company, conversation, and document context. Use when a legal user needs background before responding or deciding.
---

Create a factual briefing from connected Sandstone records using read-only GraphQL operations.

1. Confirm the matter or identify the strongest match; state ambiguity instead of silently choosing between similar matters.
2. Use schema introspection to confirm field names, then gather the matter description, status, owners, related people and companies, recent conversations, and relevant documents.
3. Prefer current records and label dates so stale context is visible.
4. Organize the result as: matter, stakeholders, timeline, documents, open questions, and sources.
5. Keep summaries faithful to the records. Mark synthesis as inference and quote only short excerpts when needed to disambiguate.

Do not provide legal advice, invent missing facts, expose unrelated records, or execute mutations while preparing the briefing.
