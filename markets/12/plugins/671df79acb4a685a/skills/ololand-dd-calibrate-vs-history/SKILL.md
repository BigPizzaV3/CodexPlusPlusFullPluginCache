---
name: ololand-dd-calibrate-vs-history
description: Use when the user asks to run the OloLand ololand-dd-calibrate-vs-history
  workflow. Apply your firm's historical projection accuracy to recalibrate the current
  deal's revenue, EBITDA, and risk projections. Surfaces systematic biases (e.g. "your
  firm consistently overestimates revenue growth by 15% in deals like this").
---


# Workflow for ololand-dd-calibrate-vs-history

Follow the OloLand command instructions below when the user asks for `ololand-dd-calibrate-vs-history` or the equivalent workflow.

# Calibrate vs. History

Uses cross-deal outcome data to adjust the current deal's headline projections by the historical bias your firm has shown in similar deals. The output is a calibrated projection: management's $X.XM EBITDA, with the historical-bias-corrected $Y.YM EBITDA shown alongside.

## Usage

```
ololand-dd-calibrate-vs-history <deal_id>
```

## Arguments

- `deal_id` (required) — The current deal to calibrate. Requires similar deals to have outcome data on file (i.e. closed and observed for at least 12 months post-close).

## Execution

1. Call `find_similar_deals` from the MCP server with the `deal_id`.
2. **If the response is `status: "no_usable_corpus"`** — stop here. Tell the user the firm does not yet have a usable cohort of closed-and-observed similar deals to calibrate against. Do NOT calibrate against a forced cohort.
3. Filter to similar deals with outcome data: deals that have entries in the outcome-tracking system showing realized vs. underwritten metrics.
4. For each metric where outcome data exists (revenue growth, EBITDA margin, leverage trajectory, risk realization rates), compute:
   - **Bias** — mean of (realized − underwritten) across similar deals
   - **Variance** — standard deviation of the bias
   - **Confidence** — sample size and recency
   > For the firm's **authoritative** measured bias — computed by the backend over every scored prediction, not derived from this cohort — call `get_firm_calibration` (`ololand-dd-firm-calibration`). Use it to sanity-check the cohort bias computed here; a large divergence usually means the cohort is too small to trust.
5. Apply the bias to the current deal's projection. Return both the management projection and the calibrated projection side-by-side, with the bias explanation.

## Output

| Metric | Management | Historical bias | Calibrated | Confidence |
|---|---|---|---|---|
| FY27 revenue growth | 22% | -7pp avg (n=6, σ=4pp) | 15% | medium |
| FY27 EBITDA margin | 24% | -2pp avg (n=6) | 22% | medium |
| Customer concentration risk realizing | 8% | flagged 5/6, realized 3/6 | 50% | high |

Plus a calibrated EBITDA dollar impact and an implied multiple correction.

## Why this matters

The hardest question to answer with general-purpose AI: "are *we* systematically too optimistic about deals like this?" That's a question only your firm's prior outcome data can answer. Calibrate-vs-history surfaces the bias and applies it to the live projection. It doesn't replace IC judgment — it gives IC the data to argue *with*.

## Example

```
ololand-dd-calibrate-vs-history deal_acme_2026
```

Returns: "Your firm has overestimated revenue growth in similar industrial-services deals by an average of 7pp (n=6 deals 2022-2024, σ=4pp). Management projects 22% FY27 growth; calibrated projection is 15%. Implied EBITDA at exit drops from $42M to $34M, implied 5x exit multiple changes from $210M EV to $170M EV — bid should reflect this."

## Related commands

- `ololand-dd-firm-calibration` — the firm-wide counterpart: how accurate this firm's predictions have been overall, measured by the backend rather than derived per-cohort here. Use it when the question is "are we systematically optimistic?" rather than "how should THIS deal move".
- `ololand-dd-similar-deals` — raw similarity output
- `ololand-dd-playbook-recall` — what worked / didn't / was missed in similar past deals


## OpenAI execution requirements

Use the connected MCP server's current tool schemas. Do not invent tool arguments, job-status endpoints, inputs, or outputs. If a referenced tool is unavailable, explain the limitation and request the needed connection or data. Invoke writes only when the user has requested the corresponding action. Do not initiate purchases or payments. An unrun, unsupported, or unavailable procedure is a gap, never a passing result.


OpenAI cannot execute local lifecycle hooks. Use the packaged explicit setup/review workflow when requested. Server-side MCP auditing remains authoritative; preserve evidence blockers and human-only approval gates.

Claim-correction submission is unsupported in this OpenAI upload because the current handler records surface=cowork. Do not invoke submit_agent_claim_correction from OpenAI. Explain the limitation and retain proposed correction text for human review without claiming submission. See unsupported-workflows.json for the excluded canonical workflow.
