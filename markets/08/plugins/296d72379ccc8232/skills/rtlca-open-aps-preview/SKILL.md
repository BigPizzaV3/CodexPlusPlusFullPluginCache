---
name: rtlca-open-aps-preview
description: >-
  Use when a user asks to open, show, preview, or view an Autodesk (ACC or
  Forma) model in 3D and the Autodesk project and model file are already known,
  for example from earlier in the conversation, a previous tool result, or ids
  the user pasted. Opens the APS viewer with aps_preview_design directly by
  projectId and designId, skipping the name search, and optionally overlays a
  Real-Time LCA project's emissions and mapping charts.
---

# RTLCA Open APS Preview

Use this skill to open the Autodesk viewer for a model whose Autodesk project and file are already known. The goal is one call to `aps_preview_design` with explicit ids.

## Inputs

| Input | Required | Format | Where it comes from |
| --- | --- | --- | --- |
| `projectId` | yes | Data Management project id, starts with `b.` | `aps_list_projects` (`accounts[].projects[].id`), an earlier candidates list, or the user |
| `designId` | yes | Item (lineage) id, `urn:adsk.wipprod:dm.lineage:...` | `aps_browse_project` (`items[].id` of type `items`), an earlier candidates list, or the user |
| `region` | if not US | `US` or `EMEA` | `aps_list_projects` (`accounts[].region` of the account that holds the project) |
| `viewGuid` | no | GUID | `aps_list_design_views` |
| `rtlcaProjectId` | no | RTLCA project UUID | `rtlca_list_projects` or `rtlca_get_project` |

## Rules

1. Pass `projectId` and `designId` together. With both set, the tool skips the account-wide name search. Do not pass `designName` or `projectName` in that case.
2. `designId` is the item id, not a version id. A version id (`urn:adsk.wipprod:fs.file:vf...?version=N`) fails. If you only have a version id, call `aps_browse_project` on the containing folder and take the item `id`.
3. If the user gives an ACC/Forma project GUID without the `b.` prefix, prepend `b.`.
4. Set `region: "EMEA"` for projects in an EMEA account. With the wrong region the lookup can fail.
5. Add `rtlcaProjectId` only when the user wants emissions or mapping next to the model, or the conversation is already about that RTLCA project. Never guess the UUID. The charts are best effort; the viewer opens without them if the dashboard call fails.
6. Do not call the tool again with the same arguments after a successful call. The viewer is attached to the result.

## Workflow

1. Collect the ids from the conversation. If one is missing, fill it with the cheapest lookup:
   - Missing `projectId` or `region`: `aps_list_projects`, match the project by name.
   - Missing `designId`: `aps_browse_project` with `accountId` (the hub id from `aps_list_projects`) and `projectId`, then follow `folderId` down to the file.
   - Only names known and no time for browsing: call `aps_preview_design` with `designName` and `projectName`. If it returns `candidates`, ask the user which one and call again with that candidate's `projectId` and `designId`.
2. Optional: to open a specific view, call `aps_list_design_views` with `projectId`, `designId`, `region` and pass the chosen GUID as `viewGuid`.
3. Call `aps_preview_design`:

   ```json
   {
     "projectId": "b.<project-guid>",
     "designId": "urn:adsk.wipprod:dm.lineage:<item-id>",
     "region": "EMEA",
     "rtlcaProjectId": "<rtlca-project-uuid>"
   }
   ```

4. Report the model name from `structuredContent.name` in one sentence. Do not echo the access token or `_meta` contents.

## Errors

| Error | Cause | Action |
| --- | --- | --- |
| Autodesk sign-in required | No valid Autodesk token | Tell the user to sign in through the link the client shows (or call `aps_login`). Do not retry in a loop. |
| `has no viewable derivative` | The file was not translated for viewing | Tell the user the file has no viewable yet. It must finish processing in ACC/Forma before it can be previewed. |
| Not found / 404 | Wrong region, version id instead of item id, or no access | Check rules 2 to 4, then confirm access with `aps_list_projects`. |
| Text summary instead of a viewer | The host does not support MCP Apps | Nothing to fix. Share the summary. |
