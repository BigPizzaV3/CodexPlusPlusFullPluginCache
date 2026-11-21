---
name: story-mapping
description: >
  Guide users through story mapping, user journey mapping, and product discovery
  using Cartographer projects. Use when the user mentions "story map", "user journey",
  "journey map", "product discovery", "map the flow", "project", "user activity",
  "story cards", "walking skeleton", "release planning", "backlog prioritization",
  or wants to visualize how users interact with a product.
metadata:
  version: '0.2.0'
---

# Story Mapping with Cartographer

Cartographer is a collaborative story-mapping tool for product teams. It implements the user story mapping methodology as an interactive project with a strict 3-tier hierarchy, card types for different kinds of work items, milestones for release planning, and statuses for workflow tracking.

## The 3-Tier Hierarchy

Every Cartographer project uses a fixed 3-tier card hierarchy that models user-journey maps:

### Tier 1 — Journeys (columns)

Top-level columns representing high-level user activities. These are the "big things" users do, read left-to-right as a narrative flow. Examples: "Discover Product", "Sign Up", "Complete First Task", "Invite Team".

A good project has **3-6 journeys**. Fewer than 3 usually means the scope is too narrow; more than 6 means either the scope is too broad or activities need consolidation.

### Tier 2 — Steps (sub-columns within a journey)

Phases or tasks within a journey. Steps break down the high-level activity into a sequence the user follows. Examples: under "Sign Up" you might have "Enter Email", "Verify Email", "Set Password", "Choose Plan".

Each journey should have **2-5 steps**. A journey with only 1 step is probably too granular to be a journey. A journey with more than 5 steps may need splitting into multiple journeys.

**ALWAYS create steps.** Never skip from journeys directly to story cards — the step layer is mandatory.

### Tier 3 — Story Cards (items within a step)

Individual work items under a step. These are the actual stories, tasks, risks, questions, and insights that the team needs to address. Story cards are where the detail lives.

Story cards can be assigned a **type**, a **status**, a **milestone**, an **estimate**, optional **start and target dates**, and optionally a **color**.

## Tool Orchestration

### Recommended creation order

1. `spaces_list` — find the target space (or `spaces_create` if needed)
2. `projects_create` — create the project within the space
3. `spaces_statuses_list` — look up available statuses before assigning them to cards
4. `cards_bulk_create` — create the whole backbone and cards in **one call** (preferred for more than a couple of cards)

`cards_bulk_create` takes a nested tree: `journeys` → nested `steps` → nested `cards`, plus optional board `milestones`. It handles tier order and positioning, and validates the whole batch before creating anything — so you don't have to create journeys, then steps, then cards one tool call at a time. A card's `milestoneId` can reference an existing milestone or a `tempId` declared in the same call's `milestones`. To add under parents that already exist, use its anchored `steps` (with `journeyId`) or `cards` (with `stepId`) arrays.

For single additions, the tier-specific tools still apply:

- `journeys_create` — one tier-1 journey column
- `steps_create` — one tier-2 step under a journey (requires `journeyId`)
- `story_cards_create` — one tier-3 card under a step (requires `stepId`)
- `milestones_create` — one time-based row for release planning

Prefer `cards_bulk_create` or the tier-specific tools over the generic `cards_create`. They handle type and parentId automatically.

### Finding projects

- `projects_list` — list all projects in the organization, optionally filtered by space ID. Good for browsing what exists.
- `find_project_by_name` — search for projects by name (case-insensitive substring match). Returns matching projects with space info. Use this when the user mentions a project by name.

### Reading project state

- `projects_list_backbone` — quick overview of journey/step structure with card counts. Use this to understand the layout without loading every card.
- `projects_list_all_cards` — full card list with parent and milestone relationships. Call before creating cards to avoid duplicates and understand the current layout. **Paginated**: keep passing the response's `nextCursor` back as `cursor` on the next call until it comes back `null` before assuming you've seen every card.
- `projects_get_card_details` — full details for a single card including description, associations, and comments.

Always read project state before modifying an existing project.

### Personas & customers

Personas represent user archetypes (e.g. "Power User", "Admin"). Customers represent real companies or segments (e.g. "Acme Corp", "Enterprise Tier"). Both are space-level entities that can be associated with story cards.

- `personas_list` — list personas in a space
- `personas_get` — get a single persona by ID
- `personas_create` — create a persona
- `personas_update` — update a persona
- `personas_delete` — soft-delete a persona
- `customers_list` — list customers in a space
- `customers_get` — get a single customer by ID
- `customers_create` — create a customer
- `customers_update` — update a customer
- `customers_delete` — soft-delete a customer
- `cards_personas_set` — associate personas with a card (replaces existing)
- `cards_customers_set` — associate customers with a card (replaces existing)

