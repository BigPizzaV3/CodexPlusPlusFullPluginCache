---
name: beeblio-multimedia
description: Analyze saved images, transcribe saved audio, or extract audio from saved video in a Beeblio project through MCP. Use for image questions, transcripts, subtitles, or video audio extraction.
---

# Beeblio multimedia workflow

Resolve the project with `list_projects` and the saved media path with `list_files` or `search_files`. Use `stat_file` to check the source before processing. These tools operate on saved project files, not unsaved editor content or a live camera or microphone. Vision and transcription can send the saved media to Beeblio's configured AI providers and use account credits; follow the user's scope and the host's confirmation requirements for sensitive media.

## Images

Call `analyze_image` with a focused prompt and a saved JPEG, PNG, WebP, or GIF path. The tool accepts images up to 20 MB. Distinguish what the result observes from inferences, and do not claim to have inspected pixels beyond the returned analysis.

## Audio and transcripts

Call `transcribe_audio` on a saved audio file no larger than 25 MB. Choose a new `.txt`, `.md`, `.srt`, or `.vtt` output path under `2-Data/derived/`, `3-Analysis/`, or `4-Reports/`. Set `diarize` according to whether speaker labels are useful, supply `language` when known, and use a unique `idempotencyKey` so retries do not duplicate charges or overwrite files. Confirm the returned transcript and output path with `read_text_file` or `stat_file`. Preserve uncertainty in names and technical terms; correct them only against independent evidence.

## Video audio extraction

Call `extract_audio` with a saved video path, a new `.mp3` output path in a generated-output directory, and a unique `idempotencyKey`. It queues a credit-metered compute job. Poll `get_analysis_job` using the returned job ID until `succeeded`, `failed`, or `cancelled`. Only report the MP3 after `stat_file` confirms it exists. If the user wants transcription, call `transcribe_audio` on that saved MP3 as a separate step.

Report the source and output paths, actual job status, and any provider or format limitation. Do not present generated or model-derived content as a verbatim record without checking it.
