---
name: ololand-dd-remember
description: "Use when the user asks to run the OloLand ololand-dd-remember workflow.\
  \ Persist a confirmed fact about an OloLand deal across sessions. Writes into deal_session_memory\
  \ so the next time you (or another analyst) open this deal, the fact is recalled\
  \ automatically \u2014 confirmed EBITDA, sponsor name, IC date, working-capital\
  \ convention, etc."
---


# Workflow for ololand-dd-remember

Follow the OloLand command instructions below when the user asks for `ololand-dd-remember` or the equivalent workflow.

# ololand-dd-remember

You are persisting a confirmed (key, value) fact about an OloLand deal into `deal_session_memory`. This is the externalized-working-memory primitive — facts written here survive across conversation sessions about the same deal.

## Required inputs

Ask the user for these if any are missing:

1. **deal_id** — the OloLand deal this fact belongs to.
2. **key** — a short, stable kebab-case identifier (≤ 200 chars). Examples:
   - `ebitda_fy24_confirmed`
   - `sponsor_name`
   - `ic_date`
   - `wc_normalization_convention`
   - `dd_milestone_status`
3. **value** — the fact itself. Any JSON value: a number, string, list, or small object.

Optional:
- **note** — short provenance note (≤ 1000 chars). Where the fact came from, what confirmed it, who confirmed it. Strongly recommended for audit trail.

## Action

Call `remember_deal_fact` with the collected fields. The tool is idempotent on `key` — re-remembering the same key replaces the value and updates the note.

After success, confirm to the user with the returned status (`created` or `updated`) and quote back the key and value. If the user supplied a note, quote that too so they see the audit trail being written.

## When to use

- A user confirms a number that the AI extracted ("yes, $34.2M FY24 EBITDA is right").
- A partner gives a fact in a meeting that should persist ("Jim from MidOcean is leading").
- A modeling convention is agreed ("we're normalizing WC against the 3-year average, not the trailing 12").
- A milestone advances ("LOI signed 2026-05-20").
- A deal-specific assumption is locked ("4.0% terminal growth — discussed with sponsor").

## When NOT to use

- For working-state of an in-progress task (use TodoWrite-style state inside the conversation instead).
- For risks, materialized risks, or claim corrections — those have dedicated capture surfaces (`record_materialized_risks`, `submit_risk_correction`, `unsupported OpenAI claim-correction workflow (see unsupported-workflows.json)`).
- For deal outcomes — use `record_deal_outcome`.
- For information that is derivable from the deal corpus by running a tool — recompute don't memorize. Reserve `ololand-dd-remember` for analyst confirmations the corpus can't yield.

## Naming discipline

Keys are durable. Pick names a future analyst would search for:

| Good | Bad |
|---|---|
| `ebitda_fy24_confirmed` | `ebitda` (ambiguous), `confirmed_ebitda_oct_2025` (date-stamped) |
| `sponsor_lead_partner` | `partner_name`, `lead`, `who_runs_this` |
| `wc_normalization_convention` | `notes`, `wc_thing` |

Companion skill: `cmd-remember` (auto-loads). Companion command: `ololand-dd-recall`.


## OpenAI execution requirements

Use the connected MCP server's current tool schemas. Do not invent tool arguments, job-status endpoints, inputs, or outputs. If a referenced tool is unavailable, explain the limitation and request the needed connection or data. Invoke writes only when the user has requested the corresponding action. Do not initiate purchases or payments. An unrun, unsupported, or unavailable procedure is a gap, never a passing result.


OpenAI cannot execute local lifecycle hooks. Use the packaged explicit setup/review workflow when requested. Server-side MCP auditing remains authoritative; preserve evidence blockers and human-only approval gates.

Claim-correction submission is unsupported in this OpenAI upload because the current handler records surface=cowork. Do not invoke submit_agent_claim_correction from OpenAI. Explain the limitation and retain proposed correction text for human review without claiming submission. See unsupported-workflows.json for the excluded canonical workflow.
