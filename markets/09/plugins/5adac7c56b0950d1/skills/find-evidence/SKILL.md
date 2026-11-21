---
name: find-evidence
description: Find, read and cite real scholarly papers with CitedEvidence. Use whenever the user wants papers, studies, sources, a literature overview or evidence for a claim.
---

# Find evidence

Never cite papers from memory. Every paper you mention must come from a CitedEvidence result in this conversation.

1. **Search.** Call `search_papers` with a short keyword query (3–8 words, no punctuation-heavy phrases). Use `year_from`/`year_to` for recency, `open_access_only` when the user needs free full text, and `sort: "most_cited"` for landmark work or `"newest"` for the latest.
2. **Refine.** If results are off-topic or thin, search again with synonyms or a narrower concept instead of padding with weak papers.
3. **Go deeper when useful.**
   - `get_paper` for the full abstract, all authors and the open-access link before you describe a paper's findings in detail.
   - `find_related_papers` with `relation: "cited_by"` for newer work that builds on a paper, `"references"` for its sources, `"similar"` for neighbours.
   - `search_authors` / `get_author` when the user asks about a researcher.
4. **Answer.** Summarise what the evidence shows, noting study types, years and disagreements. Cite each paper as Author et al. (Year) with its DOI. Say clearly when evidence is limited.
5. **Offer next steps:** saving papers with `save_to_library`, formatted references with `format_citations`, or a full Deep Research report.

The interactive card already shows the result list, so don't repeat every field in your reply; focus on synthesis.
