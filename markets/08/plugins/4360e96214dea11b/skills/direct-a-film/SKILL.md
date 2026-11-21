---
name: direct-a-film
description: Use when the user wants a short film, multi-shot scene, or sequence of clips with continuous motion through FXI Studio. Teaches the stills-first, frame-chained workflow instead of generating disconnected one-off video clips.
---

Use this skill whenever the request implies more than one shot: "short film",
"scene", "sequence", "chain these shots", "continuous motion", or when a single
generate_video result would not satisfy what the user described.

1. Break the request into 2 to 8 shot descriptions before calling any generation
   tool. Confirm the shot count and the aspect ratio with the user in the first
   turn if neither is stated — do not default silently to 16:9 when the user
   describes a short vertical film, reel, or story.
2. Generate an opening still for shot 1 with `generate_image` (optionally with a
   reference image uploaded via `upload_from_url` / `upload_media_data` /
   `create_upload_url` + `confirm_upload`) to lock composition, character identity,
   and wardrobe before any video call.
3. For every shot after the first, generate a keyframe still for where the next
   shot should end, using the previous still as the reference image. Pass
   continuity details explicitly in the prompt (costume, armor, hair, framing) —
   do not let the video model invent or change them.
4. Call `frame_chain` with each scene's `target_frame_uri` set to the matching
   keyframe still, or `compose_scene` when the user wants a scene built from their
   saved characters (look them up first with `list_characters`).
5. Poll `get_task` until the task finishes, then show the result inline. Do not
   report success before the task is actually complete.
6. If continuity drifts between shots (face, costume, or environment changes
   without being asked for), say so plainly and offer to regenerate the keyframe
   that drifted rather than presenting a broken chain as finished.

Do not skip straight to a multi-shot `frame_chain` without keyframe stills when
the user needs a specific character, costume, or environment to stay consistent
across shots — unkeyframed chains are the most common cause of identity and
costume drift.
