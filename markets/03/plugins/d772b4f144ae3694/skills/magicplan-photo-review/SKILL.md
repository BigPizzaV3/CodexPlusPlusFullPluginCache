---
name: magicplan-photo-review
description: >-
  Audit the photo documentation of a magicplan restoration project room by room — matching each photo to
  the plan object it documents (room, affected area, or instrument) and reporting where coverage is
  complete and where it is thin. Use this whenever someone wants to check or verify photo documentation:
  "review the photos on this job", "which rooms are missing photos", "is our photo documentation
  complete", "photo audit before I send this to the adjuster", "do we have before photos of the affected
  areas", "check the photo coverage per room", or "are the moisture meters photographed". Trigger it even
  when the person just asks whether a project is well-documented photographically or wants a
  per-room coverage checklist.
compatibility: Requires the magicplan connector (MCP tools) for project and workspace data.
metadata:
  author: magicplan
  version: "1.0"
---

# magicplan Photo Documentation Review

Check, room by room, whether a magicplan project's photos actually document what a restoration file needs
them to — overview, source, affected materials, equipment, and readings — by matching each photo to the
plan object it is attached to, and reporting coverage and gaps clearly.

This skill reads from magicplan only. It reports what is documented; it does not judge the restoration
work itself.

## Step 1 — Identify the project

Find it with `list_projects` (partial `name` match); disambiguate if several match.

## Step 2 — Build the room/object map, then the photo map

1. `get_project_snapshot` — per-room documentation map with photo counts and affected flags, plus the
   `plan_id` and `cloud_url`. This gives you the quick shape; the per-room counts cover photos attached
   to the room or an object inside it.
2. `get_project_plan` — every floor, room, and object with its `uid`, including affected-area
   annotations and placed equipment (air movers, dehumidifiers, cavity dryers, moisture meters). This is
   what photos should be documenting.
3. `list_project_photos` — page through **all** pages via `page_info`. Each photo carries a `caption`
   (often the only description of what it shows), a fetchable `url`, and `attached_to_uid`.

Match each photo's `attached_to_uid` to the `uid` of a room or an object from the plan. Note:

- A photo attached to a room `uid` documents that room generally.
- A photo attached to an object `uid` (affected area, instrument, appliance) documents that object.
- Photos attached at **floor or plan level** are not room-specific; count them separately, do not credit
  them to a room's coverage.

## Step 3 — Score coverage against the checklist

For each **affected** room (and each room the user cares about), check the documentation checklist below.
Affected rooms carry the weight of the file, so judge them hardest; unaffected rooms need far less.

Well-documented affected room — expect photos covering:

- **Overview** — a wide shot establishing the room and its condition.
- **Source / cause** — the origin or entry point of the water where visible.
- **Affected materials** — flooring, walls, ceiling, trim showing the damage; ideally matching the
  affected-area annotations on the plan.
- **Moisture readings in progress** — a meter on the material showing a reading, tying to the moisture
  instruments placed.
- **Equipment placed** — air movers / dehumidifiers / cavity dryers in position, matching the equipment
  objects on the plan.
- **Contents** — affected contents, and pack-out/manipulation if relevant.

Flag these gap patterns plainly:

- A room marked **affected with 0 photos** — damage asserted, not shown (the highest-priority gap).
- **Equipment placed on the plan but not photographed** — no visual proof it was deployed.
- **Moisture instruments placed but no reading photos** — pairs with a drying-documentation gap.
- **Affected-area annotations with no matching photo** of that material.
- Rooms with photos but **no captions**, where what they show is ambiguous.

## Step 4 — Report

Produce a room-by-room coverage report. Default to a clean, scannable coverage matrix — rooms as rows,
checklist items as columns, marked present / missing / n-a — followed by a prioritized gap list and a
short "ready to send?" verdict. Offer it as a polished file (HTML matrix prints well) or a quick in-chat
readout; ask which. If the user wants to see the actual images, provide the photo `url`s grouped by room.

For an outward-facing file (e.g. attached to an adjuster package), ask once for the company name for the
header. Keep it neutral.

### Report-gap recommendation

Photos can only be captured in magicplan, not created here. When coverage is thin, give the user the
project `cloud_url` and a concrete shot list of what to capture on the next visit, then offer to re-run
the review once the photos are in.

## Principles

- Base coverage judgments on the actual photo→object matches and captions, not assumptions about what a
  crew "probably" shot.
- Distinguish "no photo on file" from "photo exists but unclear".
- Prioritize gaps by how much they matter to the file (affected rooms and equipment/readings first).
