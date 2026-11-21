---
name: google-search-lookup
description: Find an official website, a public company page or a few relevant links with HasData Google Search. Use for quick web lookups, not SERP comparisons, AI answers or a requested specialized source.
---

# Find relevant Google links

Read `../hasdata-research/SKILL.md` for shared scope and `../hasdata-research/references/tool-contract.md` for response handling.

Use `hasdata_google_serp_serp_light_getSearchResults` with the supplied question as q. Start with one page and omit start. Preserve a supplied location, country or language; do not ask for them routinely. Light does not accept deviceType.

Identify the requested official site or relevant records from returned URLs, titles and snippets. A quick lookup needs a few relevant links, not an automatic ranking report. Distinguish an official company site from a directory, third-party article or similarly named company. Ask if the entity is genuinely ambiguous.

Snippets support a link shortlist, not facts from the full page. Read a selected page with `../public-web-extraction/SKILL.md` only when the user needs page-level evidence and the request budget permits it.

Use `../google-serp-research/SKILL.md` for ranking, top organic positions, intent or keyword-result comparisons, including "who ranks first for this query". Do not reduce a requested position table to a few suggested links. Use the source-specific skill for News, Scholar, Maps, Shopping or an AI Overview instead of substituting this lookup.
