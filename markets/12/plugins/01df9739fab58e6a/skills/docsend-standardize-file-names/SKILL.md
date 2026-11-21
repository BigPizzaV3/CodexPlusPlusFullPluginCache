---
name: docsend-standardize-file-names
description: Identify unclear or inconsistent document names in a DocSend Space and rename them using a consistent convention. Use for file naming cleanup, ambiguous filenames, and data room organization.
---

# Standardize File Naming

Example: “Find unclear file names in this data room and make them consistent.”

Use the DocSend MCP to inspect the target Space, propose content-supported names, and apply renames within the user's authorization.

## Find the Space and inventory

Resolve the target from conversation context or `list_spaces`. Ask only if the target remains ambiguous. Use its returned `home_folder_id` with `list_space_content`, then traverse relevant subfolders and follow pagination within each folder. Record document identifiers, current names, extensions when available, and folder paths internally. The Content Library is separate from Space content; do not substitute Library search results for the room inventory.

List the room's documents and folders in a readable form. Use folder paths or verified document links to distinguish same-named items. Disclose inaccessible items and incomplete retrieval; do not imply that an incomplete inventory covers the whole room.

## Choose a convention and inspect names

Follow the user's naming convention. Otherwise preserve useful existing conventions and prefer descriptive names containing the document subject. Do not add dates or versions unless the user requests them. Preserve existing dates, version numbers, and status labels when needed to distinguish documents or revisions; this preservation does not authorize inventing new metadata. Ask only when an unresolved choice materially affects the result.

Look for:

- Generic names such as “Document 1,” “Scan,” or “Untitled.”
- Automatically generated names such as “IMG_4821,” “DSC_0093,” timestamps, or random character strings.
- Clutter such as “Copy of,” repeated extensions, or “final_final.”
- Inconsistent capitalization, separators, date formats, or version notation.
- Names that do not clearly describe the contents.

Suggest descriptive, consistent replacements. Remove redundant version labels only when they serve no meaningful purpose. Do not erase distinctions between revisions or change the meaning of status labels for cosmetic consistency.

Inspect accessible document contents when needed to determine a meaningful name. Call `read_document` once without `page`; prefer downloading its `file_url` exactly once and analyzing the full document locally. Use a page request only for a specific-page question or when full-file access is unavailable; do not loop over every page instead of downloading the full file. Do not infer dates, versions, approval status, signatures, or document type without supporting evidence. If contents remain unavailable or unclear, flag that limitation and leave unsupported subject renames unresolved; propose purely mechanical cleanup only when it preserves meaning, and obtain approval before applying it.

Preserve a real file extension where applicable, correcting repeated extensions without changing the underlying format. Distinguish an extension stored separately by DocSend from an extension present in the display name; do not append an extra suffix merely because extension metadata exists. Check proposed names against both unchanged and other proposed names, particularly in the same folder. Avoid confusing duplicates; use content-supported distinguishing terms or ask for a material unresolved choice rather than inventing revision labels.

## Present and apply

Present a table with **Current name**, **Proposed name**, and **Reason**. Include folder context or document links when needed to identify items; never display internal identifiers. Flag rows whose contents are unavailable or unclear and indicate when no supported replacement is available. The user must approve the proposed changes before any file is renamed, including purely mechanical cleanup.

If the user requested suggestions, stop after the proposal. Otherwise ask the user to approve the proposed rename table before applying changes. A general request such as “find unclear file names and make them consistent” authorizes inspection and proposal preparation but does not substitute for approval of the proposed names. Once the user explicitly approves those changes and the convention is clear, apply only the approved rows without asking again for unchanged details. Ask only when an unresolved choice materially affects the result; leave unapproved or unresolved rows unchanged. If proposed names materially change after approval, obtain approval for those revised rows before applying them.

Use `rename_space_content` with `content_type: "document"` and the recorded document identifier, not name matching alone. Rename only the intended documents. If the tool returns a shared-document `confirmation_message`, explain the impact on other Spaces or links and obtain confirmation for that broader impact unless already explicitly authorized. Do not treat this response as a completed rename. After confirmation, retry the same change with `force: true`.

Verify resulting names with `list_space_content` in the affected folders. If a rename times out or its outcome is uncertain, inspect the current name before retrying. If an item changed since inspection, reassess instead of overwriting an unexpected name.

## Report results and boundaries

Report successful renames and failures separately, showing old and new names for successful changes. Separately identify skipped or unresolved items and why they remain unchanged. If no changes were needed, say so. Keep summaries concise and user friendly.

Do not move, delete, replace, or change access to documents as part of naming cleanup. Do not rename folders or sections unless separately requested. Discover current tool schemas and obey access checks; on `insufficient_scope`, ask the user to re-authenticate before retrying. Check text errors and structured responses before reporting success. Keep result fields named `id` or ending in `_id` internal. Do not call live write tools merely to test this skill.
