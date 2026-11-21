---
name: kazna-subscribers
description: List subscribers of a Kazna channel owned by the authenticated author.
---

# Kazna subscribers

Use MCP server `Kazna`.

## Steps

1. If channel id is unknown, call `list_channels` first and ask which channel to inspect (or pick the first if the user said so).
2. Call `list_channel_subscribers` with that channel UUID.
3. Summarize counts, platforms, and recent starts/expiries without inventing PII.

## Constraints

- Read-only; do not block or remove subscribers through this plugin.
