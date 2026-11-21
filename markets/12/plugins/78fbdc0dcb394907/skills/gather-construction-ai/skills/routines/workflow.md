---
name: routines
description: Set up recurring Gather checks and reports from the bundled routine templates when the user requests a schedule or automation.
---

# Gather routines

Read `../../shared/openai-runtime.md`, then `references/index.md` and `references/shared-conventions.md`. Preserve the bundled 26 routine definitions and use only those the user chooses. This workflow configures schedules; it does not claim to have run their reports.

1. Resolve the requested project using `../../shared/patterns/01-project-resolution.md`. Read the chosen templates under `references/routines/`. Capture cadence, timezone and required inputs; ask only for materially missing details. Do not assume the source template timezone is the user's timezone.
2. Check profile and register prerequisites. Use project-specific existing files without overwriting them. Where the template permits a quantities-only fallback, state it. Do not invent rates, dates, register rows or contract terms.
3. Discover the host's scheduling or Automations capability and read its actual schema. Establish whether future runs can access Gather, the installed skills, the input files and persistent output state. Cloud and desktop capabilities vary; a local path alone does not grant a future run access.
4. Substitute the chosen template's placeholders with real project and input references. Resolve all required placeholders before creation. Read only the chosen template, not every routine. Translate any template shorthand into a self-contained task instruction or a skill reference known to be available to the future run.
5. If the available scheduler supports the task, create it using its advertised interface. The user's request authorises the chosen schedule; do not ask again merely to confirm it. Preserve the requested timezone and report the returned task ID, cadence and state. Never lower tool permissions or claim a schedule exists without a successful tool result.
6. If no scheduler is available, or required future inputs cannot be accessed, provide the complete task brief and schedule, state that it is **prepared, not scheduled**, and identify the missing capability. Do not invent UI steps or substitute a reminder for a data-processing task without agreement.
7. Preserve existing profile and register contents. Store state only through the host's supported persistent file facilities. When persistence is unavailable, explain that change-only reporting cannot work and offer the template's stateless fallback if one exists.

Return a row per chosen routine: name, project, timezone/cadence, created or prepared status, and any concrete remaining dependency. Do not send messages or notices unless the user has authorised those actions.
