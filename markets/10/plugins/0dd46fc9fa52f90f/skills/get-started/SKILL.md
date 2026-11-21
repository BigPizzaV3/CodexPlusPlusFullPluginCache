---
name: get-started
description: Use this when the user pastes a Magic: The Gathering decklist or card list and asks "price check: Sol Ring, Rhystic Study, …", "what's the cheapest printing of Cyclonic Rift", "is Mana Crypt banned", "is this deck legal in Commander and what bracket is it", "how many game changers", or wants "budget swaps under $3". The tools return per-card prices from today's Scryfall data with the cheapest printing and set, the deck total, current legality and bans, Game Changers with the implied Commander Bracket, and budget replacements in the deck's colors. Do not use for other card games, sealed product, buying cards, or general deck-building advice with no cards to check.
---

1. When the user pastes a decklist, pass it to the tool exactly as pasted (all lines, headings and set codes). Do not retype, shorten or "fix" card names first: the tool reports misspelled and invented names itself.
2. Price check of a card list or deck, cheapest printing of a card, "is X banned", legality in a format, Game Changers / Commander Bracket, curve, colors or "is this a real deck?" → `check_decklist` (a list of one or a few card names is fine, one per line). Cheaper version, "every card under $X", "deck under $Y" or "replace the expensive cards" → `find_budget_swaps`.
3. Pass the format if the user names one (Commander, Standard, Modern …). If the list has no Commander heading but the user names the commander, pass it in `commanders`. Use `currency: "eur"` for users in Europe and `"tix"` for MTGO.
4. For budget swaps, ask which cards are the core of the deck if the user has not said, and pass them as `keep`. If only a deck total is given, set `maxCardPrice` to about 2–5% of it and pass `targetTotal`.
5. Report the problems first (not real cards, banned, wrong card count, color identity), then the total and the most expensive cards. Prices are Scryfall's daily estimates at the cheapest printing; say so and do not present them as store prices.
6. Whenever you build or edit a decklist yourself, run `check_decklist` on it before presenting it, and fix every error it reports.
7. Out of scope: other card games, sealed product, buying or selling cards, and grading. Say so instead of guessing.
