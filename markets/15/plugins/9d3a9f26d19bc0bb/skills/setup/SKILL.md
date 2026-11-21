---
name: setup
description: Prepare or diagnose Wandeo's local video, browser and offline transcription tools on macOS or Windows.
---

CLI file references are relative to the explicit `--project` directory. Resolve returned video, frame, screenshot, subtitle and workspace paths against that directory before reading files or passing them as `--input`; do not resolve them against the plugin directory. `[external file]` means the original input is outside the project; use the input path already supplied for that task. Normal results omit raw media tags, account/cache paths, process details and environment variables. Read only the source content and diagnostics needed for the user’s task.

Resolve the plugin root from this skill's directory. Run the bundled `scripts/wandeo.sh` on macOS or `scripts/wandeo.ps1` on Windows; these bootstrap Node when necessary. All CLI examples below use that launcher as `wandeo`.

Run `wandeo setup`, then read its JSON result. It downloads pinned render packages, FFmpeg, FFprobe, Chromium and Chinese fonts into a writable cache and checks the native binaries and browser. Use `--cache <directory>` only when a task needs a different writable cache; use the same cache for subsequent commands. The installed plugin directory is not a work directory.

For transcription preparation use `wandeo setup --with-asr`; otherwise the first `media transcribe` downloads the pinned Whisper model. These are local CPU operations and do not require an API key.

On failure, read the actual diagnostics. Retry interrupted downloads or run setup to repair an invalid cache. `wandeo doctor` verifies the cached programs. A host sandbox denial when starting Chromium requires the host's normal execution approval; do not disable browser sandboxing or claim that downloading a browser proves it can launch.

Use `wandeo --help` for commands. Confirm a writable project location, initialize it with `project init --project <directory>`, and continue with the capture or editing skill as appropriate. Keep the user's selected OS, output location and task constraints.
