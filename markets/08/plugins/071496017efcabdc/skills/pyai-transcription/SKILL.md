---
name: pyai-transcription
description: "Turn supplied audio recordings into text with PyAI Hear speech-to-text (STT), including asynchronous transcription workflows."
---

# Transcription

Use the connected PyAI tool schemas as the source of truth; clients may prefix tool IDs with the server name. If PyAI is disconnected, direct the user to the host's browser sign-in. Keep credentials out of chat. Respect the selected project and the user's authorized task.

Tools: `whoami`, `transcribe_audio`, `create_transcription_job`, `get_transcription_job`, `list_transcription_jobs`

For a short supplied recording, use `transcribe_audio` with base64 audio (up to 8 MiB decoded). For a larger recording already available at an authorized HTTPS URL, use `create_transcription_job`. Inspect current schemas for diarization, language and other options; never promise an option absent from the contract.

Preserve the returned `job_id`. Poll `get_transcription_job` at a reasonable interval until completion, an error, or the task's waiting limit. Pending is not failure. If waiting ends, return the actual ID and status so work can resume; do not resubmit the recording.

Return the transcript and any speaker/timestamp data actually supplied. For microphone streaming, use the Hear streaming API or SDK described in https://docs.pyai.com; an MCP transcription job is not a live audio stream.
