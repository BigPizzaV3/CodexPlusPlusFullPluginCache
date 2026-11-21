---
name: ololand-dd-scenario-analysis
description: Use when the user asks to run the OloLand ololand-dd-scenario-analysis
  workflow. Run scenario stress tests, market-condition simulations, and real-options
  valuation from OloLand's deal-scoped scenario workbench.
---


# Workflow for ololand-dd-scenario-analysis

Follow the OloLand command instructions below when the user asks for `ololand-dd-scenario-analysis` or the equivalent workflow.

# Scenario Analysis

Use OloLand's deterministic scenario workbench to stress the underwriting case and value strategic flexibility.

## Usage

```
ololand-dd-scenario-analysis <deal_id> [stress|market|real-options|all]
```

## Arguments

- `deal_id` (required) - The deal to analyze.
- `mode` (optional) - `stress`, `market`, `real-options`, or `all`. Default: `stress`.

## Execution

1. For `stress` or `all`, call `run_scenario_stress_test(deal_id)`. Default scenario types are recession, rate spike, and sector downturn unless the user provides a list. Pass `severity` and `base_params` if supplied.
2. For `market` or `all`, call `simulate_market_conditions`. Required inputs are `current_rate`, `mean_rate`, and `volatility`; ask for them if missing. Use `years`, `n_scenarios`, and `seed` only when supplied or clearly requested.
3. For `real-options` or `all`, call `value_real_options(deal_id, options)`. Ask the user for the options list if it is missing; do not invent expansion, abandonment, or deferral options without labeling them as illustrative.
4. Use returned `view_url` values for web app handoff.

## Output

Render:

- **Stress-test results** - base case vs downside cases, EBITDA/covenant/IRR impact, breakpoints.
- **Market simulation** - distribution, P10/P50/P90 outputs, and most sensitive inputs.
- **Real options** - option type, value, assumptions, exercise trigger, and strategic implication.
- **Decision implication** - bid adjustment, covenant ask, data-room ask, or no-action conclusion.

## Output URL Conventions

Use the tool-returned `view_url`. Canonical surfaces:

- Scenario workbench: `https://app.ololand.ai/deals/{deal_id}/valuation/scenarios`
- Real options: `https://app.ololand.ai/deals/{deal_id}/valuation/real-options`


## OpenAI execution requirements

Use the connected MCP server's current tool schemas. Do not invent tool arguments, job-status endpoints, inputs, or outputs. If a referenced tool is unavailable, explain the limitation and request the needed connection or data. Invoke writes only when the user has requested the corresponding action. Do not initiate purchases or payments. An unrun, unsupported, or unavailable procedure is a gap, never a passing result.


OpenAI cannot execute local lifecycle hooks. Use the packaged explicit setup/review workflow when requested. Server-side MCP auditing remains authoritative; preserve evidence blockers and human-only approval gates.

Claim-correction submission is unsupported in this OpenAI upload because the current handler records surface=cowork. Do not invoke submit_agent_claim_correction from OpenAI. Explain the limitation and retain proposed correction text for human review without claiming submission. See unsupported-workflows.json for the excluded canonical workflow.
