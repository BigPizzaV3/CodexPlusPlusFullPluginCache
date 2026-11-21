---
name: listen-to-an-article
description: Use when someone asks to hear a public webpage or replay an article recording in their TTSBuddy Library.
---

For a new recording, use `tts_convert_webpage_to_listen_link` with the supplied public URL and requested narration language. Set `confirm=true` only when the user has asked to create audio. Use one unique idempotency key for that request and reuse it on retries. Fetching or replaying an existing recording must never spend narration minutes.

For replay, use the existing player when it is already present in chat. In a fresh chat, look up the exact source URL and language with `confirm=false`. If no playable match is found, explain that result and let the user decide whether to create one.

The article player can show progress and poll for readiness. Present one player. When it is ready, the user can press Play or choose Copy share link. A person with that link can listen while it remains active. The account owner can also sign in to the iPhone Library to hear the recording.
