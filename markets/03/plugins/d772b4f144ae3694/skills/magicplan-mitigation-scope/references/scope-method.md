# Mitigation Scope Method (IICRC S500-aligned)

How to turn magicplan plan statistics and the clarifying answers into a defensible, price-free mitigation
scope. This is estimating guidance for documenting quantities, not a certification standard.

## Table of contents
1. Category & class of loss
2. Working with the price list
3. Unit conversions
4. Line-item families
5. Quantity derivation rules
6. How the clarifying answers change the scope
7. Scope document template
8. Golden rules

---

## 1. Category & class of loss

- **Category** — the cleanliness of the water. **Cat 1** clean (supply line, rainwater); **Cat 2** grey
  (appliance discharge, some contamination); **Cat 3** black (sewage, ground surface water, long-standing
  losses). Category rises with time and contamination.
- **Class** — how much water and wet porous material. **Class 1** least (minimal absorption); **Class 2**
  an entire room, water wicked up walls < ~24 in; **Class 3** greatest (water from above, saturated walls
  and ceilings); **Class 4** specialty drying (deep-bound moisture in low-permeance materials — hardwood,
  plaster, concrete).

Read category/class from the plan attributes when set. If not set, ask, or reason from the affected-area
notes and photos and **label it assumed**. Category drives whether antimicrobial, air scrubbing, and
Cat-specific tear-out variants apply; class drives equipment density and specialty drying.

## 2. Working with the price list

- Load the user's list (CSV/Excel/PDF). Index it by **code/SKU**, **description**, and **unit**; keep any
  category/selector metadata for matching. Ignore price columns entirely — the scope carries none.
- Match each derived line to the closest item by description **and** unit. Carry the user's exact SKU and
  unit into the scope; do not rename their items.
- Prefer the price list's own granularity: if their list splits "air mover — no monitoring" from
  "air mover — with monitoring", pick the one matching the answers.
- If no clean match exists for a needed item, include the line with a placeholder like `[MAP: air mover
  per 24 hr]` and flag it for the user to map. Never guess a real SKU.
- If the user has no list, use the generic families in section 4 as placeholder codes.

## 3. Unit conversions

magicplan plans are often metric; many price lists are imperial. Convert consistently and state it:

- Area: 1 m² = 10.7639 SF
- Length: 1 m = 3.28084 LF
- Volume: 1 m³ = 35.3147 CF

Common units: **SF** (surface/floor area), **LF** (linear feet), **CF** (cubic feet), **EA** (each),
**DA** (day, for per-24hr equipment), **HR** (hours). Match the unit the price-list item expects.

## 4. Line-item families

Group the scope into these phases (include only what applies):

1. **Emergency response & documentation** — emergency service call, thermal/moisture mapping (bid item),
   calcium-chloride moisture tests (per sample, esp. concrete slabs).
2. **Extraction** — water extraction from hard-surface floor / from carpet & pad (per SF of affected
   floor).
3. **Access, protection & containment** — baseboard detach & reset (LF), containment barrier / airlock
   (SF), peel-&-seal zippers (EA), floor protection (SF), block & pad / move furniture (EA).
4. **Tear-out & detach/reset** — drywall/ceiling removal, insulation removal, flooring removal, trim,
   etc., in the category-appropriate variant (see section 6). Only when the approach is "remove".
5. **Drying equipment (per 24 hr)** — air movers, dehumidifiers (LGR / conventional, sized by ppd),
   wall-cavity drying (injection, per day), drill holes + fill holes for cavity drying (EA), wood/hard
   floor drying mat systems + add-on kits (per day).
6. **Specialty drying** — Class 4 / low-permeance systems where indicated.
7. **Monitoring & setup** — equipment setup, takedown, and monitoring (HR); remote monitoring system
   (per day) where used.
8. **PPE & consumables** — gloves, goggles, suits (add if the carrier itemizes).
9. **Category-specific** — antimicrobial / biological cleaning agent (SF), negative air / air scrubber
   (per day) — **for Cat 2/3, not Cat 1**. List Cat-1-excluded items separately for reference.

## 5. Quantity derivation rules

Use the plan statistics and affected-area annotations. Show the basis for every quantity.

- **Extraction** = affected floor area (SF) per room. Offer the room-wide floor area as an alternative if
  extraction is scoped room-wide rather than to the annotated wet area.
- **Air movers (S500 rule of thumb, Class 2):** ~1 per 50–60 SF of affected floor, **plus** 1 per
  affected wall; adjust up for higher classes, offsets, and contents. Multiply by drying days for line
  quantity (e.g. 3 units × 3 days = 9 unit-days). Show the calculation.
- **Dehumidifiers:** cross-check capacity against affected volume. A common Class 2 approach: required
  pints/day ≈ affected volume (CF) ÷ an LGR factor (~50 for Class 2), giving AHAM ppd; pick units whose
  rated ppd meets it. If the plan already has units placed, scope what's placed but note whether it meets
  the calculation, and offer the calculated quantity as the alternative.
