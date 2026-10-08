# Sensor Tower Access and Research

Use when Sensor Tower can answer a research question. Recheck provider documentation and account entitlements before configuring access; product names, datasets and limits can change.

## Access choices

| Route | When to use | What must be verified |
|---|---|---|
| Official MCP | Interactive agent queries through a compatible host | Official server instructions, active API subscription, licensed datasets, host support and successful authentication |
| Official API | Repeatable bounded extraction and data workflows | API entitlement, official endpoint/schema, secure credential configuration, quota and coverage |
| Authorized browser UI | Account inspection, filters or exports where the agent environment supports it | Supported browser capability, authenticated user session, available modules and permitted operations |
| CSV/XLSX export supplied by owner | Direct connection is unavailable or export is faster | Export provenance, filters, dates, definitions and completeness |
| Scheduled feed | Repeated large-data ingestion when justified | Account entitlement, delivery destination, cadence and scope |

Official documentation states that MCP is available with an active Sensor Tower API subscription and accesses licensed datasets. A paid dashboard account alone does not establish API/MCP entitlement. Source checked 2026-09-15: [Sensor Tower MCP](https://sensortower.com/mcp-server-demo).

Sensor Tower also offers API integration and scheduled CSV/Parquet data delivery. Source checked 2026-09-15: [Sensor Tower Connect](https://sensortower.com/product/connect).

Discover available host tools/connectors before promising a connection. Follow the host's access and browser rules; do not invent server URLs, auth methods, endpoints or supported integrations. No account access has been verified merely by reading these public pages.

## Entitlement check

Keep account-specific facts in the receiving project's approved source-access record, outside this reusable skill:
- Verified date, account/workspace identity without secrets.
- Accessible products/modules and platform/country/history coverage.
- MCP/API enabled, disabled or unknown; official setup reference.
- Export formats and visible limits.
- Quotas/rate limits and permitted storage/sharing scope when relevant.
- Access method tested, minimal read result and outstanding blocker.

Use a supported secure sign-in or secret manager. Never ask for passwords, session cookies or API keys in chat or store them in the KB, source code, query logs or screenshots. If the host cannot connect, request only the missing entitlement information or a minimal export. Do not bypass access restrictions or assume UI access authorizes undocumented endpoints.

## Connect with a small read first

1. Verify current provider setup instructions and host compatibility.
2. Have the owner complete supported authentication or secure secret configuration.
3. Discover licensed datasets and required query parameters.
4. Resolve one known game by store-specific ID.
5. Read one completed period for one market/platform and relevant metric.
6. Check returned units, scope, date window, missing-value semantics and agreement with a matching UI/export when available.
7. Record verified access and query provenance, then expand only to the study's required cohort.

Respect quotas, paginate completely, retry only transient errors with documented limits, and cache timestamped snapshots. Do not run unbounded scans. Launching a recurring feed or paid upgrade requires the corresponding user request.

## Match data to decisions

The provider lists app performance, advertising, gaming taxonomy, usage and audience capabilities, but actual access varies by account. Check current coverage rather than assuming a subscription includes them. Reference: [Sensor Tower products](https://sensortower.com/) (checked 2026-09-15).

| Research question | Useful data if entitled | Interpretation limit |
|---|---|---|
| Is demand sustained and accessible? | Downloads/revenue time series by market/platform, release cohorts | Estimates and observed trajectory do not prove profit or organic growth |
| Where are emerging opportunities? | Comparable genres/mechanics, newer entrants, geographic shifts | Taxonomy and coverage must be validated; category size alone is insufficient |
| Who wins and who struggles? | Leaders, rising and mid-tier titles, decline/stagnation cases | Do not label failure from low IAP when ad revenue is missing |
| What engagement patterns matter? | Active users, sessions, time spent, retention where exposed | Comparable cohort/metric definitions required; not proof a proposed feature causes retention |
| How do competitors reach players? | Creatives, networks, exposure/SoV and spend where exposed | Exposure or longevity is not proven conversion or ROAS |
| Which audience can we serve? | Audience attributes/overlap where exposed | Panel coverage and market context limit generalization |

## Minimal extraction request

Choose fields based on the current decision:
- Research question and linked brief.
- App list with iOS/Android IDs; selection reasons and intended coverage.
- Markets and platforms separately, business model and taxonomy filters.
- Metrics, currency, gross/net and included revenue streams.
- Date range and granularity; use completed months for broad trends and finer windows only for a specific event question.
- Snapshot date, source product/API, query filters and relevant exclusions.
- Raw file/result location, transformed dataset location, and transformation notes.

A lightweight starting shape, when appropriate: a balanced seed cohort across selected directions, monthly downloads/revenue over the last 12 completed months, with relevant markets/platforms separated. It is a working default, not a required export or a substitute for including weak outcomes. Request smaller slices when sufficient; expand only when it could change the decision.

## Data quality and synthesis

Check duplicates, cross-store identity, currency, zero versus missing/suppressed, partial periods, aggregation consistency and row/pagination completeness. Record IAA/IAP/paid-download/subscription coverage; do not substitute missing streams with zero. Keep provider estimates labeled and preserve original exports.

Produce a reproducible snapshot, comparable competitor table, trend findings, limitations, and evidence-linked opportunities. Combine the data with product observation, player feedback and concept tests. Sensor Tower is an evidence source; it does not automatically validate a new game's demand or unit economics.
