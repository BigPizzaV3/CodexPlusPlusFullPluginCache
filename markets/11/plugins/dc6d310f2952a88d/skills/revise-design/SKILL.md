---
name: revise-design
description: Revise an existing SMEPost design while preserving its prior image and version history. Use when the user asks to edit, regenerate, or create a new version of a saved design.
---

# Revise a saved design

1. Select the organization and project with `list_organizations` and `list_social_projects` using `orgId`.
2. Use `list_project_designs` with `orgId` and `projectId`, then `get_design` with `orgId` and `materialId`, to identify the exact design. If several designs could match, ask the user to choose.
3. Call `list_design_versions` with `orgId` and `materialId` before changing the design. Use the latest version as reference and preserve the existing material and chat relationship.
4. Read `get_brand_context` for the selected organization, then apply the requested visual change to the authorized reference image using an actually available host capability or an image supplied by the user.
5. In ChatGPT, save the edited file with `import_asset_file` using the existing `materialId`, `orgId`, `projectId`, title, one idempotency key, and the generated or supplied file object. If SMEPost write tools are unavailable after the image handoff, ask the user to select the SMEPost App or use Workdesk's version menu action, **Save edited image as a new version**. Do not claim the host will automatically restore its tools, and never show internal IDs, file paths, raw JSON, or technical import instructions. The menu uses ChatGPT's file picker when available and the existing device-upload route otherwise. SMEPost downloads and validates the image and completes the version on the server; do not use shell PUT. In Codex or Claude Code, call `create_design_version` with the same destination plus MIME type, byte size, and `sourceHost` (`codex` or `claude_code`), upload with the bundled helper, then call `complete_asset_upload` with the returned `uploadSessionId`. Folder, description, and image prompt are optional. Make the idempotency key unique, at least eight characters, and use only letters, numbers, `.`, `_`, `:`, or `-`; reuse it when retrying the same image. Source metadata records provenance without analytics events.
6. Call `list_design_versions` again with `orgId` and `materialId`; follow `nextCursor` with `cursor` to confirm that the new version exists and earlier versions remain available. For PUT hosts, reuse a `completed` preparation result and call completion for an already uploaded session; do not repeat PUT. Locate the plugin root and run the Node helper by its resolved path, regardless of shell working directory.

Do not overwrite the only existing image or claim a new version exists until the server confirms it. Ask before using any SMEPost credit-gated image-generation workflow.
