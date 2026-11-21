---
name: landit-assets
description: Explain Landit image upload requirements, use canonical asset variables and URLs, or change an owned asset's workspace sharing.
---

# Landit assets

Read [shared safety and identity](../../references/safety-and-identity.md) and [capabilities](../../references/capabilities.md). The AI may browse verified template previews, but MUST NEVER open prospect Page links, including indirect fetches, screenshots, HEAD requests, or link checks.

Call get_image_upload_instructions when upload guidance is needed. It returns a separate asset API procedure, not an upload result or new credential. This plugin has no attachment-upload or upload-bytes tool. In ordinary ChatGPT, explain that limitation and direct the user to Landit's supported asset UI. Do not claim an attached/generated image has been stored in Landit or invent a fetch-by-URL uploader.

Only in a host with separately authorized local file/HTTP execution and an already configured same-user LANDIT_API_KEY can the instructed API procedure be performed. Never request the key in chat, inspect credential stores, substitute the MCP OAuth token, create a key, or transmit secrets/file bytes as MCP arguments. Follow the live instructions and returned max_file_size_bytes, supported raster formats, nonblank name, and explicit shared choice. Let the HTTP client generate the multipart boundary. Current instructions say HTTP 201 creates a new asset on every upload, including identical images; do not claim older deduplication/HTTP-200 behavior.

Use returned canonical slug, variable, shared, and stable Landit url; do not guess names or use expiring storage redirect targets. Explain that shared controls workspace-library visibility, whereas anyone holding the hotlink can retrieve the image. A lost upload response may follow a completed creation; reconcile in the supported asset UI before repeating. An API request alone does not prove an upload succeeded.

For a requested sharing change, resolve the exact owned asset slug and intended shared boolean, then call update_asset_sharing(slug, shared). Reconcile the canonical returned fields. No get_asset tool is exposed; after an uncertain result, use authorized UI evidence or ask the user to verify before claiming success. Do not claim that shared=false revokes public hotlink access.

For template use, obtain exact asset references through get_template_authoring_context. External spreadsheet/CRM field binding is outside this plugin; provide the verified mapping without claiming another system was changed. Do not open a prospect Page to test an asset.
