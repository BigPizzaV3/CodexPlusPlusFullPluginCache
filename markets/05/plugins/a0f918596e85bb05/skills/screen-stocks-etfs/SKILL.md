---
name: screen-stocks-etfs
description: Research and compare stocks, ETFs, sectors, and standardized illustrative portfolios using current sources and a transparent analytical panel. Use for general security screening, sector research, valuation comparisons, ETF structure, risk comparisons, historical-regime analysis, hypothetical scenario testing, and investment education. Do not collect or use personal financial circumstances, tailor results to a recipient, provide buy or sell instructions, time transactions, or prescribe allocations.
---

# Stock and ETF Research Panel — v2.6

Run an evidence-first investment-research process using blind analytical roles, an independent Chief Risk Officer, scenario testing, and explicit dissent. Panel titles are modelled analytical perspectives, not people or licensed advisers. Results must be general and impersonal: anyone selecting the same securities and published scenario assumptions receives the same analysis.

## Hard boundary: no personalization

Never request, retain, repeat, infer, or use a recipient's account type, jurisdiction, tax status, dollar amounts, income, net worth, holdings, exposures, withdrawals, expenses, liquidity needs, loss capacity, risk tolerance, age, family circumstances, or other personal financial information.

If volunteered, acknowledge once without repeating it: “I’ll treat this as a general research scenario and will not use personal financial details.” Then ignore it. Security names may remain only as candidate inputs; discard ownership claims, weights, cost bases, gains, losses, and account context.

Allowed controls are impersonal: candidate universe, security type, market/listing universe, reporting currency, hypothetical horizon, general objective, scenario shocks, and requested output depth. Never translate excluded personal facts into an allowed control.

## Required resources

Read only the resources needed for the route, but always follow their hard rules:

- [references/modes.md](references/modes.md) — depth and evidence budget
- [references/judges.md](references/judges.md) — analytical roles, weights, role boundaries
- [references/market-history.md](references/market-history.md) — historical price/regime module and geopolitical analogues
- [references/valuation.md](references/valuation.md) — valuation-sensitive candidates
- [references/report-template.md](references/report-template.md) — output contract
- [references/compliance.md](references/compliance.md) — named-security conclusions and model portfolios

Use `scripts/aggregate_scores.py` when structured scores and code execution are available. Use `scripts/graham_growth.py` for every profitable individual-stock finalist when code execution is available. Use `scripts/return_context.py` when structured multi-horizon returns are available and relative/common-window return math would reduce ambiguity.

## 1. Route the research question

Treat each invocation as a new decision unless it is clearly a follow-up in the same active research thread. Preserve securities and impersonal scenario controls only; never import personal context.

Classify the universe:

- **Closed:** user explicitly restricts analysis to named candidates.
- **Expanded:** named ideas are starting points and alternatives are allowed.
- **Open:** user asks for the best shortlist or model without restricting candidates.

If universe scope is genuinely ambiguous and would change research, ask only:

> Should I evaluate only your choices, improve them using outside alternatives, or build independently from the wider market?

If the general objective is absent after removing personal facts, ask only: “Which standardized research objective should I use: capital preservation, balanced growth, or long-term growth?” If horizon is absent, ask for a hypothetical horizon or compare predefined horizon scenarios. Do not conduct a personal intake.

## 2. Choose depth and evidence budget

Select Quick Scan, Full Panel, or Panel Debate from `modes.md`. Use the smallest evidence set capable of changing the conclusion.

Evidence-budget rules:

- Reuse one timestamped evidence packet across all roles; do not independently re-search the same fact for each role. Prefer batched/tearsheet sources that return several required fields in one call.
- Do not collect broad macro series unless they have a plausible transmission channel to the ranking.
- Do not run historical event studies merely because a geopolitical headline exists; trigger them only when the event could materially change the ranking or the user asks.
- Do not require every technical indicator for long-horizon fundamental questions. Trigger the market-history module according to `market-history.md`.
- For comparisons, use the same as-of date, return definitions, benchmark logic, and common windows across candidates. Do not web-search a fact already supplied by a current primary/structured source unless confirmation could change the decision.

## 3. Scout before constructing candidates

For a closed universe, analyze supplied candidates consistently and introduce no replacement.

For expanded/open universes, run a non-voting scout pass:

1. Translate the stated general objective into functional jobs.
2. Consider at least two credible alternatives for each material job when available.
3. Reject obvious scenario-fit failures before deep research.
4. Advance three to six candidates or strategies.
5. Record why each finalist survived; compress this in Decision View.

For standardized portfolio comparisons, a non-voting Portfolio Architect builds three genuinely distinct models when the universe permits: a submitted **impersonal scenario** model, a credible alternative, and an independent alternative. A personal portfolio is never recreated as a candidate model; retain only its security names. Differences must be substantive, not cosmetic percentage changes.

## 4. Apply objective gates

Before voting, mark candidates `pass`, `caution`, or `fail`:

- **Scenario fit:** horizon/objective alignment and product eligibility in the stated generic universe.
- **Financial integrity:** evidence quality, solvency/cash generation where relevant, and whether valuation can be estimated responsibly.

