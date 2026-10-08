# Scenario construction

For every quantitative scenario use the same market boundary, geography, annual metric, currency/price basis, baseline year, and horizon year. Record the baseline as observed, estimated, or unknown. Do not silently replace missing data with zero.

## Modeling procedure

1. Estimate addressable buyers/units and baseline paid adoption, usage, and realized price. Where suitable use installed stock, replacements, new additions, utilization, and service revenue explicitly; do not mix stock and flow.
2. Estimate uptake by buyer segment and region, constrained by purchasing cycles, institutions, distribution, and complementary investment.
3. Cross-check delivered output against feasible manufacturing, construction/installation rate, labor, energy/materials, financing, and approval capacity. Separate announced from commissioned assets.
4. Model price/cost changes separately from volume. Learning curves can be a scenario input when backed by an appropriate historical series; they are not a universal causal law. Add policy and commodity stresses when material.
5. Compare with relevant total budgets and top-down activity data. Account for displaced incumbent activity. Identify where value accrues and how competition affects margins, without converting industry growth into an investment-return estimate.

## Scenario types

**Exploratory:** alternative coherent futures used for stress-testing. No probabilities required. Do not present their range as a statistical confidence interval.

**Probability-weighted:** define mutually exclusive and collectively exhaustive states or outcome bins, including failure/stagnation. Assign each a justified subjective probability and a representative conditional mean annual size, not merely a best-case endpoint. Probabilities must sum to 1. If the “upside” world overlaps the “central” world, redesign the partition before averaging. A scenario mean above a threshold does not mean all outcomes inside that scenario cross the threshold; estimate event probability separately or model within-scenario distributions.

Downside, central, and upside are useful labels but do not imply that the central case is the mean or median. Register each horizon separately when needed. Maintain shared macro assumptions across industries; do not give each field a different favorable macro world and add the results.

## Arithmetic

- CAGR = (terminal annual size / baseline annual size)^(1 / elapsed years) − 1.
- Added annual size = terminal annual size − baseline annual size.
- Expected terminal size = sum(scenario probability × conditional mean terminal size).
- CAGR of expected terminal size is distinct from expected CAGR. The calculator labels both; neither is a promised trajectory.
- CAGR is undefined for a zero baseline. Show absolute additions and adoption metrics instead.
- A zero terminal value from a positive baseline has CAGR −100%; negative annual market-size inputs are invalid here.

Use a distribution or structural model only if inputs justify it. If running simulation, document distributions, dependencies, random seed, and sensitivity; a large number of draws cannot cure unsupported assumptions. Do not give statistical-looking uncertainty bands to a handful of subjective scenario points.

## Useful adversarial prompts

- “The forecast failed because one essential link was wrong. Which observable link is weakest, and what outside evidence would establish that?”
- “If unit prices halve while adoption doubles, what actually happens to annual revenue and buyer surplus?”
- “What deployment rate is mathematically required, and how does it compare with demonstrated capacity and lead times?”
- “Which adjacent supplier benefits across several possible winners, and what could commoditize that supplier?”
- “What evidence would make us prefer the established substitute?”
- “Which common shock could invalidate several apparently diverse candidates at once?”

These prompts organize verification; they are not measured performance guarantees.
