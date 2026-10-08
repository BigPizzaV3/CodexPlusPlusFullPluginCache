# Resolve a failed local query

Use this only when the normal bundled-script call cannot run or returns no
usable snapshot. Keep the failure stage explicit.

## Script location or tools unavailable

- Prefer the skill's installed location from the host catalog. Read this skill
  and its linked script through the host's resource tools if the catalog uses
  resource URIs. Do not assume those resources have been placed on the user's
  local disk.
- With local shell access but no resolved script path, inspect the installed
  plugin entry (`codex plugin list --json`, when supported). Otherwise search
  only the Codex plugin cache under the effective Codex home, and the default
  `~/.codex/plugins/cache` if different. For example, on a POSIX shell:

  ```sh
  rg --files --hidden "${CODEX_HOME:-$HOME/.codex}/plugins/cache" -g codex_usage.py
  ```

  Verify the containing `.codex-plugin/plugin.json` names `codex-usage`.
  Match the active installed version; do not select an arbitrary old cache.
  Use the resulting absolute path, quoted for the current shell. On Windows,
  use the equivalent file search and a verified Python 3 interpreter.
- If the local plugin cache does not contain the script, report an incomplete
  or unavailable local install. Refresh/reinstall the plugin from its existing
  source and test in a new Codex task. Do not create a fake usage directory or
  make the user run a nonexistent path.
- If the task exposes no local execution tool after tool discovery, say that
  this task lacks access to the computer's terminal. A plugin mention alone is
  not proof of local tool access. Ask the user to open a local Codex task on
  the intended computer; do not call this a missing usage record.
- If Python cannot run, report the interpreter error. Use another installed
  Python 3.9+ interpreter if available; do not silently install dependencies.

## Reader results

| `local_status` | Meaning and next step |
| --- | --- |
| `ok` | Read the recorded limits and timestamps. |
| `partial` | Some history was unreadable; the returned snapshot may not be the latest. |
| `codex_home_missing` | The checked Codex data directory does not exist. Confirm the task runs on the intended computer and installation. |
| `session_directories_missing` | The data directory exists but has no `sessions` or `archived_sessions` folders. |
| `no_session_files` | History directories exist but contain no readable candidate JSONL files to scan. |
| `no_rate_limit_snapshots` | Files were read, but no supported structured quota snapshot was found. API-only sessions may have no subscription quota data. |
| `history_unreadable` | Files or directories could not be read. Report the access failure and use the host's normal permission mechanism if available. |

The JSON diagnostics include only the checked home and aggregate file/event
counts. Use these to explain what was checked without dumping conversations.
The default Windows app home and a WSL home can be different installations;
never combine their history or infer an account identity from either.

On macOS, the CLI can be bundled in `ChatGPT.app` or `Codex.app` without being
on the terminal's `PATH`. The reader checks their standard `/Applications` and
`~/Applications` locations automatically. Use `diagnostics.codex_cli` rather
than concluding the CLI is missing from a failed `which codex` alone.

When local data cannot answer the request, try `--live --json` once using the
same `--codex-home`. Missing CLI, unavailable ChatGPT
authentication, and timeout are distinct `live_status` values. A failed live
read does not make a historical snapshot current. If both sources are
unavailable, explain the specific reason and stop; no balance can be inferred.
