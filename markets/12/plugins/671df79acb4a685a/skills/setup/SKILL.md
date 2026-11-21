---
name: setup
description: Connect OloLand and review available deal tools when the user requests
  setup or has a connection error.
---
# Connect OloLand

This is an explicit, user-invoked setup workflow. Enable the packaged `ololand`
MCP connection, complete the client's OAuth sign-in, and inspect the tools
actually available to the connected account. If authentication fails, ask the
user to reconnect. Never request, print, or store account credentials in chat.
Do not run local setup scripts or claim a session-start hook has run.
Resolve a requested deal using the connected server; do not assume a sample
deal or entitlement exists. Report connection or permission gaps explicitly.

OpenAI cannot execute this plugin's local lifecycle hooks. The upload supplies
an explicit workflow, not an automatic setup gate. Server-side MCP auditing
remains authoritative. Preserve tool-returned evidence and permission blockers;
IC approval and other human-only gates stay with authorized people in OloLand.


## OpenAI execution requirements

Use the connected MCP server's current tool schemas. Do not invent tool arguments, job-status endpoints, inputs, or outputs. If a referenced tool is unavailable, explain the limitation and request the needed connection or data. Invoke writes only when the user has requested the corresponding action. Do not initiate purchases or payments. An unrun, unsupported, or unavailable procedure is a gap, never a passing result.


OpenAI cannot execute local lifecycle hooks. Use the packaged explicit setup/review workflow when requested. Server-side MCP auditing remains authoritative; preserve evidence blockers and human-only approval gates.

Claim-correction submission is unsupported in this OpenAI upload because the current handler records surface=cowork. Do not invoke submit_agent_claim_correction from OpenAI. Explain the limitation and retain proposed correction text for human review without claiming submission. See unsupported-workflows.json for the excluded canonical workflow.
