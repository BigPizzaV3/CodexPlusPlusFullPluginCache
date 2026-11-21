---
name: family-video
description: "Make a family video with Vidova, the AI video editor. Use when someone asks for a family edit from the person's own clips and photos: a summer, a holiday, a year with the kids, a tribute, a wedding or an anniversary. Vidova cuts, captions, animates, adds music and renders the video in the cloud."
license: MIT
---

# Family video

The person's own clips of people they love, cut to music, made to be shared in the family chat.

## Steps

1. Check that the Vidova tools are available, for example with `get_active_project`. If they are not, ask the person to connect the Vidova plugin and sign in.
2. Make a project with `create_project`. If the person attached files in this chat, bring them in with `import_attached_files`. A file over 512 MB cannot be attached: call `create_upload_link` and give the person its link, where they add the file from their device. Use `import_asset_url` for a link to a file. Call `wait_for_asset` with every Asset ID until the files are ready. For a whole new edit from these files, call `start_routine` with routine `edit_prep` and the person's brief word for word before you read the footage. Call `wait_for_jobs` until it is done, follow its handoff, then go to the step that calls `check_edit`.
3. Read every clip and photo with `read_asset`: the moment with the most feeling and its time, where the faces are, whether its sound is worth keeping, and whether it is dark, shaky or soft.
4. Call `search_templates`. When a template fits, use `read_template` and `apply_template`, then adjust it with `patch_film`. When none fits, build the film with `patch_film`.
5. Cut to the music. Find a track with `search_stock` kind music, add it with `import_stock`, and read it with `detect_beats`. Grade every clip to one look.
6. Watch the result with `preview_timeline`, and with `preview_range` across the moments that move. Call `check_edit`, then `wait_for_jobs` with its Job ID, and fix what it names.
7. Call `render_video`, wait for it with `wait_for_jobs`, then give the person the project `url` and the link to the finished video.

## What makes it work

- The person's brief comes first: their order, song, length, format and rules. This skill fills in the rest.
- Use fewer, better moments, and leave out the soft, dark and shaky clips. A 25 second edit of eight good moments beats 60 seconds of everything.
- Make 20 to 40 seconds for sharing, or up to 60 seconds for a tribute.
- Open on the best moment, already happening, with people in frame 0.
- Cut every two beats in the lively parts. A hug or a sentence gets a whole bar. A wedding or a tribute is slower.
- Lower the music once for 1 to 2 seconds under a real sound, such as a laugh, then bring it back on a downbeat.
- End on the warmest wide shot for 3 seconds or more, still moving, with the music fading out with the picture.
- Use the names, places and years they wrote. Never invent them. Never darken a face, and keep text off faces.
