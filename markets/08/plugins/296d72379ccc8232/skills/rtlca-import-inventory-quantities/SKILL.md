---
name: rtlca-import-inventory-quantities
description: >-
  Use when a user asks to insert, import, add, or load material quantities into
  an RTLCA project inventory from a file, spreadsheet, CSV, pasted table, or
  screenshot (quantity takeoff, standard values list, manual bill of
  materials). Parses rows into name, group, quantity, unit, count, lifetime and
  include flag, resolves declared units, skips duplicates, confirms the batch
  with the user, creates the materials with rtlca_create_inventory_materials in
  one call, and verifies them with rtlca_get_inventory_materials.
---

# RTLCA Import Inventory Quantities

Use this skill to turn a quantity table into RTLCA project inventory materials. It creates inventory rows only. It does not map them to EPDs. For mapping, use the `rtlca-map-material` skill afterwards.

`rtlca_create_inventory_materials` is not idempotent. Calling it twice creates duplicates. Confirm the batch with the user, call it once, and verify.

## Inputs

| Input | Required | Where it comes from |
| --- | --- | --- |
| RTLCA `projectId` | yes | The conversation, or `rtlca_list_projects` matched by name |
| The table | yes | ACC/Forma file (see Reading a File from ACC/Forma), uploaded file, pasted text, or screenshot |
| `branchName` | yes | Ask the user. Suggest the file name without extension, or `Manual`. Use one value for all rows of one file. |

## Reading a File from ACC/Forma

Do not browse folders to find the file. If the user has not given the file, ask for its ACC/Forma link first.

From a link such as `https://acc.autodesk.com/build/files/projects/<guid>?folderUrn=...&entityId=<urn>`:

- `projectId` = `b.` + `<guid>`
- `itemId` = `entityId`, URL-decoded (`urn:adsk.wipprod:dm.lineage:...`)
- Ignore `folderUrn`, `viewModel`, `moduleId`, `viewableGuid`.

Then read the file in exactly two calls:

1. `aps_read_file` with `projectId`, `itemId` (default `detail: "summary"`). Take the sheet name and `rowCount`. The summary holds only 5 sample rows. Never build entries from it.
2. `aps_read_file` with `detail: "rows"` and that `sheet`. This returns up to 500 rows.

## Column Mapping

Typical layout (the header row is often missing):

| Column | Example | Maps to |
| --- | --- | --- |
| Name | `Bundplade (Generic FundamentBundplade)` | `materialIdentifier` (full text as written) |
| Group | `Fundament` | `typeIdentifier`. If empty, use the name without the parenthesis part (`Afløb (StandardværdierAfløb)` gives `Afløb`). |
| Quantity | `2,096.36` | `declaredUnitValuePairs[0].value` |
| Unit | `m²` | `declaredUnitValuePairs[0].declaredUnit` (enum, see Units) |
| Count | `8` | `materialCount` |
| Lifetime | `50` | `lifetime` (years) |
| Include | `Yes` | Create the row only when `Yes`. List the skipped rows in the summary. |

If headers exist, use them. If they do not, show the assumed mapping to the user in the confirmation step. Never guess silently between count and lifetime.

## Rules

1. Numbers: detect the separator style per file. `10,154.00` is 10154 (comma for thousands). `10.154,00` is 10154 (Danish style). Never round.
2. Units: call `rtlca_get_reference_data` with `type: "declared-units"` once. Map `m²`/`m2` to M2, `m³`/`m3` to M3, `m`/`lbm` to M, `kg` to KG, `t`/`ton` to T, `stk`/`pcs` to PCS. Set `preferred: true`. Stop and ask on any unit without a match.
3. Skip rows with quantity 0 or empty, and report them.
4. Required fields on every entry: `includeMapping: true`, `tags: []`, `speckleUserParameters: {}`.
5. Duplicates: before writing, call `rtlca_get_inventory_materials` with `model: [branchName]` and `detail: "detailed"` (limit 200, follow `nextOffset`). A row is a duplicate when `identifier` and `typeIdentifier` both match. Ask the user whether to skip it or create it anyway. To change an existing row, use `rtlca_update_material_properties` instead.
6. Never call `rtlca_create_inventory_materials` before the user approves the exact list.
7. Row count check: the number of entries must equal the number of included rows in the file minus the skipped rows. If it differs, stop and list the missing rows.
8. Call `rtlca_create_inventory_materials` at most once per file. If it fails, read the inventory before any second call and send only the missing rows.

## Workflow

1. Resolve the RTLCA project and `branchName`.
2. Parse the table into rows. Apply Rules 1 to 3.
3. Resolve units (Rule 2) and check duplicates (Rule 5).
4. Show the user a compact table: name, group, quantity, unit, count, lifetime, plus the skipped and duplicate rows with the reason. Ask for approval.
5. Call `rtlca_create_inventory_materials` once with all approved rows:

   ```json
   {
     "projectId": "<rtlca-project-uuid>",
     "entries": [
       {
         "branchName": "Standardværdier",
         "typeIdentifier": "Fundament",
         "materialIdentifier": "Bundplade (Generic FundamentBundplade)",
         "includeMapping": true,
         "lifetime": 50,
         "materialCount": 8,
         "declaredUnitValuePairs": [{ "declaredUnit": <M2 enum>, "value": 2096.36, "preferred": true }],
         "tags": [],
         "speckleUserParameters": {}
       }
     ]
   }
   ```

6. Verify: call `rtlca_get_inventory_materials` with `model: [branchName]` and `detail: "detailed"`. Check each approved row exists once with the right quantity, unit and lifetime. Do not retry the create call for rows that exist.
7. Report: created count, skipped rows with reasons, any mismatch. Offer to map the new materials with `rtlca-map-material`.

## Errors

| Error | Action |
| --- | --- |
| Not authenticated | Tell the user to reconnect the Real-Time LCA connector. Do not retry in a loop. |
| Validation error on a field | Fix the named entry and resend only the entries missing after a verify read. |
| Create call times out or returns no data | Verify with `rtlca_get_inventory_materials` before any retry. The rows may exist already. |
