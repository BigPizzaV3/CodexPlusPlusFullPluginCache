---
name: spline-3d-shape-blends
description: "Shape Blends (metaballs / SDF blending): melting meshes into ONE smooth organic surface with shapeBlend() — goo, blobs, liquid drops merging, lava lamps, slime, snowmen, clouds, soft cartoon bodies. Creating from member shapes, per-shape union/subtract/intersect, blend range tuning, the resolution budget, children-color gradients, and animating members so the goo morphs. Load for prompts like 'blob', 'goo', 'gooey', 'metaball', 'melt together', 'merge smoothly', 'liquid', 'slime', 'lava lamp', 'organic blend', 'shape blend'."
---

# Shape blends (metaballs / SDF blending)

A Shape Blend melts 2+ meshes into ONE smooth, continuous surface — THE tool
for organic soft forms: goo, blobs, merging liquid drops, lava lamps, slime,
snowmen, cumulus clouds, soft cartoon bodies, abstract fluid hero shapes.
Where a Boolean gives hard, exact CSG edges, a blend SMOOTHS the transition
between shapes over a blend range, like wet clay pressed together. It is
LIVE: the member meshes become CHILDREN of the Shape Blend container and stay
fully editable — move/scale/animate a member and the surface re-melts around
it. Only the blended surface renders; members stop rendering individually.

## Create — ALWAYS two run_code calls

Create the member meshes first, then combine them in the NEXT call (the
same two-call rule as booleans — members created in the same call are not
built yet, and the alias errors with "cannot build a shape blend with ..."):

```
mesh('Sphere', { width: 220 });
rename('Body');
position({ y: 110 });
mesh('Sphere', { width: 150 });
rename('Head');
translate({ y: 150 });
```
…then:
```
shapeBlend(['Body', 'Head']);
color('#8bd6a8');
rename('Blob');
```

- `shapeBlend(target?)` — combine the targeted (or currently selected)
  meshes into a new Shape Blend. Targets work like `boolean`'s: names, ids,
  objects from select/mesh, arrays mixing them, or `'all'`. Returns the
  blend (like `group`) and selects it, so transform/color calls right after
  target the container.
- Members join as smooth UNION with the container's global blend range —
  the right default for goo.
- Only meshes (and groups of meshes) join; lights and cameras are left
  where they are. A blend cannot nest inside another blend.

## The two dials that shape the goo

- `blendRange` (container, default 100, world units) — how far shapes melt
  toward each other. ~0 reads as a hard union; 40–80 is a subtle meniscus;
  150+ turns separate shapes into one amorphous mass. Shapes further apart
  than the blend range stay separate blobs — overlap or near-touch is what
  makes them merge.
- Distance between members — animate members closer/apart and they visibly
  merge/split like liquid. This is the whole trick behind lava lamps and
  drop-merge animations.

## Edit — shapeBlend(props) on the selection

A plain props object edits instead of creating. What it edits depends on
what is selected:

- Container selected (`geometry` type `ShapeBlendGeometry`):
  ```
  select(o => o.name === 'Blob');
  shapeBlend({ blendRange: 60, resolutionLevel: 7, useChildrenColors: true });
  ```
  - `blendRange` — the global melt radius (above).
  - `resolutionLevel` — 5–9 = a 32³…512³ surface field (see the budget
    below). Default 6.
  - `useChildrenColors` — false: the container's material paints the whole
    surface; true: each member's own color blends into a soft gradient
    across the goo.
- Member shape selected (a mesh inside the blend):
  ```
  select(o => o.name === 'Dent');
  shapeBlend({ operation: 'subtract' });
  ```
  - `operation` — 'union' | 'subtract' | 'intersect'. Subtract carves a
    soft dent/crater; intersect keeps only the overlap. Switching to
    subtract automatically tightens that shape to a LOCAL blend range of 25
    (a crisp-ish carve) unless you pass an explicit `blendRange` with it.
  - `blendRange` — a NUMBER turns on a per-shape override (this shape melts
    with its own radius); `'global'` turns the override off again.
  - `useColor` — for subtract/intersect members when the container uses
    children colors: whether this shape's color tints the surface.
- `get_objects([id])` returns a `shapeBlend` block on the container AND on
  each member in exactly this prop shape — read, tweak, pass back.

## Grow, shrink, dissolve

- ADD a member later: `moveInto('Blob', 'NewShape')` — moving a mesh into
  the blend (or a group inside it) auto-joins it as a union member.
- REMOVE a member: `moveInto('root', 'Head')` — moving it out strips the
  blend params and it becomes an ordinary mesh again.
- `hide(member)` drops a member's contribution without deleting it — cheap
  for A/B-ing a shape. `show` melts it back in.
- `ungroup` does NOT dissolve a Shape Blend (unlike Booleans/groups) — move
  the members out, then `remove` the empty container.
