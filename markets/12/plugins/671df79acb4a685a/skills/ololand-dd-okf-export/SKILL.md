---
name: ololand-dd-okf-export
description: Use when the user asks to run the OloLand ololand-dd-okf-export workflow.
  Export an OloLand deal dossier as an OKF bundle for downstream system handoff.
---


# Workflow for ololand-dd-okf-export

Follow the OloLand command instructions below when the user asks for `ololand-dd-okf-export` or the equivalent workflow.

# OKF Export

Use this command when the user asks for an OKF bundle, portable deal dossier, or machine-readable export of a deal's OloLand record.

## Usage

```
ololand-dd-okf-export <deal_id>
```

## Execution

1. Confirm the deal id.
2. Call `export_deal_okf_bundle(deal_id)`.
3. If the response includes artifact or download metadata, render it exactly and preserve provenance fields.
4. If the user wants a regulator/compliance package instead, route to `ololand-dd-regulator-export`; OKF is a deal-record handoff, not the compliance-framework export.

## Output

- Bundle id/path or artifact id.
- Included sections/data classes.
- Any warnings about missing deal data.
- Returned URL or retrieval instructions.

## Guardrails

- Do not describe OKF as a signed IC artifact.
- Do not strip provenance, source ids, or methodology fields from the exported bundle summary.


## OpenAI execution requirements

Use the connected MCP server's current tool schemas. Do not invent tool arguments, job-status endpoints, inputs, or outputs. If a referenced tool is unavailable, explain the limitation and request the needed connection or data. Invoke writes only when the user has requested the corresponding action. Do not initiate purchases or payments. An unrun, unsupported, or unavailable procedure is a gap, never a passing result.


OpenAI cannot execute local lifecycle hooks. Use the packaged explicit setup/review workflow when requested. Server-side MCP auditing remains authoritative; preserve evidence blockers and human-only approval gates.

Claim-correction submission is unsupported in this OpenAI upload because the current handler records surface=cowork. Do not invoke submit_agent_claim_correction from OpenAI. Explain the limitation and retain proposed correction text for human review without claiming submission. See unsupported-workflows.json for the excluded canonical workflow.
