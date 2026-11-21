---
name: clash-royale-decks
description: Use RoyaleTools to find observed Clash Royale decks fitting a player's collection or chosen cards, compare changes to an eight-card deck, and build non-overlapping Clan Wars decks or Crown Series Duel Decks. Activates for deck-selection or deck-improvement requests even without a RoyaleTools mention.
---

# Find and improve decks

Read [the website contract](../royaletools-navigator/references/website.md). Work through the public pages and controls, not direct data endpoints.

## Select the tool

| Goal | Page | Required context |
| --- | --- | --- |
| Best practical decks for owned cards | `/top-decks?tag={tag}` | Public Player Tag; desired mode if relevant |
| Decks containing a card or several cards | `/deck-finder` | One to eight selected cards; Player Tag optional |
| Improve an existing deck with limited swaps | `/deck-improver` | Eight distinct cards or a valid deck link; locks and tag optional |
| Four Clan Wars decks without repeated cards | `/war-decks?tag={tag}` | Public Player Tag |
| Crown Series Duel Deck: three or four decks without repeated cards, under a league's level cap | `/crown-series-decks?tag={tag}` | Public Player Tag; league if known |
| General current deck trends | `/meta-decks` | No Player Tag required |

If the user asks for the best deck for XYZ, interpret XYZ as their stated goal, card, or constraint. Do not claim collection fit without a tag. A card preference alone is enough to start Deck Finder; ask for a tag only when owned cards or upgrade costs matter. Ask which missing card or ambiguous form they mean when it changes the search.

## Use the pages

- **Top Deck Finder:** open the tag-prefilled entry. It redirects to `/player/{tag}/top-decks`. Read the actual shortlist and visible collection/readiness details. Read the offered game modes and use the requested supported mode. A suggested deck shows an Evolution or Hero only where the player has unlocked it; read the page's line naming any locked form. Pressing a card of a suggested deck offers the player's own cards to change it; do that only when the user asks for a change.
- **Deck Finder by Cards:** choose cards with the visible picker and `Search by card name`. One to seven cards require every selection in a complete deck; eight cards check an exact unordered set. Choose the observation period and optional tag. Use the page's Without choice for up to eight cards no result may use. Use up to two Evolutions, two Heroes, and three special cards in total, as allowed by the UI. Wait for matching observed decks, an empty state, or an error.
- **Deck Improver:** use `Paste deck link` or select exactly eight distinct cards. Apply requested locks and verify that they appear in the selected deck. Select optional tag, offered mode, and recent observation period, then run the visible analysis action. Distinguish the exact match from alternatives and report actual changed cards or forms.
- **War Deck Builder:** read the returned complete decks and no-repeat result. Four decks require at least 32 owned cards; explain any shortfall shown by the page. This tool uses real card levels and Ranked observations, not a promise that every deck was observed in War. When the user asks for a change, press a card to change it, or use `Swap deck` or `Change all decks`, then read the set again: a change can rebuild the other decks so no card repeats.
- **Crown Series Deck Builder:** open the tag-prefilled entry. It redirects to `/player/{tag}/crown-series-decks`. A Duel Deck is three or four decks that share no card, with the player's levels counted up to the league's cap (Level 11 in Leagues 1 and 2, up to 16 in Leagues 9 to 13). Read which league the page opened on and choose the user's league and 3 or 4 decks with the visible controls; do not guess a league. Card changes, `Swap deck` and `Change all decks` work as in the War Deck Builder. `Save set` keeps the set in that browser's Saved Decks; use it only when asked.

Use query prefill only for values already known. Deck Finder accepts `cards`, `evos`, `heroes`, `without`, `time` (`today`, `week`, `month`), `tag`, and the current `mode` key. Deck Improver shared links use `cards`, `evos`, `heroes`, `locks`, `period`, `tag`, and `mode`; prefer the site's own share URL after selection. A prefilled link still needs its result verified in the browser.

## Report

For a simple deck request, give the deck name, all eight cards with active forms, the Tower Troop when shown, and a source link. Keep the answer concise and omit routine commentary about observation snapshots, delayed refreshes, or missing win-rate data.

For collection-specific requests or comparisons, explain the relevant ranking, ownership, or upgrade gap. Include the source period or a limitation only when it changes the requested conclusion, such as a question about the current meta or win rate. Check freshness internally and avoid presenting older evidence as a verified current best deck. Observed usage is not a win rate, matchup advantage, or guarantee of wins.

Link to the completed search and use the site's deck share link when available. Copy, Save, Screenshot, or opening a game import link should match the user's requested action; do not save every suggested deck automatically.
