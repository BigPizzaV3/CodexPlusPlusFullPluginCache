---
name: rankzero-workflows
description: Use RankZero for AI search visibility analysis, brand reporting, competitor research, tracked prompts, citations, and connected GA4/GSC analysis. Use when the user asks about their RankZero data, AI SEO performance, brand visibility in AI answers, competitors, prompts, sources, or related traffic data.
---

# RankZero workflows

RankZero is an AI-search visibility platform. Prefer its live MCP data over assumptions when answering questions about a connected brand.

## Brand context

- Start with `list_brands` when the user has not identified a brand or when the brand is ambiguous.
- Pass `brand` on every call. It accepts a name, domain, UUID, or number from the last brand list.
- `set_active_brand` sets a default for calls that omit `brand`. That default is best-effort session memory, so prefer passing `brand`.
- If the user names a domain, resolve it through `list_brands` or pass the domain to a supported brand argument rather than guessing an ID.

## Core analysis

For a high-level health check, use:
1. `get_brand_overview`
2. `get_brand_competitors`
3. `get_ai_mentions`

Overview and mentions accept `period`: `24h`, `7d`, `30d`, or `90d` (default `7d`). These are rolling windows, not arbitrary historical ranges. State the window and distinguish measurements from interpretation; do not present overlapping windows as consecutive periods.

## Content and AI-search opportunities

- Use `list_tracked_prompts` to list active tracked prompts, 20 per `page`, optionally filtered by `search`.
- Use `search_knowledge_base` with `query` to search RankZero's documentation, guides, glossary, and blog (top five matches).
- Use `get_citation_sources` for cited domains by usage. It accepts the same periods (default `30d`), optional `country` and `provider`, and `limit` (default 50).
- Do not claim that a recommendation will guarantee rankings or AI citations.

## Traditional SEO + AI SEO

When the brand has integrations connected:
- Use `get_gsc_performance` for clicks, impressions, CTR, and position. `dimensions` accepts `date`, `query`, `page`, `country`, `device`, or `searchAppearance` (default `["date"]`). Dates use `YYYY-MM-DD`, defaulting to the last 28 days through today.
- Use `get_ga4_report` for traffic and behavioral data with chosen `metrics` and `dimensions`. Dates accept calendar or relative values (default `28daysAgo` to `today`).
- Compare GSC/GA4 metrics with AI visibility only when the date ranges and dimensions are comparable.

If a Google integration is unavailable, report that limitation instead of inventing the data.

## Reporting style

When asked for a report:
- Lead with the measured metrics.
- Include the time window.
- Highlight meaningful changes, competitors, mentions, and sources when the data supports them.
- Separate observations from recommendations.
- Keep recommendations concrete: pages, prompts, sources, or technical/content areas to investigate.

## Safety and accuracy

RankZero data is account-scoped. Never imply access to brands the connected account cannot access. Do not expose authentication tokens or ask the user to paste credentials.
