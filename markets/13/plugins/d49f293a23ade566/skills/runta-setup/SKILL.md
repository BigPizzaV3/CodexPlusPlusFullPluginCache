---
name: runta-setup
description: Install the Runta CLI and sign in to Runta. Use before any Runta runtime task when the `runta` command is missing, a Runta command reports `MISSING_TOKEN` or `AUTH`, or the user asks to connect, log in to, or switch Runta environments.
---

# Runta setup

If the Runta MCP tools are connected, call `whoami`. When it returns the
user's account, setup is complete and the CLI is not needed. When the client
asks the user to sign in to Runta, let the user finish that browser sign-in;
never ask for a token in the chat.

Without the MCP tools, Runta runtime tasks run through the `runta` CLI.
Confirm it is installed and signed in before doing anything else.

## 1. Check the CLI

```bash
runta --version
```

If the command is not found, install the CLI and check again:

```bash
npm install -g @runta/runta-cli
```

Do not install the CLI any other way unless the user asks.

## 2. Check authentication

```bash
runta ps --json
```

- `{"action": "ps", "runtimes": [...]}` means the CLI is signed in. Stop here.
- `error.code` of `MISSING_TOKEN`, `AUTH`, or `UNAUTHENTICATED` means the CLI
  needs to sign in. Continue to step 3.
- `error.code` of `TRANSPORT` or `INVALID_ENDPOINT`, or an `SDK` error whose
  message starts with `http error`, means the API is unreachable or
  misconfigured. Show the user the message and the current `RUNTA_ENDPOINT`
  value, if set. Do not try to sign in.

## 3. Sign in

Prefer the browser device flow. It never exposes a secret in the conversation.

```bash
runta login --no-wait --json
```

The output has `status: "authorization_pending"`, a `user_code`, and a
`verification_uri_complete`. Give the user the link and the code, and ask them
to approve the request in their browser. Then wait for approval:

```bash
runta login --resume --wait --json
```

Run `runta ps --json` again to confirm sign-in worked.

If the user already has an API key, they can set `RUNTA_TOKEN` in the
environment instead. Never ask the user to paste an API key into the chat, and
never print, log, or store the value of `RUNTA_TOKEN`.

## Environments

The CLI talks to production by default. To target another environment, the
user sets `RUNTA_ENDPOINT` to that API base URL, for example
`http://127.0.0.1:8080` for the local development stack. Only change
`RUNTA_ENDPOINT` when the user asks.
