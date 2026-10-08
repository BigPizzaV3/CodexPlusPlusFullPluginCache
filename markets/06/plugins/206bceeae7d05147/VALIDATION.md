# Validation record

Final validation date: **2026-09-17**. Plugin: **equity-council 1.0.2**.

## Website and subtitle update (1.0.2)

Added `interface.websiteURL` with the user's established Quiet Engine URL, `https://ko-fi.com/quietengine`, and an explicitly optional Ko-fi tip-jar link in the long description. Set the subtitle to `Long-Term Equity Research` (25 characters). Local checks verify the website field, tip-jar URL, subtitle limit and rebuilt archive. Research skills and calculation logic are unchanged.

## Directory artwork correction (1.0.1)

The directory upload rejected 1.0.0 because it required `interface.composerIcon` and `interface.logo`. The local authoring validator had accepted their omission; its success did not establish compliance with that directory requirement. Version 1.0.1 adds explicit references to bundled square PNG artwork: `assets/icon.png` (256 × 256) and `assets/logo.png` (1024 × 1024), plus the editable SVG source. Local verification checks PNG decoding, square dimensions, manifest references and ZIP inclusion. The corrected upload still needs to be submitted to the directory; no server-side acceptance is claimed.

## Results

| Check | Result | What it establishes |
|---|---|---|
| Official plugin-creator manifest validator | PASS | Manifest satisfies the local Codex plugin ingestion validator |
| Official skill-creator quick validator | PASS, 11/11 skills | Skill frontmatter and naming satisfy the validator |
| Skill UI metadata and local reference checks | PASS | Names, invocation prompts, description lengths and bundled links resolve |
| Python unit/integration tests | PASS, 22/22 | 17 scenario-calculator tests and 5 run-initializer tests |
| Independent implementation/contract review | One actionable finding, fixed and regression-tested | Adverse-sensitivity gate now rejects optimistic-only and economically equivalent alternatives |
| Independent bounded offline workflow exercise | Completed with correct conditional/watchlist outcome | Plan-first behavior, dilution arithmetic, source dependence and honest missing-evidence treatment |
| Baseline and specialist walkthroughs | Completed, limited scope | Synthetic decision-boundary checks; no measured improvement over baseline claimed |

## Calculation coverage

Tests cover independently calculated returns; annualized expected wealth versus probability-weighted CAGR; total loss; exact success/severe-loss boundaries; decimal probability and loss thresholds; adverse sensitivity; optimistic-only alternatives; split/renamed/zero-mass scenario equivalence; Pareto dominance and deterministic ties; evidence ineligibility; malformed numeric inputs; currency mismatch; duplicate IDs, scenario names and JSON keys; unknown fields; source snapshot preservation; UTF-8; and refusal to overwrite the input file.

The initializer tests cover default horizon settings, Unicode, explicit overrides, invalid input, preservation of existing paths and refusal to create research runs inside the plugin installation.

Run locally from the plugin root with a working Python 3.10+ interpreter:

```text
python -B -m unittest discover -s tests -v
```

The helpers and test suite use Python's standard library. Official skill/manifest validators belong to the host authoring tools and use PyYAML; that is not a dependency of the delivered research helpers.

## Review findings resolved

1. **Adverse sensitivity:** the first implementation treated any different scenario set as stress. Independent review demonstrated that an upside-only set or a split identical-payoff state could pass. The final implementation aggregates economically equivalent states, ignores zero-mass states, and requires lower expected terminal wealth/success probability or greater severe-loss probability in a noncentral set. Three regression tests cover the gap. Economic plausibility and adequate stress magnitude remain analyst responsibilities.
2. **Floating-point boundaries:** ordinary binary arithmetic can misclassify an exact loss or probability threshold. Event comparisons and probability sums use decimal arithmetic; targeted tests cover the observed boundary cases. Return annualization remains finite floating-point computation.
3. **Windows test directories:** Python TemporaryDirectory created restrictive directories in this sandbox. A normal mkdir probe isolated the issue; the test setup now uses workspace directories with inherited permissions. Production initialization behavior was preserved.
4. **Concurrent documentation timing:** the forward evaluator initially encountered an absent calculator-input.md while it was being authored. The file exists in the final package and final local-link checks verify it. The evaluator correctly used transparent alternative arithmetic rather than pretending the missing reference was present.
5. **Benchmark coherence:** the forward exercise identified different implied benchmark distributions under company-specific scenario weights. The ranking reference now explicitly requires reconciliation of the common benchmark outlook and conditional state mapping before cross-company probability comparison.

## Independent offline exercise

An evaluator received the plugin and an unseen bounded request using two fictional battery companies, stale prices, a promotional universe claim, repeated-source articles, and a doubled share count. It was forbidden to browse or use additional agents. It saved a plan before analysis, disclosed sequential specialist passes, treated the universe as partial, normalized the dilution, computed available scenarios, and returned **no current qualifying investment rank**. It still identified the stronger research candidate and explained the upside tradeoff.

Independent arithmetic checks reproduced expected wealth multiples of 1.806 and 1.5, annualized expected wealth of approximately 8.81% and 5.96%, and the distinct weighted scenario CAGRs. The evaluator did not invent missing five-/ten-year forecasts, current filings or calibrated success probabilities. The primary builder inspected the artifacts and reran their arithmetic assertions successfully.

The test validates a restricted missing-data workflow, not a full live industry report or runtime delegation. The baseline without the plugin was already strong on several financial pitfalls. No causal improvement or benchmark-beating performance is claimed.

## Remaining limits

- Installation, enabled-plugin discovery and a live end-to-end multi-agent industry run have not been tested in the user's host. This is a portable source/ZIP delivery.
- Tool availability, source access, host models, concurrency and reasoning settings vary. The plugin describes truthful sequential fallback behavior.
- Evidence eligibility, scenario rationale, economic plausibility, comparable stress coverage, benchmark consistency and source freshness require analyst/auditor judgment. Software checks cannot establish them.
- Forecast calibration, real investment returns, strategy robustness and alpha have not been established. These require dated forward observations and appropriate evaluation, not longer prompts or more agents.
- This was not an exhaustive numeric fuzzing or security audit.

**Assessment:** the authored package is structurally validated and its tested calculations/workflows behave as documented. Confidence is bounded by the untested live-execution and predictive-performance scope. The most useful next check is one live industry run with source review, followed by preserving and scoring its forecasts.
