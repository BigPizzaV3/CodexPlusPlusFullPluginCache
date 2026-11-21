---
name: runchat
description: Build, run and publish design workflows in Runchat, and drive the user's Rhino, Grasshopper, Blender or ClipChat session through the Runchat connector. Use when the user mentions Runchat, a runchat workflow, or asks to script or inspect a model in a connected desktop app.
---

# Working with Runchat

Runchat is a node-based canvas for design workflows. A saved workflow is a "runchat". The Runchat connector's tools act on the signed-in user's own account.

## Workflows

1. Find an existing runchat with `list_runchats`, or make one with `create_runchat` (pass `copy` to start from an existing runchat). Every canvas tool takes its id as `runchat_id`.
2. Add nodes with the `create_*_node` tools, wire them with `connect_nodes`, then call `organize_nodes` once.
3. `run_nodes` executes the workflow and spends the user's Runchat credits. Say what will run before running anything costly.
4. Share the returned `editor_url` so the user can open the canvas.

Load the matching guide with `use_skill` before writing code nodes, prompting image models, or building an app page.

## Desktop apps

The `run_rhino_command`, `run_blender_command`, `grasshopper_*`, `take_screenshot` and `clipchat_*` tools reach the user's own desktop app through the Runchat plugin running inside it. They change the user's open document, so describe the change before making it, and check the result with `take_screenshot`. If a tool reports that no app is connected, ask the user to open Runchat inside the app and sign in.

## Publishing

`publish_runchat` lists a workflow as a tool other people can run, and `create_artifact` puts a page at a public URL unless `visibility` is `private`. Confirm the name and visibility with the user first.
