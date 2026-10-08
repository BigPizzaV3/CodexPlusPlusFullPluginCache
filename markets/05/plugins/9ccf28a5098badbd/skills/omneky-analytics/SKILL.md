---
name: omneky-analytics
description: >-
  Read Omneky paid-media performance: ROAS, CTR, CPA, spend, impressions,
  conversions, trends, daily metrics, and dimension summaries. Use when the
  user asks how Meta/Facebook, Google, TikTok, LinkedIn, Reddit, Pinterest,
  or X Ads are performing, or wants HubSpot CRM / Semrush / Ahrefs / GSC
  lookups for the signed-in brand. Intent keywords: ROAS, CTR, CPA, spend,
  paid media, Meta ads, Facebook ads, Google Ads, TikTok ads, which ads
  should I make more of, campaign breakdown, creative leaderboard,
  trending, HubSpot, Semrush, Ahrefs, GSC, coverage check.
---

# Omneky analytics

## Activation analytics

If the host exposes a skill-activation / analytics hook, call it once per new user request with this skill name; otherwise skip silently. Never invent a tracking tool. Omneky MCP does **not** expose `track_skill_activation`.

## Purpose

Read-only performance and brand-connector reporting for the signed-in user's
brands. Answer “how did we do?” and “what should we make more of?” with
structured MCP tools only — never invented SQL, warehouse tables, or lift
endpoints.

## When to use

- How ads performed (ROAS, CTR, CPA, spend, conversions) over a date range
- Which creatives, campaigns, or channels are winning
- What rose or fell versus the prior period (also see
  `omneky-performance-movers`)
- Coverage check before querying (dates + channels)
- HubSpot CRM search, Semrush domain/keyword overview, Ahrefs DR /
  keywords / backlink stats, or Google Search Console analytics

## When not to use

- Launching, pausing, or budgeting ads → `omneky-launch-manage` /
  `omneky-pause-budget`
- Generating or editing creatives → `omneky-creative` /
  `omneky-image-ads` / `omneky-product-video` / `omneky-edit-resize`
- Catalogue SKU writes → `omneky-catalogue` / `omneky-product-import`
- Arbitrary SQL — there is **no** public `run_sql_query`
- Plan / Stripe portal as the primary ask → `omneky-billing`

## OpenAI runtime contract

- Use only tools from the current OpenAI host + Omneky MCP (`https://mcp.omneky.com/mcp`). Never invent tools.
- Prefer native ChatGPT / host widgets and question UI for decisions. Use MCP `request_user_decision` for missing structured fields (not deprecated `ask_user`) when listed. Else follow `omneky-failure-modes` § Approval / plain-chat fallback.
- When intake is incomplete, ask **one** concise chat question. Never invent a question tool.
- Approval / Generate turns: end the turn after Approve / Deny (or Generate / Cancel) via host UI or plain chat; mutate only after affirmative Approve / Generate. Never invent a fake widget tool.
- Never invent tokens; OAuth is host-managed.

## Non-negotiable output / safety contract

- Never invent metrics, score / lift endpoints, or warehouse table names.
- Always call `check_reporting_data_available` (preferred over deprecated
  `data_available`) **before** treating empty results as real zeros.
- `selected_conversion_metric_value` **varies per channel**. Never sum it
  across channels; group by channel or use a named metric.
- Prefer `get_performance_breakdown` over deprecated
  `get_dimension_summary`; prefer `get_performance_movers` over deprecated
  `get_trending` (aliases may still appear on `tools/list`).
- Prefer `search_reporting_values` over deprecated
  `search_dimension_values` when both exist.
- If brand or date range is missing, ask once. Do not guess `brand_id`.
- Lead with the answer; name the channel / campaign when filtered.
- Auth is host OAuth; never ask for a token.

## Staged workflow

### Stage 1 — Session + brand

1. `get_current_user` when `user_id` is required by later tools.
2. `list_brands` / brand picker if `brand_id` unknown.
3. `get_brand` / `get_brand_details` as needed.

### Stage 2 — Coverage gate

1. Confirm date range with the user (default a tight recent window if they
   said “lately” / “this week” — still state the range you will use).
