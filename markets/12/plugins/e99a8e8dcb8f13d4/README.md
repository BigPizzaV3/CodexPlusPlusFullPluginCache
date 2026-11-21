# Vibe Coding Control — Remote MCP

[First project guide](https://vibecodingcontrol.com/how-it-works#first-project) ·
[Первый проект](https://vibecodingcontrol.com/ru/how-it-works#first-project) ·
[English / Русский: prompts and listing copy](LOCALIZATION.md)

Connect your VCC account to read your own projects, tasks and development history,
record factual work, and request or retrieve owner decisions.

- Website: https://vibecodingcontrol.com
- Remote MCP: **https://vibecodingcontrol.com/mcp**
- [Support](SUPPORT.md) · [Privacy](https://vibecodingcontrol.com/privacy#en) · [Terms](https://vibecodingcontrol.com/terms#en)

This repository contains distribution manifests, connection examples and the
`vcc-get-started` and `vcc-workflow` skills.
An account is required. Use normal VCC sign-in (Google or email/password) and OAuth consent;
there are no tokens to copy and no server to install. Remote access includes your
own current and future VCC projects. Revoke an application at
https://vibecodingcontrol.com/mcp/connections.

## Connect

[Add to Cursor](https://cursor.com/link/mcp/install?name=vcc-remote&config=eyJ1cmwiOiJodHRwczovL3ZpYmVjb2Rpbmdjb250cm9sLmNvbS9tY3AifQ%3D%3D) · [Add to VS Code](vscode:mcp/install?%7B%22name%22%3A%22vcc-remote%22%2C%22type%22%3A%22http%22%2C%22url%22%3A%22https%3A%2F%2Fvibecodingcontrol.com%2Fmcp%22%7D)

These official install links open the editor confirmation and then the normal
OAuth sign-in. If your Markdown viewer blocks editor links, use the steps below.
Native editor installation of these links is not yet verified for this release.

| Platform | Supported connection |
|---|---|
| VS Code | MCP: Add Server → HTTP → enter the MCP URL → sign in. See `connections/vscode.json` for the equivalent configuration. |
| Cursor | Add the URL under MCP settings and complete OAuth, or install this Agent Plugins package when the public marketplace listing is approved. |
| Claude | Install from the [Claude directory](https://claude.ai/directory/vibe-coding-control) (published Community connector), or Settings → Connectors → Add custom connector → enter the MCP URL → Connect and sign in. |
| ChatGPT | Install the [VCC plugin](https://chatgpt.com/plugins/plugin_asdk_app_6ad07aa9d4588191870168df2355d42b), authorize your VCC account and select VCC in a Work chat. |
| Codex | Find Vibe Coding Control in Plugins, or use the commands below for a remote CLI connection. For work with local files, connect the project folder through VCC Connector. |
| Windsurf / Devin Desktop | Cascade: add the entry in `connections/cascade.json` to the existing MCP config, then complete OAuth. Devin Local: `devin mcp add -s user vcc-remote https://vibecodingcontrol.com/mcp`, then `devin mcp login vcc-remote`. Cascade has no MCP marketplace or one-click install. |

```sh
codex mcp add vcc-remote --url https://vibecodingcontrol.com/mcp
codex mcp login vcc-remote --oauth-client-registration dcr
```

```sh
claude mcp add --transport http --scope user vcc-remote https://vibecodingcontrol.com/mcp
```

In Claude Code, open `/mcp` and complete authentication. Client UI availability
depends on the plan, workspace permissions and product version. Merge examples
into existing configuration; preserve all other servers and the local `vcc` entry.

Ask “How do I get started with VCC?” for help. If you already have a VCC project,
ask “Show my VCC projects”, choose one, and ask “What is happening in my VCC project?”
Reuse existing task/run IDs and one stable idempotency key for each write and retry.

## Scope and review

Remote VCC cannot read local files, execute shell commands, verify Git or deploy.
Those local workflows require the existing installed VCC Connector. Agents cannot
approve owner gates: decisions remain on the VCC website and are bound to the
specific run and result. Receiving a decision does not execute the approved action.

`plugin.json` and `mcp.json` use Agent Plugins 1.0.0, supported by Cursor and
the common OpenAI directory. Both products use the same remote service.
There are no embedded credentials, app references or lifecycle hooks.
`server.json` is the official MCP Registry submission descriptor.

[Review scenarios and recording guide](REVIEW.md). The 0.1.4 source candidate adds
the setup skill and new starter prompts. Existing catalog listings remain on their
published versions until the updates are submitted and approved.
