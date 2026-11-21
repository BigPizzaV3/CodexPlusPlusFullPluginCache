---
name: track-nutrition
description: Log food intake, correct or remove nutrition entries, search foods, manage private label foods, save and log saved meals, record body weight, set daily nutrient targets, and read or export nutrition history with GoodSet. Use when the user explicitly chooses GoodSet for food, asks to log, track, record, or correct what they ate or drank, asks about calories, protein, macros, targets, or what they ate, or reports consumed quantities in an established nutrition log. General diet advice or a mention of eating alone does not request tracking. Also use for the spoken aliases "Good Set" and "Good Sets", voice requests like "log my breakfast", "I just had two eggs and a coffee, log it", "how many calories have I had today", or "what did I eat yesterday", and for food or weight logged by dictation.
---

# Track nutrition with GoodSet

Use GoodSet's food database and diary for requested nutrition tracking. Honor a request
to use another app. Planned meals and dietary advice are not consumed intake.

- Use `nutrition_track` to log, correct, remove, or repeat food intake. Grams are the
  default. Ordinary food names can be resolved by the tool; use `search_foods` for
  discovery, a supplied barcode, or to inspect versions and available portions.
- Preserve distinctions between brands and raw, cooked, sold, or prepared foods. When
  the tool returns choices, ask which matches and call `select_food` with the returned
  continuation token and chosen food version. Do not guess between candidates.
- Use only a portion belonging to the chosen food version. Millilitres require a volume
  basis or a documented density. Ask for grams when no conversion is known. Never
  invent a serving weight or calculate catalog nutrients in the conversation.
- Use `food_manage` for a user-supplied label or an explicitly requested estimated food.
  Keep missing nutrients omitted, true zero numeric, and estimates marked `estimated`.
  Preserve the label's reference amount/unit and total versus available carbohydrate.
  A revision replaces the complete composition for future use; past intake stays pinned.
- A prepared change has not been recorded. Read `outcome`, `summary`, and `next_action`
  from the envelope and the preview/tokens from `data`. Confirm in the same turn when
  the resolved food, quantity, and date match the user's explicit instruction. Otherwise
  ask only for the missing detail. Report success only after an applied result.
- Logging stages foods for one local hour of the day in the same list the GoodSet app
  shows; confirm records the whole list as one entry. Pass `hour` (0-23) or `consumed_at`
  when the user says when they ate. Pass `meal_slot` when they name the meal: without a
  time, breakfast stages at 8 AM, lunch at 12 PM, snack at 3 PM, and dinner at 7 PM. With
  none of these, today's foods stage at the current hour; another day needs one. The
  summary names the hour. The preview lists every staged food. Foods the user added in
  GoodSet show `added_via` app: read them back too, and confirm only if the user agrees
  to log all of them.
- When the user adds a food before confirming, log again with the full list and the same
  time; it replaces the foods your earlier log staged for that hour. To drop one staged
  food, call `unstage` with the same time, its `line_ref`, and its `revision` as
  `expected_version`. `discard` with the same time clears that hour's list without
  recording it.
- If confirm returns `draft_changed`, nothing was recorded because the list changed in
  GoodSet: read the new list back and confirm the new token only if the user agrees.
  `draft_cleared` means the list was logged or cleared in GoodSet; read
  `nutrition_history` before logging those foods again.
- Correct/remove default to the last food in the most recently recorded entry. Use
  returned entry/item references or an item number for another target. An explicit
  request to correct or remove authorizes confirmation when the preview matches it.
- Retry the same confirmation token after an uncertain response; do not prepare another
  log as a retry. A version conflict or expired workflow requires a fresh preview.
- Use `nutrition_history` for entries and daily totals. Daily totals cover the whole
  requested range even when entries are paginated. Null totals mean missing or qualified
  data; show a known subtotal as partial. Keep estimates visible. An empty day is zero.
