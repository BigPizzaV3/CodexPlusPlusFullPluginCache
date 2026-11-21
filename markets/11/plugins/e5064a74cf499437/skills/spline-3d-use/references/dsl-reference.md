# Spline DSL quick reference

You write straight-line JavaScript made of calls to the alias functions below,
one statement per line, each ending with `;`. Vectors are partial objects like
`{ x: 100 }` (omitted axes are unchanged). Colors are hex/CSS strings. Rotations
are in DEGREES. The most-recently created object is auto-selected, so transform/
color/material calls after a creation apply to it.

Only these functions can change the editor, but you MAY use plain local
JavaScript around them: `const`/`let`, bounded `for`/`while` loops, arrays,
`Math`, and `rand()`/`Math.random()` for randomness. Do NOT use imports, the
DOM, network APIs, or `console`. Alias return values are usable within the
same block (`const rim = addLayer(…); updateLayer(rim.id, …)`); the READ
aliases (`listMaterials`, `getMaterial`, `getGeometry`) additionally echo
their data back in
the run_code result — a block that only reads is valid and returns the data.
To return data your script COMPUTED (a profile summarized from getGeometry
arrays, measured gaps), call `report(value)` — it echoes any JSON value the
same way. Never `throw` data out: a throw fails the call and shows the user
an error.
Do NOT capability-probe the sandbox: every documented function is callable
exactly as written, but they are host-routed, so introspection proves nothing
about what a call returns — `Object.keys` of a selection handle lists only
transform metadata (mesh VERTEX data is never a key on any handle; it is read
by CALLING `getGeometry`). Never conclude a documented function or its data
is unavailable from a probe — call the function.

## Create
- `add(objectType, geometryType?, params?)` — low-level create. objectType e.g.
  `'Mesh'`, `'PointLight'`, `'DirectionalLight'`, `'SpotLight'`, `'Empty'`,
  `'PerspectiveCamera'`, `'Particle'`, `'ParticleCollider'`. For meshes pass a
  geometryType (see below).
- `mesh(geometryType, params)` — friendliest mesh creator. The `Geometry` suffix
  is optional, so `mesh('Cube', { width: 200 })` == `add('Mesh','CubeGeometry')`.
  Geometry types: `Cube`, `Sphere`, `Cylinder`, `Cone`, `Pyramid`, `Torus`,
  `TorusKnot`, `Plane`, `Rectangle`, `Ellipse` (circle), `Polygon`, `Star`,
  `Triangle`, `Dodecahedron`, `Icosahedron`, `Helix`, `Lathe` (a bezier
  profile revolved around Y — vases, bottles, bowls, glasses; load the
  `lathe` skill before building one), `Backdrop` (a curved cyclorama floor-wall),
  `Text`, `Path`, `Decal` (a projector box that stamps its own material onto
  the mesh surfaces inside it — THE tool for surface detail; see the SURFACE
  DETAIL rule below). Common params: `width`, `height`, `depth`, `radius`, plus
  `text`/`fontSize`/`font` for Text. Every shape ALSO takes smoothness and rounding
  params (segment counts, `cornerRadius`, …); see the `## Geometry` section
  below and the `building-scenes` skill for the per-shape list. An unrecognized
  geometry name falls through to an `object(name)` library import.
- TYPOGRAPHY is a design choice — a `Text` left on the default Roboto looks
  unconsidered. `font` takes a font id, `{Family}_{variant}` — e.g.
  `mesh('Text', { text: 'Studio', fontSize: 120, font: 'Playfair Display_700' })`,
  or `geometry({ font: 'Bebas Neue_regular' })` on an existing one. The WEIGHT
  is the variant in the id (bold = `_700`); there is no separate bold/weight
  prop. Curated families incl. `Inter`, `Poppins`, `Montserrat`, `Space Grotesk`,
  `Bebas Neue`, `Anton`, `Oswald`, `Playfair Display`, `Fraunces`,
  `JetBrains Mono`, `Caveat`, `Pacifico` — the `building-scenes` skill lists
  the full catalog with each family's cuts, and naming a family outside it
  throws (the error names them all). Bare family = its regular cut. Glyphs
  appear a beat after run_code returns while the font downloads.
- Flat geometries (`Plane`, `Rectangle`, `Ellipse`, `Polygon`, `Star`,
  `Triangle`) spawn VERTICAL — standing in the XY plane, facing the camera. To
  use one as a floor/ground, lay it flat with `rotation({ x: -90 })`. Give any of
  them (except `Plane`) a `depth` to EXTRUDE the 2D outline into a solid 3D shape
  (e.g. an extruded star or a rounded-rectangle slab); `extrudeBevelSize` rounds
  the extruded edge. A flat shape whose job is to sit ON another object's
  surface as art (a mark, sign face, splash, label) is the wrong tool — that
  is a `Decal` (see SURFACE DETAIL below).
- `object(name)` — import a model from the asset library by name/tag, e.g.
  `object('tree')`, `object('chair')`. Matches a whole name/tag WORD and imports
  a RANDOM one of the matches (results vary run to run); a term with no match
  imports NOTHING — the run_code result reports 0 created, so check it and retry
  with another word rather than assuming it worked.
