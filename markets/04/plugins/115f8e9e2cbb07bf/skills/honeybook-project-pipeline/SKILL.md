---
name: honeybook-project-pipeline
description: Review and analyze a HoneyBook project pipeline. Use for pipeline overviews, projects or leads by stage, active or archived project lists, custom pipeline filters, follow-up suggestions, and projects that may need attention. Do not use for general project details unrelated to pipeline position.
---

# HoneyBook Project Pipeline

Use HoneyBook's connected MCP tools to give the member a complete, accurate view of their pipeline.

## Default response contract

For an unqualified pipeline overview, render the following structure in GitHub-flavored Markdown. Replace placeholders with live data and do not wrap the response in a code fence.

```markdown
## Project pipeline

**{active} active projects** · **{lead} leads** · **{booked} booked

### Recently active

| Project | Stage | Date |
| --- | --- | --- |
| [Project name](project-url) — active today | Stage name | Project date |

### Projects by stage

| Stage | Projects |
| --- | ---: |
| Stage name | Count |

Ask me to expand any stage or show all projects.
```

Use Markdown headings, bold text, descriptive links, paragraphs, lists, and tables only. The default Projects by stage section is always a two-column count table. Show project rows by stage only after the member asks to expand a stage or show all projects.

## Workflow

1. Call `get_guidance` before choosing operations whenever the request depends on HoneyBook concepts such as lead, booked, archived, pipeline stage, or project versus workspace.
2. Call `find_action` with `readOnly: true` for the exact current operation signatures. Do not guess adapter methods or fields.
3. Use `take_action_read_only` for pipeline inspection. Keep related reads, pagination, filtering, and aggregation in one call.
4. Match the requested scope:
   - For an overview, use both `PipelineAdapter.getPipelineCounts` and `PipelineAdapter.listPipeline`. Counts provide the totals; entries provide recent activity, project dates, stage ages, and links.
   - For counts only, prefer `PipelineAdapter.getPipelineCounts`.
   - For project names or row-level details, use `PipelineAdapter.listPipeline` and retrieve every required page.
   - Default to active pipeline entries. Include archived or untracked entries only when requested or when essential to answer the question.
5. Apply filters in the API whenever supported. Do not fetch the full pipeline and filter locally when `stage_ids`, `view_id`, `group`, `category`, `tag_ids`, `project_type_ids`, `lead_source_ids`, `archived`, `untracked`, or `has_suggestion` can express the scope.
6. Verify completeness from returned pagination. If a deliberate limit is necessary, state the limit and that the result is partial.
7. Present the answer using the member's stage names. Preserve server-returned stage order for pipeline overviews; never impose a universal HoneyBook stage order.
8. Link every pipeline project name to its HoneyBook activity workspace. Build the member-facing URL from the exact IDs returned by `listPipeline`: `https://app.honeybook.com/app/event/{project_id}/workspace/{id}/activity`. Here `project_id` is the project ID and the pipeline entry's `id` is the workspace ID. Copy both IDs verbatim and URL-encode each path segment.

## Interpretation rules

- Treat a HoneyBook Project as the client job and its Workspace as the object carrying pipeline state.
- Determine lead versus booked from workspace status, not a stage name. Custom stage names are not reliable lifecycle signals.
- Use the pipeline stage to explain where work sits in the member's customized process.
- Distinguish active, archived, and untracked records. Never silently mix them.
- Treat `last_activity_at` as activity recency, not time spent in the current stage.
- Call a project "inactive" only when the response provides an activity timestamp and the relevant comparison window is explicit.
- When `current_stage.moved_at` is returned, use it to calculate time in the current stage. Keep it distinct from `last_activity_at`.
- Call a project "stuck in a stage" only when the user supplies a threshold or an established business rule defines one. Otherwise report neutral stage age, such as "in this stage for 18 days," without labeling it stuck.
- Treat `has_follow_up_suggestion` as a HoneyBook suggestion signal, not proof that the client is overdue or at risk.
- Do not infer project value, probability, revenue, conversion, or client intent from pipeline position.

For the underlying model and known adapter operations, read [references/pipeline-model.md](references/pipeline-model.md).

## Ambiguity and changes

- If a stage name could match more than one custom stage, retrieve the available stage data and ask the user to choose rather than guessing.
- If the user asks to move a project or change pipeline state, call `get_guidance` and `find_action` for that exact mutation. Proceed only if a supported write operation is returned and the target project and destination stage are unambiguous.
- A clear request to change one identified project is authorization for that exact change. Ask before acting when the project, workspace, destination, or scope is ambiguous.
- Use `take_action`, not the read-only runner, only for an explicitly requested supported change. Read its committed result before claiming success.
- If no supported pipeline-stage mutation exists, say so plainly and provide the requested read-only pipeline information when useful.

## Output

Lead with the result, then include only the detail needed for the request.

- Follow the Default response contract exactly for an unqualified overview.
- Include zero-count stages in configured order in the Projects by stage table.
- Do not place the stage-count table before Recently active. Do not repeat the totals in another table.
- Recently active contains up to six active, tracked projects with the newest `last_activity_at` values. After retrieving every required page, sort the eligible entries locally by parsed `last_activity_at` descending; do not assume the server-returned row order is correct. It is a recency shortcut, not a pipeline stage and not evidence that a project advanced.
- Exclude a closed or completed stage from Recently active only when structured stage metadata identifies it as closed, such as `system_key: _CLOSED_`; never infer completion from a customizable stage name alone. Skip entries without `last_activity_at`.
- In Recently active, keep the columns in the exact order Project, Stage, Date. In the Project cell, place relative activity after the linked name, for example `[O'Brien Fall Mini Session](...) — active 2 days ago`. Use `active today`, `active yesterday`, or `active N days ago` rather than `active 0 days ago`.
- In the Date cell, show the project date when present. When it is absent, show `No date set · {stage age}` when `current_stage.moved_at` is available; otherwise show `No date set`. Never substitute last activity for a project date.
- End the default overview with one short invitation such as: `Ask me to expand any stage or show all projects.`
- Surface one or two factual takeaways only when they are decision-useful, such as a large concentration in one stage, projects with a follow-up suggestion, or unusually old stage ages. Do not manufacture a warning tone.
- Do not list every project in the default overview. If the user asks to expand a stage or show every project, group the requested projects by stage and use a separate Markdown table under each stage heading. Keep each table's columns in the order `Project | Stage | Date`, adding another column only when it directly answers the request.
- Make each project name the primary link: `[Project name](https://app.honeybook.com/app/event/{project_id}/workspace/{id}/activity)`.
- Keep links descriptive. Do not use raw URLs or repeat a separate "Open" link in every row when the project name is already linked.
- Do not swap the two identifiers: `project_id` fills the `event` segment and `id` fills the `workspace` segment.
- If either ID is absent, show an unlinked name rather than emitting a partial or guessed route.
- For attention reviews, state the rule used, such as "no activity in 14 days," and separate facts from recommendations.
- Use a Markdown table when comparing multiple stages or projects.
- Say when a section has no matching projects.
- Omit empty-stage detail sections when expanding projects, after showing their zero counts in the overview table.
- Do not expose internal terms such as `Event` or `CoupleCard` unless they help answer a developer-facing question.
- Before sending the response, verify that Recently active precedes Projects by stage, the default stage section contains counts rather than project rows, and the response contains no angle-bracket markup.
