---
name: heygen-workflows
description: Use HeyGen for talking-avatar videos, general AI clips with HeyGen Video 1, and video, avatar, voice, translation and media workflows.
---

Use the connected server's available tools and current schemas. Never claim a capability that the connection does not expose.

## Choose the video workflow

For an ambiguous request such as "create a HeyGen video", ask once: "Would you like an avatar video, best for an avatar speaking your script, or a general AI video using HeyGen Video 1, our own AI video model?" Ask before avatar setup or generation. Skip this question when the request or conversation already makes the type clear.

For a general AI scene or a named HeyGen Video 1 request, use text_to_video, image_to_video for a first-frame image, or reference_to_video for visual/audio references. Do not require avatar setup or an avatar showcase. Follow the returned schema for supported durations, resolutions and aspect ratios; 2k text/reference generation requires 16:9 or 9:16. Image-to-video follows the image's proportions.

For a talking-avatar request without a selected avatar, use prepare_avatar_video when available and follow its guidance. Preserve the supplied topic or script and respect explicit declines of digital-twin setup. With a confirmed avatar look and exact script/audio, use create_video_from_avatar, preserving words and look. Use Video Agent for explicit Video Agent requests or polished multi-scene production according to its tool description; do not substitute it for a clear model-clip request.

## Show results and follow progress

On a widget-capable host where show_video is available, after text_to_video, image_to_video, reference_to_video or direct avatar creation returns a video ID, call show_video once in the same turn, including while pending. Do not ask whether to show the result. The player receives completion/failure updates and performs recovery reads. Do not poll get_model_video from the conversation merely to wait; use it for an explicit model-status/details request.

For an existing video ID, including a library result, first call get_video. Open show_video only after successful lookup with status other than failed and when the user wants to watch or track it. Library browsing alone should use list_videos without automatically playing a result.

On direct clients without widgets, poll get_model_video for model clips, get_video for avatar videos and completed Video Agent output, and get_video_agent_session for ongoing Video Agent work. Honor returned retry delays; otherwise wait 30 seconds. After five minutes return actual status and available links for later follow-up. Never repeat creation to check progress. Stop on failed/cancelled and explain the returned failure without regenerating unless asked.

## Assets, voices and account actions

Reuse conversation attachments through import_asset_from_chat when supported. Otherwise use a verified HeyGen asset reference or the available upload workflow: create_asset_upload, transfer bytes, then complete_asset_upload. Do not claim an upload completed without that confirmation, or assume a direct client can transfer bytes.

For avatars, browse list_avatars when available or list_avatar_groups then list_avatar_looks on direct clients. Browsing or selection does not authorize generation. For user-selected voices, use choose_voice when available; for delegated voice choice, use list_voices and create speech once with the exact agreed text and a compatible returned voice. Do not invent IDs or generate auditions unasked.

Discover translation languages before starting a requested translation. A language question does not authorize generation. Follow recording, consent and authentication handoffs. Keep account actions within the user's request and explicit confirmation requirements. For an uncertain write outcome, check status before retrying. Retry a retryable read at most once after the returned delay. Explain entitlement and renewal facts without inventing reset schedules, promoting upgrades, or initiating purchases.

## Reusable templates

Use list_templates and get_template to inspect existing templates and generate_from_template for a requested video using verified variables. For explicit template-authoring requests, use create_template with a verified user video that has a supported current-editor draft. Inspect the returned composition or get_template before binding variables; never invent element IDs. Use set_template_variables with the complete desired variable set, including every variable to keep. Text matches are exact and case-sensitive. Prefer the current edit_version as expected_edit_version and reconcile a stale-version conflict before retrying. Use update_template to rename and delete_template only when the user requests removal. Template authoring or browsing alone does not authorize video generation.
