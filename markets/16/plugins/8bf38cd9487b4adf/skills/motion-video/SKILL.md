---
name: motion-video
description: Create or revise private AI videos with Motion when a user asks for a launch video, explainer, product demo, promo, ad, motion graphic, social clip, or another finished video.
---

# Motion Video

Use Motion when the user wants a finished video created or an existing Motion video revised.

## Create a video

Call `create_video` with a concise creative brief. Preserve the user's goal, source material, audience, tone, required facts, format, duration, and aspect ratio. Let Motion make production decisions unless the user supplied exact copy or a specific visual requirement.

Motion runs asynchronously. Use the returned widget to show progress and the playable final render. Use `get_session_status` or `job_status` only when the user asks for an update or the widget is unavailable.

## Revise a video

Call `create_followup` for changes to an existing Motion result. Keep the request focused on the requested changes and preserve the existing video's context.

The first generation made through this ChatGPT plugin and its first follow-up are sponsored. Later work uses the authenticated Motion account's existing entitlements. If Motion reports that the account lacks an entitlement, explain that the job is paused; do not offer or initiate an in-ChatGPT purchase.

## Boundaries

- Do not claim a video is finished until Motion reports completion and returns the playable result.
- Do not replace a video request with animation code or a text-only storyboard.
- Do not expose private job identifiers, credentials, or internal implementation details unless needed for the user's requested status check.
- Do not invoke billing, subscription, credit-purchase, upload, or account-administration tools; they are not part of this plugin.
