---
name: optionwhales
description: Use when the user asks about US options flow, unusual options activity, dealer gamma exposure (GEX) levels, implied volatility, open interest, dark pool activity, earnings or macro calendars, or stock quotes, technicals, fundamentals and news. Answers with OptionWhales data through the OptionWhales tools.
---

# OptionWhales market data

The OptionWhales tools answer questions about US-listed options and stocks. Use them for
anything current: prices, levels and flow change every session.

## Picking a tool

| The user asks | Tool |
|---|---|
| "Where could SPY pin / stall / accelerate?", "gamma levels on QQQ" | `gex_levels` |
| "What does observed options flow show today?", "accumulation or hedging signals" | `intent_flow_current` |
| "Strongest options momentum right now" | `momentum_rankings` |
| "Any unusual options activity?", "latest unusual trades, newest first" | `abnormal_trades_current` |
| "Is NVDA implied volatility elevated / inverted?" | `volatility_term_structure` |
| "Biggest IV spikes today" | `volatility_movers` |
| "When does AAPL report?", "who reports from today through seven days from today?" | `earnings_calendar` |
| "Macro events coming up?" | `economic_calendar` |
| "How are traders positioned into earnings?" | `earnings_current` |
| Estimated Greek exposure by strike/expiry | `greek_exposure` |
| Open interest, contract chains | `oi_movers`, `oi_timeseries`, `contract_chain`, `contract_atm`, `contract_historic` |
| Market-wide or sector flow | `market_tide`, `sector_tide`, `directional_current` |
| Dark pool / off-exchange | `darkpool_ranking` |
| Quotes, candles, indicators | `stock_quote`, `stock_candles`, `technical_indicator` |
| Fundamentals, dividends, splits, news | `financials`, `dividends`, `stock_splits`, `stock_news` |
| Short interest / volume, insiders, seasonality | `short_interest`, `short_volume`, `insider_trades`, `seasonality` |
| Screening for setups | `screener` |

Gamma levels, the flow tools and the implied-volatility term structure render interactive
views; summarize the key numbers in the reply as well.

## Access

- Without an account: SPY and QQQ gamma levels, the next high-impact macro events and
  earnings reports, the top options-flow names and the latest unusual trades.
- When a tool needs an account, ChatGPT asks the user to sign in to OptionWhales. Never ask
  for passwords, API keys or codes in the conversation.
- If a tool answers `pro_required`, say the user's OptionWhales account does not include that
  tool and offer the tools that do answer. Do not retry it or promote a purchase or upgrade.

## Reporting results

- Name the returned session or snapshot date. If it is absent, say that the data's
  exact age is unavailable; a retrieval time is not a market-data timestamp.
- Gamma levels: spot versus the gamma flip, then the call wall, put wall and max pain with
  their distance from spot. Compare the numbers before calling a level above or below
  spot; a put wall can be above the current spot. When present, distinguish the levels'
  `computed_at` from `spot_resolved_at`. Explain differing snapshot times or freshness
  limits before describing levels as current intraday support or resistance.
- Options-flow intent describes inferred positioning from observed trades. It does not identify traders or guarantee direction.
- Unusual trades are ordered by timestamp descending (newest first), not by premium. Preserve that ordering and state the session date.
- For earnings over the next seven days, use `days=7` and state the inclusive range from today through today plus seven days in America/New_York. Mention preview limits.
- Earnings-calendar rows provide ticker symbols, not company names. Report each symbol exactly as returned. Do not expand a symbol into a company name unless a tool result explicitly supplies that name or another cited source verifies it; otherwise omit the name.
- Describe gamma and other dealer exposure as modeled or estimated, not as known dealer holdings. Do not invent missing values.
- For trade execution or brokerage-position requests, explain that OptionWhales
  cannot perform that action. Do not call market-data tools unless the user asks
  for relevant research. Never claim an order was placed or positions were read.
- Do not invoke OptionWhales tools for unrelated requests such as weather.
- Market data is for research and education, not investment advice. Never present it as a
  recommendation to buy or sell.
