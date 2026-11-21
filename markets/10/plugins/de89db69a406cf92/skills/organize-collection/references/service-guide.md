# Retro Game Gather — service guide

Background for all Retro Game Gather (RGG) skills. Read this when you need to explain how RGG works, which data a request refers to, or where in the app the user can do something the tools cannot.

The public documentation is the source of truth for how the service is meant to be used: https://docs.retrogather.com/ (Japanese). Link the user to the relevant page when they need app instructions.

## What RGG is

A web service (also a PWA and an Android app) for managing a retro game collection: find games, keep a wishlist, register owned games, and record play. The game database covers **games released in Japan**, over 20,000 titles, from the Famicom era through discontinued platforms such as PS3, 3DS, Wii U and PS Vita. Current-generation consoles are out of scope.

The app's basic flow is:

1. **Find (探す)** — search the database, read news, add wanted games to the wishlist.
2. **Collect (集める)** — when bought, move the game to the library; track collection goals.
3. **Play (遊ぶ)** — keep play records and play logs, then look back on them.

RGG is a data store. It identifies games, stores the user's records, and computes totals. Writing introductions, recommending games, and judging what to play are the AI's job, based on RGG data and the sources RGG links to.

## Data model

| Concept                                | What it holds                                                                                                              | Notes                                                                                                     |
| -------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| Library (マイライブラリ)               | One row per owned game: purchase date, price, place, rating, attributes, memo, reference links                             | Adding a wishlist game moves it here                                                                      |
| Physical copies (所有ソフト, PREMIUM)  | Individual copies of one library game, each with its own condition, purchase info and edition (通常版 or a バージョン違い) | One copy is active; its values are mirrored to the library row                                            |
| Wishlist (ウィッシュリスト)            | Wanted games: priority 1–5, planned date, price, place, memo                                                               | A game cannot be in the library and the wishlist at once                                                  |
| Play record (プレイ記録)               | Per owned game: status, start/end dates, total minutes, clear target date, console, rating, strategy links, memo           | Only games in the library can have one. PREMIUM keeps past cycles (replays)                               |
| Play log (プレイログ)                  | One play session: date, minutes, what was played                                                                           | The app's "clear log" (クリアログ) is a play log added together with the change to COMPLETED and a rating |
| Collection (マイコレクション, PREMIUM) | A goal: collect (LIBRARY) or clear (PLAY) a set of games chosen individually, by tag, or by platform                       | Achievement is computed by RGG                                                                            |
| Tag (ゲームタグ, LIGHT+)               | User-defined groups of games                                                                                               | Official tags exist in the app; they cannot be edited through the tools                                   |
| Console (ゲーム機, LIGHT+)             | Hardware the user owns, with maintenance logs                                                                              | Not the same as a platform (a database entry such as "Super Famicom")                                     |
| Custom data (カスタムデータ, PREMIUM)  | Platforms, publishers and games the user added because the database lacks them                                             | User entries, not RGG coverage and not ownership                                                          |
| Attributes (属性)                      | Labels such as box/manual condition, per area (library, wishlist, play)                                                    | Built-in plus user-defined; read them with listAttributes                                                 |

Play statuses and their app labels: PLANNED プレイ予定, PLAYING プレイ中, PAUSED 一時停止, COMPLETED クリア済, DROPPED 途中断念. PLANNED means "intends to play"; it does not mean "never played".

## Plans

There are three plans: FREE (通常プラン), LIGHT (ライトプラン) and PREMIUM (プレミアムプラン). Registration limits and available features differ. Call getAccount for the user's plan and limits instead of assuming numbers.

When a tool is not available on the user's plan, say what it would do and that it needs a higher plan, once, without pressing. Point to https://docs.retrogather.com/getting-started/pricing/ if they ask.

A tool can also fail because the user did not grant that permission when connecting (for example deletes, which are off by default, or custom data editing). Permissions cannot be changed in place: the user disconnects RGG and connects again, choosing the permission on RGG's consent screen. See https://docs.retrogather.com/guides/connect-ai/

## What only the app can do

Images (covers, play log screenshots), settings, news bookmarks, official tags, and bulk import other than the library are not available through the tools. When the user asks for these, explain briefly and link the matching docs page.

File export is not available through MCP. When the user wants a file, point them to the export in the app, or to `exportMyData` in the REST API with an API key: https://docs.retrogather.com/developers/rest-api/

## Docs pages

| Topic                                                          | URL                                                         |
| -------------------------------------------------------------- | ----------------------------------------------------------- |
| Searching games                                                | https://docs.retrogather.com/guides/search-games/           |
| Adding to the wishlist                                         | https://docs.retrogather.com/guides/add-to-wishlist/        |
| Adding to the library                                          | https://docs.retrogather.com/guides/add-to-library/         |
| Recording play                                                 | https://docs.retrogather.com/guides/record-play/            |
| Managing collections                                           | https://docs.retrogather.com/guides/manage-collection/      |
| Managing consoles                                              | https://docs.retrogather.com/guides/manage-console/         |
| Library (incl. physical copies)                                | https://docs.retrogather.com/features/library/              |
| Wishlist                                                       | https://docs.retrogather.com/features/wishlist/             |
| Play records                                                   | https://docs.retrogather.com/features/play/                 |
| Tags                                                           | https://docs.retrogather.com/features/tags/                 |
| Custom data                                                    | https://docs.retrogather.com/features/game-data-management/ |
| Calendar                                                       | https://docs.retrogather.com/features/calendar/             |
| Plans                                                          | https://docs.retrogather.com/getting-started/pricing/       |
| FAQ                                                            | https://docs.retrogather.com/faq/                           |
| Connecting AI tools (permissions, disconnecting)               | https://docs.retrogather.com/guides/connect-ai/             |
| What to ask AI tools                                           | https://docs.retrogather.com/guides/ai-examples/            |
| MCP / API settings (API keys, today's usage, plan differences) | https://docs.retrogather.com/features/mcp-api/              |
