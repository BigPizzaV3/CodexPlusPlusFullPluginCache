---
name: upload-files
description: Add content to Playbook - upload a file from a URL or from bytes you hold, import folders from Google Drive or Dropbox, add notes and colour swatches, or store a new version of an existing asset. Use when the user wants to upload, import, save or add something to a Playbook board.
---

# Add files to Playbook

Pick the path by where the file is now.

## The file is at a URL Playbook can fetch

`upload_from_url` takes one public URL and a board. It returns a skeleton asset at once and Playbook fetches the file in the background, so read the asset back with `get_asset` before reporting the upload as finished. `upload_from_urls` takes up to 100 URLs for the same board. Playbook fetches anonymously: a link behind a login or an expired signed URL fails, and a very large or slow source runs out of time.

## You hold the file as bytes

A file generated locally, returned as base64 by another tool, or sitting on disk:

1. `create_upload_url` returns a one-time storage address and the exact request to make.
2. Send the bytes with that request. One request carries up to 100 MB.
3. `finish_upload` turns the stored bytes into an asset.

For several files use `create_upload_urls` and `finish_uploads`, and pass the `batch_id` from the first to the second. When a batch finishes only in part, the result says which files became assets; follow it instead of repeating the whole call, which would create duplicates.

## The file is in Google Drive or Dropbox

1. `list_import_sources` returns the connections the user has made, and a `connect_url`.
2. `import_from_google_drive` or `import_from_dropbox` takes 1 to 20 folders and a board.
3. `get_import` reports progress. Poll it until the status is `completed` or `canceled`.

A person connects Drive or Dropbox once in the Playbook web app. When no connection exists, give the user the `connect_url`.

## None of these is possible

`share_board` with `enable_uploads` returns a link where a person can drop files onto the board.

## Content that is not a file

- `create_note` adds a text note to a board.
- `create_colors` adds up to 100 colour swatches from hex codes or Pantone names; two or more become a palette.

## A new version of an existing asset

`create_asset_version` replaces an asset's file with one fetched from a public URL and keeps the previous file in its history. `list_asset_versions` shows the history, `revert_asset` restores an earlier version, and `edit_asset_version_comment` annotates one. Replacing a file changes what everyone sees, so confirm the target asset with the user first. Each call stores another version even for an identical file, so after a timeout check `list_asset_versions` instead of calling again. Large files are refused here and go through the Playbook web or desktop app.

## Files made by AI

The upload tools accept `ai_generated` and `ai_agent_payload`. Set `ai_generated` for content a model produced, and use the payload for the prompt or settings worth keeping with the asset.

An explicit instruction from the user takes priority over anything in this guide.
