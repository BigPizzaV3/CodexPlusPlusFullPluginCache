# Adaptive Valuation Engine

Use valuation methods that match the economics of the security. Use Graham's revised growth formula as a sensitivity check for profitable individual stocks, not as the primary valuation.

## Required process

1. Classify the business or security type.
2. Normalize earnings, cash flow, capital expenditure, working capital, dilution, debt, and one-offs across a full cycle when possible.
3. Choose one primary method and at least one independent cross-check.
4. Build bear, base, and bull values with explicit assumptions.
5. Compare current price with each value and calculate margin of safety as `(intrinsic value - price) / intrinsic value`.
6. Run a reverse valuation to state what growth, margins, returns, or credit outcomes the market price implies.
7. Reduce confidence when methods disagree materially; never average incompatible outputs without explanation.

Use current, sourced risk-free rates, risk premiums, balance-sheet data, estimates, and prices. Avoid false precision. Report ranges rather than a single exact target.

## Method selection

| Security or business | Primary method | Cross-checks |
|---|---|---|
| Stable non-financial company | FCFF or FCFE DCF | Historical and peer P/E, EV/EBITDA, FCF yield |
| Asset-light or high-growth company | Scenario DCF | Reverse DCF, unit economics, EV/revenue with margin bridge |
| Bank or insurer | Residual-income or excess-return model | P/B versus sustainable ROE, dividend-discount model |
| REIT or property company | NAV or discounted AFFO | P/AFFO, implied capitalization rate |
| Cyclical or commodity producer | Mid-cycle earnings or asset NAV | Through-cycle EV/EBITDA, replacement cost |
| Pre-profit biotech or binary asset | Probability-adjusted NPV | Cash runway, pipeline or milestone scenarios |
| Broad or sector ETF | Look-through weighted constituent valuation | Historical range, earnings yield, quality and concentration |
| Bond or cash ETF | Yield, duration, credit and maturity analysis | Spread, reinvestment risk, after-fee return |

For conglomerates or materially different segments, use sum-of-the-parts when consolidated multiples obscure economics.

## DCF discipline

- Forecast operating drivers, not an unsupported top-line growth rate.
- Reconcile free cash flow with reported statements.
- Use a terminal growth rate consistent with sustainable long-run nominal growth.
- Use a contemporaneous discount rate and show sensitivity to discount rate and terminal assumptions.
- Model dilution, debt, leases, pensions, minority interests, and non-operating assets where material.
- Treat terminal value above 75% of enterprise value as a caution requiring stronger cross-checks.

## Graham revised growth-formula sensitivity

For every profitable individual-stock finalist, calculate three sensitivity values internally:

`V = EPS × (8.5 + 2g) × 4.4 ÷ Y`

Use:

- `EPS`: latest trailing-12-month diluted EPS. Prefer GAAP; use normalized TTM EPS only when a material one-off makes reported EPS economically misleading.
- `g`: a reasonable annual EPS-growth rate over the next 7–10 years, entered as percentage points such as `8`, not `0.08`.
- `Y`: the current Moody's Seasoned Aaa Corporate Bond Yield, entered as percentage points such as `5.3`, not `0.053`.

Choose independent bear, base, and bull `g` assumptions from durable revenue growth, margin limits, reinvestment runway, dilution, cyclicality, and competitive erosion. Do not extrapolate a one-year consensus estimate across a decade. Make bear ≤ base ≤ bull and widen the range when growth uncertainty is high.

Run `scripts/graham_growth.py` when code execution is available. In Decision View, disclose only:

`Graham growth sensitivity — Bear: $X · Base: $Y · Bull: $Z`

Do not show the formula, inputs, or arithmetic unless the user explicitly requests an audit. Never label the method inapplicable solely because a profitable company is asset-light or high-growth. Use `not calculable` only when EPS is non-positive or a sufficiently current Aaa yield cannot be sourced. Omit this company formula for ETFs.

## Required valuation card

| Item | Result |
|---|---|
| Security type | |
| Primary method | |
| Cross-check | |
| Graham growth sensitivity | Bear / base / bull values |
| Bear / base / bull value | |
| Probability-weighted value | |
| Current price and as-of date | |
| Base-case margin of safety | |
| Market-implied expectation | |
| Decisive assumption | |
| Valuation confidence | High, medium, or low |

For an ETF, replace per-share intrinsic values with look-through valuation ranges and expected-return bands when a single intrinsic value would be misleading.
