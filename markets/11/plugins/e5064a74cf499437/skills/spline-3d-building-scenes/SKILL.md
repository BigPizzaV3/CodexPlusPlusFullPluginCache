---
name: spline-3d-building-scenes
description: "Composing full scenes: units & spatial layout, grounding objects, scatter loops & cloner randomness for dense dressing, lighting & shadow tuning, fog/AO atmosphere, camera framing, color palettes, typography & the font catalog, prettify/style, arranging and grouping."
---

# Building Scenes

Guidance for composing a complete, well-framed 3D scene from scratch. Honor
the style register first (see # Style register in your core guidance):
unstated style = believable, not toy. Buildings — houses, towers, rooms —
additionally have their own `architecture` skill with proportion and
construction recipes; load it alongside this one for those.

## Units & default sizes
The editor uses arbitrary world units (loosely "pixels"). Keep a mental model
of the defaults so spacing reads correctly:

- A new mesh (`add('Mesh','CubeGeometry')` / `mesh('Cube', {})`) appears at the
  current BUILD CENTER — the camera's look-at, or the free anchor the editor
  picks when the scene already has content (given in `<editor-context>`) — NOT
  necessarily the world origin. It arrives auto-selected. Pin only the axes you
  must (usually `y`) and offset with `translate` so independent builds don't
  pile up at the origin.
- Default 2D-ish primitives (Rectangle) are about 320 x 320.
- Default Sphere / Cube are about 100 x 100 x 100.
- The default camera sits around z = 1000 looking at the origin, so objects in
  the -300..300 range read at a comfortable size. Spread multiple objects by a
  few hundred units, not a few units.
- BELIEVABLE-register anchor: treat 1 real-world meter ≈ 50 units and size
  real-world subjects from the # Real-world scale table in your core guidance
  (person 88, door 105, storey 150, car 225 long, two-lane road ≈ 300 wide,
  street tree 300-600). A real PLACE — a street, plaza, yard — spans
  THOUSANDS of units: build it at true scale and pull the camera back rather
  than shrinking the world to fit the default view; a shrunken place is what
  reads as a toy diorama.

Because every newly created object is auto-selected, the cleanest pattern is:
create -> immediately transform/color the selection -> create the next object.

## A minimal repeatable recipe
```
// 1. one hero object on the ground
mesh('Sphere', { width: 200, height: 200, depth: 200 });
color('#e0552b');
position({ y: 100 }); // sit it on the floor; x/z stay at the build center
rename('Hero');

// 2. a ground plane (rotate the plane flat, push it down)
mesh('Plane', { width: 3000, height: 3000 });
rotation({ x: -90 });
position({ y: 0 }); // ground it; x/z stay at the build center
color('#f2f0eb');
rename('Floor');

// 3. light + a soft background
light('Directional', { intensity: 0.9 });
translate({ x: 400, y: 600, z: 500 }); // offset the key light from the build center
background('#dfe3e8');
```

## Shape geometry parameters
Beyond `width`/`height`/`depth`, each primitive takes shape-specific params. Set
them at creation (`mesh('Cube', { cornerRadius: 20 })`) or later on the selection
with `geometry({ ... })`. The useful ones per shape:

- `Cube`: `cornerRadius` + `cornerSegments` (a rounded box reads as soft/plush —
  a stylized cue; NOTE it SPAWNS at cornerRadius 8, so pass `cornerRadius: 0`
  for crisp believable hard surfaces), `widthSegments`/`heightSegments`/
  `depthSegments`.
- `Sphere`: `widthSegments`, `heightSegments` — smoothness; low counts = faceted.
- `Cylinder`: thickness = `radius` (= half `width`; default `width` is 100, so
  an unsized cylinder is a fat 100-wide slug — pass `radius` or `width` for a
  slim pole/trunk). `radiusTop`/`radiusBottom` set only the TAPER — they're
  ratios relative to `width` (unequal → a taper/frustum), NOT absolute radii, so
  equal values do not make it thinner. Plus `radialSegments`, `openEnded`,
  `hollow` (0-1 wall thinness, NOT a boolean — 0.8 → a pipe/tube; `true`
  degenerates to a zero-thickness wall), `cornerRadius` (spawns at 8 — set 0
  for a crisp rim).
- `Cone`: thickness = `radius` (= half `width`; same default-100 caveat as
  `Cylinder`), `radialSegments`, `openEnded`, `cornerRadiusTop`,
  `cornerRadiusBottom`.
- `Pyramid`: `radialSegments` = base side count (3 = tetrahedron, 4 = square
  base). A 4-sided Pyramid is AXIS-ALIGNED — its faces line up with a `Cube`'s
  walls, so it caps a box squarely with the SAME Y rotation as the walls; never
  add a 45° yaw to "align" a roof, that extra rotation is what twists it off.
  (A 4-sided `Cone` sits diagonally by comparison — use `Pyramid` for a square
  roof.) Also `cornerRadius`.
- `Torus`: `radialSegments`, `tubularSegments`, `cornerRadius`.
- `TorusKnot`: `tube` (thickness), `p` and `q` (the knot winding — try 2 and 3),
  `radialSegments`, `tubularSegments`.
- `Ellipse` (circle/disc): `innerRadius` — a PERCENT of the outer radius
  (0-100, not world units; > 0 → a ring/annulus), `spikes`.
- `Polygon`: `spikes` = number of sides (3 = triangle, 6 = hexagon),
  `cornerRadius`.
- `Star`: `spikes` = number of points, `innerRadiusPercent` (point sharpness),
  `cornerRadius`.
- `Plane`: `widthSegments`, `heightSegments` (subdivide for a displaced surface).
- `Rectangle`/`Triangle`: `cornerRadius`.
- `Dodecahedron`/`Icosahedron`: `detail` (0 = base solid; higher subdivides
  toward a sphere), `corner`, `cornerSides`.
- `Helix`: `revolutions`, `radius`, `pathRadius` (coil thickness), `segments`.
- `Backdrop`: `cornerRadius` — an infinity-curve floor-to-wall sweep; a great
  seamless studio background behind a hero object.
- `Lathe`: a profile revolved around Y into a vase / bottle / bowl / glass.
  `points` is ONE cubic bezier — exactly 4 `[x, y]` control points (x =
  radius >= 0, y-down), not an arbitrary polyline; `segments` and
  `verticalSegments` control smoothness. Load the `lathe` skill for the full
  contract and profile recipes before building one.
- `Decal`: a projector box that stamps its OWN material onto every mesh
  surface inside it — the tool for stickers, labels, logos, racing numbers,
  splashes, impacts, graffiti and wear (see the SURFACE DETAIL rule in your
  core guidance). `width`/`height` size the stamp, `depth` is the reach —
  keep it generous, the box must pass THROUGH the receiving surface —
  and `offset` lifts the skin off the surface (default 1, so it never
  z-fights). Aim it like the flat Rectangle it replaces: unrotated stamps a
  camera-facing side, `rotation({ x: -90 })` a floor/tabletop, `{ y: 90 }`
  a +X side panel, `{ y: 180 }` the far side. Image + alpha-cutout recipe:
  the `materials-and-look` skill's Decals section.
- `Text`: `text` (the string; `\n` breaks a line), `fontSize`, `font` (the
  font id — see ## Typography below), `lineHeight` and `letterSpacing`
  (multipliers of the font size), `horizontalAlign` / `verticalAlign`. Width
  and height are the text BOX (`mesh('Text', { fontSize })` sizes one for you);
  a box narrower than the copy wraps it.

Flat shapes (`Rectangle`, `Ellipse`, `Polygon`, `Star`, `Triangle`, `Text`) also
take a `depth` that EXTRUDES the 2D outline into a solid, plus `extrudeBevelSize`
/ `extrudeBevelSegments` to round the extruded edge — e.g. a chunky 3D star or a
beveled logo.

Partial-sweep params are plain DEGREES: a torus `arc` (0-360), a sphere
`thetaLength` (0-180, sweeping down from the top pole), a cone/cylinder
`thetaLength` (0-360), a backdrop/ellipse `angle`. `mesh('Torus', { arc: 180 })`
is half a donut; `{ thetaLength: 90 }` on a sphere is a dome.

## Typography
A `Text` left on the default Roboto reads as unstyled. Pick a face that
carries the register: geometric sans (`Poppins`, `Outfit`, `Space Grotesk`)
for product/tech, a condensed display cut (`Bebas Neue`, `Anton`, `Oswald`)
for posters and signage, a serif (`Playfair Display`, `Fraunces`, `Lora`) for
editorial/luxury, mono (`JetBrains Mono`, `Space Mono`) for code and HUDs,
script (`Caveat`, `Pacifico`) for handwritten notes. Two families per scene is
plenty — one for headlines, one for body — and keep it consistent with the
scene's HTML overlay if there is one.

Valid font ids (format `{Family}_{variant}`, default `Roboto_regular`):

- **Sans (UI)**: `Inter` (regular, 500, 600, 700), `Roboto` (regular, 500, 700, italic), `Poppins` (regular, 500, 600, 700), `Work Sans` (regular, 500, 600, 700), `DM Sans` (regular, 500, 700), `Manrope` (regular, 500, 600, 700), `Lato` (regular, 700, italic), `Open Sans` (regular, 500, 600, 700), `Nunito` (regular, 600, 700), `Montserrat` (regular, 500, 600, 700), `Source Sans 3` (regular, 600, 700), `Space Grotesk` (regular, 500, 700), `Outfit` (regular, 500, 700), `Figtree` (regular, 500, 700), `Plus Jakarta Sans` (regular, 500, 700), `IBM Plex Sans` (regular, 500, 700), `PT Sans` (regular, 700)
- **Display**: `Bebas Neue` (regular), `Oswald` (regular, 500, 700), `Anton` (regular), `Archivo Black` (regular)
- **Serif**: `Fraunces` (regular, 600, 700), `Playfair Display` (regular, 600, 700, italic), `Lora` (regular, 600, 700, italic), `Merriweather` (regular, 700), `EB Garamond` (regular, 600, italic), `Cormorant Garamond` (regular, 600, italic), `Source Serif 4` (regular, 600, 700), `Libre Baskerville` (regular, 700, italic), `Roboto Slab` (regular, 500, 700)
- **Monospace**: `JetBrains Mono` (regular, 500, 700), `Fira Code` (regular, 500, 700), `IBM Plex Mono` (regular, 500, 700), `Space Mono` (regular, 700), `Roboto Mono` (regular, 500, 700)
- **Handwritten / Script**: `Caveat` (regular, 700), `Pacifico` (regular), `Dancing Script` (regular, 700), `Permanent Marker` (regular), `Shadows Into Light` (regular)

Join family and variant with `_` — `mesh('Text', { text: 'Studio', font: 'Playfair Display_700' })`, `geometry({ font: 'JetBrains Mono_regular' })`, `Roboto_italic`. Spaces inside family names are preserved.

- **Weight is the variant, not a separate prop** — there is no `bold`/`fontWeight` on text. Bold = the `_700` id.
- **Italic exists only where listed** — `Roboto`, `Lato`, `Playfair Display`, `Lora`, `EB Garamond`, `Cormorant Garamond`, `Libre Baskerville`. Asking for it elsewhere silently gives you the upright cut.
- A family in the catalog with a cut it doesn't list resolves to its nearest weight; a family that isn't in the catalog at all THROWS — don't invent fonts outside this list, and don't try to load a URL yourself.
- Fonts load asynchronously: the glyphs appear a beat after `run_code` returns. That is normal — don't "fix" it by re-setting the font.
- 3D extrusion (a `depth` on the text) reads best on the heavier cuts. Hairline and script faces lose their strokes once extruded and beveled.

## Grounding
Objects are created centered on their origin, so a 200-tall sphere whose center
is at y=0 will be half-buried in a floor at y=0. Lift it by half its height
(`position({ y: 100 })`). For a flat floor, create a `Plane` and rotate it
`{ x: -90 }` so it lies in the XZ plane.

SHADOW-CATCHER FLOORS: when the floor exists only to ground the subject —
product shots, a logo or hero object over a clean background color/gradient,
minimal studio looks — make it invisible and keep just the shadows:
`visibility({ shadowCatcher: true })` on that Rectangle/Plane (only those two
geometries support it). The slab disappears, the page background shows
through, and the cast shadows stay — instant "floating over the page" look
with real grounding. Pair it with a background color and a directional key
light so there IS a shadow to catch. Skip it when the floor's own surface is
part of the scene (boards, roads, grass — those want a real material).

Tip: the all-in-one `studio()` / `stage('studio')` helper builds a neutral
ground + key light + studio materials in one call. Prefer it when the user just
wants "a nice render" rather than a specific layout.

## Lighting setup
- LIGHT BUDGET — reuse before adding. Check the scene snapshot for existing
  lights (DirectionalLight / PointLight / SpotLight) first; if one is there,
  `select(o => o.isLight)` and `updateLight` / `position` it rather than
  adding another. One directional key over the built-in ambient fill is
  enough for most DAYLIGHT scenes — cap those at 3 lights unless the user
  explicitly asks for more. NIGHT/INTERIOR scenes may run more local
  Points/Spots when each has a visible job (a lamp, a sign, a doorway);
  keep shadows on at most 1–2 of them.
- `light('Directional', { intensity: 0.9 })` is the workhorse key light. It
  spawns offset +100 on each axis from the build center; `translate` it to
  taste, e.g. further up and to one side.
- LIGHT SIZE follows the scene footprint: a directional light's shadows
  exist only inside its `size` footprint (default 2000 world units). Big
  builds — buildings, city blocks, castles — outgrow that fast, and the
  shadow field visibly cuts off mid-scene. Whenever the scene spans more
  than ~2000 units, set `size: 4000` or more, matched to the whole area
  (`updateLight({ size: 6000 })` on the key light).
- OPTIONALLY add a dimmer `light('Point', { intensity: 0.4 })` on the opposite
  side as fill to soften shadows — only when the key + ambient alone leave the
  shadow side too harsh, not by default.
- EXPOSURE BUDGET: every light stacks on top of the always-on ambient fill
  (default intensity 0.75), so the sum of key + fill + ambient is the scene's
  exposure — and the right numbers depend on the REGISTER. DAYLIGHT: key at
  0.8–1, fills 0.3–0.4, and when you add a fill, dim the ambient to
  compensate; if the live shot still reads flat after repositioning, the key
  may go up to 2 — past that fix the ambient or palette instead.
  NIGHT/INTERIOR: dim the ambient and let local Points/Spots CARRY the
  exposure at `intensity` 2–8, shaped with `distance`/`decay` into tight
  pools — judge by the live capture (subject readable, highlights not
  clipping), and pair glowing materials with a small Point/Spot: emissive
  glows but does not illuminate surroundings.
- Light `color` accepts hex/CSS strings; a warm key + cool fill reads well.
- Valid light types: `'Point'`, `'Spot'`, `'Directional'` (the alias appends
  `Light` for you, so `'Directional'` -> `'DirectionalLight'`).
- SHADOW TUNING is real and cheap: every light takes `shadows` (on/off,
  default on) and `shadowRadius` (softness — 1 is crisp, raise toward 4–8
  for soft). `light('Directional', { intensity: 0.9, shadowRadius: 4 })`.
  `shadowResolution` (map size) STAYS at its low default (512) — the right
  performance call for generated scenes; raise it (1024/2048) only when the
  user explicitly asks for crisper/hero shadows.
- The page has a built-in AMBIENT fill (hemisphere-style sky/ground light).
  Tint and dim/boost it with `environment({ ambient: { color: '#bcd4ff',
  intensity: 0.7 } })` — a cool ambient + warm key is the classic outdoor mix.
  Don't fake ambience with extra point lights.

## Atmosphere (fog, AO, soft shadows)
Flat single-color backgrounds with no depth cues read as tech demos. The page
environment fixes that in one or two calls:
- `fog({ useBackgroundColor: true, near: 800, far: 4000 })` — distance fog
  blending toward the background color; distant objects melt into the sky.
  Tune `near`/`far` to your scene's depth (they're world units from the
  camera). An explicit `color` overrides the background blend.
- `environment({ ao: true })` — ambient occlusion: contact/crevice darkening
  that visually GROUNDS objects on surfaces. Cheap realism, almost always
  worth enabling for built scenes.
- LEAVE the global shadow type (`environment({ softShadow })`) alone: it is
  'normal' (stock filtering) in new documents — the right performance call for
  generated scenes, since PCSS soft shadows cost render time every frame — and
  soft in older ones, whose look was authored against it. Shape the shadow
  look with the per-light `shadowRadius` / `shadowResolution` instead.
  Switch to soft shadows ('low' | 'medium' | 'high' quality) only when the
  user explicitly asks for soft shadows.
- `fog('none')` / `environment({ ao: false })` switch them off.

## Camera framing
- `lookFrom(spec)` CHOOSES the vantage and aims the viewport camera. `spec` is a
  preset ('front'|'back'|'left'|'right'|'top'|'bottom'|'iso'|'threeQuarter') or
  `{ azimuth?, elevation?, distance?, target? }` in degrees (azimuth 0=front,
  90=right, -90=left, 180=back; elevation 0=eye level, positive=above looking
  down, 90=top-down). This is how you get a hero 3/4, a top-down flat-lay, or a
  straight-on shot. Omitted `distance` FITS the target's real bounds (the
  selection's with `target: 'selection'`, the scene's content cluster
  otherwise — a bare preset call also aims at that cluster): the framing is
  computed, so never hand-pick distance numbers for final shots. Don't chain
  `focus()` after it in the same call — `lookFrom` already frames.
