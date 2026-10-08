---
name: birdie-recordings
description: Investigate customer bug reports from Birdie screen recordings. Use when given a Birdie link, recording id, or short code, or when asked what a customer saw, what broke, or why a request failed during a reported session.
---

# Debugging with Birdie recordings

Birdie recordings carry the evidence from a real customer session: console
logs, network requests, user steps, a transcript, and video frames.

Recording identifiers come in several shapes — a numeric id (`631060`), a UUID,
a short code (`w3uqNNG`), or a full share URL. All of them work; pass whatever
the user gave you.

## Which tool to reach for

Start narrow. Only use `get_recording_diagnostics` when the question is broad
("what went wrong here?") — it pulls every signal at once and is expensive.

| Question | Tool |
| --- | --- |
| Which recording is this? | `list_recordings` (by ticket, email, text, date) |
| Browser, OS, URL, who recorded it | `get_metadata` |
| JavaScript errors | `get_console_logs` — filter `log_level: error` |
| Failed API calls | `get_network_requests` — `status_code: 5xx`, `host`, `content_type` |
| What the user did | `get_repro_steps` |
| How to reproduce a bug | `get_repro_steps` with `detail: full` |
| What the user said | `get_video_transcript` |
| Where the activity is | `get_recording_scenes` (cheap, no images) |
| What was on screen | `get_recording_frames` — **run scenes first**, then pass a `time_range` |
| Broad diagnosis | `get_recording_diagnostics` |

## Reporting findings

Use recording-relative timecodes (`01:20.132`), not UTC timestamps, when
explaining what happened. "The checkout call 500s at 01:20" is useful; an epoch
millisecond value is not.

## Mapping evidence to this codebase

<!-- EDIT THESE THREE LINES FOR YOUR PROJECT -->
- Frontend source lives in: `src/`
- Backend/API source lives in: `app/`
- API routes are defined in: `routes/`

When you find a failing request, resolve its path to the handler in the backend
directory above before proposing a fix. When you find a console stack trace,
resolve the file to the frontend directory above. Read the actual source before
suggesting a change — the recording tells you *what* broke, not *why*.

## Workflow that usually works

1. Resolve the recording (`list_recordings` if you only have a ticket number).
2. `get_recording_diagnostics` for the overall picture.
3. Narrow with the specific tool for whatever looked wrong.
4. `get_recording_scenes` → `get_recording_frames` if you need to see the UI.
5. Open the relevant source files and propose a concrete fix.

Do not guess at causes from the transcript alone — confirm against console or
network evidence before claiming a root cause.
