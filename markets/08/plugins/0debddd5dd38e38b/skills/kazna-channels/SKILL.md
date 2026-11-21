---
name: kazna-channels
description: List and inspect Kazna author channels and their subscribers via read-only MCP tools.
---

# Kazna channels

Use MCP server `Kazna`.

## Steps

1. Call `list_channels`. Summarize id, title, platform, username, subscriber counts when present.
2. If the user asks about one channel, call `get_channel` with its UUID.
3. For audience questions, call `list_channel_subscribers` with that channel id and summarize roster (no buyer phones).

## Constraints

- Channel responses intentionally omit pricing and sales settings.
- Do not offer to change access mode, prices, trials, or catalog visibility.
