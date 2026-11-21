---
name: build-edit-workflows
description: Create and edit reusable Manifestly workflow templates, including sections, steps, instructions, data fields, subtasks, ordering, and due-date rules. Use for designing a repeatable process, changing future runs, or copying a template. Excludes starting runs, completing run steps, and changing individual run assignments or deadlines.
---

# Build and edit workflows

A workflow is the reusable template. A run is one execution with its own copied steps. Use this skill to create or change the template; use run operations for work in a specific execution.

Follow the user's explicit scope and preferences over this skill's defaults. When the user asks for an outline or advice, provide that without creating records. When they request creation or a clear supported edit, carry it out without adding a routine approval step.

## Identify the target and scope

Use the account established by the user and resolve the department with `list_departments` when needed. Discover existing templates with `list_workflows` and inspect the chosen one with `get_workflow`; fetch its steps with `list_workflow_steps` using `mode: "hierarchy"`. The default step-list mode omits steps inside sections. For a complete structural inspection, follow all pages and omit `type` and `parent_step_id` filters, which override the mode and can narrow the results. Ask only when the account, target, or requested outcome is materially ambiguous.

"Add a step to this checklist" can mean changing a template or changing an open run. Resolve that distinction before writing when context does not establish it. **Template edits affect future runs; existing runs do not automatically change.** The MCP tools do not perform the app's explicit propagation action. Explain this when it affects the user's goal.

Use workflow and workflow-step IDs returned by template tools. Never substitute IDs from run responses. Tool names below refer to operations on the connected Manifestly MCP server; use the current schemas. Consult `docs` for unfamiliar operations or errors instead of guessing parameters.

## Create a template

Turn the user's process into an ordered outline with clear task titles, sections where useful, and only the requested or clearly supported data fields, subtasks, assignments, and timing. Resolve missing business decisions that would change execution; do not invent mandatory approvals or deadlines.

Prefer `create_workflow` for a new template from an outline. Put each section's steps inside its `steps` list; use top-level steps only for ungrouped work. The outline supports standard and stop-task steps, subtasks, due offsets, and one field per step.

After creation, use `list_workflow_steps` with `mode: "hierarchy"` and follow all pages to obtain the created step IDs and verify the full structure, including steps inside sections. Add further fields with `create_step_data_setting` and additional instructions with `create_step_content_block` as needed. Hierarchy responses may repeat a step at the top level and under a section; deduplicate by ID before counting or modifying steps.

Do not start a run merely to finish creating its template unless the user also requests a run.

## Edit an existing template

Read the relevant existing structure and apply a partial update that preserves unrelated settings:

| Requested change | Operation |
| --- | --- |
| Workflow name or description | `update_workflow` |
| Add a section or step | `create_workflow_step` |
| Step title, parent section, supported kind, subtasks, or due rule | `update_workflow_step` |
| Remove a section or step | `delete_workflow_step` |
| Step instructions or media | `create_step_content_block` / `update_step_content_block` / `delete_step_content_block` |
| Collected field definitions | `create_step_data_setting` / `update_step_data_setting` / `delete_step_data_setting` |
| Step order or movement across sections | `reorder_workflow_steps` |
| Holiday calendar attached to the workflow | `set_workflow_business_calendar` |
| Landing rule for dates that fall on a non-business day | `set_workflow_business_day_rule` |

On a version-controlled workflow, `update_workflow` saves the description into the published snapshot and the next promote silently overwrites it from the draft; the title is unaffected. Direct the user to edit the draft when the description must stick.

For a new step inside a section, pass its `parent_step_id`. In updates, omitting this key preserves the parent, while null moves the step to the top level. Sections cannot be nested. Updating a subtask list replaces the list, so include existing subtasks that should remain.

Before reordering, fetch the complete active hierarchy with `list_workflow_steps` using `mode: "hierarchy"`, follow all pages, and include every active nonblank step exactly once. Keep each section followed contiguously by its children. Do not accidentally include duplicate IDs from nested and top-level representations.

Template due dates are relative rules with a basis, offset, and units. Day offsets default to business-day counting; set `late_at_offset_units_mode` to `regular` when calendar days are intended. A date-field basis is configured in the editor, not these step-edit tools. Two workflow-level settings shape where computed dates land: `set_workflow_business_calendar` attaches a holiday calendar (found with `list_business_calendars`) so its dates count as non-business days, and `set_workflow_business_day_rule` moves a date that lands on a non-business day to the next or previous business day. Both need their account feature, and both affect runs started afterward only. Use `docs` with `dates` for the full rules.

Inspect field definitions before editing their configuration. Changing `value_format` to a format that carries no configuration silently clears `value_format_config`, discarding a list's choices or a data-table binding; supply the intended compatible configuration and read it back. Unknown configuration keys are silently filtered, so a list sent under other key names is accepted and left empty.

## Advanced templates and copies

For a new advanced template or an explicitly requested copy, inspect `get_workflow_schema`; use `export_workflow` when copying an existing template. Set the intended title because the export always appends " - Exported" to it, and drop source-scoped references such as `business_calendar_id` unless the destination has that same calendar. Map account- and department-scoped references to the destination, including role IDs discovered with `list_roles`. Preserve internal relationships required by the schema rather than blindly copying source IDs.

Use `validate_workflow_import` before `import_workflow`. Correct validation errors before creation. Import creates a new workflow; it is not an in-place update. Read the result back before reporting success, and check for a partial creation before retrying an uncertain or failed import. Do not archive the original as automatic cleanup: `archive_workflow` closes every scheduled or started run of the workflow and deletes its scheduled runs, and `unarchive_workflow` restores neither. Prefer renaming it with `update_workflow` when work in flight still needs it, and say what archiving does before calling it.

Assignments, conditionals, and approval configuration are not editable through the current step-edit tools. For new templates, use the import route only when its current schema and validation support the requested feature. For unsupported in-place edits, provide the workflow's returned editor link and explain the remaining action. Do not replace an approval with a stop task or clone a workflow to imitate an in-place edit.

## Verify and finish

Read back the affected template and confirm the requested structure and settings, including field configuration and date-counting mode. When verifying the full structure after creation, import, or structural edits, use `list_workflow_steps` with `mode: "hierarchy"` and follow all pages so nested steps are included. Report what changed, its effect on future runs, the returned editor link, and any unfinished or unsupported portion.

Authoring can be blocked by department permissions, archival, shared-copy locks, or version control. Explain the returned reason; for version-controlled workflows, direct the user to edit the draft and publish through the app. Do not retry unchanged 403/404/409 responses or switch accounts to evade them. For uncertain writes, read back state before retrying and reuse the same idempotency key where supported.

Remove steps, fields, or instruction blocks only within the user's requested scope. `delete_workflow_step` deactivates rather than erases, so runs in flight keep their copy; deleting a section deactivates every step inside it, so inspect it in hierarchy mode first. `delete_step_data_setting` and `delete_step_content_block` are hard deletes that cannot be recovered. Clarify the affected scope when the user's intent is unclear, rather than assuming permission to remove related content.