- `focus(target?)` / `centerView(target?)` re-frames the selection (or a passed
  target) at the CURRENT angle, without rotating; `zoom(target)` is an alias of
  focus for objects.
- `viewport('isometric'|'perspective'|'orthographic'|'reset')` changes the
  PROJECTION only — angle and projection are independent.
- `activateCamera(cameraRef?)` makes a scene camera (from `add('PerspectiveCamera')`)
  the live editor view; `activateCamera('personal')` returns to the default camera.
- These aliases move the USER's viewport — use them to set the final
  presentation angle, e.g. `lookFrom('threeQuarter')` in a NEW run_code call
  once the build is done. For YOUR OWN verification screenshots use the
  `set_view` TOOL instead: `set_view({ objects: [...] })` fits your private
  screenshot camera to your work without moving the user; nudge its
  azimuth/elevation a few degrees to add depth or reveal a hidden side, then
  `take_screenshot()`.
- SET-DRESSING RECIPES (the SUPPORTING CAST rule's concrete forms — pick
  the matching register, build scatter via loops/cloners with varied
  rotation/scale):
  tabletop/food — tray or board, napkin/cloth, side dish, drink, garnish
  or crumb scatter, one utensil;
  shop/interior — signage (text primitive), shelf or counter clutter, a
  floor mat/rug, 2–3 hanging or wall fixtures, a door/window hint;
  outdoor/nature — ground break-up (rock + grass-tuft scatter along paths
  and edges), 2–3 background silhouettes (trees, hills), sky treatment;
  arcade/game — marquee text, coin/ticket scatter, a neighboring cabinet
  or prop that hints at the venue;
  workshop/studio — tools on the wall, work-in-progress clutter, one
  visible light fixture as an object.
