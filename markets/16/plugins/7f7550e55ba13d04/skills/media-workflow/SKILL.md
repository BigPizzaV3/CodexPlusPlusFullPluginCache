---
name: media-workflow
description: Transcribe or translate audio/video, create TTS voiceovers, or check and export results through VoxStudio Cloud remote MCP.
---

This skill uses the VoxStudio Cloud plugin and its `voxstudio_cloud` MCP server at `https://voxstudio.me/cloud/mcp`. Discover tools from that server using their live schemas, including deferred tools. In OpenAI hosts, use only tool identifiers beginning with `mcp__voxstudio_cloud__`; the separate `mcp__voxstudio__` namespace belongs to the local Mac app. Keep every Cloud request on the Cloud connection. If Cloud tools are unavailable, inspect and report the actual connection or tool exposure error. Request OAuth reconnection only when authentication is required, expired or rejected; missing tools alone do not establish an OAuth failure. Do not substitute local tools or treat local sessions as the Cloud catalog.

Use the live tool schemas and actual returned IDs. For a local file, call `mcp__voxstudio_cloud__app_transcription` with action=prepare, upload the file bytes to the returned signed upload URL with its required headers, then call `mcp__voxstudio_cloud__app_transcription` with action=complete with the returned `session_id`. If the host cannot read/upload files, ask for a supported attachment or accessible HTTPS download URL; do not pass a local path as a download URL. For HTTPS attachments, call `mcp__voxstudio_cloud__app_transcription` with action=submit with `media_file.download_url`.

Poll `mcp__voxstudio_cloud__voxstudio_session_get` using the same `session_id`. Report queued/running/failure states accurately. Do not locate a submitted job again by title or create a duplicate because processing is still running. Leave language automatic unless the user specifies a language or the schema requires one.

For TTS, inspect `mcp__voxstudio_cloud__voxstudio_dub_reference_list` and select a real compatible reference. Call `mcp__voxstudio_cloud__app_dubbing` using the user's text or the agreed evidence-grounded script, then inspect `mcp__voxstudio_cloud__voxstudio_dub_result`. Do not invent reference IDs, language values, success states or download URLs.

Use the returned Cloud preview and export tools to obtain finished outputs. A submitted job is not a finished result. Cloud supports only knowledge, ASR and TTS; native editing connects separately through voxstudio_native. Poll the actual job/result before claiming completion. Keep original citations when converting extracted knowledge into speech.
