---
name: zid-ops
description: Connect and automate a Zid store. Use to connect an AI agent, n8n, Make or a script to the Zid MCP server, schedule a recurring store job, or fix a Zid MCP tool error in a saved workflow.
---

# Zid ops

Running a Zid store with automations: connecting clients to the Zid MCP server
and scheduling store jobs. The other Zid skills describe the store work; this
one covers how to run it without a chat. Building an app on the Merchant API,
OAuth or webhooks is the `zid-api` skill.

## Ground rules

- The user's explicit instructions take precedence over this skill.
- Secrets stay out of chat: the personal MCP URL and any tool credentials go
  straight into the client's or automation tool's credential settings. In
  examples, write them as placeholders such as `<MCP_URL>`.
- One writer per field. Before automating a write, check whether an installed app
  already writes it (`zid_account.list_installed_apps`) and agree with the
  merchant which one owns it.

## Pick the topic

| Topic | Use it when | Read |
| --- | --- | --- |
| MCP connections | Connecting Claude, Cursor, Codex, n8n, Make or a script to the store's tools; tool errors and statuses | [references/mcp.md](references/mcp.md) |
| Scheduled jobs | A store task should run every day or on an event, without someone in the chat | [references/jobs.md](references/jobs.md) |

Read the topic's reference before writing anything for it; a job usually needs both.

## Steps

1. Pick the topic and read its reference.
2. Settle the inputs: which store, which client or tool, what triggers the run,
   what it reads and what it may change.
3. Produce the artifact: client configuration or workflow steps, with secrets as placeholders.
4. Prove it with a read before any write: call one named read action, such as
   `zid_store.get_context` or `zid_orders.list_orders`.
5. Hand over: where each secret goes, how to rotate it, and how to tell when the
   automation fails.

Done when the client or job has run one read successfully and the merchant knows
where its secret lives.

## Common failures

Answers such as `invalid_arguments`, `confirmation_required`, the stale-plan
statuses and `429` are covered in [references/mcp.md](references/mcp.md), under
"How the tools behave".

| Symptom | Cause | Fix |
| --- | --- | --- |
| Unknown tool in a saved workflow | The workflow uses a renamed tool | Replace the step with the tool and action the matching Zid skill names |
| A skill's tool is not available | The URL loads only some areas | Add the area to `?toolsets=` ([references/mcp.md](references/mcp.md)) |
| The URL stopped working | It was rotated | Copy the new URL from the Zid AI Connector app into every client |
