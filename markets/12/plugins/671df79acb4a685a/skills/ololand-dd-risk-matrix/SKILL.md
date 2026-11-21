---
name: ololand-dd-risk-matrix
description: Use when the user asks to run the OloLand ololand-dd-risk-matrix workflow.
  Render the 67-category risk matrix (311 tracked risk factors) as an interactive
  inline tile.
---


# Workflow for ololand-dd-risk-matrix

Follow the OloLand command instructions below when the user asks for `ololand-dd-risk-matrix` or the equivalent workflow.

You have access to the `render_risk_matrix_tile` MCP tool from the OloLand server.

If the user has a deal loaded (check conversation context or call `list_deals`), invoke `render_risk_matrix_tile` with that `deal_id`. The tool's response is an MCP App — show the interactive view only if the client supports it. Otherwise explain that display limitation and summarize only data actually returned by the tool.

If no deal is loaded, ask the user which deal they want to analyze, or offer to run `ololand-dd-dd-analyze` first.


## OpenAI execution requirements

Use the connected MCP server's current tool schemas. Do not invent tool arguments, job-status endpoints, inputs, or outputs. If a referenced tool is unavailable, explain the limitation and request the needed connection or data. Invoke writes only when the user has requested the corresponding action. Do not initiate purchases or payments. An unrun, unsupported, or unavailable procedure is a gap, never a passing result.


OpenAI cannot execute local lifecycle hooks. Use the packaged explicit setup/review workflow when requested. Server-side MCP auditing remains authoritative; preserve evidence blockers and human-only approval gates.

Claim-correction submission is unsupported in this OpenAI upload because the current handler records surface=cowork. Do not invoke submit_agent_claim_correction from OpenAI. Explain the limitation and retain proposed correction text for human review without claiming submission. See unsupported-workflows.json for the excluded canonical workflow.
