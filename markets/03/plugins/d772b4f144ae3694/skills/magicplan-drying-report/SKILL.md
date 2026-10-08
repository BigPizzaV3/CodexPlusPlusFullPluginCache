---
name: magicplan-drying-report
description: >-
  Build a professional structural drying / moisture-progress report from a magicplan project's moisture
  instruments and atmospheric readings, aligned to IICRC S500 principles. Use this whenever someone wants
  to review, document, or report drying progress on a water-damage job: "generate a drying report",
  "how's the dry-out going on the Barbaro job", "pull the moisture readings into a report", "is it dry
  yet", "daily drying log", "psychrometric report", "show me the drying progress", "document the drying
  for the file", or "S500 drying documentation". Trigger it even when the person just asks whether a job
  has reached dry standard or wants the moisture history turned into something shareable.
compatibility: Requires the magicplan connector (MCP tools) for project and workspace data.
metadata:
  author: magicplan
  version: "1.0"
---

# magicplan Drying Report

Turn the moisture and atmospheric readings captured in a magicplan project into a clear structural
drying report that shows, room by room and instrument by instrument, where each material started, where
it is now, and whether it has reached a dry standard — evaluated against IICRC S500 drying principles.

This skill reads from magicplan only; it never changes workspace data. The report documents what the
readings show. State drying facts plainly, flag documentation gaps honestly, and leave restoration
method and coverage decisions to the professional and the carrier.

## Step 1 — Identify the project and pull the drying data

Find the project with `list_projects` (partial `name` match); disambiguate if several match. Then:

1. `get_project_snapshot` — project details, per-room documentation map, the `plan_id`, and the
   `cloud_url` deep link.
2. `get_moisture_readings` (needs the `plan_id`) — the core input. Returns one entry per instrument,
   localized to its floor and room, with a dated series: moisture content, material and relative scale,
   air and surface temperature, relative humidity, and humidity ratio. **Instruments placed but not yet
   read appear with an empty readings list** — keep them in the report as gaps.
3. `get_plan_forms` (needs the `plan_id`) — some crews log daily atmospheric/psychrometric readings
   (outside, unaffected/reference, affected, dehumidifier outlet) in workspace custom forms rather than
   on instruments. Check here and fold any drying-relevant forms into the report.
4. `get_plan_statistics` and `get_project_plan` — room dimensions, volumes, and the drying equipment
   placed (air movers, dehumidifiers, cavity dryers) plus affected-area notes, for context and equipment
   adequacy commentary.

## Step 2 — Understand the drying picture

Read `references/drying-standards.md` for how to interpret readings against S500 before you write. In
brief, for each material/instrument establish, from the data:

- The **dry standard / goal** — the target moisture content, ideally from a reference (unaffected
  material of the same type). If none is recorded, say the dry standard is undocumented rather than
  inventing one.
- The **initial reading** and the **most recent reading**, the **trend** across the dated series, and
  whether the material has **reached dry standard**, is **trending down**, or is **stalled/rising**.
- **Atmospheric conditions** — whether the affected-area humidity ratio (grains per pound) is being
  pulled below the reference/outside air, i.e. whether the drying system is actually removing moisture.
- **Equipment adequacy** — a sanity check of air movers and dehumidifier capacity against the affected
  area and volume (see the reference file for the S500 rules of thumb). Present this as a check, not a
  verdict.

## Step 3 — Handle the gaps explicitly

Drying files are frequently incomplete, and a report that hides that is worse than useless if a carrier
reviews it. Call out, as plain facts:

- Instruments **placed but never read** — no baseline, no progression.
- **No reference/dry-standard reading** for an affected material.
- **Missing daily readings** (gaps in the date series) — monitoring not continuous.
- **No initial reading** — the starting point is undocumented, so drying achieved cannot be proven.
- Affected rooms with **no instruments at all**.

## Step 4 — Produce the report

Build a polished, self-contained report using the exact structure in `references/drying-standards.md`
("Report structure"). Default to a clean, printable **HTML** document (single file, inline styles, no
external assets) because it renders anywhere and prints to PDF cleanly; offer Word or PDF instead if the
user prefers. Where charts help (a moisture-content-over-time line per room), include them; if charting
is not available, use clear per-day tables.

Ask once for the **company name and contact details** and the **client/property and claim reference** to
put in the header — these skills serve many restoration firms, so never assume branding. Keep the body
neutral and factual.

### Report-gap recommendation

If the drying data is too thin to support a defensible report — for example, every instrument has an
empty readings series — say so directly, give the user the project `cloud_url` so they can capture
readings in magicplan, and offer to generate the report once readings exist. A report that asserts
drying without readings is a liability, so never manufacture progression to fill the page.

## Principles

- Never invent readings, dates, dry standards, or trends. Missing data is reported as missing.
- Distinguish **documented readings** from **your interpretation** of them.
- Use the client's/region's unit expectation; state any conversion (e.g. metric plan → imperial report).
- Keep S500 references as supporting rationale, not as a compliance certification — you are documenting
  conditions, not certifying the job.
