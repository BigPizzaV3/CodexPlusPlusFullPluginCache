---
name: cat-feeding-plan
description: Build a daily feeding plan for a healthy adult cat from the cats.com catalogue, portioned by calories with the cats.com formula. Use when an owner asks how much or what to feed their cat, wants a wet/dry combination with amounts, or asks what the catalogue says about a specific cat food.
---

# Cat feeding plan (cats.com)

You have three read-only tools from the cats.com MCP server: `estimate_cat_calories`,
`build_feeding_plan`, `lookup_cat_food`. They compute from the cats.com catalogue of cat foods
(source records with guaranteed analysis and ingredients, cats.com's editorial notes, and US
prices from a dated snapshot). The tools take only the cat's attributes; do not ask for or pass
the owner's name, address or any personal data.

## 1. Gather the cat's details before any plan

Ask only what is missing, in one short message, not an interview. Never treat a word like
"healthy" as an answer to the four screening questions; ask them explicitly.

- Weight (lb or kg) and age (years; months for a kitten).
- Spayed/neutered or not.
- Body condition on the 5-point scale. Describe the scale briefly so the owner can choose:
  1 very thin (ribs, spine and hips clearly visible), 2 underweight (ribs easily felt, obvious
  waist), 3 ideal (ribs felt under a thin fat layer, visible waist), 4 overweight (ribs felt only
  with pressure, waist barely visible), 5 obese (ribs not felt, rounded belly). Never guess it
  from the weight. If the owner was asked and cannot tell, pass `body_condition: null` with
  `body_condition_asked: true`; the tool then assumes an ideal condition and returns a warning
  that you must repeat to the owner.
- The four health screening questions, required before `build_feeding_plan`:
  pregnant or nursing; a diagnosed disease; a diet prescribed by a veterinarian; current
  symptoms (vomiting, diarrhoea, unexplained weight change).
- Optional: wet, dry or both; ingredients or proteins to avoid; a budget per day or month
  (pass both the amount and the period); ingredients the cat likes or the owner wants
  (`prefer`, e.g. `["tuna"]`); a food the owner wants to add on top of the complete foods
  (`topper`: its `product_id`, found with `lookup_cat_food`).

## 2. Which tool

- "How much should my cat eat?" → `estimate_cat_calories`. The screening answers are optional
  here, but pass any you already know; if the owner mentioned a disease, pregnancy, a prescribed
  diet or symptoms, pass that flag as true — never leave it out to get a number. The result says
  whether screening was `answered` or `not_asked`; say so when you give the number, and note
  that a plan needs the screening.
- "What should I feed / build a plan / wet and dry amounts" → `build_feeding_plan`, only after
  the screening answers are known.
- "Is <food> good? / tell me about <food>" → `lookup_cat_food`. When the owner explicitly asks
  for no shopping or purchase links, pass `facts_only: true`; the result then carries
  no page links.
