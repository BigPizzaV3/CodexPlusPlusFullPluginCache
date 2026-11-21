---
name: get-started
description: How to edit an Evlop mobile app safely - read before changing pages, theme, settings or custom blocks.
---

# Editing an Evlop app

Evlop builds native iOS and Android apps for Shopify stores. This plugin edits one app as a tree of files. Nothing you write goes live: every change is staged in a draft that the merchant reviews and publishes in Evlop's code editor.

## Start every session

1. Call `list_files`, then `read_files` on `/docs/README.md` (file layout) and `/docs/block-types.md` (valid section types).
2. Read a file before changing it, and keep every field you were not asked to change.

## Pages and sections

- Prefer the section tools over editing page JSON: `list_sections` first to get ids, then `get_section`, `update_section`, `add_section`, `move_section`, `set_hidden`, `delete_section`.
- `update_section` takes a JSON merge patch: objects merge, `null` deletes a key, arrays replace.
- To stop showing a section without losing it, use `set_hidden` rather than `delete_section`.

## Theme, features and integrations

- `/config/theme.json` holds colors, fonts and text variants.
- `/features/*.json` and `/integrations/*.json` are `{ "enabled": boolean, "configuration": {...} }`.
- Use `edit_file` for small changes and `write_files` for whole-file rewrites.

## Custom blocks

- Create one with `add_custom_block` (type and name), then edit its `.tsx`, `data.json` and `configurationSchema.json` files. Compiled JS is built automatically.
- Only the allowed packages can be imported (see https://developers.evlop.com/custom-blocks/). No browser APIs and no relative imports.

## Images

- `list_images` shows uploaded images. `create_image_upload_url` returns a signed PUT URL; the merchant uploads the file, then the returned `url` can be used anywhere an image URL is expected.

## Finish

- Call `get_preview_url` and share the link so the merchant can check the result on a phone frame.
- Call `list_pending_changes` to summarise what changed. Tell the merchant to open Evlop's code editor to review and publish the draft, or use `revert_changes` if they want to discard it.
