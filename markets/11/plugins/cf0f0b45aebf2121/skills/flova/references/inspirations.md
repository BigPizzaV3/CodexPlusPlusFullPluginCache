# Using Inspirations

Read when the user selects a Flova inspiration. An inspiration defines a complete task: tools, required steps, conditional routes, references, and deliverables. Flova media generation may be only one part of it. Inspirations are not a third creation mode alongside quick generation and projects.

## 1. Retrieve Complete Instructions

Use the connected inspiration tools: `creation_inspiration_categor_items` finds published cards and `creation_inspiration_batch_get` retrieves complete published instructions by ID. Host-added prefixes may differ; use the actual schemas.

Resolve the user's name to the intended inspiration, asking only when multiple plausible matches remain. Read the complete instructions and references needed for the current step before acting; search results, card descriptions, and launch prompts do not replace the workflow. If the body or a required reference cannot be retrieved, explain the specific gap rather than inventing the workflow.

When files accompany an inspiration, preserve relative paths so referenced scripts and documents remain usable. Retain the actual inspiration ID and published revision for continuation rather than inventing a version.

## 2. Execute the Workflow

- Follow required steps in dependency order, reusing inputs, completed work, and prior analysis. Run optional steps only when their conditions apply. User constraints, route choices, and authorization take precedence over defaults; do not request an already-granted approval again for the same action.
- Follow the inspiration's explicit creation mode, supplied references, and downstream tools. If it does not specify a mode, use the main Skill's selection guidance and prefer quick generation; storyboards, reviews, or multiple revisions do not by themselves make an inspiration a project workflow.
- Check the required tools and access routes. An uninstalled tool, one plugin search returning no result, missing authorization, and unsupported host access are different states. For connection-dependent work, check the documented route and current host support before declaring it unavailable.
- Use a fallback only when the inspiration's condition is met or the user has chosen it. Explain the actual limitation before changing routes and continue useful independent work; do not silently omit required work or replace the complete task with the easiest output.
- Local helper Skills are distinct from server-side creative Skill IDs. When the inspiration already supplies sufficient rules, execute them even if the host does not expose a helper; do not ask the user to find a fixed helper name or `creative-tracker.md`. Still identify actual missing material, capabilities, or authorization.

For example, finding no installed advertising plugin does not establish that an advertising account cannot be connected. Check the applicable connection route before requesting an exported report as a fallback. If the user already supplied a report or chose file-based analysis, reuse that choice directly.

## 3. Check Delivery

Compare results against the inspiration's requested deliverables and the user's current scope. Distinguish completed work, missing inputs, and agreed substitutions. If required steps remain undone, do not describe a fallback or partial analysis as completion of the full workflow.
