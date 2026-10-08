---
name: magicplan-workspace-report
description: >-
  Report across all projects in a magicplan workspace — list, filter, search, and roll up statistics
  (recent activity, projects by assignee, by time period, by documentation or estimate posture) and
  recommend the most useful cut based on what the person is after. Use this whenever someone wants a
  workspace- or portfolio-level view rather than one project: "how many projects did we open last month",
  "list all my active jobs", "show me everything assigned to Maria", "which projects haven't been touched
  in weeks", "give me a workspace overview", "projects by loss type", "portfolio dashboard", or "what's
  in the workspace". Trigger it whenever the scope is many projects at once, or when the person asks for
  counts, trends, or a filtered project list across the workspace.
compatibility: Requires the magicplan connector (MCP tools) for project and workspace data.
metadata:
  author: magicplan
  version: "1.0"
---

# magicplan Workspace Report

Give the user a workspace-level view of their projects — filtered, searched, and rolled up the way that
answers their actual question. When the ask is vague ("give me an overview"), propose the cuts that are
most useful and let them pick, rather than dumping an undifferentiated list.

This skill reads from magicplan only and never changes workspace data.

## Step 1 — Orient

Call `get_workspace` to confirm which workspace you're reporting on. If the user's request is specific
(e.g. "projects opened last month"), go straight to Step 3. If it's open-ended, do Step 2 first.

## Step 2 — Recommend a cut

When the user hasn't pinned down what they want, suggest the reports that fit their situation and let them
choose (single or multiple). Common, high-value cuts:

- **Recent activity** — projects created or modified in a window (last week/month/quarter).
- **By assignee** — projects grouped by the user they're assigned to (`email` filter).
- **Stalled / needs attention** — projects not modified in N days.
- **New intake** — projects created recently, oldest-first, to work a queue.
- **Documentation posture** — across a subset, which projects have photos / moisture readings / estimates
  vs. gaps (deeper — see the note in Step 3 about cost).
- **Loss-type or location breakdown** — grouped by address/region or by loss type where recorded.
- **Name/keyword search** — everything matching a term.

Tailor the suggestions to any hint in their prompt (a name, a person, a timeframe).

## Step 3 — Pull the data

Use `list_projects` with the filters and paging that fit the cut:

- `name` — partial/exact name search.
- `email` — projects assigned to a user.
- `sort` — `Projects.name`, `Projects.user_created`, or `Projects.user_modified`; with `direction`
  `asc`/`desc`.
- `page` — **page through all results** using `page_info` so counts and lists are complete, not just
  page 1. Report `total_count` for any count question.

Each project row carries id, name, address, assignee, and created/modified timestamps — enough for
listing, grouping, time-window, and assignee reports directly.

**Deeper posture reports cost more calls.** Documentation/estimate posture is not in the project list; it
requires `get_project_snapshot` per project. If the user wants that across many projects, confirm the
scope first, cap it to a sensible subset (e.g. the filtered list or a stated limit), tell them how many
you'll inspect, and never silently truncate — if you cap, say what was left out.

## Step 4 — Deliver

Match the format to the cut and size:

- A **filtered list** → a clean table (name, address, assignee, created, modified), sorted as asked.
- **Counts / trends** → the headline number(s) plus a short table or simple chart (e.g. projects per
  month), with the total and the window stated.
- **Grouped** (by assignee, loss type, region) → grouped tables with subtotals.
- A **dashboard** → a self-contained one-pager (HTML prints well) with the key counts, a recency
  breakdown, and the notable lists (stalled, new intake).

Ask whether they want a polished file or a quick in-chat readout. For any file, keep it neutral; ask once
for a company name only if it's going to be shared outside the team.

### Follow-through

Workspace reports are a launchpad. When a project surfaces that clearly needs action — a stalled job, one
with obvious documentation gaps, or one with no estimate — offer the next step and, where useful, its
`cloud_url` (from `get_project_snapshot`) so the user can jump straight in, or hand it to the
project-summary, drying-report, or estimate-status skill.

## Principles

- Page through everything before reporting counts; a partial page is a wrong count.
- State the filter, window, and total behind every number so the user can trust it.
- Be honest about cost/caps on deep posture reports; never imply full coverage you didn't do.
