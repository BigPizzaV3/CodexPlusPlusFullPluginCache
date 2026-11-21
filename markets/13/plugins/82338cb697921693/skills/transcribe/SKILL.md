---
name: recordd-transcribe
description: Use Recordd to turn an audio or video recording into a speaker-labeled transcript, then help with it.
---

# Transcribing with Recordd

- If the user attached an audio or video file and wants to know what's in it, call `transcribe_audio` with the file.
- If they gave a direct link to an audio or video file, call `transcribe_audio` with `audio_url`.
- If they want a transcript but haven't attached anything, call `transcribe_audio` with no file: it shows an upload box where they pick the file.
- Recordd can't transcribe YouTube or other streaming-site links; don't call it for them.
- Pass `language` only when the user names the spoken language; otherwise it's detected.

The transcript appears in the Recordd card, so don't paste it back. Answer in the user's language: say what the recording is about in a sentence or two, then offer a summary, action items, a translation, or answers to their questions.
