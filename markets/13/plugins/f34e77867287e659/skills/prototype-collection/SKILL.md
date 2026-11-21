---
name: prototype-collection
description: Prototype a product line of confectionery recipes as a Formul.io collection through its MCP server, such as a bonbon box, a seasonal menu, an ice cream range, or a set of fillings. The line is planned against shared requirements, each item is formulated and checked against those requirements without saving, and the approved recipes are saved together into one collection with its requirements and working instructions. Use when the user wants several related recipes designed as a set, such as "design a 9-piece Christmas bonbon box", "build a summer sorbet range, all vegan", "prototype a nut-free filling line with 4 weeks shelf life", "собери коллекцию конфет", "прототип линейки", "набор рецептов для коробки". For a single recipe use develop-recipe; to gather recipes that already exist into a collection, use build-collection.
license: MIT
compatibility: Requires the Formul.io MCP server (https://api.formul.io/mcp) with the calculate, diagnose, ingredients:read, recipes:read and recipes:write scopes. Write scopes are granted only when requested at connection.
metadata:
  author: Formul.io
  version: "1.0"
---

# Prototype a recipe collection

A line is designed as a whole. Decide on the plan and the shared requirements
before you formulate anything, formulate every item without saving, review the
whole line at once, and save only after the user approves.

## 1. Brief for the line

Establish these points. Ask one grouped question for whatever is missing and
material.

- **Theme and count**: for example "9 winter bonbons" or "6 sorbets".
- **Product types**: one calculator for the whole line, or a mix such as
  ganache, caramel and pâte de fruit layers.
- **Shared requirements**, stated measurably where possible: shelf life at room
  temperature, storage, allergens (nut-free, gluten-free), vegan or halal, a
  sugar ceiling, a shared couverture or base.
- **Channel**: retail box, restaurant or wholesale. The channel drives the
  shelf life and the style.

## 2. Check what already exists

- `list_collections(search=...)`: if the collection already exists, continue in
  it. Call `get_collection(collection_id)`; its `instructions` and
  `requirements` are project preferences to honour within the user's request.
- `list_recipes(search=..., calculator_type=...)`: the user's own recipes can
  join the line as they are, or serve as a starting point. To derive a new item
  from one, formulate a variant and save it as a new recipe; never edit the
  original.

## 3. Plan the line (no formulation yet)

Present a plan table: #, working name, calculator and style, flavour concept,
what sets it apart within the line, and its source (new, existing recipe, or a
variant of an existing one).

Guidelines:

- Give each item a distinct role: contrast textures, flavours and colours
  across the box.
- Share base ingredients between items (one couverture, one cream, one glucose)
  so purchasing and production stay simple.
- Choose each item's style from `available_styles` in
  `get_calculator_guide(calculator_type, section="overview")`. The styles of
  items in one box must agree with the line's storage requirement.

Also turn every requirement into a check:

| Requirement | How it is checked |
|---|---|
| "keeps 3 weeks at room temperature" | `storage_requirement` is `ambient` and the reference `shelf_life_room_temp_days >= 21` in the metrics |
| "Aw at or below 0.80" | the `aw` metric |
| "nut-free", "vegan", "gluten-free" | the `allergens` and vegan flag on each `search_ingredients` row; search with `exclude_allergen_ids`, `vegan_only` or `gluten_free_only` |
| "same couverture everywhere" | the same `ingredient_id` in every item |
| Qualitative ("seasonal flavours") | checked by reading the plan |

**Get the user's approval of the plan before formulating.** Changing the plan
costs nothing at this point.

## 4. Formulate every item without saving

1. Call `get_calculator_guide(calculator_type, style=...)` once for each
   distinct calculator and style pair. Reuse the result for every item that
   shares the pair. Follow its `formulation_rules`, and put the style in
   `settings[<style_setting>]`.
2. Resolve the ingredient names of the **whole line** with `resolve_ingredients`
   in as few calls as possible, at most 25 names per call. When the user named
   nothing, prefer favourites (`is_favorite`, then `is_favorite_brand`).
3. For each item, call `simulate_changes` with an ad-hoc baseline
   (`calculator_type`, `ingredients`, `settings`) and put all of that item's
   candidate tweaks into one call as `scenarios` (at most 20). Give each
   ingredient the `phase` it will be saved with (pâte de fruit
   `acid_solution`, nougat `syrup`/`meringue`/`honey`, mousse
   `base`/`cream`/`gelatin_bloom`, caramel `finish`, ganache
   `chocolate`/`cream`, otherwise `main`), so the prototype computes the same
   process as the saved recipe. A row that a scenario `add` change introduces
   enters as `main`; to try an addition in another phase, put it in the
   baseline instead.
4. When an item cannot reach a band through proportions, call
   `advise_formulation`. It tells you which class of ingredient is missing.
5. Limit yourself to about three rounds per item. If an item still fails,
   record it for the review and do not keep iterating.

## 5. Review the whole line

Show one matrix. Each row is an item. The columns are its key metrics (value
against band) and a ✓/✗ for every requirement from step 3, with the actual
value. Below the matrix:

- the items that fail a requirement, with options: change the style, add a
  component, relax the requirement for that item, or drop the item
- the shared base ingredients and the total batch weight for each item
- a reminder that shelf life and Aw are predictions, and that a product for
  sale needs measurement

Iterate on single items as the user directs. Get an explicit approval of the
final line before writing anything.

## 6. Save the line (after an explicit yes)

Keep this order. It avoids an empty or duplicate collection when something
fails halfway.

1. **Recipes first.** Call `create_recipe` once for each approved item, with
   `name`, `calculator_type`, `settings` (including the style key),
   `ingredients` (`ingredient_id` + `quantity_g` + `phase`), a one-line
   `description`, and a shared line tag in `tags`. Collect the returned ids. If
   a call returns `resolution_needed`, resolve the names and retry that item. If
   a call fails, stop and report exactly which items were saved.
2. **Collection in one call.** Call `save_collection` with no `collection_id`,
   and pass:
   - `name` and `description`
   - `requirements`: one measurable target per line, as agreed in step 3
   - `instructions`: working guidance for future sessions, such as the shared
     base ingredients, the chosen styles, and what not to change
   - `add_recipe_ids`: every id from step 1

   This creating call is **not idempotent**. Never retry it blindly: run
   `list_collections` first to see whether the collection landed.
3. To add an item to an existing collection, call
   `save_collection(collection_id, add_recipe_ids=[...])`.
4. The collection is private. To share it, point the user to its settings in
   the Formul.io app; the tools cannot publish it.

Every plan can create the recipes; collections are a Pro feature. If
`save_collection` returns `entitlement_required`, say so with the plans link
from the refusal, do not retry, and list the saved recipes by name and `url`
plus the requirements text.

## 7. Report

List the collection and each recipe by name and `url`, never a bare id. Offer
next steps: `analyze_recipe` on each item for its quality score, or
`save_recipe_note(note_type="rationale")` to record why each item looks the way
it does.

## Later sessions inside the collection

Start with `get_collection(collection_id)` and treat its `instructions` and
`requirements` as the project's standing preferences. Change a member recipe
with `update_recipe(save_as_version: true)`, so the line keeps its history, and
pass the `revision` from `get_recipe` as `expected_revision` so an edit saved
in the app meanwhile is not overwritten.
Re-check that recipe against the collection's requirements after every change.

## Rules

- Do not save anything during the prototyping phases. Formulate ad hoc until
  the user approves.
- Never trade away a declared allergen or safety requirement to make an item
  fit.
- Use grams and °C, and professional formulations only.
