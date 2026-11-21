---
name: edit-video
description: Change a Crealix video after it is made, such as its lines, voices, captions, music, scene images and clips, Reddit posts, tweets and chat messages, text overlays and sound effects, with undo. Use when the user asks to change, fix, polish or re-edit a video, or reacts to a draft ("the voice is too slow", "change scene 3").
---

# Edit a video

Most edits are free and reversible. What costs credits is new media: new
images, clips, or a narration re-recorded. Say the price before any of those.

## 1. Find it and read it

- The video they mean: the one in this conversation, or `list_projects` (by type
  or folder) when it is from earlier.
- `get_project` before editing. It returns the scenes by number, the content ids
  (tweets, people, messages), what is out of date, and the editor link.
- Several changes at once: group them into one call per tool, so the user
  confirms once.

## 2. Use the right tool for the type

| Video | What changes | Tool |
|---|---|---|
| Faceless, scene by scene | Title, voice, captions, style, music, volumes; per scene its text, length, media, prompt, move, transition | `update_project`, `update_captions` |
| Faceless, scene by scene | Add or remove scenes, overlays, sound effects | `add_scenes`, `add_text_overlays`, `add_sound_effects`, `remove_project_items` |
| Faceless, scene by scene | New images or voice for some scenes | `generate_scene_media` |
| Faceless, scene by scene | Turn scenes into clips | `animate_scenes` |
| Reddit story, tweets, text messages, split screen | Words, people, voices, card, gameplay, narrator, captions, music, mix | `edit_video`, then `rerecord_narration` |
| Stock footage, AI skeleton | Title, captions, music, mix; what a scene shows | `edit_video` (`scenes`) |
| Talking objects, AI drama, AI short film, music video | Title, captions, music, mix | `edit_video` |

What no tool changes (reworking the scenes of talking objects, dramas, films and
music videos) is done in the Crealix editor: share its link. Never open it for
the user.

## 3. Rules that keep edits safe

- New words don't re-record themselves. Faceless and scene-by-scene: call
  `generate_scene_media` with voice for the changed scenes. Card formats:
  `edit_video` says what no longer matches and the cost, and `rerecord_narration`
  records just that. Say the cost first.
- Clips are approved before they are made. The first `animate_scenes` (or
  `generate_scene_media` with video) spends nothing and returns each clip's
  model, length, quality and price. Tell the user all four, and which ones
  Crealix picked because they didn't. Call it again with its `confirmationId`
  only after they agree.
- An earlier image or clip of a scene (`get_project` scenes[].versions) goes back
  with `update_project`, for free.
- `remove_project_items` cannot be undone: confirm first. Everything else can be
  reversed with `undo_last_change`, step by step.
- Better stock footage: `search_stock_media`, `import_media_from_url` with its
  `videoUrl`, then `update_project` (faceless) or `edit_video({ scenes })`.

## 4. Finishing touches

- A voice effect on the narration: `set_voice_effect` (free).
- The cover (thumbnail): follow the video-cover skill.
- A captions look of their own: `save_caption_style`, then use it here.

## 5. After editing

Say in one line what changed. A video that was already rendered shows as out
of date: offer to render again once they are done editing, and only render
when they say so (the card's Render button, or `render_project`).
