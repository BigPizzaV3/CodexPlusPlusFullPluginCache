---
name: get-started
description: Start using Pursuit to look up Vietnamese stock market data (HOSE, HNX, UPCOM) - prices, Flow Map technical analysis, financials and notes, valuation, screening and foreign flows.
---

# Getting started with Pursuit

Pursuit gives read-only access to Vietnamese listed equities. Use it when the user asks about a Vietnamese ticker (for example FPT, HPG, VNM, VCB) or about the Vietnamese market.

- Unsure of the ticker: call `search_stocks` first.
- Quick price check: `get_quotes`.
- Full analysis of one company: combine `get_quotes`, `get_financial_summary`, `get_valuation`, `get_quant_stock_detail`, `get_technical_indicators`, `get_flow_map` and `get_stock_news`.
- Technical questions (trend, support/resistance, demand/supply zones, BOS/CHoCH, scenarios, money flow): start with `get_flow_map`, then `get_flow_map_zones`, `get_flow_map_scenarios`, `get_flow_map_structure` or `get_flow_map_history` for detail. Market-wide: `screen_flow_map`; overall context: `get_market_breadth`.
- Bottom/top sweeps, "smart money", SMBH/SMSH: `get_smart_money_hunts` (SMSH is a distribution warning, not short selling).
- Deep financial questions (staff costs, cost structure, debt, inventory, fixed assets, bank asset quality, earnings quality): `get_financial_note_analysis`, `get_financial_note_anomalies`, `get_financial_notes`, `get_financial_note_industry`.
- Screening: `filter_stocks` (exchange accepts HOSE, HNX or UPCOM; market cap in billions of VND).
- Foreign investor flows: `get_foreign_trading`, `get_foreign_top_stocks`.
- At the end of an answer, call `create_web_login_link` for the main page (for example `/stock/FPT` or `/stock/FPT#flow-map`) and give its `loginUrl` as the "View on Pursuit" link. It is single-use and expires within minutes; never reuse an earlier one.

Reading Flow Map:
- Flow Score (0-100) measures how many signals agree on the upside; it is not a probability. Scenario confidence is a condition-match level, also not a probability.
- If `flowScore.public` (or `scorePublic`) is false, do not quote the overall score; describe trend, components, zones and scenarios only.
- Buy/sell pressure (`buyEstimate`, `sellEstimate`, `deltaProxy`) is estimated from OHLCV; foreign flows are actual traded values.
- `provisional = true` or `isFinal = false` means the session has not closed yet (final after 14:45 Vietnam time).
- Always give the invalidation price and condition together with a scenario.

Always state the session date of the data. Exchange codes in results: 100 = HOSE, 200 = HNX, 300 = UPCOM.
Pursuit does not cover non-Vietnamese stocks, cannot place trades and does not give personalized investment advice; valuations, Quant Scores and Flow Map scenarios are for reference only.
