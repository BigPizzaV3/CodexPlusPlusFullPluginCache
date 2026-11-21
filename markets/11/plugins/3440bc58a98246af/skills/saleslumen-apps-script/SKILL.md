---
name: saleslumen-apps-script
description: >-
  Author Saleslumen Apps Script projects via MCP: projects, file content,
  versions, deployments, metrics, and process history. Use when the user wants
  to create or edit a script project, cut a version, or manage a deployment.
  Do not use for inbox email, campaign enrollment, or running a function.
---

# Saleslumen Apps Script

Use the Saleslumen MCP connector to author Script projects. Keep the conversation natural; read and update project files with tools.

## Concepts

A project is identified by `script_id`. Content version `0` is the editable draft. Positive version numbers are immutable snapshots.

Content is a full file set (`SERVER_JS`, `HTML`, `JSON`), including `appsscript.json` for runtime, timezone, libraries, and `enabledServices`.

A deployment points at a numbered version (not draft `0`).

Processes are the user-facing run history. Use them to answer whether a past run finished.

This plugin does not run a script function, fetch callable contracts, or call a Marketplace operation. Author the project here. Execution stays in Saleslumen.

## Workflow

1. Clarify the goal (create, edit, version, deploy, metrics, or process history).
2. Read the project and `apps_script_get_content` before you overwrite files.
3. Ship with update content, then create version, then create or update deployment.
4. Confirm with the user before content replace and delete.
5. Report the project, version, or deployment that changed.

## Tools

| Task | Tools |
| --- | --- |
| Projects | `apps_script_list_projects`, `apps_script_create_project`, `apps_script_get_project`, `apps_script_update_project`, `apps_script_delete_project` |
| Content | `apps_script_get_content`, `apps_script_update_content` |
| Metrics | `apps_script_get_metrics` |
| Versions | `apps_script_create_version`, `apps_script_get_version`, `apps_script_list_versions` |
| Deployments | `apps_script_create_deployment`, `apps_script_get_deployment`, `apps_script_update_deployment`, `apps_script_delete_deployment`, `apps_script_list_deployments` |
| Processes | `apps_script_list_processes`, `apps_script_list_script_processes` |

## Guidance

- `apps_script_update_content` replaces the whole file set and requires `draft_etag` from `apps_script_get_content`. Send every intended file.
- Deploy only numbered versions.
- Stay in the Apps Script tools for this skill.
