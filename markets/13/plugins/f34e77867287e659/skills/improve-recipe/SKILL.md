---
name: improve-recipe
description: "Diagnose an existing Formul.io confectionery recipe, compare calculated improvements, and optionally save a chosen variant. Use for recipe troubleshooting, reformulation, or ingredient substitutions; not for starting a new formula or organizing collections."
---

# Improve Recipe

Turn a saved recipe and a concrete problem into a comparison the confectioner can
act on. Explain the trade-offs in the user's language. Keep the original recipe
unchanged during diagnosis and simulation.

## Establish the baseline

- Use the connected Formul.io MCP tools and their current schemas. If access is
  unavailable, say what is missing instead of inventing recipes or results.
- Reuse the recipe ID or exact name already supplied. Otherwise find it with
  `list_recipes`; resolve ambiguous matches before analysis or edits.
- Read `get_recipe` with `include:["analysis"]`; request `view:"full"` when the
  complete settings or metrics are needed. This provides the current ingredient
  rows, calculator type, settings, and diagnosed issues. Use `analyze_recipe` when
  analysis was not obtained with the recipe.
- Connect the complaint to the actual product and intended use: for example,
  softness in a bonbon filling versus fluidity in a sauce. Reuse known batch size,
  style, available ingredients, and dietary constraints; ask only for missing
  information that changes the recommendation.
- Obtain `get_recipe_metrics` when target bands or relevant metrics are missing.
  Its bands are calculator- and style-specific. Do not use a generic threshold
  from memory. Consult `get_calculator_guide` for formulation rules or settings
  needed to optimize this recipe, not just to repeat bands already returned.

## Compare targeted changes

- Propose a small, useful set of alternatives tied to the stated problem. Keep
  batch size and explicit ingredient identities fixed unless changing them is
  part of the request. Do not substitute a named product merely to improve a score.
- Pass the saved `recipe_id` and named `scenarios` to `simulate_changes`. Use one
  call for the alternatives so they share the same unchanged baseline. Changes
  support `add`, `remove`, `update`, and `substitute`; use returned ingredient IDs.
- A change's amount is `quantity` in grams, not `quantity_g`. An `update` quantity
  is the new total for that ingredient across all rows, split proportionally.
  A `substitute` needs `ingredient_id` and `substitute_id` and affects all matching
  rows; omitting its quantity preserves their amounts. Simulation does not support
  editing a single row by `entry_id`. Never claim a narrower change was previewed.
- Use `find_substitutes` for an actual availability or composition constraint.
  Its `criteria` filters candidates rather than re-ranking them. Review returned
  composition, allergens, and identity; pass the selected `suggested_change` into
  a scenario. Prefer suitable favorites only when the user left the choice open.
- If changing amounts cannot achieve a target, use `advise_formulation` to check
  achievable ranges and missing ingredient classes. It does not choose a recipe
  or a trade-off. Stop iterating when evidence cannot support an improvement.
- The calculation tools show the user no card. Show the final comparison once
  with `show_card` (`kind:"comparison"`, the same arguments as that
  `simulate_changes` call). Report failed or ineffective scenarios instead of
  treating missing results as success.

## Recommend and optionally save

Show the relevant baseline values, candidate values, exact ingredient changes,
and practical trade-offs. Distinguish calculated predictions from observed kitchen
results; do not guarantee texture, food safety, or shelf life from model output.
For a `lower_is_safer` metric, a value below the band is not a safety failure:
adding water to reach the floor can reduce stability. Suggest a focused kitchen
trial when a predicted improvement needs sensory or process validation.

Diagnosis, comparison, and recommendations do not authorize saving, notes, or
versions. Follow an existing explicit save instruction without asking again; if
the chosen variant or destination is unclear, clarify before writing.

- To retain the original as a separate recipe when the user requested a copy,
  call `create_recipe` with `name` and `from_recipe_id`. Read the new recipe using
  the receipt's `entity.id` as `get_recipe.recipe_id`, then apply changes to its
  new ID and row IDs; cloning alone does not apply a
  simulated scenario.
- Before an authorized overwrite, inspect `list_recipe_versions`. This tool lists
  metadata, not full snapshots or a restore API. Do not promise that unsaved
  baseline state can be recovered.
- Apply an approved variant with `update_recipe`. It accepts `set_ingredients`,
  not simulation change objects. Read the current recipe and send the full list,
  preserving retained `entry_id`, phases, stage pins, incorporation modes, notes,
  exclusions, and locks. Preserve all settings if replacing `settings`; omit
  unchanged top-level fields. Omit null notes because the write schema takes text.
- Pass the `revision` from that read as `expected_revision`. A
  `CONCURRENT_MODIFICATION` refusal means the recipe was saved elsewhere (in the
  app or by another agent) since you read it, and nothing was written: read it
  again, re-apply the chosen change to the new state, and only then retry. The
  receipt's `revision` is the `expected_revision` of a following update.
- `save_as_version:true` snapshots the state AFTER supplied edits, not the old
  baseline. With no changes it snapshots the current state. Make either snapshot
  only when requested or already authorized; `version_description` requires
  `save_as_version:true`.
- Verify the returned save receipt, then read the saved recipe to check the
  chosen changes. Return its actual app link and state whether the original was
  retained, updated, or left untouched. Do not blindly retry an ambiguous write.

## Example

“My dark chocolate bonbon filling is too soft. Compare two adjustments with the
ingredients I already use, keep the batch weight, and don't change my recipe.”

Find the recipe, inspect its actual style and analysis, and compare two targeted
quantity changes in one simulation. Present the comparison card and a kitchen
trial recommendation. Leave the recipe, version history, and notes unchanged.
