---
name: log-play
description: Record what the user played in Retro Game Gather (RGG) — play sessions, starting a game, clearing it, pausing or giving up, and replays. Use when the user reports playing a retro game, finishing it, stopping, or wants to start over. Japanese triggers include 遊んだ, やった, 何時間プレイ, 始めた, クリアした, エンディング, 積んだ, 諦めた, 中断, もう一周, プレイログ, プレイ記録.
---

# Record play

In the app, a game moves through play statuses and collects play logs: プレイ予定 (PLANNED) → プレイ中 (PLAYING) → クリア済 (COMPLETED), with 一時停止 (PAUSED) and 途中断念 (DROPPED) on the side. Each session is a play log. Only games in the library can have a play record.

For RGG concepts see `references/service-guide.md`; for Japanese terms see `references/glossary-ja.md`.

## Before writing

1. Identify the game and find its current record with getPlayRecords (`title`). The record shows the status and `playId`.
2. If the game is not in the library, ask whether the user owns it. Add it (collect-games skill) only if they say yes. Some people play borrowed or downloaded versions and do not want them in their library.
3. If there is no play record yet, create one with addPlayRecord. Use `status: "PLAYING"` when they are playing now. A new PLAYING record starts today; for play that began earlier, see "Past dates" below.

## Log a session

- addPlayLog with `gameId` (or `playId`), `playTime` in minutes, and `memo`.
- Convert time exactly: 2時間半 = 150, 45分 = 45. If the user gave no duration, ask. Do not estimate.
- The memo is required and should be what the user played or felt, in their words. If they only said "played for an hour", ask one short question ("何をしましたか？") or offer a one-line memo drawn from their message for approval. Do not invent progress.
- `playDate` defaults to today in Japan time. Convert "昨日" and similar yourself.
- The log does not change the status. If the record is still PLANNED, move it to PLAYING with updatePlayRecord and mention it.

## Clear a game

The app's clear log (クリアログ) is a play log plus the status change and a rating. Through the tools it takes two steps:

1. addPlayLog with the final session's minutes and the user's impressions.
2. updatePlayRecord with `status: "COMPLETED"` and `rating` (1–5) if the user gave one. The end date defaults to today. If they cleared on another day, set `playEndDate` (see "Past dates").

Ask for a rating once if they did not give one. Leave it empty if they prefer.

## Past dates

The start date must be on or before the end date, and it is checked after each update. When the user reports play that happened before today:

- Put the day on the log (`playDate`) and, for a clear, on `playEndDate`.
- Send the start date in the same updatePlayRecord call as the status and end date (`playStartDate`, `playEndDate`, `status` together). A record created today as PLAYING starts today, so a separate end-date update for yesterday would be rejected.
- For a new game played and cleared on one past day ("昨日初めて遊んでクリアした"), create the record with addPlayRecord (default PLANNED, which has no start date), add the log, then set status, start and end dates in one updatePlayRecord call.
- If you do not know when the user started, ask. Do not change an existing start date by guesswork.
- If the log was saved but the status update failed, do not add the log again. Fix the dates and retry only the update.

## Pause, give up, start again

- Pause or stop: updatePlayRecord `status: "PAUSED"` or `"DROPPED"`. If the user's words could mean either (積んだ, 止めた), ask which.
- Replay (もう一周): addPlayRecord `replay: true`. On PREMIUM the old cycle stays in the history. On FREE and LIGHT the previous record and its logs are replaced. Tell the user that before confirming.
- Hardware: if the user names the console they played on, set `consoleId` from getConsoles (LIGHT and above).

## After writing

Confirm in one or two lines: the game, what changed, and the new total play time if returned. Do not repeat the same write because a list looks stale; the write response is the result.
