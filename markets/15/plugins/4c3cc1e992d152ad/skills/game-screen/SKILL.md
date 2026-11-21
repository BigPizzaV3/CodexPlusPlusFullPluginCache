---
name: game-screen
description: Use to select a screen, measure its map viewport, pan or zoom the map, show media, or create, play and delete soundboard effects.
---

# Game screen

Call `get_game_screen` to see whether the table display is live and which components are connected. A browser can show the character list (`character_list`), map or URL (`game_view`), and overlay (`overlay`). Screen managers receive `active_screen` and the recent `live_screens`. Each has an ID, full window `width`/`height`, map `game_width`/`game_height`, and character-list `characters_width`/`characters_height` in pixels. Use the **map viewport** to frame a room. A 1920 × 1080 TV might give the map only 1920 × 864.

Use `position_game_map` for pan and zoom. Zoom 0 fits the image and 100 doubles it. X and Y offsets are percentages of the scaled image dimension on that axis. To restore the fitted, centered view, send zero for `image_zoom`, `image_position_x` and `image_position_y`. Delegated screen managers can position the visible active map. Campaign layout changes use `update_campaign` with Maintain access.

For “create an applause effect and play it,” check the member’s `list_sound_effects` first. If a playable applause cue exists, use its ID. To add a supplied or host-generated clip, use `import_upload`, then `create_sound_effect` with the signed ID as `file` and `name` set to Applause. Soundboard clips can be MP3, Ogg audio or WAV, up to 10 seconds and 2 MiB. If there’s no audio file available, ask for the clip. Play once with `play_sound_effect` when the returned `playable` flag is true. Report dispatch. The TV controls its own audio permissions.

Use `delete_sound_effect` when asked to remove a cue. Find locked slots with `include_locked: true`. Deleting a cue also removes automation rules targeting it. For a one-off image, video or audio handout, use the Reveals skill. For table dice, use the Dice rolling skill.
