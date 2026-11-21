# Playlists

A playlist plays its items in order, each for its duration, then loops.

## Build one

1. `optisigns_playlist_create(name)`.
2. `optisigns_playlist_item_add(playlistId, assetIds[])`: only ready assets. Items go on the **end**.
3. Durations and transitions: `optisigns_playlist_item_update(playlistId, itemId | position,
   durationSeconds?, transition?)`. Positions are zero-based.
4. Order: `optisigns_playlist_item_reorder(playlistId, froms[], to)`.
5. Put it on screens with `optisigns_screen_assign_content` (`contentType: "playlist"`) or inside a schedule.

## Items are positional and append-only

- `optisigns_playlist_item_add` has no position argument; it always appends.
- To place an item at position N: add it, read the playlist (`optisigns_playlist_get`) to find its index
  (the last one), then `optisigns_playlist_item_reorder{froms:[lastIndex], to:N}`.
- `optisigns_playlist_item_update` changes duration and transition only. It cannot change which content an
  item points to. To swap content: add the new item, move it into place, copy the old duration, remove the
  old item (confirm).
- Re-read the playlist after each add or remove; positions shift.

## Nested playlists

- Pass `playlistIds` (not `assetIds`) to `optisigns_playlist_item_add` to nest a sub-playlist, e.g. a
  "Menu" playlist containing breakfast and lunch playlists. One call adds one kind.
- Nesting stops at 2 levels. It isn't available on every plan; on a plan error say "that isn't available
  on this account's plan" and offer a flat playlist or a schedule instead.

## Before you change or delete

- `optisigns_playlist_where_used(playlistId)` → the screens and schedules using it. Edits show on all of
  them right away. Tell the user which screens are affected before a live edit.
- Removing items (`optisigns_playlist_item_remove`) and deleting a playlist (`optisigns_playlist_delete`)
  are confirm-gated. Say what goes and where it was playing; wait for yes. A deleted playlist goes to
  Trash (restorable in the portal for 30 days).
- Renaming: `optisigns_playlist_update(playlistId, name)`; it changes only the name.

## Copy instead of edit

`optisigns_playlist_duplicate` makes a copy to try changes on without touching live screens. Edit the
copy, then assign it once the user is happy.

## Updating content that is already playing

Replace the item inside the existing playlist rather than making a new playlist. Playlists, schedules and
screen assignments then stay as they are. Exact steps: the automate skill's update-in-place reference.

## Common requests

| Request | Do |
|---|---|
| "Show each slide for 15 seconds" | `optisigns_playlist_item_update` per item, `durationSeconds: 15` |
| "Put this first" | add → reorder `{froms:[last], to:0}` |
| "Take the old promo out" | find its item, `optisigns_playlist_item_remove` (confirm) |
| "Add this to what the lobby is playing" | find the playlist on that screen, add to it; or assign the asset with `existingContent: "append"` |
