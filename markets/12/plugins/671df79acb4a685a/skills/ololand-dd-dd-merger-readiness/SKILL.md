---
name: ololand-dd-dd-merger-readiness
description: Use when the user asks to run the OloLand ololand-dd-dd-merger-readiness
  workflow. Check per-side data readiness (target / acquirer / combined) for a merger-analysis
  deal. Zero-credit read.
---


# Workflow for ololand-dd-dd-merger-readiness

Follow the OloLand command instructions below when the user asks for `ololand-dd-dd-merger-readiness` or the equivalent workflow.

# ololand-dd-dd-merger-readiness

Report data-readiness tier for each side of a third-party merger-analysis deal so the user knows which engines are safely callable.

## Required input

- **deal_id** — the merger-analysis deal ID (starts with `merger_`). Ask if missing.

## Action

1. Call `get_merger_readiness(deal_id=...)`. The tool returns a dict keyed by side with this shape per side:

   ```
   {
     "side": "target" | "acquirer" | "combined",
     "tier": "high" | "medium" | "low" | "missing",
     "has_filings": bool,
     "has_audited_financials": bool,
     "has_market_research": bool,
     "document_count": int,
     "source_quality_score": float
   }
   ```

2. Render a compact 3-row summary (target / acquirer / combined) with tier label and document_count.

3. If any side is `low` or `missing`, list the missing artifacts (10-K / 10-Q / 8-K / audited financials / market research) and tell the user where they typically come from. Suggest uploads via `upload_deal_document(deal_id=..., deal_side="target"|"acquirer"|"combined")`.

4. If all three sides are `medium` or higher, point the user at the four merger engines that are safe to run: `ololand-dd-dd-merger-rerun-math`.

## Subscription

Zero-credit read — works on any tier including Developer. The heavy engines (premium / accretion / DCF / HHI) now also run on Developer as part of the bounded single-deal trial, metered against the monthly credit budget — they are no longer Pro-gated. Only the saleable Forensic Screen PDF (`generate_forensic_screen_pdf`) is paid.


## OpenAI execution requirements

Use the connected MCP server's current tool schemas. Do not invent tool arguments, job-status endpoints, inputs, or outputs. If a referenced tool is unavailable, explain the limitation and request the needed connection or data. Invoke writes only when the user has requested the corresponding action. Do not initiate purchases or payments. An unrun, unsupported, or unavailable procedure is a gap, never a passing result.


OpenAI cannot execute local lifecycle hooks. Use the packaged explicit setup/review workflow when requested. Server-side MCP auditing remains authoritative; preserve evidence blockers and human-only approval gates.

Claim-correction submission is unsupported in this OpenAI upload because the current handler records surface=cowork. Do not invoke submit_agent_claim_correction from OpenAI. Explain the limitation and retain proposed correction text for human review without claiming submission. See unsupported-workflows.json for the excluded canonical workflow.
