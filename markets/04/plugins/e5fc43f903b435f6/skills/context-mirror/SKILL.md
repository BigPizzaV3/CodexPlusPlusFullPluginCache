---
name: context-mirror
description: Create, update, pull, and push Camber Context Mirror agents from local coding workspaces.
---

# Context Mirror

Use this skill when the user asks to:
- mirror a local workspace into a Camber agent
- refresh an existing mirrored Camber agent
- migrate local assistant skills into Camber skills
- pull a Camber agent mirror back to local
- push local mirror changes back to Camber

## Resource map

Read only the resources needed for the current branch:

| Resource | Use when |
|---|---|
| `resources/create-update.md` | Creating or updating a workspace-mirroring agent |
| `resources/layout.md` | Explaining or validating mirror folder layout |
| `resources/pull-push.md` | Pulling an agent locally, or init -> export chat -> edit `sync.yaml` -> push |
| `resources/claude-code-chat-export.md` | Exporting Claude Code chat into the mirror |
| `resources/cursor-chat-export.md` | Exporting Cursor chat into the mirror |
| `resources/troubleshooting.md` | Debugging common mirror failures |

## Core rules

- Verify `$ camber me` before relying on the CLI.
- Inspect before writing: README/docs, project tree, manifests, entrypoints, configs, tests, commands, and local assistant context.
- If the workspace uses the Snowflake CLI, `instruction.md` must tell the agent to use `camber.snowflake` instead — never the local CLI.
- Stop for user approval before any write action: context init, pull, or push (and `$ camber agent update` when refreshing an existing agent).
- Collect every confirmation through the client's interactive question tool — `AskQuestion` in Cursor, `AskUserQuestion` in Claude Code. Do not substitute plain chat text. **Wait for the user's answer before every next step** — an unanswered question is a hard stop.
- If the requested agent already exists, update it instead of creating a duplicate. For a **new** mirror, do **not** call `agents_create` or `$ camber agent create` first — leave `agent:` blank in `.camber/sync.yaml` and let the first `$ camber agent push` create the remote agent.
- `README.md` is one source of evidence, not the whole workspace context.
- Avoid `.git`, `.env*`, and virtualenvs unless the user explicitly approves.
- Project files are mirror files only. Never add project files to Knowledge Base.
- Skills become Camber skill records. Never add `SKILL.md` or skill scripts to Knowledge Base.
- Skill `references/` files are the only skill files indexed as Knowledge Base.
- The current chat is required mirror context when syncing: export after `context init`, then wire paths through `.camber/sync.yaml` before push.
- Never push skills, project files, chat, instruction, or other mirror sections with separate CLI commands (`skill compile`, `context add`, `stash cp`). Use `context init` -> export chat (if required) -> edit `sync.yaml` -> `push`.
- During a mirror operation, only write under `.camber/`: `sync.yaml` (from `$ camber agent context init` plus placeholder edits), `instruction.md`, and `chats/`. Use **relative paths** in `sync.yaml` (for example `.camber/instruction.md`, `.camber/chats`). Add `.camber/**` to top-level `exclude` so staging files are not uploaded as project files. Remove `.camber/instruction.md` and `.camber/chats/` after a successful `push`; keep `sync.yaml`.
- Prefer `$ camber agent context init` over hand-writing `.camber/sync.yaml`. Run `context init` and `push` from the project root (fresh mirror) or from the pulled mirror root.

## Fast path

1. Verify auth:
   ```bash
   $ camber me
   ```
2. Inspect workspace and assistant context.
3. List existing agents and decide create vs update.
4. Ask the user to confirm the plan through the client's interactive question prompts — never plain chat text. **Wait for answers before continuing.**
5. Initialize the local sync config, draft `instruction.md`, export chat if needed, fill `.camber/sync.yaml` (leave `agent:` blank on first push), then push. For an existing agent only, set `agent:` to the known id or run `$ camber agent update` when instructions changed.
6. After a successful push, remove `.camber/instruction.md` and `.camber/chats/` staging files.
7. Double-check the result before telling the user the mirror is complete.

For the full create/update workflow, read `resources/create-update.md`.
