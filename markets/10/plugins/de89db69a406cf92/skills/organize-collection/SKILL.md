---
name: organize-collection
description: Organize a Retro Game Gather (RGG) collection with tags, collection goals, owned consoles and maintenance logs, and custom entries for games the database lacks. Use when the user wants to group games, set a goal such as completing a series or a platform, register their hardware or its repairs, or add a game or platform RGG does not cover. Japanese triggers include タグ付け, 分類, コンプリート, シリーズを集める, コレクション, 達成率, ゲーム機を登録, 本体, メンテナンス, 修理, 電池交換, 登録されていないゲーム, 同人, 海外版.
---

# Organize the collection

These features depend on the plan: tags and consoles need LIGHT or above; collections and custom data need PREMIUM. If a tool is missing, tell the user once which plan it needs and continue with what is available.

For RGG concepts see `references/service-guide.md`; for Japanese terms see `references/glossary-ja.md`.

## Tags

- Create with addTag. A name is enough; the server picks an unused colour. Do not ask the user to choose a colour.
- Add or remove games with updateTagGames `mode: "add"` or `"remove"`. Use `"replace"` only when the user wants the whole set redefined; it needs the tag's current revision.
- Tags hold the user's own groups. Official tags are managed in the app.

## Collection goals (マイコレクション)

Help the user turn a goal into a collection:

1. **Purpose**: collect the games (`purposeType: "LIBRARY"`) or clear them (`"PLAY"`).
2. **Scope**: listed games (`INDIVIDUAL`), everything in a tag (`TAG`), or a whole platform (`PLATFORM`). A series usually fits a tag or a list; "every Virtual Boy game" fits a platform.
3. Confirm the name and scope, then addCollection.
4. Progress: getCollectionGames. `summary` has the totals; `achieved: false` lists what is not achieved yet.
5. "Not achieved" is not the same as "not owned". Check each game's library status before suggesting anything:
   - Not in the library (usually a LIBRARY goal): offer to add it to the wishlist (collect-games skill), a few at a time and only with the user's OK.
   - Owned but not cleared (a PLAY goal): suggest adding it to the planned list or starting it (log-play and plan-next-game skills). Never send owned games to the wishlist; the tool refuses them anyway.
   - Owned but not meeting the collection's required attributes: explain the condition. Do not change attributes just to make the goal count as achieved.

## Consoles and maintenance

- A console is the user's hardware (e.g. "初代スーファミ 1号機"), not a database platform. addConsole with a name the user will recognize; link platforms it plays with `platformPriorities`.
- Repairs and upkeep: addConsoleMaintenanceLog. Past work uses `status: "DONE"` and `completedDate`; planned work uses `"SCHEDULED"` and `scheduledDate`.
- Removing a console also removes its maintenance logs.

## Games RGG does not cover (custom data)

1. Search first: searchGames by title, then by hiragana reading or abbreviation. Only continue if it is really missing.
2. Explain that custom entries are the user's own data, not part of RGG's database.
3. Resolve the platform and publisher: public ones via listPlatforms / listCompanies, or create custom ones first (addCustomPlatform / addCustomCompany).
4. addCustomGame needs the publisher, main genre and release date as well as the title and platform. These do not need to be exact: users often want to register a game from just its title and platform, and every value can be corrected later with updateCustomGame. Also add the hiragana reading (`titleKana`) so the game can be found by the hiragana search in step 1. Genre accepts main genres only.
5. If you filled in values the user did not give, tell them which ones.
6. A custom game is not owned automatically. Offer to add it to the library or wishlist.

App reference: https://docs.retrogather.com/guides/manage-collection/ , https://docs.retrogather.com/guides/manage-console/ , https://docs.retrogather.com/features/game-data-management/
