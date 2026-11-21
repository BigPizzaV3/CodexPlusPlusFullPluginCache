# Uploading a file on this host

- A file the user attached, or one made in the code sandbox: `optisigns_asset_upload_from_url` with the
  file as `file`, one call per file. The sandbox cannot reach the upload service, so never use
  `optisigns_asset_upload_begin` → POST here.
- A file at a public https URL: `optisigns_asset_upload_from_url` with `url`.
- A file that exists only as a download for the user: ask them to drop it into the chat, then upload it
  as `file`.
- If the upload still fails, hand the user the file and ask them to upload it in the OptiSigns portal;
  continue from the asset they uploaded.
