---
name: collect-games
description: Manage what the user wants and owns in Retro Game Gather (RGG) — the wishlist and the library. Use when the user wants a game, bought a game, asks whether they already own something, plans a shopping trip, updates purchase details, registers a list of owned games, or has more than one copy of a game. Japanese triggers include 欲しい, ウィッシュリストに追加, 買った, 手に入れた, 持ってたっけ, 買い物リスト, 中古屋に行く, 購入金額, 2本目, 手放した.
---

# Wishlist and library

The app's flow is: add wanted games to the wishlist, then move them to the library when bought. A game is in one or the other, never both.

For RGG concepts see `references/service-guide.md`; for Japanese terms see `references/glossary-ja.md`. For more than one copy of a game, read `references/physical-copies.md`.

## Add a wanted game

1. Identify the game (see the find-games skill). Make sure the platform is the one the user wants.
2. addToWishlist with only what the user said: priority, planned date, target price, store. Do not ask for optional fields the user did not mention.
3. Map words to priority only when the user states it clearly (for example 絶対欲しい → 5). Otherwise leave it unset.
4. If the game is already owned, the tool refuses. Tell the user they already have it.

## Record a purchase

1. Identify the game.
2. addToLibrary with the purchase details the user gave (date, price in yen, store, rating, memo). If the game was on the wishlist it moves automatically and keeps the wishlist's date, price, place and memo unless you pass new values. Pass the actual purchase values when the user states them.
3. Condition words (箱説付き, ソフトのみ) are attributes. Match them to the user's labels from listAttributes (type library); do not invent labels.
4. Report what was saved, including when it moved from the wishlist.

## Register many owned games

For a list, spreadsheet or long message:

1. Call getAccount and check the remaining library capacity and today's usage.
2. Identify the titles with searchGamesBatch (up to 20 rows per call).
3. Show the resolved list. Ask only about rows that are ambiguous or not found.
4. Preview with addToLibraryBatch `dryRun: true`, then save after the user agrees.

## Check before buying

- "Do I own X?": search the library (getLibrary `title`) and the wishlist. Remember that ports on other platforms are different games.
- Shopping trip: getWishlist sorted by priority, without the overdue filter, so games with no planned date are included. `wishDateOverdue` is a filter, not a sort: to show overdue games first, fetch `"overdue"` and `"not_overdue"` (which includes games with no planned date) separately and list the overdue ones first. Use `"overdue"` alone only when the user asks for overdue games. If you shorten the list, say what you left out. Include target price and store, and keep it short enough to read in a shop.

## Corrections and removal

- Purchase details: updateLibraryEntry. Omitted fields stay as they are.
- "I sold it" can mean one copy or the game. If the user has several copies, see `references/physical-copies.md`. removeFromLibrary also deletes the game's play records, play logs and copies. Say so and wait for a clear yes before confirming.
