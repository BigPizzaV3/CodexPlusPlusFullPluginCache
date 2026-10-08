# Economic ratings, version 1.0

These are transparent judgment rubrics designed for this plugin. They have not been empirically calibrated. Scores compare candidates within a declared scope and horizon; they are not event probabilities or investment recommendations. Freeze the chosen weights before scoring and disclose deviations.

## Three separate outputs

1. **Growth potential, 0–100:** strength of the case for substantial real economic expansion within the horizon.
2. **Overlooked opportunity, 0–100:** evidence of a gap between economic opportunity and attention or provision.
3. **Evidence confidence:** high, medium, low, or insufficient, with a claim-specific explanation.

Also report probability of a precisely defined growth event when supportable, scenario economic sizes, and likely beneficiaries/value capture. Never label the growth rating as a percentage chance.

## Growth rubric

Score each dimension from 0 to 5. Use 1, 2, and 4 for intermediate conditions; half-points only when justified by specific evidence. Unknown is null, not 0 or 2.5.

For each supplied score, test whether its evidence actually addresses that dimension and the defined economic function. Replacement of one delivery method does not prove that the underlying function becomes unnecessary. One hypothetical adverse scenario does not establish generally weak resilience; a technically possible endpoint does not establish an approaching commercial catalyst. If the evidence supports only a conditional illustration, keep it in the scenario analysis and leave the general component unknown unless other evidence justifies it. Apply this discipline to low scores as well as high ones.

| Key | Weight | 0 | 3 | 5 |
|---|---:|---|---|---|
| demand | 20% | Documented lack of willingness/ability to pay or declining relevant need | Clear buyer/budget and measurable need; uneven paid traction | Repeated paid demand across relevant buyers/regions with compelling benefits and durable drivers |
| adoption | 20% | Barriers prevent material adoption within horizon | Observable deployments; significant switching, procurement, or distribution friction | Replicable adoption with credible distribution and short enough purchase/replacement cycles |
| feasibility | 20% | Essential cost, reliability, supply, or regulatory requirements fail | Feasible in bounded settings; major scaling constraints have plausible remedies | Required economics/performance demonstrated at relevant scale; deployment resources credible |
| scale | 25% | Negligible or negative plausible added real annual activity | Material added activity under supported scenarios, but limited breadth or substantial displacement | Large added annual activity within the comparison set, credible buyer budgets and capacity, limited double counting |
| resilience | 15% | Single fragile assumption, subsidy, or easily displaced solution dominates | Survives some adverse cases but exposed to major policy/cost/substitution risks | Expansion supported under diverse plausible conditions with multiple independent demand routes |

The scale dimension must cite absolute added annual size or a defensible range and its baseline. Define scale bands appropriate to the comparison before scoring. A high CAGR alone cannot establish a high scale rating. If neither size nor a credible scale proxy is available, scale is null. Evidence confidence handles measurement uncertainty; resilience concerns the business mechanism's exposure, not source quality.

Weighted rating = 20 × sum(weight × component). Weights sum to 1. A full score is available only when every component is supplied. If any component is null, show bounds computed by assigning the missing components 0 and 5 and retain provisional status. Do not renormalize known components to disguise missing evidence.

Suggested interpretation: 80–100 very strong thesis; 65–79 strong; 50–64 mixed/conditional; below 50 weak on current assumptions. These descriptive bands are heuristic. Confidence can prevent a numerical rating from qualifying for the main ranking.

## Overlooked-opportunity rubric

| Key | Weight | 0 | 3 | 5 |
|---|---:|---|---|---|
| provision_gap | 25% | Supply/investment already adequate or no viable demand | Documented regional/segment shortage with a feasible remedy | Persistent economically material shortage despite credible demand and viable remedies |
| attention_gap | 20% | Strong attention aligned with opportunity, or no evidence of a gap | Measurable relative neglect in a specified segment | Strong comparator evidence that relevant attention or expectations lag economic fundamentals |
| bottleneck | 20% | Peripheral or easily bypassed | Useful complement with some alternatives | Necessary, hard-to-substitute enabling function across multiple growth pathways |
| inflection | 20% | No credible catalyst within horizon | Plausible catalyst with uncertain timing | Observable cost, capability, rule, or adoption threshold nearing commercial relevance |
| accessibility | 15% | Opportunity structurally closed to plausible participants | Entry paths exist with substantial capital, knowledge, or distribution needs | Credible paths for several participant types with a clear customer and manageable entry constraints |

The participant types for accessibility are suppliers, service firms, entrepreneurs, workers, and capital providers at industry level; name who actually can enter. This is distinct from stock liquidity or expected stock returns. Do not infer attention_gap from absence of search results. An unknown gap stays null. Low visibility caused by weak economics should lower the appropriate components rather than become a positive thesis.

## Ranking and robustness

Main ranking: use complete growth ratings with high/medium confidence. Show overlooked score alongside; do not blend it invisibly into growth. Low/insufficient confidence or missing growth components go to a separately labeled provisional/watchlist table. Keep all candidates in the audit data, including rejected ones. Treat near ties as tiers when modest assumption or weight changes reverse the order.

Use the calculator's one-at-a-time weight perturbations (0.5× and 1.5× each weight, normalized) to show rank ranges among eligible candidates. These rank ranges test chosen weights only; they are not confidence intervals. Also change pivotal economic inputs, timing, and common shocks. Explain correlated factors and avoid counting the same advantage repeatedly across demand, adoption, and feasibility.

Probability of expansion must be elicited against the defined event using evidence and reference classes, not derived by dividing a rating by 100. For long-horizon forecasts use sensible rounding (often five percentage points) and explain subjective uncertainty; numerical precision is not accuracy.
