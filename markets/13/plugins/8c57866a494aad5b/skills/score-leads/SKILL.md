---
name: score-leads
description: "Score and tier a list of target accounts (A, B, C by ICP fit, buying intent, recent trigger events and hiring momentum) or a list of people (Hot, Warm, Cold against a buyer persona and ICP), with a one-line 'why now' per row. Use for 'score these accounts', 'rank this list by ICP fit', 'prioritize my leads', 'which of these should I call first', 'tier my inbound leads'. Works on lists pasted in chat. Not for building a new list (use list-builder) or for research on a single company (use account-research)."
---

# Score Leads

Resolve a list, gather evidence for each row, then apply a transparent rubric the user can adjust. The scoring is your reasoning over the returned data; there is no built-in scoring engine.

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

## Choose a mode

- **Accounts:** the list is companies (names, domains). Output is a tier A/B/C with a score per account.
- **People:** the list is leads (emails, LinkedIn URLs, or name plus company). Output is Hot, Warm or Cold per person.

## Input

- **The list** (required), up to 50 accounts or 40 people per match call.
- **ICP** (required): industries, headcount and revenue buckets, countries or regions, optional tech vendors, optional intent topics. For people, also the **buyer persona**: titles, seniority, department.
- **Optional:** a source label per lead (demo request, pricing inquiry, webinar) passed through as given; weights; tier thresholds; trigger window (default 90 days).

If the ICP is missing, ask for it; do not invent one.

## How many rows to score

Every enrichment and event call returns full values, but each one uses credits per row. Score up to 50 rows in one pass; for more, score the first 50 and offer to continue in batches.

## Workflow

1. **Lock the rubric.** Restate the ICP and persona. Resolve free-text values with `autocomplete`, one term at a time. If an intent topic does not resolve, drop it and mark that axis "not configured" instead of "no intent".
2. **Resolve identities.** Run `match-business` (accounts) or `match-prospects` (people); results are complete, so read them directly.
   - An email is a unique key: a miss is a miss, never a fallback to a name search.
   - A name plus company match at a large company can be ambiguous; mark it "Verified, check".
   - A role without a name ("the CFO at Asana") does not match as a name: match the company, then use `fetch-entities` filtered by title and seniority and let the user pick.
   - Check each resolved company for the shell-entity pattern (a big brand with 1-50 employees under "Corporate Managing Offices") and retry with the alternate domain.
   - Tag each row: resolved, verified-check, ambiguous (ask the user), or failed. Never drop a row silently.
3. **Gather evidence,** naming several types per enrichment call and passing up to 50 IDs:
   - Accounts: `enrich-business` with firmographics, technographics, workforce-trends, funding-and-acquisitions, linkedin-posts and website-changes, then `fetch-businesses-events` (20 companies per call) for the trigger window.
   - People: `enrich-prospects` with `profiles` (add `contacts` if the user wants contact data), `enrich-business` with `firmographics` for their employer, and `fetch-businesses-events`. For job-change signals, `fetch-prospects-events` (`prospect_changed_role`, `prospect_changed_company`).
   - Intent: a `fetch-entities` scoped with `business_id` values and `business_intent_topics` shows which accounts have the topic; `enrich-business` with `bombora-intent` adds topic scores.
   Before using an event, check that it names the account; industry-wide stories get attributed to several companies.
4. **Score.**
   - *Accounts, 0-100:* default axis weights are Fit 45, Intent 25, Trigger 25, Workforce 5.
     - **Fit:** use only criteria specified in the ICP. Maximum points: industry 25, headcount 20, revenue 20, geography 15, company age 10, named technology 10. Industry earns 25 for a match or 10 for an explicitly accepted adjacent category. Headcount and revenue earn 20 for the requested bucket, 12 for one bucket off, 4 for two off. Geography earns 15 for a match or 8 for an explicitly accepted broader region. Age and technology earn 10 for a match. Other evidenced mismatches earn 0. Exclude unspecified criteria; report missing evidence and exclude that criterion from the denominator. Fit score = 100 times earned points divided by maximum points for the criteria actually assessed. If none can be assessed, Fit is unknown.
     - **Intent:** 90, 70 or 50 for three or more, two or one resolved topics active; 0 only when a completed topic check finds none. Without configured topics or sufficient coverage, mark the axis unknown.
     - **Trigger:** use the strongest returned event. Type score: funding or M&A 95; product launch, hiring surge or large site change 75; partnership or new office 55; generic company news 25. Multiply by recency: 0-14 days 1.0, 15-30 days 0.7, 31-60 days 0.4, 61-90 days 0.2. Use 0 if a completed event query returns no qualifying events; if the query fails or coverage is unknown, mark the axis unknown. Do not infer a CEO change from a generic employee-joined event.
     - **Workforce:** use 90 for evidenced strong growth or a hiring surge in the target department, 55 for modest growth, 20 for flat or shrinking. Cite the returned trend; do not infer exact growth percentages from headcount buckets. Without sufficient evidence, mark the axis unknown.
     - **Total:** sum(axis score times axis weight) divided by sum(available axis weights), rounded to the nearest integer. Report missing axes and assessed fit criteria. If no axes have evidence, leave the score and tier unassigned. Default tiers: A at 75 or more, B at 50-74, C below.
   - *People, three checks:* persona fit (title, seniority, department against the persona), account fit (ICP), and a trigger (account event or a recent role change for them). Hot needs persona fit, account fit and one trigger; Warm needs persona plus either; everything else is Cold. A lead missing both a professional email and a phone gets "verify contact data before outreach".
5. **Write "why now"** as one sentence anchored on the strongest signal, never the score restated. Be explicit when a strong trigger sits on a poor fit ("fresh funding, but the size bucket keeps this in C").

## Reply

- **TL;DR:** counts resolved, ambiguous and failed; the tier distribution; the top 3 with their "why now".
- **Ranked table:** rank, account or person, tier, score or checks, axis detail, why now. Use "-" for a redistributed axis.
- **Resolution summary:** input, resolved to, status; list ambiguous rows with candidates for the user to pick.
- **Rules used:** weights, thresholds, window, and anything redistributed.
- **By tier:** A or Hot for personal outreach within a day; B or Warm for a sequence that opens with the "why now"; C or Cold to watch. Offer to adjust the weights and re-rank without new calls.

## Limitations

- No scoring engine or per-row confidence; the score reflects the data fetched and your reading of it.
- Headcount and revenue are buckets, so banded scoring is the right resolution.
- Filing-based challenge and strategy data is empty for private companies and 12-18 months old for public ones; use events, funding, workforce trends and posts for current state.
- No CRM engagement data (deal stage, last activity); workforce momentum is the substitute and the gap is stated.
- One industry taxonomy and one location level per query.
- Department is empty for many Chief X Officer, President and Founder roles: "Unattributed".
