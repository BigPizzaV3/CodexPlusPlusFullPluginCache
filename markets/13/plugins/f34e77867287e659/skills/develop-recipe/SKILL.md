---
name: develop-recipe
description: Develop a new professional confectionery recipe from a brief with the Formul.io MCP server. The brief is turned into a formula, checked against the calculator's target bands without saving, iterated, and saved only after the user approves. Use when the user asks you to create, develop, formulate or design a new ganache, caramel, pâte de fruit, ice cream or sorbet, nougat, mousse, dragée or custom recipe, especially with targets such as shelf life, water activity, texture, sugar level, or vegan and allergen constraints. Triggers include "create a ganache for bonbons with 3 weeks shelf life", "develop a vegan caramel", "придумай рецепт", "разработай ганаш", "сделай рецептуру под ТЗ". Do not use it to transcribe an existing recipe (import-recipe), to diagnose a saved recipe (improve-recipe), or to design several recipes as a line (prototype-collection).
license: MIT
compatibility: Requires the Formul.io MCP server (https://api.formul.io/mcp) with the calculate, diagnose, ingredients:read, recipes:read and recipes:write scopes; ingredients:write only to add a custom ingredient. Write scopes are granted only when requested at connection.
metadata:
  author: Formul.io
  version: "1.1"
---

# New recipe from a brief

Work through every candidate formula in memory and save once. Every metric
comes from the Formul.io engine; never estimate a number yourself when a tool
can compute it. Ask questions and explain results in the user's language.

Use the connected Formul.io MCP tools and their current input schemas; the host
may prefix tool names. If a required tool or scope is unavailable, say what
cannot be calculated or saved and stop that operation. Never invent tool
results, ingredient ids or a successful save.

## 1. Pin down the brief

Establish these points. Ask only about the ones that are missing **and** would
change the formula; take a stated default for the rest, and do not ask the user
to repeat what the conversation already says.

| Point | Maps to | Default if unstated |
|---|---|---|
| Product | `calculator_type` + style | Ask, since it decides everything else |
| Batch size | total grams | 1000 g, stated |
| Storage and target life | style + `aw` band; `microbial_growth` and `storage_requirement` in the metrics; `shelf_life_room_temp_days` as a reference | the style's Aw band |
| Constraints | vegan, allergen-free, sugar ceiling, no polyols | none |
| Named products | exact brands the user owns | favourites (see step 3) |
| Texture and use | style: bonbon frame, enrobed, piping, spread… | the calculator's default style |

If the user works inside a collection, call `get_collection(collection_id)`.
Its `instructions` and `requirements` are project preferences to honour within
the user's request.

## 2. Read the target

Call `get_calculator_guide(calculator_type, style=...)`. The default section
returns:

- `optimal_ranges` for **this style**. Bands differ sharply between styles; a
  sorbet's fat band is not an ice cream's.
- `formulation_rules`: the stabilizers, emulsifiers and anti-crystallization
  agents a professional formula needs. Follow them.
- `settings_schema` and `style_setting`, the settings key that stores the style
  (for example `ganache_type`).

Fetch the guide once per calculator and style and reuse it. Do not invent
process temperatures, times or yield the guide and the user did not give; label
a process choice of your own as a proposal.

## 3. Draft and resolve

1. Write a first formula from professional practice so that the ingredients add
   up to the batch weight. It is a new formulation, distinct from any source
   recipe's quantities.
2. Resolve **all** the names in one `resolve_ingredients` call (at most 25
   names):
   - `matched` / `recommended`: use the id.
   - `alternative`: pick by actual composition (fat %, cocoa %, water %). An
     alternative or a generic category name is not an exact match for a named
     product.
   - `nearest` rows (`match.weak`) only resemble the name, such as another
     percentage of the same line. Never use one without the user's consent.
   - `needs_create`: call `search_ingredients` with `mode="selection"` and
     characteristics, for example
     `{"field": "fat", "operator": "near", "value": 35}` for 35 % fat
     cream. If nothing fits, propose
     `create_ingredient` with sourced composition and **ask first**, because it
     writes to the user's library. Never invent a composition.
3. When the user named nothing, prefer rows flagged `is_favorite` and then
   `is_favorite_brand`. Never swap a product the user named.
4. Give each line a phase where the calculator routes by phase: ganache
   `chocolate`/`cream`; mousse `base`/`cream`/`gelatin_bloom`; nougat
   `meringue`/`syrup`/`honey`; caramel `finish`; pâte de fruit
   `acid_solution`. Use `main` for everything else. Send the same phases in
   every ad-hoc call and in `create_recipe`, so the prototype computes exactly
   the process the saved recipe will run.

## 4. Iterate without saving

- Call `simulate_changes` with an **ad-hoc baseline**: `calculator_type`,
  `ingredients` (`ingredient_id` + `quantity_g` + `phase`), and `settings`
  including the style key. Put every candidate adjustment into **one call**,
  with up to 20 named `scenarios` of `add`/`remove`/`update`/`substitute`
  changes. A change's amount is `quantity` in grams, not `quantity_g`. Each
  scenario returns its deltas against the bands.
- A row that a scenario `add` change introduces enters as `main`. To try an
  addition in another phase, put it in the baseline `ingredients` with its phase
  instead.
- When you need a single formula's full metrics, use `get_recipe_metrics` with
  the same ad-hoc shape.
- Read the bands carefully. A missing metric is not a passing result. For `aw`
  and free water, being below the band is a texture or yield miss, not a safety
  risk. Adding water to close that gap makes the product **less** stable.
- If proportions stop moving a metric toward its band, call
  `advise_formulation` with the ad-hoc formula. It reports which metrics the
  current ingredients cannot reach and which class of ingredient would unlock
  them, such as a humectant or invert sugar. Add that component and do not keep
  re-weighing.
- Stop after about three rounds and show the user where things stand. Do not
  loop silently.

## 5. Present for approval

Show:

- A formula table with ingredient, grams, % of the batch, and phase.
- Key metrics against their bands, marking each in band or out of band with the
  direction.
- The trade-offs you chose and anything still out of band, with the reason.
- One `show_card` call for the final formula (`kind:"metrics"`, or
  `kind:"comparison"` with the final `simulate_changes` arguments), so the user
  sees the card. The calculation tools show no card, so call it only once.

Shelf life and water activity are model predictions. For a product that will be
sold, recommend confirming them with a measurement, such as a water activity
meter or a challenge test.

## 6. Save (after an explicit yes)

An instruction to save or create the recipe in Formul.io is that yes; do not ask
for it again. A request to explore or compare is not permission to write.

1. Call `create_recipe` with `name`, `calculator_type`, `description` (the brief
   in one sentence), `tags`, `settings` (with the style key), and `ingredients`
   as `ingredient_id` + `quantity_g` + `phase`.
2. If the result has `status: "resolution_needed"`, resolve the listed names and
   retry. Retrying is safe because nothing was saved. If the outcome of a write
   is ambiguous, check `list_recipes` for the recipe before creating it again.
3. The receipt carries the new recipe in `entity` (`id`, `name`, `url`). Call
   `analyze_recipe` with `entity.id` and report the quality score and any
   flagged issues. Fix an issue only if the user asks, using `update_recipe`
   with `save_as_version: true` and the `revision` from `get_recipe` as
   `expected_revision`.
4. Offer to record the design reasoning with
   `save_recipe_note(note_type="rationale")`. For example: why 12 % invert sugar,
   or why this couverture.
5. Give the recipe's name and `url`, never a bare id.

Every plan can create recipes and save notes. If a write returns
`entitlement_required`, that tool is a Pro feature on this account. When it is
`create_ingredient`, save the formula with `import_recipe` (`mode="confirm"`),
whose `create{...}` lines add the custom ingredients. Otherwise say so with the
plans link from the refusal, do not retry, and give the user the final formula
table so they can enter it in the app.

## Rules

- Never compromise food safety or declared allergens to hit a metric.
- Use grams and °C, and professional formulations only.
- Do not save intermediate drafts. Save only the formula the user approved.
- To modify an existing recipe, use `update_recipe`. Use
  `create_recipe(from_recipe_id=...)` only when the user wants a separate copy.
