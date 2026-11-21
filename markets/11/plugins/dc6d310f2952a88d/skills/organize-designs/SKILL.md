---
name: organize-designs
description: Find and organize SMEPost projects, folders, and saved designs. Use when the user asks to browse, locate, or sort existing social design work.
---

# Organize projects and designs

1. Call `list_organizations` and select the intended organization.
2. Call `list_social_projects` with `orgId` and identify the requested project by name before changing anything.
3. Call `list_project_folders` with `orgId` and `projectId`, and `list_project_designs` with `orgId` and `projectId`, to inspect the current project. For project/design/version searches, continue with each returned `nextCursor` as `cursor` until the requested item is found or the cursor is null; an empty filtered page can still have another page.
4. Create a folder only when requested, using `create_project_folder` with `orgId`, `projectId`, and `title`. Rename a folder with `update_project_folder` (`orgId`, `projectId`, `folderId`, and the changed fields) or a design with `update_design` (`orgId`, `materialId`, and the changed fields) only when the user gives the new name. Move a design only after the user names the destination, using `move_design` with `orgId`, `projectId`, `materialId`, and the target `folderId`; use `null` only when the user asks to remove the design from a folder.
5. Verify changes by listing the affected folder or project again. Preserve existing design/material records and versions.

Return concise names and the project URL from `get_project_link` with `orgId` and `projectId`. Never represent a folder or move in chat as if it had been created in SMEPost before the tool succeeds.