- Tree order matters for carving, like booleans: a subtract member carves
  the shapes BELOW it in the scene tree (members created earlier sit lower).
  Build the body first, the carvers after.

## Which shapes blend best (and the WebGL caveat)

- `Sphere` (incl. squashed/ellipsoid sizes), `Cube` (cornerRadius honored),
  `Cylinder` (incl. radiusTop/radiusBottom taper), and `Torus` (incl.
  partial `arc`) blend ANALYTICALLY — exact and cheapest. PREFER these
  four; they cover almost every organic build. A cone shape should be a
  TAPERED CYLINDER (`radiusTop: 0`), not the `Cone` primitive — `Cone` is
  not one of the analytic four and falls into the mesh-SDF path below.
- Any OTHER mesh (Lathe, Text, TorusKnot, customMesh, imported models…)
  joins as a baked mesh SDF — WebGPU only. On the WebGL fallback renderer
  those members are SKIPPED (the surface renders without them), so a blend
  built only from the four analytic primitives is the safe, portable
  choice.
- Up to 96 shapes per blend. Size members with GEOMETRY params
  (width/height/depth), not non-uniform `scale` — a member's scale is taken
  as uniform (only a uniform factor carries into the blend).

## Resolution & the scene-wide budget

The surface is polygonized from a voxel field; `resolutionLevel` sets its
density: 5 = 32³ (chunky), 6 = 64³ (default), 7 = 128³, 8 = 256³, 9 = 512³.
Levels cost a SHARED scene budget of 16 points: level 5 = 1, 6 = 2, 7 = 4,
8 or 9 = 16. So ONE very-high/ultra blend takes the whole budget, and a
scene fits at most 8 default-level blends. Exceeding it errors — lower an
existing blend's `resolutionLevel` or remove one. Stay at the default
unless the blob is a hero close-up with visible faceting; the field
re-evaluates live, so high levels cost GPU on every member edit and every
animation frame. One blend with 10 members is MUCH cheaper than 10 blends.

## Materials & color

- The blended surface takes the CONTAINER's material: select the blend,
  then `color`/`shading`/`layer` as usual. Glossy physical shading
  (`shading({ category: 'physical', roughness: 0.25 })`) sells the liquid
  look; add a `fresnel` layer for a wet rim.
- For multi-color goo, color the MEMBERS and turn on
  `shapeBlend({ useChildrenColors: true })` on the container — colors
  gradient into each other where shapes melt (classic lava-lamp two-tone).

## Animate the goo

Members are normal meshes — move them and the surface morphs. Motion is
code-driven (# Motion & interactivity; `animation` skill): name the drops,
then drive each member's y from the motion document with its OWN frequency
and phase so the rise/fall reads organic, never mechanical:

```js
// in the motion document's tick — per drop i, out of sync:
const y = drops[i].p.y + Math.sin(t * (0.35 + i * 0.11) + i * 2.2) * 110;
spline.updateObject(drops[i].id, { position: { y } });
```

Driving the CONTAINER moves the whole blob as one rigid object (fine for
floating/bobbing); driving MEMBERS is what makes it melt and split.

## Recipes

```
// Lava lamp — two-tone goo rising and falling inside a glass cylinder.
// Call 1: the drops (varied sizes, stacked) + the glass shell.
// Call 2: shapeBlend([...drop names]) → blendRange ~120,
//         useChildrenColors: true; then the motion document drives each
//         drop's y out of sync (see above).

// Snowman — three stacked spheres, subtle meniscus so it reads hand-packed:
// Call 1: three spheres, widths 260/190/130, stacked with slight overlap.
// Call 2: shapeBlend(['Base', 'Middle', 'Head']); shapeBlend({ blendRange: 35 });

// Soft crater / bite — carve a dent that stays smooth:
// Call 1: the body sphere + a smaller 'Dent' sphere poking into it.
// Call 2: shapeBlend(['Body', 'Dent']); then
//         select(o => o.name === 'Dent'); shapeBlend({ operation: 'subtract' });
```

## Gotchas

- Two run_code calls, always: members must exist BEFORE the call that
  combines them — "cannot build a shape blend with ..." means split the
  calls, not retry.
- `mesh('ShapeBlend')` / `add('Mesh', 'ShapeBlendGeometry')` do NOT work —
  a blend is never created empty; build it FROM its members with
  `shapeBlend([...])`.
- Hard-edged mechanical results (windows, drilled holes, machined parts)
  are BOOLEAN territory — load the boolean-operations skill instead. A
  blend always rounds and melts.
- The members' own materials stop rendering (only colors matter, and only
  with `useChildrenColors`); texture/glass layers belong on the CONTAINER.
- If the blob looks faceted in a close-up screenshot, raise
  `resolutionLevel` ONE step and re-check — don't jump straight to 8/9 (it
  spends the whole scene budget).
