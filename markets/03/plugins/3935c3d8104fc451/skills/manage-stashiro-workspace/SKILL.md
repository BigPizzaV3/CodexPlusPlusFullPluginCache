---
name: manage-stashiro-workspace
description: Use when the user asks to organize Stashiro workspace content by renaming, moving, pinning, reordering, trashing, restoring, or permanently deleting a Space, board, or card.
---

# Manage a Stashiro Workspace

Use this workflow for workspace organization and lifecycle changes, not for reading or composing card content.

1. Resolve named targets with `search`. Use an exact known ID directly. Never browse solely to validate a write destination, and never guess between duplicate names.
2. Use `rename_space`, `set_space_icon`, and `reorder_spaces` for Space metadata and sidebar order. Use `rename_board`, `move_board`, `set_board_pinned`, `reorder_pinned_boards`, and `reorder_boards_in_space` for board organization.
3. Use `move_card_to_board` for one card and `reorder_cards` for canvas layers or list distribution. Whenever a move or resize needs canvas geometry, also use the `layout-stashiro-board` skill and verify the result. Preserve every unrelated card and ordering value.
4. Prefer `trash_board` for removable boards because it is recoverable. Use `restore_board` to undo that operation.
5. Before `delete_board_permanently`, restate the exact board and that every card will be irreversibly deleted. Call it only after the user clearly confirms permanent deletion.
6. Before `delete_card`, restate the exact card when identity is not already unambiguous. The deletion is permanent.
7. Before `delete_space`, restate the exact Space and ask for confirmation. Explain that the Space is removed and every board still inside it moves to Trash. Boards moved elsewhere first are preserved.
8. After successful board or card changes, return exact `boardUrl` or `affectedBoards` links. Report deleted IDs without inventing links to deleted resources.
