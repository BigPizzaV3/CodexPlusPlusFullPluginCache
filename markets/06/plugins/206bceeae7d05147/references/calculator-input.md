# Scenario calculator input contract

The calculator is a deterministic comparison of supplied assumptions. It does not retrieve financial data, construct a valuation, validate source quality or estimate probabilities. Python 3.10+; standard library only. Input and output are UTF-8 JSON. See [complete fictional fixture](../tests/fixtures/scenario-example.json) and [method](ranking-method.md).

From the plugin root:

```text
python scripts/scenario_rank.py tests/fixtures/scenario-example.json
python scripts/scenario_rank.py /path/to/run/scenario-input.json --output /path/to/run/ranking.json
```

The output path's parent must exist. The tool refuses to overwrite the input itself, including a link to it. Other existing output files are replaced; use a new dated/versioned output path to preserve research history.

## Required fields

All fields below are required. Unknown keys and duplicate JSON keys are rejected to catch misspellings. Keep richer valuation drivers, provenance and probabilities' rationale in the run's evidence/assumptions ledgers, linked through IDs.

| Object | Fields and meaning |
|---|---|
| Run | `schema_version`: integer 1; `horizon_years`: finite positive number; `currency`: common reporting/return currency; `severe_loss_threshold`: fraction >0 and <=1; `policy`; nonempty `companies` |
| policy | `min_success_probability`, `max_severe_loss_probability`: fractions in [0,1] |
| Company | unique `id` (prefer exchange:ticker:share-class), `name`, `currency` matching run, `price`, boolean `evidence_eligible`, nonempty string array `eligibility_notes`, nonempty `scenario_sets` |
| price | `value`: positive finite entry price; `as_of`: YYYY-MM-DD; `source_id`: ledger reference |
| Scenario set | unique `name`; nonempty `scenarios`. One must be named exactly `central` |
| Scenario | unique `name` within set; `probability` in [0,1]; nonnegative `terminal_price`, `cash_distributions`, `benchmark_wealth_multiple` |

All rates/probabilities are decimal fractions, not percentage points: 20% is `0.2`. Prices/distributions are per share in the run currency. `terminal_price` must already include forecast dilution and corporate actions. `cash_distributions` is cumulative cash held without reinvestment. Benchmark wealth includes distributions under the same convention. No fees, tax or FX conversion is performed.

Each set's probabilities must sum to one within 1e-12. They are not silently normalized. Numeric booleans, NaN, infinity, duplicate identifiers and currency mismatches fail validation. The calculator checks date format, **not freshness, market sessions, filing completeness or evidence**. The analyst/auditor owns those checks before setting evidence_eligible.

## Central-only and sensitivity behavior

Central-only inputs can be calculated but are not eligible for an investment rank. At least one economically distinct adverse sensitivity set is required: it must lower expected terminal wealth or success probability, or raise severe-loss probability, compared with central. Renaming, reordering, splitting identical-payoff states, adding zero-probability states or supplying only upside cases does not satisfy this gate. Decimal comparisons protect these checks from ordinary floating-point artifacts. The script cannot establish economic plausibility, sufficient stress magnitude or comparable stress coverage. The director/auditor owns those checks and the source-linked probability rationale.

Do not populate fictional probabilities just to run this tool. If weights cannot be defended, use a nonprobabilistic scenario table and leave probability unavailable. The fixture is fictional test data, never a starting valuation template for real stocks.

## Output interpretation

Each company includes source price snapshot, calculated scenario sets, central metrics, conservative minima/maxima across sets, `has_distinct_sensitivity`, `has_adverse_sensitivity`, eligibility reasons, Pareto status, dominating IDs and numerical rank. Returns are fractions. `annualized_expected_wealth` and `probability_weighted_scenario_cagr` are different quantities; neither is a guaranteed realized annual return.

`ranked_ids` orders eligible companies with frontier members first. `success_first_eligible_ids` and `central_bull_upside_eligible_ids` are alternative comparisons **within the eligible group**. Watchlist candidates remain in `companies` with all computed scenario metrics; show their speculative upside separately when relevant and clearly distinguish their ineligible status. Exact ID tie-breaks are computational bookkeeping, not investment evidence.

The director may present tied tiers or no supported ranking after auditing evidence/model uncertainty. A rank output does not override the evidence gate, mandate or human review of assumptions. See [ranking method](ranking-method.md) for formulas and the policy rationale.
