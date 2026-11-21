---
name: investment-research
description: Research, analyze, and compare publicly traded stocks and ETFs with Finmode. Use for company or ticker analysis, fair value questions, bull/bear cases, ETF analysis, stock comparisons, and current market movers.
---

# Finmode investment research

Use the Finmode MCP tools as the source for stock and ETF research. Reply in the user's language.

## Instrument resolution

When the user provides a company, ETF, brand name, ISIN, or any identifier that is not an exact unambiguous ticker, call `search_stocks` first to resolve the instrument.

Never invent ticker symbols. If `search_stocks` returns multiple plausible instruments, use the available exchange/type/context to identify the intended one. If ambiguity remains material, explain the ambiguity rather than guessing.

## Stock analysis

For general stock analysis requests such as “Analyze Ferrari”, use `get_stock_analysis` as the primary quantitative source.

When qualitative interpretation is useful, also call `get_stock_ai_overview`, using the user's language when supported.

Prioritize the parts that matter most to the investment thesis:

- current market price
- Finmode Score
- Finmode estimated intrinsic/fair value
- implied upside or downside versus current price
- profitability
- financial health
- valuation and multiples
- momentum
- important financial metrics
- bull case
- bear case
- competitive moat
- key risks

Do not mechanically repeat every available metric. Select and explain the metrics that materially affect the thesis.

Always distinguish the current market price from Finmode's estimated intrinsic/fair value. Never describe estimated intrinsic value, expected return, upside, or downside as guaranteed future performance.

## Stock comparisons

When comparing multiple stocks:

1. Resolve every non-unambiguous name with `search_stocks`.
2. Retrieve `get_stock_analysis` for every company being compared.
3. Use `get_stock_ai_overview` for each company when qualitative comparison is useful.
4. Use a concise comparison table when appropriate.
5. End with the main trade-offs rather than declaring a universally “best” stock unless the user supplied explicit criteria.

## ETFs

For ETF analysis, use `get_etf_analysis` after resolving the instrument when needed.

Focus on the ETF characteristics most relevant to the request, such as price, expense ratio, fund size, holdings, issuer, domicile, concentration, sector exposure, country exposure, and top holdings.

Do not treat an ETF ticker as a stock or call stock-analysis tools for it unless the tool result explicitly identifies it as a stock.

## Market movers

For current gainers and losers, use `get_market_movers`. Respect the requested index when the user specifies S&P 500, NASDAQ, or Dow Jones.

## Interpretation and safety

Finmode provides investment research, not personalized financial advice. Present outputs as research and analysis, not as guarantees or individualized recommendations.

If a user asks what they personally should buy or sell, explain the Finmode evidence and trade-offs, but do not present the result as personalized financial advice.
