---
name: safe-editing
description: Edit existing WordPress posts and pages safely: small text changes, updated sections, new categories, status changes. Use whenever the user asks to change, fix, update or rewrite content that already exists on their site.
---

# Editing existing content

1. Read before writing: `wp_get_post` (or `wp_get_post_snapshot`) to see the current content and status.
2. Prefer the smallest change that does the job:
   - a word, sentence or link: `wp_alter_post` (find and replace inside one field)
   - a whole section or new layout: `wp_write_blocks`
   - title, excerpt, slug, status or date: `wp_update_post`
3. Before changing a published post, say what will change and get a clear yes.
4. Never change the status of a published post (unpublish, schedule) unless the user asked for that exact change.
5. After the change, read the post again and confirm what is now live.

For removals, `wp_delete_post` moves the item to the trash, where it can be restored. Permanent deletion is not available.
