---
name: get-started
description: Orient in a Playbook workspace - list its workspaces and boards, look at what a board holds, and choose the right Playbook tool for a task. Use when the user has just connected Playbook, asks what they can do with it, or asks about their boards or assets without naming one.
---

# Get started with Playbook

Playbook is a digital asset manager. A workspace contains boards, and a board contains assets: images, video, documents, notes and colour swatches. Boards nest inside other boards.

## Find your bearings

1. `list_organizations` returns the workspaces the signed-in account belongs to. When there is only one, later calls can leave `organization` out.
2. `list_boards` returns boards, with a title search and a hierarchy depth. `list_board_children` and `list_board_descendants` walk one branch.
3. `list_assets` with a board token returns what that board holds. `get_asset` returns one asset in full.
4. `get_asset_previews` renders images at a size you choose, which is how to actually look at an asset.

Board and asset tokens belong to one workspace. Read them again from `list_boards` or `list_assets` in each session instead of reusing a token from an earlier one.

## Where to go next

- Finding, tagging, moving or grouping assets: the `organize-assets` skill.
- Adding files, notes, colours or a new version of a file: the `upload-files` skill.
- Share links, published pages and permanent URLs: the `share-and-publish` skill.
- A hosted web app over a board, such as a gallery or catalogue: the `build-app` skill.
- Comments: `get_comments` and `create_comment`. People: `list_members`.
- Anything about the API itself: `list_documentation` and `read_documentation`.

## What Playbook cannot do here

- Hand over a file's bytes. A permalink or a `display_url` is the only way to reach a file.
- Read the text inside an image or extract captions from a video.
- Render a board as a PDF or a contact sheet.
- Turn a published-page or permalink URL back into a board or asset. Find the item by title instead. A board share link is the exception: `resolve_share_link` returns its board.

When a request needs one of these, say so and offer the nearest thing Playbook does provide.

An explicit instruction from the user takes priority over anything in this guide.
