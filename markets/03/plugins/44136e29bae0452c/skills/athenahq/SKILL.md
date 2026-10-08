---
name: athenahq
description: Report how AI assistants (ChatGPT, Perplexity, Gemini, and others) talk about a brand using AthenaHQ analytics. Trigger for AI search visibility, share of voice, mention or citation rates, ranking position vs competitors, cited sources and pages, tracked prompts, and AI-response sentiment. Do not trigger for traditional SEO (Google organic rankings, keywords, backlinks), for writing or publishing content, or for changing AthenaHQ configuration — the tools are read-only.
---

# AthenaHQ: brand visibility in AI search

Use the AthenaHQ MCP tools to answer questions about how AI assistants
mention, cite, and rank a brand versus its competitors. All tools are
read-only: they query the user's own AthenaHQ analytics and never change
anything.

## Always resolve the website first

1. Every tool except `list_websites`, `get_credits_organization`,
   `list_pitches`, and `get_pitch` requires a `website_id` (UUID).
2. Start with `list_websites` (empty arguments `{}`). One website: use it.
   Several: ask the user which one, or infer from the brand they named.
3. Before date-filtered queries, call `get_date_range` to learn the earliest
   and latest analyzed dates. Never query outside that range.

## Metric questions → tools

All metric tools take `website_id` plus a `filters` object.
`filters.start_date` (YYYY-MM-DD) is required; `end_date`, `models`,
`prompt_ids`, `competitor_ids`, `location_ids`, `persona_ids`,
`prompt_tags` are optional narrowing filters.

- "Share of voice" / "how visible are we vs competitors" →
  `get_share_of_voice_cumulative` (per-competitor totals for the range) or
  `get_share_of_voice_time_series` (daily trend).
- "How often are we mentioned" → `get_mention_rate_cumulative` /
  `get_mention_rate_time_series`.
- "How often are we cited/linked" → `get_citation_rate_cumulative` /
  `get_citation_rate_time_series`.
- "Where do we rank in AI answers" → `get_position_cumulative` /
  `get_position_time_series`.

Pick cumulative for "who is winning" comparisons and time series for
"how is it trending" questions. State the date range you used in the answer.

## Drill-down workflows

- Which domains AI models cite: `get_sources` (root domains, classified
  owned / competitor / partner / third_party) → `get_source_pages` for
  individual URLs with per-URL trends.
- What AI assistants actually said: `get_responses` (paginated via
  `page_num` / `page_size`, max 100 per page) — includes sentiment,
  sources, and ranking per response.
- Tracked prompts (the queries AthenaHQ monitors): `get_prompts`.
  Tracked competitors: `get_competitors`. Geo targets: `get_locations`.
- Content performance: `get_content_hub_sheets` (discover tabs) →
  `get_tracked_content` (list with citation/impression metrics, filter by
  `sheet_id`) → `get_content_detail` (full text of one item) or
  `get_content_citation_prompts` (which prompts cite it).
- Plan usage: `get_credits_organization` / `get_credits_website`.
- Sales pitch reports (org-wide): `list_pitches` → `get_pitch`.

## Answering style

- Lead with the number and the comparison the user asked for; name the top
  competitors by name.
- Note the analyzed date range and any filters applied.
- If a tool returns empty data, check `get_date_range` and widen the range
  before concluding there is no data.

## Boundaries

- Never claim to add, edit, or delete anything — no tool can. Point the
  user to the AthenaHQ dashboard (https://app.athenahq.ai) for
  configuration changes such as adding competitors or prompts.
- These analytics cover AI assistant answers, not Google organic search.
  Redirect traditional SEO questions instead of answering with these tools.
