---
name: ololand-dd-value-impact
description: Use when the user asks to run the OloLand ololand-dd-value-impact workflow.
  Review or preview OloLand's value-impact ledger for a deal or firm. Shows hours
  saved, labor/advisor cost avoided, platform cost completeness, and methodology snapshots.
---


# Workflow for ololand-dd-value-impact

Follow the OloLand command instructions below when the user asks for `ololand-dd-value-impact` or the equivalent workflow.

# Value Impact

Use this command when the user asks for ROI, hours saved, avoided QoE/advisor cost, value multiple, or the evidence behind OloLand's value-impact claims.

## Usage

```
ololand-dd-value-impact <deal_id>
ololand-dd-value-impact company [start=YYYY-MM-DD] [end=YYYY-MM-DD] [workflow=<workflow_key>]
ololand-dd-value-impact preview workflows=pre_loi_screen,full_qoe deals=12 cost=238800
```

## Execution

1. If the first argument is a deal id, call `get_deal_value_impact(deal_id)`.
2. If the first argument is `company` or the user asks for firm-wide ROI, call `get_company_value_impact` with any date/workflow filters.
3. If the user asks "what would this be worth if..." call `preview_value_impact` with `workflows`, `workflow_counts`, `deals_per_year`, and optional `annual_platform_cost_cents`.
4. If the user asks what assumptions drive the ledger, call `get_value_impact_assumptions`.
5. Only call `update_value_impact_assumptions` when the user explicitly asks to change company ROI assumptions and confirms the values. That tool is company-admin gated.

## Output

Render:

- **Value summary**: hours saved, labor cost avoided, advisor cost avoided, gross value, net value if platform cost is complete.
- **Cost completeness**: `ololand_cost_is_complete`, missing-cost count, and whether `value_multiple` is known or intentionally withheld.
- **Top events**: workflow, source, completed time, confidence, and methodology note.
- **Assumptions**: hourly rates, display mode, external QoE baseline when relevant.
- **Next action**: open the returned `view_url`, adjust assumptions, or run the workflow that would create missing events.

## Guardrails

- Never convert unknown OloLand cost to zero. If `net_value_cents` or `value_multiple` is null because cost is incomplete, say that directly.
- Treat the ledger as substantiated estimate, not a guarantee of actual savings.
- Preserve confidence and methodology notes when presenting dollar figures.


## OpenAI execution requirements

Use the connected MCP server's current tool schemas. Do not invent tool arguments, job-status endpoints, inputs, or outputs. If a referenced tool is unavailable, explain the limitation and request the needed connection or data. Invoke writes only when the user has requested the corresponding action. Do not initiate purchases or payments. An unrun, unsupported, or unavailable procedure is a gap, never a passing result.


OpenAI cannot execute local lifecycle hooks. Use the packaged explicit setup/review workflow when requested. Server-side MCP auditing remains authoritative; preserve evidence blockers and human-only approval gates.

Claim-correction submission is unsupported in this OpenAI upload because the current handler records surface=cowork. Do not invoke submit_agent_claim_correction from OpenAI. Explain the limitation and retain proposed correction text for human review without claiming submission. See unsupported-workflows.json for the excluded canonical workflow.
