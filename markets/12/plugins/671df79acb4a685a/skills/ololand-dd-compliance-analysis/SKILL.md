---
name: ololand-dd-compliance-analysis
description: Use when the user asks to run the OloLand ololand-dd-compliance-analysis
  workflow. Run deal-scoped compliance analysis for OFAC screening, HSR threshold
  review, and CFIUS risk. Uses OloLand's context-aware compliance workbench.
---


# Workflow for ololand-dd-compliance-analysis

Follow the OloLand command instructions below when the user asks for `ololand-dd-compliance-analysis` or the equivalent workflow.

# Compliance Analysis

Run OloLand's compliance workbench for sanctions, antitrust threshold, and national-security risk checks.

## Usage

```
ololand-dd-compliance-analysis <deal_id> [ofac|hsr|cfius|all]
```

## Arguments

- `deal_id` (required) - The deal to analyze.
- `scope` (optional) - `ofac`, `hsr`, `cfius`, or `all`. Default: `all`.

## Execution

1. For `ofac` or `all`, call `run_ofac_screen(deal_id)`. Pass explicit `entities` or `sdn_entries` only if the user supplied them.
2. For `hsr` or `all`, call `run_hsr_analysis(deal_id)`. If the user supplies transaction value, buyer size, target size, or exemptions, pass those inputs through. Dollar inputs are in millions.
3. For `cfius` or `all`, call `run_cfius_risk(deal_id, ...)`. Ask for missing acquirer country, target industry, government ownership, critical technology, critical infrastructure, sensitive data, and government-contract flags when they materially affect the result.
4. Use returned `view_url` values for web app handoff.

## Output

Render:

- **OFAC** - match status, matched entities, confidence, required remediation.
- **HSR** - reportability status, thresholds crossed, exemptions, timing risk.
- **CFIUS** - risk tier, drivers, mitigation path, filing recommendation.
- **Open diligence asks** - missing identities, jurisdictions, NAICS/product categories, ownership, sensitive-data facts.

## Guardrails

- This is workflow support, not legal advice. Tell the user to involve counsel for filings, sanctions escalations, or CFIUS mitigation.
- Do not treat missing acquirer/target details as clean results. Classify missing data as a gap.

## Output URL Conventions

Use the tool-returned `view_url`. Canonical surface:

- Compliance workbench: `https://app.ololand.ai/deals/{deal_id}/analysis/compliance`


## OpenAI execution requirements

Use the connected MCP server's current tool schemas. Do not invent tool arguments, job-status endpoints, inputs, or outputs. If a referenced tool is unavailable, explain the limitation and request the needed connection or data. Invoke writes only when the user has requested the corresponding action. Do not initiate purchases or payments. An unrun, unsupported, or unavailable procedure is a gap, never a passing result.


OpenAI cannot execute local lifecycle hooks. Use the packaged explicit setup/review workflow when requested. Server-side MCP auditing remains authoritative; preserve evidence blockers and human-only approval gates.

Claim-correction submission is unsupported in this OpenAI upload because the current handler records surface=cowork. Do not invoke submit_agent_claim_correction from OpenAI. Explain the limitation and retain proposed correction text for human review without claiming submission. See unsupported-workflows.json for the excluded canonical workflow.
