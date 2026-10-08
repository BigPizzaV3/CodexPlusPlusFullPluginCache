# Devpost Hackathons — Setup

These skills rely on one MCP server, `devpost` (`https://devpost.com/mcp`), which supplies
official hackathon data (overview, key dates, rules, submission requirements, judging
criteria) and performs the authenticated actions (register, create/update project, submit).
Authentication is OAuth via `https://auth-devpost.com`.

## Server connection

- **ChatGPT**: the Devpost Hackathons app connection provides the server automatically —
  no action needed beyond connecting the app and signing in when prompted.
- **Codex CLI** (or any MCP-capable host without the app connection), add it once:

```
codex mcp add devpost --url https://devpost.com/mcp
```

Then restart Codex.

To sign in (or re-authenticate) explicitly:

```
codex mcp login devpost
```

This opens the Devpost sign-in page. Restart Codex afterward — the running session cannot
see newly stored credentials.

## Note for skill authors

Server setup is a one-time, human-facing concern and lives here on purpose. Skills must not
walk a participant through registration, re-authentication, or restarts during a normal turn —
see **Devpost MCP Server** in `skills/PLUGIN_RUNTIME.md` for the degrade-don't-troubleshoot
contract.
