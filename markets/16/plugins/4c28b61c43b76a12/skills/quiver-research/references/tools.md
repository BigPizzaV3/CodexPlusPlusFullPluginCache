# QuiverQuant tool guide

Use the connected server's discovered tools and schemas as the authority for availability and arguments. This package's source starts from `origin/master`; a deployed server can expose a different revision. The package does not redeploy the server.

| Research need | Tool | Interpretation |
| --- | --- | --- |
| Congressional disclosures | `get_congress_trades` | Separate transaction and filing dates; preserve disclosed amount ranges and ownership labels. Use aggregation only when the connected schema supports it. |
| Congress member profile | `get_congress_politician` | Profile, estimated net worth, trading statistics, and recent trades. Do not promise a complete portfolio or donor history from this tool. |
| Legislation | `get_congress_legislation` | Bill titles, stage, dates, affected tickers, and AI-generated summaries. A summary is not authoritative statutory text. |
| Presidential trade disclosures | `get_trump_trades` | Preserve the `filed` versus `traded` distinction and reported amount ranges. |
| Insider transactions | `get_insider_trading` | Form 4 codes include purchases, sales, awards, dispositions, tax-related share payments, and option exercises. These are not interchangeable. |
| Institutional holdings | `get_institutional_holdings` | 13F disclosures lag positions. Aggregate by filer for holder rankings; preserve filing dates and report periods. |
| Executive compensation | `get_executive_compensation` | Reporting year differs from filing date. Several returned executives can belong to the same year. Compute any comparison from the rows rather than claiming a tool supplied an uncomputed delta. |
| Ownership | `get_ticker_ownership` | Insider sentiment, institutional summary statistics, and top disclosed owners. |
| Government contracts | `get_gov_contracts` | Award/action dates and obligated amounts. Obligations are not necessarily recognized revenue. |
| Lobbying | `get_lobbying` | Preserve year, client, registrant, reported amount, and issue. |
| Corporate PAC donations | `get_corporate_donors` | PAC transactions, candidate identifiers, election cycles, and amounts. Do not describe them as all employee or individual donations. |
| Off-exchange short volume | `get_dark_pool` | Daily short-volume observations; short volume is not the same as short interest or a direct measure of investor positioning. |
| Patents | `get_patents` | Choose filings, drift, or momentum according to the user's question and available schema. |
| Curated news | `get_quiver_newsfeed` | Attribute the article, preserve dates, and distinguish news summaries from source disclosures. Use bounded plain-text summaries by default. |
| Political exposure | `get_political_exposure` | Congress trades, contracts, and lobbying together. Examine actual dates, selection notes, and sample limits before describing recency or totals. No political-beta calculation is promised. |
| Ownership plus insider activity | `get_ticker_full_picture` | Combined ownership and recent insider records, with any partial-result flags preserved. |
| Compare companies | `compare_tickers` | Two to five tickers on `congress`, `insider`, `gov_contracts`, or `lobbying`; results are bounded samples. |
| Discover datasets | `search_datasets` | Signed-in catalog access. Discovery is not evidence that every dataset is entitled for the current account. |

Company financial statements, ETF holdings, market movers, social sentiment, trade execution, subscription administration, and private brokerage access are not promised by this package. Use another capability only if the host actually exposes it and the user requests it.