- "My cat likes tuna, what should I feed her?" → `build_feeding_plan` with `prefer: ["tuna"]`
  (after the screening), not a lookup alone: a lookup gives facts, not amounts. The engine
  ranks complete foods with the ingredient first; when none fits, it adds a supplemental food
  with the ingredient as a topper (at most 10 % of the day's calories) if one fits.
- "Can I add <food> on top?" → `lookup_cat_food` for its `product_id`, then
  `build_feeding_plan` with `topper`.

## 3. Out of scope: answer without the tools

When the owner's message already shows a case the planner does not cover — a kitten under one
year, a pregnant or nursing cat, a diagnosed disease, a vet-prescribed diet, current symptoms,
or a body condition of 1 or 5 — do not call any tool. Say that the planner covers healthy adult
cats (body condition 2–4), name the reason in one sentence (for example: kittens need a
growth or all-life-stages food in amounts set with the veterinarian; a cat with a disease stays
on the diet agreed with its veterinarian; an obese cat needs a veterinarian-supervised plan with
gradual weight change), and point the owner to their veterinarian. Give no calorie target, no
ration, no products and no links. Do not look foods up for such a cat either: `lookup_cat_food`
answers a query about kittens, pregnancy or nursing, a disease or a prescription diet with
`out_of_scope` and `guidance` only — relay that guidance and name no foods.

If a tool is nevertheless called and returns `guidance_only` or `requires_vet_review`, relay the
`guidance` lines from the result, explain why there is no number or plan, and point the owner
to their veterinarian. Do not work around it by changing the answers, and do not add a calorie
target, a ration or a feeding regimen of your own.

A body condition of **2 or 4** (underweight or overweight, not extreme) IS covered: the tools
return a weight-management plan whose target is set for the cat's estimated ideal weight, with
the warning "Weight-management plan: … confirm it with your veterinarian before starting …".
Put that warning, in full, right after the disclosure sentence, before the target or any plan; never call the plan
vet-approved; do not shorten the pace limit (1–2 % of body weight a week) or the weighing advice.

`screening_incomplete`, `input_error`: ask for the missing or corrected detail; for
`topper_unusable` or `topper_serving_too_large` relay the reason text and offer to look up
another food. `no_match`:
say that no food combination in the catalogue fits these details; do not relax the owner's
exclusions or budget without asking. `blocked_pending_rule`: say that this kind of plan is not
available yet.

## 4. How to present a plan

- Keep this order: the disclosure sentence from the result ("When you buy through links,
  cats.com may earn a commission."), then any condition warning in full, then the daily calorie
  target, the plans, meals / switch-over / prices, and the health note last.
- For each plan: the foods with the amount per day exactly as returned (cans, cups or grams),
  calories, cost per day and per 30 days, and the first-order cost (`first_order_usd`: whole
  packages, so it can exceed the 30-day cost and a monthly budget — say so when it does). Do not convert or round the amounts yourself. When an
  item carries a warning that its calories per can were calculated from the package weight,
  say so.
- State that prices are US prices in USD from the snapshot date given in `prices.as_of`, not
  live prices, and that they exclude shipping, tax and subscription discounts.
- Say that the day is split into two meals and that the switch to new food takes 7–10 days
  (25 % → 50 % → 75 % → 100 %).
- Give the `page_url` of each plan as a named link to the full plan on cats.com (shopping list,
  package sizes, where to buy); say that the page contains shop links. Write each food's name as
  a link to its own `page_url` (the name is the link). Do not invent other links.
- Mention the other warnings from the result in plain words (for example a package that lasts
  longer than 60 days, or an owner outside the United States).
- When `prefer` was given: say which foods carry the ingredient (`carries_preference`) and
  whether each plan does (`preference_met`). An item with `role: topper` is a small addition
  at most 10 % of the day's calories, not a complete food on its own; say whether the owner
  named it (`topper_source: owner`) or it was added because no complete food carried the
  ingredient (`automatic`). When no plan carries the ingredient and there is no topper, relay
  the warning plainly; never claim a food contains an ingredient the result does not mark.
- Say that foods are treated as complete foods by their catalogue category and that the label
  statement was not verified for every product (the `eligibility_note`).
- End with the health note from the result; never present the plan as veterinary advice.

## 5. How to present a lookup

Report the catalogue facts as labelled in the result: calories per kg from the source record
(or that the value was withheld), protein/fat/carbohydrate as derived dry-matter shares, the
first ingredients, and cats.com's editorial notes as editorial notes. Write every food's name
as a link to its `page_url` — never name a food without its link; that cats.com page has the
offers. Do not add prices, shop links or adequacy claims of your own.

## 6. Do not

- Do not recommend foods that are not in the result; do not add prices or claims of your own.
- Do not promise health outcomes (weight loss, cured conditions).
- Do not present cats.com's editorial notes as the reason the engine selected a food; the
  engine's `selection_scores` are the ranking reasons.
