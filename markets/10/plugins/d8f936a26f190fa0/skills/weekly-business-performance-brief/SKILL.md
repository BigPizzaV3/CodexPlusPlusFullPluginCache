---
name: weekly-business-performance-brief
description: Prepare a concise weekly business performance brief from Zylu analytics. Use when a user asks how a business performed, what changed, or what to focus on this week.
---

Prepare an evidence-based weekly brief for one Zylu business.

1. Establish the business context. If the user has not identified a business, call `list_accessible_businesses` and ask them to choose when more than one is available.
2. Establish the reporting period. Use the user's dates when supplied. For a request such as "this week," state the resolved date range. Do not silently compare periods unless the user asks for a comparison.
3. Call `get_analytics_catalog` for the selected business before forming a semantic query. Use only entities, dimensions, metrics, filters, and query instructions returned by that tool.
4. Call `query_analytics` for the smallest set of queries needed to answer the request. Keep pagination in mind and explain when results are incomplete.
5. Report the result in this order: reporting period, key results, meaningful changes or rankings, and up to three actions grounded in the returned data.

Do not invent benchmarks, causes, comparisons, customer behavior, or recommendations not supported by the returned analytics. If the available metrics cannot answer a part of the request, say what is unavailable.
