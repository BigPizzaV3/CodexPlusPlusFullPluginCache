---
name: oac-catalog-management
description: Manage Oracle Analytics Cloud catalog content through the OAC MCP tools. Use when a user wants to create or replace supported workbook or connection content, export a workbook to PNG or PDF, create a catalog folder, copy an item, move an item, or delete an item. Use catalog search to resolve targets when needed. Treat create, replace, copy, move, and delete operations as production-impacting mutations that require explicit approval immediately before execution; export is non-mutating but starts an export job.
---

# Oracle Analytics Cloud Catalog Management

## Configured instance

Use only the Oracle Analytics MCP connection attached to the selected configured instance. Ground requests in that instance's live tools, metadata, identifiers, and permissions. Do not fall back to the template example URL, a remembered demo account or catalog path, or another instance's connection. If no instance is configured, explain that a workspace administrator must configure one before this workflow can run.

Use this skill for catalog organization and content lifecycle actions. Use the runtime-exposed MCP schema as the source of truth for arguments, identifiers, supported options, and result fields.

## Preflight

1. Identify the exact target object and requested operation.
   - Check whether the requested outcome is supported before starting any export or mutation. Email delivery and recipient-directory lookup are outside this plugin's tools.
   - For a request to email an export, explain this limitation and ask whether the user wants a supported PNG or PDF export. Do not start an export job or select another plugin before that separate choice.
2. If the target or destination is not already established by current tool output or an unambiguous identifier, use `oracle_analytics-search_catalog` to locate it.
3. For copy or move, establish both source and destination.
4. For create or replace, establish the supported content type and target catalog location.
5. For export, establish the workbook and requested format. The documented export formats are PNG and PDF.
6. Never infer overwrite, replacement, recovery, retention, or destination behavior that is not established by the live tool schema.

## Approval rule for mutations

Before calling any modifying tool, present the exact operation as understood and require the product's explicit approval flow. Modification tools require `userApproved: true` or an explicit approval flow.

Treat these as approval-gated production-impacting actions:

- `oracle_analytics-save_catalog_content`
- `oracle_analytics-create_catalog_folder`
- `oracle_analytics-copy_catalog_item`
- `oracle_analytics-move_catalog_item`
- `oracle_analytics-delete_catalog_item`

Do not set or imply approval until the user has approved the exact operation through the supported flow. A broad request to "manage" or "clean up" content is not approval for an unspecified mutation.

## Operation workflows

### Create or replace content

Use `oracle_analytics-save_catalog_content` only for supported workbook or connection catalog content.

- State whether the action will create or replace content when that distinction is known.
- Do not silently overwrite an existing item.
- Require explicit approval immediately before execution.

### Export a workbook

Use `oracle_analytics-export_workbook` to export a workbook to PNG or PDF.

- Export does not modify the catalog, but it starts an export job.
- No catalog-mutation approval is required by the documented tool table.
- Report export or job status only from the tool response.

### Create a folder

Use `oracle_analytics-create_catalog_folder`.

- Confirm the folder name and target location.
- Require explicit approval immediately before execution.

### Copy an item

Use `oracle_analytics-copy_catalog_item`.

- Confirm the source item and destination.
- Require explicit approval immediately before execution.

### Move an item

Use `oracle_analytics-move_catalog_item`.

- Confirm the source item and destination.
- Require explicit approval immediately before execution.

### Delete an item

Use `oracle_analytics-delete_catalog_item`.

- Identify the exact item and location.
- Do not infer that an item is safe to delete because it appears unused.
- Do not invent soft-delete, recycle-bin, retention, or recovery behavior.
- Require explicit approval immediately before execution.

## MCP tools

- `oracle_analytics-search_catalog`: Locate catalog objects before an operation when needed. Experimental.
- `oracle_analytics-save_catalog_content`: Create or replace workbook or connection catalog content. Experimental; modifies OAC; approval required.
- `oracle_analytics-export_workbook`: Export a workbook to PNG or PDF. Experimental; starts an export job; does not modify the catalog.
- `oracle_analytics-create_catalog_folder`: Create a catalog folder. Experimental; modifies OAC; approval required.
- `oracle_analytics-copy_catalog_item`: Copy a catalog item. Experimental; modifies OAC; approval required.
- `oracle_analytics-move_catalog_item`: Move a catalog item. Experimental; modifies OAC; approval required.
- `oracle_analytics-delete_catalog_item`: Delete a catalog item. Experimental; modifies OAC; approval required.

## Result handling

- Do not claim success until the MCP tool confirms it.
- Report the resulting object, destination, export status, or error using only returned information.
- If an export failed or no artifact is available, do not draft text claiming the file is attached or ready for delivery.
- Preserve uncertainty and tool errors rather than masking them.

## Boundaries

- Do not change permissions in this skill; use the governance and permissions workflow for ACL changes.
- Do not invent MCP parameters or unsupported catalog object types.
- Do not provision users, update source-database records, send email, or claim that these actions were completed.
- The OAC MCP integration is in Preview and the catalog-management tools listed above are experimental.

## Example requests

- "Create a folder named FY27 Planning under Shared Folders."
- "Move the Pipeline workbook into Sales Operations."
- "Export this workbook as PDF."
- "Delete the old forecast workbook."
