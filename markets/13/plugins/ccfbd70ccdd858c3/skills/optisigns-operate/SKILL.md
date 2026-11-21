---
name: optisigns-operate
description: Publish and manage content on OptiSigns screens. Use when the user wants to upload, publish or put content on a screen, build or edit a playlist, schedule content for certain days, hours or a future date (dayparts, weekdays only, until a date), rename or organize screens, assets and folders, or find out why a screen is offline, blank or showing the wrong thing.
---

# Operate OptiSigns

Drive the OptiSigns tools correctly. Tool descriptions carry the exact arguments; this skill carries the
order and the rules. Read the matching reference before an unfamiliar step.

## Publish recipe

1. **Get the content in.** [references/publish.md](references/publish.md)
   - A file (PNG, JPG, MP4, PDF, PPTX…) that comes with a download link, or sits at a public https URL:
     `optisigns_asset_upload_from_url`, one call per file.
   - A file with no link (attached in chat, or made in the code environment): follow this host's route
     in [references/upload-route.md](references/upload-route.md).
   - A public https web page or dashboard: `optisigns_asset_create` with `url`.
   - A built-in app (weather, feeds, Google Slides…): `optisigns_app_manifest` → `optisigns_asset_create`
     with `appType` + `appData`.
2. **Wait until ready.** An upload returns while OptiSigns is still processing it: poll
   `optisigns_asset_get` with `assetIds` until it reports `ready`; stop if it returns a `note` (failed or
   `stuck`) and re-upload. Never add or assign a not-ready asset.
3. **Playlist** (several items or set durations): `optisigns_playlist_create` →
   `optisigns_playlist_item_add` → `optisigns_playlist_item_update` / `optisigns_playlist_item_reorder`.
   [references/playlists.md](references/playlists.md)
4. **Schedule** (certain days or hours, or a future start): `optisigns_schedule_create` →
   `optisigns_schedule_item_add` in the screen's local time.
   [references/scheduling-rrule.md](references/scheduling-rrule.md)
5. **Assign.** Find the screen (`optisigns_screen_search`), then `optisigns_screen_assign_content` with
   the asset, playlist or schedule. [references/assign-and-conflicts.md](references/assign-and-conflicts.md)
6. **Confirm what happened.** Say which screens now show what, from when, and in which team. Name
   anything that did not happen.

## What the tools can't do

- **Assign is now-only.** `optisigns_screen_assign_content` changes the screen immediately; there is no
  future time. For a future go-live, put the content on a schedule that starts later and assign the
  schedule now.
- **Adding always appends.** `optisigns_playlist_item_add` has no position; add, then
  `optisigns_playlist_item_reorder`.
- **No file swap.** Uploading a new version of a file creates a new asset. Replace it inside playlists
  and schedules (see the automate skill's update-in-place steps). Only web and app assets change in
  place (`optisigns_asset_update` with `url`).
- **Overlapping schedule items are rejected.** There is no priority; split the time instead.
- **Default content outside a daypart** is not settable here. Cover the other hours with their own items,
  or set the schedule's default content in the OptiSigns portal.

## Rules

- House rules: [references/house-rules.md](references/house-rules.md) (voice, truth, disclosure, escalation).
- **Confirmation.** Live changes and deletes need the user's approval, in one of two forms:
  - **Approval card:** the tool shows a card. The user approves or cancels there; don't call the tool again.
    Never say it is done before the card reports it.
  - **`OPTISIGNS_CONFIRM_REQUIRED`:** the result's first line starts with this, plus a summary. Nothing was
    written. Ask the user in plain words, quoting the summary (what changes, on which screens, which team).
    Re-call the same tool with the same arguments plus `confirmed: true` only after they say yes.
  Never confirm on their behalf.
- **Deletes go to Trash.** Deleted assets, playlists, schedules and folders can be restored in the portal
  for 30 days. Operational (power/CEC) schedules can't be trashed: they are deleted in the portal.
- **Playlist already playing.** If assigning returns `OPTISIGNS_SCREEN_CONFLICT`, ask whether to
  **replace** what is playing or **append** to that playlist (append is for a single asset only). Re-call
  with the same arguments plus `existingContent`. Never decide alone, never change `contentType`, and
  never build a new playlist to work around it.
- **Teams.** Every result names the team it acted in. If the user belongs to several teams and didn't say
  which, ask, then pass `teamId` on every write.
- **Keep the `assetId`.** The stored `name` can differ from the uploaded one (slugified, or `.docx` →
  `.docx.pdf`). Refer to assets by id; never search by the uploaded name; never rename on your own
  (offer `optisigns_asset_update`).
- **Check before you change shared things.** `optisigns_playlist_where_used` before editing or deleting a
  playlist; tell the user which screens and schedules it affects.
- **Errors.** A plan-gated feature returns "isn't available on this account's plan"; say so plainly.
  For any plan limit (a feature, a device such as Fire TV on Free), name the plan that includes it
  ("supported on the paid plans", "included from Pro Plus"); never the word "upgrade".
  Some failures arrive with an `errors` list on a normal result; read it before claiming success.

More: [references/organize.md](references/organize.md) ·
[references/troubleshoot.md](references/troubleshoot.md) ·
Help Center articles: [references/kb-troubleshooting.md](references/kb-troubleshooting.md)
