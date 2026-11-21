---
name: research-gaps
description: Identify evidenced research gaps with AnswerThis, test proposed gaps against contrary findings, and propose specific follow-up studies.
---

Produce a map of supported open questions in the user's field. A low search count is a retrieval result, not a research gap.

For library papers, locate the requested folder with `list_library_folders`, browse it with `list_library_papers`, and use `read_library_paper`. Save newly discovered papers only when the user requests it; otherwise use their available abstracts and evidence. Reading missing library text requires permission to acquire and store the PDF. Follow `next_offset` with the same `version` until every page is read. Identify abstract-only findings and inaccessible papers.

1. Break the topic into relevant populations, interventions, methods, outcomes and settings. List synonyms and narrower concepts before searching.
2. Inspect the available AnswerThis tool schemas. Discover papers with `search_papers` and retrieve citable passages with `get_evidence_passages` when it is available. Use the host's registered names, including plugin prefixes. If account connection is required, connect and continue the research task.
3. Retrieve recent reviews and primary studies that state limitations, unanswered questions or future work. For each proposed gap, search directly for work that may already address it. If contrary evidence exists, revise or reject the proposed gap.
4. Build each gap from an explicit source statement or a documented contradiction between retrieved studies. Cite both sides of a contradiction. A passage reporting a positive finding does not support an attached claim that other work is absent. Current `get_evidence_passages` evidence is abstract-only; do not imply full-text review.
5. For each supported gap, explain what is established, what is missing or disputed, why resolving it matters, and one feasible research question or design. Separate the authors' stated limitation from your proposed next study.
6. Order gaps by strength of evidence and practical value. If evidence cannot establish a proposed gap, describe the retrieval limitation instead of presenting it as an open problem in the field.
7. Use APA unless the user requests another supported `citation_style`. Pass it to `search_papers`, `get_evidence_passages`, and `list_library_papers`. In chat, pair returned `citation.inline` citations with `citation.full` bibliography entries and source URLs or DOIs. Keep raw citation IDs out of chat. For requested Writer saves or edits, use exact citation markers in `create_draft` or `update_draft` Markdown and supply the original evidence `context_ids`, including earlier searches. Leave references unlinked when no URL is available. Reconcile numbered citations across calls and include only sources used. Follow the Writer tool's prose-and-linked-citations contract and return its document link.

If `get_evidence_passages` is unavailable, clearly limit the output to what retrieved metadata or abstracts support. Never invent passages, citation identifiers, studies, or an AnswerThis saved result. A suggested research direction is a proposal, not proof that the study has never been done.
