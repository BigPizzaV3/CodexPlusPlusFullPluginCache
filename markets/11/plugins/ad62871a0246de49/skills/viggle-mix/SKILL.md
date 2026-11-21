---
name: viggle-mix
description: Create a character-motion Mix with Viggle, browse official Viggle motions, or check, recover and download an existing Mix. Use when a user wants a person, creature, avatar, illustration, or other character to reproduce motion from a driving video or an official Viggle motion. Do not use for generic text-to-video tasks without both character and motion intent.
---

# Viggle Mix

A Mix is `viggle_prepare_mix` → upload → `viggle_create_mix` →
`viggle_wait_mix`. The tool descriptions carry the details; this skill covers
what only the host can decide.

## Follow next_action

Every Viggle result carries `next_action`. Call its `tool`, honour its
`retry_after_ms`, and relay its `message` to the user as given. The server owns
every account, plan, quota, limit and error rule, and its wording changes with
the product; do not restate those rules from memory or infer state from prose.

## Account and secrets

Let the host run Viggle OAuth. Never ask for, create, store or print an API
key, access token, refresh token, cookie or authorization header: each one is
a credential for the user's account.

## client_context

Send `client_context` with every Viggle tool call so the server can tell an
outdated plugin:

```json
{ "client_context": { "host": "<actual client id, e.g. claude-code>", "plugin_version": "1.0.0" } }
```

If a result carries `client_update`, tell the user an update is available. Run
its `install_command` only in a host that can run a shell, and only after the
user agrees: it installs software on their machine.

## Choose the source

Take the first that applies, for the character and for the motion:

1. The host has put a chat attachment into `character_file` / `motion_file`:
   pass that object as given. Never build a `file_id` yourself.
2. The host can read a file the user named and make HTTPS PUT requests: follow
   [references/local-file-upload.md](references/local-file-upload.md).
3. The user gave a Viggle asset ID, or picked an official Viggle motion: pass
   it as `viggle_asset_id` or `official_motion_id`.
4. Otherwise explain that this host cannot send the file, and suggest a host
   that can attach files or read local ones.

Use only files the user supplied or authorized. Never put a local path, raw
bytes or base64 in MCP arguments: the server is remote and cannot read them.