- `customMesh({ vertices, indices?, normals?, uvs? })` — build a mesh from raw
  geometry data, like a THREE.BufferGeometry. `vertices` is a flat
  `[x,y,z, x,y,z, ...]` array; `indices` are triangle vertex indices
  `[a,b,c, ...]` (omit for a non-indexed mesh). `normals` are computed if
  omitted. COMPUTE these arrays with loops + Math. This is how you make organic /
  low-poly geometry the parametric primitives can't (terrain, faceted rocks,
  custom trees, water). NOT for surface detail: a mark or image that lives ON
  an existing surface — sticker, label, logo, splash, impact, graffiti — is a
  `Decal` (see SURFACE DETAIL below), never a hand-built outline or thin
  plate hovering at the surface. Wind each triangle's indices counter-clockwise as seen
  from OUTSIDE the surface — normals are derived from winding. XZ-PLANE GOTCHA
  (terrain, discs, anything y-up): an angle loop `(cos a, ·, sin a)` runs
  CLOCKWISE seen from above, the OPPOSITE of the XY intuition — so an up-facing
  fan is `(center, next, current)` (DECREASING angle), and an up-facing grid
  quad on XZ is `(i, i+cols, i+1)` + `(i+1, i+cols, i+cols+1)`. Winding slips
  are safety-netted: a closed solid wound inside-out is auto-flipped, and an
  open surface (a disc/heightfield has a boundary) is rendered double-sided —
  but get it right anyway so normals, AO, and shadows behave. Vertices are used
  at their REAL world-unit size (no normalization) — build at final scale.
  Indexed meshes get smooth normals; for a faceted low-poly look use
  `shading({ flatShading: true })` on the result. The read companion is
  `getGeometry` (see ## Geometry): any mesh's live geometry back in this
  same shape, so read → tweak → re-emit round-trips.
- PREFER the procedural generators over hand-written customMesh loops for
  nature assets: `terrain({...})`, `ocean({...})` (directional Gerstner
  swells — ALWAYS use this for open water, never a plane or noise bumps),
  `tree({...})` (realistic by default; `style: 'stylized'` only for
  cute/cartoon registers), `rock({...})`, `globe({...})` (an EARTH globe
  with real recognizable continents + a `project(lat, long)` handle for
  city markers — mandatory for any globe/Earth ask; never noise blobs or
  AI-texture gambles for Earth) — tuned, deterministic (seeded)
  meshes — and
  `scatter({ on, source, count, seed })` distributes a source object across
  a surface with natural jitter (create + scatter works in one call). Load
  the `procedural-generation` skill for parameters and recipes BEFORE
  building forests, landscapes, any nature scene, ANY ocean/sea/lake/
  water-body scene (water is ALWAYS `ocean()` — never a flat plane with a
  displace layer, which reads flat and fake), or ANY
  "miniworld"/"mini world"/"diorama" prompt — those follow a strict
  contained-base-slab contract the skill defines (a floating block with
  clear square bounds, never a landscape on infinite ground).
- `particles('new', props?)` — create a particle EMITTER (snow, rain, fire,
  sparks, confetti, smoke, magic dust); `particles(props)` merges props over
  the selected emitter to edit it in place. Load the `particles` skill for
  the prop reference, recipes, and runtime control (the `'Particles'`
  action) before building with these.
- `hair('new', props?)` — create a HAIR SYSTEM: simulated strands (hair, fur,
  grass, fibers) with physics, wind, clumping, and root/mid/tip coloring.
  THE way to put hair on an object: `hair('new', { on: 'Head' })` grows the
  strands from that object's surface — NEVER model hair as custom geometry
  (tubes/cones), which reads rigid and fake. `hair(props)` merges props over
  the selected hair system (same edit contract as `particles`). Load the
  `hair` skill for the prop reference and recipes before building one.

## Transform (operate on the selection)
- `position({x?,y?,z?})` — set absolute position.
- `translate({x?,y?,z?})` — move relative to current position.
- `rotation({x?,y?,z?})` / `rotate(...)` — set rotation in DEGREES.
- `scale({x?,y?,z?})` — MULTIPLY current scale by these factors.

## Color & material
- `color('#hex')` — set the object's main color.
- `opacity(0..1)` — set transparency.
- `shading({ category, ... })` — lighting model: 'phong' | 'toon' | 'lambert' |
  'physical' (+ specular/shininess/roughness/metalness). Also drives the
  mesh's VISIBILITY panel knobs: `flatShading: true|false` (Shading
  Normal/Flat — faceted per-face normals), `side: 'front' | 'back' |
  'double'` (Sides — render both faces of open surfaces), and
  `wireframe: true|false` (Wireframe Show/Hide).
  `visibility({ wireframe?, flatShading?, side?, shadowCatcher? })` sets the
  same three directly; per-mesh shadow flags are `shadows(...)` below.
  `shadowCatcher: true` (Rectangle/Plane ONLY) turns the surface into a
  SHADOW CATCHER: the surface itself becomes invisible and renders only the
  shadows cast onto it — the scene background shows through everywhere else.
  Use it when a floor should ground objects WITHOUT reading as a visible
  slab: product shots / studio scenes over a clean background color or
  gradient, logos and hero objects floating over the page background, or any
  scene where a plain gray floor would cheapen the look. The catcher is
  automatic receive-only (it never casts) and its material panel is ignored
  while enabled. Don't use it when the floor's own surface matters (wooden
  boards, roads, grass) — those want a real material.
  Physical also takes `bumpMap`/`roughnessMap: 'texture'` — reuse the
  material's texture layer as relief/gloss maps (no metalness map; see
  materials-and-look). CAUTION with `roughnessMap`: it multiplies roughness
  by the texture's LUMINANCE, so a dark texture (slate, asphalt, dark wood)
  drives roughness toward 0 — a mirror-glass surface. On dark textures skip
  it and set a flat `roughness` instead.
- `layer(type, props?)` — update the TOP layer of `type` on the selection,
  creating it if missing. THE way to edit an existing material. Layer types
  incl. 'color','light','gradient','fresnel','glass','depth','texture',
  'noise','toon','outline','matcap','cavity','dust'. A 'texture' layer can AI-generate its
  image from a text prompt via `{ style: '…' }` (see the materials-and-look
  skill). The 'cavity' layer (edge-wear curvature shading) is OPT-IN: add
  it only when the user explicitly asks for it, never as a default
  finishing move. A 'fresnel' layer's `scale` caps at 1.0 — never set it
  higher (the rim clamps at 1; more only blows it out into a flat wash).
- `addLayer(type, props?)` — stack a NEW layer even if one of `type` exists;
  returns `{ id }` — capture it to edit later in the same block.
- `updateLayer(id, props)` / `removeLayer(idOrType)` — edit/remove a layer by
  id (from `addLayer`'s return or a selected object's `.layer(type).id`);
  `removeLayer` also accepts a type to remove the top layer of that type.
