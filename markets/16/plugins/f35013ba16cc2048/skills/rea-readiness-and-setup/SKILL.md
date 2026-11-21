---
name: rea-readiness-and-setup
description: Diagnose whether REA is available in the current agent and explain its setup prerequisites; use when REA tools are missing, stale, or the user asks how to connect a supported client.
---

# REA readiness and setup

Do not install software or alter agent configuration just because a workflow is requested.

1. Check whether the active conversation already exposes REA tools. If yes, inspect its actual tool names and schemas; proceed without running a doctor command.
2. If unavailable and the user wants local setup, first explain the host requirements. Upstream currently specifies Node.js 22.19+, 24.11+, or 26+ and npm. Native analysis can additionally require a user-installed Hopper, Ghidra, or IDA; Android and firmware routes have separate prerequisites. Static JavaScript/.NET analysis may not require a native engine.
3. Offer read-only diagnosis for a confirmed client, e.g. `npx -y rea-agents@latest doctor --client codex --json`. Use the client's documented identifier, not an assumed one.
4. If configuration repair is needed, first prepare and show a dry-run plan, e.g. `npx -y rea-agents@latest setup --client codex --dry-run --json`. Review exact paths, backups, changes, and any bundled skill replacement before applying.
5. Obtain explicit approval before a setup command writes agent configuration or installs an engine. Add `--install-hopper` only if separately necessary and specifically approved. Do not install/upgrade Node, npm, Java, Ghidra, IDA, JADX, Binwalk, or Unblob as an automatic repair.
6. After approved setup, ask the user to restart/reconnect the affected client and verify the tools actually appear. A matching config file alone does not prove an active connection.

For a JavaScript app tree or ASAR, an upstream CLI fallback is `npx -y rea-agents@latest analyze-javascript-application /absolute/path/to/app --json`; this needs no MCP registration or native engine. Explain that running `npx` downloads/executes a package and should be reviewed as such. Do not run it yourself unless explicitly requested and the environment/action is authorized.

Never paste secrets, private paths, proprietary binaries, crash dumps, or private analysis projects into public issues. Upstream asks for vulnerabilities to be reported privately through its Security tab.
