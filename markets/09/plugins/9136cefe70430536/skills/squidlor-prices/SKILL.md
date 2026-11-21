---
name: squidlor-prices
description: >-
  Use when the user asks for a crypto or tokenized-stock price (BTC, ETH, SOL,
  NVDA, TSLA, AAPL...), "what is X at", a market level, a price at a past time,
  price history, OHLC candles, whether oracle providers agree, whether a price
  feed is stale, or which feeds Squidlor publishes. Answers come from the
  Squidlor MCP server tools (get_price, get_realtime_prices, compare_oracles,
  get_price_history, get_ohlc, get_price_at, list_feeds, get_audit_trail).
---

# Squidlor prices

Squidlor publishes aggregated price feeds on Arc (chain `arc`). Each feed is the
median of what the oracle providers (Chainlink, Pyth, RedStone, DIA, Supra,
eOracle, Chronicle, Stork, Squidlor's own exchange median, Uniswap TWAP) report
for a pair. The tools below read that data. None of them needs an API key.

## Which tool

| User asks | Call |
|---|---|
| "price of BTC", "what is ETH at", one current level | `get_price` with `chain: "arc"`, `pair: "BTC/USD"` |
| several assets at once, or sub-second freshness | `get_realtime_prices` with `symbols: ["BTC","ETH"]` |
| "do the oracles agree", "what does Chainlink say vs Pyth", "is this stale" | `compare_oracles` |
| "what was X at <time>" | `get_price_at` with the time as ISO-8601 or unix seconds |
| "last 24h", "chart", "candles", volatility | `get_ohlc` (candles) or `get_price_history` (median series) |
| "which feeds / pairs / assets exist" | `list_feeds` first, then the price tool |
| "did the oracle lie", deviations, flagged prints | `get_audit_trail` or `list_flagged` |

Pairs are `SYMBOL/USD`. Tokenized stocks use the ticker: `NVDA/USD`, `TSLA/USD`.
If a pair might not exist, call `list_feeds` rather than guessing.

## Reporting a price

- Quote the aggregated median and say it is an on-chain median across oracle
  providers. Give the time of the print when the result includes one.
- The result may carry a coverage verdict or age annotation (how many sources are
  healthy, how old the newest print is). Pass that on when it is anything other
  than fully healthy and fresh. A price from one source, or minutes old, is not the
  same answer as a fresh median of eight.
- When the user asks whether providers agree, give the spread in basis points or
  percent between the highest and lowest provider, name the outlier, and say
  whether it is stale.
- Do not convert a USD price into another currency unless the user asks, and then
  say which rate you used.
- Do not invent a price. If the tool errors or returns nothing, say so and stop.
