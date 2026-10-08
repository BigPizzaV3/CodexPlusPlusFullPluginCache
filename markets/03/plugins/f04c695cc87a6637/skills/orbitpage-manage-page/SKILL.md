---
name: orbitpage-manage-page
description: "Review, preview, edit, publish, and restore the OAuth-connected OrbitPage page. Use when a user asks to inspect their workspace or page, check publication status or plan capabilities, propose page changes, apply an approved preview, publish an exact revision, or restore a retained version."
---

# Manage an OrbitPage page

Operate only on the workspace connected through OrbitPage OAuth. Use the MCP tools for live state and controlled changes; never infer page contents, permissions, revisions, or publication state.

## Choose the workflow

- For workspace identity or publication questions, call `get_workspace` and `get_publication_status`.
- For page-content questions, call `get_page`. Call `get_page_capabilities` before recommending edits whose availability may depend on role or plan.
- For requested edits, follow the preview, approval, apply, and optional publish sequence below.
- For rollback requests, follow the version-restore sequence below.
- Do not activate for unrelated calendar, messaging, image-generation, domain-purchase, DNS, billing, or general web-development requests.

## Read current state

1. Call only the minimum read tools needed.
2. Treat returned public URLs, revision numbers, permissions, limits, and content as authoritative.
3. Report whether the draft is published, has unpublished changes, or is still awaiting publication.
4. Do not expose OAuth tokens, credentials, internal identifiers, or debug payloads.

## Preview and apply changes

1. Call `get_page` for every section the request may affect.
2. Call `get_page_capabilities` when the requested fields, block types, or limits may depend on the connected plan or role.
3. Preserve all unspecified content. Do not silently rewrite links, theme, menu, subpages, consent settings, or text files.
4. Call `preview_page_changes` and retain its preview token, expected draft revision, and expiry exactly as returned.
5. Show a concise proposal with the affected fields and make clear that neither the draft nor the public page has changed.
6. Stop for explicit approval. Do not interpret silence, a topic change, or an earlier general request as approval of the displayed proposal.
7. After approval, call `apply_page_changes` with the exact preview token and expected revision. Set `publish=false` so the approved result is saved as a private draft.
8. Report the saved draft revision and whether it differs from the published revision.
9. If the preview expired or the revision changed, read the current page again and create a new preview. Never force or reconstruct a stale mutation.

## Publish safely

1. Publish only after the user explicitly confirms that the saved revision should become public.
2. Call `publish_page` with the exact saved revision as the expected revision.
3. Call `get_publication_status` after publishing.
4. Confirm the public URL, draft revision, published revision, and whether unpublished changes remain.
5. If publication is pending, say so without claiming the public page is already current.

## Restore a retained version

1. Call `list_page_versions` and summarize the available retained versions without choosing one for the user.
2. Ask the user to select a specific version and explicitly confirm restoration.
3. Call `restore_page_version` only for the selected version and use the current expected draft revision when available.
4. Keep the restored result private. Never publish a restored version automatically.
5. Report the new draft revision and make clear that the public page remains unchanged until separately confirmed and published.

## Response requirements

- Distinguish clearly between a proposal, a saved private draft, a pending publication, and a completed publication.
- State the affected sections and preserve information the tools did not return.
- Use the connected workspace only; do not ask the user for tenant IDs, page IDs, OAuth tokens, or passwords.
- Ask a focused clarification when the target content or requested outcome is ambiguous.
- Decline unsupported actions and explain the nearest supported OrbitPage workflow without invoking unrelated tools.
