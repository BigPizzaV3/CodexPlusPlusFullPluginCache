# Firmory for Codex

[Illustrated installation guide](https://firmory.ai/download#codex) · [Releases](https://github.com/DepsilonAI/firmory-plugins/releases)

1. Install Codex with plugin support and sign in to your account.
2. Open **Customize → Plugins** in Codex. Drag `firmory-1.1.4-codex.zip` into that page and follow the installation prompts. Keep the ZIP compressed; no extraction is needed.
3. Connect Firmory in your client's MCP settings. If needed, run this in the terminal.

```sh
codex -c 'mcp_servers.firmory_cloud.url="https://firmory.ai/mcp"' mcp login firmory_cloud --scopes user:org:read --oauth-client-registration cimd
```

4. In the browser, sign in to Firmory, select your team and allow access. Ask "Show me the projects and files available in my workspace". Firmory verifies the team while answering; no separate setup question is needed.
5. Ask a first question.

- Show me the projects and files available in my workspace
- Find the project brief and summarize its goals and key decisions
- Open "Welcome.pdf" and summarize its key points

## Install the production plugin from GitHub instead

For Codex CLI installation, run these commands in any folder. These install the production plugin from GitHub. To keep this ZIP's environment, use the ZIP instructions above.

```sh
codex plugin marketplace add DepsilonAI/firmory-plugins
codex plugin add firmory@firmory-plugins
```

This ZIP connects to https://firmory.ai/mcp using browser sign-in. It can read the files your team permits and save changes when you ask. [Privacy](https://firmory.ai/privacy) · [Terms](https://firmory.ai/terms).

## Sync reminders

Local installers include a file-edit hook. Enable and trust the hook when your client asks; Python 3 must be available. When new file changes are discovered, including manual edits found during inspection, Firmory offers Sync now, Enable automatic sync, or Not this time, remind me next time using available host choices at task completion. Deferring reminds once when you next edit or inspect those pending files; ordinary unchanged reads do not repeatedly prompt. "Edit locally first" skips the sync question and upload. Preferences support asking after changes, explicitly authorized automatic sync of linked files, or manual sync only, scoped to the current user/team/project/local workspace. Local clients can remember the mode when requested; web clients without persistent preferences keep it in the current conversation. Automatic mode handles future observed edits, not background syncing, and never silently overwrites conflicts. Hooks cannot watch arbitrary shell commands or external editors; web plugins cannot watch local files.
