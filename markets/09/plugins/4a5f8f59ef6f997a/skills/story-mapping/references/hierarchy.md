# Project Hierarchy Reference

## The 3-Tier Model

```
Project
├── Journey (tier 1) ─── top-level column
│   ├── Step (tier 2) ── sub-column within journey
│   │   ├── Story Card (tier 3) ── work item
│   │   ├── Story Card (tier 3)
│   │   └── Story Card (tier 3)
│   └── Step (tier 2)
│       └── Story Card (tier 3)
├── Journey (tier 1)
│   └── Step (tier 2)
│       └── Story Card (tier 3)
└── Milestone (horizontal row, optional)
    └── Story cards assigned to this milestone appear in its row
```

## Tier Rules

| Property          | Tier 1 (Journey)    | Tier 2 (Step)       | Tier 3 (Story Card)                                               |
| ----------------- | ------------------- | ------------------- | ----------------------------------------------------------------- |
| parentId          | `null`              | journey ID          | step ID                                                           |
| Card type         | `journey` (auto)    | `journey` (auto)    | `none`, `objective`, `risk`, `question`, `knowledge_gap`, `learn` |
| milestoneId       | N/A                 | N/A                 | optional (milestone ID or `null` for backlog)                     |
| statusId          | N/A                 | N/A                 | optional (status ID or `null`)                                    |
| color             | N/A                 | N/A                 | optional color token                                              |
| Can have children | Yes (steps)         | Yes (story cards)   | No                                                                |
| Can be deleted    | Only if no children | Only if no children | Yes                                                               |

To delete a journey or step together with everything under it, or to delete several cards at once, use **`cards_bulk_delete`**. It cascades through the hierarchy and asks for `confirm: true` after showing a preview.

## Creation Tools

| Tier       | Preferred tool       | Fallback                                                       |
| ---------- | -------------------- | -------------------------------------------------------------- |
| Journey    | `journeys_create`    | `cards_create` with `parentId: null`, `type: "journey"`        |
| Step       | `steps_create`       | `cards_create` with `parentId: <journeyId>`, `type: "journey"` |
| Story Card | `story_cards_create` | `cards_create` with `parentId: <stepId>`, `type: <card type>`  |

For creating more than a couple of items, prefer **`cards_bulk_create`** — one call that takes a nested tree (`journeys` → `steps` → `cards`) plus board `milestones`, e.g.:

```jsonc
{
  "projectId": "<id>",
  "milestones": [{ "tempId": "mvp", "title": "MVP" }],
  "journeys": [
    {
      "title": "Onboarding",
      "steps": [
        {
          "title": "Sign up",
          "cards": [
            {
              "type": "objective",
              "title": "Verify email",
              "milestoneId": "mvp",
            },
            { "type": "risk", "title": "Spam complaints" },
          ],
        },
      ],
    },
  ],
}
```

To attach under cards that already exist, use the top-level `steps` array (each with an existing `journeyId`) or `cards` array (each with an existing `stepId`). A card's `milestoneId` may be an existing milestone id or a `tempId` from this call's `milestones`. The batch is validated in full before anything is created.

Always prefer these tools over the generic `cards_create` — they handle type and parentId automatically and validate the hierarchy.

## Placement

Cards within a section (a step's story cards, a journey's steps) are ordered by position. When creating cards, use the `placement` parameter:

- `"top"` — place at the beginning of the section
- `"bottom"` (default) — place at the end of the section

To place a card at a specific position relative to other cards, use `cards_move` with `aboveCardId` or `belowCardId`.

## Milestones

Milestones create horizontal rows that cut across all journeys and steps. They represent time-based groupings like releases, sprints, or phases.

- A story card with `milestoneId: null` appears in the backlog row (no milestone)
- A story card with a `milestoneId` appears in that milestone's row
- Milestones only affect tier-3 story cards

### Milestone Properties

| Field       | Type           | Description                                            |
| ----------- | -------------- | ------------------------------------------------------ |
| title       | string         | Milestone name (e.g., "Sprint 1", "MVP", "Q2 Release") |
| description | string or null | Optional details                                       |
| targetDate  | string or null | ISO date string for the target date                    |

## Statuses

Statuses are space-level workflow states. Each status has:

| Field    | Type          | Description                                                        |
| -------- | ------------- | ------------------------------------------------------------------ |
| id       | string (UUID) | Unique identifier — always look up, never guess                    |
| name     | string        | Display name (e.g., "Backlog", "In Progress", "Done")              |
| color    | string        | Display color                                                      |
| category | enum          | One of: `backlog`, `unstarted`, `started`, `completed`, `canceled` |

### Status Categories

- **backlog** — Not yet prioritized for work
- **unstarted** — Prioritized but not yet begun
- **started** — Actively being worked on
- **completed** — Finished successfully
- **canceled** — Will not be done

Always call `spaces_statuses_list` with the `spaceId` to discover available statuses before assigning them.

## Finding Projects

### Browse all projects

Call `projects_list` to list all projects in the organization. Optionally pass a `spaceId` to filter to a single space.

### Search by name

Call `find_project_by_name` with a `query` string to search by name (case-insensitive substring match). Returns matching projects with their space info. Use this when the user mentions a project by name — it's faster than listing all projects and scanning manually.

## Project Reading Strategies

### Quick overview

Call `projects_list_backbone` to get journeys and steps with card counts. Good for understanding structure without loading every card.

### Full state

Call `projects_list_all_cards` to get every card with tier, parent, and milestone info. Required before creating cards (to avoid duplicates) or when you need to understand the complete layout. It's paginated (default 200 items per page, max 500) — check the response's `nextCursor`, and if it's non-null, keep calling again passing that value as `cursor` until it comes back `null` before assuming you've seen every card.

### Single card detail

Call `projects_get_card_details` for a specific card's description, associations (labels, personas, customers), and comments.

## Personas & Customers

Personas and customers are space-level entities that can be associated with story cards.

### Personas

User archetypes like "Power User", "New Hire", or "Admin". Call `personas_list` to discover existing personas in a space, `personas_create` to add new ones, and `cards_personas_set` to associate personas with a card.

### Customers

Real companies or segments like "Acme Corp", "Enterprise Tier", or "SMB". Call `customers_list` to discover existing customers in a space, `customers_create` to add new ones, and `cards_customers_set` to associate customers with a card.

Both appear in the `personaIds` and `customerIds` arrays returned by `projects_get_card_details`.
