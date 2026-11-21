---
name: executor
description: Use when the user asks to build or run an Executor app, use tools in their Executor workspace, or work with data in those apps.
---

# Work with Executor

Use this plugin only for the user's requested Executor work. Begin by reading the server's Executor skill with `skills({ app: "executor", name: "executor" })`. If that app slug is unavailable, list skills and use the returned app slug.

Discover relevant tools through `execute` with `tools.search`. Read their exact schemas using `tools.search.describe` before calling them. Use only returned paths and the workspace and accounts the user intends. Read the server's app-authoring skill before building or changing an app.

Keep inputs and outputs limited to the task. Connect accounts through Executor's secure browser links; never ask for passwords, API keys, or verification codes in chat. Do not retrieve, display, or transmit stored credentials.

When execution returns an approvalUrl, show it to the user. The user answers in the authenticated browser. Continue with `resume({ requestId })` only; never supply a decision or rerun the program to continue. Earlier effects are not rolled back. Report errors and partial completion accurately, and verify writes before claiming success.

Ask for clarification before ambiguous destructive actions. Do not offer purchases, payment transactions, subscriptions, or upgrades through this plugin. Do not send feedback or other messages on the user's behalf unless they specifically request it.
