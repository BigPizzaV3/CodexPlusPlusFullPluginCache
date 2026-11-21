---
name: canvas-agent-workflows
description: "Use when the user explicitly asks for a CinAI Canvas or a multi-step workflow (for example image to video to edit) that they can open and rerun on cinai.tv. For a single image, video or voiceover use direct-creation."
---

# Build a Canvas workflow

1. Start the canvas. Call `create_canvas` with a `title` and short `description`. To continue an existing one, find it with `list_canvases` and confirm it with `open_canvas`.
2. Pick models. Call `list_models` (and `get_model` for settings) to get a `model_id` for each generator step. Never guess ids.
3. Add the steps.
   - Whole graph on a new canvas: call `compose_canvas_workflow` with `nodes` and `edges`.
   - A few steps, or changes to a canvas that already has content: use `create_canvas_node`, then `connect_canvas_nodes`. Ask before replacing anything on an existing canvas.
   - Node types: `imageInput`, `videoInput`, `audioInput` and `textPrompt` hold the user's material; `image-generator`, `video-generator`, `audio-generator` and `text-generator` create media or text; `edit-video-generator` joins clips and audio on a timeline; `threeDComposition` is a 3D scene.
   - Port handles are filled in automatically when you leave them out.
4. Tidy. Call `organize_canvas_layout`.
5. Run only with consent. Nodes do not run by themselves. Before `run_canvas_node`, call `estimate_cost` for the node's model and settings, tell the user the credits, and wait for a yes. Poll `get_job` for each run.
6. Reusable app (optional). If the user wants a reusable app, call `configure_canvas_app` to mark its inputs and final output, then tell them to press "Make app" on the canvas at cinai.tv to publish it.
7. Share the `https://cinai.tv/WorkflowEditor?id=<canvas_id>` link returned by the tools.
