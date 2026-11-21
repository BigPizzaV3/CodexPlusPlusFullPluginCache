---
name: lead-qualifier
description: Finds and prioritises German companies that match an ideal customer profile (size, industry, region, age, financial criteria) using the Implisense search, lookalike and profile tools. Use when the user wants a target list, prospects, or to qualify a list of companies against criteria.
---

# Lead Qualifier

Turn an ideal customer profile (ICP) into a prioritised list of German companies with reasons. Answer in the user's language.

## Workflow

1. **Clarify the ICP** if it is not given: size class, industries, region, company age, financial criteria (e.g. profitable, minimum equity ratio) and anything else that matters. Suggest an example ICP if the user is unsure.
2. **Find candidates**:
   - From criteria: translate the ICP into `search_companies` filters — `industry` (WZ 2008 codes or prefixes), `size` (MICRO, SMALL, MEDIUM, LARGE), `location` (e.g. `state:DE-BY`), `min_age`/`max_age`, plus `query` for keywords. Start with the default limit of 20 and page with `offset` only if needed.
   - From example customers: resolve them with `company_profile`, then call `similar_companies` with their IDs as `seed_ids` to find lookalikes.
   - From a list the user brings: resolve each company with `company_profile`.
3. **Check the best candidates** with `company_profile` (`include=financials`) where the ICP has financial criteria.
4. **Contacts** only if the user asks: follow the `contact-finder` skill for the companies they pick. Each search costs 3 Implicents and takes about a minute, so confirm before running it for more than one company.

## Output

A list sorted into High, Medium and Low fit, with one or two sentences per company on which ICP criteria it meets or misses. Collect clearly unsuitable companies briefly at the end instead of explaining each one.

## Rules

- Qualitative fit (High / Medium / Low), no invented scores.
- Use only what the tools return; never invent contacts, buying signals or figures.
- For a risk check of a list use `portfolio-analyst`; for one company in depth use `company-researcher`.
