---
name: clash-royale-learn-and-practice
description: Find and explain RoyaleTools Clash Royale guides, look up or compare card stats, recommend suitable card minigames or gameplay drills, and answer questions about the site's methodology, privacy, support, or use. Use for learning and practice rather than live deck ranking.
---

# Learn and practice

Read [the website contract](../royaletools-navigator/references/website.md).

## Guides

Browse `/blog` using the topic directory and numbered pages to find a published article matching the question. Read that article before summarizing it and link to `/blog/{publishedSlug}`. Do not invent titles or use draft guides as published advice. If no relevant guide exists, explain what a nearby tool can answer and keep your own coaching separate from the site's article.

## Card stats

Each card has a page at `/cards/{card-name}`, such as `/cards/hog-rider`, listed on `/cards`. A card's Evolution and Hero are sections of the same page. Stats are the in-game card screen's values at Tournament Standard level 11, plus hidden values the game leaves out; no other levels are listed, and a missing stat is unknown, not zero. To put 2 to 4 cards side by side, use `/cards/compare?cards={card},{card}` with page names (add `-evolution` or `-hero` for those forms). The crown on a row marks that row's best value only: a stat comparison is not a matchup result or a recommendation. Usage on a card page comes from the weekly observed Top 200 Ranked sample and is not a win rate.

## Practice

Use the [site catalog](../royaletools-navigator/references/site-catalog.json), `/minigames`, and `/puzzles` to match the user's skill goal to an activity.

- Elixir calculation/counting: Elixir Math, Elixir Rush, or Elixir Counting.
- Tracking an opponent's cycle: Cycle Tracker at `/puzzles/cycle-tracking`.
- Reaction practice: Log Reaction.
- Reading a push: Mystery Push at `/puzzles/mystery-push`, naming a hidden card from the tower damage it deals.
- Recognizing cards: the visual, clue, name, or comparison minigames, or Sound Bite, which plays a card's sound.
- Just for fun with a microphone: Sound Mimic, where the player copies a voice line or emote. Only the user can play it; never ask for or use microphone access on their behalf.
- Remembering decks or cards: Deck Recall or Flash Memory.
- Card stats and spell interactions: Stat Showdown, or the Spell Check puzzle at `/puzzles/spell-check`.

Read the activity's visible instructions and describe what the user should practice. Open the exact activity for the user to play. Do not automate a timed round, consume limited attempts without the user's intent, or register/submit an AI-generated score as their achievement. Personal bests and saved attempts can be local to this browser. Games leaderboard registration is a separate flow from public player lookup.

## Help and policies

Use `/faq` for usage/support, `/ai-plugins` for installing this plugin in ChatGPT or Claude, `/methodology` for sourcing and calculation scope, `/about` and `/about/dcmat` for the service and maker, and `/privacy`, `/cookies`, or `/terms` for their respective policies. Read the current relevant page rather than answering policy questions from a cached assumption. The support address is `contact@rekonmedia.com`; do not use it as a developer identity or send a message unless asked.

For a question about the public developer interface, `/docs/api` is a readable documentation page. Reading it does not authorize direct endpoint calls through this plugin; preserve the website-only workflow contract.

For external community recommendations, follow the current website's visible link only when it is relevant to the user's request. Do not collect or reproduce RoyaleAPI content through this plugin without documented permission covering the material and use.

Return the answer or a short practice routine with the relevant article/tool link. Do not claim the plugin can perform in-game battles or improve a player's account automatically.
