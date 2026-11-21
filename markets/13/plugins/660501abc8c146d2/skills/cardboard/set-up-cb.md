# Set up cb on this Mac

Read this when a task needs `cb`, running it failed because it is not installed, and you have no `cardboard` tools. Each
command you run may need the person's approval, so run no other check first.

First ask the person. Say that Cardboard's command-line tool, `cb`, needs to be installed on their Mac (into
`~/.cardboard`, about 200 MB to download, no admin password), and wait for a yes. Then follow the one case below that
matches the tools you have.

## Your shell runs on this Mac (Claude Code, and Codex or Work in the ChatGPT app)

Run only the installer, once. A sandbox blocks both its download and its write to `~/.cardboard`, so do not try it
sandboxed first:

- **Claude Code:** run `curl -fsSL https://assets.cardboard.ai/cb/install.sh | sh`. If your shell is sandboxed, run this
  one command with the sandbox off (`dangerouslyDisableSandbox: true`).
- **Codex or Work:** run `curl -fsSL https://assets.cardboard.ai/cb/install.sh | sh -s -- --codex` with
  `sandbox_permissions: "require_escalated"` and the justification "Install Cardboard's cb into ~/.cardboard and add it
  to Codex's MCP servers". `--codex` also registers `cb mcp` as Codex's `cardboard` MCP server. If Codex refuses the
  escalation, make one `request_permissions` call for network access (`network: { enabled: true }`) and write access to
  `~/.cardboard`, `~/.codex` and `~/.local/bin`, with the same reason, then run the same command without escalation.

The person approves the command once. The installer checks the new `cb` itself and prints its version, so do not check
or inspect the install afterwards. If it says a step failed, tell the person what it said. Running it again is safe.

Afterwards:

- **Claude Code:** carry on with the task. If `cb` is not on `PATH`, call `~/.cardboard/bin/cb` wherever these
  instructions say `cb`.
- **Codex or Work:** tell the person to start a new chat. The `cardboard` tools appear there and run outside the
  sandbox. Do not continue with `cb` in this chat: every command that changes a project would need its own approval.

`cb` keeps itself up to date, so never run the installer to update it.

## You cannot run commands on this Mac (the Claude app)

A code sandbox in the cloud is not the person's Mac, so do not install anything there. Ask the person to install
Cardboard's desktop extension once:

1. Download https://assets.cardboard.ai/cb/cardboard.mcpb.
2. Open the downloaded file. Claude shows the Cardboard extension.
3. Click **Install**.

The extension's first start installs `cb` into `~/.cardboard`. After that, Claude has the `cardboard` tools, which run
`cb` on the Mac, and Claude asks the person once the first time one runs. Ask the person to tell you when the extension
is installed, then check that you have the `cardboard` tools. If you do not, ask them to start a new chat.
