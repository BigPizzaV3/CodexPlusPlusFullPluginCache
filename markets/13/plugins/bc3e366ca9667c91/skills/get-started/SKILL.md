---
name: get-started
description: How to use DoveRunner Lab in ChatGPT: documentation search, Academy tutorials, Multi-DRM and Forensic Watermarking demos.
---

# DoveRunner Lab

Use these tools when the user asks about DoveRunner products (Multi-DRM, Forensic and Distributor Watermarking, Anti-Piracy, Transcoding & Packaging, Mobile App Security).

## Which tool

- **Documentation questions** ("how do I...", API fields, integration steps): call `search`, then `fetch` on the best result. Answer from the fetched page and link it. Do not guess specs.
- **Learning material** ("is there a tutorial on..."): call `find_tutorial`.
- **Seeing it work** ("play the DRM demo", "show watermarking"): call `play_demo` with `demo` = `drm-vod` (Multi-DRM video on demand, default), `drm-live` (live; the channel starts on demand and can take about a minute, so if the result says it is starting, tell the user to ask again shortly) or `fwm` (Forensic Watermarking).

## Rules

- For pricing, plans or purchasing, point to https://doverunner.com/contact-us/. This plugin does not quote prices or sell anything.
- Playback depends on the host. If the panel says playback is not available, share the Lab Playground link it offers; do not retry the tool.
- The Forensic Watermarking demo only shows that the watermark is invisible; its session data is the server's, not the viewer's. Do not present it as tracing a real viewer.
- Never ask for or repeat license tokens, keys or credentials.
