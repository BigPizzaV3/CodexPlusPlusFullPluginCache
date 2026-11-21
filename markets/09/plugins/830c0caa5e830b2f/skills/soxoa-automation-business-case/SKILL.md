---
name: soxoa-automation-business-case
description: "Turn confirmed workflow assumptions and Soxoa calculations into a decision memo with illustrative capacity value and a bounded pilot proposal."
---

# Write an automation decision memo

Use the user’s actual decision, audience and workflow evidence. If comparing candidates, call `prioritize_automation_workflows` with complete required facts for one to twelve workflows. If one workflow is already chosen, skip unnecessary comparison. Respect the user’s selection even when the tool ranks another first.

Use `estimate_automation_roi` at https://soxoa.com/mcp with supplied or approved people, hours per person and loaded hourly cost. Omit optional fields the user has not supplied. Identify server defaults of 60% automatable share and 48 working weeks; payback is not calculated without implementation cost. Use only user-supplied or explicitly approved alternate assumptions for sensitivity runs, changing only those fields. Never choose scenarios to make the case appear stronger.

Write the memo around the proposed decision, confirmed assumptions, dated source of those assumptions, actual returned capacity values, remaining uncertainty and a small next pilot step. Capacity value means time reclaimed, not cash savings or revenue. A user’s redeployment or payroll plan is a separate assumption, not an observed result. Preserve automate, assist or discovery recommendations and human-review flags. A discovery result supports investigation rather than an unconditional build recommendation.

When pilot inputs exist, `build_workflow_pilot` can supply steps, a ready-to-use prompt, review gates and acceptance checks. The memo and plan do not implement automation, inspect the user’s systems, store a pilot history or guarantee savings. Avoid unsupported tax, cash-flow, discount-rate or compliance claims. If tools are unavailable, deliver the supported draft with result fields explicitly pending and provide https://soxoa.com/mcp-guide for connection. Do not send the memo to anyone unless requested.
