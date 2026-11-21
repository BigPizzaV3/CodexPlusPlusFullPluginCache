---
name: soundtrack-studio
description: Generate music cues. Use for the supported Soundtrack Studio workflow.
---

Generate a five- to 47-second music cue from a scene, mood and instrumentation brief. Listen and download the audio inline. Instrumental output is requested, but musical details and duration may vary. This does not copy artists, clone voices, synchronize music to video or guarantee exclusivity or licensing rights.

Use the connected Soundtrack Studio MCP tools. Ask for a scene, mood or instrumentation brief; do not request an attachment.

Call `soundtrack_generate` once per requested output and wait for the synchronous response. Show the real inline widget with its media controls and Download. Do not replace it with a website link. If the tool is unavailable, explain the connection requirement. Never download or execute external helper code. Do not retry uncertain generation; reopen completed media with `soundtrack_generate_preview` using its actual generation_id or job_id. Never fabricate completion.

Sources are processed by Firemoon and its media providers. Source and generated media links can be accessed by anyone holding them; some processed-video result links expire after 24 hours. Respect the requested scope and explain supported limits.

## Guest access and optional account linking

This audio-only workflow requires OAuth when used; the daily image/video allowance does not apply. Account linking accesses existing account entitlements. Do not list plans or credit packs, promote digital upgrades, or create checkout links in the plugin.
