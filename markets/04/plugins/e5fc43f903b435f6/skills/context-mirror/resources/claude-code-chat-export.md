# Claude Code Chat Export

Claude Code stores one folder per working directory under:

```text
~/.claude/projects/
```

The folder name is the absolute project path with every `/` replaced by `-`.

Example:

```text
/path/to/project -> ~/.claude/projects/-path-to-project/
```

Derive the transcript folder:

```bash
$ PROJECT_DIR="$(pwd)"
$ SLUG="$(echo "$PROJECT_DIR" | sed 's#/#-#g')"
$ SRC="$HOME/.claude/projects/$SLUG"
$ ls "$SRC"/*.jsonl
```

If `$SRC` does not exist, list `~/.claude/projects/` and find the folder matching the absolute project path. Do not say Claude Code transcript export is unsupported unless the local filesystem path is inaccessible.

Because the user is currently chatting in this repo, a workspace transcript is expected. If the exact active session is unclear, export the most recently modified `.jsonl` session in the matching project transcript folder and tell the user which file was selected.

Conversion rules:
- Stream JSONL line by line.
- Keep `user` text after removing `<system-reminder>...</system-reminder>` blocks.
- Keep `assistant` `text` blocks.
- Render assistant `tool_use` blocks as short one-line summaries.
- Drop `thinking`, `tool_result`, `permission-mode`, `file-history-snapshot`, `attachment`, and other noisy metadata.
- Use `ai-title` as the markdown title when present.
- Skip records with `"isSidechain": true` unless the user asks for subagent audit logs.
- Write one markdown file per session plus a `README.md` index.
- Write all export files to `.camber/chats/` using **relative paths** in `sync.yaml`.
- Do not commit exported chats.

Wire the exported chat into `.camber/sync.yaml` (after `$ camber agent context init`), then sync with push — do not call `$ camber agent context add --chat` as a separate mirror step:

1. Point the `chat` section at `.camber/chats`.
2. Run `$ camber agent push --output json` from the project root or pulled mirror root.

Verify the accepted source URI is under:

```text
stash://<owner>/.camber/agent-context/<agent-alias>/chat/
```
