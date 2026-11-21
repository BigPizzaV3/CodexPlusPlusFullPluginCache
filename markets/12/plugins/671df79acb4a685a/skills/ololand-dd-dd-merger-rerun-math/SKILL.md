---
name: ololand-dd-dd-merger-rerun-math
description: Use when the user asks to run the OloLand ololand-dd-dd-merger-rerun-math
  workflow. Re-run one or all four merger engines on an existing merger-analysis deal
  with optional input overrides. Useful for sensitivity analysis (e.g., halved synergies).
---


# Workflow for ololand-dd-dd-merger-rerun-math

Follow the OloLand command instructions below when the user asks for `ololand-dd-dd-merger-rerun-math` or the equivalent workflow.

# ololand-dd-dd-merger-rerun-math

Re-run a deterministic merger engine on a third-party merger-analysis deal. Each engine returns `INSUFFICIENT_DATA` when required inputs are missing — never silently impute.

## Required inputs

- **deal_id** — the merger-analysis deal ID (starts with `merger_`). Ask if missing.

Optional:
- **engine** — one of `premium`, `accretion`, `dcf`, `hhi`. When omitted, run all four.
- **overrides** — JSON object of per-input pins. See "Engine-specific overrides" below.

## Action

Pick the matching MCP tool(s):

- `premium` → `run_premium_analysis(deal_id, overrides=...)`
- `accretion` → `run_accretion_dilution(deal_id, overrides=...)`
- `dcf` → `run_combined_dcf(deal_id, synergies=..., integration_costs=..., wacc=..., terminal_growth=...)`
- `hhi` → `run_antitrust_hhi(deal_id, market_definition=..., rivals=..., target_share_pct=..., acquirer_share_pct=...)`

For each run, report:
- `run_id` (for replay / lineage)
- `status` (`completed` / `insufficient_data` / `error`)
- Key outputs (numeric headlines)
- Any `assumptions` payload (with confidence labels)

If `status == "insufficient_data"`, name the missing fields and where they typically come from. Suggest uploads or `ololand-dd-dd-merger-readiness` to confirm coverage.

## Engine-specific overrides

- **premium**: `target_unaffected_price`, `offer_price_per_share`, `target_52wk_high`, `target_30d_vwap`, `sector`, `size_class`.
- **accretion**: `acquirer_eps_forward`, `target_eps_forward`, `acquirer_shares_million`, `target_shares_million`, `after_tax_synergy_runrate_million`, `synergy_phasing_pct`, `tax_rate`.
- **dcf**: `synergies` (`{revenue_runrate, cost_runrate, phasing_pct}`), `integration_costs` (`{one_time_million}`), `wacc`, `terminal_growth`. Synergies MUST be attested as incremental to standalone forecasts per the merger-mechanics skill.
- **hhi**: `market_definition` (`{industry, geography, product_segment}`) MUST be stated explicitly. `rivals` is `[{name, share_pct}, ...]`.

## Subscription

The four engine tools run on Developer as part of the bounded single-deal trial, metered against the monthly credit budget — no longer Pro-gated. If a call returns `tier_gated: true`, surface the upgrade CTA from the response.


## OpenAI execution requirements

Use the connected MCP server's current tool schemas. Do not invent tool arguments, job-status endpoints, inputs, or outputs. If a referenced tool is unavailable, explain the limitation and request the needed connection or data. Invoke writes only when the user has requested the corresponding action. Do not initiate purchases or payments. An unrun, unsupported, or unavailable procedure is a gap, never a passing result.


OpenAI cannot execute local lifecycle hooks. Use the packaged explicit setup/review workflow when requested. Server-side MCP auditing remains authoritative; preserve evidence blockers and human-only approval gates.

Claim-correction submission is unsupported in this OpenAI upload because the current handler records surface=cowork. Do not invoke submit_agent_claim_correction from OpenAI. Explain the limitation and retain proposed correction text for human review without claiming submission. See unsupported-workflows.json for the excluded canonical workflow.
