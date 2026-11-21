---
name: audit-and-research
description: Run SeoPerseo page audits, SERP analysis, keyword research and AI-visibility checks after confirming the credit cost, and report the findings with their evidence.
---

Use this skill when the user asks to audit a page or site, check a SERP, research keywords, or check how AI assistants talk about their site.

## Always read before you spend

1. Resolve the project with `projects_list`.
2. Check whether the answer already exists for free:
   - `page_audit_latest` or `page_audit_list` for a page;
   - `site_scan_get` for a crawl;
   - `work_list` for saved documents.
3. If stored evidence answers the question, use it and say when it was collected. Offer a fresh run only if the data is old or the user asks for it.

## Spending credits

4. Before calling any of `page_audit_run`, `serp_analyze`, `serp_ai_mode`, `mentions_answer_space`, `keywords_ideas`, `keywords_suggestions`, `keywords_overview`, `site_scan_run` or `ai_visibility_run`, state the credit cost the tool description reports and ask the user to confirm. Do not call it without an explicit yes.
5. Batch work into a single call where the tool supports it. `keywords_overview` takes up to 50 keywords in one request, which costs the same as one request.
6. `site_scan_run` and `ai_visibility_run` are long running and return a job ID. Poll with `jobs_get` until the job finishes, then report the result. Tell the user you are waiting instead of guessing the outcome.

## Reporting

7. Give the user the finding, what it means, and the one action that follows from it. Do not dump raw tables.
8. Attach the source and collection date to every number.
9. If a run fails or returns nothing, say so and report the reason the tool gave. Never fill the gap with an estimate.

## Boundaries

- Only audit URLs on domains that belong to the resolved project, unless the user explicitly asks for a competitor comparison that the tool supports.
- Never repeat a paid call after a failure without asking the user again.
- If the account has not enough credits, report the balance from `credits_balance` and stop.
