---
name: geo-actions
description: Read CreceRank GEO recommendations and playbook actionables, open a content brief or Reddit thread, and mark an action done. Use when the user asks what to do next, wants priorities, a brief, or to update a checklist item.
---

Use this skill for recommendations and actionables from a completed scan.

If the user gives a different instruction, follow that instruction.

1. Call `crecerank_whoami`. If no scan has completed, say recommendations are unavailable until a scan finishes.
2. If they name a brand, call `crecerank_list_brands` and `crecerank_set_active_brand` when needed.
3. Call `crecerank_get_geo_recommendations` and `crecerank_get_geo_playbook` with `compact` true.
4. Recommend at most three actions taken from those results. Name the source item. Do not add actions the tools did not return.
5. For an article outline, call `crecerank_get_playbook_content_brief` with the playbook item's `task_id` and the other ids that item includes. Pass `regenerate` true only when they ask for a new brief.
6. For a Reddit action, call `crecerank_get_playbook_reddit_thread` with that item's ids. If the result is empty, say no thread was attached.
7. Call `crecerank_save_geo_actionable_done` only after they say an item is done or not done. Pass that item's `check_id` and `done`.
8. Call `crecerank_save_geo_actionable_note` only when they provide the note text. Pass `check_id` and `note`.

These writes stay inside CreceRank. Do not publish a post, send the brief somewhere else, or mark items done on your own.
