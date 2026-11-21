---
name: daily-practice
description: Use when the user asks to start, open, or resume Freegama daily brain-game practice in the app.
---

# Freegama daily practice

Open https://freegama.com/play in the app's built-in browser for the user to play. The website handles today's games, game instructions, scoring, saved progress, and the finished-day screen. This skill needs no custom MCP server, credentials, or local game installation.

## Open practice

1. If an existing Freegama daily-practice tab is known, show that tab. Preserve an active game or the finished-day screen; do not reload it or navigate away to start again.
2. Otherwise, use the host's built-in browser-opening capability. When `open_in_codex` is available, use this input:

   ```json
   {"target":{"type":"browser","url":"https://freegama.com/play"}}
   ```

   To show a known tab with this tool, use `target.type: "browser"` and its returned `tabId`, without a URL. If a browser-control tool is needed instead, follow its current documentation to open a visible in-app tab and retain it for the user.
3. Check the opening result. Confirm only what the tool or page verifies. If opening is queued, say the page will open when the user returns to this chat; do not create duplicate tabs. If opening fails or the client has no in-app browser, provide [Start daily practice](https://freegama.com/play) and explain that the user needs to open the link.
4. Hand control to the user with one short sentence. Let them choose any profile or guest option and complete the games. Do not answer game rounds, advance the session, or submit scores for them.

## Keep the session accurate

- Let the website choose today's practice and respect a completed day. Do not calculate a separate daily set or reset progress.
- Saved website progress belongs to the browser in which the user plays. Do not promise that an external browser's profile, streak, or scores will appear here.
- Read or summarize scores only if requested, using results the user provides or that are visible on the page. Do not extract browser storage or invent results.
- Describe practice and game performance without promises about IQ, grades, or preventing cognitive decline.
- The request opens practice now. It does not request reminders or a recurring schedule.
