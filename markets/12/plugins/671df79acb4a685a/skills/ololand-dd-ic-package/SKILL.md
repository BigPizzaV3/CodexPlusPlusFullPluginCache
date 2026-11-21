---
name: ololand-dd-ic-package
description: Use when the user asks to run the OloLand ololand-dd-ic-package workflow.
  Generate or approve the canonical OloLand IC package, while preserving assumption-control
  and verifier-gate blockers.
---


# Workflow for ololand-dd-ic-package

Follow the OloLand command instructions below when the user asks for `ololand-dd-ic-package` or the equivalent workflow.

# IC Package

Use this command when the user asks to generate the canonical 8-section IC package, inspect package state, or approve a package after readiness checks.

## Usage

```
ololand-dd-ic-package <deal_id> status
ololand-dd-ic-package <deal_id> generate
ololand-dd-ic-package <deal_id> approve
```

## Execution

1. Always call `get_ic_package(deal_id)` first.
2. Before approval, run `ololand-dd-ic-approve-readiness` or directly call:
   - `get_assumption_control_summary`
   - `get_assumption_evidence_pack`
3. `generate` — assemble the best available structured `deal_data` from deal, financial snapshot, valuation, risks, verification status, and assumptions. Then call `generate_ic_package`.
4. Poll the returned `task_id` using `check_task_status`.
5. `approve` — only after the user explicitly says to approve, direct them to the in-app human-session IC package approval surface. Do **not** call `approve_ic_package` through MCP; the MCP rail is fail-closed for human approvals.
6. If the in-app approval surface reports `readiness_blocked`, `verifier_blocked`, or `bad_request`, surface the blocker verbatim and recommend the smallest remediation step.

## Output

Render:

- **Package state**: id, version, status, selected sections, approved time.
- **Generation**: task id, status, and polling result.
- **Approval**: approved or blocked, with blocker tier and exact backend message.
- **Evidence snapshot**: unsupported/weak/partial assumption counts when available.
- **URL**: use returned `view_url`.

## Guardrails

- Approval is a controlled workflow, not a drafting shortcut. Approval is app/human-session only; never invoke `approve_ic_package` through MCP, even with explicit user instruction.
- Do not set `override_verifier_block=true` unless the user explicitly gives an override reason. Preserve the reason.
- If assumptions are unresolved or evidence is missing, do not summarize as "ready".


## OpenAI execution requirements

Use the connected MCP server's current tool schemas. Do not invent tool arguments, job-status endpoints, inputs, or outputs. If a referenced tool is unavailable, explain the limitation and request the needed connection or data. Invoke writes only when the user has requested the corresponding action. Do not initiate purchases or payments. An unrun, unsupported, or unavailable procedure is a gap, never a passing result.


OpenAI cannot execute local lifecycle hooks. Use the packaged explicit setup/review workflow when requested. Server-side MCP auditing remains authoritative; preserve evidence blockers and human-only approval gates.

Claim-correction submission is unsupported in this OpenAI upload because the current handler records surface=cowork. Do not invoke submit_agent_claim_correction from OpenAI. Explain the limitation and retain proposed correction text for human review without claiming submission. See unsupported-workflows.json for the excluded canonical workflow.
