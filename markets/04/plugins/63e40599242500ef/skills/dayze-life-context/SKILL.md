---
name: dayze-life-context
description: >-
  Load and act on the signed-in Dayze user's private life graph (identity, people,
  week, memories, trackers). Use when the user asks about their day, calendar,
  who matters, memories, mood/energy, expenses, logging food/events, or "what's
  next" in their life — not for public celebrity biographies.
---

# Dayze life context

Dayze is the user's life-in-days graph. Private tools require OAuth (ChatGPT connector). Never invent calendar events, people, or memories.

## First call

1. Call `get_context_pack` once (prefer over chaining `get_life_context` + separate reads).
2. Ground the reply in pack fields: identity, pulse, who_matters, week / today_events, memories, trackers, whats_next.
3. Speak in life-days when useful (age_days, day_number) without lecturing.

## Follow-ups

| User intent | Tool |
| --- | --- |
| Search across life | `search` (phrase-first; use returned ids) |
| Calendar / agenda | `get_events` (week includes today; respect `truncated`) |
| People / CRM | `get_people` / `update_person` |
| Memories | `get_memories` |
| Log food / meal | `log_food` (and family) |
| Log calendar item | `log_event` |
| Favorite song | `log_favorite_song` |
| Patch existing rows | `update_event` / `update_food` — confirm ambiguous targets |

## Rules

- Do not invent facts missing from tool results.
- Writes change the user's real Dayze account — confirm destructive or ambiguous edits.
- If auth fails, tell them to reconnect Dayze in ChatGPT settings (OAuth), not to paste API keys in chat.
- For famous people / Nobel / birthday peers, use the **dayze-notable-people** skill / `notable_*` tools instead.

## Output

Lead with what matters today (pulse + today_events + pending). Keep lists short. Cite day numbers only when they add insight.
