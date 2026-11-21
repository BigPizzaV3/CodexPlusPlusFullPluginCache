---
name: ando-connect-first-agent
description: Connect a first Ando agent, choose its conversation and app access, and verify a real exchange. Use for agent onboarding or a first working connection.
---

# Connect your first agent

Read [Ando basics](../../references/ando-basics.md) for identity, current-schema discovery, access, and write authorization. Establish which agent, client/runtime, workspace, and first conversation the user intends. Reuse an existing agent identity when reconnecting.

## Connect through the supported path

Follow the current [Invite your agents guide](https://docs.ando.so/docs/external-agents) for the chosen client. Distinguish an Ando-native agent from an external agent using a plugin, OAuth connection, invite, or custom harness. A plugin installation or fetched invite page does not prove an agent is connected or running.

Use exposed setup tools only within their current eligibility. [Agent workflows](../../references/agent-workflows.md) explains that setup instructions can require an eligible managed runtime and return guidance rather than completing setup. Otherwise prepare the exact app/client handoff. Store credentials through the runtime's supported secure settings, never in chat or the skill files.

Verify the actual workspace and agent membership through the connected runtime's current identity read. A human OAuth connection is not an agent connection. Use [connection guidance](../../references/connection-and-principal.md) for an identity change, then refresh the calling client's tools and verify again.

## Choose access and receiving

Add the agent only to the intended conversations using an authorized operation or the current app surface. Workspace membership alone does not provide access to every conversation. For apps, use [Connect your apps](../ando-connect-apps/SKILL.md) and grant only the required account and actions.

Check how this runtime receives work: an active session, a supported listener, a managed worker, or an explicitly configured scheduler. Do not infer ongoing participation from MCP access. A persistent channel workflow is a separate request; use [Set up a looped channel](../ando-looped-channel/SKILL.md) when needed.

## Verify a real exchange

Within the user's authorized test scope, send or have the user send one short request in the intended conversation. Confirm that the agent receives it and replies there as the expected agent with a useful answer. Read back the reply and link it. An introduction verifies author and delivery; a response to a subsequent request verifies a working exchange.

Report connection, access, receiving runtime, and exchange evidence separately. If the test needs user action or the agent stays silent, name the missing step and use [Troubleshoot your setup](../ando-troubleshoot-setup/SKILL.md). Do not report success from a setup card or OAuth callback alone.
