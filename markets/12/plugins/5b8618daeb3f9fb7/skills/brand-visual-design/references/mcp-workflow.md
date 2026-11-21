# Designkit MCP workflow

Use the Designkit MCP tools attached to this plugin. Read their live schemas; do not substitute a similarly named domestic, pre, beta, or unrelated provider connection. These workflows use the existing global service at https://designkitmcp.designkit.com/mcp/chatgpt. Never ask users for access tokens or embed credentials in prompts.

## Materials and task handoff

`designkit_create_task` submits both image/design and video generation. Put the requested media type and creative requirements in `message`; use `designkit_get_artifacts` for actual progress and media. No separate video-generation or video-export tool is required. `designkit_get_profile` returns account identity, not a capability catalog.

- For a user-supplied public product/reference URL, preserve the actual URL in `attachments` with its correct media type, subject to the server's resource-domain validation. An existing public URL does not require a local-file upload.
- For an accessible local attachment, call `designkit_prepare_upload` with its filename and media type. Upload the actual bytes immediately to the returned upload URL as multipart field `file`, using a host-supported upload facility. Pass only the successfully uploaded resource URL in `attachments` to the design task. An upload ticket URL, a local path, or an attachment label is not an uploaded image URL.
- If this host cannot read or upload the attachment, explain the missing step and ask for a usable Designkit-uploaded resource or let the user upload in Designkit. Do not claim the photo was received by the design agent. Do not invent URLs or route around a server URL rejection.
- For each new design, call `designkit_create_task` once with a unique `idempotency_key`, a cohesive `message`, and the available attachments. State the deliverables and preserve the user's product facts, copy, language, and creative constraints in that message. Do not submit internal routing fields such as `req_model_path` or invented website skill IDs.
- Keep the returned `room_id`, `task_id`, and `room_url`. For revisions, use `designkit_update_task` in that same room with a new write key. For an uncertain network result, retry the same operation with its existing key; do not create a second paid task to check whether the first worked.

## Progress and questions

Call `designkit_get_artifacts` for the actual room. Send its returned `max_seq` as `after_seq` on the next incremental read; do not guess a cursor. Follow the returned task state and `next_action`.

- If Designkit asks a question, present it with its actual options. Use `designkit_answer_task` with the returned room/task/request/card context and the user's answer. Apply already-provided preferences when they answer the question; do not invent an option ID or ask the same question again.
- While running, report the actual phase and newly available outputs. Use spaced polling within the host's time limits. If the task outlasts the active turn, leave the real room link and state that generation is still running. Do not promise a future notification unless one was actually configured.
- If the account lacks entitlements, or a tool fails, report the real reason and recovery action. Do not buy credits, start checkout, repeatedly recreate tasks, or say a failed task succeeded.

## Deliver and refine

For actual image artifacts, use `designkit_show_images` with the real `room_id` and, when relevant, returned `source_seq`. Keep returned original-image links and the room link available. Distinguish completed, pending, and failed outputs; never fabricate an image, dimension, page count, download, or completion percentage.

Only generate an additional variation when it follows the user's request. A read-only status or preview request must not start another design. Marketing images do not require PPTX. Offer presentation export only for a relevant user request, using the available export tools and stating the returned format's actual limits.

## Bundled preset selection

These presets are local instructions packaged with the plugin, not server-side catalog entries. Read only the selected preset and its referenced guide. A preset label or slash-style alias is conversational shorthand, not a registered ChatGPT command. Use natural-language requests equally. Do not call `get_preset_instructions`, `list_workflows`, or any other lookup tool unless it is actually available; this release adds no such tool. Do not send local preset IDs as extra MCP arguments. Express the selected brief through the existing task `message` and real attachments.

Browsing the menu, asking for advice, or choosing a preset alone does not submit a design. An explicit creation or modification request can proceed with existing authorization once required inputs are available. Ask only for genuinely missing required inputs; a complete brief needs no additional planning approval.
