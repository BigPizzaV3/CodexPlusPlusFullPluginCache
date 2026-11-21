---
name: outfit-preview
description: Virtual try-on for clothes on your photo. Use for fashion and outfit previews with attached person and garment photos.
---

Preview an attached garment on an attached person photo. Compare the original and result inline with fullscreen, Open and Download. This is a visual concept; it cannot determine body measurements, sizing or fit.

Use the connected Outfit Preview MCP tools. Pass the actual chat attachment object into `person`, `garment`; HTTPS source fields are alternatives. Never invent attachment references or send a local filesystem path to the remote server. If the host has not exposed a downloadable attachment reference, state that limitation. Ask for missing sources or required preferences before generation.

For chat attachments, first call `outfit_prepare_person` with the person photo. Call `outfit_prepare_garment` separately with the garment photo. Pass the real returned `person_url` and `garment_url` to `outfit_try_on`. Each preparation call handles one attachment; the generation call uses the prepared URLs. The preparation step stores the source and does not generate an outfit. Call `outfit_try_on` once for the requested output. Wait for its synchronous response. Present the real inline widget; do not substitute a website link or an unrelated image editor. If the tool is unavailable, explain that the connection must be enabled. Do not download or execute external helper code. An uncertain timeout must not trigger an automatic retry. Use `outfit_try_on_preview` with an actual returned generation ID to reopen a completed result without generating again.

Inputs are processed by Firemoon and its media providers; media links are accessible to anyone holding them. Respect the user's requested scope. Never claim success after a tool error or guarantee exact fidelity.
