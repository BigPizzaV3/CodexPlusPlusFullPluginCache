---
name: research-keywords
description: Research keyword ideas, compare search demand and forecast advertising traffic using HYPD Keyword Research. Use for keyword market research and advertising planning, not campaign changes, live Account reporting or organic rank tracking.
---

# HYPD Keyword Research

Use the plugin's Keyword Research MCP for market estimates. The user's explicit instructions take precedence over these workflow guidelines. Choose only the steps needed for their request; the ideas → volumes → forecast sequence is a useful workflow, not a prerequisite for every query.

## Choose the tool

- `keyword_find_ideas`: expand 1–15 `seed_keywords` into related ideas with available search volume, competition and top-of-page bids.
- `keyword_search_volume`: look up volume, CPC, competition, bid ranges and available 12-month trends for an existing list. Batch up to 500 `keywords` per call rather than calling once per keyword.
- `keyword_ad_forecast`: estimate impressions, clicks, CTR, average CPC and cost for up to 500 `keywords`. A fresh forecast requires a positive `max_cpc` in USD and `match_type` (`exact`, `phrase` or `broad`). `forecast_window` accepts `next_week`, `next_month` or `next_quarter` and defaults to `next_month`.
- `keyword_locations_and_languages`: list the accepted country and language spellings. This static reference does not count toward lookup limits.

A HYPD sign-in is required. A Google Ads Connection is not required: ideas and volumes use Google Keyword Planner when the user has a usable Google Ads Account and DataForSEO otherwise; forecasts use DataForSEO. Let the server choose the provider. Availability depends on Account permissions and data coverage. If tools are unavailable, explain that the plugin's MCP must be enabled and authenticated before retrieving estimates.

## Establish the research inputs

Fresh research calls require `country` and `language` using the reference tool's exact spellings. Use the market already specified in the conversation; ask when it is missing or ambiguous rather than silently choosing a default. Check the reference when unsure of a spelling. Derive seed keywords from a product or topic if appropriate; the tools do not accept URL seeds. A forecast also needs the user's intended bid and match type, or an explicitly agreed hypothetical scenario.

Go directly to metrics when the user supplies a keyword list. Find ideas when they need a shortlist. Add a forecast when they ask about advertising traffic or budget. Do not fetch all three stages automatically. If a list exceeds a tool's limit, narrow or split it according to the requested scope, explaining that each fresh batch is metered.

## Reuse returned results

Results include `result_id`, `expires_at`, `page`, `page_size`, `row_count`, `total_pages`, `columns` and `rows`. They remain available for 24 hours. Use an actual ID from the same tool to retrieve further pages or re-sort; do not invent IDs or mix result types.

For a stored read, pass `result_id` with the needed `page`, `page_size` and `order_by`. Omit fresh inputs (`country`, `language`, seeds or keywords, and forecast bid/match/window). For example, an existing idea result can be read with `result_id`, `page: 2`, `page_size: 10` and `order_by: "search_volume"`. Use the returned ID rather than a placeholder.

Idea and volume ordering accepts `relevance`, `search_volume`, `competition_index`, `low_top_of_page_bid` or `high_top_of_page_bid`. Forecast ordering accepts `relevance`, `impressions`, `ctr`, `average_cpc`, `cost` or `clicks`. Stored reads do not fetch fresh data or consume another lookup. If a result expired, explain the need for a fresh lookup; if the user specifically asked to avoid one, stop at that limitation.

## Present the result and its limits

Present the returned metrics that answer the request, usually in a compact table. Use `columns` and `rows` together. Preserve missing values, currencies and units; do not reinterpret a missing metric as zero. Forecast bids and monetary metrics use USD regardless of Account currency. Retain currency supplied with other results, and do not claim one if none is given. Distinguish keyword competition and bid estimates from organic SEO difficulty.

Identify the country, language and forecast window where applicable. State when only a page of a larger result is shown. For a reused result, explain that it is stored data, not a refresh. Separate returned metrics from your own clustering, prioritization or interpretation. Do not promise traffic, rankings, conversions or ROAS from these estimates.

Fresh calls count toward the user's lookup limits. Reference lookups and valid stored reads do not. Relay returned usage notices and limit errors as given, including any reset time they state. The packaged skill is static: it cannot report how much remains. Do not invent a limit or retry a limit denial as if it were a transient failure.

This surface cannot change campaigns, Accounts, bids or budgets, and cannot retrieve live campaign performance, organic ranking positions or backlinks. It also cannot send email or create or modify calendar events. Explain the relevant boundary when a request needs those operations. For email or calendar requests, do not call the Keyword Research MCP and do not request recipient, message or meeting details as though this plugin could complete the action. State that communications and scheduling are outside this plugin's surface. Do not call research tools to simulate completing a write action.

For a getting-started request, explain these capabilities and ask which product or keyword list, country and language the user wants to research. The skill itself makes no external changes.
