---
name: plan-next-game
description: Help the user choose what to play next from their Retro Game Gather (RGG) backlog. Use when the user asks what to play, wants to clear their backlog, has limited time tonight, or asks about games they planned to finish. Japanese triggers include 積みゲー, 次に何を遊ぶ, 何やろう, 今夜遊べる, 崩す, プレイ予定, クリア目標.
---

# Choose the next game

RGG stores the backlog; you make the suggestion. Base it on the user's data and say what it is based on.

For RGG concepts see `references/service-guide.md`; for Japanese terms see `references/glossary-ja.md`.

## Where the backlog is

1. **Planned games first.** getPlayRecords `statuses: ["PLANNED"]`. Users add games they intend to play here; it is the app's backlog.
2. **Paused games** (`"PAUSED"`) are candidates for "something to resume".
3. **Overdue goals.** `clearTargetOverdue: "overdue"` finds unfinished games past their clear target date.
4. **The wider library** only when the above is empty or the user asks. First ask for a condition (platform, genre, era), then getLibrary with that filter and `fields` including `latestPlay`. Do not page through the whole library as a first step.

## Reading the data correctly

- PLANNED means "intends to play", not "never played". Check `hasHistory` and start dates.
- A library game without a play record is "not recorded", not proof it was never played.
- Present results as candidates from the user's records (登録情報上の候補).
- If fewer candidates match than the user asked for, show the ones that match. Do not add games they do not own.

## Making the suggestion

- Ask one question if it helps: time available, mood, platform at hand.
- Game length and style: use what you know or read from the game's `externalLinks` (see the find-games skill). Say when it is your estimate.
- Keep the list short (three to five) with one line of reasoning each.

## Next steps to offer

- Start the chosen game, depending on its latest record (see the log-play skill):
  - PLANNED or PAUSED: updatePlayRecord to PLAYING.
  - No play record: addPlayRecord with `status: "PLAYING"`.
  - COMPLETED, or DROPPED and the user wants to start over: this is a replay. Use addPlayRecord with `replay: true`, never updatePlayRecord — changing a finished record to PLAYING erases its end date and rating. On FREE and LIGHT a replay replaces the previous record and its logs; say so first.
  - DROPPED and it is unclear whether the user wants to continue or start over: ask.
- Set a goal: updatePlayRecord `clearTargetDate`.
- Add a wanted game to the planned list: addPlayRecord (status defaults to PLANNED) for games already in the library.
