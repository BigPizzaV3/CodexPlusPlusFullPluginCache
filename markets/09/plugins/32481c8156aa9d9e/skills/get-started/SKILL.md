---
name: get-started
description: Guide ChatGPT on discovering highlights, analyzing audiovisual dynamics, and trimming media clips using the KEEP API.
---

# KEEP Media Highlights AI Skill

This skill enables ChatGPT to interact with the **KEEP Media Processing Engine** (`https://api.skeepit.co`) to analyze media files, detect potential highlight timestamps, inspect acoustic and visual waveforms, and assemble selected intervals into clips.

## Core Capabilities

1. **Highlight Detection (`discover_highlights`)**:
   - Analyzes video or audio media files.
   - Computes audiovisual activity curves (optical motion and acoustic energy).
   - Generates 96-bin waveform samples with activity scores.
   - Returns suggested segment intervals `[[start, end], ...]`.

2. **Media Clipping (`condense_media`)**:
   - Trims and stitches specified time intervals into a single output media stream.
   - Supports MP4, WebM, MP3, and WAV container formats.

## Recommended Workflow

1. **When a user shares a video or audio URL**:
   - Invoke `discover_highlights(media_url)` to compute duration and suggested highlight intervals.
   - Present a clear summary of detected segments with timestamps (e.g. `00:00 - 01:15`, `04:30 - 05:45`).

2. **When a user asks to trim or condense the media**:
   - Propose or confirm the intervals to preserve.
   - Invoke `condense_media(media_url, segments)` with the selected `[[start, end], ...]` array.
   - Provide the resulting clip information to the user.

3. **Safety & Boundaries**:
   - KEEP processes media streams provided by the user.
   - Out-of-bounds timestamps (beyond media duration) will return an error response.
