---
name: review-activity
description: Summarize the user's retro gaming activity from Retro Game Gather (RGG) — purchases, spending, play time, clears, and collection progress over a period. Use for monthly or yearly recaps, "how much did I spend", "what did I play", trends by platform or genre, and collection goals. Japanese triggers include 振り返り, 今月, 今年, まとめて, いくら使った, 購入金額, プレイ時間, クリアした本数, 傾向, 達成率.
---

# Look back on activity

RGG computes the numbers; you write the story. Never recount totals yourself from paged lists when an analytics tool gives them.

For RGG concepts see `references/service-guide.md`; for Japanese terms see `references/glossary-ja.md`.

## Pick the source

| Question                                         | Tool                                                                                                                             |
| ------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------- |
| Purchases, spending, counts by platform or genre | getLibraryAnalytics with `sections` (`summary`, `purchase`, `platform`, `genre`, `rating`) and `buyDateFrom` / `buyDateTo`       |
| Clears, drops, statuses, play time over time     | getPlayAnalytics with `sections` (`summary`, `monthlyResults`, `status`, `playTimeTrend`, `platform`, `genre`, `completionPace`) |
| What happened in a month, day by day             | getCalendarEvents `month: "YYYY-MM"`                                                                                             |
| What the user wrote about a game                 | getPlayLogs `playId` with `fields: ["memo"]`                                                                                     |
| Collection progress (PREMIUM)                    | getCollections, then getCollectionGames `summary`                                                                                |

Request only the sections you need.

## Read the numbers correctly

- Spending from getLibraryAnalytics counts one row per game at its active copy's price. If the user has several copies of a game (PREMIUM), the app's per-copy total can be higher. Say so when reporting spending.
- Play time and clears are different measures. `monthlyResults` gives clears and drops per month; it has no minutes. Minutes played come from `playTimeTrend` (from play logs).
- `playTimeTrend` covers at most 90 days per call; `playTimeTrendGranularity: "month"` changes the grouping, not that limit. For a longer period, split it into ranges of 90 days or less that do not overlap, keep the other filters the same, and add up the minutes RGG returns. If that needs many calls, agree on the period with the user first.
- With `playTimeTrendGranularity` `week` or `month`, each point has `from` / `to` (YYYY-MM-DD, JST, inclusive): the first and last days counted in that point. Weeks are ISO weeks starting on Monday, and `period` stays `YYYY-Www`. The first and last points are cut to `playTimeTrendFrom` / `playTimeTrendTo` (a range starting on a Thursday gives a first week that starts on that Thursday), and `minutes` covers only `from`–`to`. Quote these dates instead of working them out from `period`. `day` points have no `from` / `to`, since `period` is the date.
- By default the analytics use each game's latest record. On PREMIUM, set `includeHistory: true` to include earlier cycles (for example a game cleared this year and now being replayed). If you use latest records only, say so in the answer.
- Report play time in the unit returned (minutes), converting to hours only for display.
- State the period and filters you used ("2026年1月1日〜9月30日、全プラットフォーム").
- Dates are Japan time.

## Writing the recap

- Lead with two or three facts that stand out, then the details.
- Quote game titles exactly as RGG returns them.
- Use the user's own memos for colour, and do not invent experiences they did not record.
- Keep numbers from RGG separate from your interpretation.
