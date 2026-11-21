# Demo video validation — 2026-10-19

Source: user-uploaded `mc plugin video.mp4` (97.1 seconds, approximately 90 MB). The video was inspected through extracted frames.

Observed: ChatGPT a&o Hostels app; Florence accommodation search; a property result and subsequent availability results; private room offer; booking confirmation/details panel; a&o external checkout form for guest and payment details.

Scope: This is visual evidence of the end-user flow, not MCP tools/list evidence or independently executed API tests. Do not assert a reservation was completed or payment made.

Submission blocker: video has no verified persistent reviewer-accessible HTTPS URL. Upload to an unlisted/publicly viewable host and verify playback, then add `extensions.com.openai.review.demo_recording_url` to plugin.json and rebuild the ZIP. The local video file is intentionally excluded from the plugin archive.

Public video URL supplied: https://youtu.be/LgKKHOK4O4o
Public playback verification: BLOCKED (web retrieval cache miss). Local uploaded MP4 was inspected previously.
