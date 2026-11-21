---
name: ololand-dd-managed-context-agent
description: Use when the user asks to run the OloLand ololand-dd-managed-context-agent
  workflow. Launch a feature-flagged OloLand's hosted agent service managed context
  agent for a deal when OloLand has enabled the managed executor.
---


# Workflow for ololand-dd-managed-context-agent

Follow the OloLand command instructions below when the user asks for `ololand-dd-managed-context-agent` or the equivalent workflow.

# Managed Context Agent

Use this command only when the user explicitly asks to run an OloLand managed context agent or names a registered context-agent key.

## Usage

```
ololand-dd-managed-context-agent <deal_id> <agent_key> [prompt]
```

Common agent keys depend on the deployment registry. Do not invent them. If the user does not know the key, ask them to choose from the deployment's registered context agents or use `ololand-dd-talk-to-deal` instead.

## Execution

1. Confirm the deal id and exact `agent_key`.
2. Call `launch_managed_context_agent(deal_id, agent_key, prompt)`.
3. If queued, poll the returned `task_id` with `check_task_status`.
4. If the tool returns `managed_executor_unavailable` or `agent_not_found`, explain that the deployment is not configured for that managed agent and fall back to `ololand-dd-talk-to-deal` or the standard DD tools.

## Guardrails

- The managed-agent substrate is feature-flagged and environment-specific. Do not promise availability.
- Do not route production deal data into staging-configured agents. If the backend rejects the dispatch, fail closed.
- Use this for explicit managed-agent launches, not as the default path for ordinary deal Q&A.


## OpenAI execution requirements

Use the connected MCP server's current tool schemas. Do not invent tool arguments, job-status endpoints, inputs, or outputs. If a referenced tool is unavailable, explain the limitation and request the needed connection or data. Invoke writes only when the user has requested the corresponding action. Do not initiate purchases or payments. An unrun, unsupported, or unavailable procedure is a gap, never a passing result.


OpenAI cannot execute local lifecycle hooks. Use the packaged explicit setup/review workflow when requested. Server-side MCP auditing remains authoritative; preserve evidence blockers and human-only approval gates.

Claim-correction submission is unsupported in this OpenAI upload because the current handler records surface=cowork. Do not invoke submit_agent_claim_correction from OpenAI. Explain the limitation and retain proposed correction text for human review without claiming submission. See unsupported-workflows.json for the excluded canonical workflow.
