---
name: whispertranscript-help
description: Help users open WhisperTranscript's transcription or subtitle widget, review their recent recordings and results, and understand upload, account, and sharing boundaries.
---

# WhisperTranscript help

Use the connected WhisperTranscript MCP tools for the user's recording workflow. Keep answers in the user's language and describe only actions and results that the tools or widget actually completed.

## Start a recording workflow

- For a new transcript, call `transcribe`. For timed captions, call `subtitle-generator`.
- These tools open the widget. They do not upload media or create a job. After a successful open, reply briefly and tell the user to select or drag the audio or video file inside the widget. Do not add a website link or a hypothetical fallback paragraph to that reply.
- Files attached to the ChatGPT conversation are not imported by this plugin. The user selects media inside the widget.
- The widget handles upload, job creation, and progress polling. Do not call `get-upload-url` or `insert-transcription-record` on the assistant's behalf for a normal widget upload.
- A visible widget proves only that the workspace opened. Do not claim a recording was uploaded, processed, or transcribed until the widget or a result tool reports it.

## Read and manage existing work

- Use `get-filelist` to show the connected user's recent recording jobs. It does not inspect the user's computer or another account.
- Use `get-transcription-result` only with a known `fileId`, such as the exact id the user selected from `get-filelist`. Present the returned status and content faithfully; preserve returned subtitle timings when the user asks about captions.
- Use `share-transcription` only when the user asks to share a selected completed result. The returned link gives anyone holding it read access to the shared transcript or subtitles. Do not claim it grants audio playback or download.
- Before `delete-transcription`, identify the exact selected record and obtain explicit confirmation. `deleteAll` affects every current record and requires a separately clear request and confirmation.
- `get-user-preferences` and `set-user-preferences` concern the widget's saved language and coarse access state; they are not billing or account-management tools.

## Answer common questions

- Transcription and subtitle availability depend on a connected account, available access, and processing completion. Treat a pending or failed job as such.
- Speaker labels, summaries, and timed cues should be described as available only when returned for the particular recording.
- For plain text already pasted into chat, edit, summarize, translate, or reformat it directly; do not open a recording widget merely because the text mentions transcription.
- If the user reports that the widget itself did not render, first acknowledge that actual failure and help them retry or diagnose it. Do not preemptively add recovery links to a successful widget-opening reply.
