# Emploive plugin

This folder is the Emploive plugin for ChatGPT and Codex, and a Claude Code plugin. It bundles:

- `mcp.json`: the remote MCP server at `https://api.emploive.com/mcp`. The server code is in `packages/backend/src/mcp`.
- `skills/`: three skills. `find-jobs` searches, `job-alerts` creates and changes trackers, and `review-tracker-matches` catches up on tracker jobs.
- `assets/`: the E mark as the logo and the composer icon.
- `plugin.json`: the portable manifest, with the ChatGPT display details under `extensions["com.openai"].interface`.
- `.claude-plugin/plugin.json` and `.mcp.json`: the same plugin for Claude Code.

The views (the job card and the Emploive sidebar app) and MCP Events come from the MCP server, so the plugin needs no files for them.

## Test in ChatGPT

1. In ChatGPT, open **Plugins**, select **Add**, then **Upload plugin archive**.
2. Upload a zip of this folder: `cd plugins && zip -r emploive.zip emploive`.
3. Search without an account. When you ask for alerts, ChatGPT shows the Emploive sign-in.

To test the MCP server alone, select **Create MCP App** instead and enter the server URL with OAuth.

## Test in Claude Code

```sh
claude plugin marketplace add ./plugins
claude plugin install emploive
```

## Submit

Submit through the OpenAI plugin submission portal. Prepare:

- A verified developer identity for the account that submits.
- The domain token at `https://api.emploive.com/.well-known/openai-apps-challenge`.
- Five positive and three negative test prompts, with expected results.
- A reviewer account that signs in with a password, with no email code, and has sample trackers.
- A privacy policy that names data categories, purposes, recipients, retention, and user controls.

Do not add plan prices or upgrade prompts to the skills, the tool text, or the views. OpenAI's plugin guidelines forbid them. See "Plans and upgrades" in `packages/backend/src/mcp/README.md`.
