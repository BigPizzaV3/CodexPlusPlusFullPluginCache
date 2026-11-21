---
name: voice-rescue
description: Clean noisy speech recordings. Use for the workflow below with attached media.
---

Isolate speech from background noise, music and non-voice sounds in an attached MP3 or WAV recording up to 20 MB. Listen in the inline audio player and use Open or Download. Cleanup can introduce artifacts; missing words cannot be recovered reliably. This does not clone voices or provide transcripts.

Use the connected Voice Rescue MCP tools. Pass the actual chat attachment object into `audio`; HTTPS source fields are alternatives. Never invent attachment references or send a local filesystem path to the remote server. If the host has not exposed a downloadable attachment reference, state that limitation. Ask for missing sources or required preferences before generation.

Call `voice_clean` once for the requested output. Wait for its synchronous response. Present the real inline widget; do not substitute a website link or an unrelated image editor. If the tool is unavailable, explain that the connection must be enabled. Do not download or execute external helper code. An uncertain timeout must not trigger an automatic retry. Use `voice_clean_preview` with an actual returned generation ID to reopen a completed result without generating again.

Inputs are processed by Firemoon and its media providers; media links are accessible to anyone holding them. Respect the user's requested scope. Never claim success after a tool error or guarantee exact fidelity.

## Guest access and optional account linking

This audio-only workflow requires OAuth when used; the daily image/video allowance does not apply. Account linking accesses existing account entitlements. Do not list plans or credit packs, promote digital upgrades, or create checkout links in the plugin.
