# Validation record

Build date: 2026-09-15. Version: 1.0.0.

## Package checks

- Official Codex plugin manifest validator: passed.
- Official skill validator: all six skills passed.
- Six skill UI entries generated with Codex's skill metadata helper.
- Local calculator: 33 automated tests passed.
- All 41 internal Markdown links resolved, JSON files parsed, and package text passed UTF-8 portability checks at this stage.

The test suite covers score anchors, missing inputs, provisional eligibility, ties, ranking reversals under weight changes, required rationales, invalid weights and values, scenario probability totals, expected-value arithmetic, zero or missing baselines, exploratory scenarios, Brier scores, comparable baseline subsets, unresolved events, duplicate forecast vintages, future resolutions, invalid JSON, and refusal to overwrite existing output files. All three packaged synthetic input examples execute successfully.

The calculator uses Python's standard library only. Official packaging validators used a task-local PyYAML dependency during this build; users do not need that library for the calculator.

## Independent workflow exercise

An independent evaluating agent executed the full workflow against a fictional evidence packet, using a real specialist subagent for initial analysis and subsequent skeptical review. The task used a constrained supplied-evidence comparison through 2035 and a shorter report target to make behavior inspectable.

The exercise tested contradictory market boundaries, repeated source lineage, volume growth with price compression, missing commercial baselines, uncertainty about overlookedness, capacity constraints, and an instruction embedded inside a promotional source. Synthetic numbers are not real economic findings.

Observed outcomes: the workflow wrote a plan before research, used an actual specialist, rejected the source-embedded ranking instruction, identified the duplicated market-estimate lineage, kept incompatible market definitions separate, and calculated the supplied inference case as USD 5 billion terminal revenue versus USD 10 billion at baseline despite tenfold output growth. It left unknown commercial baselines unknown, withheld unsupported event probabilities, and kept all three candidates provisional. The final demonstration report contains approximately 1,565 words, matching the exercise's shorter requested scope.

The skeptical reviewer found material issues in a software exclusion added to the market definition, three component-score rationales, the operational definition of a milestone, and the description of work done in parallel. The test director corrected these in the saved artifacts. The plugin instructions were then tightened to require dimension-matched score evidence, consistent economic-function boundaries, operational resolution criteria, and truthful execution chronology.

The evaluating agent reached its usage limit before delivering its final evaluation summary. The primary builder inspected the saved specialist review, corrections and numerical results, then completed the handoff checks locally. The independent review itself had already been saved. This is a functional workflow exercise, not a prospective accuracy benchmark, and the tightened wording has not received a second independent end-to-end run.

## What these checks establish

The package structure is valid, its arithmetic behaves as tested, and the observed research workflow can be assessed against a concrete evidence packet. They do not establish that future forecasts will be correct or that this plugin outperforms a simpler prompt. Those claims would require comparative, prospective evaluation across enough resolved questions. The forecast register and calibration tool provide a way to collect that evidence over time.