- Texture layer (`type: 'texture'`) props: `image` (reuse an EXISTING image
  asset id, e.g. one `generate_image` or `generateTexture` returned — no new
  generation, applies immediately), `style` (a text prompt instead — triggers
  Spline's OWN async image generation; the layer renders a checkerboard
  placeholder until it resolves, so re-`take_screenshot()` on a later turn
  rather than retrying; ignored if `image` is also given), `projection`
  ('uv' | 'planar' | 'spherical' | 'cylindrical' | 'triplanar' — friendly
  names accepted and converted for you), `axis` ('x' | 'y' | 'z' — only
  affects `planar` projection today), `texture: { repeat: [x, y], offset?,
  rotation? }` (tiling — the UI's "Scale"). MAPPING MATTERS: the `uv` default
  distorts on extruded shapes and elongated boxes — use `projection:
  'triplanar'` + `repeat` there, blend at `alpha` 0.6–0.8 over a matching
  base color, and keep bump low; see materials-and-look. Repeat is also
  RESOLUTION: one 512px tile stretched across a whole wall magnifies into
  blur no Sharpness setting can fix — tile it (`repeat` ≈ surface size /
  feature span) or generate at size 1024 for single-image hero surfaces.
- `generateTexture(name, draw, size?)` — DRAW a SEAMLESS texture yourself
  with plain canvas 2D and get `{ id }` back for `layer('texture',
  { image: tex.id })`. Local and instant (no image service): THE way to give
  real-world surfaces crisp repeating detail — brick/stone walls, roof
  tiles, wood planks, ceramic/checker floors, pavement — instead of leaving
  them flat or reaching for a noise layer. `draw: (ctx, { size, rng }) =>`
  runs replicated at the 8 neighboring tile offsets so anything crossing an
  edge wraps — which makes four rules load-bearing: randomness ONLY from
  the provided `rng` (never `rand()`), transforms only via
  translate/rotate/scale inside save/restore (never `setTransform`), an
  opaque full-tile base fill first, and each feature drawn ONCE (the wrap
  completes edge overhangs — a second copy "for the other edge" gets
  different rng values and mismatches the seam). Redrawing under the SAME
  name replaces the asset's pixels in place. Full drawing recipes in the
  texture-drawing skill.
- `material(materialState)` — replace whole material (advanced). Requires a COMPLETE material state incl. its `layers` array; partial objects are rejected — use `layer()`/`color()` to tweak. Never deep-copy a material with `JSON.parse(JSON.stringify(…))`: it turns texture image bytes into huge plain objects.
- Reusable material assets — THE RULE: whenever two or more objects need the
  EXACT same material (all the windows, every brick wall, each tree's
  foliage, repeated props), build the look ONCE on one object,
  `createMaterial('Name')`, and `applyMaterial('Name')` to the rest — do
  NOT rebuild the same layer stack per object. Shared assets keep the file
  small and make restyles one call instead of N (full guide in
  materials-and-look): `createMaterial(name, { layers? }?)` saves the
  selection's material as a shared asset and links the selection (returns
  `{ id, name }`); `applyMaterial(nameOrId)` links the selection to an
  existing asset; `updateMaterial(nameOrId, { name?, layers? })` edits the
  asset — every linked object updates; `deleteMaterial(nameOrId)` removes
  it (linked objects keep their look). Material assets ARE readable: the
  `<editor-context>`/`get_scene` snapshot lists them under `materials`
  (id, name, layer types, usage — same overview as `listMaterials()`), and
  `getMaterial(nameOrId)` reads ONE full definition — `{ id, name, layers:
  [{ id, type, …props }], usedBy }`, colors as hex, entries valid to pass
  back as `layers` patches. Both reads echo their data in the run_code
  result. Before minting a new asset, check the snapshot's `materials` —
  if a suitable one exists, `applyMaterial` it (or `getMaterial` + tweak)
  instead of rebuilding it. Per-object `layer()`/`color()` edits DETACH
  that object from the asset first — shared restyles go through
  `updateMaterial`; per-object edits are for making one object DIFFERENT.
  Do NOT confuse `createMaterial('Name')` (this DSL call — saves a Spline
  LAYERED material as a shared asset) with the HTML-content bridge's
  `spline.createCustomMaterial(factory)` (a custom three.js/TSL SHADER
  material for runtime-created objects — html-content skill). Different
  systems: layered assets are editable in the editor and render everywhere;
  custom shader materials are code-only and runtime-only.
- `background('#hex')` — page background color.

## Geometry
- `geometry(changes)` / `ge(changes)` — edit the selected mesh's geometry
  params, e.g. `geometry({ width: 300 })`, `geometry({ text: 'Hello' })`. Text
  content is capped at 50 characters (longer strings are truncated).