- FINISHING RITUAL (every scene build ends with this, in order): (0) the
  BRIEF-NOUN CHECKLIST from the quality bar passes — every concrete noun
  in the prompt exists, at its implied count, and is identifiable in the
  frame; (1) the
  scene has a deliberate background — `background(...)` or `style([...])`,
  never the editor's default grid void; (2) set the user's final vantage
  with `lookFrom`/`focus` on the hero content — for an INTERIOR brief that
  vantage is INSIDE the room at eye level (`select` the focal furniture,
  `lookFrom({ ..., target: 'selection' })`; never an exterior dollhouse
  shot of the shell); (3) verify with
  `take_screenshot({ view: 'live', hero: [<the brief's main object
  names>] })` — the USER'S actual view, not your
  private camera, which can frame the work perfectly while the user's view
  shows none of it — and the `hero` names are REQUIRED on the final
  check: they make the check measure the SUBJECT itself; (4) the live
  capture returns an EXPOSURE CHECK, a
  FRAMING CHECK, and a HERO CHECK — treat any warning as a failed final:
  if the frame crops
  the subject, shows it tiny, shows bare background/grid/sky, reads
  near-black, washed out, or as one flat color, or reports the hero
  off-frame, cropped, hidden behind other geometry, under ~18% of the
  frame, or overflowing it (too close), fix it and re-check. SUBJECT
  SCALE: a single-object brief (a dish, a toy, one machine, one small
  creature) is a CLOSE-UP — the subject at a third to half the frame
  height, not a speck in a room-wide shot. Do this
  EARLY too (as soon as the main structures exist), so a run cut off at a
  step ceiling still leaves a composed view. (5) Passing the check is the
  FLOOR: now polish — name the biggest weakness in the live frame (staging
  density, composition, lighting, materials, a missing brief noun), fix it,
  re-verify, and COMPARE with the previous capture: keep the change only if
  the frame reads better, REVERSE it if worse (fog/haze and camera
  pull-backs are the usual regressions), and keep the subject filling the
  frame after every cycle. At most your Refine allowance of cycles (TWO by
  default; a raised allowance arrives as a "REFINE setting" line in
  <editor-context>), then stop and summarize — once the measured checks
  pass, further nits are churn; keep cycling past the allowance ONLY while
  a declared time budget remains (IMPROVE WHILE BUDGET REMAINS in the
  quality bar).

