---
name: animation
description: Make a logo reveal, launch film, kinetic type piece, explainer, data animation, 3D scene or other motion graphic from one of Igly's 1,100+ animation prompts. Use when the user wants an animation, motion graphic, animated intro or code-made video rather than a static design.
---

# Animation

Igly has 1,100+ animation prompts with playable previews. Start from one instead of writing the animation from scratch. When the user needs an MP4 file, use the `video-template` skill instead.

## 1. Find an animation
- `list_animations` with a `query` from the request ("logo reveal", "particles", "ocean") and/or a `category` (launch-film, showreel, kinetic-type, explainer, data-viz, 3d-scene, interactive, art).
- It also opens a picker with previews in the board view. If the user wants to browse, let them pick there; their pick comes back as a message with the changes they want.
- If they have not decided between a design and an animation, call `browse_igly` instead.

## 2. Build it
- `get_animation` with the chosen id returns the full prompt.
- Build one self-contained HTML file (inline CSS and JS, libraries from a CDN) in an artifact or canvas preview, so it plays in the chat.
- Replace the original video's brand, product and company names with the user's, or a neutral placeholder if they gave none. Apply their text and colors, and keep the scenes and timing unless they ask for changes.
- If the user has not said what to change, ask for their brand name, text and colors first.
