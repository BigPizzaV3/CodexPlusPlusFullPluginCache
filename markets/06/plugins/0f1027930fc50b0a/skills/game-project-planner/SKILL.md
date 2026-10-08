---
name: game-project-planner
description: Build or revise a game Project Plan spreadsheet from a project brief, feature backlog, team capacity and delivery goals. Use for Feature List review and milestone planning; not for detailed GDD authoring or publisher operations unless explicitly in scope.
---

# Game Project Planner

## Purpose and portability

Turn a game concept or existing feature list into a concise product backlog and an executable milestone plan. Migrated into Sparkore's shared plugin from the source KB; no source project's design, staffing, technology, or scope is a default for another project. Apply the [receiving-project contract](../../references/project-context.md) when resolving project context and ownership.

Install or move the whole `sparkore-core` plugin, preserving its `skills/` and shared `references/` directories. This skill folder alone is not a standalone distribution: its receiving-project contract lives outside the folder. Keep each project's facts in its own brief and spreadsheet; do not edit this skill to store a project's timeline or feature list. Follow the receiving project's agent guide and writing policy. Discuss with the owner in their preferred language; confirm the spreadsheet language.

## Start with the relevant mode

- New plan: read [Discovery questions](references/discovery.md), extract known answers, then ask only consequential unanswered questions.
- Existing plan: first read live tab names, headers, values, notes, merges, formatting and validation. User edits and current decisions take precedence over remembered row numbers or previous assistant proposals.
- Review only: return findings and proposed changes without writing.
- Authorized update: make the scoped changes and verify them; do not repeat approval questions already answered.

Use the available spreadsheet capability for implementation. For native Google Sheets, preserve native structure and use live reads before edits. Do not rely on a particular connector being installed; state an access limitation if the requested destination is unavailable, and do not claim a draft was uploaded.

## Establish a planning brief

Resolve the product loop, target platform, delivery endpoint, player-experience horizon, responsibility boundary, team availability, reusable dependencies, time basis and destination. Compile a short brief including accepted facts, open decisions, assumptions, proposed sections and sheet schema.

For new or materially ambiguous plans, show this concrete brief before a substantial workbook rewrite. Existing explicit approval is sufficient; ask only for unresolved decisions that materially change scope or authority. Do not make the questionnaire a mandatory interview when the brief is already complete.

## Build the Feature List

Use [Spreadsheet contract](references/spreadsheet-contract.md). Treat the list as a product backlog, not an implementation task inventory.

- Identify the core playable loop and supporting progression/content/UI systems before adding secondary layers.
- Use genre-appropriate coverage prompts: controls/combat, session lifecycle, game modes, progression, economy, content, onboarding, player settings, retention, monetization and in-game service integration. These are prompts, not mandatory features or fixed section names.
- Distinguish a game capability from an implementation/QA task and from an external team's deliverable. A production team can own game-side integration without owning an admin console, marketing campaign, customer support workflow or shared publishing platform.
- Preserve owner-defined sections and names. Consolidate overlap through an explicit scoped change, not by silently deleting a feature or reintroducing a rejected feature under another name.
- Assign or preserve priority independently of delivery status. Priority does not mean a feature has been approved for the current release.
- Audit dependency chains, including reward producers and consumers: shops/gacha must have usable outputs; recycle resources need an applicable sink; FTUE must follow the system being taught.
- Do not silently rewrite accepted descriptions to repair a design contradiction. Record the proposal or ask for a decision. When descriptions are blank and drafting is authorized, fill concise descriptions directly. Put proposed replacements for existing descriptions in notes unless the owner authorizes promotion.

## Build the Milestone Plan

Choose milestones by testable product maturity and dependencies, not a fixed number or naming scheme. Break a feature into Function rows only when it needs smaller deliverables. Repeated appearances must describe different increments, integration or validation, not duplicate full implementation.

Estimate from role capacity: people, seniority, effective availability, reuse, dependencies, design/art lead time, integration, QA and rework. Do not count a PO who also performs QA as two full-time people. If part-time hours are unknown, label the estimate provisional; do not invent an FTE value or unavailable specialist. Capture capacity assumptions compactly with the schedule rather than expanding the backlog.

An illustrative calculation is available person-weeks = people × weeks × agreed availability. Apply an explicit allowance for non-feature work when useful; no fixed percentage is mandatory. Check bottlenecks by role, not only aggregate headcount. If a deadline and scope conflict, propose concrete scope/resource/timeline choices.

Each milestone needs a short name, start/end period, duration, one Objective and a few measurable Key Results. Distinguish proposed targets from measured evidence. Keep names stable for dropdown references; place timing in the OKR column by default.

Planning through soft launch does not imply waiting for a D30 cohort. Prepare the D30 journey, content, replay goals and economy before launch; actual D30 retention is a later observation unless explicitly in scope. If production owns only handoff, the endpoint is a testable build handoff, not store approval or rollout owned by another team. Shared modules are named dependencies with an owner/interface and required availability, not assumed finished systems.

Account for every retained backlog item as planned or explicitly unplanned. Do not create a Backlog milestone. Reconcile changes in both sheets without adding a deferred feature into the committed scope merely to hide an unresolved dependency.

## Revise and finish

On revisions, preserve unrelated edits, notes, formulas, status values and native controls. Re-read before index-sensitive deletes and resolve duplicate names through Section/Feature/Function or an existing ID. A red priority cell is not an instruction to delete a row: use the owner's marking convention and inspect explicit formatting.

Run [Acceptance checks](references/acceptance.md). Report the destination, actual changes, planned/unplanned coverage, material assumptions and any verification limitation. Do not claim native multi-select behavior or visual fit from display text alone.
