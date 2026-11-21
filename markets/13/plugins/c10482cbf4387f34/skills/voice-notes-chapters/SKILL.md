---
name: voice-notes-chapters
description: Read the transcripts of a Voxbind voice memoir, group one person's voice notes into titled, dated chapters in their own words, fix a misheard word, leave a note out, and set the memoir's title. Use when the user wants to edit, organise or title the chapters of a memoir made from voice messages, or check what was transcribed.
---

Use this skill when a voice memoir already has transcribed notes and the user wants to shape the memoir. The user's explicit instructions always come first.

## Flow

1. get_memoir shows the memoir, how far transcription has got and the current chapters.
2. read_transcripts returns what the person said, up to 40 notes per call, with each note's date.
3. set_chapters titles and groups the notes from the transcripts. Keep the person's own words; chapter titles come from what they talked about.
4. edit_notes fixes a misheard word in a transcript or leaves a note out of the memoir. The original recording is kept and still plays on its listening page.
5. update_memoir changes the title, subtitle or the person's name.

## Scope

- Transcripts are the person's words as spoken; corrections fix mishearings, they do not rewrite.
- One person's voice per memoir. If the user has no memoir yet, start with the voice-memoir skill.
