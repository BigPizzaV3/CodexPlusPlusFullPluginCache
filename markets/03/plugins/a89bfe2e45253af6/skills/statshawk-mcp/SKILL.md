---
name: statshawk-mcp
description: |
  Drive the StatsHawk hosted MCP server during an agent session —
  which tool to call, how to chain ids, and how to recover from OAuth
  or quota failures.
---

# StatsHawk MCP (data tools)

Endpoint: `https://mcp.statshawk.ai/mcp` (Streamable HTTP, OAuth)

## When to use

Use this skill when the agent itself needs sports data **right now**.
For product-code integration, switch to
[`../build/SKILL.md`](https://statshawk.ai/agent-onboarding/build/SKILL.md).
For finished artifacts, switch to
[`../workflows/SKILL.md`](https://statshawk.ai/agent-onboarding/workflows/SKILL.md).

## Install (if missing)

```bash
claude mcp add --transport http statshawk https://mcp.statshawk.ai/mcp
```

Other clients: https://statshawk.ai/docs/mcp/client-setup

On first tool call the client opens OAuth. The human signs in once; no
API key is pasted into MCP config.

## Tool routing

| Need | Tool | Notes |
| --- | --- | --- |
| Find a player | `search_player` | Returns `person_id` for chaining |
| Find games | `search_games` | Filter by league, date, team, status |
| Box score | `get_box_score` | Needs a game / contest id |
| Standings | `get_standings` | League slug e.g. `nba` |
| Roster | `get_team_roster` | Current roster + person ids |
| MLB matchups | `get_mlb_matchups` | Pregame pitching / lineup context |
| MLB PBP / Statcast | `get_play_by_play` | Filterable per player |
| Prop card / hit rates | `get_player_props` | **Paid plan** |
| What can I ask? | `get_stat_capabilities` / `search_docs` | When unsure |

Full catalog: https://statshawk.ai/docs/mcp/tool-catalog.md

## Default flow

1. **Discover** with `search_player` or `search_games`
2. **Fetch** with the returned ids (`person_id`, contest/game ids)
3. **Analyze** with `get_player_props` only when the account is paid
4. **Cite** ids in the answer so the human can verify

## Failure recovery

- **OAuth window never appeared** — look for a queued sign-in prompt; or
  remove and re-add the MCP server
- **`403 TIER_REQUIRES_PAID`** — analysis tools need any paid plan; use
  game logs / free tools instead, or ask the human to upgrade
- **`429 QUOTA_EXCEEDED`** — monthly units exhausted; tell the human to
  check https://statshawk.ai/dashboard
- **Connected but empty** — confirm league slug and date window; offseason
  standings still resolve to a concrete `season_year`

## Auth & quotas

https://statshawk.ai/docs/mcp/auth-and-quotas.md
