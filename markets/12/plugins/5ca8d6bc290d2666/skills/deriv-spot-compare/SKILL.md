---
name: deriv-spot-compare
description: "Derivatives vs spot comparison (basis, VWAP, derivative trade prints)"
---

## OpenAI connection notes

Tool identifiers below are raw operation names. The host may add a namespace;
use the matching advertised Global MCP tool. Resolve `<resolved-package-root>`
to this plugin's installed directory before using paths. Workflow names identify
packaged skills; they are not literal Claude slash commands.

Original procedure tool scope: `pricing___get_derivative_source_details`, `pricing___get_historical_derivative_trades`, `pricing___get_latest_derivative_trades`, `pricing___get_latest_prices`, `pricing___get_vwap`, `pricing___list_sources_by_product`, `analytics___getImpliedRates`, `analytics___getImpliedVolatilitySurface`.

# deriv-spot-compare workflow

> See [CONNECTORS.md](../../CONNECTORS.md) for tool details.

## Usage

deriv-spot-compare workflow <user input>

## Scope

Implied rates, volatility surface, and OTC FX rates are available via `Lukka-Analytics` server (`analytics___*`).

Lukka Reference Rate (sourceId 5001) and Median Reference Rate (5002) may return 404 - use the fallback below. Fallback: `get_latest_prices({ sourceId: 1000 })` (EOD) or `({ sourceId: 2000 })` (Intraday).

## Flow

1. **Spot price**: `pricing___get_latest_prices({ sourceId: 2000, pairCodes: "<user input>" })`  (sourceId 2000 = Lukka Prime Intraday)
2. **VWAP (24h)**: `pricing___get_vwap({ pairCode: "<user input>", sourceIds: "<comma_top_exchanges>", from: 24h_ago, to: now })` 
3. **List derivative sources**: `pricing___list_sources_by_product({ productType: "trades" })` , then pick Deribit (typically 4022). NOTE param is `productType` with enum `prices|trades|candles|mvwaps|market-caps|variances` - there is NO `derivatives` value and NO `product` param.
4. **DISCOVER the derivative pricing code (never construct it)**:
   `pricing___get_derivative_source_details({ sourceId: "{deribit_id}", productType: "trades" })` 
   - **This response is ~1.5 MB (3800+ pairs). Pipe through a processor (see `large-data-processing`) - do NOT load into context.** Grep the `pairs[]` for the target: match `underlyingAssetCode` == the Lukka canonical of the pair base (e.g. XBT) AND `derivativePricingCode` contains `PERPETUAL`.
   - **CRITICAL - the code you need is `derivativePricingCode`, and it uses the EXCHANGE-NATIVE ticker + `.DERI` suffix, NOT the Lukka canonical.** Do NOT build it from the Lukka code. Native != canonical for many assets: XBT->`BTC`, SOLN->`SOL`, XLT->`LTC`, PDT->`DOT`, HYPE22->`HYPE`, UNISW->`UNI`, TRUMPOFF->`TRUMP`. Example results: `BTC-PERPETUAL.DERI` (USD-settled) and `BTC_USDC-PERPETUAL.DERI` (USDC-settled) both have `underlyingAssetCode=XBT`. Perpetual pattern is `{NATIVE}-PERPETUAL.DERI` or `{NATIVE}_USDC-PERPETUAL.DERI`. Options carry strike/expiry: `{NATIVE}_USDC-9JUL26-89-C.DERI`.
5. **Derivative trades**: `pricing___get_latest_derivative_trades({ sourceId: "{deribit_id}", lukkaDerivativeCode: "{derivativePricingCode from step 4}" })`  - pass the discovered code verbatim (e.g. `BTC-PERPETUAL.DERI`), never a code you assembled from the Lukka canonical.
6. **Historical context**: `pricing___get_historical_derivative_trades({ sourceId: "{deribit_id}", lukkaDerivativeCode: "{discovered code}", from: 1h_ago, to: now, limit: 100 })` 
   - **WARNING: `limit` is enforced per time-page, not per-record - a 1h window still returns 300 KB+ (hundreds of trades). Use the SMALLEST window you need and pipe the response through a processor. A 24h window will overflow context - never request it raw.**
   - 24h volume = sum of `size` field across all returned trades (compute in the processor)
   - 24h trade count = number of rows returned
7. **Implied forward curve**: `analytics___getImpliedRates({ pairCode: "<user input>", lukkaEntityCode: "LUKKA", timeFrom: "24h_ago", timeTo: "now", curveType: "INST_FWD", modelType: "NSS", source: "FUTURES", rateType: "BASIS" })` 
   - Data available from T-1. Returns tenor (days) + annualized rate.
   - **IMPORTANT**: `ZERO+COMPOSITE` does NOT work. Use `INST_FWD/NSS/FUTURES/BASIS`.
8. **Volatility surface**: `analytics___getImpliedVolatilitySurface({ underlyingAssetLukkaCode: "{lukka_canonical_base, e.g. XBT}", lukkaEntityCode: "DERI", moneyness: "delta", timeRange: "1D", timeTo: "now" })` 
   - `underlyingAssetLukkaCode` here IS the Lukka canonical (XBT/ETH), unlike the derivative pricing code in steps 4-6.
   - `lukkaEntityCode`: use `DERI` (Deribit). `LUKKA` may return no data. Response is large (1500+ points for 1D) - process externally.
   - **`timeRange` MUST be paired with `timeTo` (or `timeFrom`) as anchor** - standalone `timeRange` returns HTTP 400.

## Output

### Derivatives vs Spot: {pair}

**Spot**
- Price: ${spot_price}
- 24h VWAP: ${vwap}

**Derivative (Perpetual)**
- Price: ${perp_price}
- Basis: ${basis} ({basis_pct}%)
- Spot vs VWAP: {bps} bps (positive = spot > VWAP)
- 24h trade count: {count}
- 24h volume: ${vol} (sum of `size` field across all trades in `get_historical_derivative_trades(24h)` response)

**Basis interpretation**
- Positive basis -> perp trading premium to spot (bullish funding pressure)
- Negative basis -> perp discount (short interest or spot squeeze)

**Implied Forward Curve** (from Lukka-Analytics)
| Tenor | Rate (annualized) | Timestamp |
|-------|-------------------|-----------|

**Volatility Surface** (from Lukka-Analytics)
| Moneyness | Implied Vol | Tenor |
|-----------|------------|-------|

**Funding Rate** (if available from derivative source)
- Not directly available via `get_historical_derivative_trades`; funding rate is exchange-specific metadata not in the Lukka-Pricing surface. Display "N/A" unless source provides it in trade metadata fields.
