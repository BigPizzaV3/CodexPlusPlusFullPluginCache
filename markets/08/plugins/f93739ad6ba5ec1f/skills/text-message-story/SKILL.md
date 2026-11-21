---
name: text-message-story
description: Make a text-message story video with Crealix, a chat that unfolds bubble by bubble (iMessage, WhatsApp, Instagram or X DMs), each person with their own voice, over gameplay. Use when the user asks for a fake text conversation, a chat story, or texts between a couple, exes, parents or friends.
---

# Text-message story

A phone screen shows a conversation, bubble by bubble, each message read in its
sender's voice, over gameplay. The chat is the story: you write it as a plain
transcript, Crealix turns it into bubbles, casts the voices and adds the
delivery and sound effects.

## 1. Read the guide

Call `get_creation_guide('text_messages', durationSec, language)`: the characters
of messages for this length, the chat apps and themes, the cast (voices,
captions, music, gameplay) and the people saved in the user's brand.

## 2. Write the chat (hybrid)

Send the transcript as `script`, one message per line: `NAME: message`.

- Two to six people. The phone's owner is the one with the most messages.
- Write the way people text: short, lowercase, fast replies, the odd typo or
  "…". Several short messages beat one long one.
- The first message is the hook: something that makes the viewer need the
  next bubble ("who ate the cake i made for grandma").
- Build tension through the replies and land a twist or reveal in the last
  messages.
- A line on its own like `3 HOURS LATER` becomes a time skip. Use it to jump
  to the payoff.
- Stay within the guide's character budget.

Use crealix mode when the user wants Crealix to write it from an idea.

## 3. Cast it

Choose what suits this conversation, from the cast and the guide's options:
- `options.voices`: a voice for each person, by name, that fits who they are
  (age, gender, personality). Anyone not listed reads with the main voice.
- `options.skin`: the chat app, and `options.theme` (light or dark).
- `options.gameplayId`: the background that fits the story's energy.
- Captions and music from the cast, the mix (`narrationVolume`,
  `backgroundVolume`), and `cover` for the thumbnail.

## 4. Propose, create, finish

`check_plan` until it is valid and fits the length, then one `validate_plan`: the
card shows each person with their voice. Recommend it in two or three lines.
On a yes in the chat, `create_video` with the `proposalId`. Follow it with
`get_status`.

Changes afterwards go through `edit_video` (messages, people, voices, app,
gameplay, music): the ids are in `get_project`'s content. Changed messages or
voices need `rerecord_narration`, which re-records only those turns. Say the
cost first. Render only when they ask.
