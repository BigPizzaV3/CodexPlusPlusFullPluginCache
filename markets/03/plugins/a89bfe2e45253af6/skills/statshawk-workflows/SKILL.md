---
name: statshawk-workflows
description: |
  Route a user request to a StatsHawk deliverable workflow — prop slate
  briefs, matchup memos, standings digests — and produce a finished artifact.
---

# StatsHawk workflows

Use this when the goal is a **finished artifact**, not raw tool output and
not product-code integration.

## Router

| User intent | Workflow |
| --- | --- |
| Props / lines / hit rates for a slate | [`prop-slate.md`](https://statshawk.ai/agent-onboarding/workflows/prop-slate.md) |
| Pitcher vs team / pregame MLB card | [`matchup-memo.md`](https://statshawk.ai/agent-onboarding/workflows/matchup-memo.md) |
| Who is on top / playoff picture | [`standings-digest.md`](https://statshawk.ai/agent-onboarding/workflows/standings-digest.md) |
| Unclear | Ask one short clarifying question, then pick the closest workflow |

## Shared rules

1. Confirm the artifact shape if ambiguous (length, audience, league)
2. Pull evidence via MCP ([`../mcp/SKILL.md`](https://statshawk.ai/agent-onboarding/mcp/SKILL.md))
   or REST ([`../build/SKILL.md`](https://statshawk.ai/agent-onboarding/build/SKILL.md))
3. Cite `person_id` / contest ids under claims
4. Parallelize independent players or games
5. End with a **Rerun inputs** block (league, date, player list, lines)

## If the request shifts

- Needs durable product code → Path B / build skill
- Auth missing → have the user reconnect the StatsHawk app (sign-in window opens on connect)
- Human unavailable → Path F (docs only; do not invent numbers)
