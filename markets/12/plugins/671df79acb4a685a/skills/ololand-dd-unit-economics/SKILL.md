---
name: ololand-dd-unit-economics
description: "Use when the user asks to run the OloLand ololand-dd-unit-economics\
  \ workflow. Analyze SaaS cohorts and unit economics \u2014 NDR/GRR triangles, LTV/CAC,\
  \ payback, anomalies vs. seller narrative."
---


# Workflow for ololand-dd-unit-economics

Follow the OloLand command instructions below when the user asks for `ololand-dd-unit-economics` or the equivalent workflow.

# Unit Economics Analysis

Deterministic cohort and unit-economics analysis. Not LLM prose — actual computation that flags discrepancies between what the seller claims and what the data shows.

## Usage

```
ololand-dd-unit-economics <deal_id> [transactions.csv]
```

## Arguments

- `deal_id` (required) — the OloLand deal ID.
- `transactions.csv` (optional) — customer-month revenue file with columns: `customer_id`, `period` (YYYY-MM-DD), `revenue`. If omitted, the tool will try to load transaction data extracted from the deal's financial documents.

## Execution

Load the `unit-economics` skill, then:

1. **Pull stated narrative** — call `get_financial_snapshot` and `get_deal` to find the seller's claimed NDR/GRR/CAC payback/LTV-CAC. If the deal materials state these, capture them.
2. **Load transactions** — read the CSV (or use deal-extracted transactions) and convert to the `[{customer_id, period, revenue}]` format.
3. **Estimate inputs for LTV/CAC** if available from the deal:
   - `sales_marketing_spend` (last 12 months)
   - `new_customers_in_period`
   - `gross_margin` (decimal, e.g. 0.75)
   - `new_arr_in_period` (for magic number)
   - `ebitda_margin`, `revenue_growth_yoy` (for rule of 40)
4. **Run the analysis** — `analyze_unit_economics` with all inputs including any `stated_*` claims.
5. **Surface anomalies** — anything in `result.anomalies` is a finding. High severity (>10pp NDR/GRR spread, >50% payback ratio deviation) belongs in the IC memo as a red flag.

## Output

Report:
- Computed weighted NDR / GRR with cohort count
- LTV / CAC / payback / LTV-CAC ratio
- Magic number, rule of 40
- Exponential decay half-life (logo retention curve fit) + R²
- **Anomalies table** — metric, stated, computed, severity. If empty, state "narrative reconciles."

Then suggest:
- `ololand-dd-risk-report <deal_id>` if anomalies are high severity
- `ololand-dd-valuation <deal_id> read all` to compare cohort findings with the governed model without changing it. Do not claim the cohort findings were incorporated. A fresh candidate requires a separate explicit `ololand-dd-valuation <deal_id> refresh dcf`, and only the returned model lineage can prove whether those inputs were applied.


## OpenAI execution requirements

Use the connected MCP server's current tool schemas. Do not invent tool arguments, job-status endpoints, inputs, or outputs. If a referenced tool is unavailable, explain the limitation and request the needed connection or data. Invoke writes only when the user has requested the corresponding action. Do not initiate purchases or payments. An unrun, unsupported, or unavailable procedure is a gap, never a passing result.


OpenAI cannot execute local lifecycle hooks. Use the packaged explicit setup/review workflow when requested. Server-side MCP auditing remains authoritative; preserve evidence blockers and human-only approval gates.

Claim-correction submission is unsupported in this OpenAI upload because the current handler records surface=cowork. Do not invoke submit_agent_claim_correction from OpenAI. Explain the limitation and retain proposed correction text for human review without claiming submission. See unsupported-workflows.json for the excluded canonical workflow.
