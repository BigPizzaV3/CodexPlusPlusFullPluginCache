---
name: market-sizing
description: Size a market as TAM, SAM and SOM with base, upside and downside forecasts, using Statista Market Insights and Statistics. Use whenever someone asks how big a market is, what a category is worth, the revenue opportunity for a launch or expansion, market potential, CAGR to a future year, or needs market numbers for a business case, annual plan or long-range plan, even if they never say "TAM".
---

# Market Sizing

Estimate what a market is worth today and at a horizon year, then narrow it to what the brand can realistically capture. Every number traces to a Statista source or to an assumption labelled as one.

## Inputs

Settle these before fetching anything. If one is missing, pick the default, state it in the output and continue.

| Input | Default |
|---|---|
| Market definition: products in and out of scope | The closest Statista Market Insights market |
| Geography | The country named in the request |
| Base year and horizon year | The latest year before the current one; base year + 5 || Brand | None. Without a brand, stop at SAM. |
| Serviceable filters: channels, sub-types, price tiers | None, so SAM = TAM |
| Obtainable share | The brand's current share; otherwise a benchmark from comparable brands |

## How the Statista tools behave

- `search-market-insights` returns one dataset per metric: revenue, volume, price per unit, growth and so on. Search on the category alone, without the country. Then pass country codes taken from that result's `covered_geos` to `fetch-market-insights`, at most five per call.
- Each dataset has a `market_type`.
  - **Consumer:** the whole market, all channels. Use this for TAM.
  - **eCommerce:** the online channel only. User counts, ARPU and penetration usually come only as eCommerce datasets, so a TAM built from users × ARPU measures the online channel, not the market.
- Market Insights revenue comes in USD. Volume × price per unit reproduces revenue exactly, so it is an internal identity and does not count as a cross-check.
- `search-statistics` also returns charts derived from Market Insights. Their `sources` field names "Statista Market Insights". Charts like these are not independent and cannot be used for triangulation.
- The brand-profile charts from `search-statistics` give each brand's awareness, usage and loyalty among category users. Usage share is a proxy for value share, not equal to it.

## Workflow

1. **Define the market in one sentence**, including what it excludes. Unclear definitions are the main cause of wrong sizes.
2. **Pull the TAM.** Use the Consumer revenue dataset from `fetch-market-insights`, covering actual and forecast years. Record the unit, the forecast vintage (the dataset `id` prefix carries its release date) and the statista.com link. Note any gap between the Statista definition and the user's.
3. **Triangulate.** Find one estimate that does not come from Market Insights, using `search-statistics` then `get-chart-data-by-id`. Retail panel data, industry associations and trade press all count. Convert it to the TAM's currency and record the rate. A gap over 20% must be explained (definition, channel coverage, year) before you go further.
4. **Narrow to SAM.** Apply each serviceable filter as a share of the TAM, such as a sub-type's share of volume or the online share of revenue. Use a sourced share wherever one exists. Label any share older than three years as stale, and any share without a source as judgement.
5. **Estimate SOM.** Apply the obtainable share to the SAM. Anchor it to the brand's current share, or to usage shares of comparable brands from brand-profile charts. Never present a SOM without its share assumption.
6. **Build the scenarios.**
   - **Base:** Statista's forecast, using the CAGR implied by the series (see below).
   - **Upside and downside:** an adjusted CAGR and share for each, every adjustment tied to a named driver with one line of evidence. Growth-rate and volume-change charts are good evidence for whether growth is speeding up or slowing down.

## Calculation

With base year b, horizon year h and y = h − b:

- **Base CAGR** = (TAM in h ÷ TAM in b)^(1/y) − 1, taken from the Statista series.
- **TAM at horizon**, per scenario = TAM in b × (1 + scenario CAGR)^y. The base scenario reproduces Statista's horizon value.
- **SAM factor** = the product of all serviceable-filter shares. Each share must be above 0 and at most 1.
- **SAM** = TAM × SAM factor, for the base year and the horizon year.
- **SOM** = SAM × the scenario's obtainable share.
- **Triangulation gap** = TAM in the check's year ÷ (check value × FX rate) − 1. Flag any gap over ±20%: explain it before use.
- **Sensitivity of base-case SOM at h:** flex each input by −10% and +10% and recompute. TAM, the SAM factor and the share all multiply together, so each swings SOM by exactly ±10% (a 20% swing). Rank these three by how uncertain each input is, not by swing. For CAGR, SOM at h scales with (1 + CAGR)^y, so its swing is ((1 + 1.1 × CAGR)^y − (1 + 0.9 × CAGR)^y) ÷ (1 + CAGR)^y.

Worked example (USD m): TAM 1,102.6 in 2025 and 1,978.7 in 2030 gives a base CAGR of 12.4%. An oat share of 0.559 gives SAM 616.4 → 1,106.1. A 4% obtainable share gives SOM 24.7 → 44.2. A retail-panel check of EUR 351.15m for 2020 at FX 1.142 is USD 401.0m against a TAM of 446.0, a gap of +11.2%. The CAGR flex moves the 2030 SOM between 41.9 and 46.7, an 11.0% swing.

Re-check the result: the base scenario's TAM at h must match the Statista series, and the SOM must equal TAM × SAM factor × share.

## Output

1. **Headline:** one sentence with the base-case SOM at the horizon year, the scenario range and the market definition. Without a brand, give the SAM instead.
2. **Sizing table:**

   | Scenario | CAGR b–h | TAM b | TAM h | SAM b | SAM h | SOM b | SOM h |
   |---|---|---|---|---|---|---|---|
3. **Assumptions log:**

   | Assumption | Value | Type (sourced / derived / judgement / stale) | Source and year |
   |---|---|---|---|

4. **Triangulation:** both estimates, the gap, and the most likely reason for it.
5. **Sensitivity:** the input to firm up first, and why.
6. **Caveats:** definition mismatches, forecast vintage, exchange rates, and proxy shares.

## Quality bar

- Never add up overlapping markets. A parent market already contains its segments.
- Keep one currency and one year per comparison.
- Call a forecast a forecast.
- If Market Insights has no matching market, say so. Then build the TAM from Statistics and label it as derived.
