# akta.pro tool reference

All tools are read-only. Credits are deducted from the authenticated account.

## Free tools (0 credits)

| Tool | Arguments | Returns |
| --- | --- | --- |
| `account_status` | none | `is_enterprise`, `package_type`, `credit_balance`, `currency` |
| `company_search` | `query` (name or website, auto-detected), `include_child_companies` | Candidates with `uuid`, `name`, `website`, `product_category`, public/private status; children carry `parent_company` |
| `industry_search` | `query` | `code`, `industry_name`, similarity score |
| `list_filters` | none | Filter catalogue: `filter`, `description`, `value_shape`, `how_to_get_values`, optional `dropdown_type`, optional `same_element_group` |
| `get_filter_values` | `lookups`: 1–25 of `{dropdown_type, query, level, limit}` | Fixed lists as `[{label, value}]`, or taxonomy matches with `code` + score; `truncated` / `total_available` |
| `news_types` | none | 77 news event-type codes in 11 categories (see [event-types.md](event-types.md)) |

## Company data

| Tool | Cost | Notes |
| --- | --- | --- |
| `company_data_concise` | 3 credits flat | Condensed overview as slimmed JSON, much smaller than full enrichment. No section selection. Use `company_data` sections for detailed funding rounds or deal records. |
| `company_data` | Per section (below) | Markdown, rendered server-side |

`company_data` section costs (credits):

| Section | Cost | Section | Cost |
| --- | --- | --- | --- |
| `firmographic` | 2 | `management_profile` | 1.5 |
| `business_model` | 2 | `product_offering` | 2 |
| `company_assessment` | 2 | `strategic_signal` | 1.5 |
| `trust_signal` | 0.5 | `customer_profile` | 1 |
| `company_hierarchy` | 0.5 | `industry` | 0.5 |
| `digital_presence` | 0.5 | `technology` | 2 |
| `financial_estimate` | 0.5 | `funding_detail` | 3 |
| `location` | 0.5 | `mna_and_investment` | 5 |

Field dictionary: https://docs.akta.pro/company-data-dictionary

Rule of thumb: if a general picture is enough, `company_data_concise` (3 credits flat) costs less than requesting several 2-credit sections. If the user needs one or two specific facets, a narrow section can be cheaper (e.g. `financial_estimate` alone is 0.5).

## Company lists

| Tool | Cost |
| --- | --- |
| `generate_company_list` | 1.5 credits per call that returns companies + 0.2 per company (20 companies = 5.5 credits). Zero matches = free. Arguments: `filters`, `limit` (default 20, max 500), `offset`, `sort_by`, `sort_order`. |

Cost does not depend on fields: every row is `uuid`, `name`, `website`, `product_category`, `company_type`, `hq_country`.

## News

| Tool | Cost | Notes |
| --- | --- | --- |
| `news_signals` | 0.1 per call + 0.01 per article | Compact list by default (id, title, AI summary, URL, date, publisher); never includes full text. `limit` default 10, max 100. Full parameter list in [news.md](news.md). |
| `news_detail` | 0.1 per call + 0.01 per article | `news_ids` (integers, up to 10). Same fields as `full_enrichment` plus `full_text`. |

## Alternative signals

All take a `company` uuid from `company_search`.

| Tool | Cost | Data |
| --- | --- | --- |
| `headcount_trends` | 2.5 | LinkedIn-sourced total employees, historical growth, and breakdown by function. No pagination. |
| `website_traffic` | 1.5 | Engagement metrics, monthly visit estimates, and traffic by acquisition channel. No pagination. |
| `job_posts` | 4 | Live LinkedIn/Indeed job posts: title, location, description, compensation, experience level, key skills. `limit` (default 10, max 200), `offset`. |
| `social_posts` | 1 | Content type, text, publish date, paid/repost flags, AI classification, engagement metrics. `limit` (default 10, max 200), `offset`. |
| `employee_reviews` | 1.5 per 50 reviews | Overall and dimension-level ratings plus individual reviews (Glassdoor et al.). `limit` (default 10, max 100), `offset`. |
| `product_reviews` | 1.5 per 50 reviews | Product catalog and per-product reviews (G2 et al.). Call without `products` for the catalog, then with product ids. `limit` per product (max 50), `offset`. Catalog-call cost isn't separately documented; don't describe it as free. |

## API equivalents (for developers)

- REST base: `https://api.akta.pro/api/v1`, header `x-api-key`
- Company data: https://docs.akta.pro/api-reference/company-data
- List generation: https://docs.akta.pro/api-reference/listgen-api
- News signals: https://docs.akta.pro/api-reference/news-signals
- OpenAPI: https://docs.akta.pro/openapi.json · LLM docs: https://docs.akta.pro/llms.txt · Agent docs: https://agent-docs.akta.pro/llms.txt

Keep API keys in environment variables or a secrets manager, never in source or chat.