## Color palettes
Pick 3-5 cohesive hex colors and apply them per object with `color()`. Match
the palette to the style register: an unstated style (the believable default)
wants muted, desaturated real-world tones with value contrast; save saturated
candy primaries for explicitly cute/stylized asks. Two powerful global helpers
exist:

- `prettify()` — auto-harmonizes every material's colors into a pleasing scheme
  (no arguments). Great as a finishing pass.
- `style(['#hex', ...], seed?)` — recolors all materials AND the background from
  a palette you supply. Pass an array of hex strings.

```
style(['#1b1f3b', '#e94f37', '#f6f7eb', '#44bba4']);
```

## Arranging multiple objects
- `arrange(margins?, target?)` spreads the selection apart so nothing overlaps,
  leaving `margins` units of gap. Select first, then call `arrange(40)`.
- For regular grids/rows, prefer the `clone` cloner (see below) or place items
  explicitly with `position()`.
- `align(path, { animate })` snaps the selection onto a path object.

### Scattering N varied objects with a loop (the density workhorse)
Bounded `for`/`while` loops around alias calls run fine in the sandbox — a
loop of create + transform calls is the NORMAL way to place many objects.
Vary size, position, and rotation per iteration so nothing repeats exactly:
```
for (let i = 0; i < 10; i++) {
  const s = 0.5 + rand();
  mesh('Icosahedron', { width: 60 * s, detail: 0 });
  color(i % 2 ? '#8d8d93' : '#75757c');
  position({ y: 30 * s });
  translate({ x: (rand() - 0.5) * 1200, z: (rand() - 0.5) * 1200 });
  rotation({ y: rand() * 360, z: (rand() - 0.5) * 30 });
}
```
Sparse scenes read as unfinished — "a scene" implies secondary and tertiary
dressing, and loops make it cheap. Keep counts bounded (tens, not thousands).

