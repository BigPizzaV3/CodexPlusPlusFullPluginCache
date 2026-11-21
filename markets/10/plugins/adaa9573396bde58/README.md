# nambli 0.3.2

nambli connects a private calendar account to a hosted MCP server and an explicitly invoked skill. Find and create events, prepare typed platform drafts, move appointments, and manage named File fields. Calendar writes never publish or schedule social posts.

Install the plugin in a supported host, complete browser sign-in and consent when prompted, and choose the intended account. Invoke `$nambli` in Codex; in Claude Code use `/tor-event-calendar-ai:nambli`. The skill verifies the selected account before private work. Adding another account uses the host plugin's Apps and Connected accounts controls when available and preserves existing connections.

The ordinary plugin connection is `https://nambli.com/mcp`; no local runtime or user-supplied API token is needed. The portable `plugin.json` and `mcp.json` are accompanied by Codex and Claude compatibility manifests. The technical package identity remains `tor-event-calendar-ai`; the display name, MCP server and skill are `nambli`.

See the [skill](skills/nambli/SKILL.md), [connection guidance](skills/nambli/references/connections.md), [MCP guide](skills/nambli/references/mcp.md), and [file workflow](skills/nambli/references/files.md). File links and metadata alone do not prove delivered bytes. A saved draft is not an active publisher or automatic publishing setup.

Advanced users may explicitly choose the included local CLI source. It requires Node 22.18+ and an OS keychain for local account credentials. From this directory, install pinned dependencies with `npm ci --ignore-scripts`, inspect `node src/cli.mjs version` and `node src/cli.mjs help`, then follow the connection guidance. CLI pairing is separate from the remote plugin's OAuth connection.

This archive is a public-upload preparation, not an approved or published store release. Review cases and release notes are carried in the root manifest. Preparation evidence and exact-version portal checks are tracked separately from this package.

[Website](https://nambli.com) · [Support](https://github.com/Tor-Production/tor-event-calendar-ai/issues) · [Privacy](https://nambli.com/privacy) · [Terms](https://nambli.com/terms) · [Recorded walkthrough](https://nambli.com/demo)

Publisher: Tor Production. The original owner-provided blue/purple artwork is retained unchanged. The proprietary Nambli font is not included.
