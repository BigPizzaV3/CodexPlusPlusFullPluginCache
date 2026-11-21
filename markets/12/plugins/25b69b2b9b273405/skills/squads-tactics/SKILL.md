---
name: squads-tactics
description: Use when the user wants to build a football line-up, explore formations, or create an animated tactical play with the Squads MCP server.
---

# Squads tactics workflow

Use the Squads MCP tools to produce a shareable football tactics board.

- For a line-up, call `list_formations` first when the user has not chosen a preset or needs formation options. Use a returned preset key exactly. Then call `create_squad` with the home team, formation, player list, and any requested opponent details. Player names are optional; if omitted, the server labels positions automatically. The response includes the share URL.
- For an animated tactical play, call `list_formations` first if you need preset keys or slot IDs, then call `create_play`. Define the starting home and optional away line-ups, followed by scenes and player or ball movements. Return the share URL and briefly describe the resulting play.
- Ask for only information needed to complete the requested board. Use reasonable defaults for unspecified board orientation, kit colors, and formation details when the server schema permits them.
- Preserve user-provided team names, manager names, player names, numbers, positions, and colors. Do not claim a line-up or play was saved by the server; the server describes the result as existing in its share URL.
- If a requested detail cannot be represented by the tool schema, explain that briefly and offer the closest supported option.
