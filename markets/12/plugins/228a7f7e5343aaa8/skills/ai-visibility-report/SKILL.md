---
name: ai-visibility-report
description: Show whether AI answer engines recommend a brand, which Reddit threads they cite, and where competitors win, even with no ReddGrow setup. Use for AI visibility, citations, competitor comparisons, and "why does AI recommend my competitor" questions.
---

# AI visibility, won through Reddit

AI answers lean on Reddit threads. The goal: find the threads AI cites for the user's category, then write the reply that puts their brand in them.

## Start here: the AI visibility scan

1. Call `get_ai_visibility_report` if the user may already have a scan.
2. `ready`: present it (see "Present the report" below).
3. `processing`: say the scan is running on 4 AI engines and that we will notify the user by email when it is ready. They can then open ReddGrow (`appUrl`) or ask here. Do not say the results are emailed.
4. `failed`: say the scan did not finish and point to `appUrl`.
5. `none`: set up a scan. You need the brand's domain and name (ask if missing). Propose 10 questions a buyer would ask an AI in their category, and up to 3 competitor domains. Show them in the chat and let the user approve or edit. Then call `run_ai_visibility_report` once with `domain`, `brandName`, `competitors` and `prompts`.
6. If `run_ai_visibility_report` returns `needs`, ask the user for exactly the items listed, then call it again.
7. On `processing`, relay the line from step 3.

Send only the domain, brand name, competitors and questions. Do not ask for anything else.

If the user asks for something the scan cannot do (daily tracking, more questions, competitor monitoring, Reddit engagement), say that is part of ReddGrow's paid plans, which monitor Reddit every day, draft comments and posts, and track competitors, and point to https://reddgrow.ai/pricing. Only say this when asked.

## Present the report

Lead with the Reddit threads, because they are what the user can act on:
1. `summary.redditThreadsAiCites`: the threads AI engines cite. Name which engines cite them.
2. `summary.questionsWhereCompetitorsWin`: buyer questions where AI named competitors instead.
3. `summary.visibilityPct`, `summary.perEngine`, `summary.topCompetitor`.
4. Give `appUrl` for the full view in ReddGrow.
5. Next step: pick a cited thread, ask the user to paste the post text, and use the draft-reddit-reply skill.

## Users who already track a brand in ReddGrow

These tools read the account, read-only. Use them when the report tools say a report already exists or the user asks for trends.

| Question | Tool |
|---|---|
| Is visibility going up or down? | `aeo_visibility_timeline` (days, or from and to) |
| How does the brand rank against competitors? | `aeo_brand_ranking` |
| Which sites do AI engines cite? | `aeo_source_domains` |
| Which Reddit threads do AI engines cite? | `aeo_list_citations` |
| Where is the brand mentioned on Reddit? | `list_brand_mentions` |
| Mention counts and sentiment | `get_brand_monitor_stats` |
| Saved comment drafts and status | `list_drafts` |

Rules:
- Report only numbers the tools returned. If an account tool returns nothing, the user has no tracked brand yet: offer the scan instead of saying there is no data.
- Filter with `engine`, `country`, `brand_id` only when the user asks.
- Do not state how often AI engines cite Reddit overall. Only report what the report returned.
