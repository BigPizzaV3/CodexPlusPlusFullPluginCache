# Create Or Update A Workspace-Mirroring Agent

## When to use

Use this when the user wants Camber Cloud to feel like the local coding workspace they are currently using.

## Inspect first

Inspect at least:
- README/docs
- project tree and important directories
- manifests and dependency files
- entrypoints and key modules
- config files
- test structure
- local commands and conventions
- project-scoped assistant context

Check the connected client's context first:
- Claude Code: `CLAUDE.md`, `.claude/settings*.json`, `.claude/commands/`, `.claude/skills/`
- Cursor: `.cursor/rules/`, `.cursorrules`, `AGENTS.md`

Only inspect user/global assistant context when it was used in the current chat or the user explicitly confirms it is relevant. Do not migrate every global skill by default.

## Runtime connector substitutions

Camber Cloud's runtime does not support the Snowflake CLI (`snowsql`, `snowflake` CLI). If the
workspace uses it, `instruction.md` must tell the created agent to use `camber.snowflake`
(Camber's Python API) instead — never the local CLI.

## Confirmation gate

Before any write action, present a plan and wait for explicit approval. Collect each confirmation through the client's interactive question tool:
- Cursor: `AskQuestion` (one decision per call)
- Claude Code: `AskUserQuestion`

Do not substitute plain chat text for these confirmations.

Include:
- proposed agent name and alias
- personal vs team scope
- whether an existing agent will be updated
- inspected context files
- selected skills
- executable backing files
- project files to upload
- sensitive exclusions
- whether extra historical chats should be included

Do not call `$ camber agent context init` or `$ camber agent push` before approval. Do not call `agents_create` or `$ camber agent create` to obtain an agent id for a first-time mirror.

**Wait for user input:** every confirmation must go through `AskQuestion` (Cursor) or `AskUserQuestion` (Claude Code). Do not proceed until the user has answered.

## Create or update

### First-time mirror (new agent)

Do **not** create the agent before push. Do **not** call `agents_create`, `$ camber agent create`, or fill `agent:` in `.camber/sync.yaml` with a uuid.

1. Draft `instruction.md` under `.camber/instruction.md`.
2. Fill `sync.yaml` with `owner`, `alias`, `name`, `description`, and paths — leave `agent:` **blank** (or `""`).
3. Run `$ camber agent push` — the CLI creates the remote agent and records the id in `.camber/sync.yaml` for later refreshes.

### Refresh (existing agent)

If the agent already exists, set `agent:` in `.camber/sync.yaml` to the known remote id (from a prior push or `$ camber agent list`). Optionally update instructions first:

```bash
$ camber agent update @owner.alias --name "<agent-name>" --description "<agent-description>" --instructions-file .camber/instruction.md --output json
```

Agent `instructions` should include:
- compact workspace mission
- code structure
- runtime assumptions
- commands
- key modules
- tests
- local assistant conventions
- safety and privacy constraints
- short migrated skill index

Do not embed full Stash path maps into the created agent instructions.

If mentioning runtime project files, use:

```text
<owner>_<agent-alias>_project-directory/
```

For team agents, `<owner>` is the team unique name. Do not tell the created agent that the runtime project folder is the original local repository folder name.

## Unified sync (init -> chat export -> sync.yaml -> push)

Do not upload project files, skills, chat, or `instruction.md` with separate CLI commands (`stash cp`, `skill compile`, `context add`). Sync everything through `.camber/sync.yaml` and `$ camber agent push`.

Run these steps from the **project root** (fresh mirror) or the **pulled mirror root**.

### 1. Initialize sync config

```bash
$ camber agent context init
```

This creates `.camber/sync.yaml` with placeholders. Prefer this over hand-writing the file.

Placeholders typically include:
- `{{AGENT_ID}}` — remote agent ID (leave empty for first-time push)
- `{{OWNER}}` — agent owner name
- `{{ALIAS}}` — agent alias
- `{{NAME}}` — display name (required for first-time push)
- `{{DESCRIPTION}}` — short description
- `{{README_PATH}}` — path to README
- `{{INSTRUCTION_PATH}}` — path to instruction file
- `{{KNOWLEDGE_BASE_PATH}}` — path(s) to knowledge-base files or directories

### 2. Draft instruction and export chat

Draft `instruction.md` to `.camber/instruction.md`.

Export the current chat (always) and any approved historical chats using the connected client chat-export resource. Write exports to `.camber/chats/` (one markdown file per session plus an index readme).

### 3. Review and fill `.camber/sync.yaml`

Replace placeholders with values that match the local directory and approved plan:
- agent identity (`owner`, `alias`, `name`, `description`)
- `agent:` — leave **blank** on first push; set only when refreshing an existing mirror
- `project.path` and top-level `exclude` patterns (include `.camber/**` so staging files are not mirrored as project files)
- `skills.path` / `skills.managed` for approved skills
- `chat.path`: `.camber/chats`
- `instruction.path`: `.camber/instruction.md`
- `knowledge_base.paths` only for approved KB sources
- enable/disable sections as approved

Use **relative paths** for all local sources. `$ camber agent push` requires relative paths, not absolute temp directories.

### 4. Push

```bash
$ camber agent push --output json
```

`$ camber agent push` reads `.camber/sync.yaml` automatically and syncs the configured sections. On first push it also creates the remote agent when `agent:` is blank. After a successful push, remove `.camber/instruction.md` and `.camber/chats/`; keep `sync.yaml` (it may now include the assigned agent id).

## Skills in `sync.yaml`

Discover project skills from:
- `.claude/skills/<skill-name>/SKILL.md`
- nested `**/.claude/skills/<skill-name>/SKILL.md`
- `.cursor/skills/<skill-name>/SKILL.md`
- `.agents/skills/<skill-name>/SKILL.md`
- `.gemini/skills/<skill-name>/SKILL.md`

List approved skill names/dirs in `sync.yaml` (for example via `skills.path` and `skills.managed`). Do not run `$ camber agent skill compile` as a separate mirror step — `push` applies the skills section.

Rules:
- Preserve the full approved skill folder in Stash under `skills/<skill-name>/`.
- `SKILL.md` becomes the Camber skill definition.
- Description-only skills do not require a backing file.
- Executable skills require an entrypoint. Set `camber-entrypoint: <relative-python-file>` in `SKILL.md` frontmatter, or rely on auto-selection: the CLI picks the sole `.py` file in the skill's `scripts/` folder when there is exactly one; with zero or multiple `.py` files, nothing is auto-selected.
- Valid `SKILL.md` frontmatter fields are `name`, `description`, and optional `camber-entrypoint`.
- Skill `references/` files are indexed as KB resources during push when supported.
- Do not manually add `SKILL.md`, scripts, or other skill files to KB.

## Instruction file

Draft `instruction.md` to `.camber/instruction.md`. Point the `instruction` section in `.camber/sync.yaml` at `.camber/instruction.md`. Let `$ camber agent push` upload it to Stash — do not run a separate `$ camber stash cp`.

The file should contain the workspace mirror instructions you would pass to `$ camber agent update --instructions-file` on a refresh.

After push, verify the Stash path:

```text
stash://<owner>/.camber/agent-context/<agent-alias>/instruction.md
```
