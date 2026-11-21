---
name: explainer-video
description: "Make an explainer video with Vidova, the AI video editor. Use when someone asks for an explainer: an idea, a product, a process, a lesson or a set of facts turned into a short animated story with a voiceover or on-screen words. Vidova cuts, captions, animates, adds music and renders the video in the cloud."
license: MIT
---

# Explainer video

One idea made clear in under a minute, so a viewer can repeat it to a friend.

## Steps

1. Check that the Vidova tools are available, for example with `get_active_project`. If they are not, ask the person to connect the Vidova plugin and sign in.
2. Make a project with `create_project`. If the person attached files in this chat, bring them in with `import_attached_files`. A file over 512 MB cannot be attached: call `create_upload_link` and give the person its link, where they add the file from their device. Use `import_asset_url` for a link to a file. Call `wait_for_asset` with every Asset ID until the files are ready. For a whole new edit from these files, call `start_routine` with routine `edit_prep` and the person's brief word for word before you read the footage. Call `wait_for_jobs` until it is done, follow its handoff, then go to the step that calls `check_edit`.
3. Write the one sentence the viewer should know at the end, then the script. A hook of up to 3 seconds, three to five steps of one sentence each, and a takeaway of 3 to 5 seconds. A script the person wrote is the script.
4. Call `search_templates`. When a template fits, use `read_template` and `apply_template`, then adjust it with `patch_film`. When none fits, build the film with `patch_film`.
5. With a recorded voice, call `transcribe_asset` for the word times and cut each scene on its sentence. Without a voice, show one short line per step. Give each step its own picture: their footage, a screen, an element from `search_elements`, or a device frame from `search_stock`.
6. Watch the result with `preview_timeline`, and with `preview_range` across the moments that move. Call `check_edit`, then `wait_for_jobs` with its Job ID, and fix what it names.
7. Call `render_video`, wait for it with `wait_for_jobs`, then give the person the project `url` and the link to the finished video.

## What makes it work

- The person's brief comes first: their order, song, length, format and rules. This skill fills in the rest.
- Open on the question or the surprising fact, in the viewer's words, over a picture that already shows it.
- A step that holds two ideas becomes two steps.
- Use only facts the person gave or common knowledge. Never invent a statistic, a date, a study or a quote.
- Never use the same picture for two steps, or footage that has nothing to do with the sentence.
- Punch in on the detail the voice names, landing on the word. A caption never covers that detail.
- Make 30 to 60 seconds for social, or 60 to 120 seconds for a lesson. Use 9:16 unless they ask for YouTube, a course or a presentation.