- **Baseboard detach & reset (LF)** = length of the base of affected walls. Offer full room perimeter as
  an alternative if cavity drying extends to all walls.
- **Containment barrier / airlock (SF)** = doorway opening area(s) being sealed; peel-&-seal zipper = 1 EA
  per containment opening.
- **Floor protection (SF)** = equipment routing / traffic path area (e.g. a hall used for access).
- **Block & pad furniture (EA)** = per room; use the price list's small-amount variant for rooms with few
  items.
- **Wall cavity drying:** injection system per affected room per day; **drill holes (EA)** ≈ along
  affected wall bases at the material's typical spacing (e.g. ~400 mm / ~16 in centres); **fill holes
  (EA)** = matches drill holes.
- **Wood/hard floor drying mats:** 1 system per affected room per day when a floating/engineered floor
  over slab must be dried without lifting it; add-on kit per day for panel coverage across affected area.
- **Setup / takedown / monitoring (HR)** = set + (visits × per-visit time) + takedown. Use the answers on
  monitoring visits.
- **Moisture tests (EA)** = per sample; typical for concrete slabs where CC (calcium chloride) or
  concrete meters are in use.

Always present the primary quantity plus any credible **alternative** (annotated area vs. room-wide,
placed vs. calculated equipment, base-of-affected-walls vs. full perimeter), so the estimator can choose.

## 6. How the clarifying answers change the scope

- **Rooms in scope** — limits which rooms generate lines; an access-only room (e.g. hall) gets protection
  lines but not extraction/drying.
- **Dry in place vs. remove** — "dry in place" drops tear-out families and leans on drying + cavity
  systems; "remove" adds the tear-out family. If a ceiling is noted sagging/structurally compromised,
  dry-in-place may be inappropriate — flag it as an open issue rather than silently drying it.
- **Category / class** — Cat 2/3 adds antimicrobial + air scrubbing and shifts tear-out to the
  Cat-appropriate variant; higher class raises equipment density and may add specialty drying. If the
  loss could reclassify (e.g. long-standing leak → Cat 2), note what changes.
- **Floor / wall build-up** — determines whether floors dry in place (mat systems) or must be removed
  (glued vs. floating flooring over slab is the classic fork). Note if unverified.
- **Air movers / equipment** — "calculate per S500" produces calculated quantities (labelled calculated);
  "document only what's placed" mirrors the plan; "calculated, listed separately" gives both.
- **Duration** — multiplies per-24hr equipment and sets monitoring hours.
- **Units** — governs SF/LF/CF vs metric and the bracketed display.

## 7. Scope document template

Mirror this structure (the paired line-item sheet carries SKU, description, unit, qty, basis):

```
# Mitigation Scope of Work — [Property address]
Project: [name] · Plan floor: [floor] · Assessor: [name] · Documented: [date] · Scope prepared: [date]
Price list: [name/structure] — SKUs and quantities only, no prices

## Basis of scope
Table: Parameter | Value | Source. Rows: loss type, category/class (note if assumed), migration path,
floor build-up (note if assumed), approach (instructed/derived), equipment & monitoring basis, rooms in
scope, units. Then an "Excluded:" line listing what's out of scope.

## Measured quantities
Per affected room: magicplan UID, dimensions, ceiling height, floor/ceiling area, wall area (net of
openings), floor perimeter, volume, affected floor area, affected wall area, equipment on plan, furniture
count, photo count.

## Line items
Grouped by the families in section 4. Each line: SKU | Description | Unit | Qty | Basis. Add
"Alternative:" notes under a group where a credible alternative quantity exists.

## [Category] reference — not included, listed for reference
Items that would apply only under a different category/class (e.g. antimicrobial, air scrubber for a Cat 1
loss), so the estimator sees what changes if the loss reclassifies.

## Bid-item alternative
Where the list offers a lump structural-drying-per-SF/CF bid item as an alternative to itemized
equipment, show it — and note: use either the itemized equipment block OR the bid item, not both.

## Open issues affecting this scope
Numbered list of gaps and assumptions: missing moisture readings, unverified build-up, category assumed,
ceiling stability, calculated-vs-documented equipment, ceiling-height anomalies, thin photo evidence.
State plainly what each means for the scope.

## Method note
Unit conversions used; that quantities come from plan statistics and affected-area annotations; no prices,
O&P, tax, or minimum charges applied.
```

## 8. Golden rules

- No prices, ever. Quantities, SKUs, units, and basis only.
- Every quantity traces to a measurement, an annotation, or a stated assumption.
- Offer credible alternatives rather than forcing one interpretation.
- Name every gap in Open issues — a scope that hides its assumptions is not defensible.
- Carry the user's own SKUs/units; flag unmatched items for mapping instead of inventing codes.
