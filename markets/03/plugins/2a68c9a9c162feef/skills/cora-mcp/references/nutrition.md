# Nutrition tool map

Use deterministic reads and copies when the data already exists. Use AI
estimation only for newly described or hypothetical food.

## Route by record type

| Intent | Read or resolve | Act | Verify or avoid |
|---|---|---|---|
| Read an exact completed day | `cora_get_nutrition` | — | Returns logged entries/items and IDs; not planned meals. |
| Read current macro targets | `cora_get_nutrition_goals` | — | Read-only; do not claim the MCP can set goals. |
| Find a vaguely referenced log | `cora_search_nutrition` with `source="entries"` | Usually `cora_duplicate_nutrition` | Search food keywords, not phrases such as “last Tuesday.” |
| Find a saved template | `cora_search_nutrition` with `source="templates"` | Usually `cora_duplicate_nutrition` | Keep `template_id` distinct from entry and planned-meal IDs. |
| Read future meals | `cora_get_planned_meals` | — | Plans are not completed diary entries. |
| Log genuinely new food eaten | — | `cora_log_nutrition` | AI-estimates and saves; do not use to recreate known Cora data. |
| Re-log a known entry/template | Resolve exact typed ID | `cora_duplicate_nutrition` | Re-read target day and compare source values. |
| Scale/delete a whole logged entry | `cora_get_nutrition` or search | `cora_edit_nutrition` | Destructive at entry scope; no item-level edit/remove. |
| Estimate without saving | — | `cora_analyze_meal` | Paid AI; analysis is not a diary write. |
| Save a future meal/template | Check `cora_get_planned_meals`; analyze if needed | `cora_plan_meal` | Does not log food as eaten or set a reminder. |
| Set/replace/clear coaching notes | Read the day's current notes | `cora_set_meal_note` | Scope to the exact date and general/per-meal note key. |

## Reuse known nutrition records

### Exact dated entry

When the user asks to repeat a logged meal and identifies its day exactly or
relatively, use this sequence:

1. Normalize the source and target dates in the user's timezone.
2. `cora_get_nutrition(date=<source_date>)`
3. Resolve one exact `entry_id` from the requested meal context; ask if
   multiple entries are plausible.
4. `cora_duplicate_nutrition(source="entry", source_id=<entry_id>,
   date=<target_date>)`
5. `cora_get_nutrition(date=<target_date>)`
6. Compare source and target title, meal slot, food/items, portions, servings,
   calories, macros, and local consumed time when returned.

Do not call search for an exact day. Do not call log/analyze/coach for a known
meal. If readback contains missing, zeroed, or changed source values, report
that the copy was not exact and do not duplicate again.

### Vague past entry

Search `source="entries"` using food-name keywords only. Use returned dates
and titles to disambiguate, then duplicate the selected `entry_id`. A relative
date in the user's sentence constrains selection after search; it is not a
fuzzy food query.

### Saved template

Search `source="templates"`, resolve the exact `template_id`, then duplicate
with `source="template"`. Do not substitute `cora_plan_meal`; a reusable
template and a scheduled planned meal are different records.

## Preserve analyze-to-plan data

When the user provides free-form food for a future date, call
`cora_analyze_meal` if structured nutrition is needed, then pass the returned
item fields to `cora_plan_meal`. Do not silently drop item quantities or
nutrition fields. Check for an existing planned meal in the requested date and
slot before creating a duplicate plan.

## Stop at unsupported boundaries

- Resolve a planned meal when the user says it was eaten, then explain that
  no deterministic `logPlannedMeal` equivalent exists. Do not silently call
  log, analyze, or duplicate as a lossy substitute.
- Do not claim to set calorie, macro, or weight goals; nutrition goals are
  read-only through this MCP.
- Do not use whole-entry scale/delete to imitate item-level update/removal.
- Do not claim a logged entry can be saved losslessly as a template; the plan
  tool has no source-entry input.
- Do not edit or delete a planned meal; those mutations are not exposed.
