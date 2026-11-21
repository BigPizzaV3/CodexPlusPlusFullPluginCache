---
name: ololand-dd-firm-playbook-recall
description: "Use when the user asks about WACC ranges, IRR targets, max EV/Revenue\
  \ or EV/EBITDA multiples, approval thresholds, preferred frameworks, or custom rules\
  \ for an OloLand deal. Reads the firm's standing playbook via `recall_firm_playbook`\
  \ \u2014 institutional preferences that are more authoritative than market-default\
  \ heuristics."
---

# Firm playbook recall

For deals on OloLand, the **firm's standing playbook** encodes the institution's codified preferences: WACC range, target IRR, min MOIC, EV-multiple ceilings, approval thresholds, standard timelines, preferred frameworks, and custom rules (e.g. "flag top-customer concentration > 30%"). When answering deal questions that produce a number under the firm's name, **honor the playbook OR explicitly call out the deviation**.

## When to call

Call `recall_firm_playbook(deal_id)` at the start of any substantive turn that will:

- Quote a WACC, terminal growth rate, exit multiple, target IRR, or MOIC
- Compare a deal to a target/criteria threshold (revenue size, growth rate, EBITDA margin)
- Recommend an approval routing (partner / IC / board)
- Apply a custom rule (concentration, leverage, segment exposure)

Skip the call for trivial Q&A (greetings, identity, single-fact lookups) where no number is being committed.

## Distinct from playbook-recall

| Tool | Scope | Returns |
|---|---|---|
| `recall_firm_playbook` | THIS firm's standing config | WACC ranges, IRR targets, approval thresholds, rules |
| `find_similar_deals` (via `ololand-dd-playbook-recall`) | Patterns from past similar deals | What worked / what didn't / what got missed |

Both can be load-bearing — the first sets the constraint, the second informs how to apply it.

## Deviation discipline

When a playbook value constrains a number you're about to commit to:

1. **In range** — proceed; cite the playbook value as the basis.
2. **Out of range, justified** — quote the playbook value, explain why the deviation is warranted, recommend partner sign-off via `ololand-dd-partner-signoff` if the artifact is IC-bound.
3. **Out of range, unjustified** — adjust the number to fit the playbook range OR refuse to commit and ask the user to confirm the deviation.

Silent substitution of OloLand defaults when a playbook is configured is a discipline failure — the analyst loses the audit trail and the firm loses the confidence signal.

## Empty playbook

If the response is `playbook: null`, the tenant has no active playbook configured. Fall back to OloLand market-default methodology without commentary, AND surface a one-line note in the answer: "Note: no firm playbook configured — using OloLand defaults."


## OpenAI execution requirements

Use the connected MCP server's current tool schemas. Do not invent tool arguments, job-status endpoints, inputs, or outputs. If a referenced tool is unavailable, explain the limitation and request the needed connection or data. Invoke writes only when the user has requested the corresponding action. Do not initiate purchases or payments. An unrun, unsupported, or unavailable procedure is a gap, never a passing result.


OpenAI cannot execute local lifecycle hooks. Use the packaged explicit setup/review workflow when requested. Server-side MCP auditing remains authoritative; preserve evidence blockers and human-only approval gates.

Claim-correction submission is unsupported in this OpenAI upload because the current handler records surface=cowork. Do not invoke submit_agent_claim_correction from OpenAI. Explain the limitation and retain proposed correction text for human review without claiming submission. See unsupported-workflows.json for the excluded canonical workflow.
