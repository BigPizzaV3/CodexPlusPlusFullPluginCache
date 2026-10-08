---
name: create-short-clips
description: "Clipping: create, inspect, reselect, repair, caption, or export short clips from an uploaded file, BlitzReels asset, or permitted public video URL."
---

# Clipping

Create or adjust one clip batch, follow its bounded state, and return verified results.

## 1. Resolve the source

- Use the identified BlitzReels asset ID when the user already chose one.
- For a ChatGPT attachment, call `media_upload_file` and use its returned asset ID.
- For an unidentified workspace file, call `media_list`; ask the user only when several plausible assets remain.
- For a public URL, confirm ownership or permission before creation. Call `media_import_inspect` when support is
  uncertain or the user asks for a preview.

Completion: exactly one verified asset ID or supported URL.

## 2. Create or adjust

- New batch: call `clips_create` once with exactly one of `assetId` or `url`.
- Public showcase: set `createSharePage` only when the user asks for one.
- Existing batch: use `clips_manage` to inspect, reselect, repair, caption, or export it.
- Selection: preserve an explicit range; use automatic best selection only when the user delegates the choice.
- Deletion: call `clip_batches_delete` for the identified batch only after the user confirms deletion.

Completion: one valid batch ID whose latest state reflects the requested creation or adjustment.

## 3. Follow the batch

- Read `batch.polling` from each result.
- When `shouldPoll` is true, call `clips_get` after the suggested delay.
- Continue the existing batch until a terminal state or the returned polling limit.

Completion: a terminal result or the latest bounded active state.

## 4. Deliver the result

- Report batch status plus rendered, review, and failed counts.
- List downloadable clips first, each with its verified title and URL.
- Include the studio URL when review or editing remains.
- Surface `lastErrorMessage` and per-clip errors from the latest tool result.
- At the polling limit, return the batch ID and studio URL and state that processing remains active.

Completion: every clip is accounted for with verified status and available links.
