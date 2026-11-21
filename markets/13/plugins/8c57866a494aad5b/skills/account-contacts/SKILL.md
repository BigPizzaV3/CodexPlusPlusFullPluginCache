---
name: account-contacts
description: "Find and rank the right people at one target company: a contact shortlist for outbound, or a buying-committee map showing economic buyers, technical evaluators, influencers and coverage gaps. Use for 'get the HR leadership at miro.com', 'who are the decision-makers at Acme', 'map the buying committee at Globex', 'contacts at Stripe for a security pitch', 'who owns this at the account'. Not for finding people across many companies (use list-builder) or for looking up a named person (use enrich-contact)."
---

# Account Contacts

Pull the right people at one company, check how reachable they are, and say who to engage first.

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

- **Company** (required): a domain (preferred) or a name.
- **Use case:** prospecting (default), deal acceleration, or renewal and expansion. For a buying-committee request, add the purpose: deal stage, who is already engaged, who is missing, and any hypothesis ("find the economic buyer").
- **Focus (optional):** a function (HR, security, finance, RevOps) or seniority (C-level, VP and above, Director and above), and how many people (default 25, up to 100).

If only a bare company is given, ask once what the contacts are for; if the user declines, build a general prospecting shortlist and say so.

## Workflow

1. **Match the company** with `match-business`. A big brand that resolves to 1-50 employees under "Corporate Managing Offices" probably hit a shell entity, so retry with the other domain. If several companies match, show the top 2-3 (industry, size, HQ) and ask.
2. **Turn the use case into a persona blueprint** before fetching:
   - *Prospecting:* broad coverage of the functions that would buy, weighted to Director, VP and C-level.
   - *Deal acceleration:* the economic buyer, a technical evaluator, procurement, and one Director-level champion candidate.
   - *Renewal or expansion:* current product-owner functions plus an executive sponsor, including Manager and Director levels.
   Apply any function or seniority the user named, and say which roles that dropped.
3. **Contact preference.** If the user did not say what contact data they want, ask using the options in the live `fetch-entities` description and set `has_contact_details` from the answer.
4. **Resolve titles.** `autocomplete` for `job_title`. A specific title uses `job_title` (add `job_level` for executives); a broad function uses `job_level` plus `job_department` only. Title filters are loose, so seniority keeps them tight. For "the CFO at Asana", do not try to match a title as a name: filter the company's prospects by title and level.
5. **Fetch** with `fetch-entities` for prospects, scoping to the company with `business_id` and the persona filters, at the requested count. Make one call that covers the whole blueprint. For adjacent functions the user named (procurement, legal, finance), add a second call so coverage gaps are visible.
6. **Enrich** the fetched people with `enrich-prospects`: `profiles` for tenure and prior roles, and `contacts` if the user wants contact data (`parameters.contact_types` to match their channel).
7. **Account signals (committee requests):** `fetch-businesses-events` for the last 90 days, because funding, new offices and hiring change who matters. A new joiner is a signal only; there is no executive-move event type. Check that an event names the company before using it.
8. **Rank** the returned people against the persona blueprint. All rows are visible, so rank the whole list.

## Reply

- **Target account:** one line with company, domain, industry, size bucket, revenue bucket, HQ, public or private.
- **Use-case frame:** what the shortlist optimizes for, and any overrides.
- **The people:** a table with, for each, name, title, seniority, department ("Unattributed" if empty), reachability, and one clause on the role they fill ("VP-level economic buyer in Sales"). Lead with the top ten when the list is longer.
- **Committee map (committee requests):** group by Economic Buyers, Technical Evaluators, Influencers (procurement, legal, operations, adjacent teams) and Potential Champions. Label a Champion only when the user supplied evidence of engagement; title alone is not enough. Mark each user hypothesis confirmed, contradicted or unresolved.
- **Coverage and risk:** gaps where the use case expected a role and nobody turned up, single-thread risk, and who to contact first with a reason each.
- **Next steps:** more people, deeper context with `account-research`, or career-change signals through `fetch-prospects-events` before a first touch.

## Limitations

- No contact data-quality sort; reachability is judged from the contact filter and enriched fields.
- No sub-department function filter; the finest cut is department plus title.
- Company type is only public or private; a subsidiary cannot be told apart from an independent private company.
- Department is empty for many senior cross-functional roles (Chief X Officer, President, Founder): "Unattributed".
- No CRM or engagement data, so champions depend on what the user tells you.
- Executives at well-known companies often have suppressed contact data; suggest LinkedIn.
