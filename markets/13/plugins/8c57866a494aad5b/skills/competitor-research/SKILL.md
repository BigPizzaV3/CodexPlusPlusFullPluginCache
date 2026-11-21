---
name: competitor-research
description: "Compare two to four rival companies side by side: size, funding, hiring trends, tech stack, recent strategic moves, and overlap with the user's target customers, with a short battlecard per competitor. Use for 'compare Gong and Chorus', 'size up our competitors', 'competitive landscape for X', 'battlecard for renewal'. Not for a deep brief on one company (use account-research) or for finding lookalike companies (use lookalike-accounts)."
---

# Competitor Research

A dated, fact-led comparison of a few named rivals.

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

- **Competitors** (required): 2-4 names or domains. Beyond four, the side-by-side stops being readable; offer a second pass.
- **Purpose** (ask once if missing): battlecard, board update, win-loss prep, renewal.
- Optional: priority angles (pricing pressure, AI roadmap, a region), the user's target customers (to judge overlap), and hypotheses to confirm or contradict.

## Workflow

1. **Anchor.** Restate the purpose, angles and hypotheses in 1-2 sentences.
2. **Match all competitors** in one `match-business` call, with name and domain where available. Check each for the shell-entity pattern (a big brand showing 1-50 employees under "Corporate Managing Offices") and retry with the alternate domain. Drop and flag any that do not resolve confidently; do not proceed with the wrong company.
3. **Enrich** all matched competitors in one `enrich-business` call, listing the types in `enrichments`: firmographics, funding-and-acquisitions, workforce-trends, technographics, competitive-landscape, strategic-insights, challenges, company-ratings, linkedin-posts. Prioritize by the user's angles, and say which were skipped.
4. **Fetch events** with `fetch-businesses-events` for the last 90 days. Keep launches (`new_product`), funding (`new_funding_round`), `merger_and_acquisitions`, `new_office` and `closing_office`, `cost_cutting`, partnerships, and notable department hiring or cuts. Before using an event, check that it names the competitor.
5. **Judge overlap** per competitor (High, Partial, None) against the user's stated target customers, using firmographics. If none were given, write "Not assessed".
6. **Check each hypothesis** as confirmed, contradicted or unresolved, citing the data point behind the call.

## Reply

- **Purpose and hypothesis check** in two or three lines.
- **Side-by-side table:** company, domain, HQ, headcount bucket, revenue bucket, founded, public or private, latest funding, latest dated move.
- **Per competitor:** snapshot, recent moves (dated), positioning in the company's own terms from strategic-insights or competitive-landscape, workforce direction, challenges, overlap, and three discovery questions rooted in specific facts.
- **Data quality:** unresolved names, empty enrichments, stale records, contradictions.
- Offer `account-contacts` to map the buying committee at a specific account.

## Limitations

- Challenges, strategy and competitive landscape come from public filings: empty for private rivals and 12-18 months old for public ones. For private companies lean on funding, events, workforce trends, tech stack and posts.
- Headcount and revenue are buckets; compare buckets, not numbers.
- Review-site sentiment (G2, TrustRadius) and earnings-call content are not in the data.
- No similar-companies model. For rivals beyond the named ones, use `lookalike-accounts` or the competitive-landscape results, and label them as approximations.
