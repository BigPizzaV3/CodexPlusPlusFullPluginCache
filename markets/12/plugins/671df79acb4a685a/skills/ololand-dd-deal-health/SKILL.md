---
name: ololand-dd-deal-health
description: Use when the user asks to run the OloLand ololand-dd-deal-health workflow.
  Summarize deal health, open actions, and meeting-prep blockers from OloLand's deal-health
  surface.
---


# Workflow for ololand-dd-deal-health

Follow the OloLand command instructions below when the user asks for `ololand-dd-deal-health` or the equivalent workflow.

# Deal Health

Use this command when the user asks "what is the state of this deal?", "what is blocking us?", "prep me for the Monday meeting", or asks to add/list critical actions.

## Usage

```
ololand-dd-deal-health <deal_id>
ololand-dd-deal-health <deal_id> actions [open|in_progress|blocked|done]
ololand-dd-deal-health <deal_id> create-action "Pull AR aging from seller" priority=high
```

## Execution

1. Call `get_deal_health_summary(deal_id)` first.
2. If the user asks for actions or blockers, call `list_deal_actions` with optional `status` or `priority`.
3. If the user asks to add an action, confirm the title and priority, then call `create_deal_action`.
4. If the answer needs supporting evidence, pair this with `search_deal_documents` or `search_extracted_knowledge` and cite the result.

## Output

Render:

- **Overall status**: score, status, and recommendation.
- **Dimensions**: financial, risk, operational scores and the reason each is high/low.
- **Open actions**: count and top five action items.
- **Risk count**: high/medium/low risks from the health payload.
- **Next action**: what should happen before the next IC/workstream review.

## Guardrails

- Do not treat a health score as IC approval. Pair IC readiness with `ololand-dd-ic-approve-readiness`.
- When creating actions, keep titles concrete and owner-ready.
- Use tool-returned `view_url` values instead of hand-building app links.


## OpenAI execution requirements

Use the connected MCP server's current tool schemas. Do not invent tool arguments, job-status endpoints, inputs, or outputs. If a referenced tool is unavailable, explain the limitation and request the needed connection or data. Invoke writes only when the user has requested the corresponding action. Do not initiate purchases or payments. An unrun, unsupported, or unavailable procedure is a gap, never a passing result.


OpenAI cannot execute local lifecycle hooks. Use the packaged explicit setup/review workflow when requested. Server-side MCP auditing remains authoritative; preserve evidence blockers and human-only approval gates.

Claim-correction submission is unsupported in this OpenAI upload because the current handler records surface=cowork. Do not invoke submit_agent_claim_correction from OpenAI. Explain the limitation and retain proposed correction text for human review without claiming submission. See unsupported-workflows.json for the excluded canonical workflow.
