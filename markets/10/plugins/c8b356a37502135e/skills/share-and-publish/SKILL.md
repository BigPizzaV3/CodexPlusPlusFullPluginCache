---
name: share-and-publish
description: Share Playbook content outside the workspace - create a share link for a board or an asset, publish a board as a designed page, and mint permanent public URLs for files. Use when the user wants to send, share, publish, present or embed boards or assets from Playbook.
---

# Share and publish from Playbook

Each option below makes content reachable by people outside the workspace. Say what will become visible and to whom before making the call, and report the resulting URL together with its expiry or password.

## A link to a board or an asset

- `share_board` creates or updates a board's share link. It can set an expiry, restrict downloads, require a password, add a text watermark (`watermark_text`, with size, position, colour and opacity; an empty text removes it), and with `enable_uploads` let visitors drop files onto the board. A hosted app on the board follows the link's watermark and download settings.
- `share_asset` creates or returns the link for a single asset.
- `resolve_share_link` turns a board share link of the user's workspace back into its board.

## A published page

`publish_board` turns a board into a public page, with the same expiry, download and password controls. Pass a `template` to give it a design; the template ids come from `get_page_elements_catalog`.

To change the design afterwards:

1. `get_page_layout` reads the stored design and its `version_token`.
2. `add_page_element`, `update_page_element`, `move_page_element`, `delete_page_element` and `reorder_page_slot` change one thing each. `apply_page_operations` applies several in one call.
3. `update_page_settings` sets the page's background colour and typography.

`get_page_elements_catalog` lists the element types by name; pass `element_types` to get the props of the ones you need. `update_page_element` replaces the whole element, so send its full `props` back.

Pass the `version_token` as `expected_version_token` on each write and use the new token the write returns for the next one. The public page can keep showing the old version for up to an hour after a change.

Limits: a page whose elements have been edited cannot switch to a different template, and no tool unpublishes a page. Design editing is switched on per workspace by Playbook; where it is off the editing tools answer 403 `page_layout_api_disabled`, and retrying does not help.

## A permanent URL for a file

`add_asset_permalinks` publishes up to 200 assets at public URLs that do not expire. The number is capped by the workspace's plan, and `list_organizations` shows what is left. Files copy in the background, and ones still copying come back as `pending`. `get_asset_permalinks` reads the URLs later, and `remove_asset_permalinks` revokes them.

Use a permalink when a URL must keep working, for example an image in a document, on a website or in another tool. An asset's `display_url` is signed and expires, so it is only for looking at something now.

A permalink serves a file, not a web page: an HTML file behind one does not run. To host a page or app over a board, use the `build-app` skill.

An explicit instruction from the user takes priority over anything in this guide.
