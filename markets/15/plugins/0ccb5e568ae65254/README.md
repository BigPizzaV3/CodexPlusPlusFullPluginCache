# stockrow

Connects ChatGPT and Codex to stockrow's read-only MCP server, so they can look up what US-listed companies report and link to where each figure came from.

## What you can do

- Look up a company's profile and headline figures.
- Read up to ten years of income statements, balance sheets and cash flows.
- Follow a ratio or metric over time.
- Compare several companies on the same metrics.
- Screen covered US-listed companies on their latest figures.
- Read insider buys and sells.
- See revenue by segment and region, and what a share price implies, for the largest US companies.
- Read the watchlist on your stockrow account.

## Try asking

- Compare Microsoft, Alphabet and Amazon on operating margin, return on invested capital and P/E.
- Show me Apple's free cash flow for the last ten years.
- Find US companies over $10B in market cap with a P/E under 15 and a dividend yield over 3%.
- Have insiders been buying or selling Nvidia this year?
- What is on my stockrow watchlist, and how did those companies do today?

## Connecting

On first use, a browser page opens. Sign in to your stockrow account and press Allow. The plugin contains no API key or other credential.

Connecting depends on your stockrow account's plan; the sign-in page tells you if yours does not include it. You can disconnect at any time on your stockrow API page.

## Tools

| Tool | What it does |
|---|---|
| `search_companies` | Finds companies by ticker or name |
| `get_company_overview` | Profile and headline figures for one company |
| `get_financial_statement` | One financial statement, as reported, up to ten years |
| `get_metric_history` | The history of one metric for one company |
| `compare_companies` | Latest values of several metrics for several companies |
| `run_screen` | Screens covered companies by their latest figures |
| `list_indicators` | The metrics and line items the other tools take |
| `get_insider_transactions` | Insider buys and sells for one company |
| `get_segments` | Revenue by segment, product and region, for the largest companies |
| `get_valuation` | What the share price implies, for the largest US companies |
| `get_my_watchlist` | The companies you follow, with today's price and change |

## Good to know

- Every tool only reads. stockrow cannot trade, move money or change anything in your account.
- Answers say where their figures come from on stockrow.com and how current they are. Cash is in US dollars, and percentages are fractions (0.15 means 15%).
- Financial information is provided for research and is not investment advice.

## Links

- [Documentation](https://stockrow.com/api/docs/mcp)
- [Privacy policy](https://stockrow.com/privacy)
- [Terms](https://stockrow.com/terms)
- [Support](https://stockrow.com/contact)