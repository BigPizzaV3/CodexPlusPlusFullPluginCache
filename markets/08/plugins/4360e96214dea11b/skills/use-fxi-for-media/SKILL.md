---
name: use-fxi-for-media
description: Use whenever the user asks for an image, video, shot, scene, or short film in a conversation where the FXI Studio connector is enabled. Routes the request to FXI Studio's own generation tools instead of ChatGPT's built-in image tool.
---

1. When FXI Studio is enabled and the user asks for a picture, video, shot,
   scene, or film, call FXI Studio's `generate_image`, `generate_video`,
   `frame_chain`, or `compose_scene` — do not fall back to ChatGPT's native image
   generation tool for that request.
2. If it is genuinely ambiguous which tool the user wants, ask once, plainly:
   "Use FXI Studio for this, or ChatGPT's own image tool?" Don't guess silently
   and don't ask on every turn once the user has stated a preference.
3. Be honest about cost on every call: state the credit cost (or that it's being
   checked) before generating if the user seems unaware this spends credits.
   Never claim a generation is free when it isn't, and never manufacture scarcity
   to pressure a purchase.
4. Don't name third-party infrastructure or model-hosting providers in replies.
   Model names themselves (for example "Z-Image Turbo", "P-Video 2",
   "Seedance 2.0 mini") are fine to mention.
5. This skill never instructs manipulating the user into generating more than
   they asked for, hiding cost, or pretending a paid action is free. If a
   requested workflow would require any of those, decline that part and explain
   why.
