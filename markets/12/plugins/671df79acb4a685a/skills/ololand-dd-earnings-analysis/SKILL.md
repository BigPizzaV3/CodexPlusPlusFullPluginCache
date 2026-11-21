---
name: ololand-dd-earnings-analysis
description: Use when the user asks to run the OloLand ololand-dd-earnings-analysis
  workflow. Analyze an earnings-call transcript for management tone, topic risk, guidance
  deltas, and deal-relevant diligence signals.
---


# Workflow for ololand-dd-earnings-analysis

Follow the OloLand command instructions below when the user asks for `ololand-dd-earnings-analysis` or the equivalent workflow.

# Earnings Analysis

Run the deal-scoped earnings-call workbench. Use this for public-company targets, public comps, or any target with management-call transcripts that should feed diligence.

## Usage

```
ololand-dd-earnings-analysis <deal_id> <transcript_or_segments>
```

## Arguments

- `deal_id` (required) - The deal to analyze.
- `segments` (required) - Transcript segments. Accept a pasted transcript, a local file path, or structured segment objects.
- `company_name` (optional) - Company name to display in the analysis.
- `call_date` (optional) - Call date.

## Execution

1. If the user provides a file path, read the transcript and split it into speaker-aware segments when possible.
2. Call `analyze_earnings_call(deal_id, segments, company_name, call_date)`.
3. Use the returned `view_url` for web app handoff.

## Output

Render:

- **Management tone** - sentiment, vocal/tone stress where available, and notable topic shifts.
- **Guidance deltas** - changed revenue, EBITDA, margin, cash-flow, or capex expectations.
- **Risk signals** - evasive answers, customer concentration, pricing pressure, churn, regulatory, liquidity, covenant, or working-capital flags.
- **Follow-up asks** - documents or management questions that should enter the diligence request list.

## Guardrails

- Do not overstate vocal stress as deception. Treat it as a diligence signal that needs corroborating evidence.
- Preserve citations or transcript timestamps for any quote or numerical claim.

## Output URL Conventions

Use the tool-returned `view_url`. Canonical surface:

- Earnings analysis: `https://app.ololand.ai/deals/{deal_id}/analysis/earnings`


## OpenAI execution requirements

Use the connected MCP server's current tool schemas. Do not invent tool arguments, job-status endpoints, inputs, or outputs. If a referenced tool is unavailable, explain the limitation and request the needed connection or data. Invoke writes only when the user has requested the corresponding action. Do not initiate purchases or payments. An unrun, unsupported, or unavailable procedure is a gap, never a passing result.


OpenAI cannot execute local lifecycle hooks. Use the packaged explicit setup/review workflow when requested. Server-side MCP auditing remains authoritative; preserve evidence blockers and human-only approval gates.

Claim-correction submission is unsupported in this OpenAI upload because the current handler records surface=cowork. Do not invoke submit_agent_claim_correction from OpenAI. Explain the limitation and retain proposed correction text for human review without claiming submission. See unsupported-workflows.json for the excluded canonical workflow.
