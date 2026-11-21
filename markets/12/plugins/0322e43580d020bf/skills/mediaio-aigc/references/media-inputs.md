# Source media

Use media belonging to the authorized user's Media.io space. `list_assets` returns `file_id`; `asset_id` is bookkeeping and cannot be substituted. For a previous result, resolve its `outputs[].asset_id` with the asset query to obtain its file ID.

| Operation | Model-specific sources in `request.inputs` |
| --- | --- |
| `image_to_image` | Image file(s), and a mask only when declared |
| `image_to_video` | Starting image and an ending image when declared/required |
| `reference_to_video` | Explicit image, video, audio or document fields; satisfy the declared required alternatives |
| `motion_control` | `reference_image_file_id` and `video_file_id`; optional audio only as declared |
| `image_audio_to_video` | `image_file_id` and `audio_file_id` |

Field names and counts differ by model. For example, GPT Image 2 editing uses `image_file_ids` (1–3), Wan 3.0 uses `reference_image_file_ids`, `reference_video_file_ids` or `reference_audio_file_ids`, and Vidu 2.0 uses separately named image references. Never send one model's fields to another model. Source metadata and cross-frame compatibility are validated by the upstream service, not inferred from opaque file IDs.

Only opaque file IDs are accepted. Never pass public URLs, storage paths, attachment handles, another account's media or invented IDs. Respect the model-specific size, dimensions, aspect ratio and file-type requirements in the current field descriptions; unsupported media requires new input from the user, not hidden conversion operations.

## Conditional local upload

Proceed only if the host can actually read the bytes, hash them and perform HTTP PUT:

1. Determine file name and exact byte size. Compute SHA-1 of the whole file (`content_hash`) and the first 1 MiB (`pre_hash`); for smaller files they are equal.
2. Call `create_upload`. If `state: "completed"` and `rapid_upload: true`, use its `file_id` directly.
3. Otherwise PUT the raw bytes to `upload_url` using exactly `upload_method` and `upload_headers`. Do not edit the signed URL or include unrelated authorization.
4. After a successful PUT, call `complete_upload` with the ticket ID and use its `file_id`.

Do not manufacture hashes, pass bytes through the MCP tools or treat a ChatGPT attachment alone as a completed upload. If the required host capabilities are absent, explain that a suitable file already in the user's Media.io drive is needed. Do not promise every host can upload.
