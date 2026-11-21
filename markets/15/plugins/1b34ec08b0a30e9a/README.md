# Sway for AI assistants

[Sway](https://www.sway.events) is the events platform for electronic music and club culture. This
plugin connects an AI assistant to Sway's public catalogue: events, artists, venues, promoters and
genres.

- Read-only. It exposes public catalogue data only: no sign-in, no personal data, no drafts.
- Remote MCP server (streamable HTTP): `https://mcp.sway.events/discovery`
- Works with any client that supports Agent Plugins or remote MCP servers (Cursor, Grok Bot, Claude,
  ChatGPT and others).

## Tools

| Tool | What it does |
|---|---|
| `search_events` | Upcoming published events by text, city, genre and date range, soonest first |
| `get_event` | One event with its lineup, venue, genres and, when it sells tickets on Sway, ticket types |
| `search_artists`, `get_artist` | Find an artist, open one |
| `search_venues`, `get_venue` | Find a venue, open one |
| `search_promoters`, `get_promoter` | Find a promoter, open one |
| `list_genres` | Every music genre name Sway knows |

## Example prompts

- "Techno events in Brussels this weekend"
- "When does this artist play next?"
- "Which venues host drum and bass?"

## Install

- Cursor and other Agent Plugins clients: add this repository as a plugin.
- Any MCP client: add the server URL above, transport streamable HTTP, no authentication.

Limits: 120 requests a minute and 1,500 an hour per address.

## Links

- Documentation: https://www.sway.events/en/docs/api/public-mcp
- Privacy policy: https://www.sway.events/privacy
- Support: contact@sway.events

Released under the MIT license (this repository only: the manifest and the documentation).
