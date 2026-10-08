# Drying Standards & Report Structure (IICRC S500-aligned)

This reference explains how to interpret magicplan moisture data against accepted structural-drying
principles, and gives the exact report structure to produce. It is guidance for documenting conditions,
not a certification standard.

## Table of contents
1. Core drying concepts
2. Reading the magicplan moisture data
3. Equipment adequacy rules of thumb
4. How to judge progress
5. Report structure
6. Tone and evidence rules

---

## 1. Core drying concepts

- **Dry standard (drying goal):** the moisture level a wet material must reach to be considered dry.
  Established by measuring an equivalent **unaffected reference** material of the same type elsewhere in
  the structure, or by a documented pre-loss/industry benchmark. Drying is complete when affected
  materials reach the dry standard, not after a fixed number of days.
- **Category of water** (1 clean, 2 grey, 3 black) and **Class** (1–4, the amount of water and how much
  wet porous material is involved) drive how aggressive drying must be. Category/class come from the plan
  attributes when set; if not set, note the assumption.
- **Psychrometrics:** drying works by keeping the air's ability to hold moisture (measured as **grains
  per pound / humidity ratio**, plus temperature and relative humidity) higher in capacity than the
  moisture leaving the materials. Compare **affected-area** air to **reference/outside** air: the drying
  system should be pulling the affected space drier than it would be otherwise.
- **Daily monitoring:** S500 expects moisture and atmospheric readings taken and recorded on each visit
  so progress is demonstrable. A single reading, or a placed-but-unread meter, does not document drying.

## 2. Reading the magicplan moisture data

`get_moisture_readings` returns per instrument: floor, room, and a dated series with moisture content,
material and its relative scale, air temperature, surface temperature, relative humidity, and humidity
ratio. For each instrument:

- Sort the series by date. The first entry is the **initial reading**, the last is **current**.
- Identify the **material** so you can pair it with a sensible dry standard and reference.
- If an instrument is a reference/unaffected point, use it as the dry-standard basis for like materials.
- An **empty readings list** = placed but never read: a gap, not a reading of zero.

Atmospheric/psychrometric daily logs may instead live in `get_plan_forms` (custom forms). Merge those:
typical logged points are Outside, Unaffected (reference), Affected, and Dehumidifier outlet, each with
temperature/RH and often grains per pound.

## 3. Equipment adequacy rules of thumb

Use these as sanity checks against the equipment placed on the plan (from `get_project_plan`). Present
findings as a check with the assumptions shown, never as a pass/fail verdict.

- **Air movers (Class 2 example):** roughly one air mover per 50–60 sq ft of affected floor, plus one
  per affected wall, adjusted for offsets and contents. More for higher classes.
- **Dehumidification:** estimate required capacity from the affected volume and the target grain
  depression; compare against the rated capacity of the units placed. Note if placed capacity is well
  under or over the estimate.
- **Cavity / specialty drying:** wall-cavity injection, floor/wood-floor mat systems, etc. should appear
  where the migration path or assembly requires them (e.g. wet wall cavities, floating floors over slab).

## 4. How to judge progress

For each affected material, classify current state from the data:

- **Dry standard reached** — current MC at or below the dry standard/reference.
- **Trending to dry** — MC falling across recent readings, above standard.
- **Stalled** — little/no change across recent readings.
- **Rising / anomalous** — MC up, or atmospheric conditions worsening; flag for attention.
- **Undocumented** — no baseline or no readings; cannot be judged.

Report a plain-language **estimated completion** only when the trend supports it, and label it an
estimate. Never assert a job is dry without readings that show it.

## 5. Report structure

Use this structure for the deliverable:

```
# Structural Drying Report — [Property / claim reference]
[Company name] · [contact] · Report date: [date]
Loss type / category / class: [values or "not recorded"]

## 1. Summary
[3–5 sentences: overall drying status, how many affected materials have reached dry standard, expected
completion if supportable, and the single most important gap or risk.]

## 2. Scope of monitoring
Rooms monitored, instruments placed, monitoring period (first→last reading date), number of visits.

## 3. Atmospheric conditions
Table/chart of daily psychrometric readings (Outside, Reference, Affected, Dehu outlet) where available,
with a note on whether the system is depressing grains in the affected area.

## 4. Room-by-room moisture progress
For each affected room:
  - Materials monitored and their dry standard (with the reference basis, or "undocumented").
  - Per-instrument table: date series of moisture content (+ trend), and current vs. standard.
  - A moisture-content-over-time chart where possible.
  - Equipment placed in the room and an adequacy note.
  - Status: reached dry / trending / stalled / undocumented.

## 5. Documentation gaps & open items
Explicit list: unread instruments, missing dry standards, missing initial readings, monitoring gaps,
affected rooms with no instruments.

## 6. Method notes
Units and any conversions; that findings reflect readings on file; S500 principles referenced.
```

## 6. Tone and evidence rules

- Documented readings and interpretation are kept visibly separate.
- No fabricated readings, dates, standards, or completion claims.
- Gaps are stated as facts, neutrally.
- The report documents conditions; it does not certify the job or decide coverage.
