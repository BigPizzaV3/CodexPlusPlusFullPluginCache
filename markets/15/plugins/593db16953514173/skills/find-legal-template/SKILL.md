---
name: find-legal-template
description: Find a legal document template (tenancy agreement, NDA, will, employment contract, power of attorney, deed of sale and more) for one of 36 jurisdictions in the Forms Legal library, in English or in the country's own language, and link the user to its page. Use when someone asks for a legal form, contract or letter template for a specific country, or for the statute a template follows.
license: CC-BY-4.0
---

# Find a legal template on Forms Legal

Forms Legal is a library of legal document templates for 36 jurisdictions. Each template is written in the official language of its country, and most templates name the statute they follow. Templates can be filled in online and downloaded as PDF or Word without an account. Templates are reference documents, not legal advice.

Explicit instructions from the user take priority over this skill.

## When to use

- The user wants a template for a named document in a named country ("residential tenancy agreement Ireland", "contrato de arrendamiento Colombia", "Kenya employment contract").
- The user asks which law a standard document in that country follows.
- The user wants several options to compare (fixed-term vs. open-ended contract, and so on).

Do not use it to give legal advice, to judge whether a clause is valid, or to fill in, sign, file or send a document: the tools only find templates and return links.

## Steps

1. If the user has not named a country, ask which country the document is for. Do not guess it.
2. Call `search_legal_templates` with:
   - `query` (required, 2 to 80 characters): the document type in a few words, in English or in the country's language ("tenancy agreement", "deed of absolute sale", "contrato de arrendamiento"). Words match whole words or word beginnings, and common document types match across languages (lease, tenancy, arrendamiento, bail, Mietvertrag, huurovereenkomst). Fewer, more specific words give closer matches. Keep names, health details and other personal information out of the query.
   - `country`: a slug, English name or two-letter code (`kenya`, `Philippines`, `GH`), or a state, province or city inside a covered country (`California`, `Ontario`, `Lagos`). Quebec has its own slug (`quebec`), separate from `canada`. Belgium is served in French. A value that names no country returns an error listing the slugs.
   - `language` (optional): `en` returns English titles and summaries for every result. Leave it out to get each result in its jurisdiction's own language.
   - `limit` (optional, 1 to 20, default 5).
3. If no result comes back, try once more with a broader term, the English name or the native-language name, or without a city or state name. If there is still nothing, say that no matching template was found. When `match` is `partial`, no template matched every word: present the results as the closest matches. When `coverage` is `false`, the country is not covered: say so, using the `message`, and do not offer another country's template as if it applied.
4. Pick the result whose title and `jurisdiction` match the user's country and situation. Prefer one or two strong matches over a long list.
5. Answer with:
   - the title; for a non-English jurisdiction, the native title with `title_en` in brackets when present;
   - the link, exactly as returned in `url` (never build or change a URL);
   - the statute from `jurisdiction`, quoted as "references ...", not as a guarantee of compliance; if `jurisdiction` is empty, say nothing about the statute;
   - that the template can be filled in online and downloaded as PDF or Word, and is a reference document, not legal advice. For a high-stakes matter (a will, a property sale, a dispute), suggest checking with a licensed lawyer in that country.
6. Do not invent documents, URLs or statute sections that the tool did not return.

To cite a page that the search returned, use `get_citation` (see the `cite-legal-fact-table` skill).

## Fallback: the JSON API

When the MCP tools are not available, the same search is a GET request:

```
GET https://forms-legal.com/api/search-docs?q={query}&country={slug}&limit={n}&lang={code}&include_noindex=1
```

`country` here takes only a site slug: `usa`, `uk`, `canada`, `quebec`, `australia`, `new-zealand`, `ireland`, `singapore`, `uae`, `hong-kong`, `india`, `nigeria`, `philippines`, `malaysia`, `kenya`, `ghana`, `pakistan`, `espana`, `mexico`, `colombia`, `chile`, `argentina`, `brasil`, `portugal`, `france`, `belgium`, `deutschland`, `switzerland`, `austria`, `italy`, `netherlands`, `sverige`, `norge`, `suomi`, `danmark`, `polska`. `lang` takes `en`, `es`, `pt`, `de`, `fr`, `it`, `nl`, `sv`, `nb`, `fi`, `da` or `pl`. `include_noindex=1` returns the same set of templates as the tool. The response has the same result fields (`id`, `title`, `url`, `country`, `category`, `subcategory`, `jurisdiction`, `summary`, `language`, `title_en`) plus `total_matches` and `match`. A query under 2 characters returns 400. On HTTP 429, wait a few seconds and retry once; send requests one at a time. The full contract is in https://forms-legal.com/openapi.json (operation `searchDocs`).

## Edge cases

- The user names a city or state (Lagos, Abuja, Ontario, Texas): pass it as `country` or keep it in the query. The tool maps it to its country and ranks a template for that place first when one exists; otherwise pick the general template.
- Peru and other countries outside the 36 jurisdictions have no templates yet: the tool answers with `coverage: false` and the list of covered jurisdictions. Say so instead of offering another country's template as if it applied.
