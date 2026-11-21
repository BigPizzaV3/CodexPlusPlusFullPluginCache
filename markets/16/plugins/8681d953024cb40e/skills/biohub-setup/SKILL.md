---
name: biohub-setup
description: Connect and sign in to the Biohub MCP that every Biohub skill uses, and fix connection, sign-in, permission, or credit problems. Use when the Biohub tools are missing from the catalog, a tool returns an authentication or permission error, or the user asks how to install or set up Biohub. Never ask for secret values.
license: MIT
---

# Biohub setup

The user's instructions take precedence over guidelines provided in a skill.
If explicit user instructions conflict with a skill's instructions, prioritize the user's instructions.

Every Biohub skill runs on one remote server, the Biohub MCP at `https://biohub.ai/mcp`.
It needs no API key, no local Python, and no other install. The user signs in to Biohub once, in the browser, through the host.
The plugin declares the server in `.mcp.json` as `biohub`, so a plugin install adds it.

## Check the connection

The Biohub MCP is connected and signed in when the tool catalog lists, with or without a host prefix:

- `ui_show_structure` and the `esm_atlas_*` tools, for Atlas lookups and structure views;
- `esmfold2_fold_complex`, `esmfold2_fold_max_accuracy`, and `biohub_get_inference_run`, for folding;
- `esmc_score_mutations` and `esmc_scan_mutation_tolerance`, for ESMC.

If the tools are missing, the server is either not added or not signed in.

## Add the server

Give the user the one command for their host, because it changes their host configuration; never run it yourself:

- Claude Code: `claude mcp add --transport http biohub https://biohub.ai/mcp`
- Codex: `codex mcp add biohub --url https://biohub.ai/mcp`
- Any other host: add a streamable HTTP server at `https://biohub.ai/mcp` that signs in with OAuth.

## Sign in

- Claude Code: run `/mcp`, choose `biohub`, and choose to authenticate.
- Codex: run `codex mcp login biohub`.
- Any other host: use its connect or sign-in button for the server.

The host opens a Biohub sign-in page in the browser. The user signs in, or creates a free account at <https://biohub.ai>, and approves access.
The host may need to reload its MCP servers before the tools appear; then resume the original request on the user's next message.
Resume only the steps that did not run: when an analysis finished and only its structure view failed, make only that view call.

## Fix errors

- Sign-in expired, or a `401`: sign in again as above.
- A `403` naming the app: Biohub does not accept that client; connect with a supported app, such as Claude Code or Codex.
- A `403` about the account: quote the message, which says what access the account needs.
- A `503` saying sign-in could not be checked: try again shortly; the sign-in is not lost.
- Out of credits: point to <https://biohub.ai/developer-console> for the account's credits, and never invent a quota.
- A call the host blocks, for example by denying approval, is a tool failure, not a missing connection or sign-in.

Never ask the user to paste a password, token, or key in the chat, and never print or store one.
