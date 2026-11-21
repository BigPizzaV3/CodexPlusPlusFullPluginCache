---
name: aperiodic-research
description: How to answer market questions with the Aperiodic tools - point-in-time order flow, liquidity, trading-cost, funding, basis and open-interest data for crypto and RWA perpetuals (tokenized stocks, ETFs, commodities, FX) on Binance, OKX and Hyperliquid. Use when the user asks about these markets, backtests, execution costs, liquidity or trading signals.
---

# Researching markets with Aperiodic

Aperiodic holds point-in-time metrics and raw data for perpetual futures on `binance-futures`, `okx-perps` and `hyperliquid-perps`: crypto, and real-world-asset (RWA) perpetuals on stocks, ETFs, commodities and FX. The tools return small JSON (catalog, schemas, statistics, file handles), never bulk rows.

## Workflow

1. **Pick the dataset.** Map the question to a dataset (table below). If unsure, call `list_datasets` or `search`, then `describe_dataset` for its fields, intervals and how far back each venue goes.
2. **Find the symbol.** Call `find_symbols` with the venue and a ticker. It matches ids, not names: search `TSLA` or `GOLD`, not "Tesla" or "gold".
3. **Get the numbers.**
   - With code execution: `get_data` returns signed Parquet URLs (valid for one hour), the schema, row counts, column stats, five sample rows and a Polars snippet in `load_with`. Load the files in code and work there.
   - Without code execution: `summarize` computes per-column statistics, a correlation matrix, or a series resampled to at most 500 points, on Aperiodic's side. It takes up to 12 numeric columns.
4. **Answer.** Lead with the answer, then the evidence: a small table (at most 10 rows) or a few bullets, plus the code you ran. Say which venue, symbol, interval and dates the answer covers, and its limits (for example, one month of one symbol is a lead to test, not a result).

Never paste file contents or long row dumps into the conversation; summarize them.

## Datasets by question

| Question | Datasets |
|---|---|
| Trading costs, liquidity | `slippage`, `l1_liquidity`, `l2_liquidity`, `impact` |
| Order-book pressure | `l1_imbalance`, `l2_imbalance` |
| Order flow | `flow`, `trade_size` |
| Premium over the underlying, carry | `basis`, `funding` |
| Positioning | `open_interest` |
| Volatility | `returns`, `range` |
| Prices | `ohlcv`, `vtwap`, `derivative_price`, `l1_price` |

Raw data is addressed as `raw:<id>`: `raw:trades`, `raw:quotes` (top of book), `raw:mark_price`, `raw:index_price`, `raw:funding_rate`. Open interest comes only as the `open_interest` metrics dataset. Raw files are monthly before August 2026 and daily after, and are much larger than the metrics, so prefer a metrics dataset when one answers the question.

## Symbols

- Ids are Atlas ids: `perpetual-BTC-USDT:USDT`, or `perpetual-TSLA-USDT:USDT` for a tokenized stock on Binance or OKX.
- A Hyperliquid HIP-3 market keeps its dex before the colon: `perpetual-XYZ:TSLA-USDC:USDC`. Several dexes can list the same asset (for example `XYZ`, `CASH`, `FLX`, `KM`, `MKTS`); say which one you used, or compare them if the user asks about the asset as a whole.
- RWA history starts when each contract listed, mostly in 2026. Hyperliquid data starts in 2025. Check `describe_dataset` before asking for older dates.

## Details that change answers

- **Timestamps:** `timestamp="exchange"` (default) uses the exchange-reported time; `timestamp="true"` uses the arrival time at Aperiodic's servers. State which one an analysis used.
- **Bars:** `time` is the bar timestamp in UTC. When joining datasets (for example `flow` with `ohlcv`), join on `time` at the same interval and venue.
- **Ranges:** monthly files cover whole months; filter on `time` as `load_with` does. A long range may come back with `truncated: true` and a `next_start_date`; call `get_data` again from that date for the rest. `missing_periods` lists gaps.
- **Intervals:** 1m to 1d for most accounts. 15s and 30s bars may not be included in the user's plan.

## Access

- Without signing in, every metrics dataset is available for the Binance BTC-USDT perpetual, 5-minute bars, May 2025, and `raw:trades` for June 2025. Anything else needs the user to sign in. The client handles that when a call needs it.
- If a tool says a dataset or date is not available on the user's plan, tell the user in one line and continue with what is available. Do not retry the same call.

## Live data

`live_feed` returns the WebSocket URL, a subscribe message and a Python client for streaming metrics datasets (raw data is not streamed). The stream runs in the user's own code, outside this conversation, and needs an Aperiodic API key in the `APERIODIC_API_KEY` environment variable (the key is on the user's API page at https://aperiodic.io/home/api). Signing in to this app does not give the stream access. Hand the user the client; do not try to consume the stream in the conversation.
