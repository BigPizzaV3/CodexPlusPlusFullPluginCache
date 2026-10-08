# Receiving-project contract

These workflows were migrated together from a project KB. Resolve project facts
and local authority before using them in another project; the hosting project's
game, tool choices, timeline, and migration phases are not defaults.

## Resolve context once per task

Read the receiving project's agent guide, current-state note, and relevant domain
context when available. `AGENTS.md`, `PROJECT_STATE.md`, `_Context.md`, and
`00_System/` are the source KB's conventions, not files in this installed plugin.
Use the receiving project's equivalents. If a location does not exist, establish
only the ownership needed for the task; do not create an entire KB taxonomy just
to satisfy a filename convention.

An explicit request to initialize or onboard a shared project KB uses the
[KB Bootstrap workflow](../skills/kb-bootstrap/SKILL.md). That new workflow can
create a minimal starter for an empty KB or map an existing layout; ordinary
domain tasks still do not trigger a full setup.

Apply the project's source-of-truth policy. The bundled
[authority reference](source-of-truth.md) supplies reusable evidence distinctions
when the project has no equivalent. A project's active balance plan and release
process determine its current phase and promotion gates; no Backpack Legends
migration milestone is imposed on another project.

Existing explicit user authorization covers its stated scope. Ask only for new
material decisions, unresolved ownership, or a required approval that has not
already been given. Audit-only requests produce findings rather than edits.

## Paths and companion skills

Paths in a skill's Markdown links are relative to that installed skill file.
Project paths written in backticks refer to the receiving project. For scripts,
resolve the installed skill directory and pass the target project explicitly;
never assume the current working directory is the plugin cache.

The whole core plugin is the distribution unit; keep its `skills/` and shared
`references/` directories together. Copying one skill folder alone loses required
resources. A host that imports only isolated skill folders needs a separate,
tested export with the full dependency set; that export is not provided here.

Eight core skills ship together: kb-bootstrap, knowledge-steward, kb-maintenance,
gdd-authoring, gdd-migration, balance-analysis, runtime-audit, game-project-planner.
Load companions only when the task needs them and only once per task; do not
recursively reload a companion that is already in context. Use the host's skill discovery or
read the named sibling's `SKILL.md`; do not require a legacy `.agents/skills` copy.

The market research plugin is separate. Resolve available browsing, spreadsheet,
visual-design, repository and analytics capabilities from the host. Named products
in examples are not required services. Use the receiving project's designated
equivalent. If a capability is unavailable, identify the missing evidence/output
and continue only the supported part; do not silently change the destination or
claim access, execution or publication that did not occur.

## Language and data

Follow the receiving project's writing policy. If no policy is supplied, use
English for canonical KB documents, retaining the source workflow's default, and
the user's language in conversation. Keep exact IDs and localized strings.
Live configurations, current decisions, research datasets, schedules, team
capacity, and working-state artifacts belong to the project, not this plugin.

## Lint layout

The read-only lint script now supports project profiles, with the source layout
as its default. Follow [runtime and profile guidance](../skills/kb-maintenance/references/linting.md)
to select directories, metadata requirements, ID conventions and link types.
Check the effective profile, matched files and coverage limitations in its output.
Empty input, unmatched project conventions and skipped checks are not proof of KB
health. Plugin instruction directories are excluded by default. Python and the
bundled runtime requirements must be available; installing the plugin alone does
not provide them.
