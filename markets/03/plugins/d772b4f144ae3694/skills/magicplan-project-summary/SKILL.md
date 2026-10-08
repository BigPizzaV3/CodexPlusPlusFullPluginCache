---
name: magicplan-project-summary
description: >-
  Produce a detailed, purpose-driven summary of a magicplan restoration project — rooms, affected
  areas, measurements, and documentation status (photos, moisture readings, forms, estimates, files),
  including the gaps. Use this whenever someone wants to understand, summarize, brief, or catch up on a
  magicplan project: "summarize project X", "what's the situation on the Barbaro loss", "brief me before
  my client call", "give me an overview of this job", "catch me up on unit 6188302", "write a status
  email about this project", or "prep me for the adjuster". Trigger it even when the person only names a
  project and asks "what's going on here" — the whole point is to turn raw magicplan documentation into a
  summary shaped for how they are about to use it (client call, email, internal brief, or quick status).
compatibility: Requires the magicplan connector (MCP tools) for project and workspace data.
metadata:
  author: magicplan
  version: "1.0"
---

# magicplan Project Summary

Turn the documentation captured in a magicplan project into a clear summary shaped for how the user is
about to use it. A summary for a client phone call sounds nothing like an insurer-facing status email,
so the work is two parts: first read the project completely and honestly, then package it for the
purpose.

This skill only reads from magicplan; it never changes workspace data. Report what the documentation
shows, keep observed facts separate from your own inferences, and leave coverage decisions to the
carrier and adjuster.

## Step 1 — Identify the project

If the user named a project, find it with `list_projects` (use the `name` filter — partial matches
work). If the name is vague or returns several hits, show the candidates (name, address, last modified)
and ask which one before going further. If they gave no project, ask for a name, address, or assignee
email rather than guessing.

## Step 2 — Read the project completely

Always start with `get_project_snapshot` — it returns project details, a per-room documentation map
(whether each room is affected, its photo count, and how many moisture instruments were placed), the
`plan_id`, the estimates, and a `cloud_url` deep link to the project. Then fill in the detail with the
other tools as the purpose requires:

- `get_project_plan` — claim attributes (carrier, claim number, category/class of loss), and per floor
  and room the field values, placed objects, equipment, and **affected-area annotations with their
  notes**. This is where the actual damage description lives.
- `get_plan_statistics` (needs the `plan_id`) — floor and wall areas, ceiling heights, volumes, door/
  window/furniture counts, per room.
- `get_moisture_readings` (needs the `plan_id`) — drying history per instrument. An instrument with an
  empty readings list was placed but never read: a drying-documentation gap, not something to omit.
- `list_project_photos` — photo evidence, with captions and the `attached_to_uid` linking each photo to
  a plan object. Page through `page_info` if there are many.
- `get_plan_forms` (needs the `plan_id`) — completed workspace custom forms (intake, room condition).
- `list_project_files` — reports, third-party assessments, and other documents already on file.
- `list_estimates` / `get_estimate` — estimate posture and, if needed, line items.

For a quick status you may not need every tool; for a full pre-call or pre-handoff brief, read them all.

## Step 3 — Assess documentation status and gaps

The documentation status is often the most useful part of the summary, so make it explicit. For each
affected room, check whether it has photos, moisture readings (if instruments were placed), and a
condition form. Flag these patterns plainly:

- A room marked **affected** with **0 photos** — the damage is asserted but not shown.
- Moisture **instruments placed but with no readings** — no drying evidence.
- **Empty claim attributes** — no carrier, claim number, category, or class of loss set.
- **No estimate** created, or an estimate that does not cover an affected room.
- Rooms present in the plan but never marked affected and never photographed — condition unrecorded
  rather than confirmed clear.

Name gaps as facts ("no moisture readings are on file"), not as failures or accusations.

## Step 4 — Ask what the summary is for

Before writing the summary, ask the user the purpose, because it changes the tone, length, and format.
Offer these modes (single choice), and let them describe something else:

- **Client call prep** — a talking-points brief you can glance at while on the phone.
- **Client email / update** — a ready-to-send written message with a subject line.
- **Internal team brief** — an operational catch-up for a colleague or crew.
- **Adjuster / carrier status** — a neutral, factual status suitable for the insurer.
- **Quick status** — a short in-chat readout, no file.

Read `references/output-modes.md` for the structure of each mode. Match the depth of your Step 2 reading
to the mode they choose.

For any outward-facing document (client email, adjuster status, or a client-call leave-behind), ask once
for the **company name and contact details** to put in the header — these skills are used by many
restoration companies, so never assume a brand. Keep the output otherwise neutral.

## Step 5 — Deliver

Unless they chose a quick in-chat status, produce a polished file in the fitting format (a clean written
document for emails and briefs; a scannable one-pager for call prep) and hand it over. Keep the
in-chat message to a one-line summary plus any critical gaps they should know before they use it.

### Report-gap recommendation

magicplan can generate formal reports and estimates that this skill cannot create for the user. When the
summary would be stronger with something that does not yet exist — no estimate on file, no formal report
document, thin photo coverage — tell the user and give them the project's `cloud_url` so they can
generate or capture it in magicplan, then offer to fold the result into the summary once it exists. For
example: "There's no estimate on this project yet. You can build one here: <cloud_url>. Once it's in,
I can add its totals and status to this summary."

## Principles

- Separate **documented facts** (from forms, photos, readings, measurements) from **assumptions** you
  are making to fill gaps, and label the assumptions.
- Never invent measurements, readings, dates, or claim details. If it is not in the data, say so.
- Convert units to the audience's expectation when helpful, and state the conversion.
- This skill works with whatever assistant and file tools are available; if a document-creation
  capability is present, use it for the polished deliverable, otherwise deliver clean formatted text.
