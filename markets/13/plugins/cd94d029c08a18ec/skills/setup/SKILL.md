---
name: setup
description: Set up the Buzzy plugin after install. Use when the user just installed Buzzy, asks to connect Buzzy, or needs to confirm the Buzzy MCP server is signed in.
---

# Buzzy setup

Confirm the bundled Buzzy MCP server is connected, then stop. Do not ask for an API key. This package does not store credentials.

1. The host signs the user in with Buzzy OAuth using the ChatGPT client `https://chatgpt.com/oauth/client.json` and the `mcp` scope. No client secret is stored in this package. If the connection is missing or unauthorized, ask the user to finish that sign-in and wait.
2. Call `list_model` once. A successful response means the server is ready. If it fails because the user is not signed in, send them back to the host sign-in and do not retry with a made-up token.
3. Tell the user Buzzy is ready, in one short sentence. Do not start a generation during setup.

After setup, use the connected server directly:

- A single image or video: call `list_model`, copy `resolution`, `aspect_ratio`, and `duration` from the chosen model, then call `generate_image` or `generate_video`. Poll `get_task` until it succeeds. Do not submit the same generation again while it is still running.
- A narrated, ad, UGC, or story video: call `load_workflow` with no arguments, then load the matching workflow by name. Call `create_project` before any tool that needs `projectId` or `project_id`, and reuse that id for the rest of the run.
