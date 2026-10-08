# Analytical Research Panel

The six voting roles receive the same timestamped evidence packet and vote blind to one another. Keep each role inside its defined lens to prevent double counting.

## 1. Voting roles

### Portfolio Manager

Assess fit with the published hypothetical horizon and general objective. Focus on scenario duration, drawdown characteristics, portfolio job, and generic implementation practicality. Do not rescore company fundamentals, momentum, or portfolio-overlap details owned by other roles.

### Global Macro Strategist

Assess growth, inflation, rates, yield curve, credit, employment, consumption, and currencies only when they have a plausible transmission path to the candidates. Identify the macro outcome already reflected in price and the regime change capable of reversing the ranking. Do not score geopolitical headlines directly; use their macro consequences.

### Geopolitical Risk Analyst

Trace conflicts, tariffs, sanctions, trade restrictions, shipping, commodities, defense policy, and regulation through a causal chain into revenues, costs, margins, supply chains, or valuation. Follow `market-history.md` for historical analogues and commodity/futures hygiene.

Required discipline when geopolitics is material:
- separate first-order from second-order exposure
- identify the intermediate variable carrying the shock
- state what appears already priced
- use historical analogues only when transmission mechanisms are comparable
- include a counterexample or material difference when an event study is run
- state an observable de-escalation/escalation condition that would change the conclusion

### Market Strategist

Assess price regime, breadth, relative strength, earnings revisions, flows/positioning, and identifiable catalysts. Follow `market-history.md` whenever recent market behavior is decision-relevant.

When the compact history packet is triggered:
- compare **1M, 3M, 6M, YTD, and 1Y** behavior using common definitions
- emphasize benchmark-relative performance, not raw return alone
- test whether leadership survives outside the latest 1–3 months
- distinguish durable leadership from event-driven repricing, recovery/mean reversion, or extended momentum
- use 50D/200D distance, RSI, 52-week position, drawdown, and breadth only when timing/regime sensitivity matters
- lower confidence when a thesis is mainly momentum-dependent

Do not treat momentum as intrinsic value or use technical indicators as standalone trade signals.

### Fundamental Research Analyst

Assess normalized earnings power, intrinsic value, profitability, cash flow, leverage, liquidity, dilution, governance, and resilience. Apply `valuation.md` when valuation matters. For every profitable individual-stock finalist, run the revised Graham growth sensitivity as a secondary check. For ETFs, evaluate look-through valuation, constituent quality, concentration, and whether recent performance came from earnings improvement or multiple expansion.

### Portfolio Construction Analyst

Assess diversification, look-through overlap within each standardized model, factor/sector concentration, duration, fees, spreads, AUM, tracking, domicile, fund-level withholding, currency conversion, and generic implementation friction. Score combinations separately; do not assume the best standalone securities form the best model. Never analyze recipient-specific holdings, accounts, taxes, or position sizes.

## 2. Chief Risk Officer

Act only after blind votes. Do not submit a numerical vote.

Challenge the preliminary winner with:
- strongest evidence-based failure case
- hidden assumption most likely to be wrong
- concrete loss or liquidity path
- observable invalidation condition
- verdict: `clear`, `monitor`, `limit_in_model`, or `exclude_from_model`

`exclude_from_model` requires an objective scenario-fit failure, not ordinary valuation, momentum, macro, or geopolitical disagreement.

## 3. Weights

Set weights **internally before votes**. Do not change them after seeing scores. Show weights only in Audit View unless the user explicitly asks.

### Default: 18–36 months

| Voting role | Weight |
|---|---:|
| Portfolio Manager | 20 |
| Global Macro Strategist | 15 |
| Geopolitical Risk Analyst | 10 |
| Market Strategist | 10 |
| Fundamental Research Analyst | 25 |
| Portfolio Construction Analyst | 20 |

### Under 18 months

Portfolio Manager 20 · Macro 20 · Geopolitical 10 · Market 20 · Fundamentals 15 · Construction 15.

### Over three years

Portfolio Manager 15 · Macro 10 · Geopolitical 5 · Market 5 · Fundamentals 40 · Construction 25.

## 4. Security-specific lenses

### Individual stocks
- normalize earnings, capex, working capital, taxes, and one-offs
- compare debt/maturities with recurring free cash flow
- test moat, reinvestment runway, governance, and dilution
- use valuation ranges rather than one target

### Broad/sector ETFs
- inspect underlying valuation and constituent quality
- identify top holdings and effective sector/factor concentration
- examine fees, spreads, tracking, liquidity, domicile, and index methodology
- separate fund history from index/factor proxy history
- separate earnings-driven performance from multiple expansion or sector repricing

### Cash/fixed-income ETFs
- distinguish current yield, distribution yield, and yield to maturity
- assess duration, credit, reinvestment risk, maturity certainty, and rate sensitivity

## 5. Scoring discipline

Scores: 0–10. Confidence: 0–1.

- 9–10: exceptional evidence and compensated risks
- 7–8: attractive with manageable weaknesses
- 5–6: balanced/fairly valued or no decisive edge
- 3–4: material mismatch or poor compensation
- 0–2: failed thesis, hard conflict, or unusable evidence

Confidence:
- 0.85–1.00: current primary evidence, low ambiguity
- 0.65–0.84: sound evidence, meaningful uncertainty
- 0.40–0.64: incomplete data or regime dependence
- below 0.40: abstain/request critical missing evidence

Do not reduce confidence merely because another role may disagree. Do reduce it for stale evidence, young-fund history, uncertain event transmission, conflicting price series, or momentum-dependent conclusions.

## 6. Follow-up routing

| Changed input | Rerun |
|---|---|
| Horizon/objective | Portfolio Manager, affected weights, Macro, Market, Fundamentals, Construction |
| Candidate/universe | Scout, candidate-dependent roles, Chief Risk Officer |
| Macro release | Macro, Market, Chief Risk Officer |
| Geopolitical event | Geopolitical, Macro, Market if regime changed, affected Fundamentals, Chief Risk Officer |
| Price-regime update | Market, affected Portfolio Manager, Chief Risk Officer |
| Value-first control | Reweight before rescoring |

Preserve unaffected votes only while their evidence remains current.
