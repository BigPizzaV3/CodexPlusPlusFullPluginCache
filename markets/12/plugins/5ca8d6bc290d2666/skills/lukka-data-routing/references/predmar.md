# Lukka-Predmar (prediction-markets) - 11 Production Tools

Prediction market data from Polymarket, Kalshi, and Gemini. All tools exposed as `prediction-markets___<tool>`.

Lukka-Predmar is OAuth-gated like every other hosted Lukka server (authenticate once via the host's MCP connection settings). All tools use `Get*` naming convention. Output disclaimers are covered by the bundled DISCLAIMER.md.

## Core Discovery (3 tools)

| Tool | Use when | Key params |
|------|----------|-----------|
| `prediction-markets___GetPredictionMarkets` | Find / list prediction markets | `search`, `sort_by` ("total_volume_usd_1hr", "total_volume"), `sort_dir` ("asc"/"desc"), `limit`, `event_ticker` (to pull one event) |
| `prediction-markets___GetSimilarMarkets` | Related markets via embeddings | `event_ticker` |
| `prediction-markets___GetPredictionMarketsTaxonomy` | Schema / available fields | - |

## Classification (1 tool)

| Tool | Use when |
|------|----------|
| `prediction-markets___GetPMCSstats` | Classification counts (supersector / macro / mid / sub) |

## Market Context (7 tools)

| Tool | Use when |
|------|----------|
| `prediction-markets___GetMarketNews` | News attached to a market / topic |
| `prediction-markets___GetMarketOverview` | Dashboard-style summary |
| `prediction-markets___GetMarketRecap` | Day-over-day recap. Can return `null` with no error on a given day - treat `null` as "no recap yet" and degrade gracefully (skip the section), not as a failure. |
| `prediction-markets___GetOpenInterest` | Open interest per market |
| `prediction-markets___GetPredictionMarketTotalVolume` | Aggregate volume |
| `prediction-markets___GetPriceHistory` | Contract price history. **Required: `event` + `exchangeId`** (example IDs from this environment: 4137=Polymarket, 4141=Kalshi, 4008=Gemini - discover current IDs via `GetExchanges` rather than hardcoding; the `exchangeId` must match the event's own exchange). Pass `event` = the `event_ticker` straight from GetPredictionMarkets (numeric `base_market_id` / `market_id` also work). Returns OHLC candles for ALL outcome-markets under the event, grouped by timestamp; use `from`/`to` (ISO-8601) + `interval` (ms). **Empty result = the window has no trades, NOT a broken endpoint** - short-lived / already-resolved markets (BTC-15min, hourly-settle) only hold data inside their brief live window. Use a recent window over an actively-trading event. |
| `prediction-markets___GetExchanges` | Supported venues list. **2 required params**: `limit`, `offset`. `primary_location`, `vasp_classification`, `vasp_score`/`gt`/`lt` are optional filters; `vast_type` is a legacy optional field. Response includes a full VASP profile per venue (vaspScore, letterGrade). |

## Entities

| Code | Platform |
|------|----------|
| POLYMARK | Polymarket |
| KALSHI | Kalshi |
| GMNI | Gemini |

## Quick Examples

```
# Top 5 bitcoin markets by last-hour volume
prediction-markets___GetPredictionMarkets({
  search: "bitcoin",
  sort_by: "total_volume_usd_1hr",
  sort_dir: "desc",
  limit: "5"
})

# Full detail for one event
prediction-markets___GetPredictionMarkets({
  event_ticker: "bitcoin-above-100k.POLYMARK"
})

# Recap for today
prediction-markets___GetMarketRecap({})

# Similar markets
prediction-markets___GetSimilarMarkets({
  event_ticker: "bitcoin-above-100k.POLYMARK"
})
```
