---
name: keyword-opportunity-plan
description: Build a prioritized keyword and content opportunity plan from Linkeddit keyword jobs, search results, and connected search performance data when users ask what buying queries or pages to work on next.
---

# Keyword opportunity plan

Establish the product, intended buyer, and target market from the request. Retrieve existing research with `list_keyword_jobs` and `get_keyword_results`, using returned job IDs. Prefer completed jobs and identify the research date. Returned limits and filtered rows are not the complete keyword universe.

When the user wants first-party search evidence, resolve a visibility project with `answer_projects_list` and use `gsc_queries_get` if connected. Keep the requested days, query impressions, clicks, and average position together. A missing connection is not zero demand. Search performance data does not by itself prove conversions or revenue.

Use `keyword_serp` for selected queries to examine result titles, related searches, and questions. Use `keyword_autocomplete` for expansion when useful. These tools accept a query, not a locale argument in the inspected source. Do not claim results are localized or supply unsupported geography parameters. Suggestions are ideas, not verified search volume.

Cluster queries by buyer task and intent. Keep stored priority scores and conversion-potential estimates distinct from observed demand and your own judgment. Prioritize relevance to the user's product, evidence of demand, plausible page fit, and current coverage. Do not invent traffic forecasts, difficulty scores, or search volume. Cite the returned source links or job IDs.

Return a practical opportunity list: query cluster, buyer intent, evidence, proposed page type, and reason to prioritize. Treat a suggested landing page as a proposal unless its existence and relevance are verified. For a requested content brief, derive the questions to answer and evidence to include; do not fabricate competitor claims. Creating research jobs, publishing pages, and scheduling work require a separate user request and available tools.
