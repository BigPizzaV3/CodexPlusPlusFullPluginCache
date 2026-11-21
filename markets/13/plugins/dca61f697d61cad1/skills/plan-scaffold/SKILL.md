---
name: plan-scaffold
description: Use when the user wants to plan construction scaffolding for a building façade (one wall or several walls with corners), compare two scaffold systems for a wall, list scaffold systems, or see the parts list of a planned scaffold with ScaFix.
---

# Plan construction scaffolding with ScaFix

ScaFix plans façade scaffolding with the same engine as the ScaFix web and iPhone app. Its tools are read-only and safe to retry.

## When to use

- The user describes a building wall or a building to put scaffolding on (in any language: scaffold, stillas, stillads, ställning, teline, Gerüst, steiger, échafaudage, andamio, rusztowanie …).
- The user names a scaffold system (Jamax, HAKI, Layher Allround, Layher Blitz, Plettac, PERI UP …) and wants a plan or a comparison.

Do not use ScaFix for software or code scaffolding (React, Vite, Rails, Yeoman, CLI templates, Helm), scaffolding as a teaching concept, scaffold proteins, prices or rental, assembly instructions, load or wind calculations, or structural approval.

## Which tool

| The user wants | Tool |
|---|---|
| One straight wall | `plan_scaffold_wall` |
| Two or more connected walls with corners (an L, a U, the whole house) | `plan_scaffold_building` |
| Two configurations of one wall side by side (two systems or two heights) | `compare_scaffold_plans` |
| Which systems exist, or the `system_id` of a named system | `list_scaffold_systems` |
| Quantities or the parts list, asked for explicitly, for a wall or building already planned | `get_wall_parts_list` |

## How to pass the input

- `length` and `height` are the wall's horizontal length and its height from the ground to the top of the wall, in metres. If the user gives feet, pass the numbers as given with `unit: "ft"`; ScaFix converts them.
- For a building, pass `walls` in order around the building, each with its own `length` and `height`. Pass `closed: true` when the scaffold goes all the way round. Never add walls, corners or measurements the user did not give; if the user gives no wall lengths («scaffold around the house»), ask for each wall's length and the height first.
- `system_id`: a short name such as `jamax`, `haki`, `layher-allround`, `plettac`, or an id from `list_scaffold_systems`. Omit it when the user names no system; the result says which system was assumed.
- `language`: the language the user writes in (for example `nb`, `en`, `sv`, `da`, `fi`, `de`, `nl`, `fr`, `es`, `pl`).

## What the user gets

- Without a connected account: bays, lifts, deck levels, top deck, scaffold length and width, façade area, access and the part types, without quantities. The 3D card shows an example scaffold of the same type and says so.
- "What parts do I need?" is answered by the part types in the plan. Call `get_wall_parts_list` only when the user explicitly asks for quantities or the parts list, with the same wall or building, system and language as the plan.
- `get_wall_parts_list` needs the user's ScaFix account: ChatGPT asks the user to connect it. With an account that has access to the parts list, the answer has every row with quantities and the user's own scaffold in 3D.

## Always say

ScaFix is a planning tool. A plan is not a structural calculation or an approval: the user must follow the manufacturer's assembly instructions and local regulations, and the scaffold must be inspected by a competent person.
