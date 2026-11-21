---
name: create-social-project
description: Create an SMEPost social content project in a user-selected organization and return its project link. Use when the user asks to start a campaign, launch, or ongoing social content workspace.
---

# Create a social project

1. Call `list_organizations`; ask the user to choose if the destination is ambiguous.
2. Call `list_social_projects` with the selected `orgId` to avoid creating a duplicate. Follow `nextCursor` with `cursor` until the requested project is found or no further page remains.
3. Confirm a concise project name and purpose if either is unclear.
4. Call `create_social_project` with `orgId`, `name`, and optional `description` using the selected organization and user-approved details.
5. Use `list_project_folders` with `orgId` and `projectId` to review the new project's folders. Create only a folder the user requested or that is needed for the agreed organization, using `create_project_folder` with `orgId`, `projectId`, and `title` (optional `icon` and `color`).
6. Call `get_project_link` with `orgId` and `projectId`; return the created project name and its SMEPost URL.

Do not say the project exists until `create_social_project` succeeds. Never create an organization on the user's behalf.