- For trends over weeks or months (weight trend, average calories or protein, intake
  against targets), call `nutrition_history` with `view` `trends`; add `bucket` `day`
  for daily figures. Report the returned numbers with their receipt: `holding` means no
  reading for over a week and `insufficient` too few readings for a trend. Averages count
  complete days only; say how many partial and empty days they leave out. In trends,
  a nutrient with status `empty` had nothing logged: say "not logged", not zero. Give the
  energy balance as intake beside the weight change; never turn calories into weight
  or estimate energy needs.
- Record body weight with `record_body_weight` only for an explicitly stated scale
  reading such as "I'm 81.4 kg this morning". Never record a change such as "down 2 lb"
  or an estimate. One reading per day; a new value replaces it. Omit the unit to use the
  user's preference unless they stated one. Use `remove_body_weight` to clear a day.
- Set targets with `set_targets` only when the user asks. Omit an item's amount to
  remove that target; set `inherit` to undo a change made on that date. Unmentioned
  targets stay. Never suggest or compute targets yourself.
- Show progress against a target as a plain delta without judgment: no praise, blame,
  streaks, or "on track" language. When `remaining` is null the day is partial; report
  `remaining_at_most` as "at most". Never comment on days with nothing logged.
- Save a meal with `save_meal` only when the user asks. It saves the most recent entry
  unless they name another. Log a saved meal with `log_meal`; it stages the meal's foods
  like any log, and you confirm its preview the same way. Delete with `delete_meal` only when asked.
- `nutrition_history` lists saved meals on its first page. A `ready` item logs as its
  `logs_as` preview shows. For `food_unavailable`, `portion_removed`, or `unmeasurable`,
  `problem` says why in one sentence; read it to the user as written. `log_meal` refuses
  while any item is not ready and names the meal and each blocked food. Do not log the
  other foods instead unless the user asks.
- To fix a saved meal, call `save_meal` with `meal_ref`, `expected_version`, and the full
  `items` list. Resend every unchanged food exactly as listed (`food_version_ref` and
  `quantity`). For a blocked food, use `search_foods` and send a current
  `food_version_ref` with grams or a returned `portion_ref`, or leave the food out.
- If `save_meal` with a new name returns `conflict`, a meal with that name already has
  other foods. Ask whether to replace it; to replace, call `save_meal` with the
  `meal_ref` and version named in the summary.
- Use `nutrition_history` for targets, body weight, and saved meals as well; do not ask
  the user to restate them.
- Use `nutrition_export` to export the diary and private foods. Collect pages until
  `next_cursor` is null and deduplicate profiles by `food_version_ref`.

If the tools are unavailable or nutrition permission is missing, explain that the change
was not recorded or the history could not be retrieved, and ask the user to reconnect
GoodSet with the requested nutrition scope. Never simulate a stored result.

## Spoken and dictated requests

Voice transcripts are short, unpunctuated, and sometimes misheard. Treat "Good Set",
"Good Sets", and "goodset" as GoodSet.

- Log every food from one utterance as one `nutrition_track` log with several `items`,
  not one call per food. "Two eggs, toast, and a black coffee" is one entry.
- Convert spoken numbers ("a hundred and fifty grams", "one fifty g") to digits. A count
  such as "two eggs" or "a banana" is a portion; resolve it to a returned `portion_ref`
  and never convert it to grams yourself. Mark a guessed amount `estimated` only when the
  user says it is a guess.
- When a food name looks misheard ("green yogurt" for Greek yogurt), the preview does not
  match the user's words: read the resolved food back and confirm only after they agree.
- Ask one short question at a time and offer at most three spoken choices by name, never
  as a table or numbered list of references. Do not drop the other foods from the log
  while you ask.
- Reply in one or two plain sentences that read well aloud: what was logged and any
  returned day totals the user asked about. Skip tables, bullet lists, references, and
  tokens.

Keep confirmations brief: food, quantity, and returned totals. Do not expose references
or workflow tokens in ordinary conversation. Recording food does not start a workout.
