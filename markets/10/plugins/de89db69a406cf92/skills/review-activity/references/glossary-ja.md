# Japanese terms → RGG data and tools

Users talk in the app's Japanese labels or in collector slang. Map their words to the right data before choosing a tool. App labels follow the official docs glossary.

## App labels

| Japanese                                             | Meaning                                                                       | Data / tools                                                               |
| ---------------------------------------------------- | ----------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| マイライブラリ / ライブラリ                          | Owned games                                                                   | getLibrary, addToLibrary, updateLibraryEntry                               |
| ウィッシュリスト / 欲しいもの                        | Wanted games                                                                  | getWishlist, addToWishlist, updateWishlistEntry                            |
| 所有ソフト                                           | Individual copies of an owned game (PREMIUM)                                  | getPhysicalCopies, addPhysicalCopy, updatePhysicalCopy, removePhysicalCopy |
| 版 / バージョン違い / 通常版                         | Editions of a game (廉価版, 限定版, "the Best" etc.). 通常版 is the base game | editions field of game data; editionRef on physical copies                 |
| プレイ記録                                           | Play status of an owned game                                                  | getPlayRecords, addPlayRecord, updatePlayRecord                            |
| プレイログ                                           | One play session                                                              | getPlayLogs, addPlayLog                                                    |
| クリアログ                                           | Clear entry: a play log plus status COMPLETED and a rating                    | addPlayLog + updatePlayRecord                                              |
| プレイ予定 / プレイ中 / 一時停止 / クリア / 途中断念 | PLANNED / PLAYING / PAUSED / COMPLETED / DROPPED                              | status                                                                     |
| プレイをやり直す / 周回                              | Start a new cycle                                                             | addPlayRecord with replay: true                                            |
| プレイ履歴                                           | Past cycles (PREMIUM)                                                         | getGamePlayHistory                                                         |
| クリア目標日                                         | Clear target date                                                             | clearTargetDate                                                            |
| マイコレクション / コレクション                      | Collection goal (PREMIUM)                                                     | getCollections, getCollectionGames, addCollection                          |
| ゲームタグ / タグ                                    | User tag (LIGHT+)                                                             | getTags, addTag, updateTagGames                                            |
| ゲーム機                                             | Owned hardware (LIGHT+)                                                       | getConsoles, addConsole                                                    |
| メンテナンス記録                                     | Console maintenance log                                                       | getConsoleMaintenanceLogs, addConsoleMaintenanceLog                        |
| プラットフォーム / 機種                              | Platform in the database                                                      | listPlatforms                                                              |
| 発売元                                               | Publisher                                                                     | listCompanies                                                              |
| カスタムデータ / 独自ゲーム                          | User-added platform, publisher or game (PREMIUM)                              | addCustomPlatform, addCustomCompany, addCustomGame                         |
| 属性                                                 | Labels such as condition or accessories                                       | listAttributes                                                             |
| 優先度                                               | Wishlist priority 1–5                                                         | priority                                                                   |
| 購入予定日 / 購入予定金額 / 購入予定場所             | Wishlist plan                                                                 | wishDate / wishPrice / wishPlace                                           |
| 購入日 / 購入金額 / 購入場所                         | Purchase                                                                      | buyDate / buyPrice / buyPlace                                              |
| 評価                                                 | Rating 1–5                                                                    | rating                                                                     |
| 型番                                                 | Model number printed on the package or disc (e.g. SLPM-66037)                 | modelNumber                                                                |
| JAN / バーコード                                     | Barcode number                                                                | janCode                                                                    |

## Collector slang

| Japanese                        | Usual meaning                           | How to handle                                                                                 |
| ------------------------------- | --------------------------------------- | --------------------------------------------------------------------------------------------- |
| 積みゲー                        | Owned but not finished                  | Start from PLANNED (and PAUSED) play records. There is no "unplayed" flag                     |
| 箱説 / 箱説付き / 完品          | Box and manual included / complete      | Library or wishlist attributes; check listAttributes for the user's exact labels              |
| 裸 / ソフトのみ / カセットのみ  | Cartridge or disc only                  | Same as above                                                                                 |
| 買った / 手に入れた             | Bought                                  | addToLibrary (moves it from the wishlist if present)                                          |
| 遊んだ / やった                 | Played                                  | addPlayLog on the play record                                                                 |
| クリアした / エンディングを見た | Cleared                                 | Clear entry (see above)                                                                       |
| 投げた / 積んだ / 諦めた        | Stopped playing                         | DROPPED, or PAUSED if they may resume. Ask if unclear                                         |
| 2本目 / もう1本                 | Another copy of a game already owned    | Physical copies (PREMIUM). Not a second library row                                           |
| 売った / 手放した               | Sold one copy / no longer owns the game | removePhysicalCopy for one copy; removeFromLibrary only if they no longer own the game at all |

## Platform nicknames

Resolve platform names with listPlatforms (it returns abbreviations). Common ones: ファミコン / FC, ディスクシステム / FDS, スーファミ / SFC, メガドラ / MD, PCエンジン / PCE, ゲームボーイ / GB, GBA, サターン / SS, プレステ / PS, PS2, ドリキャス / DC, N64, GC, DS, 3DS, PSP, Vita.
