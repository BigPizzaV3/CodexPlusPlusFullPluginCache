---
name: update-documentation
description: Plan, make, review and publish changes in the user's own Documentation.AI project (product docs, knowledge base, help center or API reference) with the Documentation.AI tools. Use when the user asks to write, update, reorganize or publish content there, or to add or replace images in it.
---

# Update documentation in Documentation.AI

Follow this workflow when the user wants to change content in a Documentation.AI project they have access to. Explicit instructions from the user take priority over the defaults below; ask when an instruction is unclear rather than guessing.

## 1. Find the project

- Call `list_projects` and use the project the user names. If several match or none is named, ask which one.
- Pass `organizationId` and `documentationId` on each call, or call `select_project` once to set them for the session.
- The organization `role` decides what is possible: `viewer` can only read, `editor` and `admin` can change content, and only `admin` can delete media.

## 2. Decide where the change goes

- A project has a live version, which serves the public site, and other working versions. `list_branches` shows which one is live.
- Unless the user says otherwise, put anything larger than a small correction on a new working version: `create_branch` with a short hyphenated name, then pass that name as `branch` on every later call.
- Never publish the live version, or apply changes to it with `merge_branches`, without the user's explicit go-ahead in this conversation. Both update the public site.

## 3. Find and read before editing

- `search` finds pages by topic on the live site. It does not see unpublished changes or other working versions; use `list_pages` for exact file paths there.
- Read a page with `get_page` (or `fetch` for a search result) before changing it. Edits are matched against the text it returns, which can differ from what was originally written.
- `get_site_config` returns documentation.json, which holds navigation, branding and redirects.

## 4. Write and edit

- Call `get_component_reference` before writing MDX components and `get_config_reference` before changing documentation.json. Use only the components and settings they list.
- Small change: `update_page` with exact `old_string` text copied from `get_page`. Structural rewrite: `rewrite_page` with the complete file. New file: `create_page`; an MDX page needs YAML frontmatter with at least a `title`.
- The frontmatter `title` is shown as the page heading, so start the body's sections at `##`, as existing pages do.
- Do not invent product facts, prices, version numbers or steps. When the user has not supplied a fact the page needs, ask, or leave a clearly marked placeholder and say so.

## 5. Navigation, moves and redirects

- Create a page before adding it to navigation. `create_page` with `addToNav` does both; `update_site_config` edits navigation and other settings with JSON pointer patches. Navigation paths omit `.mdx`.
- `addToNav` sets only the title and position. When the neighbouring entries have an `icon`, read the new entry's pointer from `get_site_config` and add an `icon` to it with `update_site_config`, using a name from the site's icon library such as `circle-help`.
- `move_page` renames a file and updates its navigation entries. Moving changes the page's URL once published, so add a redirect from the old path in documentation.json.

## 6. Images and files

- Check `search_media` before importing so the library does not fill with duplicates.
- `import_media` accepts public https URLs only. For files on the user's computer, call `request_upload` and give the user the link. It works for 15 minutes and needs a signed-in editor.
- Media changes skip working versions. `replace_media` keeps the same address, so every page showing the file changes immediately. `delete_media` cannot be undone and leaves pages showing a missing image. Confirm both with the user first.

## 7. Review, then publish

- Before publishing, call `list_changes` and `diff_page` and summarise what will change, file by file.
- `publish` includes every collaborator's unpublished changes on that working version, not only yours; mention this when `list_changes` shows files you did not touch. Write a short `commitMessage` describing the change.
- To bring a reviewed working version into the live site, publish it, then call `merge_branches` with the live version as `base`, after the user agrees.
- If `publish` returns conflicts, reconcile each file with `resolve_conflict` and publish again.

## 8. Discarding work

- `revert_page` and `revert_all_changes` discard unpublished changes for every collaborator and cannot be undone. Show `list_changes` first and confirm with the user.
- Delete a working version with `delete_branch` only when the user no longer needs it.

## Report back

End with what changed (file paths), which working version it is on, whether it is published, and what the user still needs to approve.