- Params you'll reach for most (details + per-shape list in the `building-scenes`
  skill):
  - `cornerRadius` (+ `cornerSegments`) — round the edges of a `Cube`, `Cylinder`,
    `Pyramid`, `Torus`, `Rectangle`, `Polygon`, `Star`, `Triangle` (`Cone` uses
    `cornerRadiusTop`/`cornerRadiusBottom`). A rounded `Cube` reads as soft/plush —
    a deliberately cute/stylized cue. NOTE: `Cube`/`Cylinder`/`Cone` SPAWN softly
    rounded (cornerRadius 8 by default), so for crisp believable hard surfaces
    (architecture, furniture, machines) pass `cornerRadius: 0` explicitly.
  - Segment counts — smoothness/faceting: `widthSegments`/`heightSegments`
    (`Sphere`, `Plane`), `radialSegments` (`Cylinder`/`Cone`/`Pyramid` — also sets
    a `Pyramid`'s base sides), `radialSegments`/`tubularSegments` (`Torus`),
    `detail` (`Dodecahedron`/`Icosahedron`). Low counts = deliberately low-poly.
  - `Cylinder`/`Cone`: THICKNESS is the `radius` (= half the `width`). The
    default `width` is 100, so an unsized cylinder is a chunky 100-wide slug —
    for a slim pole/peg/trunk you MUST set `radius` (or `width`), e.g.
    `mesh('Cylinder', { radius: 8, height: 400 })`. A Cylinder's `hollow`
    is a FRACTION 0..1 (`hollow: 0.4` = 40% opening — tires, pipes, rings);
    never write percent numbers like `hollow: 40`. `radiusTop`/`radiusBottom`
    set only the TAPER: they're ratios relative to `width`, not absolute radii
    (equal values just give a straight cylinder at `width` — they do NOT make it
    thinner), so use them to taper to a point or a frustum. Plus `openEnded`,
    `hollow` (0-1 wall thinness, not a boolean — Cylinder → a tube/pipe).
  - `Ellipse`: `innerRadius` (0-100, a PERCENT of the outer radius → a
    ring/donut). `Polygon`: `spikes` = number of sides (`6` = hexagon).
    `Star`: `spikes` = points, `innerRadiusPercent`.
  - `depth` + `extrudeBevelSize` on any flat shape — extrude a 2D outline to 3D.
  - `Lathe`: its `points` profile has a strict contract — load the `lathe`
    skill for it (and the recipes) BEFORE building or editing one.
- Mesh geometry IS readable: `getGeometry(target?, options?)` — a READ alias —
  returns any mesh's LIVE geometry as customMesh-shaped data: `{ id, name,
  geometry, space, vertexCount, triangleCount, indexed, bounds: { min, max,
  size }, vertices, indices?, normals?, uvs? }` (flat arrays). Works on every
  mesh kind: parametric primitives (their real tessellation), customMesh /
  procedural results, Text glyphs, Boolean results, generated models. `target`
  is an id, a name, or a select()/mesh() handle; omitted = the single selected
  mesh. Default `space: 'local'` is the mesh's own frame — the numbers
  `customMesh` would rebuild it from (the object's transform still applies on
  top); `space: 'world'` runs vertices (and normals) through the world matrix —
  e.g. sample a terrain's surface heights to sit props on it exactly. The full
  arrays are usable IN-SCRIPT — read → modify → re-emit via `customMesh` is
  the vertex-edit path — while the echo in the run_code result bounds long
  arrays to a leading preview + "+N more" marker; to SEE a specific region,
  pull a bounded window with `start`/`count` (vertex indices; windowed reads
  omit `indices`) and `channels: ['vertices']` etc., one window per read;
  `count: 0` returns just the counts + bounds, no arrays. To see a WHOLE-mesh
  derived view (a width profile per height, extents per part), compute it
  in-script from the full arrays and `report()` it — pass `count: 0` to those
  reads so the raw arrays don't also flood the result.
  Meshes created by THIS run_code call aren't built yet — read them in the
  next call. `get_objects` reports each mesh's vertex/triangle counts, so
  gauge the size before pulling a dense mesh's arrays.

## Lights
- `light(type, props?)` / `addLight(...)` — create a light. type: 'Point',
  'Spot', 'Directional' (the 'Light' suffix is appended for you). props:
  `intensity`, `color`, `distance`, `decay`, `angle`, `size` (Directional
  only — the square world-unit footprint its shadows cover; see LIGHT
  SIZE), plus shadow control:
  `shadows` (on/off), `shadowRadius` (softness — raise for softer edges),
  `shadowResolution` (shadow map size — new lights default to 512, the Low
  tier, the right performance call; leave it there and raise it (1024/2048)
  only when the user explicitly asks for crisper shadows).
- `updateLight(props)` — update the selected light.
- LIGHT SIZE (Directional): shadows exist only inside the light's `size`
  footprint (default 2000 world units, centered on the light) — outside it
  objects cast nothing and the shadow field cuts off mid-scene. LARGE
  scenes — buildings, cities, castles, mountains, race tracks, courts,
  anything spanning thousands of units — need `size: 4000` or more to
  cover the whole area; match it to the scene's footprint, and
  `updateLight({ size: 6000 })` the key when a build outgrows it. A bigger
  footprint spreads the same shadow map thinner, so soften the result with
  `shadowRadius` rather than raising `shadowResolution`.
- LIGHT BUDGET: before adding ANY light, check the scene for existing ones —
  the `<editor-context>` snapshot / `get_scene` list them by type
  (DirectionalLight / PointLight / SpotLight), and a fresh scene usually
  already ships with one Directional Light. If a suitable light exists, REUSE
  it: `select(o => o.isLight)` then `updateLight(...)` / `position(...)`
  instead of stacking a new one on top. DAYLIGHT scenes: one directional key
  (over the always-on ambient fill) is enough for most, a second light only
  as a deliberate fill, and 3 lights the ceiling — piling on lights
  overexposes the scene, muddies shadows, and costs render time.
  NIGHT/INTERIOR scenes may run more: shadowless Points/Spots are cheap, so
  a handful of local pools is fine when each has a visible job (a lamp, a
  sign, a doorway) — but keep SHADOWS on at most 1–2 of them. Emissive
  materials make a surface glow but do NOT light its surroundings — pair
  each glowing prop (neon, screen, lamp shade) with a small low-`distance`
  Point/Spot whenever its light should touch nearby surfaces.
- EXPOSURE — match the scene's register and judge it in the live capture:
  DAYLIGHT (ambient fill at its default ~0.75): a key around 0.8–1.0, fills
  0.3–0.4. If the shot still reads flat or dim after repositioning the key,
  raising the key up to 2 is fine — past that, raise the ambient or fix the
  palette instead. Blown-out whites / washed-out colors mean back off.
  NIGHT / INTERIOR / MOODY (ambient dimmed or recolored): local lights ARE
  the exposure — Points and Spots commonly need `intensity` 2–8, shaped
  with `distance` + `decay` into tight pools against dark surroundings.
  There is no fixed cap in this register: raise until the subject reads in
  the live screenshot and stop before highlights clip. Under-lit is THE
  classic night-scene failure — "moody" never means "invisible".
- SPOTLIGHTS are underused and often the right tool: a directed cone with
  `angle` (spread) and `penumbra` (0 = hard rim, 1 = fully feathered;
  0.3–0.6 reads theatrical-soft). Reach for one whenever light should have
  DIRECTION — desk/street lamps, stage and product spots, car headlights, a
  shaft through a window, picking the hero out of a dark scene. Place and
  aim it like a camera — `position(...)` + `rotation(aimEuler(yaw,
  pitch))` — with `distance` bounding the throw.
- The page also has an always-on ambient sky/ground fill — tune it with
  `environment({ ambient: { color, intensity } })` below, don't try to build
  one from point lights.

## Environment & atmosphere (page-wide)
- `fog(props | 'none')` — distance fog: objects fade toward the fog color
  between `near` and `far` (world units). `fog({ useBackgroundColor: true,
  near: 800, far: 4000 })` is the classic atmospheric-depth move — distant
  content melts into the sky. THE cheapest way to add depth/mood to a scene.
  `mode: 'height'` swaps in realistic ground fog (a layer that thins with
  altitude — reads clear from above, dense at ground level): `fog({ mode:
  'height', useBackgroundColor: true, density: 0.005, heightFalloff: 0.01 })`;
  `heightBase` sets the layer's floor (world Y). near/far only apply to the
  linear component; `mode: 'both'` stacks a near/far distance haze ON TOP
  of the height layer (one fog color). density/heightFalloff are
  per-world-unit physical values; the editor UI shows their reciprocals in
  world units (Distance = 1/density — sight range at the base; Thickness =
  1/heightFalloff — the layer's height), so "fog distance ~400 units" means
  density: 0.0025.
- `sky(props | 'none')` — a REAL atmospheric sky rendered behind the scene in
  place of the flat background color: physically-based atmosphere + volumetric
  clouds. `sky({ timeOfDay: 18, weather: 'storm' })`. `timeOfDay` is hours
  0-24 and drives the sun (~6 sunrise, 12 noon, ~18 sunset — golden-hour and
  night looks come from here); `weather`: 'clear' | 'mostlyClear' |
  'partlyCloudy' | 'mostlyCloudy' | 'overcast' | 'storm'; plus `clouds`
  (on/off), `wind` (m/s) + `animateWind` (clouds drift), `exposure`, `seed`.
  By default the sky also DRIVES the scene lighting (a sun light + sky dome
  replace the page's ambient fill — dawn/dusk scenes light themselves); tune
  with `lightingIntensity` or opt out with `lighting: false`.
  `sky({ hdri: { image?, rotation? } })` switches to an equirectangular
  environment image instead — `image` takes an existing image asset id (e.g.
  from `generate_image`), a built-in env preset name ('Blue photo studio',
  'Qwantani dusk', 'Sunset fairway', 'Forest', 'Neon city', 'Studio dark',
  … — loose spellings match, unknown names error listing all presets), or an
  image URL; `rotation` in degrees; with no image a studio preset is
  applied. `hdri: { showBackground: false }` keeps the environment's lighting
  and reflections but hides the image — the flat background color shows. `sky('none')` turns the sky off (the flat background returns). Use it for any OUTDOOR scene that wants a believable sky, sun
  position, or weather mood; the flat `background()` color stays the right
  call for studio/abstract looks. (Renders on the WebGPU backend; the WebGL
  fallback keeps the flat background color.)
- `environment({ fog?, sky?, ambient?, ao?, softShadow? })` — one call for the
  page environment: `ambient` ({ color, intensity } — hemisphere-style fill, or
  false to disable), `ao` (ambient occlusion — contact/crevice darkening that
  grounds objects; `true` or { radius, bias }), `softShadow` ('normal' — stock
  shadow filtering, the DEFAULT and the right performance call — or 'low' |
  'medium' | 'high' to switch to PCSS soft shadows at that quality; soft
  shadows cost render performance every frame, so pick them only when the
  user explicitly asks for soft/contact-softening shadows), `sky` (same
  argument as `sky(...)`).
- `shadows(props)` — per-mesh shadow flags on the selection (the Visibility
  panel's Shadows dropdown): `shadows(false)` (none), `shadows(true)`
  (cast & receive), `shadows({ cast: true, receive: false })` (cast only).

## Camera & view
These aliases move the USER's viewport camera — use them to set the view the
user should end up with (the final presentation angle), or when the user asks
to change the view. For framing your own verification screenshots pass the
same aiming fields to the `take_screenshot` TOOL (or pre-aim with the
`set_view` TOOL) — they drive your private screenshot camera without
moving the user. (When one of these aliases does move the viewport, your
screenshot camera follows it, so a screenshot right after `lookFrom`/`focus`
still shows the framing you just set.) The private camera is for WORKING
shots; the user's final view is verified with
`take_screenshot({ view: 'live' })` — see FINAL CAPTURE in the quality bar.
- `lookFrom(spec)` — aim the viewport camera at a vantage and look at the
  target. `spec` is a preset — 'front' | 'back' | 'left' | 'right' | 'top' |
  'bottom' | 'iso' | 'threeQuarter' (hero 3/4) — OR `{ azimuth?, elevation?,
  distance?, target? }` in DEGREES. azimuth: 0=front, 90=right, -90=left,
  180=back (front is toward the viewer). elevation: 0=eye level, positive=above
  looking down, 90=straight top-down. DISTANCE FITS BY DEFAULT: leave it out
  and it is computed from real bounds — the selection's when
  `target: 'selection'`, the scene's content cluster otherwise (a bare
  `lookFrom('threeQuarter')` also aims at that cluster) — so the framing is
  correct by construction. NEVER hand-pick a distance number for a final
  shot; the two hero-shot forms are `lookFrom('threeQuarter')` for the whole
  scene and `select(<hero>)` then `lookFrom({ azimuth: -35, elevation: 25,
  target: 'selection' })` for one subject. `target` is [x,y,z] or
  'selection'. Do NOT chain `focus()` after `lookFrom()` in the same
  run_code call — it would undo the angle; `lookFrom` already frames in one
  call. And a `lookFrom` is only FINAL if nothing changes after it: any
  scene edit that follows it re-runs the framing + live check. INTERIOR
  briefs use the selection form on the focal FURNITURE (never the room
  shell): the fit sizes to the furniture cluster, which lands the camera
  inside the room — see INTERIORS ARE SHOT FROM INSIDE in the quality bar.
- `focus(target?)` / `centerView(target?)` / `zoom(target?)` — re-frame the
  selection or a target at the CURRENT angle (does not rotate the camera).
- `viewport(mode)` — PROJECTION only: 'perspective' | 'orthographic' |
  'isometric' | 'reset'. Set the ANGLE with `lookFrom`, not here.
- `camera(props?)` — switch camera projection (alias of `viewport`).
- A run that starts on the DEFAULT camera in orthographic mode has it switched
  to perspective automatically (results read better with depth) — no need to
  call `viewport('perspective')` yourself, and don't switch back to
  orthographic unless asked. A custom camera the user activated is never
  auto-switched: if it is orthographic, that is their deliberate choice.
- `activateCamera(cameraRef?)` / `useCamera(...)` — make a scene camera the
  active EDITOR VIEWPORT view (your screenshot camera follows it). This does not
  choose the camera used by Play/export.
- `setPlayCamera(cameraRef?)` — choose the page's Play/export camera. It accepts
  the same selected object/object/id/name/`'personal'` references as
  `activateCamera`. Referencing a camera by object/id works in the same call as
  its `add`; by NAME needs a later call (same staleness rule as `select`).
- `playControls(mode)` — the file's PLAY-MODE camera controls (the Publish
  orbit settings, honored in play mode and exports): what the user's
  pointer/wheel does to the play camera. `'none'` disables rotate/pan/zoom/
  auto-rotate entirely, `'orbit'` restores the defaults, or pass
  `{ rotate?, pan?, zoom?, autoRotate? }` to toggle individually. Code that
  drives the play camera per frame (HTML-layer games — `games` skill) MUST
  call `playControls('none')`: while any control is on, play mode attaches
  orbit controls to the play camera and they re-aim it against the code.

## Selection
- `select(filter | target | 'Name' | 'all' | count?, mode?)` —
  `select(o => o.isMesh)`, `select('Cube')` (by name, case-insensitive, or id),
  `select('all')`, `select(o => o.shape('sphere'))`, `select(o => o.color('#f00'))`.
  Pass `'add'` as last arg to add to the current selection.
- `unselect(filter?)` — clear or narrow the selection.
- A filter/name selection resolves against the LIVE scene at the point it
  runs, so it matches objects created earlier in the SAME run_code call —
  `add('cube'); select(o => o.name.indexOf('Cube') === 0);` sees it. No need
  to split creation and selection into separate calls.
- A selected object exposes: `id`, `name`, `type`, `position`, `rotation`,
  `scale`, `visible`, `isMesh`/`isLight`/`isCamera`/`hasCloner`, `shape(name)`,
  `color(hex)`, `width`/`height`/`depth`, `geometry` (a mesh's full geometry
  params, including its `type`), `material`, `shading`, and `layer(type)` —
  the top material layer of that type (its props plus its `id` for
  `updateLayer`/`removeLayer`). `id` is the bridge from `get_scene`/`get_objects`
  (which return ids) back to a selection: `select(o => o.id === '<id>')`.

## Structure
- `group(target?)` — group into a new Empty; RETURNS the group, so
  `const g = group(...)` can be passed to `moveInto`/`select` in the same call.
  For a multi-part assembly, build the parts UNROTATED, group, then rotate the
  GROUP once — don't pose parts individually (see Critical conventions).
  Do NOT include cameras in a group unless explicitly asked (a camera in a
  rotating/animated group moves with it and its view goes static) — group only
  the content, e.g. `select(o => !o.isCamera)` before `group()`. The PLAY
  camera especially must stay at the page root: grouped play cameras come up
  mis-aimed in play mode (`games` skill).
- `ungroup(target?)` — dissolve the selected group(s): children move up to the
  group's parent (keeping their world position) and the empty wrapper is
  deleted. Affects Empties (groups) and Boolean objects (frees the operands).
- `boolean(operation, target?)` — combine the targeted (or selected) meshes
  into ONE live CSG object: 'union' | 'subtract' | 'intersect'; shorthand
  verbs `subtract(target?)` / `union(target?)` / `intersect(target?)`.
  `subtract` CUTS HOLES: the BOTTOM object in the scene tree is the base
  that survives (among meshes created in one call that's the one made FIRST —
  new objects insert on top), everything above it is carved out. TWO-CALL
  RULE (stricter than select's): the operands must already exist BEFORE the
  run_code call that combines them — create the solid and the overlapping
  cutter(s) in one call, then `subtract(['Solid', 'Cutter'])` by name/id in
  the NEXT call. Operands must be closed solids (give flat shapes a
  `depth`) and stay editable as the Boolean's children; the result takes
  the Boolean's own material. Returns the Boolean (like `group`); with a
  single existing Boolean targeted it changes that Boolean's operation
  instead. ALWAYS `load_skill` the `boolean-operations` skill before ANY
  boolean work, even a single cut.
- `shapeBlend(target?)` — melt the targeted (or selected) meshes into ONE
  smooth organic surface (metaball/SDF blending) — goo, blobs, merging
  liquid, lava lamps, soft cartoon bodies. The members become the new Shape
  Blend's CHILDREN and stay editable: move/scale/animate a member and the
  surface re-melts around it. Same target forms and TWO-CALL RULE as
  `boolean` (members must exist before the combining call); returns the
  blend (like `group`). `shapeBlend(props)` edits the SELECTED blend
  container ({ blendRange, resolutionLevel, useChildrenColors }) or member
  shape ({ operation: 'union' | 'subtract' | 'intersect', blendRange,
  useColor }); add/remove members with `moveInto` (`ungroup` does NOT
  dissolve a blend). Hard-edged cuts and merges are `boolean`'s job — a
  blend always rounds. ALWAYS `load_skill` the `shape-blends` skill before
  building one.
- `merge(target?)` — collapse the targeted (or selected) meshes into ONE
  editable mesh (bakes their world-space geometry together). DESTRUCTIVE:
  the extra meshes are deleted (their states/events/animations die) and the
  result renders with a single material (the LAST target's) — merge only
  static same-material dressing. Same TWO-CALL RULE as `boolean`. THE tool
  for "too many objects" performance fixes; load the `scene-optimization`
  skill before using it.
- `bakeBoolean(target?)` — apply a live Boolean's CSG result in place (the
  inspector's "Apply & Edit"): the Boolean becomes a plain editable mesh, its
  operand children are deleted, and the CSG stops recomputing. DESTRUCTIVE
  (the cut can no longer be edited/animated); the go-to fix for nested or
  numerous Booleans flagged by the performance analyzer. Same TWO-CALL RULE
  as `boolean`; load the `scene-optimization` skill first.
- `decimate(target, ratio)` — reduce a mesh's VERTEX COUNT while keeping
  its shape, uvs, textures and materials (quadric-error edge collapse;
  surviving vertices keep their original uvs/normals/colors, and uv seams,
  hard edges and material borders are pinned). The TARGET LEADS and is
  required (this edit is destructive, so it never inherits the selection —
  pass `get('selection')` to drive it from there, or `'all'` for every
  mesh); `ratio` is the fraction to KEEP, so `decimate('Statue', 0.5)`
  halves it. THE polygon fix for meshes with
  no segment dials — imported and AI-generated models, baked booleans, merged
  dressing, sculpted subdivs; on a parametric primitive lower its segments
  with `geometry(...)` instead, which stays editable. DESTRUCTIVE (the mesh
  becomes a plain non-parametric mesh). Live Booleans must be baked first and
  Shape Blends take `resolutionLevel`. A READ alias — the result carries the
  per-mesh before/after counts, so report the reduction from those. It stops
  short of the target rather than wreck the shape (`reachedTarget: false` +
  `stoppedBecause`: pinned seams/hard edges, or the deviation budget) —
  that's the mesh's floor, not a call to retry. Same TWO-CALL RULE as
  `boolean`; load the `scene-optimization` skill first.
- `moveInto(parent, target?, { before?, after? })` — reparent target (or the
  selection) into `parent`: an object from select/group, an id, a NAME, or
  'root' for the page root. World positions are preserved — objects don't
  jump. `before`/`after` (a sibling ref) set the position among the new
  siblings; reorder = moveInto the current parent with `before`/`after`.
  Parent NAMES resolve when the commands run, so a group created earlier in
  the SAME call is a valid parent.
- `hide(target?)` / `show(target?)` — scene-tree visibility (the eye toggle).
  Find hidden objects with `select(o => !o.visible)`.
- `duplicate(target?)`, `clone(props)`, `cloneTo(target, props)`,
  `remove(target?)` — the selection, `'all'` (clears scene), a name/id
  string, or an object/array from select/add — `rename('Name')`,
  `arrange(margins?, target?)`. `clone` makes the selection a CLONER —
  `type`: 'linear'|'radial'|'grid', each with a same-named sub-object of
  settings (per-step `linear` position/rotation/scale = stacks, spirals,
  twists; `radial` radius/arc/alignment = rings; `grid` count/size). Cloners
  can RANDOMIZE per instance (`randomness: true` + `randomnessObject`) and
  `cloneTo` scatters clones across another object's surface. On an object
  that is ALREADY a cloner, `clone` merges — partial props edit it in place
  (`get_objects` returns the current settings). See the building-scenes
  skill for the recipes that make dense, varied dressing cheap.
- `component(target?)` — turn the selection (or `target`) into a reusable
  component (the master copy).
- `instance(target?)` — add a linked instance of the selection: makes it a
  component first if it isn't one, then adds a copy that stays in sync — edits
  to the component propagate to every instance.
- `detachInstance()` — break the selected instance's link to its component so
  it becomes an independent, standalone object.
- `path(points?)` — create a path curve: a closed, rounded loop through the
  given `[x,y,z]` points (defaults to a rectangle-ish loop if omitted). RETURNS
  the path object, so `const p = path(...)` can be handed straight to `align`.
- `align(path, { animate?, duration? })` — snap the selection onto a path so it
  follows the curve. Pass the object `path()` returned, or a path's name/id;
  `animate: true` slides the object along the path on Start (`duration` in ms).

- `layout({ constraints: [...], fixed?, region?, seed? })` — constraint
  solver for PRECISE placement of existing objects: `near` / `apart` /
  `on` / `against` / `facing` / `align` / `inside` / `spread`, with
  automatic overlap avoidance. Use it instead of hand-computing coordinates
  whenever objects must relate ("chairs around the table", "lamp on the
  desk", "sofa against the wall"); anchor immovable objects with `fixed`.
  Load the `procedural-generation` skill for the constraint reference.

## Animation / interactivity — the OPT-IN states machinery (see skills)
MOTION IS CODE-DRIVEN BY DEFAULT (see # Motion & interactivity): motion and
behavior live as JavaScript in the HTML layer, driving objects through the
`spline` bridge — load the `animation` skill. The aliases below are the
BUILT-IN states/events machinery — reach for them ONLY on an explicit user
ask (states, transitions, timeline, variables, the States panel), for
physics-coupled kinematic motion or scroll-driven sequences, or to edit
interactivity a scene already has.
- `animate(stateProps, transitionProps?)` — all-in-one: new state + event +
  transition. `stateProps`: position/rotation/scale/color/width/height/depth/
  geometry/material. `transitionProps`: duration(ms), delay(ms), easing
  ('linear'|'ease'|'ease-in'|'ease-out'|'ease-in-out'|'cubic'|'spring'),
  loop:true, direction:'alternate', trigger (event name).
- Create: `addState(name?)`, `addEvent(type)` → eventId,
  `addAction(eventId, actionType, container?)` → `{actionId, tweenId}`,
  `addTween(eventId, actionId, props?)` → tweenId. To add beneath a Conditional
  action use `addAction(eventId, actionType, { parentActionId, branch: 'if' })`
  (or `branch: 'else'`). Nested Conditional creation is unsupported.
- Edit: `updateEvent(eventId, props)` (e.g. `{ key: 'Space' }`,
  `{ enabled: false }`), `updateAction(eventId, actionId, props)` (e.g. a
  Link's `{ url }`, a SetVariable's `{ variableId, expression: 'clicks + 1' }`
  — the new value, variables by name; a Conditional's `{ condition:
  'score >= 3' }`; full syntax in the interactivity skill),
  `updateTween(eventId, actionId, tweenId, { duration, delay, easing:
  'spring', loop: true, direction: 'alternate' })`, `selectState(name)` then
  transform/color calls to restyle an existing state (`selectState(null)` =
  Base State), `renameState(state, name)`.
- Delete: `removeEvent(eventId)`, `removeAction(eventId, actionId)`,
  `removeTween(eventId, actionId, tweenId)`, `removeState(nameOrId)`.
- Variables: `setVariable(name, value)` — create-or-update a basic scene
  variable (number/string/boolean); returns its id.
  `dynamicVariable(name, type, props?)` — create-or-update a self-updating
  variable, type 'counter'|'random'|'time'|'timer'|'stopwatch'.
  `renameVariable(nameOrId, newName)`, `removeVariable(nameOrId)`.
- Bindings: `bindVariable(property, variable)` drives a property of the
  SELECTED object(s) with a variable's live value — 'position.x/y/z',
  'rotation.x/y/z', 'scale.x/y/z', 'text' (Text objects show the value —
  scores, timers), or ANY numeric parametric-geometry parameter by its
  schema name: 'width'/'height'/'depth', 'cornerRadius', 'cornerSides',
  'radius', 'sides', 'segments', 'innerRadius', 'tube', 'arc', … (the
  geometry rebuilds live as the variable changes; Vector/Path geometries
  excluded — their shape is point-derived). Numeric properties need a
  number-valued variable. `unbindVariable(property)` freezes the current
  value back. Details + recipes in the interactivity skill.
- To EDIT existing interactivity, call `get_objects([objectId])` FIRST to get
  real event/action/tween/state ids, `select(...)` the object, then update by
  id.
- Event names: 'Start','MouseDown','MouseUp','MousePress','MouseHover',
  'KeyDown','KeyUp','KeyPress','Scroll','Collision','Trigger','DragDrop', etc.
- Action types: 'Transition','Animation','Link','SwitchCamera','SceneTransition',
  'Create','Destroy','Reset','SetVariable','Audio','Video','Particles', etc.
  Not every action is valid on every event — invalid combos throw an error
  listing what IS allowed.
- Containers: most events keep actions in one list; on 'Conditional' events
  pass `'in'`/`'out'` as `addAction`'s 3rd arg, on 'DragDrop' `'drag'`/`'drop'`,
  on 'API' `'success'`/`'error'`.
  Conditional ACTION branches are different:
  `const gate = addAction(e, 'Conditional'); updateAction(e, gate.actionId,
  { condition: 'score >= 3' });
  const win = addAction(e, 'Transition', { parentActionId: gate.actionId,
  branch: 'if' });` The if branch runs when true and else when false. Nested
  child actions are edited/deleted by id automatically.

## Aesthetic / utility helpers
- `prettify()` — auto-harmonize all material colors.
- `style(['#a','#b',...], seed?)` — recolor everything + background from a palette.
- `studio()` / `stage('studio')` — instant neutral studio lighting + ground.
- `physics(props)` — enable physics on the SELECTED object(s) (also switches
  physics on for the page). `type`: 'dynamic' (falls under gravity and collides)
  or 'positioned' (an immovable collider — floors, walls, obstacles). Plus
  `bounce` (0..1 bounciness), `friction` (0..1), `gravityScale` (1 = normal,
  0 = floats), `damping`, `density`. Pair with a `Collision` event to react.
  For the full simulation reference (colliders, group bodies, axis locks,
  moving platforms, spawning dynamic objects), load the `physics` skill.
  For a GAME or game-like scene, ALWAYS load the `games` skill first —
  games are code-driven by default (a JS game loop + HTML UI via
  `set_html_content`, started by the user from a start screen), NOT built
  on physics/GameControl; the built-in Game Controls feature is opt-in
  (`game-controls` skill) for when the user explicitly asks for it.
- `fx(type, props?)` — page post-processing. type: 'bloom' |
  'chromaticAberration' | 'vignette' | 'hueSaturation' | 'brightnessContrast' |
  'depthOfField' | 'noise' | 'pixelation'. `fx('bloom', { intensity: 1.2 })`
  enables + tunes; `fx('bloom', 'none')` turns that one off; `fx('none')` clears
  all. Per-effect props in the materials-and-look skill. POST EFFECTS ARE
  OPT-IN: enable one ONLY when the user asks for it — by name or by a look
  that names it ("glowing neon" implies bloom, "film grain" implies noise).
  The single exception is `depthOfField`, which you may add unprompted when
  it genuinely serves the shot (a close-up hero against a distant
  background) — skip it otherwise. Never finish a scene with a habitual
  bloom/vignette pass: atmosphere comes from fog, lighting, and AO, not
  from post effects.
- `play()` — enter Play (to test interactions; not undoable): boots the live
  preview of the document in the published runtime — events, physics, scene
  scripts, and runtime-spawned objects all run for real. While it runs,
  take_screenshot captures that LIVE view through the play camera (set_view
  does not apply to it).
- `stop()` — leave Play and return to editing (the inverse of `play()`;
  not undoable). Call it once you're done testing so the user isn't left in
  play mode.
- `iterate(o => { ... })` — run a callback once per currently selected object,
  with that object selected during the callback — THE way to apply alias calls
  to each object of an existing selection (a plain loop can't re-select them).
  For creating N new objects, a normal bounded `for` loop is the right tool.

## Worked examples

Create a red sphere on a floor with a key light:
```
mesh('Sphere', { width: 200, height: 200, depth: 200 });
color('#e0552b');
position({ y: 100 }); // sit it on the floor; x/z stay at the build center
rename('Hero');
mesh('Plane', { width: 3000, height: 3000 });
rotation({ x: -90 });
position({ y: 0 }); // ground it; x/z stay at the build center
color('#f2f0eb');
rename('Floor');
light('Directional', { intensity: 0.9 });
translate({ x: 400, y: 600, z: 500 }); // offset the key light from the build center
background('#dfe3e8');
```
…then frame it in a SECOND run_code call (select can't see objects created in
the same call):
```
select('all');
focus();
```

Set a hero camera angle — a low three-quarter view from the left. Pick the
vantage with `lookFrom` (in its own call, after the objects exist):
```
lookFrom({ azimuth: -40, elevation: 15 });
```
Presets cover the common shots: `lookFrom('threeQuarter')` for a 3/4 hero,
`lookFrom('top')` for a flat-lay, `lookFrom('front')` for a straight-on shot.
Pass an explicit `distance` to pull back for a wider establishing shot.

The user EXPLICITLY asked for a States-panel animation — pulse forever as a
state + looping transition (for every other motion ask the DEFAULT is the
code path — # Motion & interactivity):
```
animate({ scale: { x: 1.3, y: 1.3, z: 1.3 } },
        { duration: 900, easing: 'ease-in-out', loop: true, direction: 'alternate' });
