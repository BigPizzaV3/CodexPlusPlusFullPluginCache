---
name: gilmos-assets
description: "Prepare gilmOS character, location and prop assets; read or select reference versions; run native asset-image, description, panorama and character-sheet workflows. Use for persistent production references, not a free sandbox variation."
---

# Prepare and maintain production assets

Read the project and asset records before using names or versions. `gilmos_get_project` is bounded; paginate `gilmos_read_resources` on `assets` for a missing character, location or prop. Skip deleted records and distinguish a base asset from its variations. A moodboard/reference document is creative guidance, not automatically an attachable production asset.

Create explicitly requested assets with `gilmos_create_assets`: each asset has `name`, `type` (`character`, `location`, `other`), description and optionally prompt/characterRole. Character roles are `main`, `secondary`, `small_role`, `extra`, `voice_only`. This creates production records with an initial empty version, not reference images. Use `gilmos_create_style_palette` for a requested palette. For supplied public source images, `gilmos_import_asset_references` takes `payload.references` entries with `assetId` and `imageUrl`, plus source/rights/notes when known. The import service validates and downloads them; inspect both successful imports and failures. Do not fabricate URLs or infer that a storage path has been visually inspected.

## Reference versions and tags

Use `gilmos_read_asset_versions` to read the exact image version. The selected `current_version_id` represents the user's active choice; do not silently substitute the newest version. `gilmos_select_asset_version` changes that active choice using the actual `versionNumber` (1 is the first version). Simply using an older reference does not require changing the active choice: pass the exact `{assetId,versionId}` pair to an operation that accepts it.

Source generation prompts must include the canonical tag, for example `@ROZ` or `@ROZ/Winter`. Preserve the exact spelling, including the variation. A name in plain prose or only an asset ID does not replace the tag. Free generations use `gilmos_generate_media`, where gilmOS resolves selected visual versions and translates provider tags. Unknown/ambiguous tags or assets without images require resolving the reference before billable work. Explicit version pairs can disambiguate; read them first.

## Native asset production

- For descriptions of a selected set, call `gilmos_start_asset_description_workflow` once. Supply `resourceIds` and choose `onlyMissing=true` only when completing missing descriptions is intended.
- For reference images stored as **new asset versions**, use `gilmos_start_asset_image_workflow` with `resourceIds` or exact `resourceNames`. Keep the requested model, count/scope, resolution and instruction. Omitted selectors can cover all assets. Do not route this task to free sandbox generation, which has a different destination.
- For a panorama or character reference sheet, use `gilmos_run_sandbox_recipe` with its native `action` (`panorama` or `character_reference_sheet`). Do not recreate these recipes with an improvised free prompt. Set `output=asset_version` with the intended target asset, or `output=sandbox` when a sandbox item is requested; use verified `itemIds` or `assetVersions` when referencing existing media.

Track description/image workflows with `gilmos_get_alfred_workflow_status` and native recipe jobs with `gilmos_get_job`. Submission is not completion. An uncertain response requires checking `gilmos_list_jobs`/versions before starting another paid task. Stop a workflow only when requested, using `gilmos_stop_alfred_workflow`; already submitted provider work may still complete and be billed.

Read [examples.json](references/examples.json) for exact argument templates. After completion, reread the actual saved versions and show images with `gilmos_get_media(table="asset_versions", id=versionId)` when requested. Confirm the persisted destination and version, not just the launch.
