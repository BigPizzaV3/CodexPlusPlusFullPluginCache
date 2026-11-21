---
name: event-recap-video
description: "Make an event recap with Vidova, the AI video editor. Use when someone asks for a recap or aftermovie of an event or a year: a party, a festival, a conference, a launch, a team or school year, or a community celebration. Vidova cuts, captions, animates, adds music and renders the video in the cloud."
license: MIT
---

# Event recap

The people who were there watch it to see themselves, and everyone else watches to wish they had been.

## Steps

1. Check that the Vidova tools are available, for example with `get_active_project`. If they are not, ask the person to connect the Vidova plugin and sign in.
2. Make a project with `create_project`. If the person attached files in this chat, bring them in with `import_attached_files`. A file over 512 MB cannot be attached: call `create_upload_link` and give the person its link, where they add the file from their device. Use `import_asset_url` for a link to a file. Call `wait_for_asset` with every Asset ID until the files are ready. For a whole new edit from these files, call `start_routine` with routine `edit_prep` and the person's brief word for word before you read the footage. Call `wait_for_jobs` until it is done, follow its handoff, then go to the step that calls `check_edit`.
3. Read every photo and clip with `read_asset`: who is in it, where the faces are, whether it is a stage, a crowd, a speaker or the group photo, and whether its sound matters. Leave out blurry and dark files.
4. Call `search_templates`. When a template fits, use `read_template` and `apply_template`, then adjust it with `patch_film`. When none fits, build the film with `patch_film`.
5. Follow the order they gave. Find music with `search_stock` kind music, add it with `import_stock`, and read it with `detect_beats`. Keep a speech line or a cheer in its real sound, with captions from `transcribe_asset`.
6. Watch the result with `preview_timeline`, and with `preview_range` across the moments that move. Call `check_edit`, then `wait_for_jobs` with its Job ID, and fix what it names.
7. Call `render_video`, wait for it with `wait_for_jobs`, then give the person the project `url` and the link to the finished video.

## What makes it work

- The person's brief comes first: their order, song, length, format and rules. This skill fills in the rest.
- Name the event in the first second, over faces and energy.
- A named order is a hard rule.
- Match the mood: a party or a festival is fast and upbeat, a memorial is warm and steady, a conference is clean and confident.
- A photo fills the frame with a slow push, with the faces in the upper half.
- End on everyone together, with a closing line or the next date they gave.
- Use only the names, roles, dates, places and numbers they wrote or that appear on their own pictures. Spell names exactly.
