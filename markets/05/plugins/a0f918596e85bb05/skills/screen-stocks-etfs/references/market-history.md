# Historical Market Behavior and Regime Context

Use this module when recent price behavior, sector leadership, entry risk, a macro/geopolitical regime, or historical analogues could materially change the research conclusion. Do not force it into every long-horizon fundamental Quick Scan.

## 1. Trigger rules and cost control

**Always run the compact history packet** for:
- comparisons among two or more ETFs/sectors where recent leadership is part of the question
- short- or medium-horizon research under 36 months
- explicit momentum, “is it extended?”, “rest of year”, rotation, drawdown, or timing-sensitive research
- geopolitical/macro shocks already moving relevant sectors, commodities, currencies, or rates

**Run only if decision-relevant** for:
- a single long-horizon stock or broad-market ETF where fundamentals dominate

**Escalate to a historical event study** only when the user asks or the Geopolitical Risk Analyst can identify a material transmission channel that could change the ranking.

## 2. Compact multi-horizon history packet

When triggered, collect comparable **1M, 3M, 6M, YTD, and 1Y** returns. Add 5D only for fast-moving events and 3Y only when long-run context matters.

Rules:
- Prefer total return when reliable; otherwise label price return explicitly.
- Use the same return definition and as-of date for every candidate.
- Compare each candidate with an appropriate benchmark or peer set, not only in absolute terms.
- For funds with different inception dates, use a common-start-date comparison. Never treat a partial-period YTD number as equivalent to a full-period YTD number.
- For a fund with a short live record, supplement with the underlying index/factor history when available and clearly separate proxy history from fund history.
- Do not infer durable alpha from a short live history.

When structured data and code are available, use `scripts/return_context.py` to calculate benchmark-relative returns and the preceding 3-month return implied by 6M and 3M returns.

## 3. Momentum-dependency test

For any conclusion materially supported by recent performance, ask:

1. Is leadership broad across 3M, 6M, YTD, and 1Y, or concentrated in the latest 1–3 months?
2. Does the candidate still look strong relative to its benchmark outside the latest 3-month window?
3. Is price strength confirmed by earnings revisions, breadth, fundamentals, or a durable macro driver?
4. Is the move now extended enough that expected return has worsened even if the thesis remains intact?

If the ranking depends heavily on the latest 1–3 months, lower confidence and label it **momentum-dependent**.

## 4. Trend and extension diagnostics

Use only when timing/regime sensitivity matters. Prefer:
- 50-day and 200-day moving averages
- distance from those averages
- 52-week high/low and distance to high
- RSI(14)
- recent maximum drawdown
- sector breadth when available

These are regime/extension evidence, never intrinsic value and never standalone trade signals.

## 5. Performance-driver decomposition

Classify recent outperformance primarily as one or more of:
- earnings/fundamental improvement
- valuation multiple expansion
- interest-rate sensitivity
- commodity exposure
- currency movement
- sector/factor rotation
- geopolitical event premium
- recovery/mean reversion

A Market Strategist conclusion that cites price strength must identify the likely driver and the evidence that would distinguish durable leadership from temporary repricing.

## 6. Geopolitical and trade-shock transmission

Do not score headlines. Build a causal chain:

`event → market/economic variable → company/fund exposure → earnings/cash-flow effect → valuation/price implication`

Examples of intermediate variables include tariffs, freight rates, shipping capacity, oil/gas prices, inventories, spare capacity, input costs, export volumes, currency moves, sanctions enforcement, defense spending, or regulatory restrictions.

The Geopolitical Risk Analyst must state:
- what exposure is first-order versus second-order
- what part of the shock appears already priced
- what observable development would weaken or reverse the thesis

## 7. Historical event studies

When escalated, identify **2–4 genuinely comparable episodes** when available. Similar headlines are insufficient; the transmission mechanism must be comparable.

For each useful analogue, examine relative performance around the event at approximately:
- +1 week
- +1 month
- +3 months
- +6 months

Also compare starting conditions that can invalidate the analogy, such as:
- valuation
- interest-rate regime
- inventories and spare capacity
- credit conditions
- economic growth/recession state
- currency regime
- policy response

Include at least one counterexample, failed analogy, or reason the present episode may behave differently. Historical analogues are conditional evidence, not forecasts.

## 8. Commodity and futures data hygiene

For oil, gas, metals, or agricultural shocks:
- identify whether the series is spot, front-month futures, a specific contract, or continuous futures
- never compare returns from different contract definitions without flagging it
- flag contract expiry and roll effects
- prefer physical inventories, spare capacity, production/export disruption, and official supply data when they explain the transmission channel
- if sources disagree because of contract construction, explain the difference rather than choosing the most convenient number

## 9. Regime label

When this module materially affects the conclusion, classify the setup as one or more of:
- durable fundamental leadership
- cyclical leadership
- event-driven leadership
- recovery / mean reversion
- extended momentum
- deteriorating trend
- insufficient history

State the observable condition most likely to change that classification.
