---
name: codex-usage
description: Run the bundled local reader to check remaining Codex usage, weekly or five-hour limits, reset times, and reset-card availability. Use for Codex quota questions in a local Codex task, including ChatGPT Plus/Pro users. Requires access to that computer's local terminal.
---

# Codex usage

Answer in the user's language. A usage question is a request to **run the
query**, not just supply a command or offer to locate the script later.

## Run the installed reader

1. Use the local terminal tool for the computer running the user's Codex task.
   If tools are deferred, discover the host's terminal/execution tool first.
   A cloud code interpreter cannot read another computer's Codex history.
2. Resolve [scripts/codex_usage.py](scripts/codex_usage.py) relative to the
   actual installed location of this `SKILL.md` supplied by the skill catalog.
   Use the host's resource reader when it supplies a skill resource URI instead
   of a filesystem path. Do not treat `plugin://` or `skill://` as a file path.
3. Run that verified script using the local terminal:

```sh
python3 "<this-skill-directory>/scripts/codex_usage.py" --json
```

Replace the placeholder with the resolved absolute directory before executing.
The script is bundled **inside the plugin**; `~/.codex` holds the user's data.
The plugin does not install `~/.codex/usage/codex_usage.py`. Do not invent that
path or copy a path from the publisher's computer. If the script, Python, or
local terminal is missing, follow [troubleshooting](references/troubleshooting.md)
before responding with an unavailable result.

Requires Python 3.9+ with no third-party packages. On Windows, use an available
Python 3.9+ interpreter such as `py -3` if `python3` is absent. The reader uses
`$CODEX_HOME` when set, otherwise `~/.codex`; `--codex-home` selects a specific
installation. `--timezone Asia/Shanghai` sets display times; the default is the
machine's local timezone. No browser or new login is needed.

## Interpret the result

Report the remaining percentage, used percentage, reset time with timezone,
snapshot time, and source file. The reader scans only structured usage events in
`sessions` and `archived_sessions`; it does not output conversation text.

- Identify windows by duration: 10080 minutes is weekly, 300 minutes is five
  hours. Either can appear in `primary` or `secondary`.
- Local results are recorded account snapshots, not a live balance. If the reset
  time has passed, describe the result as an expired snapshot; do not claim the
  old percentage still applies or assume it reset to 100%.
- Local history cannot verify which account is currently signed in. If the user
  mentions an account switch, explain that limitation before attributing a
  snapshot to an account. Keep different limit IDs separate.
- `credits.balance` describes paid credits, **not reset cards**. Missing reset
  card data means unknown, not zero. `available_count: 0` is a known zero only
  when an explicit reset-card summary supplies it. Card details can be partial.
- Do not convert percentages or cumulative conversation token counts into a
  fixed number of messages. A `pro` plan value does not by itself establish 20×.

If no usable snapshot exists (`limits` is empty, the requested window is absent,
or its reset time has passed), run one bounded read through the existing Codex
CLI authentication. Also use this read when the user
asks about unrecorded reset cards or explicitly wants a live refresh:

```sh
python3 "<this-skill-directory>/scripts/codex_usage.py" --live --json
```

This only calls `initialize` and `account/rateLimits/read` on the installed
Codex app server. It does not start an agent task or read credential files.
The reader detects both a CLI on `PATH` and the CLI bundled with the macOS
ChatGPT/Codex app; `diagnostics.codex_cli` reports the detected path. A missing
`codex` shell command does not by itself mean the CLI is unavailable.
Keep live results separate from local history and identify which source answers
the question. If the CLI has no applicable authentication, retain the local
result and report `live_status`. Do not launch a login flow
or browser merely to answer a local usage question.

For an unavailable result, state the actual failure stage: terminal access,
script installation, Python, or the reader's `local_status`. Include the checked
Codex home and file counts from `diagnostics` when the reader ran. An empty
history means this installation has no recorded quota; installing the plugin
does not transfer another computer's records. Never claim to have checked local
records without an execution result, or report a missing balance as zero.

The plugin does not redeem cards, buy credits, alter authentication, or modify
Codex history. Requests for those actions are outside its query capability.
Missing files or malformed records should produce an honest unavailable result,
not an invented balance. Do not dump raw logs, auth files, or account identifiers
to troubleshoot a missing snapshot.
