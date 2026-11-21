---
name: research-sec-filings
description: Look up public SEC companies, find filings by filer name or ticker, inspect filing metadata and document lists, and review disclosed insider transactions using Earnings Feed.
---

Use the connected Earnings Feed tools for the user's SEC records research. Follow the user's requested company, forms and scope; explicit user instructions take priority over this workflow guidance.

Choose the tool that fits the request:

- `get_company`: resolve a ticker or CIK to company metadata. CIK takes precedence when both are supplied.
- `get_recent_filings`: list filing metadata, optionally filtered by filer ticker/CIK and form types.
- `search_filings`: match filer company names or tickers. It does not search document text or match ownership issuers.
- `get_filing`: use a returned or user-supplied accession to inspect metadata and document filenames. It does not retrieve document bodies or passages.
- `get_insider_transactions`: retrieve disclosed transactions for a company. `buy` means all acquisitions; `sell` means all dispositions. Awards, gifts, exercises and other transactions may appear; preserve `transactionCode` and `acquiredDisposed` rather than labeling every result an open-market trade.

Use ticker/CIK, accession, forms and bounded result counts relevant to the request. Ask for the company when it is missing or ambiguous. When resolving a filing's subject, distinguish its filer (`cik`, `companyName`) from a separately returned `issuer`; an insider or shareholder may be the filer.

Show filing dates, form types, accessions and returned SEC `url` and `earningsFeedUrl` links. Preserve null prices and quantities as unavailable. The tools return records available at request time; do not imply complete coverage or a guaranteed delivery delay. When `hasMore` is true, say the displayed results are a subset. Reuse `nextCursor` only with the same query and filters; keep paging within the user's requested scope.

If asked for document analysis or exact quotations, explain the metadata-only boundary and offer the filing links or ask for the relevant text. Do not invent passages, financial facts or a full-text capability. The plugin has no tools to create alerts, monitor future events, manage subscriptions or execute trades.

Let sign-in happen through Earnings Feed's OAuth flow. Do not ask users to paste passwords, tokens or API keys. If sign-in or quota prevents a call, explain the returned error and retry/reset guidance. Do not bypass access controls, repeatedly retry before a reset, advertise plans or direct users to subscription checkout.
