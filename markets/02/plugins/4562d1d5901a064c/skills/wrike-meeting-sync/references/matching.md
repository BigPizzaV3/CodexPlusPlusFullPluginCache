# Matching Meeting Notes to Wrike

Match the polished meeting notes to Wrike tasks, projects, and folders. The notes are the only source for what happened in the meeting; Wrike is the source for current work state. Do not use the raw transcript or infer facts that are missing from the notes.

Matching is read-only. It inspects Wrike and prepares proposals, but it never creates, comments on, or updates anything. Applying approved changes happens later in the workflow (see `operation-rules.md`).

## Requirements

A Wrike MCP connector must be connected so you can search and read items. Use the connected Wrike tools (for example `Wrike:search_tasks`, `Wrike:search_folder_project`, `Wrike:get_task`, `Wrike:get_folder`, `Wrike:get_contacts`, `Wrike:get_workflows` — match the actual tool names your connector exposes) to read state. If no Wrike connector is available, say so and stop; do not guess at Wrike contents.

## Find relevant work

- Read and report the connected Wrike user first, so the user knows whose account is in scope.
- Identify the narrowest relevant space, project, or folder, and scope searches to it whenever possible.
- Resolve explicit Wrike links or item IDs first. Otherwise derive distinctive search terms from the notes — the project, product, client, or initiative named around each action item.
- Search projects and folders as **two separate calls** (`project: true` and `project: false`). They are different queries; a single search will miss one kind.
- Use a task search when a mentioned work item may be a task-based custom type (Campaign, User Story, etc.), and inspect its parents for destination context.
- Inspect plausible items before proposing an action — check title, type, parent, status, people, dates, description, custom fields, and permalink as relevant.
- Treat an explicit ID as item identity, not as proof that a change is supported by the notes.
- Never invent owners, dates, statuses, field values, or outcomes.

### Choosing a destination (do not guess)

Prefer a destination only when its title, hierarchy, description, and the notes' context make it **clearly more relevant** than the alternatives. Do not choose a destination merely because it has a keyword match — a shared keyword is not a match.

If, for a given action item, there is **no credible destination** or **more than one credible destination**, do not pick one. Put the item under **Needs your input** with up to three candidate names and permalinks and ask the user to choose. Different action items may belong in different destinations.

## Cover every action item

Account for every action item in the meeting notes. Do not silently omit one. Give each action exactly one visible outcome:

- update an existing Wrike item;
- create a new Task, Project, or Folder;
- **Already represented / no action needed**;
- **Needs your input**;
- **Not tracked**, with a short reason.

Prefer structured Wrike work over comments, because a comment is easy to miss and does not drive Wrike's own reporting:

1. Update canonical fields on an exact existing item when appropriate: status, people, dates, description, or custom fields.
2. Create a new item when the notes contain explicit work and no suitable item exists.
3. Use comments to preserve rationale, decisions, or meeting context.

A comment alone does not count as representing an action item unless the action is purely informational. An existing comment that mentions an owner, status, or date does not prove the corresponding Wrike fields are populated — inspect those fields and propose updates when they do not reflect the notes.

When one action item contains distinct work with different owners, timing, or dependencies, prepare separate proposals when that creates clearer accountability.

## Check for existing work before creating

Before proposing to create anything, search the resolved parent for work that already represents the action. "No visible match" alone is not permission to create — the notes must contain an explicit action or creation decision. A restated commitment in the notes (unchanged since a prior meeting, already a task, recap of a decided date) is not a creation decision.

Run a real duplicate search, not a single glance:

- Search **active and deferred** items using the deliverable's distinctive nouns and verbs.
- Run a close-title search first and, when needed, one broader keyword search.
- Also search meeting-notes tasks in the destination; a prior notes item that already records the same owner, deliverable, and date is a match.
- Compare title, description, assignees, and status. A shared keyword alone is not a duplicate.

Then branch on the result:

- **Clear match** — report the action as **Already represented**, linking the existing item; do not create a duplicate.
- **Ambiguous match** — put it under **Needs your input** with the candidate(s) linked, and state the single decision needed.
- **Failed or unavailable search** — disclose it in the preview; never treat a failed search as a silent "no duplicate."

## Prepare supported actions

Prepare read-only proposals for: comments and due dates; creating standard Tasks, Projects, or Folders; status changes, including completing or cancelling tasks; adding or removing task assignees or project owners; description edits; and custom-field changes.

- **Dates** — copy the notes' Due token (`YYYY-MM-DD` or `none`) into the Wrike due-date field as that same single token. Do not re-anchor to today, convert weekday names to day-of-month numbers, invent a day for a named week, or add parentheticals.
- **Creation** — resolve the exact parent (per "Choosing a destination") and run the duplicate search above first.
- **Statuses** — inspect the relevant workflow and resolve the exact standard or custom status. Do not guess from a display label.
- **People** — resolve each name to a unique Wrike user ID. If more than one person matches, put the proposal under **Needs your input**.
- **Descriptions** — fetch the full current description. Never prepare an edit from truncated content.
- **Custom fields** — resolve the field ID and type, and inspect allowed options when applicable. Clearing a field must be explicit.

## Preview

Group proposals into the sections below.

### Ready to apply

Use a compact table:

| Row | Action | Wrike item | Change |
|---|---|---|---|

- Use stable row labels such as `M1`, `M2`, `M3` for the current preview. Each row is one operation.
- Existing-item actions must identify an exact item and include its canonical ID and permalink.
- Creation actions must identify the exact parent and item type.
- Keep the Change cell short, such as `Active → Completed`, `Sam → Alex`, or `Add comment`.
- Do not dump full comments or descriptions into the table.

Show detailed content only below the table when needed: the exact comment body (before any signature the apply step adds); a description diff or complete before/after text; a new item's title, parent, description, people, status, and dates; custom-field name with human-readable old/new values; and an inline note such as `Runs after M1` when an operation depends on a prior creation.

A proposal belongs under **Ready to apply** only when the exact target or parent, required IDs, valid values, duplicate checks, and complete preview content are all resolved.

### Needs your input

List proposals that need one clarification — an ambiguous person, target, parent, status, field, value, destination, or duplicate. State the single decision needed, and link up to three candidates when a choice of destination or item is involved. Do not create a row that looks ready when required information is missing.

### Already represented / no action needed

List action items that require no Wrike change, and identify the item or evidence that already represents the work. Check canonical fields rather than relying on a comment alone.

### Not tracked

List any action intentionally not represented in Wrike, with the reason.

Every action item must appear under exactly one of these four sections. If the notes support no Wrike actions, say so plainly.
