---
name: split-screen
description: Make a split-screen video with Crealix, two clips stacked or side by side, such as the user's own clip over gameplay, with optional narration and captions. Use when the user wants a split screen, their clip or podcast over Minecraft or satisfying footage, or gameplay under a video they have.
---

# Split screen

Two clips play at once, stacked or side by side: usually the user's clip on
one half and gameplay on the other, which keeps viewers watching. Narration
with captions is optional. Without it, the video lasts as long as the longer
clip and costs nothing to make.

## 1. Get the clips

Each half is either a file in Crealix storage (`url`) or a gameplay clip
(`gameplayId` from `browse_catalog('gameplay')`).

The user's own clip must be in Crealix first:
- attached to the chat: `import_media_from_url` with `file`;
- a public link to the file: `import_media_from_url` with `url`;
- on their device: `upload_media` shows a card to pick it. Its Crealix URL comes
  back in their next message.

Don't ask for a public link when they can attach or upload the file.

## 2. Read the guide

Call `get_creation_guide('split', durationSec, language)`: the narration budget,
the options and the cast (voices, captions, music, gameplay).

## 3. Decide the narration

- Their clip already talks (a podcast, a vlog, a reaction): usually no
  narration. Leave `script` out and keep its sound on.
- A voice-over tells the story: write it yourself (hybrid) within the budget,
  spoken and conversational, with a hook first. Crealix voices and captions it.
- Crealix writes it from an idea (crealix mode) only when the user asks.

## 4. Set it up

- `options.first` (top or left) and `options.second` (bottom or right). Put the
  clip the viewer should follow on top. Mute the gameplay (`muted: true`) or
  keep it low (`volume`).
- `options.splitDirection` and `options.splitRatio` when one half should be
  bigger.
- With narration: a voice from the cast that suits it, captions and
  `options.captionPosition` where they don't cover a face, and music if it
  helps. `cover` for the thumbnail.

## 5. Propose, create, finish

`check_plan` until it is valid, one `validate_plan` with two or three lines of why,
then `create_video` with the `proposalId` on a yes in the chat. Follow it with
`get_status`.

Changes afterwards go through `edit_video` (the narration, either clip, the
split, captions, music). A changed narration or voice needs `rerecord_narration`.
Say the cost first. Render only when they ask.
