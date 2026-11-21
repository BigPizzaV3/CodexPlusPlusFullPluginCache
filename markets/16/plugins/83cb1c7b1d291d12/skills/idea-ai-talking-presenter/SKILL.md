---
name: idea-ai-talking-presenter
description: "Create a talking presenter video with idea.ai by combining an approved portrait, script, selected voice, and generated narration."
---

# Talking presenter

Read [the shared MCP workflow](../../references/mcp-workflow.md) before calling tools. It defines discovery, file handling, cost authorization, waiting, and delivery for this skill.

## MCP operation

Use `create_audio` for approved narration and `create_video` for the presenter. Reuse the generated narration URL and upload the portrait through the free upload flow when needed.

## Prepare the presenter and script

Use the user's approved portrait and intended script. Establish language, voice preferences, delivery, target duration, and video format. Preserve names, numbers, and factual claims; get user wording for unresolved claims rather than inventing endorsements.

If the user already supplies suitable narration, reuse it instead of generating replacement audio. Otherwise inspect a speech model such as ElevenLabs v3 (`eleven_v3`). Its `inputs` contain text and a `voice.voice_id`; obtain that ID from the model's actual `voiceCatalog` through `list_voices`.

Use voice facets to help resolve unspecified preferences, then show a small relevant selection. Never invent voice IDs or reuse an ID from a different catalogue. Price the narration and presenter generation as separate paid actions.

## Generate narration, then the presenter

Review or obtain approval for narration when pronunciation and delivery matter before spending on video. Preserve the accepted audio output URL.

Inspect HeyGen Avatar 5 (`heygen_avatar_5`) or another suitable available model. Its inspected contract requires `sourceImage` and `sourceAudio`; the audio limit is 1–120 seconds. Use actual aspect-ratio and resolution options, and check that the portrait and narration meet current file constraints.

## Review and deliver

Assess spoken wording, pronunciation, pacing, lip synchronization, face stability, framing, and duration. Mark aspects that cannot be played or inspected as unverified. Correct audio issues before rebuilding an otherwise acceptable video.

Deliver the presenter video, approved script, and narration asset where useful. Do not promise a reusable trained avatar, voice cloning, or scene editing unless the chosen tool explicitly supports it and the user requested it.
