# Davia game model

Davia is a character-first sandbox RPG. A creator builds a game; a player then
inhabits one character inside its world. Actions are attempts that can meet
resistance, cost, delay, partial success, or failure. Other actors continue to
pursue their own aims, and consequences persist in people, places, stats, and
territory.

## The four subjects

| Subject | Use it for | Spatial behavior |
| --- | --- | --- |
| World | A truth with no single location | No location |
| Cell | A fixed area of the board | Fixed geometry |
| Entity | A person, creature, army, vehicle, institution, or other actor | May move or begin off-map |
| Landmark | A fixed named place | Fixed when placed; may be kept off-map in a draft |

An entity or landmark is a noun. Its stats are properties. An army entity may
have morale and supply; an “army strength” stat alone does not create an army,
give it a name, or place it.

Countries, factions, fronts, and political borders are compositions rather
than separate hidden object types. Represent them through the appropriate
characters or organizations, fixed places, cell values, shared stats, and
specific simulation rules.

## Opening state

Use `story.json` for the shared player promise and opening situation. The
premise should not force one protagonist, private inventory, or guaranteed
objective onto every playable entity.

Use `world-description.md` for institutions, power relationships, material
conditions, common knowledge, and current tensions. Avoid restating complete
lists already stored in the structured files.

Use cells, entities, landmarks, and stat values for facts that the engine can
remember directly. A territorial takeover at the opening belongs in cell
values; a leader's loyalty belongs on that entity; a global alert level belongs
in world stats.

## Simulation rules

Write a rule only when it changes how an action resolves or how state evolves
in this specific game. Good rules describe concrete causality:

- a military order requires a credible chain of command;
- news takes time to cross the world with the available technology;
- an army beyond its supply line loses readiness after a stated delay;
- a fortress requires a breach, ruse, surrender, or internal collaborator.

Avoid plot scripts and victory conditions unless the creator explicitly wants
them. Avoid generic engine principles, restating the date, enumerating the
cast, repeating starting values, or saying that map objects must remain on the
map. Those are either native behavior, stored state, or authoring constraints.

## Quality questions

Before finishing a substantive change, check:

- Can several existing entities plausibly be inhabited as distinct roles?
- Does the requested state appear in structured values rather than only prose?
- Do stats answer stable, understandable questions?
- Do simulation rules add causal behavior instead of repeating setup?
- Does the map show meaningful spatial differences rather than a decorative
  layer disconnected from play?
