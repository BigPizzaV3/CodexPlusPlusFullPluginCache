---
name: welcome
description: Orient the user to available OloLand tools when requested after connection.
---

# Welcome to OloLand

You're connected to OloLand's M&A intelligence engine — available tools for due diligence.

## What You Can Do

**Ask about deals:**
- "What are the top risks for the Paragon Flight School deal?"
- "Reconcile the revenue figures across the CIM and audited financials"
- "Run a risk-adjusted DCF with sensitivity analysis"

**Run analysis:**
- `ololand-dd-dd-analyze` — Bounded extraction, risk, and financial-snapshot pipeline; it does not run valuation, forensic, war-game, reconciliation, or memo engines
- `ololand-dd-valuation <deal_id> read all` — inspect governed DCF/LBO and source-backed comps; use `ololand-dd-valuation <deal_id> run <method>` or `ololand-dd-valuation <deal_id> refresh <method>` only when you explicitly want a fresh model candidate
- `ololand-dd-risk-report` — risk assessment across 67 categories / 311 risk factors
- `ololand-dd-similar-deals` — Find comparable transactions from deal history
- `ololand-dd-war-game` — Competitive strategy simulation

**CRE underwriting:**
- `run_cre_stress_test` — Multi-scenario stress on debt service coverage
- `run_cre_debt_sizing` — Size loans against DSCR / LTV / debt-yield constraints
- `verify_sponsor_assumptions` — Cross-check sponsor proforma against comps and market data

**Multi-turn conversations:**
- `create_conversation_session` / `list_conversation_sessions` / `get_conversation_session_summary` — Persist context across long-running deal investigations

**Generate documents:**
- `ololand-dd-talk-to-deal` — Conversational deal Q&A
- CIM and investment memo generation

## Try It Now

Resolve Paragon Flight School through available tools if the user wants to explore a sample; do not assume it exists in this workspace. Start with:

> "What are the key risks and opportunities for the Paragon Flight School acquisition?"

This will demonstrate OloLand's risk taxonomy, source provenance, and decision framework — the capabilities that generic LLMs can't replicate.


## OpenAI execution requirements

Use the connected MCP server's current tool schemas. Do not invent tool arguments, job-status endpoints, inputs, or outputs. If a referenced tool is unavailable, explain the limitation and request the needed connection or data. Invoke writes only when the user has requested the corresponding action. Do not initiate purchases or payments. An unrun, unsupported, or unavailable procedure is a gap, never a passing result.


OpenAI cannot execute local lifecycle hooks. Use the packaged explicit setup/review workflow when requested. Server-side MCP auditing remains authoritative; preserve evidence blockers and human-only approval gates.

Claim-correction submission is unsupported in this OpenAI upload because the current handler records surface=cowork. Do not invoke submit_agent_claim_correction from OpenAI. Explain the limitation and retain proposed correction text for human review without claiming submission. See unsupported-workflows.json for the excluded canonical workflow.
