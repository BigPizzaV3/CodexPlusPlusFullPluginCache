---
name: vertical-remix
description: Reframe short videos. Use for the supported Vertical Remix workflow.
---

Reframe an attached MP4/MOV up to ten seconds and 50 MB into vertical, square or portrait formats. Choose center crop or padding; optional AI extension supports vertical and square. Watch and download the result inline. Crop can remove edge content; AI extension may alter details or audio.

Use the connected Vertical Remix MCP tools. Use actual chat attachment objects or user-supplied HTTPS links; never invent references or pass local paths to the remote server. If the host exposes no downloadable attachment reference, explain that limitation. Supply a stable request_id for each video edit; reuse it to recover interrupted crop/pad processing.

Call `reframe_video` once per requested output and wait for the synchronous response. Show the real inline widget with its media controls and Download. Do not replace it with a website link. If the tool is unavailable, explain the connection requirement. Never download or execute external helper code. Do not retry uncertain generation; reopen completed media with `reframe_video_preview` using its actual generation_id or job_id. Never fabricate completion.

Sources are processed by Firemoon and its media providers. Source and generated media links can be accessed by anyone holding them; some processed-video result links expire after 24 hours. Respect the requested scope and explain supported limits.

## Guest access and optional account linking

Start by calling the workflow tools directly. Do not request account linking before using the anonymous daily image/video allowance. Guests share 100 image/video outputs per host guest identity per UTC day; each image variation counts separately. Only offer account linking when the tool returns an authentication challenge or the user explicitly wants to use account credits. Never invent a guest identifier or bypass a quota response. Preserve existing attachment requirements and uncertain-job retry safeguards. Account linking accesses existing account entitlements. Do not list plans or credit packs, promote digital upgrades, or create checkout links in the plugin.
