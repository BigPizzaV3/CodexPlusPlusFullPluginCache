---
name: mozonic-upload-a-song
description: Use whenever the user wants to get a local song, mix, track, or audio file into Mozonic from ChatGPT or Codex.
---

# Upload a song to Mozonic

This directory plugin intentionally cannot upload audio bytes or generate S3
presigned URLs. Do not ask for a file path, base64 payload, or file metadata.

Tell the user to upload the audio in the Mozonic app at
https://app.mozonic.com. Once it appears in their library, use
`mozonic_list_mixes` to find it and continue with analysis, correction, or
mastering. For a standalone mastering upload, the same rule applies: upload in
the Mozonic app, then use `mozonic_list_mastering_sessions`.

Requires a Mozonic Pro account.
