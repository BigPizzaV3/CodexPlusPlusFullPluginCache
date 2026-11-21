---
name: lip-sync
description: Create a Clout lip-sync video from an owned photo or video plus uploaded speech or an approved generated voice track
---

# Lip sync

Use when speech should drive the visible face. Read [the shared workflow](../../references/creative-workflow.md) first.

1. Select the face source: a ready owned image/video from `clout_list_assets` / `clout_get_asset`, or a saved character from `clout_list_influencers` / `clout_get_influencer`. Confirm that the user has rights to use the likeness. Do not infer consent from a filename.
2. Ask for the intended script or audio if missing. For uploaded speech, use the shared upload/finalize flow and wait for verified audio metadata. Do not pass an arbitrary public URL or an unprocessed attachment as the audio source.
3. For generated speech, search `clout_list_voices`, choose a returned voice ID with the user, and preserve the approved script. Estimate `clout_generate_speech` if needed, generate using existing credits and a UUID request ID, and poll `clout_get_asset` until the audio is ready.
4. Read the actual audio duration and source dimensions. Call `clout_list_models` with `mediaType: "lipsync"`; choose a returned model that supports the face type, audio length, and requested format. Do not assume that every model supports both photos and videos.
5. Build the exact `clout_generate_media` input with the ready face and audio URIs plus ownership references. Use existing credits for this requested stage and respect the total budget, if specified.
6. Call `clout_generate_media` using existing credits and a new UUID for this stage. Poll `clout_get_generation`; do not create a second clip while the first remains pending.
7. Deliver the completed owned clip through `clout_get_download`. When preview is available, check lip timing, speaker identity, intelligibility, and the full approved line. Describe defects honestly and quote any requested retry separately.

A generated speech asset is not yet a lip-sync result. Keep the two stages and their generation stages clear. Never clone a real person's voice or imply an endorsement without a supported and authorized workflow.

Follow the shared direct-generation policy: no extra credit-approval step. Immediately show the returned Clout job with `clout_show_generation`; never substitute native ChatGPT image generation or another provider.
