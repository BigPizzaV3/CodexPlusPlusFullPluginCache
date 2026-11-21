---
name: docsend-build-data-room
description: Create and organize a DocSend data room for fundraising, M&A, due diligence, or another document-sharing workflow. Use for setting up Spaces, organizing materials into meaningful folders, improving file names, and identifying potential content gaps.
---

# Build a DocSend Data Room

Example: “Build a fundraising data room using these documents.”

Use the DocSend MCP. Discover current schemas before acting; use supported workflows and obey tool approval requirements. This skill builds and reviews rooms; creating the skill itself does not authorize live DocSend mutations.

## Establish purpose and sources

Identify the deal purpose, desired Space name, source materials, and requested structure from context. Ask only for information needed for the requested actions. A request to build a room authorizes its Space and folders, but does not authorize external access.

Use `list_spaces` when needed to identify an existing Space the user refers to or reconcile an uncertain creation result. Inspect existing links/groups before adding materials to an existing room, since visitors may already have access.

Use supplied materials or locate documents with `search_documents` and `list_content_library`. The Content Library is separate from Space content. Inspect rooms with `list_space_content`, starting with the returned `home_folder_id`; inspect relevant subfolders and pagination.

Inspect accessible contents when names alone are insufficient. Call `read_document` once without `page`, prefer downloading its `file_url` exactly once, and analyze the full file locally. Use page requests only for a specific-page question or when the file URL is unavailable. Keep inaccessible materials distinct from missing documents.

## Build and organize

Follow the user's requested structure when provided. Otherwise develop meaningful, shallow folders based on the deal purpose and available materials.

Create the Space and folders with `create_space` and `create_space_folder` within the authorized scope. Preserve user-provided Space names and descriptions exactly; ask for a shorter value if rejected by length limits. Leave questions and unrelated settings unchanged unless requested. Inspect state before retrying an uncertain creation result.

If an appropriate company logo or banner image is available, upload it to supported Space logo/banner fields. The current MCP has no branding-image update fields: leave them unchanged and report the limitation unless new tools support them. Do not add branding images as substitute room documents.

Add available materials to the data room using the DocSend MCP upload workflow below and verify that documents appear in their destination folders. Currently there is no direct Content Library-to-Space add/copy operation. `move_space_content` only moves content within one Space. When exact source bytes are accessible, use the upload workflow below; otherwise report the materials that require manual addition. Finding or reading a Library document does not add it to a room.

Organize by subject and purpose. Avoid a generic catch-all folder and unnecessary depth. Do not guess a document's purpose: clarify unresolved placements and report them. Use `move_space_content` for existing content, batching only items with the same source parent. Verify destinations after moves and additions.

### Upload preparation and completion

1. Obtain exact file bytes and metadata. Before `request_space_upload`, show the exact Space/folder destination and each file's `original_name` and `size_bytes`, explain that uploaded content is visible to Space visitors, and ask the user to approve those uploads, as required by the upload tools. This approval covers finalization for the unchanged file and destination; changes require updated details, confirmation, and a fresh target.
2. Call `request_space_upload`. This prepares a presigned target; it does not transfer bytes or add a document.
3. Keep each response paired with its matching file. Build a multipart POST containing every returned `upload_body_params` property exactly once as text, preserving names, case, and values byte-for-byte. Do not decode/re-encode them. Let the HTTP library generate the multipart Content-Type header and boundary; the returned Content-Type is a signed form field. Append the matching file last as `file` and POST to `upload_url` before `expires_at`.
4. Only HTTP 201 permits finalization. For expiry, non-201, or unknown transfer outcome, do not finalize; request a fresh target if continuing. If byte transfer is unavailable, report that preparation is incomplete work.
5. After HTTP 201, call `upload_file_to_space` using the unchanged `upload_key`, destination, and identical original name, MIME type, and size. Finalization is not idempotent: inspect the destination before retrying an uncertain result to avoid duplicates.
6. Immediately check the destination with `list_space_content`. For PENDING, wait about 10 seconds and check again; if still PENDING, wait about 20 seconds and check once more. Stop after three checks total and report ongoing processing. SUCCESS confirms processing, not an available AI summary; ERROR indicates processing failure. Distinguish prepared, transferred, added, and processed materials in the result.

