---
name: davia-creation
description: Create and edit Davia games through the Davia Creation MCP. Use whenever a creator asks to design, inspect, revise, rebalance, or complete a game, including its premise, world, simulation rules, stats, cells, entities, landmarks, or starting state.
---

# Davia creation

Help the creator build a character-first sandbox RPG: a player inhabits one
character inside a world that has geography, other actors, material limits,
and persistent consequences. Keep the creator's intended game central. The
files are a representation of that game, not the creative goal by themselves.

## Start every task this way

1. Call `list_drafts`.
2. If no game is active, identify the intended game by its display name and
   call `select_draft`. Never guess an id.
3. Read [`references/editing-with-the-mcp.md`](references/editing-with-the-mcp.md).
4. Read the current files that govern the requested change. Use `grep` to find
   related names, stat ids, values, and rules across the game.
5. Explain any creative choice that would materially change the premise,
   playable cast, map meaning, or simulation. When the creator already gave a
   precise instruction, carry it out without reopening settled decisions.
6. Make focused edits, then reread the changed files to verify the resulting
   state.

Use the language of the creator's first message for conversation and visible
game content. Keep technical keys exactly as the files expose them.

## Route the work

- Read [`references/game-model.md`](references/game-model.md) when shaping the
  premise, world, playable roles, map meaning, or simulation rules.
- Read [`references/stats-contract.md`](references/stats-contract.md) before
  creating or changing stat definitions or values.
- Read
  [`references/entities-and-landmarks.md`](references/entities-and-landmarks.md)
  before changing a character, group, place, or placement.
- Read [`references/map-assets-catalog.md`](references/map-assets-catalog.md)
  only when the creator asks for a 3D asset recommendation. The current MCP
  does not expose asset assignment for editing.

## Keep authored state separate from simulation rules

Put what is true at the opening in the premise, world description, entities,
landmarks, cells, and starting stat values. Put only causal, game-specific
constraints in simulation rules.

For example, if the creator says that one bloc controls all of Africa at the
start, update the relevant premise or world context and the applicable cell
values. Do not invent a new simulation rule merely to restate that starting
state. A rule belongs only when it changes how later actions resolve, such as a
specific supply delay, legal constraint, or chain-of-command requirement.

Do not repeat Davia's native principles in every game. Generic statements such
as “the world evolves,” “actions have consequences,” or “no future is fixed”
consume attention without making this particular world behave differently.

## Respect current capability boundaries

The MCP can add, edit, and remove entities and landmarks through their complete
objects in `entities.json` and `landmarks.json`. Read the entity and landmark
reference before doing so because creation requires a duplicate check and new
landmarks require a precise on-map placement.

The MCP can append complete stat definitions to `stats.json`. Existing stat
identities and order remain fixed, and stat definitions cannot be removed. The
MCP does not add or remove cells, change cell geometry, or assign 3D assets.
Never claim that one of those unsupported operations succeeded. Use the
editable fields to make as much progress as possible and state the exact
remaining Creation Hub action when a requested change crosses those bounds.
