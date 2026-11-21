---
name: muesli-agent
description: Use when a user supplies a Muesli transcript for notes or action items, or when a macOS agent with local command access needs to inspect meetings and dictations, transcribe audio, or update notes through muesli-cli.
---

# Muesli Agent

Use the transcript the user supplies in chat, or Muesli's bundled CLI when the agent has local command access on the user's Mac. This skill does not give a cloud ChatGPT session access to files or meetings on the Mac.

## When the transcript is supplied in chat

Analyze the supplied text directly. Identify decisions, action items with owners and dates only when stated, open questions, and a concise summary. Mark uncertain or missing details rather than inventing them. Offer Markdown notes the user can copy into Muesli. Do not claim to have read a different meeting or saved notes back to the app.

If the user asks for a meeting that has not been supplied and local command access is unavailable, ask them to paste or attach its transcript from Muesli. Explain the local CLI option for a shell-capable agent if useful.

## When local CLI access is available

### Discover and check the CLI

1. Try `command -v muesli-cli`.
2. If needed, use `/Applications/Muesli.app/Contents/MacOS/muesli-cli`.
3. A `muesli` alias is acceptable only after `muesli info` confirms it is the Muesli CLI.
4. For development, use the resolver in `scripts/resolve_muesli_cli.sh` from this skill directory.
5. Run the resolved binary's `spec` command before relying on options from a packaged reference. Installed versions can differ.

Never use a similarly named command without checking its identity. When the CLI is absent, tell the user how to install or locate Muesli.

### Workflows

- For a local `.mp3`, `.mp4`, `.m4a`, or `.wav` file, run `transcribe <file>`. Use `--format json` when duration, model, warnings, or saved meeting ID matter. Use `--save-meeting` only when the user asks to store the import.
- To find a meeting, use `meetings list --limit 10`, then `meetings get <id>`. Analyze `rawTranscript` and `formattedNotes`; use the transcript when `notesState` is `missing` or `raw_transcript_fallback`.
- To inspect dictation history, use `dictations list`, then `dictations get <id>`.
- To save revised meeting notes, use `meetings update-notes <id> --stdin` or `--file <path>` only when the user asks to update them. This replaces `formattedNotes`; it does not edit `rawTranscript`.

Data commands return JSON. `transcribe` returns plain text unless `--format json` or `--format markdown` is supplied. Inspect `ok`, `data`, `error`, and `meta.warnings` rather than assuming a zero exit means useful content. Treat transcripts and local file paths as private user data; share or upload them only as requested.

Read `references/cli-contract.md` for examples and field meanings. Use the installed binary's `spec` as the authority for available options.
