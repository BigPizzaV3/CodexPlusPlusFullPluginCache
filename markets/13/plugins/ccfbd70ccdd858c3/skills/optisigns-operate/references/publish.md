# Publish: getting content into OptiSigns

## Pick the path

| The user has | Tool | Result |
|---|---|---|
| A file (image, video, PDF, Office doc) | File upload below | File asset |
| A public https web page or dashboard | `optisigns_asset_create` with `url` | Website asset (live page) |
| An OptiDev project (`*.optidev.ai` URL) | `optisigns_asset_create` with `url` | OptiDev asset |
| A built-in app (weather, social feed, Power BI, Google Slides…) | `optisigns_app_manifest(appType)` → `optisigns_asset_create` with `appType` + `appData` | App asset |

`optisigns_asset_create` uploads nothing. A Website asset shows the page live, so it updates itself when
the page does. If a page refuses to load inside other sites, it may show blank; suggest a built-in app or
a file instead.

## File upload

A file that comes with a download link, or sits at a public https URL: call
`optisigns_asset_upload_from_url` with `file` or `url`, one call per file (max 100 MB). OptiSigns fetches
and uploads it, and the result is the same as step 3 below. For any other file, [upload-route.md](upload-route.md)
says which path this host takes; use the 3 steps only where it sends you to them.

### 3 steps, all required

1. `optisigns_asset_upload_begin` → `uploadUrl`, `params`, `signature`, `restrictions`. Read
   `restrictions.allowedFileTypes` and `restrictions.maxFileSize`; don't guess limits.
2. **POST the file yourself** from the code environment, straight from disk:
   `curl -sS -X POST <uploadUrl> -F params=<params> -F signature=<signature> -F file=@/path/to/file.png`.
   If the file is at a URL, download it to disk first. Never read the bytes into the conversation. The
   reply JSON has `assembly_id`; a 200 reply can still carry an `error` field, so check it. The options are
   short-lived: if the POST reports an expiry, call step 1 again.
3. `optisigns_asset_upload_finish` with that `assemblyId` and `name` = the user's filename unchanged,
   **with its extension** (the extension tells OptiSigns how to process it). Optional `folderPath`.

Skipping step 2 and calling step 3 anyway creates an empty asset stuck "converting" forever. Never invent
or reuse an `assemblyId`.

If the environment cannot make the POST, say so, hand the user the file and ask them to upload it in the
OptiSigns portal; then continue from the asset they uploaded.

### Several files

POST each file (step 2), then call `optisigns_asset_upload_finish` **once** with `files[]` (up to 20), one
entry per file with its own `assemblyId` and `name`.

## Ready

- `optisigns_asset_upload_finish` returns as soon as the asset is registered, with `ready: false`;
  `optisigns_asset_upload_from_url` first waits ≈15 s.
- Poll `optisigns_asset_get` with `assetIds` (up to 50 at once) until each reports `ready`: seconds for an
  image, minutes for a large video or document.
- Stop polling when it returns a `note`: status `failed`, or `stuck` (still converting after 10 min, so the
  file POST likely never landed). Tell the user, delete the asset and re-upload.
- Never add a not-ready asset to a playlist or assign it to a screen; the screen would show blank.

## Names and ids

- Keep the `assetId` the tool returned and use it for every later step.
- OptiSigns may change the stored name (slugified, or `.docx` saved as `.docx.pdf` after conversion); the
  result gives the stored `name`.
  Never look the asset up by the uploaded name. Never rename it unprompted; offer
  `optisigns_asset_update` with a new `name` if the user wants.

## Allowed file types

- Images: png, jpg, jpeg, gif, bmp, svg
- Video: mp4 (H.264 recommended), 3gp, m4v, webm, avi, mov, mpeg, mpg, wmv, m3u8, mpd
- Audio: mp3
- Documents: pdf, doc, docx, ppt, pptx, xls, xlsx, odt, ods

Not accepted: webp, heic, avif, mkv, html, zip. Convert first (for example webp/heic → png or jpg) and
tell the user you converted it.

## Folders

- `folderPath` on create or finish files the asset straight into an existing folder, e.g. `"/Marketing"`.
- Home (the top level) is `"/"` or omit the field.
- The folder must exist: `optisigns_folder_get_by_path`, or create it with `optisigns_folder_create`
  first ([organize.md](organize.md)).

## Re-publishing the same thing

`optisigns_asset_create` takes an optional `idempotencyKey`; reusing the same key updates one asset
instead of creating another. Without it, every call makes a new asset.

## After publishing

The asset is in the library but on no screen yet. Continue with a playlist, a schedule or
`optisigns_screen_assign_content`, then tell the user what is now live and where.