When the scattered copies share one look (the same rock grey, one foliage
green), don't restyle each iteration — create the material ASSET first and
link every copy to it (see materials-and-look). One `updateMaterial` then
restyles the whole batch:
```
createMaterial('Rock Grey', { layers: [{ type: 'color', color: '#8d8d93' }] });
for (let i = 0; i < 10; i++) {
  mesh('Icosahedron', { width: 60, detail: 0 });   // new mesh is the selection
  applyMaterial('Rock Grey');
  // …position/rotation variation as above
}
```

### Cloners (procedural duplication)
`clone({...})` turns the selected object into a cloner. Each `type` has a
same-named sub-object of settings; unspecified keys keep sensible defaults.
Calling `clone` on an object that is ALREADY a cloner MERGES — partial props
edit it in place (`get_objects` returns the current settings in this same
shape). `hideBase: true` hides the original object. Useful shapes:
```
// a 5x1x5 grid; grid.size is the spacing per axis (default: object size +10%)
clone({ type: 'grid', count: [5, 1, 5], grid: { size: [120, 0, 120] } });

// linear accumulates PER STEP — each clone offsets/rotates (in degrees) by
// this much more than the previous one: stacks, spiral staircases, twisted
// towers, fanned cards. scale is a LINEAR ramp, not compounding: clone i gets
// 1 + (scale - 1) * i, so 0.94 hits zero around clone 17 — keep shrink
// factors close to 1 on long stacks. (Default is a small +X offset.)
clone({ type: 'linear', count: 12,
  linear: { position: [0, 40, 0], rotation: [0, 25, 0], scale: [0.94, 0.94, 0.94] } });

// a radial ring — SET radial.radius (the default, 2x the object's size, is
// usually too tight). start/end (degrees) make a partial arc, alignment: true
// faces each clone along the ring, axis ('x'|'y'|'z') picks the ring plane.
// Unlike linear, radial's position/rotation/scale are a CONSTANT offset
// applied to every clone — position [0, 40, 0] raises the whole ring, it
// does NOT spiral.
clone({ type: 'radial', count: 12, radial: { radius: 260, alignment: true } });
```

