---
name: legal-text-research
description: Research and verify Côte d'Ivoire and regional legal sources with Nanan when a user asks for a law, code, decree, article, quotation, corpus count, legal basis, or source-backed legal explanation.
---

# Nanan legal-text research

Use the Nanan tools for source-grounded legal-text discovery in Côte d'Ivoire and supported regional corpora.

## Workflow

1. Search with the user's legal topic, exact title, official number, or article reference. Preserve important qualifiers such as jurisdiction, date, and legal domain.
2. Fetch the strongest matching results before drawing conclusions. Prefer article-level results over a whole-code overview when the question concerns a specific rule.
3. When the user or draft answer attributes wording to a specific article, call `check_legal_citation`. Supply `quoted_text` whenever wording is presented as a quotation or close paraphrase. Treat `quote_mismatch`, `ambiguous`, and `not_found` as hard stops: correct the citation or state that the corpus did not verify it.
4. Use `count_corpus_sources` for questions about how many documents, decisions, or sources Nanan holds. Apply the narrowest supported filters and report the returned scope. Never count search results or extrapolate beyond the inventory response.
5. Cite the canonical Nanan URL returned by each fetched result. Name the legal text and article number in the prose.
6. Report the source's status and confidence when present. If status is unknown, historical, repealed, modified, or not recently verified, say so plainly.
7. Separate what the text says from interpretation. Explain ambiguity and ask for missing facts when they could change the answer.
8. Treat results as legal information, not a substitute for advice from a qualified professional. Recommend professional review for deadlines, litigation, criminal exposure, large transactions, or irreversible action.

## Answer contract

For substantive legal answers, structure the result around:

1. **Rule established by the fetched source** — concise and source-backed.
2. **Application or interpretation** — clearly marked as analysis rather than quoted law.
3. **Verification limits** — status, date, corpus gaps, or facts that could change the conclusion.
4. **Sources** — canonical Nanan links beside the claims they support.

## Integrity rules

- Never invent an article, quotation, effective date, court decision, or source.
- Do not present a search snippet as the full provision; fetch it first.
- Do not silently substitute a neighboring article when an exact citation cannot be resolved.
- Do not describe a paraphrase as a quotation or declare semantic legal correctness from a text match alone.
- Do not infer the size or exhaustiveness of the corpus from paginated search results.
- Do not imply that Nanan's corpus is exhaustive. If the search is empty or weak, state the limitation.
- Quote only the amount necessary and keep the canonical URL beside the claim it supports.
- Never expose internal identifiers when a human-readable title and URL are available.
