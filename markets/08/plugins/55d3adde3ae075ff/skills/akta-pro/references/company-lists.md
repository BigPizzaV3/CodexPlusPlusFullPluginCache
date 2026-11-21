# Finding companies with filters

Use `generate_company_list` for any request that returns a set of companies: target account lists, ICP lists, market maps, peer sets, TAM screens, lookalikes, investor portfolios, competitor sweeps.

## The required sequence

```
list_filters()                         # free: what filters exist
  -> get_filter_values(lookups=[...])  # free: exact values; batch up to 25 lookups in one call
  -> generate_company_list(filters)    # paid: run the list
  -> company_data / news_signals       # paid: depth on the few uuids that matter
```

Skipping `get_filter_values` is the most common failure. A value written from memory doesn't error; it matches zero companies, or gets dropped and silently broadens the list.

## Filter catalogue

This mirrors `list_filters` (41 filters). Always confirm keys against `list_filters` before calling. "Lookup" means the filter has a `dropdown_type`: get values from `get_filter_values` and use them verbatim.

### Firmographic
| Filter | Shape | Values |
| --- | --- | --- |
| `firmographic.company_type` | string or list | Lookup (public / private) |
| `firmographic.ownership_category` | string or list | Lookup (PE-controlled, VC-backed, family-owned, founder-bootstrapped, state-owned…) |
| `firmographic.operating_status` | string or list | Lookup (operating, acquired, closed, IPO'd) |
| `firmographic.founded_year` | `{"gte": int, "lte": int}` | Direct |

### Industry
| Filter | Shape | Values |
| --- | --- | --- |
| `industry.industry` | list | Lookup with `query` → `code`s. Primary sector filter; matches primary or secondary industry at any level |
| `industry.naics` | list | Lookup with `query`. Use only when the user names NAICS |
| `industry.sic` | list | Lookup with `query`. Use only when the user names SIC |

### Location
| Filter | Shape | Values |
| --- | --- | --- |
| `location.hq.region` | list | Lookup (UN M49 codes, e.g. Europe, Northern America). A broad region covers every country in it |
| `location.hq.country` | string or list | Lookup |
| `location.hq.city` | string or list | Direct (city name as stored; prefer country/region when unsure) |
| `location.market_served.is_global` | bool | Direct |
| `location.market_served.markets.country` | list | Lookup (ISO-3). Group: markets |
| `location.market_served.markets.region` | list | Direct, substring. Group: markets |
| `location.offices.country` | list | Lookup. Group: offices |
| `location.offices.city` | list | Direct. Group: offices |

### Financial estimates
| Filter | Shape | Values |
| --- | --- | --- |
| `financial_estimate.revenue_estimate` | string or list | Lookup (revenue bands) |
| `financial_estimate.valuation_estimate` | string or list | Lookup (valuation bands) |

### Funding
| Filter | Shape | Values |
| --- | --- | --- |
| `funding_detail.funding_overview.funding_stage` | string or list | Lookup (current stage; use for simple stage questions) |
| `funding_detail.funding_overview.total_funding_usd` | `{"gte", "lte"}` | Direct |
| `funding_detail.funding_overview.last_funding_date` | `{"gte": "YYYY-MM-DD", "lte": ...}` | Direct |
| `funding_detail.funding_overview.num_funding_rounds` | `{"gte", "lte"}` | Direct |
| `funding_detail.funding_rounds.round` | list | Lookup. Group: funding rounds |
| `funding_detail.funding_rounds.date` | `{"gte": "YYYY-MM-DD", "lte": ...}` | Direct. Group: funding rounds |
| `funding_detail.funding_rounds.amount_usd` | `{"gte", "lte"}` | Direct. Group: funding rounds |
| `funding_detail.funding_rounds.investors.uuid` | list | Lookup with `query` = investor name. Group: funding rounds |
| `funding_detail.funding_rounds.investors.name` | list | Direct, substring (prefer uuid when known). Group: funding rounds |
| `funding_detail.funding_rounds.investors.lead_investor` | bool | Direct. Group: funding rounds |

### Business model
| Filter | Shape | Values |
| --- | --- | --- |
| `business_model.gtm_type` | string or list | Lookup (B2B / B2C…) |
| `business_model.gtm_motion` | list | Lookup (product-led, enterprise sales, channel/partner-led…) |
| `business_model.revenue_model` | list | Lookup (subscription, usage-based, licensing, transaction fees…) |
| `business_model.offering_type` | string or list | Lookup (product, service, both) |

### Assessment
| Filter | Shape | Values |
| --- | --- | --- |
| `company_assessment.customer_concentration.classification` | string or list | Lookup |
| `company_assessment.competitive_moat` | list | Lookup (network effects, switching costs, IP, scale…) |

### Technology
| Filter | Shape | Values |
| --- | --- | --- |
| `technology.ai_maturity.scale` | int or list of ints | Lookup. 0 (no AI) to 5 (AI foundational). Multi-select: "at least AI-differentiated" is `[3, 4, 5]`, not a range |
| `technology.api_detail.has_api` | bool | Direct |
| `technology.app_detail.has_app` | bool | Direct |
| `technology.is_technology_focussed` | bool | Direct |

### Customers and partnerships
| Filter | Shape | Values |
| --- | --- | --- |
| `customer_profile.select_customer.name` | string or list | Direct, substring |
| `strategic_signal.partnership.name` | list | Direct, substring. Group: partnership |
| `strategic_signal.partnership.type` | list | Lookup (reseller, technology, distribution…). Group: partnership |
| `strategic_signal.partnership.strategic_tier` | list | Direct. Group: partnership |

There is no headcount filter; use `sort_by: "employee_range"` to rank by size, or check `firmographic` on the shortlist.

## Rules

- Filters combine with AND, so every extra filter narrows the list.
- Always include at least one selective filter. Unfiltered or very broad queries are rejected.
- Filters in the same group (offices, markets, funding rounds, partnership) must all match the **same** element. For example, `funding_rounds.round` = Series B plus `funding_rounds.investors.uuid` = Sequoia means Sequoia invested in the Series B, not just in any round.
- Industry depth: keep `level: ["l4"]` for a specific niche; use `level: ["all"]` for a broad sector or when unsure. A broader code matches every company beneath it. Code length shows depth: 2 chars = l1, 4 = l2, 6 = l3, 8 = l4. Levels can be mixed in one list.
- Use `industry_search` codes for news; for lists, resolve industry with `get_filter_values` (`dropdown_type: "industry.industry"`).

## Sorting and paging

- `limit` defaults to 20 (max 500); `offset` pages.
- `sort_by`: `relevance` (default), `revenue_estimate`, `total_funding`, `valuation_estimate`, `founded_year`, `employee_range`. Band fields sort by magnitude. `sort_order` `desc` (default) gives largest / most funded / most recently founded first.
- Use sorting for "top 20 best-funded…", "largest…", "newest…" instead of pulling a big list and ranking it yourself.

## Reading the result

- `warnings`: always check and report.
  - A **dropped** value means that constraint was not applied; the list is broader than the user asked for. Say so, and fix the value with `get_filter_values` if possible.
  - A **coerced** value was normalised to its canonical form. Harmless; reuse the canonical spelling.
- `total_count` saturates at 500. Treat 500 as "500 or more" and suggest narrowing rather than paging further.
- Rows contain only `uuid`, `name`, `website`, `product_category`, `company_type`, `hq_country`. Don't claim revenue, headcount, or funding from a list row; enrich the uuids first.

## Filter wide, then narrow

Some criteria don't map to a filter (a fuzzy niche, "sells to hospitals", "uses Snowflake"). In that case:

1. Apply the filters that do map reliably, plus sorting, to get a manageable candidate set.
2. Enrich candidates with only the sections that test the remaining criterion (e.g. `customer_profile`, `technology`, `product_offering`).
3. Drop companies that don't fit, and tell the user which criterion was verified this way.

## Cost control

- Cost is 1.5 credits + 0.2 per returned company (20 companies = 5.5 credits; zero matches = free). Ask for the page size the user actually needs.
- Screen with the list, then enrich only the shortlist.
- Before enriching many companies, estimate the total and confirm with the user.

## Examples

**PE sourcing:** "Founder-owned B2B software companies in Western Europe, founded before 2015, $10–50M revenue."
1. `get_filter_values` in one call: `industry.industry` (`query: "software"`, `level: ["all"]`), `firmographic.ownership_category`, `location.hq.region` (`query: "Western Europe"`), `business_model.gtm_type`, `financial_estimate.revenue_estimate`.
2. `generate_company_list` with those values plus `firmographic.founded_year: {"lte": 2014}`, `sort_by: "revenue_estimate"`.
3. Report count, warnings, and a table; offer to enrich the top N.

**VC portfolio:** "Companies where Sequoia led a Series A since 2023."
1. `get_filter_values`: `funding_detail.funding_rounds.investors.uuid` (`query: "Sequoia"`), `funding_detail.funding_rounds.round` (`query: "Series A"`).
2. Filters: round = Series A, investors.uuid = Sequoia's uuid, `lead_investor: true`, `funding_rounds.date: {"gte": "2023-01-01"}` (all one group, same round).

**GTM ICP:** "US product-led SaaS companies with an API, AI maturity 3+, best funded first."
1. `get_filter_values`: `location.hq.country`, `business_model.gtm_motion`, `business_model.revenue_model`, `technology.ai_maturity.scale`.
2. Filters: country, gtm_motion = product-led, revenue_model = subscription, `technology.api_detail.has_api: true`, `technology.ai_maturity.scale: [3, 4, 5]`; `sort_by: "total_funding"`.
