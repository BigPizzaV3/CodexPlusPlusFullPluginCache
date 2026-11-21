---
name: video-cover
description: Design the cover (thumbnail) of a Crealix video, a short headline in a cover style over a striking frame, or over an AI image made for it. Use when the user asks for a thumbnail, a cover, a title on the first frame, or "make an image for my thumbnail".
---

# Video cover

The cover is baked into the first frame of the rendered MP4, the one TikTok,
Reels and Shorts show before anyone presses play. It is a few words in a cover
style over a frozen moment of the video, or over an image. Setting it is free.

## 1. Know the video

`get_project` for its title, type, aspect ratio and length. Styles and how each
looks are in `get_creation_guide(type).cast.coverStyles`.

## 2. Write the headline

- Three to six words that make someone stop scrolling. Not the full title.
  A promise, a number, a shock or a question ("HE LIED FOR 40 YEARS").
- Say it in the video's language. The style's letter case applies.
- No headline at all when the image already says everything.

## 3. Choose what is behind it

- **A moment of the video** (`frameSec`): the most striking frame, a face, a
  reveal, the peak of the action. Not a transition or a blank frame.
- **An AI image made for the cover**:
  1. `generate_images` at the video's aspect ratio, with a prompt for one bold,
     readable subject and empty space where the headline will sit. It costs
     credits: say the price.
  2. Wait until it is done (`get_status`).
  3. Use its URL as `imageUrl`.
- **The user's own image**: bring it into Crealix (`import_media_from_url`, or
  `upload_media`) and use that URL.

## 4. Set it

`set_cover({ projectId, cover: { title, style, position, frameSec or imageUrl } })`.
Choose the style and position that suit this video and keep the headline off
faces and key details. `fontSize` goes up for two or three big words.

Say in one line what the cover says and shows. `undo_last_change` reverts it;
`remove: true` takes it off.

## 5. Render

The cover goes into the next render. A video that was already rendered needs
rendering again to show it: offer it, and render only when they say so.

New videos can carry their cover from the start: pass `cover` in the proposal
(`validate_plan` and `create_video`).
