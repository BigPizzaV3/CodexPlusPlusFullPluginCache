---
name: vaiz-agents
description: Work safely with Vaiz AI agents — recognise agent members (isAgent true), learn what each agent does with list_agents, confirm with the user before assigning or mentioning one, report whether the agent run started, and review past runs.
---

# Vaiz AI agents

A Vaiz space can have AI agents: configured automations that act on their own inside their project/board scope. Each agent is also a member of the space, so it shows up next to people and is assigned or mentioned by its member id. It is not a person: never treat an agent as a teammate who will "pick up" a task.

## Prerequisite

The Vaiz MCP server (`https://api.vaiz.com/mcp`) must be available through the installed Vaiz plugin and authorized with OAuth (open the Vaiz connection and complete OAuth sign-in). Reading agents and runs needs the `agents:read` permission of the connection; starting an agent by assigning or mentioning it needs `agents:write` ("Start AI agents" on the consent screen).

Vaiz tools can appear under different names depending on how Vaiz is connected: `mcp__Vaiz__query_tasks` for a directly configured MCP server, or `mcp__codex_apps__vaiz_query_tasks` (sometimes with a longer app prefix such as `vaiz_testing_`) when Vaiz is installed as an app. Match tool names case-insensitively and by the tool suffix (`query_tasks`, `show_tasks`, …), not by an exact `Vaiz` prefix. Tools may also be loaded lazily: a Vaiz tool that is not in the current tool list is not missing — load it through tool search (for example `Vaiz list_agents`) before concluding it is unavailable. Work with Vaiz only through these tools: do not open app.vaiz.com in a browser or drive the Vaiz desktop app with Computer Use, even if the user's `@Vaiz` mention also resolves to that app.

## Recognising an agent

- Member, task, follower, and comment tools mark agent members with `isAgent: true`. A comment whose author has `isAgent: true` is an agent's reply. History tools add "(AI agent)" to the name instead.
- `list_agents` (optional `projectId`) lists agents with `memberId`, `instructions`, `trigger`, `runsWhen`, `mode`, `writeCapabilities`, `scope`, and `status` / `paused`.
  - `agentsEnabled: false` — agents are off in the space; assigning one does nothing.
  - `status: disabled` — the agent cannot run; `statusReason` says why. Do not assign or mention it.
  - `canStartAgents: false` — the connection lacks `agents:write`; an assignment or mention will not start a run. Tell the user they can reconnect and allow it.
  - `aiCreditsExhausted: true` — no agent can start until credits refresh or are bought; only the space owner can buy them.

## What starts a run

| Action | Effect |
| --- | --- |
| Assign an agent to a task (`create_task` / `edit_task` assignees) | Starts a run on that task |
| Mention an agent in a task comment (`create_comment` / `edit_comment`) | Starts a run that answers in the thread |
| Mention in a milestone or document comment, or inside any body | Nothing runs |
| Add an agent as a follower | Nothing runs |

Only agents with `answersAssignmentsAndMentions: true` react to assignments and mentions. Agents with event triggers can also react to your edits: creating or changing a task, adding a comment, or creating or editing a milestone in their scope (`runsWhen` says when). Board automations never wake agents.

The agent's `mode` decides what happens to its changes: `suggest` only proposes, `ask` waits for a human approval on the run page (comments are posted right away), `auto` applies changes immediately. Every run spends the space's AI credits.

## Rules

1. **Confirm first.** Before assigning or mentioning an agent, tell the user it is an AI agent, what it will do (instructions, mode, write capabilities from `list_agents`), and that it will start a run. Proceed only after the user agrees, unless they explicitly asked for that agent.
2. **No agent as a fallback assignee.** When the user asks to assign "someone" or a role, choose among people. Offer an agent only when its instructions fit, and say it is an agent.
3. **Use the member id** from `list_agents` (the same id as in `query_members`), never `agentId`.
4. **Report the outcome.** `create_task`, `edit_task`, `create_comment`, and `edit_comment` return `agentInvocations` with `runStarted`, `runUrl`, `mode`, or `notStartedReason`. Say plainly whether the agent started and, if not, why. If an invocation carries `buyCreditsUrl`, give the user that link.
5. **Do not wait for the agent.** Point the user to the task, its comments, or `runUrl` instead of polling.
6. **Unassigning stops nothing.** A started run is cancelled only on the run page by a Manager or Owner of the agent's scope.

## Reading what agents did

- `list_agent_runs` — runs newest first, one page at a time (default 20, max 50), filtered by `agentId`, `projectId`, `taskId`, `statuses`, `triggers`, `modes`, or dates. Load the next page with `nextCursor` only when the user needs older runs.
- `get_agent_run` — one run by `runId` or `number`: the agent's report and every proposed or applied action with its decision (`pending` actions wait for approval on the run page).

Reading runs never starts an agent and spends no credits. `create_milestone` and `edit_milestone` do not report the runs they cause; check `list_agent_runs` if the user asks.

Further reading: https://vaiz.com/help/tutorials/how-to-connect-vaiz-to-mcp · https://vaiz.com
