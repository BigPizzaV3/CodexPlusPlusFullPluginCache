---
name: clash-royale-progression
description: Use RoyaleTools to calculate Clash Royale collection or selected-card upgrade gaps, Evolution and Hero progress, King Tower and Star Level plans, and help with browser-local saved decks or resource balances.
---

# Progression and saved decks

Read [the website contract](../royaletools-navigator/references/website.md).

For an upgrade calculation, request the public Player Tag if missing and open `/progression?tag={tag}`. The entry redirects to `/player/{tag}/progression`. Use the visible Overview, Cards, Evolutions & Heroes, King Tower, or Star Levels view that matches the goal.

For a specific deck or card plan, import the supplied Clash Royale/RoyaleTools deck link or use the visible card picker. Verified prefill accepts `cards`, `deck`, and `view` (`overview`, `cards`, `forms`, `king-tower`, `star-levels`). URL-encode a supplied deck URL. Verify the resulting selected cards and active view before reading costs.

Use the actual displayed resource requirements. Explain permanent owned levels separately from temporary seasonal battle levels when the page distinguishes them. Do not infer partial Evolution Shard ownership or hidden Hero currency from public data.

## Collection Level rewards

For questions about Collection Level milestone rewards, open `/collection-level-rewards` to list every reward from Level 20 to 2,500, or `/collection-level-rewards?tag={tag}` to show which milestones the player's level has reached and the next reward. Reached only means the level is at or above a milestone; the page cannot tell whether a reward was collected in game.

## Entered resources

Gold, Gems, Wild Cards, Wild Shards, Hero Coins, and banked per-card Evolution Shards are optional player-entered values saved in that browser for the selected tag. Request only balances that the affordability question needs. Enter them through the UI only when the user asks you to use/save those values. Verify the correct tag and the `Your resources` setting.

Blank means unknown. Turning `Your resources` off keeps saved balances but excludes them from calculations. Card-level `Can upgrade to` treats one card at a time, does not unlock unowned cards, and does not check Gold; do not present it as a whole-plan affordability guarantee. Explain the page's distinction between required work and affordability.

## Saved decks and tags

Open `/saved-decks` only in an available browser that can access the user's saved collection. A fresh/cloud browser cannot automatically read decks saved in their Chrome. If it is empty, explain that browser scope rather than claiming the user has no saved decks. Request a deck link or provide a handoff to their browser when needed.

Saved decks can sit in folders and be searched by deck name, card name or card nickname. `Your saved sets` holds War and Crown Series deck sets saved from those builders. Folders, Select and Add decks only organize what is already saved in that browser.

Use Save, Share, move, or remove controls only for the deck/tag action the user requested. Saved Tags and saved decks are separate. Do not clear existing resources, decks, or preferences as a setup step.

Return the selected plan, required resources, which balances were known, and the tool link. Never promise an upgrade purchase or an in-game action.
