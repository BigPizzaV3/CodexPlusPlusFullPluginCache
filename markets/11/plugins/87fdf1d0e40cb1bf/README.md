# Vinktar for coding agents

[Vinktar](https://vinktar.com?ref=agent-plugin) is product analytics and error tracking your coding
agent can use. This plugin gives Claude Code, Cursor and Codex two things at once:

- **The Vinktar MCP server** (`https://mcp.vinktar.com/mcp`). You sign in in the browser and choose
  a workspace, the projects it may reach, and read, build or configure. No key to paste.
- **The `setup` skill.** Run `/vinktar:setup` in Claude Code, or ask your agent to "set up Vinktar".
  It reads your repo, installs the SDK for your stack in a standard layout, fetches the project's
  write key over the connection, wires identify, errors and source maps, defines each event it
  tracks, checks what actually arrived, and ends with a list of every environment variable and where
  it goes.

Once it's installed, ask it things like "what changed this week?" or "which errors hit the most
people since the last release?".

You don't need an account beforehand. Before anyone signs in, the agent can start a project on its
own (`start_project`), set the app up with its key and check that
data arrives; you then open the claim link it gives you, which signs you in or makes your account and
keeps the project with its data. Unclaimed, a project takes up to 10,000 events and is deleted with
its data after 7 days.

## Install

**Claude Code**

```sh
claude plugin marketplace add vinktarhq/agent
claude plugin install vinktar@vinktar
```

Run `/vinktar:setup`. It can set the app up before you sign in; to ask questions about your data
later, run `/mcp`, pick `vinktar` and authenticate.

**Claude Desktop**

Add the plugin and ask Claude to set up Vinktar. To ask about your data afterwards, connect Vinktar on
the plugin's Connectors tab or at
[claude.ai/customize/connectors](https://claude.ai/customize/connectors): adding the plugin does not
sign you in by itself.

**Cursor**

Install Vinktar from the Cursor Marketplace, or import this repository under Customize → Plugins →
From GitHub Repository. Cursor asks you to sign in the first time it connects.

**Codex**

```sh
codex plugin marketplace add vinktarhq/agent
codex plugin add vinktar@vinktar
codex mcp login vinktar
```

**Any other MCP client**

Add `https://mcp.vinktar.com/mcp` as a Streamable HTTP server; it finds the sign-in on its own. Then
ask your agent to call `get_install_guide`. Setup for each client:
[vinktar.com/docs/mcp](https://vinktar.com/docs/mcp?ref=agent-plugin).

**A harness that reads skills but has no plugin format**

Copy `.agents/skills/setup/` into your repository (or your home directory, wherever your
tool looks). It is the same skill, at the path most tools agree on, and it needs the MCP server
added separately.

## What it can and can't do

The agent sees what you'd see in the workspace and project you approved. The only things it can
delete are boards and panels, and those stay restorable from the boards page for 30 days. It can't
delete events, errors, issues or projects, create projects or keys once you are signed in, manage
members or billing, or add somewhere new to send your data. Before sign-in it can start one project
nobody owns until you claim it. Every call is logged on the project's AI agents page, and an
admin can switch agents off.

Vinktar works on every plan, Free included. Data requests count against a monthly allowance;
setting a project up never does, and nothing is charged per call.

## License

MIT
