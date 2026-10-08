# Pull And Push

## Pull an agent mirror locally

Use pull when the user wants to restore an existing Camber agent mirror into the local directory where they are standing.

Confirm the target agent tag and destination parent folder via the client's interactive question tool (`AskQuestion` in Cursor, `AskUserQuestion` in Claude Code) before running pull.

Claude Code:

```bash
$ camber agent pull @owner.alias --integrate claude-code
```

Cursor:

```bash
$ camber agent pull @owner.alias --integrate cursor
```

Rules:
- Pull writes into `project_<owner>_<agent-alias>/` under the current directory by default.
- Use `--dest <parent-dir>` only when the user wants a different parent folder.
- Mirror files are restored directly under that pulled folder: `.camber/sync.yaml`, `README.md`, `chat/`, `knowledge-base/`, `project/`, `requirements/`, `schema/`, and `instruction.md`.
- Cloud `skills/` is not restored as a root `skills/` folder.
- Claude Code pull creates `.claude/agents/<owner>.<agent-alias>.md` and `.claude/skills/<skill-name>/`.
- Cursor pull creates `.cursor/rules/camber-agent-<agent-alias>.mdc` and `.cursor/skills/<skill-name>/`.
- Pull hard-replaces pulled/generated local paths.

## Unified local -> Camber sync flow (create, refresh, or push)

Run `context init` and `push` from the **project root** (fresh mirror) or from the **pulled mirror root** that contains `.camber/sync.yaml`.

1. Initialize sync config on the user's machine:
   ```bash
   $ camber agent context init
   ```
   This creates `.camber/sync.yaml` with placeholders.
2. Export chat if required (current chat and any approved historical chats), using the connected client chat-export resource. Write exports to `.camber/chats/`.
3. Draft `instruction.md` to `.camber/instruction.md`. Review `.camber/sync.yaml` and replace placeholders with values that match the local directory (agent tag, paths, enabled sections, excludes, skills, etc.). Use **relative paths** (`.camber/instruction.md`, `.camber/chats`). Leave `agent:` **blank** on first push — do not create the agent beforehand to obtain a uuid.
4. Push — the CLI reads `.camber/sync.yaml` automatically and syncs the configured sections:
   ```bash
   $ camber agent push --output json
   ```

Confirm with the user via `AskQuestion` (Cursor) or `AskUserQuestion` (Claude Code) before running push because it updates the remote mirror. **Wait for the user's answer** — do not push on assumptions.

Rules:
- Do not call `agents_create` or `$ camber agent create` before a first-time push just to fill `agent:` in `sync.yaml`.
- Add `.camber/**` to top-level `exclude` so `.camber/instruction.md` and `.camber/chats/` are not uploaded as project files.
- Do not push skills, project files, chat, instruction, or other mirror sections with separate CLI commands (`skill compile`, `context add`, `stash cp`).
- Prefer `$ camber agent context init` over hand-writing `.camber/sync.yaml`.
- If unsure whether the current directory is the project root, a pulled mirror, or some other folder, stop and ask via the interactive question tool.
- Do not ask for an agent tag override. Push reads the target from `.camber/sync.yaml`.
- Do not suggest `--dry-run`, partial push flags, or confirmation flags.
- Enabled sections are force-synced. Disabled sections are left unchanged.
- `knowledge-base/`, `chat/`, and skill `references/` files are indexed when supported.
- `project/`, `README.md`, `instruction.md`, `requirements/`, and `schema/` are mirror files, not KB.
- Unsupported files in indexed sections are skipped with a warning.
- After a successful push, remove `.camber/instruction.md` and `.camber/chats/` staging files; keep `sync.yaml`.

After push completes, summarize changed sections, warnings, duration, and whether staging was cleaned up.
