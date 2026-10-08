---
name: daily-leveling
description: Turn things the user commits to in conversation into tracked quests worth XP, mark them complete, and report real progress. Use whenever the user mentions something they intend to do, says they finished something, or asks how they are doing.
---

# Daily Leveling

Daily Leveling is an RPG-style habit tracker. Tasks are **quests** worth XP, longer
objectives are **goals**, and completed work accrues into seven **stats**.

## When to reach for this

Act when the user:

- **Commits to something** — "I need to call the dentist", "I should start running again".
  Offer to add it. Do not silently create quests for things they merely mentioned.
- **Reports finishing something** — "I hit the gym", "sent the proposal". Find the
  matching open quest and complete it.
- **Asks about progress** — "how am I doing", "what's my level", "what's left today".
  Call the tool. Never estimate from memory of the conversation.

Do not act on hypotheticals ("I was thinking about maybe..."), on things clearly
belonging to someone else, or on past events with no matching quest.

## The seven categories

Every quest and goal takes exactly one:

`business` · `health` · `fitness` · `education` · `personal` · `finance` · `travel`

Pick the one the user would pick. Gym and running are `fitness`; doctors, sleep, and
diet are `health`. Client work and admin are `business`; bills, rent, and budgeting are
`finance`. Courses, reading, and languages are `education`. Everything else personal is
`personal`.

## XP follows priority

| Priority | XP |
|---|---|
| `low` | 20 |
| `medium` | 30 |
| `high` | 50 |

Default to `medium` unless the user signals urgency ("this is critical", a hard
deadline) or triviality. Never invent an XP number — it is derived from priority, and
the tool returns the real value.

## Workflows

**Creating.** Confirm the title in the user's own words before creating. Keep titles
short and actionable — "Call the dentist", not "The user needs to schedule a dental
appointment". Set a deadline only when the user gave one.

**Completing.** Call `list_quests` first and match against open quests. If several
plausibly match, ask which. If none match, say so — do not create a quest and complete
it in the same breath to manufacture a match.

**Reporting.** `get_stats` returns total XP, level, and per-category XP. Lead with what
moved and what has been neglected; the categories with the least XP are usually the
more useful observation.

**Looking something up.** `search` finds quests and goals by topic and returns ids;
`fetch` returns one in full. Use both rather than guessing at ids.

## Boundaries

- Nothing here deletes. There is no tool to remove a quest, goal, or account. If asked,
  say so and point to the app: **Profile → Account → Delete Account**, or
  <https://www.dailyleveling.app/delete-account>.
- The connection is scoped to one account. It cannot read another user's quests, crew
  standings, email, or password. Crew leaderboards live in the app.
- Completion is reversible in the app, which returns the XP — but say what you are
  about to complete before completing it.
