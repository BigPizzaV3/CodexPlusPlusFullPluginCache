---
name: token-weather
description: Show estimated space and recent changes for the exact local Codex chat, open its weather page or replay a supplied local event recording when asked.
---

# Token Weather

Find this skill's plugin folder two levels up. For requested weather, use the
current project's absolute path and the exact root chat ID from trusted host
metadata. Explain briefly on first use that the helper reads this chat's local
record, reduces selected numeric/lifecycle fields and does not save one-off
history by default. That weather request authorises this limited read; do not
ask for the same approval again after its scope has been disclosed.

Run `python3 "<plugin-root>/scripts/weather.py" --workspace "<project>" --thread-id "<exact-root>" weather`.
Use `--compact` or `--json` as needed. Do not guess another chat when the ID,
record binding or format is unavailable. Local access and Python 3.11+ are
required; ChatGPT web-only context is unavailable. Automatic discovery checks
matching filenames under sessions, not arbitrary chat contents. Use an archived
record only when its exact file is explicitly selected.

One-off weather reads do not cache or read config by default. Use
`--cache-history` only when the person requests saved numerical history; use
`--read-config` only for a requested local reference-config check. An explicit
`--compact-limit` can supply an advisory reference without reading config.
Read [local data and privacy](../../docs/PRIVACY.md) when explaining storage,
retention/deletion or access limits. Raw record bytes may enter memory even
though message/tool/summary values are not decoded or retained.

For a requested persistent page, explain that `weather-service start` creates
a loopback collector and numeric history until explicitly stopped. Use the
same project/chat ID; open only the returned local URL. `weather-service status`
and `weather-service stop` inspect or stop its own instance. Closing the tab
does not stop it. `weather --html <new-output.html>` exports an offline snapshot
without starting a service. Keep exports local and do not overwrite inputs.

For a supplied recording, read [local replay](references/REPLAY.md). Replay
keeps original timestamps and does not execute recorded tools or file edits.
Default weather/replay outputs minimise identifiers; detailed replay metadata
is an explicit diagnostic option. Do not paste raw records into chat or send
them to a remote service for a reading.

Report estimates, stale/unknown fields and the whole-turn output average
accurately. Account windows are separate from chat space. A lower usage count
alone does not prove native compaction. The optional local helpers have no hooks, automatic alerts or native controls.
The separate numeric MCP receives no local records and cannot transfer a chat/lease.
