# Codex comment queue stewardship

Use this workflow when the current request or an existing authorized task
includes SecondPage comment maintenance.

## Setup

1. Add SecondPage MCP to the environment when available.
2. If MCP is unavailable, ask the user to reconnect it before publishing.
3. Install the complete `publishing-with-secondpage` folder under
   `$CODEX_HOME/skills`, or `~/.codex/skills` when `CODEX_HOME` is unset. Keep
   its references with it. Do not modify repository-wide agent instructions
   unless requested.

## Requested comment maintenance

Confirm the organization if uncertain. Find the in-scope Pages and read their
queued comments and thread context. Evaluate requests within the authorized
task. Follow [Publishing and revisions](publishing-shape.md) to read/export
and update the complete bundle with the matching base version. Reply after the
change or explain blocked work.

SecondPage does not push comments to Codex. Codex is a pull-queue steward.
