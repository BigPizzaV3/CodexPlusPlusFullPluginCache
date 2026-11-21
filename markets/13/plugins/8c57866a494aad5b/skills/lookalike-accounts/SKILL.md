---
name: lookalike-accounts
description: "Find companies that resemble a seed company by rebuilding its industry, size, region and tech-stack profile and searching for others that share it. Use for 'find companies like Stripe', 'lookalike accounts for Acme', 'similar companies to our best customer', 'expand my territory', 'extend this account list'. Not for similar people (use list-builder) or for comparing named rivals (use competitor-research). Results are an approximation, not a similarity score."
---

# Lookalike Accounts

Rebuild the profile of one seed company, then search for companies that share it.

## Connector rules

Use only the AgentSource tools in your tool list. Each tool's live description and input schema are authoritative; if this skill disagrees with a tool, follow the tool.

- **`tool_reasoning`** is required on every call: the user's original request in their exact words (up to 2000 characters), reused unchanged across chained calls for the same task. Never replace it with a per-step rationale or add personal data the user did not write.
- **Sessions:** reuse `session_id` from the previous response while continuing the same request; omit it to start a new request. Never invent one.
- **Chaining by ID:** pass `business_id` and `prospect_id` values from `match-business`, `match-prospects` or `fetch-entities` results. Do not re-match entities that a fetch already returned.
- **`autocomplete` first**, one concept per call, for `linkedin_category`, `naics_category`, `company_tech_stack_tech`, `job_title`, `interests`, `skills`, `business_intent_topics`, and US `city_region`. Use the returned values as-is. Use ISO codes directly for countries (`US`) and regions (`US-CA`).
- **What you see:** every tool returns full results inline. `fetch-entities` returns up to `page_size` rows per call (at most 500) and a `next_cursor` for the next page; `fetch-entities-statistics` returns aggregates over every match.
- **Credits:** every data call uses credits on the user's AgentSource account. Request only the rows and enrichments the task needs, count with `fetch-entities-statistics` before a large pull, and confirm with the user before fetching more than 100 rows or enriching contact details for more than 50 people.
- **Limits per call:** `match-business` 50 companies, `match-prospects` 40 people, `enrich-business` and `enrich-prospects` 50 IDs, `fetch-businesses-events` 20 companies. Name several enrichment types in one `enrichments` list rather than one call each.
- **Presenting:** show returned records in a table with the fields that matter for the task. Never mention session IDs or internal table names.
- **Event details:** if a fetch used the `events` filter and the user did not already ask for event details, ask before calling `fetch-businesses-events` or `fetch-prospects-events`.
- **Lists:** work from lists pasted in chat or text from attached files, in batches that respect the limits above.

## Input

- **Seed company** (required): a name or domain. If the user gives a person, or asks for similar contacts, use list-builder instead; this skill returns companies.
- **Count:** default 25, up to 100.
- **Overrides (optional):** country or region focus, size or revenue bucket, public-only, and extra tech-stack requirements.

## Workflow

1. **Match the seed** with `match-business`, using name and domain. If several candidates return, pick the one whose domain matches and say which you chose. If none resolves, ask for a domain.
2. **Check the seed.** A big brand that resolves to 1-50 employees under "Corporate Managing Offices" is a shell entity. Retry with the other domain, since a wrong seed produces unrelated results.
3. **Read the seed's profile** with `enrich-business` and `firmographics` plus `technographics`. Take: industry (LinkedIn or NAICS, whichever is populated), headcount and revenue bucket, country (or the region the user asked for), and the top 3-5 technologies, favoring category-defining tools (CRM, marketing automation, data warehouse, cloud) over ubiquitous ones. Skip anything that comes back empty and do not guess.
4. **Resolve values** with `autocomplete` for the industry and each technology. For flagship vendors, try the product-qualified name first ("Snowflake Data Cloud", "Stripe Payments"), because the bare name often returns noise. Drop anything that does not resolve cleanly, and tell the user.
5. **Apply overrides,** replacing or extending the profile. Keep one industry taxonomy and one location level.
6. **Size the pool** with `fetch-entities-statistics` (`entity_type: businesses`, same filters). If it is smaller than the count asked for, relax the most restrictive filter first (the last technology, then the others, then widen the headcount bucket to an adjacent one) and re-check. If it is far larger than needed, add a technology back or narrow the region. For a country-scoped pool, read the per-location breakdown, because the headline count may include other countries.
7. **Fetch** with `fetch-entities` for businesses with the final filters, plus `business_id` set to the seed's ID from the match with `negate: true`, because a company matches its own profile. Set `page_size` to the count.

## Reply

- **Header:** "Lookalikes for [seed] ([domain])" and the profile used: industry, headcount bucket, revenue bucket, country or region, technologies. State the size of the pool.
- **Pattern notes (2-4 bullets):** dominant geography, size concentration, how dense the tech overlap is (tech data is not populated on every company), and any widening you had to apply ("industry widened because the seed had no LinkedIn category").
- **Results table:** name, domain, industry, headcount and revenue buckets, country.
- **Next steps:** offer the next page, `list-builder` for the people at these accounts, or `enrich-company` to go deeper on one.

## Limitations

- There is no similarity model or score. Results are companies that match the rebuilt filters, in fetch order, not ranked by closeness.
- Technology data is incomplete, so stacking several technologies can shrink the pool faster than expected.
- If neither industry taxonomy is populated on the seed, the match falls back to size, region and technology, which is looser. Say so.
- Headcount and revenue are buckets; a seed near a bucket edge can look further from a neighbor than it is.
- No metro-area filter.
- Returns companies only, not similar people.
