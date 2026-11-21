---
name: spline-3d-boolean-operations
description: "Boolean (CSG) operations: carving holes, windows and tunnels with subtract(), merging shapes with union(), keeping overlaps with intersect() — operand ordering (which object survives a subtract), live editing of operands, adding cutters later, materials on the result, closed-geometry rules, and performance. Load for prompts like \"make a hole\", \"cut out\", \"carve\", \"boolean\", \"subtract\", \"hollow out\", \"window in a wall\", \"tunnel\", \"merge these shapes\"."
---

# Boolean operations (CSG)

A Boolean combines 2+ meshes into ONE object by union, subtraction, or
intersection — THE tool for holes, windows, tunnels, mugs, arches, and any
shape the primitives can't express by stacking alone. It is LIVE: the operand
meshes become CHILDREN of the Boolean object and keep their own geometry and
transforms — move/scale/animate a child and the result recomputes. Only the
combined result renders; the children stop rendering individually.

Booleans are HARD-EDGED and exact. If the merge should look SOFT and organic
— shapes melting into each other like goo, liquid, or clay — that is a Shape
Blend, not a Boolean: use `shapeBlend(...)` and load the `shape-blends`
skill instead.

## Create — ALWAYS two run_code calls

Building a Boolean needs the operands' runtime bounding boxes, which only
exist for objects created BEFORE the current run_code call. So the flow is
always: create (and name) the operand meshes in one call, combine them in the
NEXT call. First call:
```
mesh('Cube', { width: 300, height: 300, depth: 300 });
rename('Block');
mesh('Cylinder', { radius: 60, height: 400 });
rotation({ x: 90 });                 // aim the cutter along Z, through the cube
rename('Drill');
```
Second call:
```
subtract(['Block', 'Drill']);
rename('Block with hole');
```
- `boolean(operation, target?)` — wrap the targeted meshes (or the current
  selection) into a new Boolean. `operation`: `'union'` | `'subtract'` |
  `'intersect'`. `subtract(target?)` / `union(target?)` /
  `intersect(target?)` are one-word shorthands for the same thing.
- Reference operands by NAME or id in the combining call (`rename` them at
  creation so the names are unambiguous). Objects from a `select(...)` in
  the combining call also work — they existed before it. Passing a `mesh()`
  return (or relying on its auto-selection) from the SAME call throws
  "cannot build a boolean with …" — that error always means: split the
  creation and the boolean into separate calls.
- Omitting the target uses the current selection (pre-existing objects only,
  same rule).
- Non-mesh targets (lights, cameras, Empties) are ignored; a Boolean operates
  on meshes only. Do NOT try `mesh('Boolean')` — it creates an empty Boolean
  with no operands, which renders nothing.
- Like `group`, the call RETURNS the new Boolean object, so `rename` right
  after applies to it. A freshly created Boolean is itself subject to the
  two-call rule: to use it as an operand of ANOTHER boolean (nesting), do
  that in yet another call.

## Subtract order — which object survives

For `subtract`, the BASE (the object that survives, with the others carved
out of it) is the BOTTOM child in the scene tree. New objects are inserted at
the TOP of the tree, so among freshly created meshes the base is the one you
created FIRST: create the solid first, then the cutters. Selection order does
NOT matter — only tree order does.

If the order is wrong (you subtracted the block from the drill), fix it by
reordering the children: `moveInto(theBoolean, 'Cutter', { before: 'Base' })`
— the last child is the base. `union`/`intersect` are symmetric; order never
matters for them.

Cutters should PROTRUDE clean through the base — make them longer/deeper than
the wall they pierce (the 400-tall drill vs the 300 cube above). Never leave a
cutter face exactly flush with a base face: coplanar faces make the CSG
ambiguous and the surface flickery. Overshoot by a few units.

## Edit after creation

- Operation: with ONE existing Boolean selected/targeted, `boolean(op)`
  changes its operation in place — `boolean('intersect', 'Block with hole')`
  retypes it, no re-wrapping.
