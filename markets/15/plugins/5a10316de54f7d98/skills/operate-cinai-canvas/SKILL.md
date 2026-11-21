---
name: operate-cinai-canvas
description: "Use when the user wants to find, inspect, edit or run nodes on one of their existing CinAI Canvas projects."
---

# Operate an existing Canvas

1. Find it. Call `list_canvases`, then `open_canvas` with the chosen `canvas_id` to confirm it and get its link.
2. Read it. Call `get_canvas_state` for the node and edge graph, and `get_canvas_node_details` for a node's prompt, settings and outputs.
3. Change it.
   - `update_canvas_node` edits a node's title, prompt, settings or model. Say what will change and get a yes first, because it overwrites the old values.
   - `create_canvas_node` and `connect_canvas_nodes` add steps and wires. Take `model_id` values from `list_models`; never guess them.
   - `disconnect_canvas_nodes` and `delete_canvas_nodes` remove things. Only act on nodes the user named, and confirm before deleting.
   - `organize_canvas_layout` tidies the layout without changing content.
4. Run a node. Call `estimate_cost` for the node's model and settings, tell the user the credits, and wait for a yes. Then call `run_canvas_node` with a new `idempotency_key` and poll `get_job`. The finished media is written back into the node.
5. Share the `https://cinai.tv/WorkflowEditor?id=<canvas_id>` link so the user can open the canvas.

There is no tool to delete a whole canvas; the user can do that on cinai.tv.
