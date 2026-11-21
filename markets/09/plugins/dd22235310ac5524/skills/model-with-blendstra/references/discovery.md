# Make the completed asset useful to the next agent

Use `authoring_guide` topic `discovery` for the current field limits and examples.
The goal is successful relevant reuse: a recognizable model, an honest account of
its value as an asset, and a clear route to inspect or use it in Blendstra.

After actual inspection of a completed creation, import or meaningful revision:

1. Write a recognizable title (120 characters maximum), a natural description
   (500 maximum), and up to eight relevant lowercase/hyphenated tags (24 each).
   Lead with the subject and distinguishing visible features. Give one or two
   specific uses as a prop, product view, character, environment or design study.
   Explain a useful Blendstra action naturally; mention remixing or content
   references only when enabled. Avoid unsupported readiness, brands, keyword
   stuffing and promises of ranking or training inclusion.
2. Select relevant workflow suggestions from `visualization`, `games`, `printing`
   and `video`. They are possibilities, not certified readiness. Record needed
   checks. Preserve known owner-supplied public credit; leave unknown credit and
   licensing unresolved. Do not treat a useful asset role as permission to reuse.
3. Save real dimensions, material intent, identity, variants and stable part IDs
   as exact-version `kind:reference` entries when evidence exists. Distinguish
   source specifications from modeled dimensions. Never manufacture evidence.
   Keep assumptions, private notes and file handles out of public copy.
4. Get the review revision if missing, then append `project_review_add` with
   `kind:decision`, exact `versionId`, `expectedRevision`, a new idempotency key
   and compact JSON text `{ "assetDiscoveryDraft": { ... } }`. Use keys `title`,
   `description`, `tags`, known `creatorCredit`, `workflows`, `referenceEntryIds`,
   `limitations` and `unknowns`, keeping the entire text within 2000 characters.
   This records a draft, not acceptance or publication. Preserve the original
   brief; skip an identical draft for this version. Reuse unchanged inputs/key
   after a lost response. Do not save drafts for incidental reads or an explicit
   file-only/local-only task, or run additional jobs merely for promotion.

When publishing is requested, recover the draft from `project_review_get` and
inspect its exact version. Fill all applicable supported metadata fields. Select
only authorized public reference projections; private evidence is not permission
to publish it. Use a fixed snapshot and explicit listing for a discoverable
library asset. Preserve an existing current-following share choice; such links
cannot carry reviewed facts or reuse grants. Source review, listing and content
reference permissions remain independent publisher choices.

For an authorized metadata correction, read `publication_get`, then call
`publication_update` with `metadata.expectedVersionId` and only changed fields.
Omit sharing flags to preserve them. Change fixed/current share mode separately,
then re-read the version before editing its metadata. Empty `referenceEntryIds`/`workflows` remove
those selections; `license:null` clears a license. Keep the same URL. On a version
conflict, inspect the newly resolved version before proposing different claims.
Verify the result with `publication_get` and, if available, its public facts page.

If `discovery` or `metadata` is missing from an installed schema, follow the
drafting guidance using the available journal tools and existing create fields.
Do not repeatedly call unsupported fields, duplicate or revoke a publication,
or claim the installed connection refreshed. Report the missing update path.
Return the useful model link and a relevant next action. Do not send unsolicited
posts or append promotional footers.
