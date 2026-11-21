---
name: business-profile
description: Read and update the existing Reteno Business Profile using user-provided business information, files, logos or explicitly identified account emails. Preserve omitted fields and verify saved changes. Supports brand voice, languages, colors, fonts, links and business facts. Does not crawl websites or extract a profile from a site.
---

# Business Profile updates

Use only the selected authenticated Reteno MCP connection. Read `get_business_profile` first
and retain its `orgId` and complete normalized `brandkit` as the baseline. Derive updates from
the user's supplied information/files or explicitly selected account emails. Existing saved
values remain evidence. Do not browse a website or run website extraction for this skill.

1. Identify requested fields and evidence. Omitted means preserve. Empty strings, empty arrays
   and null are explicit changes, never placeholders for unknown values. Arrays replace in full;
   retain existing entries unless removal was requested. Show material inferred changes before
   writing when the user's intent is ambiguous, and continue directly for explicit updates.
2. Build a partial profile document using the live contract. It must include `brand: {}` even
   for top-level changes. Use `scripts/profile_update.py prepare` to reject accidental clears
   and create a merge preview. The helper validates scope, not the entire server schema.
3. For fields supported by the advertised patch schema, use `patch_business_profile(patch=...)`.
   For other updates use `prepare_business_profile_upload(operation="profile_update")`, upload
   JSON with `<plugin-root>/scripts/transfer.py`, and call
   `save_business_profile(uploadSessionId=..., operation="profile_update")` with no website
   argument. Require an error-free receipt identifying the same organization.
4. Read `get_business_profile` again. Verify requested changes and preservation of omitted
   fields against the baseline/merge preview. Report normalization warnings or unavailable
   read-back instead of claiming full success. Keep receipts; inspect after an ambiguous save
   before any retry. Never repeat a full replacement to recover a patch.

When changing an existing language pair, update both `languages` and
`brand.brandVoice.defaultLanguages` together. Unknown languages are omitted, not `[]`.
Null is not omission: blankable strings may become empty, some lists may clear, and typed
collections such as logos reject null. Stored invalid `importantLinks` rows may be dropped by
server read normalization; report that behavior if relevant. Open extension fields are preserved.

For supplied logos, read [the host image workflow](../email-model-editor/HOST.md). Host original
bytes with `prepare_image_upload` / `upload_image(purpose="logo")`, inspect the final converted
asset, and reuse the exact returned URL. Uploading a logo does not itself update the profile.
Never invent brand facts, URLs or legal text. This plugin never calls `extraction_replace`,
`replace_business_profile_from_extraction`, Browserbase or website brand extraction helpers.

```sh
python3 <skill-dir>/scripts/profile_update.py prepare \
  --current <get-business-profile.json> --changes <partial-profile.json> \
  --organization-id <id> --output <upload.json> --expected <merged-preview.json>
# For a requested clear only, add --clear /brand/organization/description (JSON Pointer).
python3 <skill-dir>/scripts/profile_update.py verify \
  --current <fresh-get-business-profile.json> --expected <merged-preview.json> --organization-id <id>
```
