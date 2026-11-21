---
name: get-started
description: Grind settings for the user's own coffee grinder, and help choosing one to buy. Use when someone asks what grind to use on their grinder, needs a recipe's grind setting translated to the grinder they own, or is deciding which grinder to get.
---

# BrewMark grind settings

BrewMark covers 200+ home coffee grinders. It can do four things:

- **Translate a setting between grinders.** A recipe says "18 clicks on a Comandante" and the user owns a Baratza Encore: call `convert_grind_setting`.
- **Give the settings for one grinder.** The user wants to know what to use for espresso, pour over, French press and so on: call `get_grinder_chart`. If they named a brew method, pass it as `method` so the card leads with it and its starting recipe.
- **Say what to try next after tasting.** The user brewed at a setting and it tasted sour or bitter: call `dial_in` with the grinder, the setting, the result and the brew method if they said it. If they say it now tastes good, call it again with result `good`.
- **Help choose a grinder.** The user is deciding what to buy: call `find_grinder` with the brew methods, budget, hand or electric, and must-haves they mentioned. Leave out anything they didn't say. BrewMark doesn't sell grinders; each pick links to its buying guide on brewmark.io. Don't use it to place an order.

Users name grinders however they like. Pass the name as they said it. If the tool reports more than one match (for example "Comandante" covers the MK3 and MK4), ask the user which one they have. Don't guess.

Every number is a starting point. Burr wear, bean density and roast change the right setting, so say that once and suggest adjusting by taste: finer if sour or fast, coarser if bitter or slow.

Answers show as a card with the numbers drawn on the grinder's dial. Don't repeat every number from the card; give the advice around it. The card has "Too sour" and "Too bitter" buttons; if the user taps one, its new suggestion reaches you as context, so follow it.
