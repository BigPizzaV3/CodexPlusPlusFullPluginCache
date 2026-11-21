---
name: ololand-dd-firm-calibration
description: "Use when the user asks to run the OloLand ololand-dd-firm-calibration\
  \ workflow. Read how accurate your firm's own past predictions have been \u2014\
  \ prediction accuracy, systematic biases, risk-category precision, and the fields\
  \ analysts keep overriding. Firm-wide, not deal-scoped."
---


# Workflow for ololand-dd-firm-calibration

Follow the OloLand command instructions below when the user asks for `ololand-dd-firm-calibration` or the equivalent workflow.

# Firm Calibration

Answers "how accurate have *we* been?" — the firm's own track record on predictions that have since been scored against realized outcomes. This is the institutional-memory read behind any claim that a forecast from this firm is trustworthy.

Firm-wide by construction. There is **no deal argument**: the scope always comes from your authenticated workspace, and the tool cannot be pointed at another firm's data.

## Usage

```
ololand-dd-firm-calibration [sector=<sector>]
```

## Arguments

- `sector` (optional) — restrict to one deal sector, e.g. `sector=Healthcare`. See the coverage caveat below: this filter does **not** reach every section.

## Execution

1. Call `get_firm_calibration`, passing `sector` only if the user gave one.
2. **Check `suppressed` first.** If `suppressed: true` with `suppression_reason: "ethical_wall_enforced"`, stop and report that calibration is *withheld* for this workspace because it carries an enforced ethical wall — the underlying sources aggregate company-wide and cannot be filtered to the deals you're cleared for. This is **not** "no data" and must never be reported as an un-calibrated firm.
3. **Read `coverage` and `total_with_outcomes` before quoting any accuracy figure.** `overall_accuracy` is computed only over predictions with a realized actual recorded. A firm with a handful of closed deals will produce a confident-looking percentage resting on very little.
   - If `total_with_outcomes` is small, say **"insufficient calibration history"** and report the sample size. Do not manufacture a verdict on the firm's reliability from a thin sample.
   - Always report the sample size next to the number, never the number alone.
4. Report the sections that carry data. Skip empty ones rather than printing empty tables.
5. If the user asked how a *specific deal's* projections should shift given this history, that is `ololand-dd-calibrate-vs-history` — this command gives the firm-level picture, not a per-deal adjustment.

## Reading the payload honestly

**Nulls mean "not measured", never zero.** In `category_accuracy`, only `precision` is aggregated upstream. `recall`, `true_positives`, `false_positives`, and `false_negatives` come back **null** — render them as `—`. Printing `0` would state that the firm was measured and made zero errors, which is materially false calibration evidence. The same applies to `confidence` in `correction_patterns`.

**The sector filter does not reach everything.** The payload's `sector_filter_applies_to` names the sections it reached — `prediction_stats`, `systematic_biases`, `correction_patterns`. `category_accuracy`, `deal_count`, and `coverage` stay **firm-wide** even on a sector request. If the user passed a sector, say so explicitly; never present the whole readout as one coherent sector-scoped calibration.

**Nothing here describes model retraining.** Model/retraining performance is deliberately absent — those metrics carry no per-firm dimension and would mix other firms' data in. Do not infer anything about model quality or retraining from this tool.

**`total_predictions` vs `total_with_outcomes`** — the first is every prediction recorded, the second only those with a realized actual. The gap between them is the firm's outcome-capture debt, and it is often the more actionable number: an un-calibrated firm usually has a recording problem, not a modelling problem.

## Output

Lead with the headline and its sample size, then only the populated sections:

| Prediction type | Predictions | With outcomes | Mean accuracy | Bias |
|---|---|---|---|---|
| exit_multiple | 14 | 8 | 90% | overestimate 12% |

| Risk category | Precision | Recall | TP/FP/FN |
|---|---|---|---|
| Customer Concentration | 75% | — | — |

| Field analysts override | Corrections | Avg shift | Sectors |
|---|---|---|---|
| risk.severity | 7 | -1.25 | Healthcare |

Close with one line on what the firm should do about it — e.g. "the firm's exit-multiple forecasts run 12% high on an 8-deal sample; discount new exit assumptions accordingly, and note 6 of 14 predictions still have no recorded outcome."

## Cost

A metered read (1 credit), on the same footing as the other institutional-memory reads. Not available on the free post-trial allowlist — if a call returns `tier_gated: true`, surface the upgrade CTA from the response rather than pre-refusing.

## Why this matters

Every AI tool will produce a forecast. Almost none can tell you whether *your firm's* forecasts have historically been right, or in which direction they've been wrong. That answer lives only in your own recorded outcomes — which is why the calibration and the outcome-capture debt are reported together.

## Related commands

- `ololand-dd-calibrate-vs-history` — applies historical bias to **one deal's** projections (deal-scoped counterpart to this command)
- `ololand-dd-record-outcome` — records realized actuals; this is what makes calibration possible at all
- `ololand-dd-playbook-recall` — what worked, didn't, or was missed on similar past deals


## OpenAI execution requirements

Use the connected MCP server's current tool schemas. Do not invent tool arguments, job-status endpoints, inputs, or outputs. If a referenced tool is unavailable, explain the limitation and request the needed connection or data. Invoke writes only when the user has requested the corresponding action. Do not initiate purchases or payments. An unrun, unsupported, or unavailable procedure is a gap, never a passing result.


OpenAI cannot execute local lifecycle hooks. Use the packaged explicit setup/review workflow when requested. Server-side MCP auditing remains authoritative; preserve evidence blockers and human-only approval gates.

Claim-correction submission is unsupported in this OpenAI upload because the current handler records surface=cowork. Do not invoke submit_agent_claim_correction from OpenAI. Explain the limitation and retain proposed correction text for human review without claiming submission. See unsupported-workflows.json for the excluded canonical workflow.
