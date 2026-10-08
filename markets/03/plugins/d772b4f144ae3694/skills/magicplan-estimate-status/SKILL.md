---
name: magicplan-estimate-status
description: >-
  Surface the status of estimates in a magicplan project or across the workspace at a glance — which
  estimates exist, their status (draft, sent, approved, etc.), what they cover, and what's outstanding —
  without opening each one by hand. Use this whenever someone wants an estimate overview or to find work
  that needs action: "what's the status of the estimates on this job", "which estimates are still in
  draft", "show me all open estimates", "what estimates are waiting on approval", "estimate status across
  my projects", "which projects don't have an estimate yet", or "what needs to go out". Trigger it
  whenever the focus is estimate status, outstanding estimates, or estimate coverage rather than building
  a new estimate.
compatibility: Requires the magicplan connector (MCP tools) for project and workspace data.
metadata:
  author: magicplan
  version: "1.0"
---

# magicplan Estimate Status

Give a fast, honest read on where estimates stand — for one project or across the workspace — so the user
can see what's drafted, what's out, what's approved, and what still needs attention, without opening each
estimate manually.

This skill reads from magicplan only and never changes workspace data.

## Step 1 — Set the scope

Decide whether the user means **one project** or **across the workspace**, and ask if it's unclear. A
single project is one snapshot; a workspace sweep is many calls, so confirm before a broad run.

## Step 2a — Single project

1. `list_projects` (partial `name` match) to find it; disambiguate if needed.
2. `get_project_snapshot` — returns the project's estimates with their status, newest first, plus the
   `cloud_url`. This alone answers most status questions.
3. `get_estimate` — only for the estimates where the user needs the detail: line items, totals, and what
   the estimate covers. Use this to spot outstanding items (see Step 3).

## Step 2b — Across the workspace

1. `get_workspace` to confirm context, then `list_projects`, **paging through all** results via
   `page_info`. Apply `name`/`email`/`sort` filters if the user narrowed the scope.
2. For each project in scope, read its estimates from `get_project_snapshot` (and `list_estimates` /
   `get_estimate` where more detail is needed). This is one-or-more calls per project — **tell the user
   how many projects you'll sweep, cap it sensibly, and don't silently truncate.** If they only care about
   a status (e.g. "all drafts"), you can often answer from the snapshot's estimate list without pulling
   every estimate's line items.

## Step 3 — Read status and what's outstanding

For each estimate, capture its **status** and, where the user needs it, what it **covers** and what's
**outstanding**. Outstanding / needs-attention signals include:

- Estimates still in **draft** (not sent) — especially on older projects.
- Estimates **sent** and awaiting a response for a while.
- Projects with **affected rooms but no estimate at all**.
- An estimate that **doesn't cover every affected room** (compare its coverage against the affected rooms
  from `get_project_snapshot` / `get_project_plan`).
- Rejected or superseded estimates needing a revision.

Sort the output by attention needed, so the most actionable items are at the top.

## Step 4 — Deliver

Default to a compact **status table** — project, estimate, status, coverage, and a short "next action" —
sorted by what needs attention first, with a one-line headline (e.g. "3 drafts unsent, 2 projects with no
estimate"). Offer a polished file or a quick in-chat readout. For each item that needs action, include the
project `cloud_url` so the user can jump straight to it, or hand it to the mitigation-scope skill to build
a missing estimate's scope.

## Principles

- Answer at the cheapest level that's accurate — the snapshot's estimate list before per-estimate detail.
- Page through everything before making "all"/"none"/count claims across the workspace.
- Be explicit about any cap on a workspace sweep; never imply full coverage you didn't do.
- Report status as it is; don't opine on whether an estimate's amount is right.
