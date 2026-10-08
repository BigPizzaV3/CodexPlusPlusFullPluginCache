---
name: legal-research
description: Research Indian judgments, tribunal decisions, statutory text, and later judicial treatment with Vitark MCP; use for authority finding, named-case lookup, source verification, and citation-grounded legal research.
---

# Vitark Legal Research

Use Vitark MCP for Indian legal research. Treat retrieved material as research evidence, not legal advice, and state material source and coverage limits.

## Choose the tool

- Use `vitark_search` for issue-based research. Pass the user's legal question verbatim; the tool performs query planning, retrieval, deduplication, reranking, and enrichment internally. Use `scope="cases"`, `scope="statutes"`, or `scope="all"`. Put a bench or case type in the query text because those are not filters. Add `courts`, date or year bounds, statute-year bounds, `ministry`, or `limit` only when the request supplies or clearly requires them.
- Use `vitark_statute_search` for focused statutory research and exact Act-and-section retrieval. When a prior result supplies `act_id`, pass it back with `section_number`; do not guess `act_slug`. Quote `section_text`, never the clipped `snippet`, and treat the section as complete only when `section_text_complete` is true.
- Use `vitark_case_find` for a party or case name, docket number, neutral citation, or CNR. Pass either `name` or `case_number`. A partial name match is only a candidate until the metadata or text confirms the same matter.
- Use `vitark_case_text` when the judgment's reasoning or exact words matter. It accepts a CNR and can also resolve an unambiguous neutral citation or docket number. Continue long judgments with the returned `next_offset` while `truncated` is true.
- Use `vitark_similar_cases` after identifying a strong seed CNR. Set `group_by_case=true` when the user needs distinct judgments rather than passage-level results.
- Use `vitark_entity_suggest` to resolve a judge, party, advocate, Act, or place to the canonical value used by the entity index.
- Use `vitark_cases_by` for metadata lists by judge, party, advocate, Act and section, court, year, category, disposition, case type, or case number. Prefer a norm returned by `vitark_entity_suggest`. Always pair `section` or `act_year` with `act` or `act_norm`. This index covers only the entity-extracted subset and is topic-blind.
- Use `vitark_case_citations` for Acts and cases cited by a known judgment and for approximate later citing candidates. It requires a CNR returned by Vitark.
- Use `get_credit_balance` when the user asks about credits, a call is declined, or a planned workflow would make many paid calls. It is free.

The callable surface has exactly these nine tools. Do not call a name absent from the connected server's tool catalog.

## Read result envelopes

Tool results arrive as JSON text. Parse the JSON object before assessing it; do not expect structured-content fields or an output schema.

For search envelopes, distinguish `results` (cases) from `statute_results` (statutes). Check `status`, `source_outcomes`, `resolved_scope`, `notes`, `empty_corpora`, and `unresolved_courts`. `resolved_scope.legs.partial_detail` identifies incomplete sources and gives human-readable reasons. A partial or failed source, an unresolved court, a searched corpus with no matches, and an ordinary zero-result query are different outcomes; report the one the response actually states.

Read `support_basis` before interpreting `support_level`. In case search it grades rerank relevance, not legal entailment. In focused statute search it grades Act-and-section identity, not whether the provision answers the user's question. Review `statutory_provisions` before semantic statute rows, then follow `resolved_scope.statute_reading_order`; duplicate statute mirrors may have been collapsed. If statute rows were not reranked, do not compare producer vector ranks across collections.

If the user gives a section number without identifying the Act or regulation, ask which enactment they mean before any tool call. Do not guess an enactment or quote a same-numbered provision. For an exact statute read, re-request an incomplete semantic row with its returned `act_id` and `section_number`. Quote it as complete only when `section_text_complete` is true; otherwise label the retrieved text partial and do not present it as the complete provision. Do not assert a corpus gap unless the current response reports it.

`vitark_cases_by`, `vitark_entity_suggest`, and `vitark_case_citations` rely on a partial entity-extraction index. Preserve `entity_coverage` caveats. In citation results, `acts_referred` and `cases_referred` are cited by the seed judgment; `citing_candidates` point in the reverse direction and can include title collisions. Treat a candidate as confirmed only when its citation edge is resolved. `treatment="not_checked"` means later treatment was not examined, not that the authority remains good law.

Do not convert an error or unavailable capability into a negative legal finding. Fix and retry an explicit caller error. Do not automatically retry outages or insufficient-credit responses, because a repeated paid call may debit again. Empty results and errors are not charged by the current service behavior, but the price and consent shown by Vitark at use time control.

## Write the answer

Prefer primary material and stronger courts while still testing relevance. Read the full text of authorities that carry the conclusion. Separate what each source states from your analysis, and identify it with the best metadata returned: title, court, decision date or year, citation or case number, CNR, and source URL.

Quote only text retrieved from complete `section_text` or judgment text, keep excerpts short, and label paraphrases. Do not invent missing reporter citations, paragraph numbers, quotations, holdings, treatment, or procedural history. Explain conflicting or weak authority and state when no responsive primary source was found. Do not guarantee a legal outcome. For decisions with real consequences, tell the user to verify current law and obtain qualified advice.

Vitark uses the signed-in customer's existing account and shared credit wallet. The MCP connection requests `research:read` for research tools and `credits:read` for the balance tool. Connecting another host does not create another wallet or signup benefit. Do not promote a purchase or account upgrade.
