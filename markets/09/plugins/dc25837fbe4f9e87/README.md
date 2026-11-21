# Compelling Agent Plugin

Build B2B target lists with [Compelling](https://compelling.ai) directly in Claude, ChatGPT, Codex,
Cursor or another AI client. For sales and business development teams in any B2B market, from
German manufacturers to IT service providers and consultancies.

Describe your ideal customer in your own words: industry, location, size, technologies,
certifications, products or hiring activity. Compelling's AI research agents find matching
companies and check each one against your criteria.

- **Find target companies:** turn a plain-language description into a list of your total addressable market (TAM).
- **Find decision-makers:** identify the right people by role and research business emails and LinkedIn profiles.
- **Research anything:** answer custom questions per company, such as revenue, headcount, tech stack or funding, with source evidence.
- **Rank by fit:** score accounts against your weighted ideal customer profile (ICP) and see why each one ranks where it does.

Results are saved as live lists in your Compelling workspace, with native integrations for
HubSpot, Salesforce, Pipedrive, monday.com and more.

Try: "Find 10 machinery manufacturers in Germany with 100-500 employees that use SAP."

Requires a Compelling account. Built in Cologne, Germany, on European infrastructure.

This is an [Agent Plugin](https://agent-plugins.org) bundling:

- **MCP server** — the remote Compelling MCP at `https://mcp.compelling.ai` (Streamable HTTP,
  OAuth). Connect with your Compelling account.
- **Skills** — playbooks that teach your agent to use Compelling well:
  - `build-tam-list` — find target companies by geography and custom criteria
  - `enrich-contacts` — research company data and buying signals, or find and enrich decision-makers
  - `rank-by-icp` — prioritize target companies with explicit, weighted customer-fit criteria
  - `feedback` — report a bug or rough edge from right inside your agent

## Requirements

A [Compelling](https://compelling.ai) account. Reading data is free; sourcing, contact
discovery, enrichment, and ranking draw on your workspace's credit balance.

## Install in Claude Code

```
/plugin marketplace add seekwhens/compelling-plugin
/plugin install compelling@compelling
```

Then connect the `compelling` MCP server with your Compelling account (OAuth) when prompted.

## Install in Cursor / Grok Bot

Once listed in the Cursor Marketplace: Customize → search **Compelling** → Install. Grok Bot uses
the same Cursor plugin format (`.cursor-plugin/`), so the listing covers both.

Until then, load locally:

```bash
mkdir -p ~/.cursor/plugins/local && rsync -a --exclude .git /path/to/compelling-plugin/ ~/.cursor/plugins/local/compelling/
```

Copy the folder rather than symlinking it: Cursor skips symlinks in `~/.cursor/plugins/local` that point outside that folder.

Then reload the window and open Customize. Connect the MCP with your Compelling account (OAuth).

Setup docs: https://compelling.notion.site/Compelling-MCP-3cfc763a76238174a7aaf14f7e6353fb

## Install in Codex

Add the marketplace, then install the plugin:

```bash
codex plugin marketplace add seekwhens/compelling-plugin
codex plugin add compelling@compelling
```

For a local checkout, use `codex plugin marketplace add /absolute/path/to/compelling-plugin`
and the same install command. Start a new session, then connect the `compelling` MCP server
with your Compelling account (OAuth).

## ChatGPT

Once listed, install Compelling from the Plugin Directory at https://chatgpt.com/plugins.

Until then, add it in developer mode: Plugins, Create app, server URL `https://mcp.compelling.ai`,
authentication OAuth. Then connect with your Compelling account and pick your workspace.

## Other clients

Any [Agent Plugins](https://agent-plugins.org/specification)-compatible client can load this
directory (spec v1.0.0) — the spec's client list includes VS Code, Cursor, GitHub Copilot,
ChatGPT/Codex, and Kiro. The repo additionally ships the Claude Code plugin layout
(`.claude-plugin/`), so both ecosystems resolve the same skills and MCP server.

## Structure

```
plugin.json                        # Agent Plugins manifest (agent-plugins.org), source for the generated manifests
mcp.json                           # Agent Plugins MCP declaration
.claude-plugin/plugin.json         # Claude Code plugin manifest (generated)
.claude-plugin/marketplace.json    # Claude Code marketplace catalog (this repo)
.mcp.json                          # Claude Code / Codex MCP declaration
.codex-plugin/plugin.json          # OpenAI Codex / ChatGPT manifest (generated)
.agents/plugins/marketplace.json   # OpenAI Codex marketplace catalog (this repo)
.cursor-plugin/plugin.json         # Cursor / Grok Bot manifest (generated)
.cursor-plugin/marketplace.json    # Cursor / Grok Bot marketplace catalog (generated)
skills/
  build-tam-list/SKILL.md
  enrich-contacts/SKILL.md
  rank-by-icp/SKILL.md
  feedback/SKILL.md
```
