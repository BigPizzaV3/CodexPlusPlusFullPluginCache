# Lukka-Analytics - 3 Production Tools

All tools exposed as `analytics___<tool>`.

## Implied Rates (2 tools)

| Tool | Use when | Key params |
|------|----------|-----------|
| `analytics___getImpliedRates` | Forward curves, zero curves, par curves | `pairCode`, `lukkaEntityCode` (def: "LUKKA"), `timeFrom`, `timeTo`, `curveType` (INST_FWD/ZERO/PAR), `modelType` (MC/NSS/NS/SVEN), `source` (FUTURES/SWAPS/ALL), `rateType` (BASIS/COMPOSITE) |
| `analytics___getImpliedRatesOtcFx` | OTC FX implied rates | `pairCode`, `lukkaEntityCode` (def: "LUKKA"), `timeFrom`, `timeTo` |

### getImpliedRates - all 7 params required

- `curveType`: INST_FWD (instantaneous forward), ZERO, PAR
- `modelType`: MC (Monte Carlo), NSS (Nelson-Siegel-Svensson), NS, SVEN
- `source`: FUTURES, SWAPS, ALL
- `rateType`: BASIS, COMPOSITE
- **IMPORTANT**: `ZERO+COMPOSITE` does NOT work. Use `INST_FWD/NSS/FUTURES/BASIS` as default combo.
- Optional: `limit` (def: 24, max: 24), `dataShape` (flat/2L), `timeRange`
- Response: pairCode, timestamp, tenor (days), rate (annualized), metadata (convergence, rmse, dataPoints)
- Data available from T-1 (not real-time)

### getImpliedRatesOtcFx

- Optional: `limit` (def: 24, max: 24), `dataShape` (flat/2L), `timeRange`
- Response: tenor, price, bidPrice, askPrice, basisPrice, bidAskSpread, staleness, tradeCount, volume

## Volatility Surface (1 tool)

| Tool | Use when | Key params |
|------|----------|-----------|
| `analytics___getImpliedVolatilitySurface` | Options vol surface by delta or strike | `underlyingAssetLukkaCode`, `lukkaEntityCode` (def: "LUKKA"), `timeFrom`, `timeTo`, `moneyness` (delta/strike) |

- Optional: `limit` (def: 6, max: 6), `dataShape` (flat/2L/3L), `timeRange`, `tenor` (1D/1W/1M/3M/6M/1Y)
- **`limit` counts time windows, not records** - each window returns a full grid (all tenors x delta/strike points), so `limit: 3` returns 3x the per-window point count. Size accordingly.
- Response: gridLabel, impliedVolatility, tenor, tenorNumericYearFraction

## Key Patterns

- Rate limit: 5 req/s (200ms enforced delay between calls)
- API timeout: 30s
- Auto-summarization at >100 items or >50K chars (TOON format)
- Pair format: `XBT-USD` (same Lukka canonical codes as pricing)
- `lukkaEntityCode` defaults to "LUKKA" - pass explicitly
- **timeRange MUST be paired with either `timeFrom` or `timeTo` as an anchor.** Standalone `timeRange` without an anchor returns HTTP 400. Example: `timeRange: "1D"` + `timeTo: "2026-07-02T00:00:00Z"`

## Quick Examples

```
# BTC implied forward curve (NSS model, futures-derived, basis rate)
analytics___getImpliedRates({
  pairCode: "XBT-USD",
  lukkaEntityCode: "LUKKA",
  timeFrom: "2026-05-07T00:00:00Z",
  timeTo: "2026-05-08T00:00:00Z",
  curveType: "INST_FWD",
  modelType: "NSS",
  source: "FUTURES",
  rateType: "BASIS"
})

# ETH volatility surface (delta moneyness, 1M tenor)
analytics___getImpliedVolatilitySurface({
  underlyingAssetLukkaCode: "ETH",
  lukkaEntityCode: "LUKKA",
  timeFrom: "2026-05-07T00:00:00Z",
  timeTo: "2026-05-08T00:00:00Z",
  moneyness: "delta",
  tenor: "1M"
})
```