After verifying uploads, confirm completion with the document names grouped under their destination folders so the user can review both the materials and folder structure. Keep this confirmation user friendly: omit byte counts, MIME types, upload keys, processing codes, internal identifiers, and transport details. Describe pending processing or failures in plain language. Keep exact technical metadata in tool calls and any disclosure explicitly required for upload approval, rather than repeating it in completion summaries.

## Names and potential gaps

Once the Space is created and its available materials are organized, proactively review file names for clarity and consistency without waiting for a separate request. Suggest content-supported replacements for ambiguous names such as “Document 1,” “Scan,” or “Final v2.” Do not invent dates, versions, or approval status. Ask whether to apply suggestions unless renaming was already authorized. Use `rename_space_content` for approved changes and verify them. If a shared-document confirmation is returned, explain its cross-Space/link impact and confirm that impact before retrying with `force: true`.

Next, if applicable, proactively assess potential content gaps against deal purpose, stage, user context, and reviewed materials without waiting for a separate request. Distinguish “appears missing from reviewed materials” from “could not inspect.” Explain why each proposed addition may be useful; do not present a generic checklist as mandatory. The structure and gap assessment are organizational guidance, not a statement that the room satisfies every diligence requirement. Do not create placeholder documents or represent suggested materials as existing.

## Setup summary

Return a concise summary containing:

- Space name, verified admin URL, and folder structure. Use the Space URL returned by DocSend; never construct one from an internal identifier. Report if an admin URL is unavailable.
- Added materials and destination folders, including processing still underway.
- Suggested or completed name improvements.
- Potentially missing materials and their relevance, separately identifying inaccessible materials.
- Unresolved placements and actions that could not be completed, including unsupported branding or content operations.

Once organization, the proactive file-name review, and any applicable gap assessment are complete, ask whether the user is ready to share the Space. If sharing was already authorized, proceed within that authorization; if the user requested a private room, respect that preference. Creating a room alone never authorizes granting external access.

## Sharing and visits

Configure sharing/access only when requested. Links and groups are the Space's access methods. Groups grant external visitor access; they are not internal collaborators.

For a shareable URL, use `create_space_link` with supported settings matching the user's instructions. Name new links recognizably, such as the intended company/person or a readable creation date/time in the user's timezone. Ask only for missing consequential access choices. Return the link URL and summarize its effective settings in plain language: whether downloads are enabled, whether an email is required, whether that email must be verified, whether screenshot protection is enabled and at what level (including mobile protection when reported), and any configured expiration, watermark, or access restrictions. Distinguish email collection from verification. Describe screenshot protection settings without promising that all screenshots are impossible. Identify any requested setting not applied or setting that could not be confirmed; do not guess defaults.

If the user explicitly wants DocSend to send invitations, create a named group with `create_space_group` rather than a regular link. Use only authorized recipients and invitation text. After a successful invitation operation for the specified recipients, tell the user the invite has been sent. Do not add caveats about email deliverability. If the operation fails or does not invite anyone, report that action accurately rather than claiming an invite was sent.

Check `list_space_permissions` before modifying existing access. Follow explicit confirmation requirements for link updates and visibility changes. For group updates, show the before/after state, every email added/removed, exact invitation message, and setting changes; obtain confirmation before calling `update_space_group`. Email removals must be separate from other changes. Stop on group capacity errors; do not retry smaller batches.

Current tools do not configure NDA settings; links also lack passcode/media-playback controls. Direct users to the admin page for unsupported settings. Group screenshot protection requires a subsequent update: do not claim it exists at creation or invite recipients before resolving protection required to precede access.

Retrieve available visits using `list_visits` scoped to the Space, following pagination. Attribute activity to a particular link/group only when returned evidence supports it; do not label room-wide activity as recipient-specific. Omit `contact_id` except for a specific visitor resolved with `search_contacts`. Summarize visitor identity, dates, documents, and relevant engagement with correct units. No recorded visits does not prove non-delivery.

Retrieve visits when available during the task or on follow-up; do not imply a subscription to future events. If the user requests ongoing monitoring, use supported scheduling tools when available; otherwise explain the limitation.

## Tool handling

On `insufficient_scope`, ask the user to re-authenticate before retrying. Check structured responses and text errors before reporting success. Keep all values named `id` or ending in `_id` internal, including in displayed links and summaries. Identify items by names, returned URLs, emails, or dates. Do not call live write tools merely to test this skill.
