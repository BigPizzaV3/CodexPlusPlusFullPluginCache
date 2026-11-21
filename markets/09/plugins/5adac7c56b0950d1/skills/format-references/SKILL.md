---
name: format-references
description: Produce correctly formatted references, in-text citations and BibTeX with CitedEvidence. Use when the user asks for a bibliography, citations in a given style, or BibTeX.
---

# Format references

1. Collect identifiers: DOIs, PMIDs, arXiv ids, ISBNs, URLs, CitedEvidence paper ids (W…), or exact titles.
2. Call `format_citations` with up to 30 items and the user's style: `apa`, `modern-language-association` (MLA), `chicago-author-date`, `chicago-note-bibliography`, `harvard1`, `ieee`, `vancouver`, `american-medical-association`, `nature` or `apa-6th-edition`. Default to APA 7 if the user doesn't say.
3. Return the references exactly as formatted, in the order given, with in-text citations if the user is writing. Don't retype or "improve" the formatting.
4. For items that couldn't be formatted, say why and ask for a DOI or a fuller title. Never invent missing details.
5. The card lets the user switch styles and copy references or BibTeX, so you don't need to repeat BibTeX unless asked.
