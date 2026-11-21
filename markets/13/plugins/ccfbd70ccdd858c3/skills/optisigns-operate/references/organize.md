# Organize

## Folders

- Each kind has its own folders: `type` = `asset` (default), `screen`, `playlist`, `schedule`. Pass the
  right `type` on every folder call.
- Find: `optisigns_folder_list(type, path?)`, `optisigns_folder_get_by_path(path, type)`.
- Create: `optisigns_folder_create(name, type, parentPath?)`. A sibling with the same name (any case) is
  refused and the existing folder's id is returned; use that one.
- Move: `optisigns_folder_move_items(itemIds[], targetFolderPath, type)`; ids must match the type.
- Paths look like `"/Marketing/Fall"`. Home (top level) is `"/"` or omit.
- New uploads go straight into a folder with `folderPath` ([publish.md](publish.md)).
- `optisigns_asset_list` without `path` lists only the top level; pass `path` or follow `cursor`.
- Deleting a folder (`optisigns_folder_delete`) is confirm-gated and moves it, with its contents, to
  Trash (restorable in the portal for 30 days).

## Screens

- Rename or rotate: `optisigns_screen_update(screenId, name?, orientation? LANDSCAPE|PORTRAIT)`.
- Pair a new screen: `optisigns_screen_pair(pairingCode)` with the code shown on the screen.
- Unpair (`optisigns_screen_unpair`) is confirm-gated; it releases the screen from the account.

## Naming convention (suggest, don't impose)

- Screens: `<Location> – <Spot>`, e.g. `Austin – Lobby`, `Austin – Break Room`.
- Folders: by location or department, matching screen names.
- Recurring content: one stable name per slot, e.g. `Weekly Update – current`.

Never rename on your own; offer it.

## Teams

- `optisigns_me` lists the user's teams. Results carry `actingTeam`.
- If the user has several teams and didn't say which, a write is refused with "You have several teams —
  say which team (pass teamId): …". Ask, then pass `teamId` on every call.
- Folders, screens and content belong to one team; moving between teams isn't done with these tools.