```

Same explicit states ask, interactive — on click, spin 180deg with a spring:
```
animate({ rotation: { y: 180 } },
        { trigger: 'MouseDown', easing: 'spring', stiffness: 120, damping: 12 });
```

Recolor every mesh in the scene from a palette:
```
style(['#1b1f3b', '#e94f37', '#f6f7eb', '#44bba4']);
```

Procedural custom geometry — compute the vertices/faces, then build the mesh.
A faceted low-poly cone (use `customMesh` for shapes the primitives can't make):
```
const verts = [];
const idx = [];
for (let i = 0; i < 16; i++) {
  const a = (i / 16) * Math.PI * 2;
  verts.push(Math.cos(a) * 50, 0, Math.sin(a) * 50);
}
verts.push(0, 120, 0);
// Wind triangles counter-clockwise seen from OUTSIDE so auto-computed normals
// face outward (here: base vertex, apex, next base vertex — NOT base,next,apex):
for (let i = 0; i < 16; i++) { idx.push(i, 16, (i + 1) % 16); }
customMesh({ vertices: verts, indices: idx });
color('#8a5a2b');
```

Dress a scene with varied trees + atmosphere. A bounded loop of alias calls is
the normal way to scatter N objects — vary size/placement/rotation per
iteration so nothing repeats:
```
for (let i = 0; i < 8; i++) {
  const s = 0.6 + rand() * 0.8;
  mesh('Cone', { radius: 40 * s, height: 160 * s, radialSegments: 7 });
  color('#2e7d4f');
  position({ y: 80 * s });
  translate({ x: (rand() - 0.5) * 900, z: (rand() - 0.5) * 900 });
  rotation({ y: rand() * 360 });
}
fog({ useBackgroundColor: true, near: 900, far: 4500 });
environment({ ao: true, ambient: { color: '#bcd4ff', intensity: 0.7 } });
```
