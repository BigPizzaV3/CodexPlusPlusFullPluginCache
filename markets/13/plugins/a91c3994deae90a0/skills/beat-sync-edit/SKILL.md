---
name: beat-sync-edit
description: "Make a beat-synced edit with Vidova, the AI video editor. Use when someone asks for an edit cut hard to a song: a fan edit, a car or bike edit, a gaming, anime or movie montage, a phonk or hype edit. Vidova cuts, captions, animates, adds music and renders the video in the cloud."
license: MIT
---

# Beat-sync edit

A song and the best few seconds of every clip, cut so each hit of the song lands on something happening.

## Steps

1. Check that the Vidova tools are available, for example with `get_active_project`. If they are not, ask the person to connect the Vidova plugin and sign in.
2. Make a project with `create_project`. If the person attached files in this chat, bring them in with `import_attached_files`. A file over 512 MB cannot be attached: call `create_upload_link` and give the person its link, where they add the file from their device. Use `import_asset_url` for a link to a file. Call `wait_for_asset` with every Asset ID until the files are ready. For a whole new edit from these files, call `start_routine` with routine `edit_prep` and the person's brief word for word before you read the footage. Call `wait_for_jobs` until it is done, follow its handoff, then go to the step that calls `check_edit`.
3. Call `detect_beats` on the song for the beats, the downbeats and the drop. Read each clip with `read_asset` and note its peak moment to a tenth of a second. Those peaks are what the edit is made of. Leave out clips where the subject is small or off screen.
4. Call `search_templates`. When a template fits, use `read_template` and `apply_template`, then adjust it with `patch_film`. When none fits, build the film with `patch_film`.
5. Start 4 bars before the drop, where a bar lasts 4 x 60 / bpm seconds. Use 2 to 4 slower shots for the intro, then one beat each, then half a beat in the last bar. Put the best clip on the drop, and one beat or half a beat per shot after it. End on the strongest image, slowed so it still moves.
6. Watch the result with `preview_timeline`, and with `preview_range` across the moments that move. Call `check_edit`, then `wait_for_jobs` with its Job ID, and fix what it names.
7. Call `render_video`, wait for it with `wait_for_jobs`, then give the person the project `url` and the link to the finished video.

## What makes it work

- The person's brief comes first: their order, song, length, format and rules. This skill fills in the rest.
- Use the song they named or uploaded. Never swap it for another.
- Every shot shows the subject of the edit.
- Put every clip's peak on a beat: rush into it, slow hard to about quarter speed on the beat, and rush out. It never stops.
- Frame 0 is the thumbnail: a bright, readable frame of the subject.
- Vary the shot lengths. An even run of equal shots reads as a metronome.
- `search_effects` and `apply_effect` put one effect on the drop. Never put effects on every cut.
