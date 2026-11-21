---
name: spline-3d-architecture
description: "Buildings & man-made structures in the believable register: real-world proportions, crisp edges (cornerRadius 0), pitched roofs with overhangs, framed windows/doors, wall/roof textures, muted palettes, streets & neighborhoods at real scale. Load for prompts like \"house\", \"building\", \"cabin\", \"tower\", \"city\", \"skyline\", \"street\", \"town\", \"village\", \"neighborhood\", or any named real-world place."
---

# Architecture (buildings & structures)

Buildings are where the toy-house failure lives: a rounded cube + an oversized
pyramid + candy colors reads as a plush toy. A BELIEVABLE building (the
default register when the user named no style — see # Style register) is made
of the same primitives plus real proportions, crisp edges, overhangs, frames,
and real material finishes. All of it is cheap with the recipes below. (For a
deliberately cute/toy house, invert these rules — rounding, saturation, and
chunky proportions become correct.)

## Proportions (copy reality's ratios)

Pick a storey unit S ≈ 150 world units and derive everything from it:

- WALLS: one storey ≈ S tall; a 2-storey house ≈ 2S. Footprint beats height —
  a family house is wider and deeper than it is tall (≈ 3S × 2S × 4S w×h×d).
  Towers invert that.
- ROOF: pitch 25–40° — the rise is ≈ 0.3× the span it covers, not a giant
  witch hat. It must OVERHANG the walls by 5–10% per side (eaves). A roof cut
  flush with the walls is the #1 toy-house tell.
- DOOR: person-scale and small next to the facade — ≈ 0.7×S tall, 0.3×S wide.
- WINDOWS: vertical rectangles ≈ 0.5×S tall, sills ≈ 0.3×S above each floor
  line, repeated in aligned columns/rows. Repetition reads real; one giant
  window reads dollhouse.
- CHIMNEY: slim (≈ 0.3×S square) and rising past the ridge.

## Crisp edges (kill the plush look)

`Cube`/`Cylinder`/`Cone` SPAWN softly rounded (cornerRadius 8 by default) —
that alone reads toy. Pass `cornerRadius: 0` (or 1–2 for a worn edge) on
every structural box, and keep flatShading off in this register.

## Walls, roof, chimney (the structure)

Build the parts UNROTATED at the build center and group at the end (the
compound-object rule — group + name in a later call).

```
// call 1 — structure (S = 150; a 460 × 300 × 640 two-storey house)
mesh('Cube', { width: 460, height: 300, depth: 640, cornerRadius: 0 });
position({ y: 150 });
rename('Walls');
// gabled roof: an extruded Triangle prism, wider AND deeper than the walls
// (eave + rake overhang), rise 160 over a 260 half-span ≈ 32° pitch. An
// extruded flat shape grows FORWARD (+z) from its origin plane — unlike a
// centered Cube — so pull it back by depth/2 to center it over the walls.
mesh('Triangle', { width: 520, height: 160, depth: 700 });
position({ y: 380 });
translate({ z: -350 });
rename('Roof');
// chimney: slim, offset from center, punching past the ridge
mesh('Cube', { width: 45, height: 200, depth: 45, cornerRadius: 0 });
position({ y: 400 });
translate({ x: 120, z: 140 });
rename('Chimney');
```

- HIP ROOF variant: `mesh('Pyramid', { width: 520, height: 150, depth: 700,
  radialSegments: 4, cornerRadius: 0 })` — a 4-sided Pyramid is ALREADY
  axis-aligned with the walls (same Y rotation, NO habitual +45° "fix"), and
  never a 4-sided Cone (its base sits diagonal).
- FLAT/MODERN roof: a thin slab (`height: 12`) overhanging 6–8%, plus a low
  parapet of four thin boxes.
- Verify alignment with the `size`/position that `run_code`/`get_scene`
  report — eaves should overhang evenly on both sides.

## Doors & windows (proud panels, framed)

Openings sit PROUD of the wall face by a few units — never coplanar
(z-fighting) — as dark glazing panels with thin frame slats. Real cut
openings are the advanced path: load `boolean-operations` first if the user
needs to see through. Proud panels read right from normal viewing distances
and stay cheap. Give every panel real `depth` (never a zero-depth
`Rectangle` AT the wall plane), and derive its offset from the wall's
half-depth, not by eye. If a run_code result reports a "Z-FIGHTING RISK"
between a panel and its wall, the panel is sitting flush — push it out along
the facade normal and fix it before building further.

```
// call 2 — door + a 2×3 window grid on the front face (wall face at +320
// from the build center, so panels at +322 sit proud, not coplanar)
mesh('Cube', { width: 46, height: 105, depth: 4, cornerRadius: 0 });
position({ y: 53 });
translate({ z: 322 });
color('#6d5138');
rename('Door');
for (let i = 0; i < 2; i++) {
  for (let j = 0; j < 3; j++) {
    if (i === 0 && j === 1) continue; // the door takes the middle ground bay
    mesh('Cube', { width: 55, height: 80, depth: 4, cornerRadius: 0 });
    position({ y: 90 + i * 150 });
    translate({ x: (j - 1) * 140, z: 322 });
    color('#20303d'); // dark glazing
    shading({ category: 'physical', roughness: 0.1, metalness: 0 });
    rename('Window');
  }
}
```

- FRAMES sell the windows: four thin slats (e.g. 4×88×6 verticals, 63×4×6
  horizontals) in a trim color hugging each opening — loop them like the
  windows. Skip them for far-away buildings; add them for hero shots.
- LIT-WINDOW option (dusk shots): `shading({ category: 'phong', emissive:
  '#ffd9a0' })` on a few panes, with a dimmer, cooler ambient.

## Materials (half the realism — mapping and restraint are the craft)

Flat lambert colors read as plastic, but a photographic texture slapped on at
defaults reads WORSE: the default `uv` projection STRETCHES on extruded
shapes (the Triangle-prism roof) and elongated boxes (the chimney), and one
un-tiled image makes stones the size of windows. Texture every big surface —
but always with the mapping set (full projection/tiling reference in
materials-and-look):

- PROJECTION: pass `projection: 'triplanar'` on EVERY architectural surface
  (walls, roof prisms, chimneys, slabs). It maps per world axis from the
  object's own space, so nothing smears along a slope or stretches on a tall
  box. Default `uv` is only safe on simple flat panels.
- TILE DENSITY: `texture: { repeat: [n, n] }` sets how often the image tiles
  — pick n so features read at REAL size against the object's dimensions
  (stone courses ~30–60 world units, bricks ~15–25, shingle rows ~25–40).
  Without it one giant image spans the whole wall.
- SUBTLETY: keep the layer's `alpha` at 0.6–0.8 over a `color()` base in the
  same family (the texture tints the base instead of shouting over it), ask
  for restraint IN THE PROMPT ('subtle', 'fine grain', 'low contrast', 'even
  tone'), and keep `bumpMapIntensity` at 1–2 — high bump plus a busy texture
  is the fastest way to make a wall look diseased. No texture on glazing.
- SOURCE: crisp REPEATING patterns — brick/stone courses, roof tiles and
  shingle rows, plank siding and decks, pavement, checker floors — draw
  best with `generateTexture` (local canvas drawing, instant, seamless by
  construction; recipes in materials-and-look) applied via `image:`. Keep
  `style` generation for photographic irregular surfaces (weathered stucco,
  rough stone, rust). Same mapping rules apply to both.

```
// call 3 — finishes (selects work: the parts were created in earlier calls)
select(o => o.name === 'Walls');
color('#e9e5dc');
layer('texture', { style: 'subtle white painted stucco, fine even grain, low contrast, seamless',
  projection: 'triplanar', alpha: 0.7, texture: { repeat: [3, 3] } });
shading({ category: 'physical', roughness: 0.9, metalness: 0,
          bumpMap: 'texture', bumpMapIntensity: 1.5 });
select(o => o.name === 'Roof');
color('#5c5f66');
layer('texture', { style: 'gray asphalt roof shingles, straight even rows, low contrast, seamless',
  projection: 'triplanar', alpha: 0.75, texture: { repeat: [4, 4] } });
shading({ category: 'physical', roughness: 0.85, metalness: 0,
          bumpMap: 'texture', bumpMapIntensity: 2 });
select(o => o.name === 'Chimney');
color('#9a5a44');
layer('texture', { style: 'red brick, small even courses, low contrast, seamless',
  projection: 'triplanar', alpha: 0.75, texture: { repeat: [2, 4] } });
```

- Wall prompts that work: 'weathered red brick wall', 'horizontal wood siding
  planks', 'raw board-marked concrete'; roofs: 'terracotta roof tiles', 'dark
  slate roof shingles' — always append ', low contrast, seamless'. Textures
  resolve ASYNC (checkerboard until then — re-screenshot on a later turn,
  don't retry); if the backend can't resolve them, fall back to muted flat
  colors + a subtle 'noise' layer.
- JUDGE the texture pass in your screenshot: if a pattern looks smeared along
  the roof slope or stretched down the chimney, the projection is wrong
  (triplanar fixes it); if features look monumental, raise `repeat`; if the
  surface shouts, lower `alpha` toward 0.6 or drop the texture for a flat
  finish; if a wall or roof looks GLASSY or see-through (it mirrors the sky/
  ground), you passed `roughnessMap` on a dark texture — remove it and keep a
  flat `roughness` (roughnessMap multiplies by luminance; dark = mirror). A
  wall texture should be visible at hero distance and nearly disappear at
  establishing distance.
- PALETTE: sample the real street — off-white/greige walls, gray-brown roof,
  wood-tone door, dark glazing. Muted and desaturated, 3–5 tones. Saturated
  primary red/green/blue surfaces are what scream toy.

## Ground & dressing

- Ground it: a path/driveway (flat `Rectangle`, `rotation({ x: -90 })`,
  `position({ y: 0.5 })` — proud of the ground, no z-fighting), low hedges
  (small boxes — hedges MAY keep a little cornerRadius, they're clipped
  plants), a tree or two (organic-scenes), a fence of thin slats.
- `environment({ ao: true })` + one soft directional key (intensity ≤ 1,
  `shadowRadius` 2–4): AO in the eaves and window reveals is what makes a
  facade read dimensional.
- Camera: a near-eye-level 3/4 (`lookFrom({ azimuth: -35, elevation: 8 })`)
  reads architectural; a high diorama angle reads toy.

## Streets & neighborhoods (places at real scale)

A street/town/village prompt is a PLACE — several buildings related by a
road — and it lives or dies on shared scale (# Real-world scale: 1 m ≈ 50
units). The classic toy tells are ratio errors, not object errors: a road
narrower than the houses are tall, shrub-sized "trees", knee-high fences,
one giant prop or person. Derive everything from the anchor table and the
same primitives read as a real place.

- ROAD FIRST — it sets the axis and the scale. A flat `Rectangle`
  (`rotation({ x: -90 })`, `position({ y: 0.5 })`), asphalt gray
  `'#55585e'` (weathered, never pure black), LENGTH in the thousands of
  units, width from the table: one lane 150–165, a two-lane residential
  street ≈ 275–325, a main road with parking 450+. Optional subtle
  `noise` layer or low-alpha texture; skip shouting markings — center
  dashes only where a real road of that class has them (thin white boxes
  ≈ 5 × 120, gap ≈ 180, `y: 1`); many residential lanes have only edge
  lines or nothing. A crosswalk at a junction is 5–7 white strips
  (≈ 40 × 120, gap 40) and instantly reads urban.
- CURBS + SIDEWALKS: raised strips along both edges (height ≈ 8, sidewalk
  width 75–125, light concrete `'#9b9992'`); everything built sits behind
  them, not on the asphalt.
- LOTS, NOT A LINEUP: each house (recipes above, S = 150) sits on its own
  lot — setback varied 60–250 from the sidewalk, behind a low wall/fence
  (60–90 tall, 8–12 thick, muted render/stone tones) or hedge (50–75);
  vary footprint, storey count (1–2), roof type, and hue WITHIN one muted
  family per street; keep facades parallel to the road; leave ≥ 60 between
  lots. Identical spacing/height is what reads as a train set.
- REGIONAL SIGNATURES: a NAMED style or region is a hard constraint —
  give every building that register's three signature elements, never a
  generic gable box with a label. Alpine chalet: deep eaves (15–20%
  overhang), dark timber beams/band over light stucco, balcony with
  slat railing, stone plinth. Japanese: low boundary wall, tiled
  hip/gable, deep entry canopy, window grids. Mediterranean: warm-white
  stucco, low-pitch terracotta, shuttered openings. SELF-CHECK the
  screenshot: if the houses would look the same with the region removed
  from the prompt, the register didn't land — add the signatures before
  finishing.
- DETAIL BY DISTANCE: build for the person standing IN the scene, not
  just the overview. The two or three buildings nearest the final
  camera get the FULL treatment from the recipes above — framed
  windows, a real door with a canopy/porch, eaves, wall texture; the
  mid-ground keeps true window grids and doors; only fog-distance
  buildings may simplify to massing. At eye height every facade within
  ~1500 units must show openings and trim — a blank wall next to the
  viewer is the "as soon as you get closer it falls apart" failure.
  AT ARM'S LENGTH (the buildings a visitor can walk right up to), flat
  fills read as unpainted card: run their wall/roof texture layers
  STRONGER than the distance defaults (alpha 0.8–0.9, bumpMapIntensity
  ~2, repeat tuned so grain is visible at 5 m), and give the hero door
  hardware — an inset panel and a small knob/handle box at ~55 units
  height. Glazing gets a fresnel or slight tint variation so panes
  aren't one flat navy fill. EVERY face a visitor can reach gets this
  treatment, not just the street facade: a side or rear wall along a
  path, yard, or gap carries the same texture layer, one or two
  openings (window, vent, side door) or structural relief (timber
  band, downpipe, pilaster), and the plinth carried around the
  corner. NO LARGE PLANE SHIPS BARE — a dressed front with a blank
  flank is the miss every close inspection lands on.
- VERTICALS SELL THE DEPTH: utility poles every 900–1200 along ONE side —
  `Cylinder` radius 6–8, height ≈ 500, weathered gray `'#8a8578'`,
  `cornerRadius: 0`, a short crossarm box near the top — with WIRE spans
  between consecutive poles: a wire is a thin box (width 1.5–2, height
  1.5–2, depth = the span) hung just below the crossarms; build each span
  as two half-spans meeting ~10–15 units lower at mid-span (tilt each
  ±1–2°) so the wire SAGS — straight taut wires read CG, sagging wires
  read photographed. Add lamp posts (250–400), a road sign (pole ≈ 110),
  and one or two anchor props at true size (vending machine ≈ 90 × 60 ×
  35, post box ≈ 60 tall, planters).
- TREES AT TREE SCALE: `tree({ height: 350–600 })` (realistic default
  style), varied seeds and heights, in verges and yards — a street tree
  stands TALLER than the fences and reads against the houses' ridge
  lines. A 100–150-tall canopy blob is a bush; placing bushes where trees
  belong is one of the strongest toy cues. MIX `kind`s (oak/birch along
  the street, a pine or two in yards) — a row of identical spherical
  canopies reads as decoration, varied species read as planting.
- PEOPLE / VEHICLES (only when asked): person ≈ 88 tall with head ≈ 12 —
  a bigger head is deliberately chibi; car ≈ 225 × 90 × 72, aligned to a
  lane with margin.
- ATMOSPHERE: `sky({ timeOfDay, weather })` for real outdoor light, plus
  `fog({ useBackgroundColor: true, near: ~2500, far: ~9000 })` scaled to
  the street's length so the far end melts away; a wide, LOW `terrain()`
  band or two in the far background closes the horizon (distant hills);
  `environment({ ao: true })`. A NAMED time of day or mood ("golden
  hour", "dusk", "sunset", "night", "overcast") is a HARD constraint:
  set `sky({ timeOfDay })` to match (~17.5-18.5 golden hour, ~19 dusk,
  12 noon) so the sun angle and color carry it, and check the
  screenshot actually reads warm/dark/gray as asked — a neutral
  white-daylight render of a golden-hour prompt fails review. FOG
  RESTRAINT: fog is for the FAR end only — if the mid-ground houses in
  the screenshot look pale or grayed, push `near`/`far` out (or thin
  the fog) until the hero block reads full-contrast; a scene-wide haze
  is the "cheap miniature" look, not atmosphere.
- FINISH PASS (not optional — flat single-tone facades down a whole
  street read as a cardboard model): give the road a subtle `noise`
  layer over its asphalt gray; vary each house's wall hue AND value a
  step within one muted family; put a real wall texture (stucco /
  brick / siding, `projection: 'triplanar'`, alpha 0.6–0.8) on at
  least the two or three houses nearest the camera — ONE style string
  shared across them (identical styles reuse one generated image;
  vary `repeat`/alpha/base color per house), and a roof-tone
  variation or tile texture on their roofs; walk the ARM'S-LENGTH
  check above (doors with frame + inset + knob, no bare reachable
  wall); build reachable street furniture from its parts — a bench
  is slats on legs and a backrest, never one solid box; keep
  lawns/verges muted (`'#6a8f5a'`-family, never saturated toy green);
  `environment({ ao: true })` always.
- CAMERA: a raised three-quarter looking DOWN the street axis (azimuth
  within ±30° of the road direction, elevation 10–18° — nearer eye
  level than drone, so facades face the camera — distance framing the
  whole block). Top-down diorama angles miniaturize the scene —
  they're for the stylized register. ENCLOSED places (a town square,
  plaza, courtyard) are framed from just INSIDE the enclosure — near
  one edge, looking across the fountain/space to the far facades
  (elevation 8–15°); from outside the building ring the render reads
  as a model on a table, not a place. Either way the GROUND runs to
  the frame edges: a wide muted surround plane (paving/grass) beyond
  the built block, so no raw background shows below the horizon.

## Towers & city blocks

A tower is storeys × S tall with a REPEATING window grid — loop it, never
freehand it. For a whole block/skyline, boxes with a `layer('texture',
{ style: 'modern office building glass facade with lit windows, seamless' })`
beat hundreds of window meshes; vary heights and footprints per building
(loops + `rand()`), keep every edge crisp, and light it with one key + fog
for depth.

CITY COUNT: a "city" is a COUNT before it is anything else — it starts
reading as one around ~40 distinct buildings and improves past 80. LOOP
a grid of blocks (vary footprint, height, setback, and a few degrees of
yaw via seeded `rand()`), carve street gaps, and step heights toward a
downtown cluster; 10–15 hand-placed chunky boxes is a train-set, not a
city. This holds in EVERY register, including the white
museum/architectural-model style: that look comes from the monochrome
palette and crisp edges, NOT from fewer, simpler buildings. A model
city on TERRAIN (topographic style) pairs with mountains built at the
procedural-generation skill's MOUNTAIN settings (resolution 200+,
octaves 5–6) — smooth default hills beside a detailed city read as
unfinished dough. Waterfront cities: thin bridge/causeway decks between
land masses, piers, and small hull-shaped boats at true relative scale
— a dense city ringed by EMPTY flat water reads abandoned.

## Order of work

Structure (walls + roof + chimney) → openings (door/windows/frames) →
materials/textures → ground & dressing → lights/AO/fog → group + name (a
later call than creation) → `set_view({ objects: [...] })` +
`take_screenshot()` → judge against the quality bar (style fidelity first)
→ final `lookFrom`.
