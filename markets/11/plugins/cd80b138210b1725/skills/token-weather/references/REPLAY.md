# Local recorded-event replay

Replay is available without MCP or hooks. Use the exact recording supplied
by the person; do not search unrelated chats to create a guessed input.
The helper reduces recorded events and writes an optional report. It does
not execute recorded tools, edit source files or connect to a live runtime.

```sh
python3 "<plugin-root>/scripts/weather.py" --workspace "<project>" replay-usage --input "<recording.json>" --output "<usage-report.json>"
python3 "<plugin-root>/scripts/weather.py" --workspace "<project>" replay-control --input "<recording.json>" --output "<control-report.json>"
```

These commands accept the existing pinned `codex-cli 0.160.0` event envelope,
not arbitrary chat text. Maximum input: 256 KiB and 500 events. A usage
recording has schema_version, engine_version, thread_id, absolute workspace,
thread_response and events. Each event has its original UTC Unix observed_at
and message. A control recording also identifies turn_id. Missing, future,
invalid or out-of-order timestamps are rejected. New formats remain unsupported
until verified; do not relabel them as an older version.

Replay retains original timestamps. Old measurements stay old; reports never
become proof of current context, live quiescence or permission to control Codex.
Usage reports have production_promotion and exact_active_occupancy set to false;
control replay cannot certify quiescence. Explain these limits with the result.

The parser projects only necessary usage/lifecycle fields. Raw input bytes
briefly enter memory, but message previews, tool arguments and error text are
not decoded or returned. Default results omit binding identifiers and control
member/operation IDs. Only when explicitly requested for local diagnostics,
add `--include-local-metadata` to return detailed IDs and paths; keep that report
local and explain that it contains private metadata. Output files must be new
and outside Codex/plugin-owned storage. Do not overwrite a supplied recording.

To review recorded weather on the original local page, use the token-weather
command with `weather --events <notifications.jsonl> --html <snapshot.html>`.
This is a separate format: a supported bounded JSONL notification capture with
exact root filtering. The capture does not establish project ownership or live
freshness; the workspace only selects the local execution directory. It exports the existing interactive history and
forecast display; it does not replay file edits. Retain the requested offline
export locally and do not upload private event recordings or checkpoints.

Read [local data and privacy](../../../docs/PRIVACY.md) for storage, retention,
host processing and manual deletion. This edition does not use the full
plugin's caches or automatically adopt its checkpoint workflows.
