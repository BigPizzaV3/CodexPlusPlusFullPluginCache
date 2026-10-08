---
name: setup
description: Set up Cirro for recording or editing demo videos. Use when a demo-videos workflow needs the bundled Cirro launcher.
---

# Set up Cirro

Cirro is a command-line tool for recording screens and windows and editing recordings
into demo videos.

Use this skill's launcher. On macOS/Linux, run
`sh "/absolute/path/to/setup/scripts/cirro.sh" <command> ...`. In Windows PowerShell,
run `& "C:\absolute\path\to\setup\scripts\cirro.cmd" <command> ...`. Pass the same Cirro
arguments on either platform.

Choose one absolute path for `DEMO_VIDEOS_CACHE` from the current task's writable paths,
in this order:

1. A shared cache root, when the sandbox allows writing it (for example,
   `$XDG_CACHE_HOME`, `~/.cache`, `~/Library/Caches`, or `%LOCALAPPDATA%`).
2. An allowed temporary root, such as `$TMPDIR`, `/tmp`, or `%TEMP%`.
3. The task's writable working directory.

Use a `demo-videos-cache` subdirectory of the chosen root. On macOS/Linux set
`export DEMO_VIDEOS_CACHE="/absolute/chosen/path/demo-videos-cache"`; in PowerShell set
`$env:DEMO_VIDEOS_CACHE = "C:\absolute\chosen\path\demo-videos-cache"`. Pass the same
value to every Cirro invocation, including new shells, changed working directories, and
tests. Do not assume an OS-default cache or temp path is writable unless the active
sandbox permits it.

The launcher downloads the pinned release from the OpenAI CDN on first use. It checks
the SHA-256 of the release's `SHA256SUMS` against the skill's pin, then checks the
selected platform archive against that manifest. It caches both files and rechecks them
before every use. If `DEMO_VIDEOS_CACHE` is unset, the launcher defaults to
`.demo-videos-cache` in the working directory. Each run extracts a fresh private copy,
keeps its libraries together, and removes it on exit. A verified cache works offline. No
Python, pip, FFmpeg installation, or Node.js is needed for editing.

Supports Ubuntu 24.04-compatible Linux x64/ARM64, macOS 14+ Apple Silicon or macOS 15+
Intel, and Windows 11 x64/ARM64. macOS/Linux need curl and unzip; Windows uses system
curl and tar. First use needs HTTPS access to `persistent.oaistatic.com`. For setup
failures, report the exact error and platform; checksum errors name the cache file to
remove before retrying. Keep TLS verification and OS security policies enabled. The
macOS and Windows binaries are signed; Linux binaries have no OS publisher signature.
The launcher verifies downloaded bytes against the manifest pin, not platform
signatures.
