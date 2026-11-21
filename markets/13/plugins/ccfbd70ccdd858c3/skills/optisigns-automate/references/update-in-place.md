# Update in place

Goal: the new version plays exactly where the old one did, without touching playlists, schedules or
screen assignments. **[confirm]** marks a call that needs approval. If it shows an approval card, the user approves
there. If it returns `OPTISIGNS_CONFIRM_REQUIRED`, ask the user (or use a standing approval, see SKILL.md), then
re-call with `confirmed: true`.

## The stable "current" slot

- One asset per recurring board, named `<Board> – current`, e.g. `Weekly Update – current`,
  `Lobby KPIs – current`. For files, the new upload takes the same name with a date:
  `Weekly Update – 2026-11-02.png`, and the old one is removed from the playlist.
- One playlist (or schedule) the slot lives in; screens point at that, never at the slot directly, unless
  the user wants a single full-screen board.
- Record the ids (asset, playlist, schedule, screens, team) in the task prompt. Look up by id each run;
  names can change.

## A. Web or app asset (true in place)

1. Regenerate and publish the page at its new URL (or keep the same URL if the page refreshes itself; then
   there is nothing to do in OptiSigns).
2. **[confirm]** `optisigns_asset_update(assetId, url: <new https URL>)`.
3. Verify: `optisigns_asset_get(assetId)` shows the new link.

Every playlist, schedule and screen using the asset changes immediately. The old URL is not kept; note it
in the report if the user may want to roll back.

## B. File asset inside playlists

There is no file swap: an upload always creates a new asset id.

1. Upload the new file as in optisigns-operate's publish recipe and keep the returned `assetId`.
2. Wait for `ready`; if not, poll `optisigns_asset_get` until it reports `ready`. Stop here if it never
   becomes ready; the old version stays.
3. Take the playlists to update from the task prompt (their ids). `optisigns_playlist_where_used(playlistId)`
   lists the screens and schedules each one feeds, for the report. For each playlist:
   1. `optisigns_playlist_get(playlistId)` → the old item's position `oldIdx`, its item id and duration.
   2. `optisigns_playlist_item_add(playlistId, assetIds: [newAssetId])`: it lands last.
   3. `optisigns_playlist_get` again → `lastIdx`.
   4. `optisigns_playlist_item_reorder(playlistId, froms: [lastIdx], to: oldIdx)`.
   5. `optisigns_playlist_item_update(playlistId, position: oldIdx, durationSeconds: <old duration>)`.
      The playlist read doesn't return transitions, so a custom transition on the old item isn't carried
      over; mention it if the user set one.
   6. **[confirm]** `optisigns_playlist_item_remove(playlistId, itemIds: [oldItemId])`. Use the item id, not
      the position: positions shifted.
4. Verify: `optisigns_playlist_get` shows the new asset at `oldIdx` and no old item.
5. Optional cleanup: offer to delete the old asset (`optisigns_asset_delete`, **[confirm]**) only if
   nothing else uses it. Keeping the last one or two allows rollback.

An unattended run stops after step 2 and asks, naming the new asset, each playlist and the screens it
feeds. Step 3 changes what screens play, so it runs only after the user's yes (or under a standing
approval for this slot), as one sequence.

## C. Schedule items

1. Upload and wait ready (B.1–2), or reuse a playlist.
2. `optisigns_schedule_item_list(scheduleId)` → the item id currently playing the old content.
3. **[confirm]** `optisigns_schedule_item_update(scheduleId, itemId, scope: "ALL", contentId: <new id>,
   contentType: "asset" | "playlist")`. Omitted times are kept. For one date only use `scope: "SINGLE"`
   with `occurrenceStart`.
4. Verify with `optisigns_schedule_item_list`.

Better: point the schedule item at a playlist and update the playlist (B). The schedule then never changes.

## D. Direct assignment (asset on a screen, no playlist)

1. Upload and wait ready.
2. **[confirm]** `optisigns_screen_assign_content(deviceIds, contentId: <new id>, contentType: "asset")`.
   If it returns `OPTISIGNS_SCREEN_CONFLICT`, the screen is on a playlist: stop and ask replace or append.
3. Suggest moving the board into a one-item playlist so future runs use B and screens stay untouched.

## Rollback

- Web asset: `optisigns_asset_update` back to the previous URL **[confirm]**.
- File: the previous asset still exists until deleted; repeat B with it.
