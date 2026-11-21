---
name: get-started
description: How to find job offers in Spain with the SylvaraJob tools. Use it when the user asks for jobs, vacancies or job offers in Spain, in any language: which tool to call, how to pass the search terms with their English translation, how to filter by province, city, country or work mode, and how to open the public record of an offer.
---

# Searching job offers on SylvaraJob

SylvaraJob exposes three read-only tools. No account, sign-in or key is needed. Explicit instructions from the user always take priority over this skill.

## 1. Search offers: `buscar_ofertas`

1. Put the profession or keyword exactly as the user said it in `terminos`, together with its English translation (for example `["enfermera", "nurse"]`). The server expands every term with synonyms in Spanish, Catalan, Portuguese, English, French, Italian, Chinese and Japanese and ignores accents, plurals and gender.
2. Add the optional filters the user mentioned: `provincia`, `ciudad`, `pais` (ISO-2 code, `ES` for Spain), `modalidad` (on-site, remote or hybrid) and `origen` (own or external offers). Use `listar_categorias_y_provincias` first if you are unsure which values are valid.
3. Results list offers published on SylvaraJob first and then external offers published by other companies on their own career sites. External offers are marked as such and only carry title, company, city, date and a link to the source.
4. Present each offer with title, company, city, date and link, say how many results there are in total, and offer the next page if there are more (maximum 20 per page).

## 2. Open an offer: `ver_oferta`

Use the `id` returned by the search: a number for offers published on SylvaraJob, or `ext-N` for external offers. Summarise the public record (description, requirements, conditions, salary when the company publishes it) and give the public link where the user can apply.

## 3. Browse what is available: `listar_categorias_y_provincias`

Call it when the user asks which categories, provinces, cities, countries or sources currently have open offers, or to validate a filter value before searching.

## Limits

- The tools are read-only: never claim to have applied on the user's behalf, created an account or contacted a company. Applications happen on the offer's own link.
- The tools never return personal data of candidates or recruiters; do not promise contact details that are not in the public record.
- Do not invent offers, counts or salaries: report only what the tools return.
