# Start here

Think of a Codex chat as a notebook with limited room. Token Weather shows a
rough weather report for that room.

- **Clear or Fair:** There appears to be plenty of room.
- **Cloudy or Showers:** The chat is getting fuller. Save important notes if
  you plan to keep working for a while.
- **Storm:** The chat is near the reference limit. Ask Codex to save a
  checkpoint before a long task.
- **Clearing:** Codex reported that it shortened the chat history.
- **Unknown:** There is not enough reliable information yet. Try again after
  a new reply.

The large number is an estimate of chat space used. The line on the chart shows
how that estimate changed. The five turn outlook is a guess based on recent
turns. A long tool result can make the chat grow faster than the guess.

The model is the type of assistant used for the chat. The thinking setting
shows how much thinking was requested. The output tokens per second number
counts small pieces of text from the current turn and divides them by the time
since the turn began. It includes waits for tools, so it is not a speed test.

The account usage section is separate from chat space. It shows a recent
account snapshot only when Codex provides one. It does not show a price.

Token Weather reads the current chat's local record and keeps only small
number summaries for its history. The weather reader does not send the chat
record to an RSI AI server. The page opens on your own computer. If Codex
cannot verify which chat or format it is reading, it leaves the number unknown.

## What to ask Codex

- "Show the weather for this chat."
- "Open my Token Weather page."
- "Save a checkpoint for this work."

The public plugin needs local Codex access for weather readings. This Skills-only edition provides local weather and replay when asked, with
no hooks; numeric MCP planning is a separate connected workflow. Checkpoints support manual handover; new chats stay manual.

For recorded events, ask "Replay this local usage recording". See
[local replay](../skills/token-weather/references/REPLAY.md) for format limits.

One-off weather reads save no history and read no config by default. Saved
history and the persistent page are requested choices; they use separate
Skills-edition storage. Checkpoints may contain private task notes and retain
earlier versions. See [local data and privacy](PRIVACY.md) for exact access,
retention and removal. Evidence files are not read without --verify-evidence.
