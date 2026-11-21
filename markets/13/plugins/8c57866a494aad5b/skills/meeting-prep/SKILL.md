---
name: meeting-prep
description: "Prepare a 30-minute call brief for a target account: headline signals, attendee profiles, ranked talking points, discovery questions, a suggested agenda, and what to avoid. Use for 'prep me for a call with Acme', 'I have a meeting with Jane at Globex tomorrow', 'pre-meeting research', renewal or QBR meetings. Not for general research with no meeting (use account-research) or for a standalone person lookup (use enrich-contact)."
---

# Meeting Prep

Gather the company, signal and attendee evidence, then write a tight brief the user can read in five minutes.

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

- **Account** (required): a company name or domain.
- **Attendees** (recommended): names with the company, or emails. Without them the brief stays generic.
- **Meeting context** (strongly recommended): purpose, stakes, deal stage, what the user wants to walk out with, known tensions, competitors, what they are selling, and hypotheses to test. If it is missing, ask once; otherwise prepare general notes and say so.

## Workflow

1. **Anchor.** Restate the purpose and desired outcome in 1-2 sentences and pick 3-5 priority topics and any hypotheses.
2. **Match the company** with `match-business`, checking for the shell-entity pattern (big brand, 1-50 employees, "Corporate Managing Offices") and retrying with the alternate domain.
3. **Enrich the company** in one `enrich-business` call, listing the types in `enrichments`: firmographics and technographics, funding-and-acquisitions, strategic-insights and challenges, workforce-trends, competitive-landscape and company-hierarchies, linkedin-posts and website-changes. Gather broadly now; decide what matters at the writing step.
4. **Fetch events** with `fetch-businesses-events` on a 30-90 day window. Keep only events that name this company and tie to the meeting.
5. **Match the attendees** with `match-prospects`, by email when known, otherwise full name plus company (add the `business_id`). Report anyone who does not match; never invent their role. Enrich matched people with `enrich-prospects` and `profiles` for title, tenure and prior roles, plus `linkedin-posts` for recent topics they post about. Add `contacts` only if the user wants to reach out, with `parameters.contact_types` set to `["email"]` unless phone is needed.
6. **Write the brief,** then the TL;DR last. Choose what matters for this meeting, drop generic press, and mark past-dated milestones "verify". Describe engagement or objections only when the user supplied direct interaction evidence. Without it, write 'Engagement unknown'; tenure, prior employers and public company activity do not establish an attendee's attitude toward the user or offering.

## Reply

- **TL;DR:** purpose and desired outcome, the top 3 things to know, a one-line check of each hypothesis (confirmed, contradicted, unresolved), and a suggested opening line.
- **Company snapshot:** industry, size bucket, revenue bucket, HQ, and one paragraph on strategy and challenges.
- **Signals worth raising,** grouped by funding, hiring, tech stack, events, voice and competitors.
- **Attendees:** name, title, department ("Unattributed" if empty), seniority, tenure, contact details if enriched, engagement evidence or "Engagement unknown", why they matter for this meeting, and 1-2 specific talking points. "Profile data limited; verify elsewhere" when thin.
- **Talking points (3-5)** and **discovery questions (3-5),** each tied to a specific fact.
- **Suggested agenda (30 minutes):** open, explore, develop, close on a specific next step.
- **What not to do:** 1-3 concrete failure modes for this meeting.

## Limitations

- Strategy and challenge data come from public filings: empty for private companies and 12-18 months old for public ones.
- No CRM history or deal-stage data; engagement status depends on direct interaction evidence supplied by the user, not profile or public company activity.
- No executive-move event type; infer leadership changes from workforce trends and profiles.
- Size and revenue are buckets; quote them as such.
- Attendees who cannot be matched stay unresolved.
