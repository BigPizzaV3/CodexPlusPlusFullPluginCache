# Host-owned visualization

Use ChatGPT's image capabilities when available. Cladwell never generates a plugin
try-on, queues a generation job, consumes inference credits or saves the chat result.
Do not fall back to its native provider when host generation is unavailable.

A person can supply a photo directly in ChatGPT and request a visualization using
available clothing references. Do not require uploading it into Cladwell. The
special Cladwell reference package below is for a saved Cladwell body photo.

For an explicit request to use a saved photo, `get_try_on_photos` returns actual
photo choices under separate photo-sharing permission and entitlement. Let the
person select the photo; do not silently choose or load photos for ordinary advice.
Call `get_try_on_context` with that returned `photo_ref`,
`photo_selection_confirmed: true`, exact owned clothing IDs in the advertised roles
and the selected capsule. The package requires a top/bottom/shoes or dress/shoes;
optional accessories are supported. This read returns ordered actual images,
reference labels and the native prompt as optional guidance. It starts no generation.

Use those actual images with the host's image tool if reference transfer is supported.
Preserve person identity/body and the selected clothing details/layers; adapt the
presentation to the user's request. The prompt is guidance, not a requirement for a
fixed Cladwell style. Describe the result as an appearance visualization, not a fit
prediction, and claim completion only after an actual host image is returned.

MCP images being visible does not prove they can be reused by every host image tool.
If transfer or generation is unavailable, explain the missing capability and offer
the prepared prompt or a supported user-provided image route. Never invent file
handles, promise subscription-specific image availability, or say the image was
saved in Cladwell. The result stays in chat.
