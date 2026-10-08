# Cursor Chat Export

Cursor stores chats in SQLite, not JSONL.

Cursor user data directories:

| OS | Path |
|---|---|
| macOS | `~/Library/Application Support/Cursor/User/` |
| Linux | `~/.config/Cursor/User/` |
| Windows | `%APPDATA%\Cursor\User\` |

Important files:

```text
workspaceStorage/<hash>/workspace.json
globalStorage/state.vscdb
```

Use `workspaceStorage/<hash>/workspace.json` only as a project-to-workspace-hash cross-check. Read chat content from `globalStorage/state.vscdb`, table `cursorDiskKV`.

Reliable export flow:
1. Enumerate `composerData:%` rows from the global DB.
2. Keep only composers whose embedded `workspaceIdentifier` matches the target project path or workspace hash.
3. For each kept composer, read exact `bubbleId:<composerId>:<bubbleId>` rows.
4. Render non-empty user and assistant text into markdown.

Do not rely on `workbench.panel.composerChatViewPane.<id>` keys. In current Cursor builds those are stale view-pane state, not reliable composer IDs.

Key layout:
- `composerData:<composerId>`: conversation header with title, timestamps, workspace identifier, and ordered bubble refs.
- `bubbleId:<composerId>:<bubbleId>`: message bubble. Type `1` is user, type `2` is assistant.

Conversion rules:
- Open the global DB read-only when possible.
- Query only `composerData:%` and exact bubble keys.
- Never dump the full `cursorDiskKV` table.
- Match workspace by `workspaceIdentifier.id`, `workspaceIdentifier.uri.fsPath`, `workspaceIdentifier.uri.path`, or `workspaceIdentifier.uri.external`.
- Skip empty-text bubbles, pure tool frames, stale panel/view state, and unrelated workspaces.
- Write one markdown file per composer plus `README_CURSOR.md`.
- Write all export files to `.camber/chats/` using **relative paths** in `sync.yaml`.
- If the DB is locked or reads fail, ask the user to close Cursor and retry.
- Do not commit exported chats.

Wire the exported chat into `.camber/sync.yaml` (after `$ camber agent context init`), then sync with push — do not call `$ camber agent context add --chat` as a separate mirror step:

1. Point the `chat` section at `.camber/chats`.
2. Run `$ camber agent push --output json` from the project root or pulled mirror root.

Verify the accepted source URI is under:

```text
stash://<owner>/.camber/agent-context/<agent-alias>/chat/
```
