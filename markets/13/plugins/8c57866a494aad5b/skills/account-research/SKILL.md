---
name: account-research
description: "Build a purpose-driven intelligence brief on one target company: firmographics, funding, hiring and workforce trends, tech stack, recent business events, and peers. Use for pre-call research, renewal or QBR prep, competitive evaluation, and outbound targeting, for example 'research stripe.com for outbound to finance leaders', 'account brief on Snowflake', 'profile this company before my call'. Not for a quick lookup of one data point (use enrich-company), a comparison of several rivals (use competitor-research), or a meeting agenda with attendee profiles (use meeting-prep)."
---

# Account Research

A brief on one company, framed around why the user needs it.

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

- **Company** (required): a name or domain.
- **Purpose** (strongly recommended): one sentence on why the brief is needed and what decision it supports (renewal risk, competitive evaluation against Acme, outbound to finance leaders). If it is missing, ask once; if the user declines, produce general account intelligence and say so.

## Workflow

1. **Anchor on purpose.** Restate it in one sentence and pick 2-4 themes (for renewal risk: workforce changes, executive moves, competing vendors, expansion signals). Themes decide which enrichments to add and how to filter peers.
2. **Match the company** with `match-business` using name and domain. A major brand that resolves to 1-50 employees in "Corporate Managing Offices" is likely a shell entity; retry with the other domain or the plain name. If there is no confident match, ask the user.
3. **Enrich in tiers** with one `enrich-business` call listing the chosen types in `enrichments`:
   - *Always:* `firmographics`, `company-hierarchies`, `funding-and-acquisitions`, `workforce-trends`, `linkedin-posts`.
   - *By purpose:* competitive evaluation adds technographics, webstack and competitive-landscape; renewal or QBR adds company-ratings, challenges and strategic-insights; outbound adds website-changes and website-keywords (keywords tied to the user's offering); investor or M&A adds financial-metrics (optional `date`); buying-intent questions add bombora-intent.
   - *Skip* the rest unless the purpose calls for them. Any enrichment that is skipped or empty gets a one-line note in its section so the reader can tell "not investigated" from "no data".
4. **Fetch business events** with `fetch-businesses-events` for the last 90 days. Useful types: `new_funding_round`, `new_product`, `new_partnership`, `new_office`, `closing_office`, `cost_cutting`, `merger_and_acquisitions`, `outages_and_security_breaches`, and the `hiring_in_*`, `increase_in_*` and `decrease_in_*` department types. Use `employee_joined_company` as a rough signal for leadership hires. Before quoting an event, confirm it actually names the target: industry-wide stories can be attributed to several companies.
5. **Peer set (directional, up to 5).** Derive a sub-category from the purpose, not from a broad industry label: for "vs Databricks", the data-platform sub-vertical; for outbound to finance leaders, the target's go-to-market sub-vertical. Run `fetch-entities` for businesses with those filters and include any competitor the user named, labeled "named by user". If fewer than 3 solid peers come back, skip the section and say so.
6. **Reconcile, then write.** If an event shows a newer funding round than the funding enrichment, trust the event and flag the lag. For public companies, add a one-line financial posture marked "verify". Mark past-dated milestones "verify". Cross-check signals (a new CTO plus a webstack change plus engineering hiring is a timing signal). Write the summary last.

## Reply

- **TL;DR:** the purpose, a 2-4 sentence "why now", the 3 most consequential facts, and 1-3 specific actions.
- **Snapshot:** domain, industry, headcount and revenue buckets, HQ, public or private, founded.
- **Sections:** funding and capital, workforce and hiring, tech stack and website activity, challenges and strategy, recent events (dated, grouped when there are four or more), peers. Skip sections with no data and say why.
- **Next steps:** actions tied to a named signal or person. Offer `account-contacts` for the people to contact and `meeting-prep` if a call is scheduled.

## Limitations

- Challenges, strategy and competitive landscape come from public filings: empty for private companies and 12-18 months old for public ones.
- No similar-companies model; peers are approximated from filters and are directional only.
- No executive-move event type. Leadership changes must be inferred from `employee_joined_company`, hiring events and posts, and flagged as inferred.
- Headcount and revenue are buckets.
- Matching returns no confidence score.
