---
name: find-games
description: Identify Japanese retro games in Retro Game Gather (RGG) and introduce them with cited sources. Use when the user asks what a game is, wants a game looked up by title, nickname, JAN barcode or model number, asks which platforms a game came out on, or wants games found by platform, genre or release period. Japanese triggers include ゲームを調べて, どんなゲーム, 紹介して, 探して, 型番, バーコード, 何機種で出た, ファミコンのRPG.
---

# Find and introduce games

RGG's value here is exact identification of games released in Japan, plus curated links to sources about each game. RGG does not store introductions or reviews. You write those from the sources you actually read.

For RGG concepts see `references/service-guide.md`; for Japanese terms see `references/glossary-ja.md`.

## Identify the game

1. Pick the identifier the user gave: title or nickname → `query`; barcode number → `janCode`; package or disc code → `modelNumber`.
2. If the user named a platform ("SFC版", "PS版"), resolve it with listPlatforms and set `platformIds`.
3. Read the candidates. Numbered sequels, ports, remakes and compilations often match together. Choose from title, platform and release date. Ask only when the choice changes the answer, and ask with the short list, not an open question.
4. A match on `alias` is a reading or nickname, not the official title. Say which game you took it to be.
5. A match with `edition: true` came from a バージョン違い (e.g. a budget re-release). The result is the parent game. RGG does not know which edition the user owns unless they record it as a physical copy (PREMIUM).
6. If nothing matches, retry with a short hiragana reading or a common abbreviation before saying the game is not covered. Coverage is Japan-released retro games only; do not invent titles or data.

Always quote official titles exactly as RGG returns them.

## Introduce a game

1. Get `externalLinks` (included in getGameDetail by default).
2. Choose sources for the question: fan wikis for story, systems and trivia; Wikipedia for an overview; the Media Arts Database (メディア芸術データベース) and Game Preservation Society (ゲーム保存協会) for bibliographic facts; IGDB for international information; PULSE (a Japanese game-tracking service) for how players rate the game.
3. Open the URLs with your browsing tool and read the section for the right platform version. Use URLs as returned; never build them from the title.
4. Write the introduction from what you read and cite the pages. Keep RGG's registered facts (release date, publisher, platform, model number, price) separate from what the sources say.
5. Avoid ending spoilers unless the user asks.
6. If you cannot open a source, say so. Do not present unread content as sourced.

## Explore by conditions

- "RPGs on the Famicom", "games released in 1994": browseGames with `platformIds`, `genreId` (from listGenres), and release dates. This needs PREMIUM.
- Without PREMIUM, searchGames still needs a title or identifier. Suggest narrowing by a series name, or point to platform and genre browsing in the app: https://docs.retrogather.com/guides/search-games/
- For genres such as "action RPG", pass the single genreId from listGenres. Do not combine a main and a sub genre yourself.

## Next steps to offer

After identifying a game, offer the natural next action once: add it to the wishlist, or to the library if they own it (see the collect-games skill). Do not add anything without the user asking.
