---
name: generate-deep-art-video
description: Generate a brand-new video from a text description with the Deep Art AI MCP server. Use when the user asks Deep Art AI to create, generate, render, animate, or explore a video, cinematic scene, motion concept, advertisement, product video, animated background, portrait sequence, or visual variant. Do not use for editing an existing video unless the connected Deep Art AI tool supports video-to-video editing and the user requests it.
---

# Generate a Deep Art AI Video

Create an video with Deep Art AI, preserve the user's intent, and display the result in the conversation.

## Workflow

1. Extract the subject, setting, composition, style, mood, lighting, palette, aspect ratio, and exclusions from the request.
2. Ask a question only when a missing detail would materially change the result. Otherwise choose tasteful defaults and proceed.
3. Connect to the Deep Art AI MCP server and inspect the current create_video tool schema before constructing arguments. Never guess tool names, parameter names, or enum values.
4. If the server or generation tool is unavailable, explain that Deep Art AI must be connected. Do not silently substitute another video generator.
5. Build one concise visual prompt. Put the subject and composition first, followed by style, environment, lighting, palette, camera or rendering details, and constraints.
6. Preserve requested text exactly. Warn briefly that video models may render text imperfectly.
7. Map only options supported by the current tool schema. Honor requested dimensions, aspect ratio, video length, quality; otherwise use server defaults.
8. Generate once unless the user requests variants. If the server reports an actionable prompt or parameter error, revise once and retry.
9. Use the jobId returned from tool create_video when submitting the video and call the get_video_status tool to check its status. Do not submit the video again.
10. Inspect the response for the video URL or an error. If neither is available, wait 20 seconds and call get_video_status again with the same jobId. Repeat until the video URL is returned or the server reports an error.
11. When the video URL is available, show the download URL to the user. Request network permission before downloading when required, then download and save the video and display it to the user.

## Prompt Guidance

- Describe visible details instead of abstract praise.
- Keep negative constraints in a negative-prompt field when supported; otherwise append a short `Avoid:` clause.
- For variants, keep the core subject stable and change one dimension at a time.
- Do not claim that Deep Art AI generated a video until the tool returns successfully.

## Example Requests

- “Use Deep Art AI to generate a cinematic video of an alpine lodge at blue hour.”
- “Create an 8-second cinematic video of a robot tending a rooftop garden.”
