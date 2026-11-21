# Aqua for Claude Code

For the Codex package and local marketplace, see [Aqua Voice for Codex](CODEX.md).

Find your Aqua meetings and dictations, read notes and transcripts, and manage
customizations through Aqua's remote MCP server. Meeting features require
Meetings access on your Aqua account and respect Aqua access permissions.

Local installation and removal have been tested with Claude Code 2.1.215.
Public repository and marketplace publication are pending.

## Install

Use Claude Code and an Aqua account. From this directory (`plugins/aqua` in
the Aqua repository, or a copy of this directory), run:

```sh
claude plugin marketplace add ./
claude plugin install aqua@aqua-voice
```

Start a new Claude Code session. The package connects to
`https://api.aquavoice.com/mcp` over HTTP. It contains no credentials or local
server.

## Connect your account

Open `/mcp`, select Aqua, and select **Authenticate**. Check the permissions
in the consent screen; manual authentication can request write access on the
first connection. Do not assume that initial access is read-only.

After sign-in, ask Claude: "Call `aqua_get_me` and show which Aqua account and
permissions are connected." Confirm the returned `email` and inspect
`credential.scopes`. If `history_available` is false, stored session history
is unavailable through this connection.

A write call with a read-only token requires additional permission. The
complete sign-in, permission upgrade, and refresh flows still need validation.

## Try it

- "Find my recent Aqua meetings."
- "Summarize this Aqua meeting and list action items: [meeting link]."
- "Find my five most recent dictations about the release plan."
- "Show the complete transcript for the dictation I selected."
- "For this dictation, send negative feedback: replace 'Base Ten' with
  'Baseten' in the corrected text. Keep the rest of the text unchanged."

These examples require a working account connection. The last example
requests a write through `aqua_send_session_feedback`. It stores feedback and corrected text in Aqua;
it does not edit text already inserted into another app. The server tells
Claude to send feedback only when you report a transcription error or ask to
rate a dictation.

## Remove

Before uninstalling, open `/mcp`, select Aqua, and clear its authentication
if you connected an account. Package removal alone does not clear stored
OAuth credentials.

```sh
claude plugin uninstall aqua@aqua-voice
claude plugin marketplace remove aqua-voice
```

## Validate the package

From the package directory:

```sh
claude plugin validate .
claude plugin validate .claude-plugin/plugin.json --strict
claude plugin validate .claude-plugin/marketplace.json --strict
python3 -m json.tool .claude-plugin/plugin.json > /dev/null
python3 -m json.tool .claude-plugin/marketplace.json > /dev/null
python3 -m json.tool .mcp.json > /dev/null
```

For an isolated install check, set `CLAUDE_CONFIG_DIR` to a new temporary
directory before running the install and remove commands. This keeps the
check separate from your normal Claude settings.

See the Claude Code [plugin reference](https://code.claude.com/docs/en/plugins-reference),
[marketplace guide](https://code.claude.com/docs/en/plugin-marketplaces), and
[MCP authentication guide](https://code.claude.com/docs/en/mcp#authenticate-with-remote-mcp-servers).
