# Aqua Voice for Codex

This package connects Codex to Aqua's existing remote MCP server. It contains
no credentials or local server. The portable `plugin.json` and `mcp.json`
describe the Codex package. The Claude files remain available for Claude Code.

## Test locally

The repo marketplace is `.agents/plugins/marketplace.json`. Its plugin path
resolves from the repo root to `plugins/aqua`.

1. Register the repo root with `codex plugin marketplace add`, as shown below.
   Check that `codex plugin marketplace list` includes `aqua-voice`.
2. Open the Plugins Directory and select the Aqua Voice marketplace. Restart
   the desktop app if the new marketplace is not visible.
3. Install Aqua and complete the Aqua account connection. You can also install
   the local package with `codex plugin add aqua@aqua-voice`.
4. Start a new chat. Ask: "Call aqua_get_me and show my connected account
   and permissions."
5. Check the email, `credential.scopes`, and `history_available` before
   reading history or making changes.

Use a working Codex CLI to register the repo root:

```sh
codex plugin marketplace add /absolute/path/to/aqua-ai
codex plugin marketplace list
codex plugin list --marketplace aqua-voice --available --json
```

If the shell's `codex` command fails because its binary is missing, the macOS
ChatGPT app also bundles a CLI at
`/Applications/ChatGPT.app/Contents/Resources/codex-cli/CodexCLI.app/Contents/MacOS/codex`.
Use that executable when it exists. Registration and installation are separate
from completing the account connection.

The desktop app loads an installed copy of the plugin. Refresh the local
installation after package changes, then test in a new chat.

## Check the connection

Try these requests with an account that has stored history:

- "Find my recent Aqua meetings."
- "Summarize this Aqua meeting and list action items: [meeting link]."
- "Find my five most recent dictations about the release plan."
- "Show the complete transcript for the dictation I selected."
- "Show my Aqua dictionary and text replacements."

Then request one explicit write, such as adding a dictionary word. Check
the consent screen and the returned state. A read-only token needs additional
permission for writes. Test reconnect and token refresh before distribution.

The server instructs the assistant to send feedback when the user reports a
transcription error or asks to rate a dictation. Feedback stores a correction
in Aqua; it does not edit text already inserted in another app.

Test the store review account separately. Its setup and reset steps are in
[Aqua MCP](../../docs/mcp.md#store-review-account).

## Add workflows later

The package uses the tools available to the connected Aqua account. Add skills under
`skills/<name>/SKILL.md` when a task needs a repeatable procedure, such as
turning a dictation into a project brief or updating a dictionary from
confirmed transcription errors. Skills do not add server capabilities.

## References

- [Package a plugin](https://developers.openai.com/plugins/build/plugins)
- [Submit a plugin](https://developers.openai.com/plugins/deploy/submission)
- [Aqua MCP](../../docs/mcp.md)
