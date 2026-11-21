---
name: literature-review
description: Synthesize a literature review with AnswerThis paper discovery and retrieved evidence, comparing methods, findings, contradictions, and retrieval limits.
---

Build a review around the user's research question and the evidence retrieved in this conversation.

For library papers, locate the requested folder with `list_library_folders`, browse it with `list_library_papers`, and use `read_library_paper`. Save newly discovered papers only when the user requests it; otherwise use their available abstracts and evidence. Reading missing library text requires permission to acquire and store the PDF. Follow `next_offset` with the same `version` until every page is read. Identify abstract-only findings and inaccessible papers.

1. Define the question's population, methods, outcomes and timeframe where relevant. Plan the terms and synonyms for each facet. State any scope assumption that affects inclusion.
2. Inspect the available AnswerThis tools and their current input schemas. Use `search_papers` to discover papers and resolve identifiers. Use `get_evidence_passages`, when available, to retrieve citable evidence. Request account connection if the tool requires it, then resume the same task. Use the host's registered tool names even when they include a plugin prefix.
3. Cover the question from several relevant angles. Start with recent reviews to map terminology, then retrieve primary research for measured effects and study methods. Retry a search when a missing facet has a concrete new query or source to try. Record uncovered facets as retrieval limits.
4. Maintain an evidence table with paper identity, study design, population, relevant finding and the passage that supports it. Mark information that the returned evidence does not provide. `get_evidence_passages` currently returns abstracts, not full papers; report that reading limit and avoid claims about inaccessible sections.
5. Write the review around comparisons across studies. Separate primary studies from reviews, explain disagreements and methodological differences, and distinguish supported conclusions from your interpretation. An empty search cannot establish that research does not exist.
6. Use APA unless the user requests another supported `citation_style`. Pass it to `search_papers`, `get_evidence_passages`, and `list_library_papers`. In chat, pair returned `citation.inline` citations with `citation.full` bibliography entries and source URLs or DOIs. Keep raw citation IDs out of chat. For requested Writer saves or edits, use exact citation markers in `create_draft` or `update_draft` Markdown and supply the original evidence `context_ids`, including earlier searches. Leave references unlinked when no URL is available. Reconcile numbered citations across searches with a consistent paper-to-number mapping.
7. End with supported conclusions and the remaining uncertainties. In chat, include a bibliography of sources actually used. Save to AnswerThis through `create_draft` only when requested, following its prose-and-linked-citations contract so Writer generates the exported bibliography. Then offer the returned document link.

Deliver the review in the conversation unless the user requests a file or saving to AnswerThis. If an import/editing tool is available, inspect its schema and use it only for the requested save or edit. A local draft or host-generated answer has not automatically been saved in AnswerThis.
