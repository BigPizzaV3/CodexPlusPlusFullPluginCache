---
name: spline-3d-procedural-generation
description: "Procedural terrain/ocean/tree/rock/globe/building generators, seeded surface scatter, the constraint-based layout() solver, and the miniworld/diorama, city-street, enclosed-terrain (canyon/cave) and creature-rig recipes. Load for prompts like \"forest\", \"island\", \"landscape\", \"ocean\", \"canyon\", \"cave\", \"city\", \"miniworld\", \"mini world\", \"diorama\", \"arrange the furniture\", \"place these neatly\", or any scene needing many natural assets or exact relative placement."
---

# Procedural generation & constraint layout

Purpose-built generators beat hand-rolled customMesh loops: they are
deterministic (same `seed` => same mesh), tuned to look good, and cheap to
vary. The `layout()` solver replaces coordinate guessing with declarative
constraints. Everything here composes with the rest of the DSL (color,
shading, physics, code-driven motion...). And surface MARKS are not meshes at all:
a sticker/splash/impact/logo ON an existing surface is a `Decal` (see the
SURFACE DETAIL rule in your core guidance), never a customMesh outline.

PROCEDURAL AS RUNTIME BEHAVIOR: everything in this skill AUTHORS a static,
editable result into the tree — one baked output of a generator. When the
user explicitly asks for procedural/generative CONTENT ("procedural X",
"generated at runtime", "different every time"), they want the generator
itself: build it in the HTML layer with `spline.createObject` /
`spline.cloneObject` (load the `html-content` skill — raw vertex meshes
included, via `createObject('CustomMesh', {vertices, indices?})`, and
custom TSL shader materials via `spline.createCustomMaterial` when the
generated surfaces need looks the layer system can't express), and
use THIS skill to author what that script needs: template objects to clone,
and any surface built with the tuned generators below — their
terrain/ocean/tree algorithms are DSL-only, so at runtime you either
hand-roll the vertex math or clone their authored output.

They are also TURN SAVERS — treat them that way. Build in a few big
run_code blocks, not many small ones. If one object looks wrong, edit or
replace THAT object; never delete and rebuild the whole scene.

## Generators

- `terrain({ width?, depth?, maxHeight?, resolution?, seed?, noiseScale?,
  octaves?, falloff?: 'none'|'island', plateau?: 0..1, color?, name?,
  position?: [x,y,z] })` — rolling low-poly heightfield, base plane at y=0 of
  its position. `falloff: 'island'` fades height to zero at the rim (islands,
  dioramas). Default ~2000 units wide. Name it if you'll scatter onto it.
  `noiseScale` 1.5-3 = rolling hills (the default already is); higher packs
  more, smaller features. DETAIL BUDGET: frequencies the grid can't
  represent are clamped, and the grid comes from `resolution` — at the
  default 96, cranking noiseScale/octaves stops adding detail almost
  immediately. MOUNTAINS are not default hills: raise `resolution` FIRST
  (200-240), then `noiseScale` 3.5-6, `octaves` 5-6, `maxHeight`
  0.25-0.4 × width (the 0.14 default is a hill), `plateau` 0. A RANGE is
  2-3 overlapping `falloff: 'island'` tiles at different seeds, widths,
  and heights (taller behind) — one smooth low-res tile standing in for
  "mountains" is the diorama-dough failure. Dress steep slopes with
  scattered high-`angularity` rock(); above a tree line go snow
  `'#e8ecf0'` or bare rock `'#8d8578'`, never green to the summits.
  BIOME COLOR: the default is grass green — ALWAYS pass `color` for any
  other biome (desert sand `'#d9c08b'`, snow `'#e8ecf0'`, bare rock
  `'#8d8578'`, martian `'#b06b45'`). A green-tinted desert is a failed
  desert; double-check the screenshot for leftover green. And in the
  believable register even GRASS gets an explicit olive `'#5d7a4d'`-family
  color — the bright default green reads as felt.
- `ocean({ width?, depth?, waveHeight?, wavelength?, direction?,
  choppiness?: 0..1, resolution?, seed?, color?, name?, position? })` —
  open-water surface built from directional Gerstner swells (sharp crests,
  wide troughs, horizontal chop), smooth-shaded. MANDATORY for every
  ocean/sea/lake/water-body ask: NEVER fake water with a flat plane + a
  displace layer or noise bumps (always reads as a flat sheet), and NEVER
  hang the water's look on an AI texture. A flat-looking ocean is a
  failed ocean.
  SCALE: open sea wants `width` 6000-9000; `waveHeight` defaults to
  width * 0.012 — pass up to width * 0.02 for heavy seas, down to
  width * 0.004 only for calm harbor/lake water. Total relief comes out
  ~2.5x waveHeight. `direction` aligns swells with the scene's wind.
  MATERIAL: keep the generated deep teal or darken it, `lighting` low
  (30-50) so the surface stays glossy-dark, add a subtle `noise` layer
  (scale ~4-6% of width) as specular mottle so light breaks up across
  the surface, a slightly lighter `background` +
  `fog({ useBackgroundColor: true })` so the horizon melts. For a
  "simulation"/moving-water ask, drive a `displace` layer's `movement`
  slowly per frame from the motion document (`animation` skill) ON TOP of
  the geometry — motion comes from code, the swell SHAPE comes from
  ocean(); animated displacement alone is not an ocean.
  FINAL CAPTURE for water: set the camera 18-35° ABOVE the surface looking
  across the swells — a sea-level grazing angle plus fresnel washes the
  whole frame to white/sky. The finished shot should be mostly WATER with
  visible swell shapes, not mostly sky. SELF-CHECK the screenshot: if the
  horizon is a straight line and the surface reads flat, the waves are too
  small for this camera distance — double `waveHeight` (or move the camera
  closer/lower) and re-screenshot before finishing.
- `tree({ kind?: 'oak'|'pine'|'palm'|'birch'|'bush', height?, seed?,
  leafiness?, style?: 'realistic'|'stylized', trunkColor?, leafColor?,
  name?, position? })` — tree with trunk + canopy grouped, base at y=0.
  Default height ~260. `style` DEFAULTS TO 'realistic' (lobed,
  noise-displaced canopies clustered on visible limbs); pass
  `style: 'stylized'` (smooth blob canopies) ONLY when the prompt asks
  for cute/cartoon/toy scenes. In the believable register ALWAYS pass
  explicit muted colors — the bright defaults lean stylized:
  `leafColor` olive/forest ('#5d7a4d' broadleaf, '#3f5a44' conifer,
  jittered per tree), `trunkColor` gray-brown ('#6b5744') — a mint or
  lime canopy is a toy cue. tree() is a BAKED whole — right for scenery;
  a tree that must GROW or move branch by branch is decomposed into
  named per-branch parts instead — the `animation` skill's
  structure-generation rules.
- `rock({ size?, seed?, detail?: 0|1|2, angularity?: 0..1,
  flattenBottom?: 0..1 (a NUMBER, not a boolean — 0.35 sits naturally),
  color?, name?, position? })` — faceted boulder, base at y=0. Default
  size ~120.
- `globe({ radius?, style?: 'dots'|'relief', cellStep?, dotSize?,
  oceanColor?, landColor?, name?, position? })` — an EARTH globe with
  REAL continent geometry (built-in geographic mask — the viewer will
  recognize the Americas, Africa, Eurasia, Australia). Use it for ANY
  "globe" / "earth" / "world with cities" ask; NEVER build Earth from
  noise blobs and never gamble on an AI texture for it. `style: 'dots'`
  is the dotted data-viz look; `'relief'` is raised low-poly land. CITY
  MARKERS: give the globe an explicit `position` (e.g. [0, 0, 0]); the
  returned handle has `project(lat, long)` → [x,y,z] relative to the
  globe's center — place a small emissive sphere at
  `[gx + p[0], gy + p[1], gz + p[2]]` for each city's REAL coordinates
  (New York 40.7,-74 · London 51.5,-0.1 · Tokyo 35.7,139.7 · Paris
  48.9,2.4 · Sydney -33.9,151.2 · São Paulo -23.6,-46.6 · Cairo 30,31.2 ·
  Mumbai 19.1,72.9 ...) — they will sit exactly on the right continents.
  A slow code-driven yaw sells it — `rotation.y = (t * 8) % 360` on the
  globe group in the motion document (`animation` skill).
- `scatter({ on, source, count?, seed?, align?: 'normal'|'up',
  spread?: 'random'|'even' (a distribution MODE, not an amount),
  scaleJitter?: 0..1, rotationJitter?: degrees, hideBase?: boolean })` —
  distributes `source` over
  the surface of `on` with a seeded surface cloner + natural yaw/scale
  jitter. `on`/`source` accept names or the handles returned by the
  generators, and resolve when the block runs — so create + scatter works in
  ONE run_code call. `hideBase` defaults true (the source becomes the
  scatter template). Instances stay UPRIGHT by default (trees, props,
  buildings keep the template's orientation, jittered only in yaw); pass
  `align: 'normal'` to make instances hug the surface tilt instead —
  right for rocks and pebbles, wrong for trees on steep ground.

Seeds: vary `seed` per asset for variety (three pines with seeds 1/2/3 look
like siblings, not clones). Rerunning with the same seed reproduces the mesh
exactly — useful for "same tree but taller".

GROUNDING hero objects on terrain: the handle terrain() returns carries
`heightAt(x, z)` — the surface height in the terrain's LOCAL frame (its
base plane is y=0 at wherever you positioned it). Give the terrain an
explicit `position` (e.g. [0, 0, 0]) when you'll stand things on it, then
place each object at `y = terrainY + heightAt(objX - terrainX, objZ -
terrainZ)` (plus half the object's height if its origin is centered).
Feet, paws, wheels and foundations must TOUCH the surface — a character
half-sunk into the ground fails review. scatter() already does this
automatically for its instances.

### Forest island in one block

```
const ground = terrain({ width: 2600, maxHeight: 320, seed: 7,
  falloff: 'island', color: '#6f9e58', name: 'Island' });
const pine = tree({ kind: 'pine', height: 300, seed: 3, name: 'Pine' });
scatter({ on: ground, source: pine, count: 70, seed: 5 });
const boulder = rock({ size: 150, seed: 11, name: 'Boulder' });
scatter({ on: ground, source: boulder, count: 14, seed: 9,
  scaleJitter: 0.5 });
```

Then set atmosphere (fog, background, lighting) per the organic-scenes skill,
and frame with lookFrom/orbit. For hero foreground trees, place 2-3
individually with `position` and distinct seeds instead of scattering them.
Keep dark moods (night, storm) READABLE: strong key + rim on the subject,
background a step lighter than the darkest surfaces, fog subtle — never let
the scene collapse to near-black.

## Cities & streets — density is the point

- `building({ width?, depth?, height?, style?: 'modern'|'futuristic'|
  'blocky', seed?, litRatio?: 0..1, bodyColor?, windowColor?, litColor?,
  name?, position? })` — a tower with seeded setback massing, roof
  mechanicals/antenna and REAL per-window geometry (a dark-pane grid +
  a seeded LIT subset — instant night-city window variety). Towers are
  ALWAYS `building()` — never plain extruded boxes, and never glass
  boxes waiting on an AI window texture: the texture service fails
  often, and building()'s window grids + lit subset are GEOMETRY that
  need no texture at all. One `building()` per tower, varied
  `seed`/`height`/`style`/footprint, is the same effort and looks 10x
  denser. Vary `bodyColor` VALUE between neighbors (readability rule).
- STREETS make the city read as a city, not a bar chart. Between the
  block rows lay dark asphalt strips (`mesh('Plane')` or thin boxes,
  `#2a2d33`) at road width from the # Real-world scale table (a lane is
  150-165; a two-lane street ≈ 300), then loop: center dashes (thin
  white boxes ~5 × 120 with ~180 gaps), streetlight pairs (thin cylinder
  + small emissive sphere, 250-400 tall) along the curbs, a few simple
  two-box cars (~225 long, one per lane) with varied yaw and color, and
  sidewalk trees (`tree({ height: 350-550 })` — street trees are
  TALLER than streetlights; 120-tall blobs read as shrubs and
  miniaturize the whole city) or planters. A crosswalk (4-6 white
  strips) at intersections is 6 objects and sells the whole street.
- LAYOUT: tower grid step = footprint + a REAL street corridor, not a
  gap: e.g. 340 footprint + two-lane road 300 + sidewalks 2 × 80 ≈
  800-900 between tower centers, jittered; tallest cluster in the
  middle, lower blocks at the rim. (A tight ~420 step with slot-canyon
  gaps is a stylized diorama cue — fine when that's asked for.) Fog + a
  slightly lighter sky ground the far edge (READABILITY still applies
  at night). For ground-level streetscapes (residential streets, towns,
  storefronts) load the `architecture` skill — its streets &
  neighborhoods recipe covers lots/setbacks, utility poles with sagging
  wires, and street furniture at true scale.

## Miniworlds & dioramas — the containment contract

A "miniworld" / "mini world" / "diorama" is NOT a landscape on infinite
ground. It is a CONTAINED model on a floating base block with clear
square/rectangular bounds — like a slice of world cut out with a knife:

1. BASE SLAB first: a rectangular block with visible THICKNESS —
   `mesh('Cube', { width: 1600, height: 140, depth: 1600, cornerRadius: 12 })`
   in an earth/rock tone. The slab's side faces ARE part of the look
   (layered cross-section: darker earth below, sand/grass rim at the top
   edge). Stack a second, thinner, slightly smaller slab for the top
   layer color when the biome needs it.
2. EVERYTHING STAYS INSIDE the slab footprint. Nothing overhangs the
   edge; trees/props near the rim sit fully on the slab. Scatter with a
   `spread` small enough to keep instances off the edge.
3. WATER is an INSET BLOCK, not a plane: a translucent box
   (`opacity` ~0.55-0.7, glass or fresnel layer) sunk into the slab so
   its cut face shows blue on the slab's side — with a thin `ocean()`
   patch (small `waveHeight`, `width`/`depth` = the water area) laid on
   top for the wavy surface. Shorelines are carved by the sand layer's
   outline, not by falloff fading.
4. GROUND detail: a thin `terrain()` (low `maxHeight`, `width`/`depth`
   = slab size, no falloff) sitting ON the slab top gives dunes/hills
   that still END at the square edge.
5. BACKDROP: plain soft studio color (`background()`), NO fog-to-horizon
   — the miniworld floats like a product shot. Soft key + gentle AO;
   subtle contact shadow reads well.
6. CAMERA: elevated 3/4 view (elevation ~30-40 degrees) with the WHOLE
   slab in frame plus margin — the silhouette of the block is the
   composition.
7. SCALE: mini — dense small props, mini people/creatures; charm comes
   from density inside the bounds, not from world size.

The same contract applies to any "mini X" (kitchen, city block, farm):
base slab, contained content, studio backdrop, whole-slab framing.

## Enclosed terrain (canyon, cave, valley) + first-person scenes

The two classic failures here are a camera buried inside a wall and a
near-black interior. Both are avoided by BUILD ORDER:

1. SHELL FIRST, one block: floor + walls + lights + rim overview camera.
   Canyon floor: `terrain({ width: 6000, depth: 1800, maxHeight: ~120 })`
   in bare-rock/martian tones. Walls: two rows of LARGE rocks
   (`rock({ size: 400-700 })`, y-scale 2-3x, varied seeds) along BOTH
   long edges — overlapping rocks read as stratified cliffs and always
   leave an open corridor between them.
2. LIGHT THE INTERIOR in the same block: default ambient does not reach
   inside — add a warm key angled down the corridor plus 1-2 fill lights
   INSIDE it, and keep the sky visible past the corridor ends so depth
   reads. If a screenshot comes back near-black, raise the lights ONCE
   (READABILITY rule) and move on.
3. The overview camera looks down the corridor axis from ABOVE THE RIM
   (elevation 25-35 degrees), whole corridor in frame — that is the
   resting viewport AND the final capture. Never leave the viewport at
   eye level inside the canyon.
4. PROPS next (alien trees, gems, pools — scattered on the floor with
   heightAt grounding), then the FIRST-PERSON RIG LAST: eye-height
   (~170) play camera + controls in one block. If the run gets cut
   short, the scene survives; only the rig is lost.
5. HUD/score plumbing (counters, money labels): ONE turn maximum. If
   variable binding isn't available, a static Text label is fine — say
   so and move on.

## Simple creature rigs (fish, birds, walkers)

One creature = ONE pivot. `add('Empty', { name: 'Fish1' })`, build the
body parts, select them and `group()` under that pivot, then DRIVE the
GROUP from the motion document (`animation` skill — "Orbits, spins &
travel"): a travel path plus a small yaw sway computed from time, with
per-creature phase offsets so the school feels alive. NEVER chain
nested Empties as pivots for a simple swim/fly — one level is enough;
nested-pivot rigs are how a run loses ten minutes to "delete and rebuild
the rig". If parenting comes out wrong, fix it with ONE group/reparent
call — never rebuild the creature from scratch.

## layout() — constraint-based placement

`layout({ constraints: [...], objects?, fixed?, region?, seed?,
iterations?, noOverlap? })` moves EXISTING objects so the constraints hold
(simulated annealing — overlap avoidance is always on unless
`noOverlap: false`). References are names/ids/handles. Positions update
after the block dispatches; call get_scene only when a later step needs the
exact numbers — a confirmation pass after every layout() is a wasted turn.

Constraint vocabulary:
- `{ type: 'near', a, b, min?, max? }` — footprint gap between a and b within
  [min, max] (units; default 0..60).
- `{ type: 'apart', items: [...], min }` — every pair at least `min` apart.
- `{ type: 'on', a, b }` — a rests on top of b (stacks y, keeps a inside b's
  footprint). Lamp on desk, cup on table.
- `{ type: 'against', a, b, margin? }` — a touches b's nearest side face
  (sofa against wall).
- `{ type: 'facing', a, b }` — rotates a so its front (+Z) aims at b.
- `{ type: 'align', items, axis: 'x'|'z' }` — shared coordinate (chairs in a
  line).
- `{ type: 'inside', items? }` / `{ type: 'spread', items }` — keep in the
  region / distribute evenly.
- `fixed: [...]` — anchors the solver must not move (walls, the table).

### Dining set

```
layout({
  constraints: [
    { type: 'near', a: 'Chair', b: 'Table', max: 40 },
    { type: 'near', a: 'Chair 2', b: 'Table', max: 40 },
    { type: 'near', a: 'Chair 3', b: 'Table', max: 40 },
    { type: 'near', a: 'Chair 4', b: 'Table', max: 40 },
    { type: 'facing', a: 'Chair', b: 'Table' },
    { type: 'facing', a: 'Chair 2', b: 'Table' },
    { type: 'facing', a: 'Chair 3', b: 'Table' },
    { type: 'facing', a: 'Chair 4', b: 'Table' },
    { type: 'apart', items: ['Chair', 'Chair 2', 'Chair 3', 'Chair 4'],
      min: 20 },
    { type: 'on', a: 'Vase', b: 'Table' },
  ],
  fixed: ['Table'],
  seed: 2,
});
```

Guidance:
- PRECISION-FIRST WORKFLOW: create objects with rough positions (or defaults),
  then `layout()` them — never hand-compute touching/facing coordinates.
- Prefer a SEPARATE run_code call for layout after creating objects: sizes of
  objects created in the same block are estimated from geometry params, while
  a second call measures true bounds. Same-block layout still works when the
  stand-ins are simple boxes.
- layout() solves in the objects' own coordinate frame — use it on TOP-LEVEL
  objects (or siblings in one group), not across different groups.
- If a constraint can't be satisfied (e.g. six sofas against one tiny wall),
  the solver gets as close as it can; widen the region or relax min/max
  rather than piling on weight.
- Unresolvable names are skipped silently — double-check names with get_scene
  if the result looks off.
- TURN BUDGET: even a dense interior needs only a handful of rounds — shell +
  furniture in 1-2 blocks, one `layout()` pass, decor, lighting, then ONE
  camera framing (lookFrom/orbit) with at most one adjustment after a
  screenshot. If time remains, spend it on materials and lighting — not on
  re-checking, reframing loops, or rebuilding. Atmosphere (fog, haze,
  background) is ONE pass after geometry and framing — if it reads wrong,
  fix it in ONE adjustment; never spend multiple turns chasing haze.

Cross-references: organic-scenes (atmosphere, water, palettes for nature),
building-scenes (units, camera framing, dressing loops).