2. Call `check_reporting_data_available` for brand + dates + channels.
3. If coverage is empty for the requested slice, report coverage — do not
   fabricate zeros.

### Stage 3 — Choose the performance tool

| Intent | Tool |
| --- | --- |
| What moved vs prior period | `get_performance_movers` |
| Day-by-day time series | `get_daily_metrics` |
| Ranked breakdown (campaign / creative / channel / …) | `get_performance_breakdown` |
| Resolve a name → id for filters | `search_reporting_values` |
| AI creative / media recommendations | `get_recommendations` (tight window; on `status=timeout` narrow — no identical retry this turn) |
| Channel spend / budget snapshot | `get_channel_budget` |

### Stage 4 — Interpret safely

1. Summarize winners / losers with evidence from tool payloads only.
2. Keep conversion metric commentary channel-scoped when using
   `selected_conversion_metric_value`.
3. If the user asks what to create or launch next, hand off to
   `omneky-creative` / `omneky-launch-manage` after the read-out.

### Stage 5 — Brand connectors (reads only)

HubSpot / Semrush / Ahrefs / GSC have **no** connect or disconnect tools on
this surface. Check status first. Semrush is **not** in
`list_connector_statuses` — call `get_semrush_connection_status` directly.
GSC is included in that fanout.

**HubSpot**

1. `get_hubspot_connection_status`
2. `hubspot_search_contacts` / `hubspot_search_companies` /
   `hubspot_search_deals`
3. Then `hubspot_get_contact` / `hubspot_get_company` / `hubspot_get_deal`

**Semrush**

1. `get_semrush_connection_status`
2. `get_semrush_domain_overview` / `get_semrush_keyword_overview`
3. Respect Nexus unit quotas (HTTP 429 / 503 → say capped; do not hammer)

**Ahrefs**

1. `ahrefs_connection_status`
2. `ahrefs_domain_rating` / `ahrefs_organic_keywords` /
   `ahrefs_backlinks_stats`

**GSC (organic — not paid media)**

1. `get_gsc_connection_status`
2. `gsc_list_sites`
3. `gsc_query_analytics` with a `site_url` from the list

### Stage 6 — Billing adjacent

Company plan / Stripe portal / credit balance live on prod
`mcp.omneky.com` when listed. See `omneky-billing` /
`omneky-credit-balance`. Out of credits for creatives → upgrade plan path
— never invent prepaid purchase tools.

## Failure boundaries

| Failure | Required response |
| --- | --- |
| Empty-looking metrics | Run `check_reporting_data_available`; explain coverage gaps. |
| Temptation to sum conversions across channels | Refuse; break out by channel. |
| `get_recommendations` timeout | Narrow dates; no identical retry this turn. |
| Missing brand / dates | One question; stop. |
| Invented `run_sql_query` | Refuse; stay on structured tools. |
| Connector disconnected | Status-first; tell user to connect in brand settings (no public connect tools for HubSpot/Semrush/Ahrefs/GSC). |
| Semrush / Ahrefs 429 | Report quota; do not tight-loop. |
| User pivots to launch / gen | Hand off to the matching skill with safety contracts. |
| Auth failure | `omneky-failure-modes` / host re-OAuth. |

## Worked intake example

User: “How did Meta and TikTok do last week for Brand X?”

1. Resolve Brand X → `brand_id` via `list_brands` (picker if ambiguous).
2. `check_reporting_data_available` for last 7 days, channels facebook + tiktok.
3. If covered: `get_daily_metrics` for trend + `get_performance_breakdown` by
   creative or campaign (channel-filtered when the tool allows).
4. Optional movers: `get_performance_movers`.
5. Report channel-separated conversion commentary; never sum
   `selected_conversion_metric_value` across Meta + TikTok.
6. Offer: recommendations (`get_recommendations`) or hand off to creative /
   pause-budget if they ask what to do next.

## Sibling map

| Need | Skill |
| --- | --- |
| Movers-only | `omneky-performance-movers` |
| Credits / plan | `omneky-billing` / `omneky-credit-balance` |
| Launch / pause | `omneky-launch-manage` / `omneky-pause-budget` |
| Failures | `omneky-failure-modes` |
| First-run | `omneky-getting-started` |