Use `personas_list` / `customers_list` to discover existing entries before creating new ones. The `projects_get_card_details` response includes `personaIds` and `customerIds` arrays.

### Other tools

- `spaces_get` — get a single space by ID
- `spaces_update` — update space name or description
- `spaces_delete` — soft-delete a space. Call once without `confirm` to preview how many projects/personas/customers will become inaccessible, then again with `confirm: true` to actually delete
- `statuses_create` / `statuses_get` / `statuses_update` / `statuses_delete` — manage a space's workflow statuses directly (usually not needed — spaces are seeded with default statuses on creation)
- `projects_update` — update project name or description
- `projects_delete` — soft-delete a project. Call once without `confirm` to preview how many cards/milestones/comments will become inaccessible, then again with `confirm: true` to actually delete. Canvases in the parent space are unaffected
- `cards_update` — update card metadata (title, description, type, status, estimate, dates, color). It can't change a card's parent or milestone; use `cards_move` for that
- `cards_move` — move or reorder a card (change parent, milestone, or position)
- `cards_delete` — soft-delete a card (cannot delete cards with children)
- `cards_bulk_delete` — soft-delete many cards in one call, cascading through steps and story cards under them. Use it for "delete these" or "delete everything except X" instead of repeated `cards_delete` calls. Call once without `confirm` to preview how many cards will go, then again with `confirm: true` to actually delete
- `milestones_list` — list existing milestones
- `milestones_get` — get a single milestone by ID
- `milestones_update` — update milestone metadata
- `milestones_delete` — delete a milestone. Cards still assigned to it keep a stale `milestoneId` until moved with `cards_move` (`toSection.milestoneId`), so move them first
- `comments_list` — list comments on a card or milestone, paginated
- `comments_get` — get a single comment by ID
- `comments_create` — add a comment to a card
- `comments_update` / `comments_delete` — edit or delete a comment. Restricted to the comment's original author or an organization owner/admin
- `comments_resolve` — mark a comment thread resolved
- `canvases_list` / `canvases_get` / `canvases_create` / `canvases_update` / `canvases_delete` — manage whiteboard canvases in a space
- `canvases_attach_to_card` / `canvases_detach_from_card` — associate a canvas with a card
- `whoami` — check authenticated user info and role
- `feedback_submit` — report a tool that errored or misbehaved, a capability you needed that no tool provides, or a confusing description, error, or response. Works for viewers and without a subscription. Call it after retrying or working around the problem, not instead of doing so

## Card Types

Story cards (tier 3) have a `type` field. Choose the type that best matches the card's purpose:

| Type            | When to use                                                                                     |
| --------------- | ----------------------------------------------------------------------------------------------- |
| `none`          | Generic story card — a task or user story with no special semantics                             |
| `objective`     | A goal or desired outcome ("User can export data as CSV")                                       |
| `risk`          | A threat, concern, or uncertainty ("Third-party API may have rate limits")                      |
| `question`      | An open question to resolve ("Do users need SSO?")                                              |
| `knowledge_gap` | Something the team needs to learn ("How do competitors handle onboarding?")                     |
| `learn`         | An insight, learning, or validated assumption ("Users prefer email over SMS for notifications") |
| `pain_point`    | A frustration or problem users have today ("Admins rebuild the weekly report by hand")          |
| `opportunity`   | A chance to create value that isn't a committed story yet ("Auto-send the report to finance")   |

Use typed cards liberally — they make the project scannable and help teams identify what needs attention. A step with only `none`-typed cards is a missed opportunity to surface risks, questions, and goals.

See `references/card-types.md` for deeper guidance on each type.

## Color Philosophy

Do NOT assign colors by default. Colors are reserved for **cross-cutting groupings** that span multiple columns — for example, tagging cards by persona, team, or workstream across different journey steps.

If you do use color, limit to **2-4 colors** per project. Available tokens: `blue`, `red`, `cyan`, `green`, `yellow`, `pink`, `orange`, `navy`, `gray`.

