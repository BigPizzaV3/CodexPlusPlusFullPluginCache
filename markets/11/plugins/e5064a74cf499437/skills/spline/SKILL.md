---
name: spline
description: Build and edit 3D scenes and 2D designs (websites, landing pages, app screens, UI) live in the Spline editor, which opens in a panel beside the chat. Use when the user mentions Spline, or asks for a 3D scene, object, animation or interactive 3D experience, or for a page or screen design they want to see and keep editing visually.
---

# Spline

One set of tools drives two Spline editors:

- **3D** (`3d_*` tools): scenes, objects, materials, lighting, cameras,
  animation and interactivity, authored in Spline's editor DSL.
- **2D design, "Hana"** (`2d_*` tools): websites, app screens, UI and
  posters, authored as an HTML + CSS subset that becomes a live Spline design.

Pick by what the user wants to end up with: a 3D scene → `3d_*`; a page or
screen → `2d_*`.

## Start

1. **Put an editor on screen.** Call `spline_create_file` (`kind: "3d"` or
   `"2d"`) for something new, `spline_open_file` for an existing file, or
   `spline_canvas` to just open Spline. It opens the Spline panel beside the
   chat, where the user watches you build. Call the scene tools right after;
   they wait for the editor to load. (Where there is no panel, the result is
   a link instead: give it to the user and carry on.)
2. **Read the authoring guide before you author.** 3D:
   `3d_load_skill("authoring-guide")`, then the further parts it names. 2D:
   `2d_load_skill("authoring-guide")` and `2d_load_skill("authoring-guide-2")`,
   plus any effect skill the design needs. The guides own the syntax and the
   quality bar; don't guess either.
3. **Ground yourself** with `3d_get_scene_mcp` or `2d_get_canvas_state`.

## Build, look, refine

Spline's own in-editor agent works in passes, and the results show it. Work
the same way:

- Build in steps (`3d_run_code`; `2d_reserve_frames` then `2d_write_html`).
- After each meaningful step, **look**: `3d_take_screenshot` (aim it with
  `3d_set_view`) or `2d_review_frame`. Check facts by re-reading the scene;
  judge looks from the image.
- **Refine at least twice** before you call it done: first composition,
  scale and framing; then materials, lighting and detail. Fix what the
  screenshot shows, not what you meant to build.
- Stop when the result meets the guide's quality bar, not when the first
  build runs without errors.

## Rules

- **One file per design.** Follow-up requests edit the open file; don't call
  `spline_create_file` again. If a create reports a file is already open,
  carry on in it.
- If a tool says no editor is open, open one (step 1) and retry. If it says
  the editor didn't finish loading, retry in a moment instead of creating
  another file.
- If a call says Spline isn't signed in, ask the user to reconnect the Spline
  app rather than building the design some other way.
- **To undo**, when the user asks to undo, roll back or go back to how
  it was: `3d_list_versions` / `2d_list_versions`, then
  `3d_restore_version` / `2d_restore_version` with the version to go back
  to. A "Before AI edits" version is saved before your first edit of each
  request, so the newest one undoes your last request. Say which version
  you restored, then re-read the scene before editing again. Don't try to
  undo by rebuilding what was there by hand.
- When you finish, tell the user the result is in the Spline panel and what
  you built, so they can keep editing it themselves.
