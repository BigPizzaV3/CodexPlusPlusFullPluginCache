---
name: literature-discovery
description: Find and curate scientific papers on a research topic using Paperguide. Use for exploratory literature searches, foundational and recent study lists, or requests to discover papers; not for comparing a fixed set of saved PDFs or claiming an exhaustive systematic search.
---

# Literature discovery

Use Paperguide's MCP tools for a transparent, exploratory search. A search result is not a screened study or a full-text-verified finding.

## Workflow

1. Extract the research question and explicit boundaries (population, intervention/exposure, study type, years, languages). If open-ended, proceed with a clearly stated reasonable scope; ask only if an essential restriction is ambiguous. Do not invent filters.
2. Build a small set of complementary search queries: the main concept, important synonyms, and distinct subtopics. Use `search` with the user's year, PDF, OA, citation, and journal-quartile filters only when requested. For foundational papers, consider wider years; for recent work, use the requested lower year. Search returns at most 20 results per call; refine and make additional distinct calls as needed.
3. Combine results and deduplicate by DOI, then normalized title/year when DOI is missing. Evaluate topical relevance from title/abstract; do not rank by citation count alone or treat journal quartile as a definitive quality assessment.
4. Use `fetch` for promising or ambiguously indexed papers to verify bibliographic metadata, abstract/summary, DOI and publication type. Public `search`/`fetch` do not constitute full-text access. For a user requesting full-text conclusions from *their saved papers*, use reference-manager tools or the paper-critical-appraisal/evidence-comparison skill instead.
5. Group the curated papers by theme or methodological role where helpful. Present exact tool-supplied title, year, DOI/link and a short why-it-matters explanation. Label abstract-based takeaways as such.
6. State what was searched, explicit filters, and limits. Offer to save papers only when useful; use `add_reference` after the user requests saving, handle duplicate IDs, and check `get_import_status` if an import job is returned.

## Output

Provide a concise **search scope**, **relevant papers** (citation/source, why relevant, access/verification level), **themes or unresolved questions**, and **limitations / suggested next search**. Never fabricate DOIs, citations, effect sizes, paper counts, PRISMA flows, or full-text conclusions. A few exploratory calls cannot establish exhaustiveness or absence of evidence.

Read `references/search-quality.md` when designing searches with multiple concepts or discussing reproducibility. Explicit user instructions and applicable platform safeguards take precedence over default workflow choices here.
