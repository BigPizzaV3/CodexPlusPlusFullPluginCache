---
name: brand-kit
description: Set up the user's Crealix brand so new videos start on-brand (voice, style, captions, music, format, card identity), design their own caption styles (My Captions) and save recurring characters. Use when the user says "always use…", or asks to save defaults or a brand, make custom captions, or keep a mascot consistent.
---

# Brand kit

Their brand (My Brand) is what every new video starts from. Their own caption
styles live in My Captions, and their recurring people and mascots are saved
characters. Everything here is free, except drawing a character's portrait
(about 1 credit).

## 1. See what they have

`get_brand` shows their brand as a card: what they set, and what falls back to
Crealix's featured picks.

## 2. Save to the brand, only when asked

`update_brand` changes only the fields sent (null clears one). Use it only when the
user asks: "always use this voice", "make this my default", or "Save to my
brand" on a proposal. Never on your own.
- Voice (`voiceId`) and delivery (`voiceSettings`), visual style, captions (a
  preset or one of theirs) and their position, music, aspect ratio, language,
  volumes, gameplay.
- Card identity: `reddit` (display name, subreddit, verified, theme) and `x`
  (display name, handle, verified, theme).

Say what changed, and that videos already made keep their settings. To undo,
send back the `previous` values from the answer.

## 3. Their own captions (My Captions)

`save_caption_style` designs a style and shows it with a live preview:
- from scratch: a `name` and the look (font, size, weight, letter case, the
  spoken word's colour, the other words' colour, box, highlight, animation,
  words at a time, height, outline, shadow);
- from a Crealix preset or one of theirs (`basedOn`), with only what changes;
- or change one of theirs (`styleId`).

Its id then works wherever a caption preset does: proposals, `update_captions`,
`edit_video`, the brand. Changing it later doesn't touch videos already made.
`delete_caption_style` only when they ask and confirm which one.

## 4. Characters that come back

`create_character` saves a person, mascot or creature so it looks the same in
every video:
- from their picture (in Crealix first: `import_media_from_url` or
  `upload_media`), free;
- or drawn from a description, optionally in a visual style to match their
  videos (about 1 credit, ready in under a minute; check `get_status`).

Use it in faceless videos, AI skeletons, AI short films and music videos
(`characterIds`), in avatars and motion control (`characterId`), or as a
reference image.
