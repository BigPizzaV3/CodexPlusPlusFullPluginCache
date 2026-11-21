---
name: spline-3d-lathe
description: "The Lathe primitive: revolving a 4-point bezier profile around Y into vases, bottles, bowls, cups, glasses, lamp bases, chess pieces, columns, domes. The points contract (x = radius, y-down, top-first), sizing behavior, segments, open rims & double-siding, profile recipes, and multi-lathe / customMesh fallbacks for complex silhouettes. Load for prompts like \"vase\", \"bottle\", \"bowl\", \"cup\", \"pot\", \"goblet\", \"lathe\"."
---

# Lathe (profiles of revolution)

A Lathe revolves a 2D profile curve 360° around its vertical (Y) axis — THE
primitive for anything a potter or wood-turner could make: vases, bottles,
bowls, plates, cups, glasses, jars, lamp bases, chess pieces, balusters,
domes, bells. Prefer it over stacking spheres/cylinders whenever the object
is rotationally symmetric with a curved silhouette.

## Create & edit

```
mesh('Lathe', { points: [[28, -90], [8, -60], [85, 30], [30, 90]] });
color('#c96f4a');
position({ y: 90 }); // lift by half the height to sit on a floor
rename('Vase');
```
- `mesh('Lathe', { points?, width?, height?, radius?, segments?,
  verticalSegments? })` — create. With no params you get the default
  100-unit egg/barrel profile.
- `geometry({ ... })` — edit the SELECTED lathe: pass new `points`, or just
  `width`/`height`/`radius` to rescale the current profile.
- `get_objects([id])` returns a `lathe` block ({ points, segments,
  verticalSegments }) in exactly this prop shape — read, tweak, pass back. In
  the same code block, `select(...)[0].geometry.points` reads it too.

## The points contract (get this right)

`points` is EXACTLY 4 `[x, y]` control points of ONE cubic bezier —
`[start, handle, handle, end]` — NOT a polyline through 4 positions:

- `x` is the distance from the central axis (the radius). It MUST be >= 0;
  a negative x is an error.
- `y` runs DOWNWARD (screen-style, like the editor's 2D curve widget): the
  most NEGATIVE y is the TOP of the object, the most positive y the bottom.
- Write the curve from the TOP down (`points[0]` = top, `points[3]` =
  bottom). A bottom-first profile is the same curve, so the DSL flips it for
  you — but write top-first so handles read sanely.
- Units are world units. The DSL recenters the profile vertically (the
  object's origin becomes the middle of the shape, like every primitive) and
  keeps `width`/`height`/`depth` synced to the profile's extents, so
  `get_scene` sizes and the selection box stay true.
- The middle two points are bezier HANDLES — the curve does not pass through
  them, it is pulled toward them (a bulge reaches roughly 3/4 of the handle's
  offset: the default profile's handles sit at x 50 but the real belly radius
  is 37.5). Sizes are derived from the control hull (handles included),
  matching the editor's own convention — keep handles inside the silhouette
  you intend.

Endpoints decide open vs closed:
- an endpoint AT the axis (`x: 0`) closes that end to a smooth tip/base;
- an endpoint OFF the axis (`x > 0`) leaves an OPEN circular rim — the
  surface has zero thickness and no cap. Fine for a floor-hidden base;
  visible openings (cup/bowl interiors) need `shading({ side: 'double' })`
  or the inside faces vanish.

## Sizing & smoothness

- `width` (or `radius` = width/2) scales the profile radially; `height`
  scales it vertically; `depth` is always identical to `width` (it's a
  revolution). `geometry({ width: 240, height: 400 })` rescales the existing
  curve — no need to recompute points.
- `segments` — sides around the axis (default 64). 8–12 + `shading({
  flatShading: true })` = a faceted, wood-turned low-poly look.
- `verticalSegments` — subdivisions along the curve (default 64; lower it
  for low-poly, raise past 64 only for very tall glossy heroes).
- ANIMATION caveat: geometry size writes do NOT re-render a lathe (the
  profile drives the surface) — that goes for the bridge's
  `updateObject({ geometry })` and state/`animate({ geometry: ... })`
  tweens alike. Animate a lathe with `scale` instead.

## Profile recipes (top-first, y-down)

```
// Vase — narrow neck, fat belly, planted base (open bottom hidden by floor)
mesh('Lathe', { points: [[28, -90], [8, -60], [85, 30], [30, 90]] });

// Bowl — wide open rim, rounded closed bottom; double-side the interior
mesh('Lathe', { points: [[90, -40], [88, 10], [55, 42], [0, 40]] });
shading({ side: 'double' });

// Bottle — slim straight neck flaring into a straight-walled body
mesh('Lathe', { points: [[9, -110], [9, -20], [55, -25], [42, 110]] });

// Chess pawn — round head, pinched stem, flared base
mesh('Lathe', { points: [[0, -70], [45, -70], [0, 20], [40, 70]] });
```
Iterate like a designer: build, `set_view` + `take_screenshot`, then nudge
handles (belly out, neck in) with `geometry({ points })` — small handle moves
change the silhouette a lot.

## One bezier is the limit — composing past it

A single cubic can't do a wine glass (bowl + stem + foot) or an ornate
column. Three escape hatches, in order of preference:

1. STACK LATHES: build each section as its own lathe, align them on the same
   axis (`position`/`translate` y only), then `group()` — e.g. glass bowl
   lathe + thin `Cylinder` stem + squat foot lathe.
2. WALL THICKNESS: a lathe surface is infinitely thin. For a visible-walled
   vessel, boolean-`subtract` a slightly smaller inner lathe from the outer
   one (load the `boolean-operations` skill first), or accept
   `side: 'double'`.
3. CUSTOM REVOLUTION (`customMesh`): any polyline profile, computed in a
   loop — rings of vertices around Y, band-triangulated. Use when the
   silhouette needs more than one curve segment:
```
// profile as [radius, y] pairs, TOP first (y-up here — you own the math)
const profile = [[0, 160], [30, 150], [12, 120], [12, 40], [55, 20], [60, 0]];
const seg = 24;
const verts = [];
const idx = [];
for (let i = 0; i < profile.length; i++) {
  for (let s = 0; s < seg; s++) {
    const a = (s / seg) * Math.PI * 2;
    verts.push(Math.cos(a) * profile[i][0], profile[i][1], Math.sin(a) * profile[i][0]);
  }
}
for (let i = 0; i < profile.length - 1; i++) {
  for (let s = 0; s < seg; s++) {
    const sn = (s + 1) % seg;
    const top = i * seg;
    const next = (i + 1) * seg;
    idx.push(top + s, top + sn, next + s);
    idx.push(top + sn, next + sn, next + s);
  }
}
customMesh({ vertices: verts, indices: idx });
```
(Open boundaries render double-sided automatically; see the organic-scenes
skill for more `customMesh` patterns.)

## Gotchas

- Exactly 4 points, x >= 0, y-down, top-first — the errors tell you which
  point is wrong; fix that point, don't regenerate everything.
- A lathe spawns centered at the build center like every mesh: lift it by
  half its height to sit on a floor.
- Materials apply to the whole surface — a two-tone vessel (glaze + clay) is
  two stacked lathes or a gradient/fresnel layer, not two materials.
- Don't use a lathe for straight-sided prisms — `Cylinder`/`Cone` with
  taper/corner params are cheaper and rounder-handled there.
