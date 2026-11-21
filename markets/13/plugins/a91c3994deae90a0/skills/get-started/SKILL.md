---
name: get-started
description: "Get started with Vidova and make a first edit. Use right after the plugin is set up, or when someone asks how to start with Vidova."
license: MIT
---

# Get started with Vidova

Help the person get a finished video from their own footage. Keep it short.

## Steps

1. Call `whoami` to confirm the Vidova account is connected.
2. Ask what video they want, and ask them to attach their clips or photos in this chat, up to 512 MB each.
3. When they attach files, make a project with `create_project`, bring the files in with `import_attached_files`, and call `wait_for_asset` with every Asset ID.
4. Call `start_routine` with routine `edit_prep` and their request word for word, then call `wait_for_jobs` until it is done and follow its handoff.
5. Watch the result with `preview_timeline`. Call `check_edit`, then `wait_for_jobs` with its Job ID, and fix what it names.
6. Call `render_video`, wait for it with `wait_for_jobs`, then give the person the project `url` and the link to the finished video.

If they have a file over 512 MB, or their files are on another device, call `create_upload_link` and give them its link.