Cloners can RANDOMIZE every instance — position/rotation/scale jitter with a
seed — which turns a rigid grid into organic scatter in one call. Unspecified
`randomnessObject` keys keep their defaults (`strength` 100, `movement` 1).
The scatter is STATIC: `movement` is a phase offset into the noise, not
motion — changing it (like `seed`) just reshuffles the pattern; nothing
drifts on its own. `freqScale`/`noiseType` ('perlin'|'simplex') shape the
noise:
```
// a 6x1x6 patch of the selected object, jittered into a natural-looking field
clone({ type: 'grid', count: [6, 1, 6], randomness: true,
  randomnessObject: { strength: 100, position: [80, 0, 80],
    rotation: [0, 180, 0], scale: [0.4, 0.4, 0.4], seed: 3 } });
```

`cloneTo(target, { count, spreadType, seed })` distributes clones onto another
object's SURFACE — trees/rocks over a terrain mesh, spikes over a sphere.
`select` returns an ARRAY of matches and `cloneTo` takes ONE object, so grab
the target with `[0]` first:
```
const island = select(o => o.name === 'Island')[0];
select(o => o.name === 'Tree');
cloneTo(island, { count: 18, spreadType: 'random', seed: 7, hideBase: true });
```
(`spreadType`: 'random' | 'polygon_center' | 'vertex' | 'edge' — for the
non-random types `count` means a PERCENTAGE (0-100) of the candidate spots
and `seed` is ignored. `align: 'normal'` tilts each clone to the surface
normal; `align: 'axis'` + `axis` ('x'|'-x'|'y'|'-y'|'z'|'-z') keeps a fixed
orientation instead. `hideBase: true` hides the original left at its old
spot.)

