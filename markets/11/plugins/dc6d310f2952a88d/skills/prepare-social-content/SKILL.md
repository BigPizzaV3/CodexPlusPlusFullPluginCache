---
name: prepare-social-content
description: Draft channel-ready social copy and connect it to an SMEPost project or publishing handoff. Use when the user wants captions, campaign messaging, platform adaptations, or to continue saved designs toward publishing.
---

# Prepare social content

1. Ask for the campaign goal, audience, channel, language, and any brand or product facts that are missing.
2. Draft concise copy for the chosen channel. Mark assumptions and keep claims grounded in the user's source material.
3. Read relevant brand guidance with `get_brand_context` using `orgId`. Find the destination with `list_organizations`, `list_social_projects`, and `list_project_folders` when the user wants the content stored with existing work. Use `save_design_caption` only when the user asks to save copy to a design; provide `orgId`, `materialId`, and `caption`, with optional `hashtags`, `title`, and `platform`.
4. Use `prepare_publishing_handoff` only when the user explicitly asks to continue toward publishing and approves the handoff; provide `orgId`, `projectId`, `materialId`, and `userApproved: true`. Explain that this opens SMEPost's full website review outside the Workdesk app; it does not itself publish or schedule a post.
5. Return the copy, its intended channel, and the project URL from `get_project_link` with `orgId` and `projectId` when available.

Do not publish, schedule, or create image assets unless the user asks for those actions.
