# HoneyBook pipeline model

Read this reference when selecting pipeline operations or interpreting lifecycle state.

## Entities

- A member-facing **Project** is internally an `Event`.
- A **Workspace** is internally a `CoupleCard` and belongs to a project.
- Pipeline state, tasks, messages, and meetings attach to the workspace rather than directly to the project.
- A project can have more than one workspace. Do not assume a project ID and workspace ID are interchangeable.

## Lifecycle versus pipeline position

Use workspace status as the reliable lead/booked signal:

| Workspace status | Meaning |
| --- | --- |
| `lead` | Lead, not booked |
| `lead_sent` | Lead with a file sent, not booked |
| `client` | Booked |
| `client_archived` | Booked and archived |
| `lead_archived` | Archived or dead lead |

Pipeline stages are company-customizable. Their category can be `lead`, `booked`, or `other`; their group can be `opportunities` or `projects`. Stage names supplement workspace status but do not replace it.

## Known read operations

Always confirm current signatures with `find_action` before execution.

### Pipeline summary

`PipelineAdapter` from `@honeybook/sdk/pipeline` provides `getPipelineCounts` for active, archived, and untracked totals plus category and stage counts. Use it when the user needs aggregate pipeline shape rather than project rows.

Supported filters include team member, custom view, group, category, tag, project type, lead source, and follow-up-suggestion presence.

### Pipeline entries

`PipelineAdapter.listPipeline` returns workspaces by stage with pagination. It supports up to 100 records per page and filters for stage, view, group, category, tags, project types, lead sources, archived state, untracked state, and follow-up suggestions.

Useful returned fields include:

- workspace entry ID
- project ID and name
- project date and end date
- project location and type
- current stage
- active and tracked flags
- tags and member count
- follow-up-suggestion presence
- current-stage movement timestamp (`current_stage.moved_at`), when present
- last activity and creation timestamps

Build the canonical member-facing activity URL from a pipeline entry as follows:

```text
https://app.honeybook.com/app/event/{project_id}/workspace/{id}/activity
```

- `project_id` is the Project/Event ID.
- The pipeline entry's `id` is the Workspace ID.
- Copy both opaque IDs exactly and URL-encode each path segment.
- Link the project name rather than displaying the raw URL.
- Do not create the URL if either identifier is missing.

Supported sorting includes stage movement, project date, name, last activity, creation date, stage, project type, and lead source. Calculate time in stage from `current_stage.moved_at` only when that field is present. Do not substitute `created_at` or `last_activity_at` for it.

### Project lookup

`ProjectsAdapter.listProjects` can search by project name and optionally include workspaces. Use it when a user names a project and the pipeline entry alone cannot resolve the intended project or workspace.

## Completeness

List responses return `data` and `pagination`. Use `total_pages` or `last_page` to retrieve all pages required by the request within one `take_action_read_only` call. A page of 100 is not proof that the pipeline contains only 100 records.
