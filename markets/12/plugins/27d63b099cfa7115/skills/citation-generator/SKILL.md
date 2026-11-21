---
name: citation-generator
description: Turn a DOI or an ISBN into APA 7, MLA 9 and Chicago citations with the generate_citations tool, or format a source without a DOI or ISBN with format_manual_citation, including BibTeX, RIS and text reference-list downloads.
---

# Zovo Citation Generator

Use `generate_citations` when the user gives a DOI or an ISBN (or a list of them) and wants a citation, a works cited list, or to cite their sources.

1. Pass every identifier the user gave in `identifiers` (up to 25). DOIs may be a bare `10.xxxx/...`, a `doi:` value or a `https://doi.org/...` link; ISBNs may have hyphens and may be ISBN-10 or ISBN-13.
2. Pass `style` when the user names one: `apa7` (default), `mla9`, `chicago_ad` or `chicago_nb`. If the user names more than one style, call the tool once per style.
3. Pass optional `keep_capitals` (e.g. `["London", "Studies"]`) to preserve source words case-insensitively. APA uses mechanical sentence case and shows a caution note when it lowercases source capitals. The manual tool also accepts this list inside `record`.
4. Read the citation for each item straight from the result. Do not add authors, years or page numbers yourself: every field comes from Crossref or Open Library, and a missing field is reported as a warning.
5. Share the warnings, the reference-list order, and the BibTeX, RIS and text download links. The widget lets the user switch style, copy a citation, and download the files.
6. If an identifier is not in Crossref or Open Library, the item status is `not_found`; tell the user and use `format_manual_citation` only if they type the source fields.

Use `format_manual_citation` when the source has no DOI or ISBN, or the user gives the fields by hand. Pass `record` with `type` (book, journal_article, web_page or chapter) and `title`, plus the authors, year, container, volume, issue, pages, publisher, URL and access date that apply.

Do not read or upload files, do not search for a DOI by title, and do not cite legal cases, patents or datasets; those get a generic format with a warning. Check citations before submitting academic work.