## Procedural custom geometry (`customMesh`)
The parametric primitives can't make terrain, rocks, or organic forms — for those,
GENERATE the geometry. Build flat `vertices` (and `indices`) arrays with loops +
Math, displacing points to shape them, then pass them to `customMesh` (normals are
auto-computed). Patterns:
- Terrain/island: a grid or concentric rings of vertices on the XZ plane with `y`
  displaced by `Math.sin`/`rand()` for hills; triangulate adjacent vertices into
  quads (two triangles each).
- WINDING — the XZ-plane gotcha: normals come from index order (CCW seen from
  OUTSIDE = front), and on the XZ plane an angle loop `(cos a, ·, sin a)` runs
  CLOCKWISE seen from above — the OPPOSITE of 2D XY intuition. Up-facing
  patterns: ring fan `idx.push(center, 1 + (s+1)%seg, 1 + s)` (note: NEXT
  angle before CURRENT); ring band `(base+s, base+sn, next+s)` +
  `(base+sn, next+sn, next+s)`; grid quad `(i, i+cols, i+1)` +
  `(i+1, i+cols, i+cols+1)`. Slips are safety-netted — an inside-out CLOSED
  solid is auto-flipped (signed-volume test), and an OPEN surface (disc,
  heightfield — anything with a boundary edge) renders double-sided — so a
  winding mistake can't make the mesh invisible, but correct winding still
  gives the cleanest normals/AO/shadows.
- Faceted rock: a low-segment dome/fan of vertices, each jittered by `rand()`.
- Low-poly tree: a `customMesh` cone of foliage over a thin `mesh('Cylinder')` trunk.
Vertices are used at their REAL world-unit size (no normalization) — generate
them at the final scale you want instead of building small and scaling up.
Keep vertex counts modest (hundreds). For the faceted low-poly look, set
`shading({ flatShading: true })` on the result (indexed meshes otherwise get
smooth averaged normals). Check proportions with the `size` [w,h,d] that
`run_code`/`get_scene` report for each object — that's the ground truth for
alignment — and save `take_screenshot()` for judging the LOOK.
Compose several such meshes (varied scale/rotation/color) for a rich scene rather
than relying on a few bare primitives.

