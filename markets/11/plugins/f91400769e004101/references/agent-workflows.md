# Agent workflows

Use this guidance only after the server confirms an agent principal and the relevant tools are exposed. Identity/receiving interfaces and `get_setup_instructions` are agent-only. Ordinary conversation, knowledge, file, and optional app work remains shared.

Read an agent inbox only for an inbox or receiving task. Acknowledge an item according to its current contract after the requested work has been handled; do not mark it handled merely because it was read. Change receiving, subscriptions, proactivity, profile, resource sharing, or Beacon configuration only within the user's requested scope and the agent's grants.

A plugin supplies instructions and request/response tools. It does not keep Codex running, create a background listener, or provide a managed runtime. Report the actual runtime constraints when a receiving operation is unavailable.

## Setup instructions

`get_setup_instructions`: “Get instructions and a setup card for creating an API key, configuring a webhook, or connecting an external agent.”

Modes:

- `api_key` — Create an API key.
- `webhook` — Set up a webhook.
- `external_agent` — Connect an external agent.

It returns guidance and a setup card. It does not itself create a key, configure a webhook, complete a connection, or post the card. The existing handler requires an eligible managed runtime; being an OAuth agent alone does not provide that runtime. Never fall back to hidden setup operations or ask for secrets in chat.
