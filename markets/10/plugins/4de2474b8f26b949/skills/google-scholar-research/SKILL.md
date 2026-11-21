---
name: google-scholar-research
description: Find Google Scholar papers, retrieve their citation formats or inspect a supplied Scholar case-law result with HasData. Use for scholarly metadata and citations, not claiming to read a full paper from its snippet.
---

# Find papers and citation formats

Read `../hasdata-research/SKILL.md` and the Search sources section of `../hasdata-research/references/tool-catalog.md`.

Search `hasdata_google_scholar_scholar_getScholarSearchResults` with q. Preserve requested year range, language and scope using actual source filters. Select a matching returned paper; clarify genuinely ambiguous titles. Return authors, title, year, snippet and source links only where provided. Abstracts and snippets do not establish full-paper findings.

For bibliography formats, reuse a matching result when available. Otherwise one search plus citation lookup needs at most two requests. Call `hasdata_google_scholar_cite_getScholarCitationFormats` with q equal to the exact returned resultId. Here q is an identifier, not the title, DOI, article URL, arXiv ID or a reconstructed value.

Return only actual formatted snippets and export links. A missing BibTeX link stays unavailable. If resultId is absent or the user forbids the lookup needed to acquire it, stop and explain rather than inventing an ID or presenting a remembered citation as fetched.

A BibTeX export link is not the .bib file's text. Label it as a link; do not claim to have retrieved BibTeX content unless that URL was actually read within the remaining budget.

For an explicitly requested Scholar case-law opinion, use `hasdata_google_scholar_case_law_getScholarCaseLawOpinion` with an actual supplied or returned caseId. Do not invoke it for an academic-paper request or turn returned opinion text into personalized legal advice.