Under 18 months emphasize catalysts, regime sensitivity, preservation, and entry risk. At 18–36 months balance catalysts and normalized economics. Beyond three years emphasize intrinsic value, quality, and compounding.

A hard `fail` requires an objective failure such as financial distress, unusable evidence, product ineligibility, or inability to value responsibly. Macro, geopolitical, momentum, or ordinary valuation concerns are not vetoes; they change score, confidence, or scenario sensitivity.

## 5. Build one timestamped evidence packet

Research candidates using comparable definitions and current sources whenever prices, holdings, earnings, estimates, rates, laws, conflicts, or economic releases may have changed.

Source priority:

1. Filings, company reports, and official fund pages
2. Central banks, statistical agencies, treasuries, regulators, official inventories
3. Index providers and official holdings files
4. Reputable wire services for unfolding events
5. High-quality secondary sources only when primary evidence is unavailable

Collect only decision-relevant evidence from these modules:

**Core fundamentals/structure**
- normalized earnings power, cash flow, leverage, liquidity, profitability, dilution
- ETF holdings, concentration, factor/sector exposure, AUM, spread, tracking, fees
- valuation and market-implied expectations

**Market behavior — trigger per `market-history.md`**
- systematic 1M / 3M / 6M / YTD / 1Y behavior when market regime or recent leadership is decision-relevant
- benchmark-relative performance and common-window comparisons
- breadth, revisions, positioning, trend/extension only when useful
- whether recent leadership is fundamental, cyclical, event-driven, mean-reverting, or merely extended

**Macro/geopolitical — trigger only when causal**
- rates, inflation, growth, employment, credit, consumption, currency
- conflicts, tariffs, sanctions, trade restrictions, shipping, commodities, regulation
- explicit transmission path from event → economic variable → revenue/cost/margin/valuation → candidate
- historical analogues only under the rules in `market-history.md`

**Implementation under generic assumptions**
- fund-level withholding, domicile, hedging, currency conversion, liquidity and trading friction when material to the stated generic market universe

Always distinguish fact, estimate, and inference. Flag stale holdings, one-offs, peak-cycle earnings, distorted multiples, source conflicts, young-fund history, and futures-series roll effects.

For valuation-sensitive candidates apply `valuation.md`.

## 6. Run the blind committee

Use the roster and weights in `judges.md`. Set weights before seeing votes. Give every voter the identical decision brief and evidence packet. Later members may see factual gate findings, not another member's scores or preference.

Each voter returns:

```json
{
  "candidate": "TICKER",
  "committee_member": "analytical_role_title",
  "score": 0,
  "confidence": 0.0,
  "thesis": "one sentence",
  "best_evidence": ["dated claim with source"],
  "main_risk": "one sentence",
  "invalidation": "observable condition"
}
```

Scores are 0–10; confidence is 0–1. Abstain when critical evidence is missing. Keep roles inside their defined lens so momentum, macro, geopolitics, valuation, and portfolio construction are not double-counted.

## 7. Aggregate, challenge, and debate

Aggregate with confidence and disagreement penalties using `aggregate_scores.py` when available. Do not select a winner mechanically from score alone.

After all votes, the non-voting Chief Risk Officer challenges the preliminary winner with the strongest evidence-based failure case, hidden assumption, concrete loss/liquidity path, invalidation condition, and one verdict: `clear`, `monitor`, `limit_in_model`, or `exclude_from_model`.

Use Panel Debate only when requested, when finalists are close, disagreement is large, or the ranking depends on a contested assumption. Freeze blind baseline votes before rebuttal; permit one evidence-based revision per affected member.

## 8. Run scenarios that can actually change the ranking

Choose two or three precise shocks with real transmission channels: recession, rate shock, inflation resurgence, commodity shock, trade restriction, currency move, earnings disappointment, or another event supported by the evidence packet.

Rate each finalist resilient, neutral, or vulnerable with one causal sentence. Quantify only when assumptions are explicit. State whether any scenario changes the winner and which observable condition would invalidate the base classification.

## 9. Present the smallest useful result

Follow `report-template.md`. Lead with the research conclusion, then evidence, complete role decisions, strongest dissent, Chief Risk Officer, and decisive scenarios. Keep raw scoring machinery in Audit View unless requested.

For standardized combinations, evaluate the combination separately: look-through sector exposure, duplicated holdings, factor/currency concentration, costs, and each security's distinct job. Effective single-sector exposure above 55% is a caution.

Never direct a purchase, sale, position size, entry price, order type, or execution timing. End covered responses with the publisher-conflict statement and exact disclosure in `compliance.md`.

## 10. Follow-ups

Reuse unaffected evidence and votes while still current. Rerun only what changed:

- candidate/universe → scout plus candidate-dependent work
- horizon/objective → fit, weights, and affected roles
- macro release → Macro, Market, Chief Risk Officer
- geopolitical event → Geopolitical, Macro, Market when price regime changes, and Chief Risk Officer
- `show scores` / `audit this` → switch presentation view without rerunning research

Never repeat the full report unless requested.
