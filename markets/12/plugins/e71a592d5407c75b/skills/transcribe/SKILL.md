---
name: transcribe
description: Turn a public video or audio link into timestamped text, then summarize, subtitle or export it with the JustTranscribe tools.
---

Use the JustTranscribe tools when the user shares a link to a public video or audio
recording (YouTube, TikTok, Instagram, Facebook, Pinterest, Google Drive) and wants
its words: a transcript, a summary, quotes, key moments, subtitles or a translation
of what was said.

Do not use them for web pages or articles (the user wants a page summary, not a
transcription), for writing a script from scratch, or for translating text the user
typed. Private videos, live streams and links that need a login cannot be fetched;
say so and suggest uploading the file at justtranscribe.ai instead.

How to work:
1. Call `transcribe_url` with the link. It waits up to about a minute and returns
   the transcript when the recording is short. If it answers "processing", call
   `get_transcript` with the returned id right away and keep calling until the
   status is "complete"; never tell the user to wait and come back.
2. Read the text with `get_transcript` (ask for `segments` only when timestamps
   matter). Summaries, bullet points, quotes and translations are yours to write
   from that text.
3. For subtitles or a file, call `export_transcript` with `srt`, `vtt`, `txt`,
   `md` or `csv`.
4. `list_transcripts` shows the account's recent transcripts; `delete_transcript`
   removes one when the user asks.

Limits to mention when relevant: one link at a time per account, recordings up to
150 minutes, a handful of new transcripts per hour. The user's
full library, uploads of their own recordings and Word export live at
https://justtranscribe.ai.
