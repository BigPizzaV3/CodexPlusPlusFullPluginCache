# Publishing, uploads, and revisions

Follow the core contract for input choice, visibility, target matching, and conflict recovery. These details extend it. The runnable examples below are validated against the registered MCP schemas.

## Single document

<!-- example:create-html -->
```json
{"tool":"create_page","args":{"title":"Weekly brief","html":"<!doctype html><html lang=\"en\"><head><meta charset=\"utf-8\"><title>Weekly brief</title></head><body><main id=\"brief\"><h1>Weekly brief</h1><p>Three decisions for the week.</p></main></body></html>","visibility":"organization"}}
```

Plain `html` is limited to 512 KiB of UTF-8 bytes, creates index.html, and cannot be combined with another content mode or a custom entrypoint. Use a file bundle for local assets, multiple routes, or larger documents. No extra model call or remote asset fetch occurs.

## Signed upload

Compute byte_size and lowercase SHA-256 from the exact file bytes, locally. Start with an inventory of every file, including unchanged files. PUT only entries marked `upload_required`; entries already present need no upload. Use returned URLs and required_headers exactly and do not expose signed URLs to others.

<!-- example:create-upload -->
```json
{"tool":"create_page","args":{"title":"Hello","upload_files":[{"path":"index.html","content_type":"text/html","byte_size":5,"sha256":"185f8db32271fe25f561a6fc938b2e264306ec304eda518007d1764826381969"}],"source_meta":{"filename":"index.html"}}}
```

This inventory describes the UTF-8 bytes `Hello`. A real Page should contain your complete HTML. The server returns upload_session_id and the required PUT instructions; use that returned ID on completion. The UUID below stands for the returned ID in this executable fixture.

<!-- example:create-complete -->
```json
{"tool":"create_page","args":{"title":"Hello","upload_session_id":"33333333-3333-4333-8333-333333333333","source_meta":{"filename":"index.html"}}}
```

The manifest is optional when the bundle uses the default index.html route. If supplying one, schema_version is the string `"1.0"`. Include its entrypoint and routes mapping public path to file_path, with asset_paths when known. The upload_files inventory supplies file metadata; manifest.files is optional. If you include manifest.files, recompute it from the edited bytes. Never reuse stale sizes or hashes. Put multi-route sites in one Page and verify every internal link resolves to a file and route.

Keep original title, visibility, source_meta, target_choice and other requested metadata on create completion. For update sessions keep page_id, base_version_id and requested update metadata. The server binds an update session to its original base. If another revision publishes, reconcile against a fresh read/export and start a new session.

## Export, edit, update

Read before revising. Fixture UUIDs below represent IDs returned by the preceding calls.

<!-- example:read-before-update -->
```json
{"tool":"read_page","args":{"page_id":"11111111-1111-4111-8111-111111111111"}}
```

When file_bundle is null, export the full current bundle. Edit the main file and all auxiliary files, respecting their encoding. For a reference file, fetch its URL through an authorized viewer; if unavailable, ask the human for the file. Verify each fetched reference against its supplied sha256 and byte_size: its published URL can advance after export. On a mismatch, re-export and reapply your edit. Do not drop an inaccessible asset, relabel old bytes, or change sharing to retrieve it. Retain the version_id and manifest in the export response; they describe the same immutable version. A read followed by a later export can span a concurrent publication. Preserve the exported entrypoint and routes through both upload calls. Custom route mappings require signed uploads; if your client cannot PUT files, hand off that upload instead of flattening the routes into an inline update.

<!-- example:export-current -->
```json
{"tool":"export_page","args":{"page_id":"11111111-1111-4111-8111-111111111111","export_type":"html"}}
```

<!-- example:update-html -->
```json
{"tool":"update_page","args":{"page_id":"11111111-1111-4111-8111-111111111111","base_version_id":"22222222-2222-4222-8222-222222222222","html":"<!doctype html><html lang=\"en\"><title>Weekly brief</title><main id=\"brief\"><h1>Weekly brief</h1><p>The decision is approved.</p></main></html>","update_reason":"Record the approved decision"}}
```

This replaces the whole Page with one index.html. For a multi-file Page send all files instead. On version_conflict, re-read/export, compare the intervening changes, reapply the intended edit, then update with the fresh base. Replaying a completed upload is safe only for that original session and intent; it is not a way to overwrite a later revision.

## Preserve custom routes when updating

This fixture has index.html containing `<h1>Home</h1>` and report.html containing the edited `<h1>Report approved</h1>`. The inventory includes both files with hashes and sizes computed from those exact UTF-8 bytes. The manifest preserves `/` and `/report` from the export and intentionally omits file metadata. Replace the fixture IDs with the exported page/version and returned upload session IDs.

<!-- example:update-upload -->
```json
{"tool":"update_page","args":{"page_id":"11111111-1111-4111-8111-111111111111","base_version_id":"22222222-2222-4222-8222-222222222222","upload_files":[{"path":"index.html","content_type":"text/html","byte_size":13,"sha256":"1a7133067a4ac7fe06565943dd44870f232041b1d28b4340e2b678244a3b79f6"},{"path":"report.html","content_type":"text/html","byte_size":24,"sha256":"157d6df2aaa248f3db3045d2312762e100dccaa9de8927e2eb2ada74f66ed962"}],"manifest":{"schema_version":"1.0","entrypoint":"index.html","routes":[{"path":"/","file_path":"index.html","asset_paths":[]},{"path":"/report","file_path":"report.html","asset_paths":[]}]},"update_reason":"Record report approval"}}
```

PUT only files marked upload_required. Keep the same base and manifest when completing:

<!-- example:update-complete -->
```json
{"tool":"update_page","args":{"page_id":"11111111-1111-4111-8111-111111111111","base_version_id":"22222222-2222-4222-8222-222222222222","upload_session_id":"33333333-3333-4333-8333-333333333333","manifest":{"schema_version":"1.0","entrypoint":"index.html","routes":[{"path":"/","file_path":"index.html","asset_paths":[]},{"path":"/report","file_path":"report.html","asset_paths":[]}]},"update_reason":"Record report approval"}}
```

An interrupted or completed upload retry cannot restore earlier sharing after a human changes access. Follow the returned refusal and start a fresh authorized update when required.

## Comments

<!-- example:read-comments -->
```json
{"tool":"read_comments","args":{"page_id":"11111111-1111-4111-8111-111111111111","queued_only":true}}
```

<!-- example:reply-after-update -->
```json
{"tool":"add_comment","args":{"page_id":"11111111-1111-4111-8111-111111111111","parent_comment_id":"77777777-7777-4777-8777-777777777777","body":"Updated the decision in the latest version."}}
```

Use the returned comment ID as parent_comment_id to reply after publishing the requested change. Explain blocked requests rather than silently dropping them.

## File bundle checks

Build locally before sending files: there is no server build step. Use relative paths, supply every referenced asset, validate links and markup, and keep stable review targets. Limits depend on the organization's plan and custom settings; handle the server's returned maximum and actual values rather than guessing or retrying an oversized bundle unchanged.

## Deck publishing

For newly authored slides, give every slide a stable ID and call `prepare_deck` to assemble the supported shell without publishing or calling a model. Publish the returned bundle with `presentation: { "intent": "deck" }`. For an existing deck export, preserve and publish its files directly rather than rebuilding it through the assembler. Report the live URL and the separate version-bound presentation status; only `ready` means presentation controls are verified.
