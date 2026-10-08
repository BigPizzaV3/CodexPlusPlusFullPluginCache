---
name: magicplan-mitigation-scope
description: >-
  Build a defensible water-damage mitigation scope of work from a magicplan project and the user's own
  price list — deriving line items (SKUs and quantities, no prices) through a short guided conversation,
  aligned to IICRC S500. Use this whenever someone wants to turn a magicplan loss into an estimate scope:
  "build a mitigation scope for this job", "derive the line items for the Stanton Close water damage",
  "scope this loss against my Xactimate price list", "what quantities should I estimate here", "create a
  scope of work from the plan", "help me estimate the drying for this project", or "turn this project
  into an itemized scope". Trigger it whenever the goal is an itemized mitigation scope or estimate from
  magicplan documentation — it will ask for the price list and clarify the situation before scoping.
compatibility: Requires the magicplan connector (MCP tools) for project and workspace data.
metadata:
  author: magicplan
  version: "1.0"
---

# magicplan Mitigation Scope of Work

Turn a magicplan water-damage project into a clean, defensible mitigation scope — the SKUs and quantities
an estimator needs, each tied to its basis in the plan — by reading the documentation, asking a short set
of clarifying questions, and mapping S500-driven quantities onto the user's own price list. The output
carries **no prices**: SKUs, descriptions, units, quantities, and the basis for each. Pricing, overhead,
tax, and minimums stay with the estimator and their price list.

This skill reads from magicplan only and never changes workspace data. It documents and reasons from what
the plan shows; where the plan is silent it asks or states an assumption. It does not decide coverage.

## Step 0 — Get the price list (required)

This skill needs the user's price list so the scope speaks in their SKUs and units. **Ask for it before
scoping.** Explain what's useful:

- Their price list export — Xactimate / Verisk structure, or any in-house list — as a file (CSV, Excel,
  or PDF) placed in the working folder or attached.
- It should include, at minimum, **item codes/SKUs, descriptions, and units**. Category/selector metadata
  helps matching. **Prices are not needed and will not be used** — reassure the user on this; the scope is
  quantities only.

Load and index the price list (see `references/scope-method.md`, "Working with the price list"). If the
user has no price list handy, offer to proceed with a **generic S500 line-item structure** they can map
to their list later, and make clear the codes will be generic placeholders.

## Step 1 — Load the project

Find it with `list_projects` (partial `name` match); disambiguate if several match. Then read it fully —
this scope is only as good as the reading behind it:

- `get_project_snapshot` — affected rooms, per-room documentation, `plan_id`, `cloud_url`.
- `get_project_plan` — claim attributes (carrier, claim #, **category/class of loss**), affected-area
  annotations **and their notes** (cause, migration path, material notes), and every placed object
  including equipment (air movers, dehumidifiers, cavity dryers, meters).
- `get_plan_statistics` (needs `plan_id`) — floor/wall areas, ceiling heights, volumes, perimeters,
  openings, per room. These are your quantity inputs.
- `get_moisture_readings` (needs `plan_id`) — instruments and readings (empty series = a gap).
- `list_project_photos` — captions/URLs that confirm materials and conditions; page through `page_info`.
- `get_plan_forms` (needs `plan_id`) — intake/room condition forms with extra field detail.

## Step 2 — Report what's documented and what's missing

Before asking questions, give the user a short two-part readout, exactly in this spirit:

- **Documented:** per affected room — dimensions, ceiling height, affected floor/wall area, migration
  path, materials noted, equipment placed, meters placed.
- **Gaps:** e.g. no claim attributes (carrier/claim #/category/class), zero moisture readings, no air
  movers placed, rooms on the loss floor not marked affected.

This mirrors how a good estimator orients before scoping, and it tells the user what the clarifying
questions are about to resolve.

## Step 3 — Ask the clarifying questions

The plan rarely records everything a scope needs, so ask a focused set of questions and let the user
steer. Present them as clear multiple-choice where possible (with an option to answer freely). Ask only
the ones the data leaves open; skip any the plan already answers. The core set:

1. **Rooms in scope** — which rooms the scope should cover (e.g. affected rooms only / whole loss floor /
   affected rooms + access route like a hall).
2. **Approach — dry in place vs. remove** — dry in place, detach & reset, or tear out; and how far (e.g.
   remove sagging ceiling + dry walls / flood-cut walls / dry in place throughout / let the moisture data
   decide).
3. **Category & class of loss** — if not set on the plan, which to scope against (Cat 1/2/3, Class 1–4).
   Offer "you tell me from the photos" and reason from the evidence if they prefer.
4. **Floor & wall build-up** — the actual assembly where the plan/meters don't say (e.g. carpet over
   slab / laminate-engineered over concrete / bare tiled concrete / check the photos). This drives
   whether floors can dry in place or must come up.
5. **Air movers / equipment** — when equipment is under-placed on the plan, whether to calculate per S500,
   document only what's placed, or calculate and list separately.
6. **Equipment & monitoring duration** — number of drying days and monitoring visits to scope (e.g.
   3 days + 3 visits / 5 days + 5 visits / per-day lines at qty 1 / "I'll give you the dates").
7. **Units** — the plan may be metric while the price list is imperial (SF/LF/CF). Convert to imperial,
   show metric with imperial in brackets, or keep metric.
8. **Deliverable** — how they want it handed over (see Step 6).

`references/scope-method.md` explains how each answer changes the scope.

## Step 4 — Derive quantities

Compute quantities from the plan statistics and the answers, following the S500 logic and formulas in
`references/scope-method.md`. Every line's quantity must have a traceable **basis** (e.g. "Bedroom —
primary, affected floor area", "3 units × 3 days", "400 mm centres along affected wall bases"). Where a
quantity depends on a choice the data can't settle (annotated affected area vs. room-wide), compute the
primary figure and offer the alternative in a note, as the reference shows.

## Step 5 — Map to the price list

Match each derived line to the user's price list by description and unit, and carry the user's **exact
SKU/code and unit**. Keep families together (emergency/documentation, extraction, access/protection/
containment, tear-out & detach/reset, drying equipment, specialty drying, monitoring, PPE, and any
category-specific items like antimicrobial or air scrubbing). If a needed item has no clear match, list it
with a clearly-marked placeholder code and flag it for the user to map. Never inject prices.

## Step 6 — Deliver

Produce the scope in the format the user chose. Default to a polished pair: a **line-item sheet**
(Excel/CSV: SKU, description, unit, quantity, basis — ready to import or paste into the price list) **plus
a short scope document** (the basis of scope, measured quantities, line items by phase, alternatives, and
open issues) using the template in `references/scope-method.md`. Offer alternatives: sheet only,
document only (markdown/HTML), or sheet + assumptions memo.

Always include an **Open issues** section listing the gaps and assumptions that affect the scope (missing
readings, unverified build-up, category assumed, ceiling stability, equipment calculated vs. documented).
This is what makes the scope defensible if a carrier reviews it.

### Report-gap recommendation

If the loss floor or affected areas are too thin to scope responsibly (e.g. no affected-area annotations,
no measurements), tell the user and give them the project `cloud_url` to complete the documentation in
magicplan, then offer to build the scope once it's there.

## Principles

- **No prices.** Quantities, SKUs, and basis only. Say so on the deliverable.
- Every quantity is traceable to a measurement, an annotation, or a stated assumption.
- Keep documented facts, S500 calculations, and user instructions distinguishable in the basis notes.
- State unit conversions; never silently mix metric and imperial.
- Reason from the photos and notes when asked, but label anything inferred rather than measured.
