# Writesonic Agents Plugin

> Connect Writesonic Agents to Claude Code. Manage tasks, playbooks, grids, knowledge base, and pages from chat — triage work, follow what agents did, inspect playbook runs, read grids, search your Knowledge Base and Brand Kit, and pull Pages reports.

Works with **Claude Code**. The MCP server also connects to **Claude.ai**, **Claude Desktop** and **ChatGPT**.

---

## Installation

Claude Code:

```
# Add the Writesonic marketplace (one-time)
/plugin marketplace add Writesonic/mcp-plugins

# Install this plugin
/plugin install writesonic-agents@writesonic
```

Then `/mcp` → select `agents` → sign in with your Writesonic account in the browser.

---

## What's Included

| Skill | What it does |
| ----- | ------------ |
| **task-triage** | Open task counts grouped by assignee, then the high-priority tasks that aren't done |
| **agent-run-review** | Step-by-step walkthrough of what an agent did on a task |
| **status-snapshot** | One-shot status — open tasks, recent playbook runs, failing integrations — chained in a single `execute_batch` call |
| **whoami** | `/writesonic-agents:whoami [project]` — identity and accessible projects |
| **tasks** | `/writesonic-agents:tasks [filter]` — list tasks by priority, status, assignee or keyword |
| **new-task** | `/writesonic-agents:new-task <title>` — create a task (confirms first) and assign it to you |
| **brand-voice** | `/writesonic-agents:brand-voice <question>` — answer from the Brand Kit / Knowledge Base |

---

## Requirements

- **MCP-compatible client** – Claude Code, Claude.ai, Claude Desktop or ChatGPT
- **Writesonic account with Agents access** – currently limited to selected enterprise and agency accounts in beta
- **At least one project** in your Agents workspace

---

## Usage

**Just ask naturally** – skills auto-trigger based on your request:

```
"How many open tasks do I have, grouped by assignee?"           → task-triage activates
"What did the agent do on task ABC-123? Walk me through it"      → agent-run-review activates
"Give me a status snapshot of the workspace"                     → status-snapshot activates
```

Quick commands run on demand: `/writesonic-agents:whoami`, `/writesonic-agents:tasks high priority open`, `/writesonic-agents:new-task Refresh the pricing page for AI search`, `/writesonic-agents:brand-voice what does our guide say about tone`.

Only `create_task`, `update_task` and `comment_on_task` change anything — everything else is read-only, and writes are shown to you and confirmed before they happen.

### Example Workflows

#### Task Triage

1. Ask: "How many open tasks do I have, grouped by assignee?"
2. Skill resolves your project, then counts open tasks per person
3. Skill lists the high-priority tasks that aren't done
4. You get a workload table and the list that needs attention

#### Follow an Agent's Work

1. Ask: "What did the agent do on task ABC-123?"
2. Skill fetches the runs for that task
3. Skill walks the latest run's steps in order
4. You get what was asked, each step, the outcome, and anything that failed

#### Status Snapshot

1. Ask: "Give me a status snapshot: open tasks, recent playbook runs, failing integrations"
2. Skill chains the three reads in one batched call instead of round-tripping
3. Skill flags disconnected or failing integrations
4. You get a three-section status you can paste into a standup

---

## MCP Configuration

The plugin connects to the hosted Writesonic Agents MCP server at `https://mcp.agents.writesonic.com/mcp` — no local server or API keys.

- **Claude.ai / Claude Desktop**: Settings → Connectors → Add custom connector → paste the URL → sign in
- **Claude Code without the plugin**: `claude mcp add writesonic-agents --transport streamable-http https://mcp.agents.writesonic.com/mcp`
- **ChatGPT**: enable Developer Mode and add the URL as a connector

Docs: [MCP server](https://apidocs.writesonic.com/agents-mcp/mcp-server) · [Setup](https://apidocs.writesonic.com/agents-mcp/setup) · [Use cases](https://apidocs.writesonic.com/agents-mcp/examples) · [Tools reference](https://apidocs.writesonic.com/agents-mcp/tools-reference)
Support: support@writesonic.com
