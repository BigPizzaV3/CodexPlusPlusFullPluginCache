---
name: clash-royale-competitive-data
description: Research Clash Royale meta decks, observed card usage, current or archived leaderboards, and country leaders on RoyaleTools. Use when the question needs competitive evidence or ranking context.
---

# Competitive data

Read [the website contract](../royaletools-navigator/references/website.md).

| Question | Website workflow |
| --- | --- |
| Which decks are popular in the sampled meta? | `/meta-decks`; use the visible mode and time controls |
| Which archetypes represent the current sample? | `/meta-decks?view=map` |
| How often is a card or form observed? | `/card-usage`; search/filter and sort visible rows |
| Who leads a mode or country? | `/leaderboards`; choose the current offered board and country |
| Who is first in each supported country? | `/leaderboards?view=countries` |
| What were earlier standings? | `/leaderboards?view=past`; select an available saved season |

Meta Decks supports `time=week` or `month`, `view=all` or `map`, and current mode keys. Do not reuse old category filters that the page no longer offers. Leaderboard links can preserve `view`, `board`, and `country`; use values supplied by the live selectors, not guessed board IDs.

Read card forms separately. Base, Evolution, and Hero rows can differ. Card Usage movers compare the page's week with the week before; report them as changes in observed usage, and say so when the page shows that a young week falls back to the last full week. A displayed 0% means the form was absent from that sample, not absent from the whole game. Usage/battle share is not win rate. A Meta map tile is one representative observed deck per classified archetype, not all variants of that archetype.

RoyaleTools has no head-to-head comparison of two players at the moment. Do not open `/head-to-head` or invent a record; offer each player's public profile or Leaderboards instead.

Use the visible timestamps and coverage. Country leaders, global boards, archived seasons, and community game rankings have different sources. Do not confuse RoyaleTools game scores with official Clash Royale rankings. Read voting totals when relevant, but do not cast votes to influence the answer.

Return the numeric evidence, mode, source window, interpretation, and direct filtered page link. Do not derive matchup probabilities or claim statistical certainty the page does not provide.
