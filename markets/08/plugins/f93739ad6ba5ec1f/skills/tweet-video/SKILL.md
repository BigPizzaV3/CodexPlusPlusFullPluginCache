---
name: tweet-video
description: Make a tweet video with Crealix, an X (Twitter) thread shown as cards, the main tweet and each reply read in its own voice, over gameplay. Use when the user asks for a tweet video, a viral thread, a hot take with replies, or an X post turned into a video.
---

# Tweet video

The main tweet appears as an X card and is read aloud, then the replies come in
one by one, each with its own voice, over gameplay. The thread is the video:
a strong post and replies that argue, joke or add the twist.

## 1. Read the guide

Call `get_creation_guide('tweets', durationSec, language)`: the characters for
this length, the most tweets a thread holds, the options, the cast (voices,
captions, music, gameplay) and the X profile saved in the user's brand.

## 2. Write the thread (hybrid)

Send it as `script`, blocks separated by a blank line:
- The first block is the main tweet, posted by the account in `options.account`
  (default: the user's brand).
- Every reply starts with its author: `Jane Doe @jane: reply` or `@jane: reply`.

What makes it work:
- The main tweet is a hook on its own: a hot take, a confession, a relatable
  disaster.
- Replies escalate: agree, argue, one-up, and one of them flips it. Keep each
  short, like a real reply.
- End on the funniest or most surprising reply.
- Invent the people and their handles. Never make a real person or brand
  appear to post something they didn't.

Use crealix mode when the user wants Crealix to write it.

## 3. Cast it

Choose what suits this thread, from the cast and the guide's options:
- `options.voices`: a voice for each person, by @handle or name, that fits how
  they write. Anyone not listed reads with the main voice.
- `options.account`: who posts the main tweet, when it shouldn't be the brand.
- `options.displayMode` (the whole thread or one tweet at a time), `options.theme`
  and `options.cardOpacity`.
- `options.gameplayId`, captions and music from the cast, the mix and `cover`.

## 4. Propose, create, finish

`check_plan` until it is valid and fits the length, then one `validate_plan` (the
card shows each person with their voice) with two or three lines of why. On a
yes in the chat, `create_video` with the `proposalId`. Follow it with `get_status`.

Changes afterwards go through `edit_video` (edit, add or remove tweets, each
person's voice, the theme, gameplay and music): tweet ids are in `get_project`'s
content. Changed words or voices need `rerecord_narration`, which re-records only
those tweets. Say the cost first. Render only when they ask.
