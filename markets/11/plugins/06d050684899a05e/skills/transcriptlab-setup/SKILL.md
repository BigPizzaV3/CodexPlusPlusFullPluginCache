---
name: transcriptlab-setup
description: Use when the user wants a YouTube transcript, a transcript of an audio or video file, caption languages, a search inside a transcript, or their TranscriptLab credits.
---

# TranscriptLab

These tools fetch YouTube captions and transcribe audio or video with speech-to-text.

## Route the request

| The user gives you | Call |
| --- | --- |
| a YouTube link or video ID | `transcriptlab_get_transcript` |
| an audio or video file attached to the chat | `transcriptlab_transcribe_file` |
| a direct link to a media file (.mp3, .mp4, and similar) | `transcriptlab_transcribe_media_url` |
| a question about which subtitle languages exist | `transcriptlab_discover_captions` |
| a phrase to find inside a transcript already delivered | `transcriptlab_search_transcript` |
| a request to reopen an earlier transcript | `transcriptlab_list_transcripts` |
| a question about their plan or credits | `transcriptlab_get_usage` |
| no link or file yet, a file over 300 MB, several links at once, or a wish to browse | `transcriptlab_open` |

`transcriptlab_get_transcript` may answer with a job id instead of text: check it with
`transcriptlab_get_job_status` and read it with `transcriptlab_retrieve_transcript` once done.
`transcriptlab_transcribe_file` and `transcriptlab_transcribe_media_url` return an id to poll with
`transcriptlab_get_speech_transcript`.

These tools belong to the launcher and uploader views. Never call them:
`transcriptlab_mentions`, `transcriptlab_begin_audio_upload`,
`transcriptlab_start_audio_transcription`, `transcriptlab_read_audio_transcript`,
`transcriptlab_submit_batch`, `transcriptlab_list_job_items`, `transcriptlab_export_link`.

## How to behave

- Answer with the transcript. Never invent text, a title, a timestamp, or a caption language. If a
  tool returns nothing, say so in one sentence and offer the next option.
- Talk about their content, not the plumbing. Do not name tools, describe the connection or the
  transcription engine, explain the views, or list what the plugin can do. Do not offer install,
  setup, or troubleshooting detail unless something has actually failed.
- Poll quietly. Wait a few seconds between checks, back off, and stop after about ten tries; then
  report that the job is still running. Do not narrate each attempt.
- Mention that a first transcript may use a credit only when it affects their choice. Otherwise stay
  quiet about it.
- Captions are not transcription. If a YouTube video has no captions, say so plainly and offer to
  transcribe the audio when they can attach the file or give a direct media link. Never imply the
  audio was transcribed when it was not.

## If something fails

- A reconnect or sign-in prompt, or an authentication error: ask them to reconnect the plugin once,
  then retry.
- Out of credits, or the monthly caption-discovery limit: state the limit and stop. Do not retry.
- A job that never finishes: give the job id and its last status instead of continuing to poll.
