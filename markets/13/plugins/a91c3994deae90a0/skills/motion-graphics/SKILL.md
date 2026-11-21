---
name: motion-graphics
description: "Make a motion graphics piece with Vidova, the AI video editor. Use when someone asks for animated type, shapes, numbers and logos for a launch, an announcement, a promo, stats or a brand sting, with or without footage. Vidova cuts, captions, animates, adds music and renders the video in the cloud."
license: MIT
---

# Motion graphics

Type, shapes, colour and numbers that move to music, with each scene one idea read in a second.

## Steps

1. Check that the Vidova tools are available, for example with `get_active_project`. If they are not, ask the person to connect the Vidova plugin and sign in.
2. Make a project with `create_project`. If the person attached files in this chat, bring them in with `import_attached_files`. A file over 512 MB cannot be attached: call `create_upload_link` and give the person its link, where they add the file from their device. Use `import_asset_url` for a link to a file. Call `wait_for_asset` with every Asset ID until the files are ready. For a whole new edit from these files, call `start_routine` with routine `edit_prep` and the person's brief word for word before you read the footage. Call `wait_for_jobs` until it is done, follow its handoff, then go to the step that calls `check_edit`.
3. Find what it announces, the one fact that matters and the call to action. Bring in their logo with `search_logo` and `import_logo`, or use `remove_background` on a logo that sits on a box.
4. Call `search_templates`. When a template fits, use `read_template` and `apply_template`, then adjust it with `patch_film`. When none fits, build the film with `patch_film`.
5. Call `search_elements` and `import_element` for titles, charts, counters and maps. Write a component with `replace_component` when no element fits. Find music with `search_stock` kind music, add it with `import_stock`, and start every scene on a downbeat from `detect_beats`.
6. Watch the result with `preview_timeline`, and with `preview_range` across the moments that move. Call `check_edit`, then `wait_for_jobs` with its Job ID, and fix what it names.
7. Call `render_video`, wait for it with `wait_for_jobs`, then give the person the project `url` and the link to the finished video.

## What makes it work

- The person's brief comes first: their order, song, length, format and rules. This skill fills in the rest.
- Make 12 to 25 seconds, with 5 to 8 scenes of 1.5 to 3 seconds. Each scene says one thing in five words or fewer.
- The hook is on frame 0 and already moving. Never an empty background, a black frame or a logo first.
- Build to the strongest fact. End on the name or logo with one line and the call to action, for 2 to 3 seconds, still moving.
- Set the design before you write: a background, an ink and one accent colour, and one type family unless the brand names its own.
- Keep side margins of 80 px on a 1080 wide frame, and nothing smaller than 44 px.
- A logo alone is enough. Do not fill the piece with unrelated photos from the person's library.
- Use their real words and numbers. Never invent a feature, a price or a number.
