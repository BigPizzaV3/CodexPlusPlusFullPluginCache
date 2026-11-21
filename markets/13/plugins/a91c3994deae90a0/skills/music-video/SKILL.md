---
name: music-video
description: "Make a music video with Vidova, the AI video editor. Use when someone asks for a music video, a visualizer, a lyric video or a song teaser for the person's own song, from their clips, generated shots or both. Vidova cuts, captions, animates, adds music and renders the video in the cloud."
license: MIT
---

# Music video

Pictures that move with a song. The song is the script: its sections set the cut rate, its hits set where the picture turns, and its words set what appears.

## Steps

1. Check that the Vidova tools are available, for example with `get_active_project`. If they are not, ask the person to connect the Vidova plugin and sign in.
2. Make a project with `create_project`. If the person attached files in this chat, bring them in with `import_attached_files`. A file over 512 MB cannot be attached: call `create_upload_link` and give the person its link, where they add the file from their device. Use `import_asset_url` for a link to a file. Call `wait_for_asset` with every Asset ID until the files are ready. For a whole new edit from these files, call `start_routine` with routine `edit_prep` and the person's brief word for word before you read the footage. Call `wait_for_jobs` until it is done, follow its handoff, then go to the step that calls `check_edit`.
3. Call `detect_beats` on the song for the beats, the downbeats and the sections, and `transcribe_asset` for the lyrics with word times. Read each clip with `read_asset`: its best seconds, where the faces are, and whether someone sings on camera.
4. Call `search_templates`. When a template fits, use `read_template` and `apply_template`, then adjust it with `patch_film`. When none fits, build the film with `patch_film`.
5. Cut to the sections. For a lyric video, put one phrase at a time on the vocal. For a visualizer, `search_elements` has audio bars that follow the song.
6. Watch the result with `preview_timeline`, and with `preview_range` across the moments that move. Call `check_edit`, then `wait_for_jobs` with its Job ID, and fix what it names.
7. Call `render_video`, wait for it with `wait_for_jobs`, then give the person the project `url` and the link to the finished video.

## What makes it work

- The person's brief comes first: their order, song, length, format and rules. This skill fills in the rest.
- Make a teaser of 15 to 30 seconds unless they ask for the whole song. A teaser starts a bar or two before the hook, not at the slow intro.
- Pick one visual world for the film: one place, one light, one colour story.
- Verse: one cut per bar, on the downbeat. Build: a cut every two beats. Chorus or drop: the best shots, cut on the beats. Breakdown: one long shot, slowed, that keeps moving. Outro: the strongest image, a face or the brightest light.
- Vary the shot lengths by section. When every shot has the same length, the edit reads as a metronome.
- When someone sings on camera, keep that clip at normal speed and line it up with the vocal.
- Take the artist and the title from the message or the file name. Never invent an artist, and never replace their song.
