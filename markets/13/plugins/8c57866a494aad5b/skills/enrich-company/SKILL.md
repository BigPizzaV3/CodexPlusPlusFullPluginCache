---
name: enrich-company
description: "Look up one company, or a pasted list of up to 50 names or domains, and add firmographics, tech stack, funding and acquisitions, workforce and hiring trends, ratings, company hierarchy, website changes, or LinkedIn posts. Use for 'enrich this company', 'what does acme.com use', 'how big is Stripe', 'funding history for Asana', 'add industry and headcount to this list of domains'. Not for finding new companies (use list-builder) or a full multi-section brief (use account-research)."
---

# Enrich Company

Resolve named companies to AgentSource records, then add the data the user asked for.

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

One or more company names or domains, typed or pasted (up to 50 per match call). A name plus a domain matches best. Optional: which kinds of data the user wants.

## Workflow

1. **Match.** Call `match-business` with each company's `name` and/or `domain`. The result is complete, so read it directly.
2. **Check the match.** A well-known brand that resolves to 1-50 employees in a "Corporate Managing Offices" category probably landed on a registered-agent shell. Retry with the alternate domain or the plain company name. The match has no confidence score, so when the candidates look ambiguous, ask the user instead of guessing. Report unmatched rows and do not substitute other companies.
3. **Choose enrichments** from what the user asked for. With no preference, use firmographics plus technographics.

   | Need | Enrichment |
   |---|---|
   | Name, description, size, revenue, location, industry | `firmographics` |
   | Tech stack | `technographics` |
   | Web infrastructure | `webstack` |
   | Rounds, investors, IPO, acquisitions | `funding-and-acquisitions` |
   | Headcount and department trends | `workforce-trends` |
   | Employee-satisfaction ratings | `company-ratings` |
   | Parent, subsidiaries, org tree | `company-hierarchies` |
   | Public-company financials | `financial-metrics` (optional `parameters.date`) |
   | Keywords on their website | `website-keywords` (needs `parameters.keywords`) |
   | Site content changes | `website-changes` |
   | Recent company posts | `linkedin-posts` |
   | Buying-intent topics | `bombora-intent` (topics from `autocomplete` with `business_intent_topics`) |
   | Risks, competitors, strategy (from filings) | `challenges`, `competitive-landscape`, `strategic-insights` |

   Pass the chosen types together in the `enrichments` list of one `enrich-business` call, with up to 50 `business_ids`. Use the schema's exact enum names.
4. **Present** the returned values. For a list longer than five companies, show a table of the requested fields instead of cards.

## Reply

One short card per company (up to 5): name, domain, industry, headcount bucket, revenue bucket, HQ, public or private, then the enrichments requested. Leave out empty fields and name any enrichment that came back empty, so the user can tell missing data from data that was never requested.

## Limitations

- Risks, competitors and strategy come from public filings: empty for private companies and 12-18 months old for public ones. Use funding, workforce trends, events and posts for current signals.
- Headcount and revenue are buckets. Quote the bucket, not an exact number.
- Matching returns an ID or nothing, with no confidence score.
- Every enrichment type uses credits per company, so request only the types the user needs.
