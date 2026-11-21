---
name: ololand-dd-qoe-analysis
description: "Use when the user asks to run the OloLand ololand-dd-qoe-analysis workflow.\
  \ Run or retrieve OloLand's deal-scoped Quality of Earnings analytical workbench\
  \ for revenue quality, EBITDA adjustments, working capital, and evidence-backed\
  \ QoE findings \u2014 plus an optional cross-document conflict scan that surfaces\
  \ contradictions across the data room."
---


# Workflow for ololand-dd-qoe-analysis

Follow the OloLand command instructions below when the user asks for `ololand-dd-qoe-analysis` or the equivalent workflow.

# QoE Analysis

Run the deal-scoped Quality of Earnings workbench. The backend auto-hydrates from the latest financial snapshot when explicit data is not provided, while still accepting overrides for replay or power-user workflows.

## Usage

```
ololand-dd-qoe-analysis <deal_id> [latest|run]
```

## Arguments

- `deal_id` (required) - The deal to analyze.
- `mode` (optional) - `latest` to inspect the cached result; `run` to create a fresh analysis. Default: `latest`, then run if no result exists.

## Execution

1. Call `get_latest_qoe_analysis(deal_id)`.
2. If there is no cached result, or the user asks to rerun, call `run_qoe_analysis(deal_id)`.
3. If the user supplied structured overrides, pass them through to `run_qoe_analysis`: `revenue_items`, `expense_items`, `financial_data`, `transactions`, `adjustments`, `reported_ebitda`, `revenue_data`, and `working_capital_data`.
4. Use the returned `view_url` for the web app handoff.

## Cross-document conflict scan (optional)

QoE findings are only as good as the documents agree with each other. When the user asks to "find contradictions", "check the documents against each other", or is prepping a data-room quality read, run the cross-document conflict detector:

1. Call `run_conflict_detection(deal_id)`. This dispatches the Deal Document Conflict Detector over the cross-doc reconciliation engines, surfacing conflicts across financials, dates, entities, and terms. It returns a `task_id` and dual-writes a replayable `agent_runs` row plus a `conflict_report` artifact.
2. Poll `check_task_status(task_id)` until complete (it runs async).
3. Fold the returned conflicts into the QoE read as evidence gaps or blockers — a management figure that contradicts the CPA financials is a QoE concern, not a footnote. Cite the two conflicting documents for each finding.

This is the all-in-one equivalent of the standalone `ololand-forensic-qoe` plugin's `/conflicts` command.

## Output

Render:

- **QoE verdict** - clean / watch / concern / blocker, based on the returned risk and adjustment profile.
- **EBITDA bridge** - returned base, computed adjustment totals, classes, dollar impacts, and evidence limitations; do not infer accepted normalized earnings from a computed total.
- **Revenue quality** - concentration, cut-off, recurring/non-recurring indicators, and any source gaps.
- **Working capital** - DSO/DPO/DIO and normalization flags.
- **Evidence gaps** - data classes that prevented stronger conclusions.

For a separate `build_ebitda_bridge` invocation on OpenAI, confirm the current
live schema and require explicit `financial_data` with finite numerical
`reported_ebitda` and an explicit `adjustments` list alongside `deal_id`.
Do not transfer this workbench's native snapshot fallback to that tool. Its
OpenAI result is a caller-supplied unverified scenario with `base_ebitda`,
`basis_is_canonical=false`, and `evidence_verification=not_performed`;
source/documentation labels and `source_claim` fields are not verified
citations. Heuristic classifications do not approve adjustments or establish
accepted normalized earnings. Missing evidence remains a blocker for a full
source-backed normalized review.

## Output URL Conventions

Use the tool-returned `view_url`. Canonical surface:

- QoE workbench: `https://app.ololand.ai/deals/{deal_id}/valuation/qoe`


## OpenAI execution requirements

Use the connected MCP server's current tool schemas. Do not invent tool arguments, job-status endpoints, inputs, or outputs. If a referenced tool is unavailable, explain the limitation and request the needed connection or data. Invoke writes only when the user has requested the corresponding action. Do not initiate purchases or payments. An unrun, unsupported, or unavailable procedure is a gap, never a passing result.


OpenAI cannot execute local lifecycle hooks. Use the packaged explicit setup/review workflow when requested. Server-side MCP auditing remains authoritative; preserve evidence blockers and human-only approval gates.

Claim-correction submission is unsupported in this OpenAI upload because the current handler records surface=cowork. Do not invoke submit_agent_claim_correction from OpenAI. Explain the limitation and retain proposed correction text for human review without claiming submission. See unsupported-workflows.json for the excluded canonical workflow.
