---
name: import-recipe
description: Import confectionery recipes from an external source into Formul.io through its MCP server, keeping source quantities, phases and method intact. Use when the user wants to import, digitize, transcribe, save or move in a recipe that already exists somewhere else, such as pasted text, a cookbook page, a web page, a photo you can read, or a file you can read, one recipe at a time. Triggers include "import this recipe", "add this recipe to Formul.io", "digitize my recipe book", "импортируй рецепт", "перенеси рецепт в Formul.io", "оцифруй рецепты из файла". Do not use it for a formula invented in the conversation; that belongs to develop-recipe.
license: MIT
compatibility: Requires the Formul.io MCP server (https://api.formul.io/mcp) with the recipes:read, recipes:write, ingredients:read and calculate scopes; diagnose is optional. Write scopes are granted only when requested at connection.
metadata:
  author: Formul.io
  version: "1.0"
---

# Import a recipe into Formul.io

The goal is a faithful copy of someone else's recipe. Transcribe the source as
it is written and do not improve it. Optimizing is a separate step that the
user asks for after the import.

## Pick the path

| Source | Path |
|---|---|
| One recipe you can read: pasted text, a web page, a photo you can see, a book page | **Structured import**: `import_recipe` |
| A file you can read that holds a few recipes | Read it and import each recipe separately, one `import_recipe` call per recipe, each previewed with the user |
| A long file, a whole recipe book, or a file you cannot read | Point the user to the file import in the Formul.io app, which reviews the whole file and asks about doubtful lines there |
| A scanned PDF without a text layer, or a photo you cannot read | Point the user to the photo import in the Formul.io app |
| A Formul.io export file | Tell the user to restore it in the app, which reads it back exactly |
| A formula the user and you are composing now | Not an import. Use `develop-recipe` |

## Import one recipe

### 1. Transcribe

Record these fields from the source:

- `name`, `description`, and `source_url` for attribution. The server does not
  fetch the URL.
- Every ingredient line **in source order**. Keep a repeated ingredient as
  separate lines when it enters at different points, for example water in the
  syrup and water that dissolves the acid.
- The full method as a `general` note in Markdown, step by step, in the source
  language. Put source tips in `tip` notes and warnings in `warning` notes. The
  tool expects the method to be kept, so never drop it.

### 2. Convert every quantity to grams

`quantity_g` must be greater than 0. Weights convert directly. For everything
else, convert the amount and keep the original in the line `note`, for example
`source: 2 sheets`:

- Volumes: multiply by the ingredient's density (cream ≈ 1.0 g/mL, glucose
  syrup ≈ 1.4 g/mL, honey ≈ 1.4 g/mL).
- Counts: an egg without its shell ≈ 50 g, a yolk ≈ 18 g, a white ≈ 32 g.
  Gelatin sheets vary by grade (gold ≈ 2 g, silver ≈ 2.5 g, bronze ≈ 3.3 g).
- Baker's percentages: ask for the total batch weight first.

Every conversion is an assumption. List the conversions in the review in step 5.
When no reasonable conversion exists, ask the user.

### 3. Choose the calculator, style and phases

- `calculator_type` is one of `ganache`, `caramel`, `dragee`, `patedefruit`,
  `icecream`, `nougat`, `mousse`, or `recipe` (Custom Recipe, freeform) when
  the product fits none of them.
- Call `get_calculator_guide(calculator_type, section="overview")`. Pick the
  `available_styles` entry that matches the source and write it to
  `settings[<style_setting>]`, using the key the guide names, such as
  `ganache_type`. When the style is unclear, leave the default.
- Set `phase` on each line when the calculator routes by phase: ganache
  `chocolate`/`cream`; mousse `base`/`cream`/`gelatin_bloom`; nougat
  `meringue`/`syrup`/`honey`; caramel `finish`; pâte de fruit `acid_solution`,
  used for both the acid and its dilution water. Use `main` for everything else.
- Leave out `stages`. The calculator generates its process graph from the
  settings and phases.

### 4. Preview (writes nothing)

Call `import_recipe(mode="preview")` with every field from steps 1–3. Each line
comes back with a `resolution.status`:

| Status | Action |
|---|---|
| `matched` / `recommended` | Use its `ingredient_id` |
| `alternative` | Pick a candidate by **actual composition**: cream 35 % and 30 % change the result, and so do dark chocolate 64 % and 70 %. When the choice moves the numbers and the source does not settle it, ask the user. A generic name such as "sugar" never binds a specific product. |
| `needs_create` | You need a composition. Rows under `nearest` are marked `match.weak`: they only resemble the name (another percentage, a shared word), so never use one without asking the user. Try `search_ingredients` first; its `reference_candidates` carry USDA/CIQUAL data. Otherwise use the manufacturer's data sheet or ask the user. **Never invent a composition.** |
| `incomplete` | The search failed. Retry later and do not create a duplicate. |

For a branded product, prefer the exact product over a generic one. Keep any
brand the source names.

### 5. Review with the user

Show a table with the source line, the library ingredient or the new custom
ingredient with its data source, the grams, and the phase. Below it, list the
unit conversions and any assumptions. Wait for explicit approval before
writing.

### 6. Confirm (this writes)

Call `import_recipe(mode="confirm")` with the same `name`, `calculator_type`,
`description`, `settings`, `tags`, `notes` and `source_url`. Add `resolved[]`
with **one entry per ordered line**, carrying the same name, quantity, phase
and note as in the preview, plus **exactly one** of:

- `ingredient_id`, or
- `create{...}` with percentages by mass. `water_pct`, `carbohydrate_pct`,
  `fat_pct` and `protein_pct` are required. `carbohydrate_pct` excludes fibre,
  and `alcohol_pct` is the ethanol mass fraction, not ABV. When the same new
  ingredient appears on several lines, repeat the identical `create{}` payload
  on each line.

### 7. Report

Give the recipe's name and `url` from the result, never a bare id. Mention any
`created_ingredients`, `post_commit_warning` or `detail_error`. You can offer
`analyze_recipe` as a next step, but do not change the imported recipe unless
the user asks.

## Rules

- Do not change the source's proportions, substitute ingredients, or "fix"
  quantities during an import.
- Persist only after the user has approved the preview.
- Resolve ingredients in batches and do not search for one name at a time.
- Use grams and °C throughout.
