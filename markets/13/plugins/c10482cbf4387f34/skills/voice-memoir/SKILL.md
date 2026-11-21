---
name: voice-memoir
description: Make a memoir from one person's voice messages (a WhatsApp chat export or audio files), with transcripts in dated chapters and listening pages that play their voice. Use when the user wants to keep or transcribe a parent's, grandparent's or loved one's voice messages, or turn them into a memoir.
---

Voxbind keeps one person's voice notes under the user's ChatGPT account and turns them into a memoir: dated chapters with transcripts, listening pages that play the original recordings, and a download of the recordings. The user's explicit instructions always come first.

## Flow

1. show_sample_memoir shows a finished sample (a made-up grandmother whose voice is synthetic) when the user wants to see what Voxbind makes or hasn't exported anything yet.
2. import_voice_notes reads an attached WhatsApp chat export (a .zip exported with media) or audio recordings (opus, m4a, mp3, wav or ogg; up to 10 files at a time). It returns the people who sent voice notes, with their counts and dates, and the consent statement. When the attachment doesn't come through, or the export is over 512 MB, its result or create_upload_link gives a private upload page on voxbind.ambientapp.ai that takes up to 1 GB.
3. The user says whose voice to keep and confirms the consent statement in their own words. choose_speaker then keeps that person's voice notes, deletes the rest of the export and starts transcribing each note in the language it was spoken.
4. get_memoir shows progress and the chapters. For shaping the chapters, use the voice-notes-chapters skill: read_transcripts, set_chapters, edit_notes and update_memoir.

## Scope

- One person's voice per memoir, kept by the name the export shows, or the name the user gives for recordings. Voxbind keeps and plays the original recordings; it doesn't clone, imitate or identify voices.
- Up to 600 voice notes per memoir, each up to 30 minutes long.
- delete_memoir deletes a memoir's recordings, transcripts, chapters and listening pages.
- The tool results say what this user's memoir includes.
