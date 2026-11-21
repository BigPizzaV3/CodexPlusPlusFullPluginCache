---
name: optisigns-automate
description: Keep OptiSigns screens up to date automatically. Use when the user wants signage refreshed on a recurring basis or when a source changes, such as "every Monday", "daily", "each morning", "when the sheet changes", "keep the board current", or a weekly summary of email, chat, calendar, releases or social posts turned into slides, a KPI board, a menu change or an event countdown.
---

# Automate OptiSigns content

Recurring loop: **source → summarize → regenerate → update in place → verify**. Publishing itself
follows the operate skill's recipe; this skill adds the recurring part.

## 1. Choose content that updates itself (in this order)

1. **A built-in app, or a live web page that refreshes its own data** (a dashboard, a published sheet, a
   calendar view, a status page). No recurring job is needed for OptiSigns at all. Always check this
   first and say so if it fits. Ask which playlist or screens should show it, list them by name, and
   publish with `optisigns_asset_create` only after the user says yes.
2. **A web asset whose URL is swapped.** The job regenerates a page at a new URL, then
   `optisigns_asset_update{assetId, url}` (confirm). Playlists, schedules and screens keep pointing at the
   same asset; screens change immediately.
3. **A file swapped in place.** The job regenerates an image, PDF or video, uploads it (new asset), then
   replaces the old one inside each playlist or schedule. Most steps; use only when 1 and 2 don't fit.

Exact sequences and confirm points: [references/update-in-place.md](references/update-in-place.md).

## 2. The loop, each run

1. **Source.** Read it with the user's own connected tools (email, chat, calendar, spreadsheet, social).
   This plugin covers OptiSigns only.
2. **Summarize.** What matters on a wall: 3–5 items, short lines, readable from a distance. Apply the
   `signage-design` skill. A screen is public: show the user the exact items taken from their email,
   chat or calendar and let them drop any before anything is published. Never put private or personal
   content on a screen without their yes.
3. **Regenerate.** Same template, size and style every run so the screen looks consistent.
4. **Update in place** into the stable "current" slot; never create a new playlist or reassign screens
   each run.
5. **Verify.** New asset `ready`; `optisigns_playlist_get` or `optisigns_schedule_item_list` shows it in
   the old spot; the old item is gone. Report what changed, where, and when.

**Nothing new in the source?** Leave the screen as it is and report "no change". Never publish an empty or
placeholder slide.

## 3. First run, then recurrence

1. Do the first run with the user watching: show the generated slide or page and the target playlist and
   screens by name, and publish only after they say yes.
2. Only after they approve the result, set up the recurrence with your assistant's scheduled tasks.
   Write a self-contained task prompt: [references/host-scheduled-tasks.md](references/host-scheduled-tasks.md).
3. Ready-made task prompts for 7 common boards: [references/patterns.md](references/patterns.md).
4. **End your first reply with the draft task prompt**, in a code block, for the user to review; never
   create the scheduled task yourself. List prerequisites above it ("connect Slack", "approve the first
   slide"). It names the schedule, the source, what to generate, the exact asset/playlist slot to update
   in place, and that each run prepares the new version and asks before changing live screens unless
   the user wrote a standing approval.

## Confirmation in unattended runs

- A scheduled run only PREPARES the new version: read the source, generate, upload, wait `ready`. It does
  not touch any playlist, schedule, asset link or screen.
- Then it stops and asks the user, naming the new asset, the playlist or schedule, the screens it plays
  on, and the planned change. Only after their yes in the conversation does it update in place.
- **Standing approval** is the one exception: where the tool takes `confirmed`, a run may update in place
  and pass `confirmed: true` only when the task prompt contains the user's explicit approval in their own
  words (e.g. "I approve replacing the Weekly Update slide in Lobby Loop every Monday without asking").
  Quote it in the run's report. Scope is exactly that slot and those screens; anything else (a delete, a
  new screen, a different playlist) still asks.
- Never invent or widen a standing approval; never confirm on the user's behalf. Where a tool shows an
  approval card, there is no standing approval: the user approves on the card.

## Rules

- House rules: [references/house-rules.md](references/house-rules.md) (voice, truth, disclosure, escalation).
- Keep the target ids (asset, playlist, schedule, screens, team) in the task prompt; look them up by id
  each run, not by name.
- Pass `teamId` when the user has several teams.
- A `OPTISIGNS_SCREEN_CONFLICT` in a run: stop and ask; never pick replace or append alone.
- If a run fails (signed out, source unreachable, upload error), leave the screen as it was and report the
  failure plainly with the next step.
