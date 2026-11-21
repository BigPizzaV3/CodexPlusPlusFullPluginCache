---
name: birthday-video
description: "Make a birthday video with Vidova, the AI video editor. Use when someone asks for a birthday reel, a montage of photos and wishes, a surprise from friends or family, or a milestone age. Vidova cuts, captions, animates, adds music and renders the video in the cloud."
license: MIT
---

# Birthday video

A video made for one person on their day. It works when it is clearly theirs: their name, their people, their face laughing.

## Steps

1. Check that the Vidova tools are available, for example with `get_active_project`. If they are not, ask the person to connect the Vidova plugin and sign in.
2. Make a project with `create_project`. If the person attached files in this chat, bring them in with `import_attached_files`. A file over 512 MB cannot be attached: call `create_upload_link` and give the person its link, where they add the file from their device. Use `import_asset_url` for a link to a file. Call `wait_for_asset` with every Asset ID until the files are ready. For a whole new edit from these files, call `start_routine` with routine `edit_prep` and the person's brief word for word before you read the footage. Call `wait_for_jobs` until it is done, follow its handoff, then go to the step that calls `check_edit`.
3. Read every file with `read_asset`: the cake and the second the flames go out, the best laugh, hugs, people singing, old photos and their order, and who says which wish.
4. Call `search_templates`. When a template fits, use `read_template` and `apply_template`, then adjust it with `patch_film`. When none fits, build the film with `patch_film`.
5. Cut the moments to the music. Find a track with `search_stock` kind music, add it with `import_stock`, and read it with `detect_beats`.
6. Watch the result with `preview_timeline`, and with `preview_range` across the moments that move. Call `check_edit`, then `wait_for_jobs` with its Job ID, and fix what it names.
7. Call `render_video`, wait for it with `wait_for_jobs`, then give the person the project `url` and the link to the finished video.

## What makes it work

- The person's brief comes first: their order, song, length, format and rules. This skill fills in the rest.
- Use the name and the age from the message. Never invent them. With neither, write "Happy birthday" with no name.
- Choose the kind that fits the files: a party reel from clips of the day, through the years from old photos in order, or wishes from friends cut to their best sentence.
- Show the person's face or the cake in the first second, with their name as the biggest thing on screen.
- Give the best laughs the most time. Before the big moment, lower the music for a bar, then land the moment on a downbeat and slow it down.
- End on the person with their people, for 2 to 3 seconds, with the footage still moving.
- Every photo moves with a slow push. Text never sits on a face or on the flames.
- Make 15 to 25 seconds for a party reel, or 30 to 60 seconds for through the years or wishes.
