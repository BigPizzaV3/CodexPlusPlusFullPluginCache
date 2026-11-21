---
name: cite-legal-fact-table
description: Use when quoting a government fee, duty rate or filing rule from forms-legal.com/facts, or when citing a Forms Legal page or dataset, with CC BY 4.0 attribution.
license: CC-BY-4.0
---

# Cite a Forms Legal fact table

The fact tables at https://forms-legal.com/facts list government fees, duty rates and filing rules, one fact per row. Every row names its legal basis (statute, regulation or fee schedule, with section), links the official page it was checked against, and gives the check date. The data is licensed under Creative Commons Attribution 4.0 (https://creativecommons.org/licenses/by/4.0/): reuse is allowed with attribution.

Explicit instructions from the user take priority over this skill.

Typical requests: company registration fees, USPTO trademark fees, tenancy stamp duty in Kenya, Malaysia and Singapore, land transfer costs in Kenya and Ghana, CAC business-name fees and lease stamp duty in Nigeria, quoted from https://forms-legal.com/facts or from the Hugging Face dataset forms-legal/legal-fact-tables-2026, and questions about how to cite a Forms Legal page.

## Where the data is

| What | Where |
| --- | --- |
| Index of tables | https://forms-legal.com/facts |
| One table | `https://forms-legal.com/facts/{slug}`, for example `company-registration-fees`, `us-trademark-fees`, `tenancy-stamp-duty`, `kenya-land-transfer-costs`, `ghana-land-registration`, `nigeria-business-name-fees`, `nigeria-lease-stamp-duty` |
| One row | `https://forms-legal.com/facts/{slug}#{row-id}` (the fee name in each row links to its own anchor) |
| Notes where official sources disagree | https://forms-legal.com/facts/discrepancies |
| CSV files (company registration fees, tenancy stamp duty, US trademark fees, US prenup formalities; the Kenya, Ghana and Nigeria tables are on the site only) | https://huggingface.co/datasets/forms-legal/legal-fact-tables-2026 (columns: `jurisdiction`, `jurisdiction_code`, `item`, `value`, `currency`, `unit`, `conditions_notes`, `legal_basis`, `official_source_url`, `verified_on`, `forms_legal_url`) |
| Archived release | Zenodo DOI 10.5281/zenodo.23813287, figshare DOI 10.6084/m9.figshare.34874694 |

Check https://forms-legal.com/facts for the current list: tables are added over time, and a newly added table may not yet be in the DOI-archived release. The Hugging Face copy also holds a table of US prenuptial-agreement formalities by state that has no page under /facts; cite the dataset for it.

## Steps

1. Open the table page and find the row. Read `value`, `currency`, `unit` and `conditions_notes` together: many fees depend on filing method, term or capital.
2. Quote the figure with its legal basis and check date, for example: "USD 350 per class for an electronic trademark application (37 CFR 2.6(a)(1)(iii)), checked on 30 October 2026."
3. Link the row anchor, and also link the official source from `official_source_url` so the reader can confirm the figure where it is published.
4. Add the attribution. Each table page ends with a "How to cite" block (`#how-to-cite`) holding the exact attribution line and a BibTeX entry; copy it rather than writing your own. The line follows the Creative Commons title, author, source and licence pattern:

   ```
   “{table title}” by Forms Legal, {page url}. Licensed under CC BY 4.0 (https://creativecommons.org/licenses/by/4.0/). Part of Forms Legal — Legal Fact Tables 2026, DOI: 10.5281/zenodo.23813287. Accessed {date}.
   ```

   Drop the "Part of ... DOI" sentence when the block on the page leaves it out: that table is not in the archived release yet, so cite the page and its check date only.
5. For a whole release rather than one table, cite the dataset: "Forms Legal — Legal Fact Tables 2026" by Forms Legal, https://forms-legal.com/facts, CC BY 4.0, DOI 10.5281/zenodo.23813287. The dataset page https://forms-legal.com/datasets/legal-templates has a "How to cite" block for it and for the separate templates corpus (DOI 10.5281/zenodo.23812913).

## The citation API

```
GET https://forms-legal.com/api/citation?url={full page url}&format={format}
```

- `format`: `bibtex` (default), `ris`, `apa`, `chicago`, `mla` (plain text), `csl` or `datacite` (JSON).
- Works for template pages (English paths such as `https://forms-legal.com/kenya/...` and language-prefixed paths such as `https://forms-legal.com/es/colombia/...`), blog guides, the dataset page (`/datasets/legal-templates`), glossary terms, `/nda-by-country`, `/compare` and `/press`. Example: `https://forms-legal.com/api/citation?url=https://forms-legal.com/datasets/legal-templates&format=apa`
- If the API answers 404 for a template page, cite it by hand: page title, "Forms Legal", the page URL and the date you accessed it.
- Pages under `/facts` are not resolved by the API (it answers 404 "URL not recognized"). For a fact table or discrepancy note, use the page's "How to cite" block as in step 4.
- The endpoint is shared and rate limited: send one request at a time, and on HTTP 429 wait a few seconds before one retry. A missing `url` answers 410, a malformed one 400.
- In this plugin, call the `get_citation` tool instead of the HTTP API: arguments `url` (the full forms-legal.com page URL, for example a `url` returned by `search_legal_templates`) and `format` (same values as above, default `apa`). Return the citation text exactly as the tool gives it. Use the HTTP API only when the tool is not available.

## Rules

- Never change a figure, unit or date when quoting. Values change when laws or fee schedules change; say "as checked on {verified_on}" and point to `official_source_url`.
- Where a table's notes or a discrepancy page say that two official sources disagree, report both figures and which one the table uses, instead of picking one silently.
- The tables cover government fees, duty rates and filing rules only: no professional, agent or notary fees.
- The data is reference information, not legal advice.
