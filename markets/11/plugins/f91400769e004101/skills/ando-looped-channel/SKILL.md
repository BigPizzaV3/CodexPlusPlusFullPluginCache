---
name: ando-looped-channel
description: Set up or refine an Ando channel where an agent follows ongoing work through events, recurring checks, or agent judgment. Use for requests to loop in an agent, watch a channel or source, or keep a workflow moving over time.
---

# Set up a looped channel

Read [Ando basics](../../references/ando-basics.md) for identity, current-schema discovery, access, and write authorization. Discover only tools needed for this request.

Create a persistent, understandable channel workflow with a real execution mechanism and a clear way to pause it.

## Clarify intent before implementation

Before creating or changing channels, triggers, agents, or automation, clarify the user's intended behavior. Use facts already supplied; ask only for unresolved decisions. Establish:

- The outcome and target channel: what should the agent help accomplish?
- Activation: incoming events, a recurring check with timezone, agent judgment about when intervention is useful, or a combination?
- Inputs and scope: which conversations, apps, projects, or records should inform it?
- Authority and reporting: investigate, summarize, ask people, create tasks, or take specified actions? When should it post, escalate, or stay quiet?
- Ownership and stopping: who owns the workflow, and when should it stop or be paused?

Summarize the agreed behavior before implementation. A vague request to “loop this channel” is insufficient to choose autonomous actions or a cadence. Do not add a second approval round when the user has already supplied the necessary intent and authorization.

## Resolve the channel and execution mechanism

Inspect the current Ando identity, workspace, tool catalog, and existing channel context. Reuse the intended channel and existing workflow when appropriate. Check grants before assuming channel creation, agent configuration, or automation tools are available.

Choose an execution mechanism that actually exists in this environment:

- Event-driven: a supported incoming source and trigger, or an agent receiver that can wake the runtime.
- Recurring: a saved Ando automation when available, or an explicitly selected external runtime scheduler.
- Agent judgment: channel participation/proactivity settings and instructions for an agent whose runtime can receive relevant activity. Define the evidence that warrants intervention and its permitted actions. Judgment determines whether and how to act; it does not itself keep a process running.

Inspect live schemas before using automation, subscription, or proactivity tools; these may be unavailable to an external plugin identity. If configuration requires Studio or provider consent, give the exact remaining handoff and complete independent preparation. MCP access or a written prompt alone does not establish ongoing execution. Do not create a Codex schedule when the user intends an Ando-native agent without clarifying that runtime choice.

For connected sources, inspect the exposed schemas. The compact catalog uses `list_connections`, `search_app_tools`, and `get_app_tool_schemas` (older compact servers use `list_app_tools`) for account and tool/schema discovery; legacy catalogs may expose `list_tools` and `get_tool_schemas`. Use only current exposed tools to verify the account, scope, and actions. For a provider alert feed, follow [the alert-channel skill](../ando-alert-channel/SKILL.md); otherwise consult Ando's current provider setup guide.

## Configure the agreed behavior

Write a concise operating instruction containing the objective, scope, trigger, decision criteria, allowed actions, posting destination, and escalation/stop conditions. Agent judgment should use concrete signals such as an unanswered request, a changed blocker, or a deadline at risk. Preserve the user's notification preference; avoid unchanged updates unless they requested regular reports.

Prevent repeated work using stable source IDs and durable progress where the runtime supports it. Exclude the agent's own outputs from re-triggering the same action and bound retries and agent-to-agent exchanges. Keep follow-up in the source thread when appropriate. An inbox acknowledgment is not proof that the underlying assignment is complete.

Use existing rich cards for source objects. Use a miniapp when people need structured input or ongoing triage; discover its actual command and action contracts. Controls must invoke supported, authorized operations. A decorative card or saved miniapp does not provide a trigger or worker.

## Verify and hand off

Read back the saved configuration and perform a bounded test of the chosen activation path. Check the resulting agent run and channel output separately from event acceptance. For judgment-based participation, test both a situation that warrants a response and one that should remain quiet when feasible. Do not fabricate a production incident to test the workflow.

Report the channel, execution owner, activation/decision rules, allowed actions, test evidence, and where to pause or edit it. Distinguish configured, awaiting human/provider setup, and verified running. If a live test cannot be completed, name the exact missing evidence.

Current references: [Ando MCP](https://docs.ando.so/docs/ando-mcp), [Agents](https://docs.ando.so/docs/agents), [External agents](https://docs.ando.so/docs/external-agents), [Studio](https://docs.ando.so/docs/studio). Refresh relevant guidance and live schemas at use time.
