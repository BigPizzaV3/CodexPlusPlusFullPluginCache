---
name: tl-brand-creator-connection
description: Find evidence-backed connections between a named brand and a YouTube creator using the creator's public video statements. Use when the user asks about brand-creator fit, a personal angle for a specific brand and creator, or brand-grounded talking points; use tl-creator-brief for a creator profile without a brand connection.
---

# Creator and brand connection (MCP)

Use ThoughtLeaders records and indexed public video material. This MCP version does not have the CLI skill's local scripts, multi-agent quote verification, or general web-search tool.

## Workflow

1. Call tl_whoami, then tl_skill_track with skill="tl-brand-creator-connection" and stage="started"; retain its run_id. Resolve the creator with tl_channels_find and a named brand with tl_brands_find. Ask the user to disambiguate ambiguous matches.
2. Inspect tl_schema_es and tl_describe. Make a bounded tl_db_es query scoped to the resolved channel and relevant terms. Request IDs, titles, URLs, dates, and transcript highlights only as needed. Use include_highlight=true for excerpts and pricing=true for a dry run if the query may be costly.
3. Build an evidence ledger: theme, excerpt as returned, video title and URL, and timestamp only if actually supplied. Separate direct statements from inference. Never fabricate quotes, timestamps, personal facts, or brand claims.
4. For brand fit, use available brand and sponsorship evidence. Ask for the brand brief when needed; do not present external brand facts as researched.
5. Give an honest fit verdict and grounded talking points. Flag thin evidence and avoid unnecessary sensitive personal details.

Keep internal notes separate from creator-facing copy. If full transcript context or timestamps are unavailable, label excerpts unverified; do not claim the CLI's quote-verification or HTML workflow was run.

Before the final response, call tl_skill_track with skill="tl-brand-creator-connection", stage="completed", the retained run_id, and outcome="completed", "no_results", "failed", or "cancelled". Never include user content, queries, or results in that tracking call.

