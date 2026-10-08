# Calculation interface

Run `python <plugin-root>/skills/horizon-forecast/scripts/forecast_math.py MODE INPUT.json --output NEW-OUTPUT.json` using an available Python 3 runtime. Modes are `scores`, `scenarios`, and `calibrate`. Only the standard library is required. The script performs local arithmetic and never calls external services. Output paths must be new; it refuses to overwrite evidence or previous results. Omitting `--output` prints JSON.

Adapt executable/path syntax to the host. In Codex desktop, discover the bundled runtime if the ordinary Python command is unavailable. If code execution is unavailable, show transparent arithmetic and disclose that the helper did not run.

## Scores

Input object:

- `comparison_scope`: common geography, metric and horizon description.
- Optional `growth_weights`, `overlooked_weights`: exact dimension keys from [scoring](scoring.md), nonnegative and totaling 1. Defaults are the version 1.0 rubrics.
- `candidates`: nonempty array of `{name, confidence, confidence_reason, growth, overlooked, rationale}`.
- `growth` and `overlooked`: each includes all rubric keys, with numbers from 0 to 5 or null. `confidence` is high/medium/low/insufficient. `rationale` maps each supplied component key to an evidence-based explanation with claim/source IDs.

Output preserves rationales, scores, missing-data bounds, and confidence. Only complete growth scores with high/medium confidence enter the main ranking. A candidate may have an eligible growth rank with an incomplete overlooked score; the latter remains explicitly bounded. Ties share a rank. Sensitivity rank ranges vary one growth weight at a time by 0.5× and 1.5×, then normalize, among the same eligible candidates.

The script validates arithmetic and required metadata. It cannot verify that a rationale is true, a market is comparable, or a confidence label is deserved. The director must audit those properties. Do not interpret bounds from missing components as probabilistic intervals.

## Scenarios

Required metadata: `market`, `geography`, `metric`, `currency`, `units`, `price_basis`, `baseline_source`, `baseline_year`, `horizon_year`, `baseline_size`, and `mode` (`weighted` or `exploratory`). All sizes must use the same units, annual flow definition, and declared price basis. Each scenario includes `name`, `terminal_size`, and `assumptions`.

For weighted mode add `partition_confirmed: true`, `partition_definition`, and scenario `probability` plus `probability_basis`. Define terminal_size as a conditional mean. Probabilities use 0–1 and sum to 1. For exploratory mode omit probabilities or use null. The input's partition assertion must be checked by an analyst; the script cannot prove the states are non-overlapping or exhaustive.

Output computes per-scenario added annual size/CAGR. Weighted mode additionally reports expected terminal size, CAGR of expected terminal size, and expected CAGR. It deliberately does not infer expansion-event probability from scenario means. A missing baseline cannot be calculated; use qualitative analysis rather than passing zero. A genuinely zero observed baseline is allowed but gives null CAGR.

## Calibration

Required top-level fields: `evaluation_date` (YYYY-MM-DD), `vintage_policy` describing how a common lead time was selected, and nonempty `forecasts` array. Each event has `event_id`, `question`, `forecast_date`, `deadline`, `resolution_rule`, `probability`, and `outcome` (0, 1, or null). Resolved rows also require `resolved_on` and `resolution_source`. Optional `baseline_probability` must come from a comparator available at the forecast time.

Use one vintage per event. The helper rejects duplicate event IDs, future resolutions, invalid probabilities, and forecasts recorded at/after the deadline. Resolution before deadline is allowed for an event that has already occurred under its rule. The analyst must verify early resolution is justified, information was actually available at the forecast date, and events are not duplicated under different IDs.

Output: resolved/pending counts, binary Brier score, descriptive reliability bins, and baseline comparison using exactly the subset with supplied comparator probabilities. A zero baseline loss gives null skill score to avoid division by zero. Unresolved rows do not count as failures.

Runnable synthetic inputs are in [examples](../../../examples/). They demonstrate structure and arithmetic, not real forecasts. Run [tests](../../../tests/test_forecast_math.py) with `python -m unittest discover -s <plugin-root>/tests -v`.
