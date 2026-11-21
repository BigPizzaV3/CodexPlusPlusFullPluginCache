# Muesli CLI contract

This is a guide to the CLI shipped with Muesli. Run `muesli-cli spec` to see the command tree and model names supported by the installed version.

## Commands

```text
muesli-cli spec
muesli-cli info [--db-path <path>] [--support-dir <dir>]
muesli-cli transcribe <file> [--format text|json|markdown] [--model <model>] [--dictionary <path>] [--summarize] [--save-meeting] [--title <title>] [--output <path>]
muesli-cli meetings list [--limit <n>] [--folder-id <id>]
muesli-cli meetings get <id>
muesli-cli meetings update-notes <id> (--stdin | --file <path>)
muesli-cli dictations list [--limit <n>]
muesli-cli dictations get <id>
```

Examples:

```bash
muesli-cli transcribe interview.m4a --format json
muesli-cli meetings list --limit 10
muesli-cli meetings get 42
muesli-cli dictations get 7
cat notes.md | muesli-cli meetings update-notes 42 --stdin
```

Data commands use a JSON envelope with `ok`, `command`, `data`, and `meta`. Failures set `ok: false` and include `error.code`, `error.message`, and often `error.fix`. `transcribe` returns transcript text by default; its JSON result can include `transcript`, `summary`, `durationSeconds`, `wordCount`, `model`, `warnings`, `savedMeetingID`, and `title`.

Meeting list rows include `id`, `title`, `startTime`, `durationSeconds`, `wordCount`, `folderID`, and `notesState`. A full meeting includes `rawTranscript` and `formattedNotes`. `notesState` is `missing`, `raw_transcript_fallback`, or `structured_notes`. Dictation details include `rawText`, `appContext`, `timestamp`, and `durationSeconds`.

`--summarize` uses the summary backend configured in Muesli and may return a warning while preserving the transcript if summarization fails. Local agent analysis of a returned transcript does not require a separate Muesli summary backend. `--save-meeting` stores an imported audio file as a meeting. `--output <path>` writes the selected output format to a file.
