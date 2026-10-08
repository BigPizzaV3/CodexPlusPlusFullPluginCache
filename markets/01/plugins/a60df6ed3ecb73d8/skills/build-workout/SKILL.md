---
name: build-workout
description: >
  Builds a Hyperhuman team workout from library exercises.
  Use when the user asks to create a workout, assemble exercises and rests,
  or draft a session in their Hyperhuman team library.
  Requires OAuth. Not for guest sample browse, embeds, social drops, pricing, or medical advice.
---

# Build a workout

## Goal

Create a reviewable team workout from explicit structure choices.

## Steps

1. Confirm OAuth. If missing, stop and ask the user to connect Hyperhuman.
2. Gather: name, duration intent, category/difficulty, locale if needed.
3. Load options as needed: `list_team_goals`, `list_workout_categories`, `list_equipment`, `list_muscle_groups`, `list_team_exercises`.
4. For each step: `create_exercise_instance` or `create_rest_instance` with clear duration/reps.
5. Call `create_workout` with the collected `exercise_map` / instances and metadata.
6. Offer `update_workout` only if the user requests edits.
7. Reply with workout id, name, step count, and one next action (open in Teams or adapt).

## Output

- Created workout id + name
- Short structure summary
- Link guidance: manage at team.hyperhuman.cc

## Guardrails

- Explicit invocation preferred; do not invent team content when unauthenticated.
- Respect team library only; do not claim stock was added unless a tool did it.
- No pricing or checkout.
- See [references/create-flow.md](references/create-flow.md).
