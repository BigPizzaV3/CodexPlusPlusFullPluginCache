---
name: generate-social-design
description: Create a social campaign image with an image capability available in the current host and save it into an SMEPost project or folder. Use when the user asks for a new visual, post image, campaign creative, or design asset.
---

# Generate and save a social design

1. Confirm the organization, project, target channel, aspect ratio, and visual brief. Use `list_organizations`, `list_social_projects` with `orgId`, and `list_project_folders` with `orgId` and `projectId` to resolve existing destinations.
2. Read `get_brand_context` with `orgId` before creating the visual brief. Apply the authorized brand voice, colors and design rules. Check the current host for an image-capable tool; use it when available, otherwise use an image supplied by the user. Do not assume image generation is available.
3. For a ChatGPT image, pass its file object to `import_asset_file` with `orgId`, `projectId`, `idempotencyKey`, and `title`; `folderId`, `materialId`, `description`, and `imagePrompt` are optional. Keep one stable idempotency key per file and target. SMEPost fetches and validates the file and returns the completed design. Do not pass the ChatGPT file's temporary `download_url` outside the `file` field or copy it into metadata.
4. For a local image from Codex or Claude Code, read its MIME type and byte size, then use `prepare_asset_upload` with `orgId`, `projectId`, `idempotencyKey`, `title`, `mimeType`, `fileSize`, and `sourceHost`; `folderId`, `materialId`, `description`, and `imagePrompt` are optional. Set `sourceHost` to `codex` in Codex or `claude_code` in Claude Code. It records the asset's source in SMEPost and does not enable funnel events or campaign tracking. Make the idempotency key unique, at least eight characters, and use only letters, numbers, `.`, `_`, `:`, or `-`.
5. If the prepare result contains `completed`, reuse that saved result. If it is already uploaded, proceed to completion. Otherwise locate the installed plugin root from this skill's path and run `node "<plugin-root>/scripts/upload-asset.mjs" "<prepare-result.json>" "<image-file>"`. Do not assume the shell starts in the skill folder. Check that the host can execute a file upload; if unavailable, report that limit and return the existing project link. The helper accepts an approved SMEPost upload URL and supported image bytes up to 4 MiB, and prints the session ID without credentials.
6. Call `complete_asset_upload` with `orgId` and the returned `uploadSessionId` for the local-image route.
7. Verify the returned design or call `list_project_designs` with `orgId` and `projectId`. Call `get_project_link` with `orgId` and `projectId`; return the design name, destination folder, SMEPost URL, and `creditsCharged` result.

For Codex, use an available Codex image-generation capability. For Claude Code, use a user-provided image or an external image tool already configured in that session. Do not assume either host provides image generation. SMEPost image generation can use SMEPost credits; explain this and get explicit authorization before using that paid route. An external image import does not deduct SMEPost image credits, but normal storage and upload limits apply.

Report generation, upload, and asset registration as separate facts. If any step fails, say which step failed and do not claim the design was saved.
