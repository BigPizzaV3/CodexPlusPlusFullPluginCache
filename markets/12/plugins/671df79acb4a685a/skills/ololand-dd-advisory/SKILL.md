---
name: ololand-dd-advisory
description: Use when the user asks to run the OloLand ololand-dd-advisory workflow.
  Request or inspect buyer-side advisory engagements attached to a deal.
---


# Workflow for ololand-dd-advisory

Follow the OloLand command instructions below when the user asks for `ololand-dd-advisory` or the equivalent workflow.

# Advisory Engagement

Use this command when the user asks for an OloLand advisor, diligence support, external expert help, or the status of an advisory request.

## Usage

```
ololand-dd-advisory <deal_id> list
ololand-dd-advisory <deal_id> request buy_side_diligence
```

## Execution

1. Call `list_deal_advisory_engagements(deal_id)` first.
2. If action is `request`, confirm the requested engagement type, scope, and any fee estimate, then call `request_advisory_engagement`.
3. Render status and deliverable state from the returned engagement payload.

## Output

- Engagement id, type, status, requested time, assigned advisor summary if present.
- Scope and deliverables, if present.
- Conflict or manual-fulfillment notes when returned.
- Next step: wait for assignment, clarify scope, or review deliverable.

## Guardrails

- Do not imply instant advisor assignment or automated payment. This is a buyer-side request workflow.
- Admin queue, assignment, and fulfillment remain native OloLand operations.
- Do not bypass reviewer/advisor conflict checks.


## OpenAI execution requirements

Use the connected MCP server's current tool schemas. Do not invent tool arguments, job-status endpoints, inputs, or outputs. If a referenced tool is unavailable, explain the limitation and request the needed connection or data. Invoke writes only when the user has requested the corresponding action. Do not initiate purchases or payments. An unrun, unsupported, or unavailable procedure is a gap, never a passing result.


OpenAI cannot execute local lifecycle hooks. Use the packaged explicit setup/review workflow when requested. Server-side MCP auditing remains authoritative; preserve evidence blockers and human-only approval gates.

Claim-correction submission is unsupported in this OpenAI upload because the current handler records surface=cowork. Do not invoke submit_agent_claim_correction from OpenAI. Explain the limitation and retain proposed correction text for human review without claiming submission. See unsupported-workflows.json for the excluded canonical workflow.
