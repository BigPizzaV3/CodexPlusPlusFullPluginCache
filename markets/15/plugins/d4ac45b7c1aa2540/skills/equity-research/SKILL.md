---
name: equity-research
description: Research and compare company quality, screen equities by qualitative scores, and manage personal watchlists through a connected Baseline account. Use for Baseline research requests; live quotes and brokerage trading require other services.
---

# Baseline equity research

Use the connected Baseline MCP tools for the user's requested research or watchlist task. Tool names may include a host-specific namespace before their Baseline names.

## Choose the research tools

- Use `baseline_catalog` to resolve exact field and sector names when they are not already known from this conversation. For an exact symbol lookup, `baseline_tickers` accepts `ticker: "MSFT"` and an optional `country: "US"`; it does not search company names. Resolve an unknown symbol before using that filter. Other research and watchlist tools take `SYMBOL.COUNTRY`, such as `MSFT.US`.
- Use `baseline_scores` for comparisons across stocks or a watchlist. Put multiple tickers in one request. Omit fields when the user needs all scored fields, or pass a group to include its sub-scores. Request short rationales only when useful.
- Use `baseline_rationale` for the analysis behind a score, with up to five requested fields per call. Groups expand into their descendants. Responses are capped at 24,000 serialized characters; follow `pagination.next_cursor` using the same ticker and fields until it is null. A large individual entry appears in `fragment` instead of `rationales`: concatenate its `text` in `offset` order for that `entry_index`, then parse the assembled JSON to recover the entry. A fragment is incomplete research until assembled. If research changes and a cursor is rejected, restart the request without that cursor; do not combine snapshots. If continuation fails, identify the incomplete coverage instead of claiming a complete analysis.
- Use `baseline_results` when the user needs result documents or data fields alongside scores. Keep requests narrow; it does not provide the rationale tool's response-size cap. Use `include_documents: false` for lean result metadata.
- Use `baseline_query_by_score` for one score condition. Use `baseline_screen` to AND-combine up to five conditions, with optional sector and country filters. Preserve pagination and limit the first request to what the user needs.

Include the returned `as_of` or `updated_at` date when presenting research. Explain missing fields or empty results from the actual tool response. Distinguish qualitative scores from data fields: a data field can have a null score and a value; Market Cap values are in USD when identified as such by the response. Baseline research figures reflect their research date and do not establish a live quote.

## Work with watchlists

Use `baseline_watchlists` to resolve the connected user's watchlists. Apply the user's requested changes with `baseline_create_watchlist`, `baseline_watchlist_add_stock`, `baseline_watchlist_remove_stock`, or `baseline_delete_watchlist`. Resolve ambiguous targets before changing them. Deleting a watchlist also removes its entries and is irreversible. Confirm changes from successful tool results and read back the watchlist when useful.

## Connection and access

Baseline uses browser-based OAuth sign-in and consent. Never request tokens or login credentials in the conversation. If tools report an entitlement restriction, explain that the requested feature is unavailable to the connected account without claiming that the research succeeded. Do not promote upgrades, surface checkout links, or initiate a subscription. If the connection has expired, use the host's reconnect flow.

Product documentation: https://baseline.a5labs.com/mcp-docs
