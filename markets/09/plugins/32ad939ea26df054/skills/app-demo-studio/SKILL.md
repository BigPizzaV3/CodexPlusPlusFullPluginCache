---
name: app-demo-studio
description: Animate screenshots into demos. Use for the workflow below with attached media.
---

Animate an attached app screenshot into a five- or ten-second promo concept, optionally supplying an ending screenshot. Describe camera movement and transitions, then watch and download the MP4 inline. This is generated animation, not a recording of app behavior; text and interface details may distort.

Use the connected App Screenshot Promo Maker MCP tools. Pass the actual chat attachment object into `screenshot`; HTTPS source fields are alternatives. Never invent attachment references or send a local filesystem path to the remote server. If the host has not exposed a downloadable attachment reference, state that limitation. Ask for missing sources or required preferences before generation.

Call `app_animate` once for the requested output. Wait for its synchronous response. Present the real inline widget; do not substitute a website link or an unrelated image editor. If the tool is unavailable, explain that the connection must be enabled. Do not download or execute external helper code. An uncertain timeout must not trigger an automatic retry. Use `app_animate_preview` with an actual returned generation ID to reopen a completed result without generating again.

Inputs are processed by Firemoon and its media providers; media links are accessible to anyone holding them. Respect the user's requested scope. Never claim success after a tool error or guarantee exact fidelity.

## Guest access and optional account linking

Start by calling the workflow tools directly. Do not request account linking before using the anonymous daily image/video allowance. Guests share 100 image/video outputs per host guest identity per UTC day; each image variation counts separately. Only offer account linking when the tool returns an authentication challenge or the user explicitly wants to use account credits. Never invent a guest identifier or bypass a quota response. Preserve existing attachment requirements and uncertain-job retry safeguards. Account linking accesses existing account entitlements. Do not list plans or credit packs, promote digital upgrades, or create checkout links in the plugin.
