---
name: reddit-story
description: Make a Reddit story video with Crealix, a post read aloud over gameplay with the Reddit card and captions. Use when the user asks for a Reddit story, an AITA, TIFU, confession, revenge or relationship-drama story, or a storytime video over Minecraft or other gameplay.
---

# Reddit story

A narrator reads a Reddit-style post over gameplay: the post card opens the
video with its title, then the story plays with captions. The story is the
whole video, so the writing matters most.

Reddit stories are for paid plans. If Crealix answers that the plan doesn't
include them, say so plainly and offer a format that can tell the same story,
such as a faceless video or a text-message story. Never suggest upgrading.

## 1. Read the guide

Call `get_creation_guide('reddit_story', durationSec, language)`: the characters of
body for this length, the options, the cast (voices, captions, music, gameplay)
and what the user saved for their Reddit card in their brand.

## 2. Write the post (hybrid)

Send the post title as `title` and the body as `script`.

- The title is the hook and is read first: a question or a shocking statement
  that makes the viewer need the ending ("AITA for skipping my sister's wedding
  after she read my diary in her speech?").
- The body is first person and conversational, like a real post: short
  paragraphs, specific details (ages, places, what was said), no clichés.
- Open inside the conflict, not with background. Raise the stakes every few
  lines and keep the key reveal for late.
- End with a twist, an "UPDATE:" or a question to the reader that invites
  comments.
- Plain text: no markdown, hashtags or emojis. Stay within the guide's
  character budget.
- Invent the people. Don't retell a real person's private story without saying
  it is fiction.

Use crealix mode when the user wants Crealix to write it from an idea.

## 3. Cast it

Choose what suits this story, from the cast and the guide's options:
- A narrator voice that sounds like the person who wrote the post.
- `options.gameplayId`: the background clip that fits the story's energy and
  audience (`browse_catalog('gameplay')` to search).
- The card: `options.subreddit` and `options.displayName` (default: their brand),
  `options.theme`, and `options.cardMode` (the card only at the start, or all
  along).
- Captions and music from the cast; `options.narrationVolume` and
  `backgroundVolume` for the mix. `cover` for the thumbnail.

## 4. Propose, create, finish

`check_plan` until it is valid and fits the length, then one `validate_plan` with
two or three lines of why. On a yes in the chat, `create_video` with the
`proposalId`. Follow it with `get_status`; the card plays the draft.

Changes afterwards go through `edit_video` (the post, card, voice, captions,
gameplay, music). Changed words or voice leave the recording behind: say what
re-recording costs, then `rerecord_narration`. Render only when they ask.
