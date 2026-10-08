# Ranking and scenario policy

## Separate four questions

1. What could the shareholder earn at today's verified price?
2. How likely is the explicitly defined success event, conditional on assumptions?
3. What could be lost, and through which mechanisms?
4. How strong is the evidence behind the model?

No confidence score, expert vote, or checklist total may be presented as a success probability. Coarse subjective scenarios are not calibrated investment odds. If defensible weights are unavailable, report unweighted scenario ranges and conditional ranks; omit percentage probabilities and the automated probability ranking.

## Scenario construction

Use mutually exclusive, collectively exhaustive states at an appropriate level of detail. Include commercial failure, funding stress or severe competition when material. A bull/base/bear split can represent broad regimes, but is not automatically sufficient. For clinical or binary-event businesses use conditional event trees before aggregating to states. Do not multiply dependent probabilities as though independent.

For each state document demand, price/share, revenue, margins, reinvestment, tax, financing, diluted shares, cash distributions, terminal valuation, and matched benchmark wealth. Keep driver relationships coherent: revenue growth requires capacity or reinvestment; buybacks require cash; high rates can affect demand, funding and multiples together. An optimistic terminal multiple plus exceptional operating growth requires an explicit justification.

Across companies, reconcile benchmark assumptions to the same market outlook. If state weights differ because they condition on company-specific events, document the joint/conditional mapping and reconcile the implied benchmark marginal distribution. Identical bull/base/bear labels with different probabilities do not establish a common market scenario. Flag inconsistent benchmark forecasts before comparing success probabilities. The calculator evaluates supplied states; this economic consistency check belongs to the analyst/auditor.

Define distributions using reference classes, base rates, current evidence and explicit adjustments. Record each probability's rationale and range. When the evidence is weak, carry multiple plausible probability sets rather than presenting a finely calibrated point. A Monte Carlo model is optional; simulated path count is not new evidence.

## Return conventions

The bundled `../scripts/scenario_rank.py` assumes one initial purchase and terminal wealth equal to terminal per-share price plus cumulative cash distributions **held as cash**, with no reinvestment, fees or tax. Terminal price must already incorporate dilution and corporate actions. Normalize into the run currency before input. The benchmark must use the same distribution/cost conventions. For timed distributions, reinvestment, FX paths or user-specific after-tax returns, create a separate auditable cash-flow model and label it; do not silently feed an IRR into a CAGR field.

For horizon H, entry P, terminal price V and distributions D:

`wealth_multiple = (V + D) / P`

`total_return = wealth_multiple - 1`

`scenario_CAGR = wealth_multiple ** (1/H) - 1`

`expected_total_return = sum(p * wealth_multiple) - 1`

`annualized_expected_wealth = sum(p * wealth_multiple) ** (1/H) - 1`

The last quantity is **not** the weighted average of scenario CAGRs, a typical path, or a guaranteed annual return. Total loss is wealth zero and CAGR -100%. Benchmark-relative success requires matched states; a fixed guessed benchmark hides uncertainty. The default success event is strict wealth > 1 and strict wealth > benchmark wealth; equality is not success. Terminal loss probability is not maximum drawdown, and does not prove permanent impairment.

## Default rank

1. Apply human evidence/survivability checks before marking evidence_eligible. Do not exclude ordinary uncertainty merely for being uncertainty; explain material gaps.
2. Require central plus at least one genuinely adverse plausible sensitivity set. Calculate metrics for each. Use common, comparable stress definitions across companies; padding one candidate with mild stresses is invalid.
3. Conservative metrics are minimum annualized expected wealth and success probability, and maximum severe-terminal-loss probability across these sets. These are stress-envelope summaries, not confidence bounds.
4. Apply the mandate's disclosed probability/downside thresholds. Defaults 60% success and at most 20% probability of terminal loss >=40%, plus positive conservative annualized expected wealth. These are configurable policy assumptions.
5. Within eligible candidates form a Pareto frontier: higher conservative return, higher success, lower severe-loss probability. A company is dominated if another is at least as good on all three and strictly better on one.
6. Order the frontier by conservative annualized expected wealth, then success, then lower loss; exact computational ties use security ID for reproducibility only. Then list other eligible candidates, explicitly marked dominated. Present uncertainty-overlapping candidates in tied tiers even if the script assigns positions.
7. Also show probability-first and maximum-central-scenario-upside tables. The upside table is speculative potential, not a recommended substitute for the main ranking. Display nonqualifiers and reasons separately.

## Sensitivity and interpretive checks

Rebuild 5-, 7- and 10-year economic forecasts independently; changing only the annualization denominator is not a horizon sensitivity. Assess growth, margin, reinvestment, dilution, terminal multiple/discount rates, benchmark states and probabilities. Identify the smallest economically plausible assumption changes that reverse adjacent ranks. Show a break-even entry price or value range with explicit assumptions, not a precise price target implying certainty.

Test realistic correlated downside and the role of favorable tail outcomes. A high expected return driven entirely by a remote bull state deserves separate labeling. Compare candidates with the broad-market alternative; do not manufacture an industry winner when all candidates are unattractive or unsupported. All-in position sizing requires portfolio context and is outside a bare industry-ranking mandate.
