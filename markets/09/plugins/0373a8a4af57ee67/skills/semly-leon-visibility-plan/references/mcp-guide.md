# Semly MCP — Leon's action guide

This guide maps use cases to tools; it does not replace the current schema. Tool names below are logical names and may have a prefix such as `semly_`. Discover the connected Semly tools and read their schemas before calling them. Do not assume a fixed plugin, account, brand, or model ID: customers use their own connections. Never store secrets in a skill.

## Choosing data

| Need | Tools and use |
|---|---|
| Brand selection and permissions | `list_brands`, `get_brand`, `get_account_context` (with brandId, also GSC/Bing status and models) |
| Available allowance | `get_brand_limits` before adding questions or generating articles; check the relevant allowance and current use |
| Visibility and trends | `get_report_statistics`: `query.view` summary/overview/analytics/trend/ai_growth_score; from/to dates, optional model and question/topic scope |
| Historical reports | `list_reports`, `get_report`; retrieve a full answer separately with `get_prompt_answer` |
| Readable presentation | `show_brand_visibility` with explicit dates; `show_brands` for selection. Use when the client supports the widget; also summarize important findings in text |
| Competitors | `get_competitor_statistics`: list, visibility, analysis, answers, prompts. Use IDs from that brand's data |
| Questions and answers | `list_prompts`, `list_prompt_topics`, `get_prompt_statistics`, `list_prompt_answers`, `get_prompt_answer` |
| Sources | `get_source_statistics`: list/detail/prompt/categorized; a domain and an exact URL have different scopes |
| Google | `get_search_console_overview`, `list_search_console_pages`, `list_search_console_queries`, `get_search_console_page_statistics`, `get_search_console_query_statistics`, `list_search_console_page_queries`, `list_search_console_query_pages`, `get_search_console_pages_metrics`, `get_search_console_insights`, `get_search_console_cannibalization`, `inspect_search_console_url` |
| Bing and comparisons | `get_bing_statistics`: overview, pages, queries, page, query, page_queries, query_pages, comparison_pages, comparison_queries |
| Existing recommendations | `list_recommendations`, then `get_recommendation` for the selected ID |
| Articles and performance | `list_articles`, `get_article`, `get_content_statistics`; bot statistics are not audience traffic |

`get_brand_limits` accepts `page` and `limit`, with no `brandId` argument. Find the correct brand in `data.brands.items`, paginating if needed. Use that brand's effective limit and usage; unused account allowance is not necessarily allocated to the brand.

Both Bing and GSC use top-level `from` and `to` arguments. Each GSC tool is a separate operation with top-level arguments and no `view` selector. For `list_search_console_page_queries`, use `url` for the page URL and `page` for the results page number. `inspect_search_console_url` accepts `brandId`, `url`, and optional `locale`, without dates. GSC inspection checks the current known state of a URL, not its historical state in a requested date range. Distinguish connection errors from empty results. Account for returned `appliedInput`, default filters, time zones/dates, `lastSuccessfulSyncAt`, `latestAvailableDate`, `availableFrom/To`, and `refreshedAt`.

Read further result pages when they matter to the conclusion. Label a partial dataset as a sample or top list, not a complete audit. Do not compute every competitor's rank or share from the first page. Join records using correct IDs and full URLs; do not merge distinct language or product versions through aggressive URL normalization.

## Action boundaries

- `create_prompt` / `create_prompts` add active questions. A batch contains 1–100 items sharing a country and language. Check existing questions and allowance; group markets separately. Evaluate partial success per item. Do not retry an entire failed batch before reading saved questions. These tools do not edit or delete old questions, create topics, or trigger a report.
- `get_prompt` reads an active or inactive question by `brandId` and `promptId`. When deactivation or replacement is requested, `deactivate_prompt` requires `prompts:deactivate` consent and returns the saved `active=false` state while preserving history, topics, country and language. It is idempotent. For an approved replacement, read the old settings first, deactivate, check the released allowance, then use `create_prompt` once with the same settings.
- For generation, briefs, editing, and publication, read [article-workflow.md](article-workflow.md) before the first such action.
- `update_recommendation_status` only changes the saved status of an existing recommendation when requested. First read `get_recommendation` and its allowed statuses. It does not implement a fix, generate an article, or edit a file. Do not update virtual recommendations without saved details. For sitemaps, file generation status and `isCompleted` mean different things. Reading recommendations does not create new ones or automatically recheck the site.
- Semly MCP does not provide general HTML retrieval for every website, arbitrary CMS/product-page editing, DNS/server access, robots.txt changes, email sending, or forced AI report generation. Use available browsing to read public pages. If page content is unavailable, request the necessary passage and never invent a "before" version. Deliver implementation material, or use an additional integration only when available and within the task.
- Do not create reports, brands, or trial articles to test access. After an interrupted write, inspect the state instead of automatically repeating a non-idempotent operation.

## When something is unavailable

Missing connection: explain how to connect Semly and continue with a supplied export when available. Missing write permission: deliver the ready solution and identify the exact unavailable action. No allowance: present the topic/questions and request a decision about the allowance; do not bypass it by creating a new brand. Unconfirmed result: report the state and include an operation/article ID only when it helps the customer resume, without claiming success.
