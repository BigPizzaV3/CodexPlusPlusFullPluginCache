---
name: token-tally
description: See your lifetime tokens, busiest day, activity streak, and longest agent turn, then create a card to save or share. Works on a computer or a phone connected to one.
---

# Token Tally

Use the bundled Python helper for account retrieval and rendering. Resolve all paths relative to this skill folder. No backend, leaderboard enrollment, scheduled job, or external upload is part of this version.

## Renderer setup

Before the first export, run the helper's `doctor` to resolve Tesseract CLI 0.3.1 and fonts. Do not stop at the first mismatched installation: the helper checks all standard candidates. If missing or mismatched, follow [Token Tally setup](../token-tally-setup/SKILL.md) as part of the requested card workflow and then resume the original export. Do not add a separate conversational confirmation for routine renderer setup needed to fulfill the card request. Use normal host permission mechanisms for downloads, installation, and rendering; never bypass a denied permission. Respect explicit user restrictions. If setup is declined or blocked, retain any collected snapshot and report the specific blocker. Never claim a card was generated when it was not.

## Default: check stats and export the card

Run `python3 scripts/token_tally.py stats --output <new-absolute-output.json> --card-dir <new-absolute-card-directory> --tsrct <absolute-tsrct-path>` using this skill's absolute script path. Choose a user workspace output path. The helper uses the existing Codex sign-in without reading or exporting credentials. It only requests initialization and `account/usage/read`; it never starts a model turn.

This command automatically retrieves stats AND exports the PNG and editable card. Do not stop after reporting numbers: inspect and display the generated PNG, and provide its download link. Use `--no-card` only when the user explicitly requests numbers only or no image. If automatic rendering fails, preserve the snapshot, resolve the rendering problem, and retry the `card` command below with that snapshot; do not claim the workflow is complete.

The card presents lifetime tokens, peak daily tokens, current streak, and longest agent turn; do not repeat them in prose unless requested. A turn is one user request and the agent work that follows, not time the user spent in the app. The service does not document how approval waits, tool waits, or idle time affect this duration; do not call it uninterrupted compute time. Null means unavailable, not zero. Daily usage record count describes returned date buckets, not confirmed active days. Do not describe totals as all ordinary ChatGPT chats, verified environmental impact, or externally verified leaderboard results. Do not add cached or reasoning tokens to this already aggregated total.

If the local server needs permission to initialize its state directory, use the host's normal permission mechanism. If signed out, have the user sign in through the official app/CLI. Never request credentials in chat. Mobile and web chats can use this workflow through a connected desktop. Resolve dependencies on that execution host, not the phone. A chat without connected local execution cannot run this skill.

## Re-export a saved snapshot

For a design revision, a requested historical snapshot, or recovery after an export failure, run:

`python3 scripts/token_tally.py card --snapshot <absolute-output.json> --output-dir <new-absolute-directory> --tsrct <absolute-tsrct-path>`

The output directory must be new to preserve earlier exports. Requires Python 3.10+, Tesseract CLI 0.3.1, and a compatible signed-in Codex CLI. The helper uses installed SF Pro Display fonts when all three weights are present, otherwise bundled open-license Inter Display. No font download is needed. `--font-set bundled` forces the portable fonts; all three explicit font flags may override them. Run `doctor --tsrct <path>` to check dependencies without collecting stats. Do not redistribute proprietary font files in the plugin. Stats retrieval still works with --no-card if rendering is unavailable and the user explicitly wants numbers only. Never substitute example numbers for a failed read.

The card uses blue lifetime tokens, black secondary stats, and no daily-record count. Numeric values and snapshot dates come from the snapshot. The bottom-right record mark encodes the exact lifetime total, collection time (UTC, to the second), declared source, and a checksum. Supplied snapshots use T1S; account-tagged snapshots use T1A. The mark is an unsigned consistency record, not authentication. Missing totals produce no mark.

Open and inspect the generated PNG before delivering it. On success, finish with the PNG inline and one PNG download link, then stop. Keep the editable .tsrct export available, but link it only if the user asks for an editable file. Do not append a stats list, setup instructions, dependency details, a follow-up question, or offers to make more versions. Answer any explicit additional question the user asked. Successful generation and delivery is the stopping condition; further edits require a user request. This version has no live destination URL for "Create your card". Do not present the graphic as a functioning button or a published service.

Keep raw errors and credentials out of public artifacts. Never publish the user's card, enroll them, or create a schedule merely because they requested an export.

## Decode a card record

For requests to check, decode, or compare a Token Tally card, read the small bottom-right mark and run `python3 scripts/token_tally.py decode <mark> --tokens <visible-exact-lifetime-total>` (absolute script path). If only the abbreviated total is available, omit --tokens and compare displayTotal to the visible main number. If the mark is unreadable, ask for the original PNG or transcribed mark; never guess ambiguous characters. Report the decoded total, collection time, and whether they match the visible number. A mismatch is an inconsistency, not proof of intentional fraud. A valid checksum only checks the mark itself. Anyone can regenerate the mark; never label it signed, verified, tamper-proof, or proof of account ownership. Do not compare today's usage to a historical card.
