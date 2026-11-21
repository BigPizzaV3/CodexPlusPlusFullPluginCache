---
name: enrich-contact
description: "Look up one person or a small pasted list of people and return their professional profile and contact details: work email, phone, LinkedIn, title, seniority, department, work history, and recent job changes. Identify people by email, LinkedIn URL, phone number, or full name plus company. Use for 'find the email for Jane Smith at Acme', 'enrich this contact', 'who is this person', 'background on these attendees'. Not for finding new people by role (use list-builder or account-contacts) or for drafting outreach."
---

# Enrich Contact

Resolve people to AgentSource records, then add the profile and contact data the user asked for.

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

For each person, one of: an email, a LinkedIn URL, a phone number, or a full name with a company name or domain. A name without a company cannot be matched. Up to 40 people per `match-prospects` call. Optional: whether the user wants contact details, a profile, or career changes.

## Workflow

1. **Pick the strongest identifier** for each person: email, then LinkedIn URL, then phone, then name plus company. Do not fan out several strategies for one person. If the user gave a role instead of a name ("the CFO at Asana"), do not match on the title; use `match-business` to get the company, then `fetch-entities` for prospects filtered by title and seniority, and let the user choose.
2. **Match.** Call `match-prospects`. For a name plus company, add the company's `business_id` from `match-business` when you have it. Results are complete: a person is either matched or null. A typo in an email is a miss; do not retry it as a name search, since that could return a different person.
3. **Report misses.** Say which people did not match and why a retry might help: an email, LinkedIn URL or company domain improves the odds. Enrich only the matched people. Do not replace an unmatched person with someone similar.
4. **Enrich** the matched people with `enrich-prospects`, naming the types in `enrichments`:
   - `profiles` for title, location, work history and education.
   - `contacts` for email and phone. Set `parameters.contact_types` to `["email"]` unless the user needs phone numbers too; leaving it empty requests both.
   - `linkedin-posts` for the person's recent posts, if asked.
   Company context, if asked for, comes from `enrich-business` with `firmographics` on the employer's `business_id`.
5. **Career changes,** if asked: `fetch-prospects-events` with `prospect_changed_role` or `prospect_changed_company` and a `timestamp_from`. These are the only people-level event types.
6. **Present** the returned values. For more than five people, use a table instead of cards.

## Reply

A card per person (a table for more than five): name, title, company, seniority, department ("Unattributed" if empty), professional email, phone, LinkedIn. When the user asked for background, add a 3-5 sentence synopsis written only from the returned data: current role, one or two earlier roles, tenure, and any recent change. Say "not available" for thin profiles instead of guessing.

## Limitations

- High-profile executives often have suppressed contact data. Suggest LinkedIn instead of cold email.
- No per-contact accuracy score and no "last updated" date. Treat a professional email plus a phone as the practical quality signal.
- Seniority and department are coarse; department is empty for many Chief X Officer, President and Founder roles.
- Do not use contact data for anything beyond the lookup the user asked for.