- Operands: they're normal children — `select(o => o.id === '<childId>')`
  (ids from `get_scene`, where they're listed with the Boolean as parent),
  then transform as usual. Moving the drill moves the hole. `animate` on a
  child transform = an animated hole.
- Add a cutter later: create the mesh in one call, then reparent it in the
  NEXT call — for a subtract, keep the base LAST:
  `moveInto('Block with hole', 'New cutter', { before: 'Drill' })`. Plain
  `moveInto` appends last, which would silently make the new mesh the base.
- Remove a cutter: `moveInto('root', cutter)` pulls it back out (world
  transform preserved), or `remove(cutter)` deletes it.
- Dissolve: `ungroup(theBoolean)` frees the operands back into plain meshes
  and deletes the Boolean wrapper.
- Nesting works: a Boolean can be an operand of another Boolean (the mug
  recipe below). Booleans transform like any mesh — `position`/`rotation`/
  `scale`/`group`/`animate` on the Boolean move the whole result.

## Materials

The result renders with the Boolean object's OWN single material (seeded from
the base operand's material at creation). Recoloring a child changes nothing
visible — select the BOOLEAN and use `color`/`layer`/`shading` as usual.

Shading of cut edges: `geometry({ phongAngle: 60 })` on the selected Boolean
raises the smooth-shading angle (default 35) — raise it if a curved cut looks
faceted, lower it toward 0 for deliberately crisp facets.

## Closed geometry — the rule that breaks booleans

Operands must be CLOSED solids (watertight). An operand with open edges is
silently DROPPED from the result (only a subtract's base may be open):
- Flat shapes (`Plane`, `Rectangle`, `Ellipse`, `Polygon`, `Star`,
  `Triangle`) have no volume — give them a `depth` (extrude) before using
  them as operands. A cutter that "does nothing" is almost always this.
- Avoid `openEnded: true` cylinders/cones as operands.
- Primitives, extruded shapes, extruded `Text`, and Toruses are fine.
If the result looks like plain union-less overlap or a cutter has no effect,
check these before anything else; also confirm the operands actually overlap
(`get_scene` positions + `size`).

## Recipes

Window in a wall (multiple cutters, one subtract). Call 1 — create + name:
```
mesh('Cube', { width: 800, height: 400, depth: 24 });
rename('Wall base');
mesh('Cube', { width: 160, height: 200, depth: 60 });
translate({ x: -180, y: 30 });
rename('Window L');
mesh('Cube', { width: 160, height: 200, depth: 60 });
translate({ x: 180, y: 30 });
rename('Window R');
```
Call 2 — combine:
```
subtract(['Wall base', 'Window L', 'Window R']);
rename('Wall');
```
All children above the base are carved out in one operation — one Boolean,
not one per cutter. (Cutter depth 60 > wall 24: clean through-cuts.)

Mug (hollow with subtract, then union the handle onto the Boolean — nesting
needs its own extra call). Call 1 — the parts:
```
mesh('Cylinder', { radius: 90, height: 220 });
rename('Body');
mesh('Cylinder', { radius: 78, height: 220 });
translate({ y: 24 });                    // leaves a floor; rim overshoots
rename('Bore');
mesh('Torus', { width: 130, height: 130 });
translate({ x: 100 });                   // sink it into the cup wall
rename('Handle');
```
Call 2 — hollow: `subtract(['Body', 'Bore']); rename('Cup');`
Call 3 — attach: `union(['Cup', 'Handle']); rename('Mug');`

Lens / rounded tile: `intersect` two overlapping spheres (or a sphere and a
cube) — the shared volume is the result.

## Performance

The result recomputes live whenever an operand changes — cost scales with
triangle counts. Keep operand segment counts modest (a 24-segment sphere cuts
like a 64-segment one, far cheaper); prefer animating child `scale`/position
over geometry `width`/`height`/`depth`; don't stack dozens of live Booleans
when one subtract with several cutters does the job.

## Verifying

`run_code` reports the Boolean's id; `get_scene` shows it as a Mesh with
geometryType `BooleanGeometry`, its `size` being the RESULT's real bounds —
an intersect that missed (no overlap) reads as size ~0 there. A hole doesn't
change the bounds, so judge cuts visually: `set_view` + `take_screenshot`
from an angle that FACES the cut — a hole reads as nothing from the side.
