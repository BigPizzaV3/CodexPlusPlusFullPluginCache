# Shareout

Your agent made it. Share it out.

Share work from your AI workspace with clients, contractors and collaborators outside it—even people who do not use AI themselves.

Your agent helped make it. The people reviewing it do not need an agent. Send an HTML proposal, report or interactive prototype as a browser link. Recipients can view and try the page without joining your Claude, Codex or Cline workspace. Grant commenting access separately when you want feedback; your agent can read it and revise the work at the same address.

[Try a shared page](https://shareout.io/d/cujufgdheurd) · [Connect your agent](https://shareout.io/agents) · [Templates](https://shareout.io/templates/)

This repository contains the public plugin, skill, and connection configurations. The hosted service and standalone CLI are maintained separately. Repository installation is available independently of curated directory approval; see [distribution status](docs/distribution.md).

## Claude Code

```sh
claude plugin marketplace add geland/shareout-integrations
claude plugin install shareout@shareout
```

The plugin includes the hosted MCP connection and a short publishing skill. Connect your Shareout account through the host's OAuth flow. In Claude web or desktop, you can also add `https://shareout.io/mcp` as a custom connector where your plan supports it.

## Codex

```sh
codex plugin marketplace add geland/shareout-integrations
codex plugin add shareout@shareout
```

For an MCP-only connection, merge [configs/codex.toml](configs/codex.toml) into your Codex configuration and run `codex mcp login shareout`. This repository is a community-installable source; it does not imply approval in the public ChatGPT/Codex directory.

## Gemini CLI

```sh
gemini extensions install https://github.com/geland/shareout-integrations
```

The extension bundles the hosted MCP connection and the Shareout skill. Start Gemini and run `/mcp auth shareout` to connect your account. The skill loads workflow details only when needed. Gemini uses `httpUrl` for Streamable HTTP; this repository supplies the host-specific manifest.

## Cline

```sh
cline skill install geland/shareout-integrations --skill shareout
cline mcp install shareout --transport http https://shareout.io/mcp
```

The skill and MCP connection are separate installations. Complete Shareout sign-in in Cline before using hosted tools, or use the standalone CLI for local files. Marketplace review is separate from direct installation.

## Skills CLI / skills.sh

```sh
npx skills add geland/shareout-integrations --skill shareout
```

Choose your agent when prompted, or add `--agent cline` (or another supported agent). Try asking: “Publish this HTML proposal with a private review link,” or “Update this Shareout page while keeping its link.” This installs the skill; connect the MCP separately or use the CLI. Avoid installing the same skill again if your plugin already supplies it. skills.sh discovers skills through its CLI's install telemetry; a repository does not imply a directory ranking or listing.

## OpenCode

Merge [configs/opencode.json](configs/opencode.json) into your `opencode.json`, preserving existing settings. Then:

```sh
opencode mcp auth shareout
```

Install the skill with the Skills CLI if desired. OpenCode uses `mcp`, while other clients may use `mcpServers`; the files are deliberately separate.

## Cursor and VS Code / GitHub Copilot

Cursor accepts the portable Agent Plugins package in this repository. For an MCP-only connection, merge [configs/cursor.json](configs/cursor.json) into `.cursor/mcp.json`.

VS Code accepts the repository's [.mcp.json](.mcp.json) at your project root. [configs/vscode.json](configs/vscode.json) provides the legacy `.vscode/mcp.json` form. Start the server from the MCP settings and connect your account. These are connection configurations, not claims of curated marketplace acceptance.

## Local CLI and MCP

The standalone CLI reads files directly from disk. Get it from [Shareout Downloads](https://shareout.io/download), then connect it using **Connect your agent** in the Shareout console. No Node, npm, or Go runtime is required for the CLI.

```sh
shareout doctor --json
shareout mcp
```

[configs/stdio.json](configs/stdio.json) is a reference for hosts using `mcpServers`. Use the executable's full path if your desktop app cannot find `shareout`. Prefer either a local or hosted MCP connection for a task, rather than enabling both.

## What the host needs

- A Shareout account. Signup requires email; an owner-issued setup link lets a local agent connect without its own inbox.
- Hosted MCP uses OAuth with PKCE, or an existing API key passed privately as a bearer header.
- **Hosted publishing accepts native ChatGPT HTML attachments or direct HTTP file transfer.** With a native `file` reference, Shareout retrieves one self-contained HTML attachment as index.html; publish only after ready=true. Other hosts and multi-file bundles use the short-lived HTTP upload handoff. A host with neither capability can still read and manage documents; use local MCP or the CLI to publish.
- Document bytes never go in MCP arguments. Eight tools expose compact, paginated results. The skill does not repeat their schemas or load every template.
- Use self-contained HTML and relative assets. See the [authoring rules](https://shareout.io/guidelines.md).

## Support

Shareout is published by [Greg Eland](https://gregeland.com). For account or service help, email [hello@gregeland.com](mailto:hello@gregeland.com). For plugin installation issues, you can also [open an issue](https://github.com/geland/shareout-integrations/issues).

Never post API keys, private documents, or bearer links in a public issue. Describe the problem and include a redacted error message when available.

See [Privacy](https://shareout.io/privacy), [Terms](https://shareout.io/terms), and [Support](https://shareout.io/support).

## Package development

Run `python3 scripts/validate.py` with `jsonschema` and `PyYAML` installed, and `claude plugin validate .claude-plugin/plugin.json --strict` when Claude Code is available. Build the review ZIP with `python3 scripts/package.py`; it uses an explicit file allowlist. Generated ZIPs live in ignored `dist/`.

The MIT license covers these integration files. It does not license the hosted service, grant rights to the Shareout name or marks, or change the service's terms. Report packaging issues through this repository; never include API keys, private documents, or bearer links in an issue.

## MCP/CLI 0.7.0 and plugin 0.2.0

The endpoint stays `https://shareout.io/mcp`. Refresh tool discovery in an existing host after the service release; update the installed skill/plugin or Gemini extension through that host. Eighteen separate operations replace grouped catalog, document, link, comment and version tools. Local MCP uses standalone CLI 0.7.0. Old hosted calls remain compatible during migration. OpenAI publication is a separate owner action.
