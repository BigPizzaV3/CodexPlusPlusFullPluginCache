---
name: ololand-dd-watchlist
description: Use when the user asks to run the OloLand ololand-dd-watchlist workflow.
  Create, inspect, and promote OloLand watchlists for continuous company and signal
  monitoring.
---


# Workflow for ololand-dd-watchlist

Follow the OloLand command instructions below when the user asks for `ololand-dd-watchlist` or the equivalent workflow.

# Watchlist

Use this command when the user wants ongoing monitoring for a sourcing thesis, signal-driven target tracking, or promotion of a watchlist match into a deal.

## Usage

```
ololand-dd-watchlist list
ololand-dd-watchlist create "Healthcare IT carveouts" criteria='{"query":"healthcare IT carveouts","company_scope":"both"}'
ololand-dd-watchlist matches <watchlist_id>
ololand-dd-watchlist promote <watchlist_id> <match_id>
```

## Execution

1. `list` — call `list_watchlists`.
2. `create` — ask for a name and criteria if absent, then call `create_watchlist`.
3. `matches` — call `list_watchlist_matches`, defaulting to active/non-dismissed matches.
4. `promote` — confirm the user wants to create a deal, then call `promote_watchlist_match`.
5. If the user starts from prose instead of a watchlist id, run `ololand-dd-company-discovery` first and use its filters as watchlist criteria.

## Output

- For lists: watchlist name, matched count, threshold, last matched time, and criteria.
- For matches: company, match score, match reason, signal count, promoted deal id if present.
- For promote: created deal id, canonical company name, and returned `view_url`.

## Guardrails

- Promotion creates a real deal row. Confirm before calling `promote_watchlist_match`.
- Dismissal/pinning remains a UI workflow unless the user explicitly asks for match state updates.
- Watchlists are monitoring infrastructure, not diligence conclusions.


## OpenAI execution requirements

Use the connected MCP server's current tool schemas. Do not invent tool arguments, job-status endpoints, inputs, or outputs. If a referenced tool is unavailable, explain the limitation and request the needed connection or data. Invoke writes only when the user has requested the corresponding action. Do not initiate purchases or payments. An unrun, unsupported, or unavailable procedure is a gap, never a passing result.


OpenAI cannot execute local lifecycle hooks. Use the packaged explicit setup/review workflow when requested. Server-side MCP auditing remains authoritative; preserve evidence blockers and human-only approval gates.

Claim-correction submission is unsupported in this OpenAI upload because the current handler records surface=cowork. Do not invoke submit_agent_claim_correction from OpenAI. Explain the limitation and retain proposed correction text for human review without claiming submission. See unsupported-workflows.json for the excluded canonical workflow.