## Grouping & structure
- `group(target?)` groups the selection (or creates an Empty if nothing is
  selected) and RETURNS the group. Group related parts so the user can move
  them together.
- ONE THING = ONE GROUP. The scene tree the user expects mirrors the things
  you built, not the primitives they're made of: a table is a 'Table' group
  containing its top and legs, a refrigerator is a 'Refrigerator' group
  containing body/door/handle, a forest is a 'Trees' group containing the
  scattered trunks/canopies. Build the parts with a shared name prefix
  ('Table Top', 'Table Leg 1', …), then select by that prefix, `group()`,
  `rename('Table')` — all in the same run_code call, since select() sees
  objects created earlier in that call. Grouping makes every later step
  cheaper — posing, duplicating, animating, and the user's own edits all get
  one handle per thing instead of a flat pile at the root.
  Independent things stay SEPARATE sibling groups (never one grab-bag), and
  cameras/lights that serve the whole scene stay at the root.
- COMPOUND ASSEMBLIES — build straight, group, rotate ONCE. When an object is
  made of several primitives (a mushroom = stem + cap, a rocket = body + nose
  + fins), build every part UNROTATED in the upright frame, stacking them with
  `position`/`translate` so they align on a shared axis. Then group and apply
  any tilt to the group — one rotation, applied last. Rotating each part
  individually to pose the assembly is how parts end up misaligned: each part
  pivots around its OWN center, so equal angles still shear the stack apart.
  ```
  // build the parts straight (no rotation), then select/group/pose — all in
  // ONE call: select() sees objects created earlier in the SAME run_code.
  mesh('Cylinder', { radius: 20, height: 120 });
  position({ y: 60 });
  rename('Stem');
  mesh('Sphere', { width: 140, height: 90, depth: 140 });
  position({ y: 140 });
  rename('Cap');
  select(o => o.name === 'Stem' || o.name === 'Cap');
  const g = group();
  rename('Mushroom');
  rotation({ z: -15 }); // the ONLY pose rotation, on the group
  ```
  Per-part rotation is still right for a part's own local shape (laying a flat
  shape down with `rotation({ x: -90 })`, turning a cylinder sideways for an
  axle) — do that when creating the part, before grouping, not to pose the
  whole assembly.
- `moveInto(parent, target?)` reparents into an existing group/object (by
  object, id, name, or 'root'); world positions are preserved. Use it to
  organize an existing scene's tree: `const g = group(...); rename('Props');`
  then `moveInto(g, o => o.shape('rock'));`.
- `ungroup(target?)` dissolves a group — children hoist to its parent, the
  empty wrapper is deleted.
- `hide(target?)` / `show(target?)` toggle scene-tree visibility — prefer
  hiding over deleting when the user might want something back.
- `rename('Name')` names the selected object — always name hero objects and
  groups so the scene tree is readable.
- `duplicate(target?)` copies the selection in place.
- `remove(target?)` deletes the selection (`remove('all')` clears the scene).

## Suggested order of operations
1. (existing scene) read the `<editor-context>` scene digest in the user's
   message to learn what's there — no `get_scene()` call needed until you have
   edited something and want to verify it.
2. Block out hero geometry and ground.
3. Dressing pass — scatter secondary/tertiary elements (loops, cloner
   randomness, `cloneTo`).
4. Color / material pass — in the believable register that means `physical`
   shading + texture layers on the big real-world surfaces (see
   materials-and-look), not just flat colors (or `prettify()` / `style()`).
   Whenever two or more objects need the EXACT same material, build it once
   and share it: `createMaterial` + `applyMaterial`, never N per-object
   copies of the same layer stack.
5. Lights + atmosphere (`fog`, `environment({ ao, ambient })`).
6. Frame YOUR check with `set_view({ objects: [...] })`, `take_screenshot()`,
   critique against the quality bar, iterate.
7. Set the user's final presentation angle with `lookFrom()`.
