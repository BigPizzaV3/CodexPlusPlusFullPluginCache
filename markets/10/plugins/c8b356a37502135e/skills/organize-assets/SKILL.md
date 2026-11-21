---
name: organize-assets
description: Find assets in Playbook and put them in order - search by keyword or by what an image shows, tag, set status and custom field values, move or copy between boards, archive and unarchive, and group variants. Use when the user wants to find, sort, label, clean up or restructure assets or boards in Playbook.
---

# Organize assets in Playbook

## Find the assets

- `search_assets` matches filename, title and tags, and filters by uploader, status and custom field value. Use it when the user gives words that appear on the asset.
- `ai_search` matches what an image shows or means, and filters by uploader and date range. Use it for a description such as "product shots on a white background".
- `list_assets` walks one board or a whole subtree when the user wants everything in a place rather than a match.

Look at candidates with `get_asset_previews` before acting on a visual judgement.

## Label them

- Tags on one asset: `change_asset_tags` adds and removes in one call.
- Title, description, tags, status, custom field values and board together: `update_asset`.
- The built-in Status field: `update_asset_status`.
- Approval and scheduled visibility for up to 1000 assets: `set_asset_approval`.

Custom fields have exact names and, for option fields, exact option names. Call `list_custom_fields` first and use the names it returns. A `multi_select` field takes a list (`["Web", "iOS"]`) and then holds exactly those options; every other field takes one value, and `""` or `[]` clears a field. A field or option the workspace does not have comes back as an error that lists the valid ones; that field keeps its previous value and the rest of the update is still saved. `create_custom_field` defines a new field (`field_type: "multi_select"` for one that holds several options), and called with the name of an existing option field it replaces that field's options, deleting any left out.

## Restructure

- `create_board` and `update_board` create, rename and re-parent boards.
- `move_assets` moves up to 1000 assets to a board in one call. `copy_assets` copies up to 1000 and finishes in the background.
- `archive_assets` archives up to 1000 assets. Each leaves its group unless the group is archived with it, and a group left with one asset is dissolved. `unarchive_assets` moves archived assets to a board the user picks, since the original board is not remembered; find them with `search_assets` and `include_archived: true`, which searches every media type.
- `group_assets` stacks variants under a parent asset; `ungroup_assets` reverses it. Children move to the parent's board.

## Before a large change

Moving, archiving, re-tagging or deleting many assets is hard to undo by hand. State which assets and boards will change and how many, and get the user's go-ahead before the call. `delete_asset` sends an asset to the trash, where it can be restored.

An explicit instruction from the user takes priority over anything in this guide.
