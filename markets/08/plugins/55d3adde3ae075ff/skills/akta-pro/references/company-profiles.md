# Company profiles and alternative signals

## Choosing between concise and sections

- `company_data_concise` (3 credits flat): a condensed overview as slimmed JSON, much smaller than full enrichment. No section selection. Use for "tell me about X" when a general picture is enough.
- `company_data` (billed per section): Markdown. Choose sections explicitly; there is no "all" option. A single narrow section can cost less than concise (e.g. `financial_estimate` alone is 0.5). For detailed funding rounds or deal records, use `funding_detail` / `mna_and_investment`.

## Sections

These are typical contents; coverage varies by company. Exact fields per section: https://docs.akta.pro/company-data-dictionary

| Section | Credits | What it covers |
| --- | --- | --- |
| `firmographic` | 2 | Name, legal name, company type, founded year, description, operating status, ownership, headcount range |
| `location` | 0.5 | HQ, offices, markets served |
| `industry` | 0.5 | akta industry taxonomy, keywords, SIC/NAICS codes |
| `business_model` | 2 | GTM type and motion, offering type, revenue model, pricing, marketing and distribution channels |
| `product_offering` | 2 | Products and brands, problem solved, benefits, outcomes, differentiators |
| `customer_profile` | 1 | Segments, ideal customer profiles, named customers |
| `management_profile` | 1.5 | Founders, executives, board, backgrounds |
| `financial_estimate` | 0.5 | Revenue and valuation estimate bands |
| `funding_detail` | 3 | Funding stage, total raised, rounds, investors |
| `mna_and_investment` | 5 | Acquisitions, investments, deal records |
| `technology` | 2 | Core tech, integrations, AI maturity, API and app availability |
| `digital_presence` | 0.5 | Official web, social, and app footprint |
| `company_hierarchy` | 0.5 | Parent company, subsidiaries |
| `trust_signal` | 0.5 | Compliance, certifications, regulatory updates, awards |
| `company_assessment` | 2 | Market position, strengths, weaknesses, competitive moat, risks, customer concentration, peers |
| `strategic_signal` | 1.5 | Partnerships, recent strategic moves, leadership changes, expansion |

## Intent to section

| The user wants… | Sections |
| --- | --- |
| Peers, competitors, comparables | `company_assessment` |
| SWOT, strengths, risks, moat | `company_assessment` |
| Partnerships, recent strategic moves | `strategic_signal` |
| Funding history and investors | `funding_detail` |
| Acquisitions and investments made | `mna_and_investment` |
| Leadership team | `management_profile` |
| Who they sell to | `customer_profile` |
| How they make money | `business_model` |
| Revenue / valuation estimates | `financial_estimate` |
| Tech stack, AI maturity, API | `technology` |
| Parent / subsidiaries | `company_hierarchy` |

## Full profile recipe

When the user asks for a complete profile: `firmographic`, `location`, `business_model`, `product_offering`, `customer_profile`, `management_profile`, `financial_estimate`, `funding_detail`, `strategic_signal`, `company_assessment` (16 credits), plus recent `news_signals(primary_company=…)` (0.1 + 0.01 per article). Unless the user has already set a budget that covers it, state the approximate cost first.

## Alternative signals

All take a `company` uuid. Use only the signals the question calls for.

| Tool | Credits | Data | Good for |
| --- | --- | --- | --- |
| `headcount_trends` | 2.5 | LinkedIn-sourced total employees, historical growth, breakdown by function | Workforce momentum, functional expansion or contraction, post-layoff analysis |
| `website_traffic` | 1.5 | Engagement metrics, monthly visit estimates, traffic by acquisition channel | Demand, web momentum, marketing mix |
| `job_posts` | 4 | Live LinkedIn/Indeed posts: title, location, description, compensation, experience level, key skills | Hiring intent, team build-outs, geographic expansion |
| `social_posts` | 1 | Content type, text, publish date, paid/repost flags, AI classification, engagement | First-party announcements, posting cadence |
| `employee_reviews` | 1.5 per 50 reviews | Overall and dimension-level ratings, individual reviews (Glassdoor et al.) | Culture, workforce sentiment, diligence |
| `product_reviews` | 1.5 per 50 reviews | Product catalog, then per-product reviews (G2 et al.) | Product sentiment, competitive comparison |

- `job_posts`, `social_posts`, `employee_reviews`, `product_reviews` accept `limit` and `offset`. `headcount_trends` and `website_traffic` have no paging.
- `product_reviews`: call once without `products` to get the catalog and product ids, then again with the ids the user cares about. Never guess product ids. The catalog call's cost isn't separately documented; don't describe it as free.

## Interpreting alternative signals

- Headcount is LinkedIn-sourced, not a payroll count; growth alone doesn't prove revenue growth.
- Website traffic figures are estimates of visits, not unique users, customers, or revenue.
- Job posts show recruiting priorities, not confirmed hires or net headcount change. Avoid double-counting repeated listings.
- Social posts: separate original, repost, and paid content when flagged; engagement is not conversion; the AI classification is an inferred label.
- Employee and product reviews: a returned page is a sample. Don't call the page count the total, and keep each product's reviews separate.
- When combining signals (e.g. headcount growth plus open roles in a function), label the conclusion as directional.

## Who uses this

- **Financial services** (PE, VC, investment banking, credit, research): sourcing, market maps, peer sets, diligence, portfolio and deal monitoring.
- **GTM and sales**: ICP and target account lists, account research, buying-signal and trigger monitoring, territory planning.
- **Product builders and agents**: embed the same data in AI agents, platforms, and apps via MCP or API.
