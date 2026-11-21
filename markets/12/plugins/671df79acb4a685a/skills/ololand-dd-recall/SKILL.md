---
name: ololand-dd-recall
description: "Use when the user asks to run the OloLand ololand-dd-recall workflow.\
  \ Read confirmed facts about an OloLand deal from deal_session_memory. Use at the\
  \ start of any session about a deal to load the analyst-confirmed context \u2014\
  \ EBITDA, sponsor, IC date, conventions \u2014 without re-asking the user."
---


# Workflow for ololand-dd-recall

Follow the OloLand command instructions below when the user asks for `ololand-dd-recall` or the equivalent workflow.

# ololand-dd-recall

You are reading the persistent fact store for an OloLand deal. Every fact returned was confirmed by an analyst at some point and survives across conversation sessions.

## Required inputs

1. **deal_id** — the OloLand deal whose facts to recall.

Optional:
- **keys** — list of specific keys to filter on (e.g. `["ebitda_fy24_confirmed", "sponsor_name"]`). Omit to recall every fact stored for the deal.

## Action

Call `recall_deal_facts` with the `deal_id` and (optionally) `keys`. Render the response in this format:

```
Confirmed facts for <deal_id>:
  <key>: <value>
    Provenance: <note if any>
    Last updated: <updated_at>
```

If the result is empty:

```
No confirmed facts for <deal_id>. Use ololand-dd-remember to start building the deal's persistent record.
```

## When to use

- **At the start of any new session about a deal.** Run `ololand-dd-recall` before doing anything else so you have the analyst-confirmed context loaded before the conversation drifts.
- **Before composing an IC memo or CIM section.** Cross-reference what the corpus says with what analysts have explicitly confirmed; conflicts are signal.
- **When a previous answer feels wrong.** A recalled fact may explain why — e.g. the model is quoting unaudited management figures when the analyst confirmed an adjusted number lives at key `ebitda_fy24_confirmed`.

## When NOT to use

- For information that's pulled from the deal corpus on demand (use `search_deal_documents` or `search_extracted_knowledge` for that).
- For deal-level metadata (use `get_deal` instead).
- As an audit trail for AI claim corrections (use the corrections endpoint — `unsupported OpenAI claim-correction workflow (see unsupported-workflows.json)`).

## Pairing rule

`ololand-dd-recall` and `ololand-dd-remember` are companions. The institutional-memory pattern:

1. Open a session — start with `ololand-dd-recall <deal_id>`.
2. Do work; surface a fact that the corpus cannot give you.
3. Confirm with the user.
4. `ololand-dd-remember` it.
5. Future sessions start the loop again with `ololand-dd-recall`.

Companion skill: `cmd-recall` (auto-loads). Companion command: `ololand-dd-remember`.


## OpenAI execution requirements

Use the connected MCP server's current tool schemas. Do not invent tool arguments, job-status endpoints, inputs, or outputs. If a referenced tool is unavailable, explain the limitation and request the needed connection or data. Invoke writes only when the user has requested the corresponding action. Do not initiate purchases or payments. An unrun, unsupported, or unavailable procedure is a gap, never a passing result.


OpenAI cannot execute local lifecycle hooks. Use the packaged explicit setup/review workflow when requested. Server-side MCP auditing remains authoritative; preserve evidence blockers and human-only approval gates.

Claim-correction submission is unsupported in this OpenAI upload because the current handler records surface=cowork. Do not invoke submit_agent_claim_correction from OpenAI. Explain the limitation and retain proposed correction text for human review without claiming submission. See unsupported-workflows.json for the excluded canonical workflow.
