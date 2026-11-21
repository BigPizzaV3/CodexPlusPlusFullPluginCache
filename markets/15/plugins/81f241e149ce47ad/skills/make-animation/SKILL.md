---
name: make-animation
description: Make a 3D character animation with NoCapMocap from a described movement. Choose Roblox R15 or Humanoid, then preview, compare and download the versions. Use for dances, emotes, walks, runs, idles and other body movements.
---

# Make an animation

NoCapMocap makes animations from text. Each new animation costs credits. Previews, version comparisons and downloads cost no credits.

1. Choose Roblox or Humanoid from the request and context. Ask only if the answer changes the result. R6 is not supported for now. Offer R15 instead. Keep the user's movement details, direction, speed and order. Use `get_capabilities` for the options and `get_account` for credits and allowance.
2. Follow the prompt guidance in `quote_animation`. Start with "A person …" and describe physical movement in English.
3. Call `quote_animation`. Show the movement, character type, length, number of versions and exact credit cost. Wait for clear approval. Quote again if the input changes.
4. Call `generate_animation` with that input, a new UUID `requestId`, and `maxCredits` equal to the quoted `creditCost`. Keep the returned `jobId`. For `retry: "same_request_id"`, retry with the same ID and input. For `retry: "new_request_id"`, explain the cause and use a new ID only after the cause is resolved. Never offer to buy credits in the chat. The user manages credits and connection allowances on NoCapMocap.
5. In hosts that show apps, call `open_animation_preview` right after `generate_animation`. Otherwise, poll `get_generation` after each `nextPollAfterSeconds`. Stop at `readyForDownload`, `failed`, or `deliveryUnavailableReason`. After an interruption, continue with the same `jobId` without a new generation. Number versions from 1: `variationIndex` 0 is version 1.
6. For a download without the preview, call `get_animation_asset` for the chosen version and a format from its manifest. Download the URL without an Authorization header before `expiresAt`. Save the returned filename. Never share or log the URL. Get a new link if it expires.

For Roblox, download `roblox_r15_base64`, the Studio import text file, first. Tell the user to paste the whole file into RBXMonkey in Roblox Studio. They can also import any version from Motion Lab History with the same NoCapMocap account. Download `roblox_r15_fbx` only when asked. For Humanoid, choose `standard_fbx` or `mixamo_fbx` from the manifest.

For an optional Studio import, use `studioImport.requestLuau`, then `statusLuau`, through the Roblox Studio MCP's `execute_luau`. Set `UPLOAD = true` only when the user asks to publish to their Roblox account. The result includes the Animation ID. If they specify game playback, set `PLAY`. The user still clicks **Set it up** in Motion Lab.

Generated animations are not locked to one spot, but a character move must stay in one spot. Send the user to the editor for that. **Find a loop** there makes a cycle, such as an idle, a walk or a run, and **Bake loop** keeps it in one spot. For a walk and run, tell the user to use **Walk and run** on both in the editor.

Call the model Surge. If a tool returns `REGION_UNAVAILABLE` or `deliveryUnavailableReason`, tell the user that message and stop. Tell them when `get_generation.expiresAt` removes the job from History and Motion Lab. They can save a version to their Library to keep it.

The MCP never edits an animation. It cannot cancel or delete an active generation. Library tools, video to motion, checkout and other skeletons are unavailable here. Never ask for a password, token or API key. The user connects through NoCapMocap's sign-in page.
