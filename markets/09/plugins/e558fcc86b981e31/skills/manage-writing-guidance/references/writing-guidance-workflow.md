# Writing guidance: safe updates and inheritance

## Retrieve and target

Read the current published company or voice context immediately before preparing a change. Use stable target IDs and the returned metadata; duplicate names need clarification. For a new person, use a unique `target_profile_client_ref` until the reviewed apply returns a stable ID. A linked user is optional, and must resolve to active membership when requested. Do not invent personal facts.

Person context is composed from company and person entries. Only person-owned entries may be submitted as the person’s mutable snapshot. Filter by returned ownership/source_scope; inherited company items are context, never person-owned replacements. Existing company requirements cannot be suppressed by personal overrides.

## Propose and apply

Use `propose_company_writing_guide_update` or `propose_voice_writing_guide_update` with the public structured profile/items contract. Omitted fields preserve their existing value; explicit null/empty values can clear content. Omit unrequested profile fields rather than reconstructing them with empty strings.

When submitting `items`, preserve all existing target-owned items exactly except intended changes; a supplied array is a snapshot, not an append operation. Exclude computed read metadata from editable fields. Use tool-supported selection to limit apply scope when needed: explicit empty item/removal arrays mean no selected item changes, not full replacement. Selection ordering and scope must agree with preview. Do not invent a raw operations API.

For inspirations, reuse the catalog identity and returned author/style snapshot, selected qualities, blend mode and channel scope. Follow the service’s validated blend schema, not an anonymous text-only replacement. Unrequested channels remain intact. Resetting a personal blend to company inheritance removes only the applicable personal inspiration adjustment, never company requirements or unrelated personal refinements.

Inspect the immutable preview: correct company/person, intended item/profile changes, no incidental deletion, renaming, summary clearing or reorder. If it differs, stop and explain; do not apply a plausible approximation. Present the changes and obtain review approval. Apply via the matching company/person tool with returned `proposal_id`, `preview_hash`, and `confirmed=true`. Read the published guide back and report actual revisions. Preserve private drafts/chat; never reset them to make an update pass.

If stale, expired or conflicting, retrieve fresh context and ask for a new review as appropriate. Do not reuse a mismatched hash, invent a conflict acknowledgment or silently retry to force success. Respect server idempotency; after uncertain completion, read/replay the same operation rather than create a duplicate.

## Shared history and restore

Use `get_brand_writing_history` for the resolved target and actual change detail. Call `propose_brand_writing_restore` with that `change_id`, explicit restore scope and the entire freshly retrieved `saved.versions` object, including company/person/foundation values returned by the service. Do not send only the top-level revision. Restore scope uses the tool’s item_ids/remove_item_ids/profile_fields meaning; review the actual preview rather than infer operation direction from an ID alone.

A selective restore creates a new revision, preserving unrelated later edits. `restore_noop` means no change, not failure requiring a broader scope. Conflicts need explicit review of the bound server-returned acknowledgment; never auto-acknowledge. Apply the restore through the existing target-specific apply tool after approval, then read back guidance/history. Do not claim to restore private chat or whole historical database state.

## Archive lifecycle

Only act on explicit archive/unarchive intent and a stable named-voice ID. `archive_named_voice` / `unarchive_named_voice` create reviewed lifecycle proposals; inspect them, then use the existing voice apply tool after approval. Preserve the voice content, draft/chat and shared history. An archived target is unavailable for normal context retrieval; use explicit lifecycle listings for management. Do not delete and recreate a voice to simulate archive or restore.

## Samples and privacy

A generated passage in the current AI chat is a draft, not a saved shared guide example or saved BuyerTwin private sample. The public tools do not expose in-app private chat/sample controls. Save a generated example only on explicit request through a new reviewed guide proposal. Preserve its illustrative/source status and attribution; permission to save it does not establish author approval. Public context, exports and history must exclude private transcripts, editing sessions, pending proposals and unsaved private samples.
