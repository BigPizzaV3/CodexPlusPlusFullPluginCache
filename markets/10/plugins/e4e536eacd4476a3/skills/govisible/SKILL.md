---
name: govisible
description: Use when the user asks about their brand's AI visibility, GEO (generative engine optimization), mention strength, sentiment, share of voice, citations, buyer prompts, AI answers, competitor visibility, or a GoVISIBLE audit or monthly report. Retrieves read-only data from the connected GoVISIBLE account and explains it without inventing metrics.
---

# GoVISIBLE

Use the connected GoVISIBLE MCP server to answer questions about how brands appear in AI-generated answers. All tools are read-only and return only data the signed-in GoVISIBLE account can access.

## When not to use

- Do not use GoVISIBLE tools for requests unrelated to AI visibility, GEO, or the user's GoVISIBLE projects.
- GoVISIBLE cannot create, edit, or delete projects, run new benchmarks, change settings, or process payments. Say so instead of calling a tool.
- Never try to access or describe data from another customer's GoVISIBLE account.

## Choose the project first

1. Most tools need a `projectId`. If the user has not identified a project, call `list_projects`.
2. If exactly one project matches the brand the user named, use it. If several match or none is named, ask the user which project to use.
3. Use `get_brand_info` when you need the project's brand profile, tracked competitors, or configured AI engines.

## Pick the right tool

| User asks for | Tool |
| --- | --- |
| Overall visibility | `get_visibility` |
| Visibility by AI engine, date, cluster, journey, persona, intent, or competitor | `get_visibility_by_AiEngine`, `get_visibility_by_date`, `get_visibility_by_cluster`, `get_visibility_by_journey`, `get_visibility_by_persona`, `get_visibility_by_intent`, `get_visibility_by_competitors` |
| Mention strength | `get_mention_strength` and its `_by_` variants |
| Sentiment | `get_positive_sentiment`, `get_negative_sentiment` and their `_by_Clusters` / `_by_AiEngines` variants |
| Share of voice | `get_ShareOfVoice`, `get_ShareOfVoice_by_Clusters`, `get_ShareOfVoice_by_AiEngines` |
| Citations, cited websites, pages, and domains | `get_citations`, `get_citation_domains`, `get_websitecitation_share`, `get_websitecitation_pages`, `get_page_intelligence` and related citation tools |
| Competitor leaderboard | `get_competitors_analysis` |
| Buyer prompts and per-prompt results | `list_prompts`, `get_prompt_data`, `get_prompt_drilldown` |
| Raw AI answers and their citations | `list_ai_answers` |
| Benchmark run history and KPI trends per run | `list_runs`, `get_brand_run_metrics` |
| Complete audit report | `get_audit_report` |
| Monthly report for a calendar month | `get_monthly_report` |

Prefer one report tool (`get_audit_report` or `get_monthly_report`) over stitching many metric tools together when the user asks for a report.

## Dates and filters

- Omit `startDate` and `endDate` unless the user asks for a specific period. The default window is the last calendar month of completed benchmark runs.
- Pass dates as `YYYY-MM-DD` only when the user asks for a custom range.
- Preserve every filter the user gives: date range, AI engine, cluster, journey, persona, intent, and competitors.

## Presenting results

- State the project, reporting period, and filters that the tool returned.
- Lead with the most relevant metrics, then supporting detail.
- Keep measured GoVISIBLE data separate from your interpretation or recommendations.
- Keep answers concise unless the user asks for a detailed analysis.

## Accuracy

- Treat tool results as the only source of GoVISIBLE metrics. Never invent, estimate, or fill in missing values.
- If a tool returns an error, no data, or a truncated result, say so plainly and suggest a narrower date range or a different filter.
- If the connection is not authorized, ask the user to reconnect GoVISIBLE. Never ask for or repeat passwords, OAuth tokens, or API keys.
