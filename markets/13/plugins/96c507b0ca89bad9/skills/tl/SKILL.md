---
name: tl
description: Analyze ThoughtLeaders YouTube sponsorship, channel, brand, video, and audience data through this plugin's MCP tools. Use for multi-step data questions or custom queries; use focused skills for topic research, creator briefs, evidence reviews, saving lists, or views-guarantee questions.
---

# ThoughtLeaders data analysis (MCP)

Use the authenticated ThoughtLeaders tools as the source of truth. This is a multi-step workflow: inspect access and schemas, estimate cost, run bounded queries, and explain evidence and limits. Do not use local tl CLI commands or assume shell scripts are available.

## Workflow

1. Call tl_whoami to confirm authentication, organization, persona, feature access, and balance. On auth failure, ask the user to reconnect the app. Then call tl_skill_track with skill="tl" and stage="started"; retain its run_id.
2. Resolve named channels and brands first with tl_channels_find or tl_brands_find; use canonical IDs afterward.
3. For common look-alike or audience-fit questions, prefer the dedicated similarity/recommender tools. Read the tl://guide/tools resource when choosing among overlapping tools.
4. For custom analysis, inspect tl_schema_pg, tl_schema_es, or tl_schema_fb and tl_describe before writing a query. Use only documented fields and query forms.
5. Before billable work, check tl_balance and the relevant resource rate. Use pricing=true for database dry runs when available, especially for broad or transcript-heavy queries.
6. Narrow data server-side. Use aggregations for counts; do not fetch rows just to count them. Avoid transcripts unless needed and request bounded highlights.
7. State date range, filters, metrics, and assumptions. Separate observed data from inference; include IDs or source links when available.

Never invent credit estimates. Quote estimates only from pricing responses; use tl_balance or tl_usage_history to confirm actual charges. Query tools are read-only. Do not claim to create or update a report, workflow, or other record unless a supported write tool succeeds.

Before the final response, call tl_skill_track with skill="tl", stage="completed", the retained run_id, and outcome="completed", "no_results", "failed", or "cancelled". Do not send user prompts, query text, or returned data to this tracking tool.