Bad: coloring every card in a step the same color (that's what the step column already communicates).
Good: coloring cards `blue` for "Admin persona" and `green` for "End-user persona" across multiple steps.

## Statuses

Statuses are space-level workflow states (e.g., Backlog, In Progress, Done). Each status has a category: `backlog`, `unstarted`, `started`, `completed`, or `canceled`.

- **Always call `spaces_statuses_list`** before assigning statuses to cards. Never guess status IDs.
- Set `statusId` when creating or updating tier-3 story cards.
- Pass `null` to clear a status.
- Statuses are only meaningful on tier-3 story cards, not on journeys or steps.

## Milestones

Milestones define horizontal rows on the project for time-based grouping — think of them as releases, sprints, or phases. Cards not assigned to any milestone appear in the "backlog" row.

Use milestones when the user has timeline information (releases, sprints, quarters) and wants to prioritize cards vertically. Not every project needs milestones.

To put a card in a different milestone (or back in the backlog), use `cards_move` with `toSection: { parentId: <stepId>, milestoneId: <milestoneId or null> }`.

## Estimates and Dates

- **Estimates** size a story card. Pass an integer from the space's scale or a t-shirt size (`XS`, `S`, `M`, `L`, `XL`) as `estimate` when creating or updating cards; `null` clears it. Flag L and XL cards as candidates for splitting.
- **Dates** are optional `startDate` / `targetDate` (`YYYY-MM-DD`) on story cards and milestones, shown on the project's Gantt view. A card without dates inherits its milestone's range for display. **Never invent dates** — only set them when the user gives a schedule or asks for one.

## Access

Organization members are owners, admins, members, or viewers. Viewers are read-only: every create, update, delete, move, or set tool fails with `VIEWER_READ_ONLY`. If unsure, call `whoami` (its response includes `role` and `readOnly`) before planning writes, and offer a read-only deliverable (a review, a markdown plan) to viewers instead.

## Workflow Skills

This plugin includes focused skills for common story-mapping jobs. Use them when the request matches:

| Skill                    | Use for                                                                 |
| ------------------------ | ----------------------------------------------------------------------- |
| `user-story-mapping`     | Building a new map from a brief, PRD, or idea                           |
| `interview-to-story-map` | Turning interview transcripts or research notes into an evidence map    |
| `feedback-to-story-map`  | Theming support tickets, NPS comments, or feature requests onto the map |
| `mvp-slicing`            | Walking skeleton, release slices, Now / Next / Later                    |
| `story-splitting`        | Breaking big stories into small vertical ones (SPIDR)                   |
| `story-map-review`       | Critiquing an existing map's structure and assumptions                  |
| `story-map-to-backlog`   | Writing tickets with acceptance criteria from a slice                   |
| `sales-discovery-map`    | Mapping a prospect's workflow and pains from discovery calls (MEDDICC)  |
| `mutual-action-plan`     | A shared buyer/seller plan from evaluation to go-live                   |
| `sales-playbook-map`     | A sales or CS playbook organized along the customer journey             |

This skill (`story-mapping`) is the reference for how Cartographer's tools work; the workflow skills describe the method.

## Story Mapping Methodology

Cartographer implements Jeff Patton's user story mapping approach:

1. **Start with the backbone** — Identify the user's journey as a left-to-right narrative of activities (journeys) and tasks (steps). This is the "walking skeleton" of the product.

2. **Walk the user's experience** — For each step, ask: "What does the user do here? What could go wrong? What do we not know?" This naturally generates story cards of different types.

3. **Slice horizontally for releases** — Use milestones to draw horizontal lines across the project. Cards above the first line are the MVP or first release. Cards below are later iterations.

4. **Surface risks and gaps** — A good story map isn't just tasks. It explicitly captures risks, questions, knowledge gaps, and learnings. These typed cards make invisible concerns visible.

5. **Read it as a story** — The project should read left-to-right, top-to-bottom as a coherent narrative of the user's experience, with each release slice being a viable version of that experience.

## Common Anti-Patterns

- **Skipping steps**: Going directly from journeys to story cards. Always create the step layer.
- **Too many journeys**: More than 6 journeys usually means the scope is too broad. Consolidate related activities.
- **Too few steps**: A journey with 1 step is probably at the wrong level of abstraction.
- **No typed cards**: All `none`-typed cards means you're not capturing risks, questions, or objectives. Ask probing questions.
- **Color overload**: Every card colored differently. Colors lose meaning when overused.
- **Skipping project read**: Modifying a project without first reading its current state leads to duplicates and structural errors.
- **Guessing status IDs**: Always call `spaces_statuses_list` first. Status IDs are UUIDs, not human-readable.

## Working with Existing Projects

When asked to modify an existing project:

1. Call `projects_list_all_cards` to understand current state
2. Identify what's there and what's missing
3. Suggest changes before making them
4. Create new cards in the right tier and parent
5. Use `cards_update` to modify existing cards rather than deleting and recreating
