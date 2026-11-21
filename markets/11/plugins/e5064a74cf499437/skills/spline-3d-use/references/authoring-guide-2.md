**Part 2 of 3 of the Spline 3D authoring contract** — continues `load_skill("authoring-guide")` (load Part 1 first if you haven't). This part has the critical conventions, the topic-skill catalog, and the first half of the DSL quick reference (Create, Transform, Color & material, Geometry, Lights).

# Critical conventions (follow exactly)

- Rotations are in DEGREES (e.g. `rotation({ x: -90 })` lays a plane flat).
- COMPOUND OBJECTS — build STRAIGHT, group, THEN rotate. Anything assembled
  from 2+ primitives (a mushroom, a rocket, a lamp, a tree) must be built with
  every part UNROTATED and axis-aligned: position the parts relative to each
  other in that upright frame, `group()` them, and apply the tilt/orientation
  ONCE to the GROUP. Rotating parts one by one to pose the assembly compounds
  small errors and the parts drift out of alignment. Per-part rotation is only
  for a part's own LOCAL shape (e.g. `rotation({ x: -90 })` to lay a flat
  shape down, or `rotation({ z: 90 })` to turn a cylinder into a horizontal
  axle) — never for the assembly's overall pose. Remember the selection rule:
  create the parts in one `run_code` call, then select + group + rotate in the
  NEXT call.
- PYRAMID ROOFS / square tops: a `Pyramid` (`radialSegments: 4`) is ALREADY
  axis-aligned — its four faces line up with a `Cube`'s walls, so a roof takes
  the SAME Y rotation as the walls (0 on an unposed house). Do NOT add a
  habitual +45° Y "correction": Spline's `Pyramid` is not a raw cone and needs
  none, and that extra 45° is exactly what leaves the roof twisted off the
  house. For a square roof use `Pyramid`, never a 4-sided `Cone` (a Cone's base
  IS diagonal).
- FLOORS: any floor/ground/table-top made from a `Plane` or `Rectangle` MUST be
  rotated flat with `rotation({ x: -90 })` — unrotated it stands upright like a
  backdrop wall behind your objects. When you verify with `get_scene`, a
  correct floor reads rotation [-90, 0, 0]. ALSO ground it with
  `position({ y: 0 })`: a freshly created object lands at the current build
  center (the camera look-at, or the editor-picked anchor), not the origin, so an
  ungrounded floor floats at some arbitrary height while objects you place with an
  absolute `position({ y: ... })` do not — the two end up mismatched and objects
  appear to sink through or hover above it.
- SURFACE DETAIL — USE A DECAL: any localized image or mark that belongs ON
  another object's surface is a `Decal`, not a flat plane hovering at the
  surface and not a remodel of the target: stickers, labels, logos and racing
  numbers on products and vehicle bodywork (cars, motorbikes, helmets), paint
  and ink splashes, bullet impacts, scorch marks and cracks, graffiti/posters
  /signs on walls, dirt and wear patches, keypads and vents on appliances.
  `mesh('Decal', { width, height, depth })` makes a projector box that stamps
  the decal's own material onto every surface inside it: it wraps curved
  bodywork, needs no exact alignment (just make the box pass through the
  surface), and cannot z-fight — its skin lifts itself off the surface
  (`offset`, default 1). Aim it exactly like the flat Rectangle it replaces:
  unrotated it stamps a camera-facing surface, `rotation({ x: -90 })` a
  floor/tabletop, `{ y: 90 }` a +X-facing side, `{ y: 180 }` the far side.
  Cutout stickers (splashes, logos) need two extra steps —
  `removeLayer('color')` plus a transparent-background `generateTexture`
  image on a `layer('texture', { image })`; the `materials-and-look` skill's
  Decals section has the full recipe. A decal stamps EVERYTHING its box
  touches — size it to the detail (three bullet holes = three small decals)
  and shrink/pull it if it bleeds onto neighboring objects. The harness
  CHECKS decal placement: a "EMPTY DECAL" report in a
  run_code result means that decal's box touches no visible surface and it
  renders as NOTHING — fix its position/rotation/depth in the NEXT call;
  never respond by swapping it for a plane or custom mesh.
- AVOID Z-FIGHTING: two surfaces occupying the SAME plane flicker/dither as
  the camera moves — the depth buffer cannot order them. The classic
  offenders: a window/door/decal panel placed flush ON a wall face, an
  overlay plane resting exactly on a floor or road, two solids overlapping
  with their outer faces flush (a roof slab against a facade, overlapping
  wall segments meeting at a corner), and an object accidentally created
  TWICE in one spot. Prevent it by construction: give facade panels real
  depth (e.g. `depth: 4`) and place them PROUD so the panel's front face
  clears the wall plane — never a zero-depth rectangle AT the wall plane;
  lift floor overlays with `position({ y: 0.5 })`; flat art/markings on a
  wall or floor (posters, road paint, signage) are better as a `Decal`
  (see SURFACE DETAIL — it cannot z-fight), else push the plane out with
  `position({ z: 0.5 })`; where two solids would share a flush outer face,
  butt-joint or inset one instead of overlapping them. Objects sitting ON a
  surface rest at it, never embedded exactly in it. The harness CHECKS your
  work: whenever a `run_code` call leaves coplanar surfaces among the
  objects it created or moved, the result carries a "Z-FIGHTING RISK"
  report naming each pair and the shared plane (e.g. `z ≈ 320`). Treat every
  line of that report as a placement bug: offset, resize, or delete the
  duplicate in your NEXT call, before building further — never finish a
  request with an unresolved report.
- The newly created object is auto-selected; subsequent transform/color/material
  calls target it. To act on something else, `select(...)` it first.
- Colors are hex or CSS strings: '#e0552b', 'tomato', 'rgb(20,30,40)'.
- Vectors are partial objects passed to the alias: `{ x?, y?, z? }`. Omitted
  axes are left unchanged. `scale` MULTIPLIES the current scale.
- `position` is world units (~pixels). The default camera is near z=1000; spread
  objects by hundreds of units. Lift objects off the floor by half their height.
- A new object SPAWNS at the current build center — the camera's look-at, or a
  free anchor the editor picks when you add to a scene that already has content
  (it's given to you in `<editor-context>`) — NOT necessarily the origin. So set
  only the axes you must pin (usually `y`, to sit on a floor) and let `x`/`z`
  default to that center; use `translate` for offsets relative to it. Hard-coding
  `position({ x: 0, z: 0 })` drags new content back onto whatever sits at the
  origin and makes independent builds overlap — use absolute `x`/`z` only to place
  something relative to a KNOWN object's coordinates from the `<editor-context>`
  snapshot or `get_scene`.
- Editor changes happen ONLY through the documented alias functions (plus
  `iterate(cb)`). You MAY use ordinary local JavaScript around them:
  `const`/`let` variables, `for`/`while` loops, arrays, and `Math`/`rand()` —
  both to COMPUTE values (vertex/index arrays for `customMesh`) and to CALL
  alias functions repeatedly. A bounded `for` loop of create + transform calls
  is the NORMAL way to place N varied objects (trees, rocks, clouds): vary
  position/scale/rotation/color per iteration with `rand()` so nothing repeats
  exactly. Keep loops BOUNDED (never `while(true)`; cap the count), and do NOT
  use imports, the DOM, network/`fetch`, or `console`.
- One statement per line, each ending with `;`. You MAY capture an alias's return
  value in a `const` within the same code block (e.g. event/action ids from
  `addEvent`/`addAction`) and reuse it in later lines of that same block.
- `select(filter)`/`select('all')` and `iterate(cb)` match the scene as it was
  when the current `run_code` call STARTED — objects created earlier in the
  SAME call are invisible to them. Create objects in one `run_code` call, then
  select/arrange/animate them in the NEXT call. (Chaining transforms right
  after a creation is fine — they target the auto-selected new object.)
- CAMERAS stay OUT of groups. When you group, move, or reparent scene content —
  especially "select all then group" — do NOT include cameras in the group
  unless the user explicitly asks for it. A camera inside a group inherits the
  group's transform: if the group rotates or animates, the camera travels WITH
  it, so its view of the grouped content never changes and the motion cancels
  out. This is exactly why "add a rotating camera" must NOT be built by grouping
  the whole scene (camera included) and spinning the group — that leaves the
  view static. To orbit/rotate a camera, animate the CAMERA itself (or a camera
  rig Empty that contains ONLY the camera) while the scene content stays put.
  When grouping content, select the meshes/lights explicitly (or
  `select(o => !o.isCamera)`) so cameras are left at the root.
- ORGANIZE THE TREE: every multi-part THING becomes ONE named group — a table
  group wrapping its top and legs, a refrigerator group wrapping its body, door
  and handle. Do NOT leave an assembly's parts loose at the root. Name parts
  with a shared prefix as you create them ('Table Top', 'Table Leg 1', …), then
  in the NEXT `run_code` call `select(o => o.name.startsWith('Table'))`,
  `group()`, and `rename('Table')` (the fresh group is selected, so `rename`
  hits it; this is the same group a compound object's pose rotation goes on).
  Scatter sets get one group for the whole set ('Trees', 'Rocks'). Several
  independent things = several sibling groups, never one grab-bag group.
- Name hero objects and groups with `rename(...)` so the scene tree stays clean.
- PRESERVE what's already there. If the scene already has objects, ADD your work
  alongside them — do NOT `remove('all')`, reset, or delete anything the user
  didn't ask you to. "Build/add X" in a populated scene means place X next to the
  existing content (the editor auto-anchors a fresh build in free space — see the
  build-center rule above), NOT wipe-then-build. Clear the scene ONLY when the
  user explicitly asks to start over / replace / clear it.
- A scene must keep at least one Page. When the user DOES ask to reset,
  `remove('all')` clears every object but preserves the page — never select or
  delete a Page yourself.
- If you need to create multiple custom meshes that touch each other, try to reuse vertex position between the two if it makes sense (when they are 2 faces of one structure for an example).

# Detailed guidance (load on demand)

When a task needs depth, call `load_skill(name)` first — the body comes back
as the tool result and stays in your context.

Some of these are NOT optional. Load the skill BEFORE you write the code, not
after the first attempt disappoints:

- ALWAYS before ANY boolean/CSG operation (cutting holes, windows, tunnels;
  merging shapes) or ANY Shape Blend / metaball work — however simple it looks.
- ALWAYS before ANY motion, animation, or interactivity work (`animation` —
  motion is code-driven by default, see # Motion & interactivity). Its channel
  map decides HOW the motion is built, and that decision constrains how the
  objects must be created, so reading it afterwards means rebuilding.
- Before games (game loops, playable characters), non-trivial materials, and
  full-scene composition.

Available skills:
- dsl-reference: The FULL Spline DSL reference: per-shape geometry params, layer/texture prop tables, generateTexture rules, light/shadow/fog/sky tuning, camera fitting, cloner settings, states/events containers, and worked examples. Load BEFORE the first substantial build or restyle of a session, when a DSL call errors unexpectedly, or when you need a prop the index in the base instructions omits.
- building-scenes: Composing full scenes: units & spatial layout, grounding objects, scatter loops & cloner randomness for dense dressing, lighting & shadow tuning, fog/AO atmosphere, camera framing, color palettes, typography & the font catalog, prettify/style, arranging and grouping.
- organic-scenes: Nature & organic scenes, stylized or believable: terrain and islands (displace layer vs customMesh), trees/rocks, water, clouds, graded skies, surface scatter, atmosphere, palettes, and ambient motion. Load for prompts like "floating island", "forest", "landscape", "ocean". (Planets/space have their own 'planets' skill.)
- procedural-generation: Procedural terrain/ocean/tree/rock/globe/building generators, seeded surface scatter, the constraint-based layout() solver, and the miniworld/diorama, city-street, enclosed-terrain (canyon/cave) and creature-rig recipes. Load for prompts like "forest", "island", "landscape", "ocean", "canyon", "cave", "city", "miniworld", "mini world", "diorama", "arrange the furniture", "place these neatly", or any scene needing many natural assets or exact relative placement.
- architecture: Buildings & man-made structures in the believable register: real-world proportions, crisp edges (cornerRadius 0), pitched roofs with overhangs, framed windows/doors, wall/roof textures, muted palettes, streets & neighborhoods at real scale. Load for prompts like "house", "building", "cabin", "tower", "city", "skyline", "street", "town", "village", "neighborhood", or any named real-world place.
- planets: Planet & space scenes: realistic textured planets (AI texture layer — take the initiative), stylized procedural planets, atmosphere rims, rings, moons, space lighting and backdrop. Load for prompts like "planet", "earth", "mars", "moon", "solar system", "space scene".
- lathe: The Lathe primitive: revolving a 4-point bezier profile around Y into vases, bottles, bowls, cups, glasses, lamp bases, chess pieces, columns, domes. The points contract (x = radius, y-down, top-first), sizing behavior, segments, open rims & double-siding, profile recipes, and multi-lathe / customMesh fallbacks for complex silhouettes. Load for prompts like "vase", "bottle", "bowl", "cup", "pot", "goblet", "lathe".
- boolean-operations: Boolean (CSG) operations: carving holes, windows and tunnels with subtract(), merging shapes with union(), keeping overlaps with intersect() — operand ordering (which object survives a subtract), live editing of operands, adding cutters later, materials on the result, closed-geometry rules, and performance. Load for prompts like "make a hole", "cut out", "carve", "boolean", "subtract", "hollow out", "window in a wall", "tunnel", "merge these shapes".
- shape-blends: Shape Blends (metaballs / SDF blending): melting meshes into ONE smooth organic surface with shapeBlend() — goo, blobs, liquid drops merging, lava lamps, slime, snowmen, clouds, soft cartoon bodies. Creating from member shapes, per-shape union/subtract/intersect, blend range tuning, the resolution budget, children-color gradients, and animating members so the goo morphs. Load for prompts like 'blob', 'goo', 'gooey', 'metaball', 'melt together', 'merge smoothly', 'liquid', 'slime', 'lava lamp', 'organic blend', 'shape blend'.
- animation: DEFAULT recipe for ALL animation/motion/interactivity asks ("animate …", "make it grow/bloom/orbit/spin", hover/click behavior, ambient life): scene by run_code with stable names + a pivot at every motion origin; the motion as plain JS in the HTML layer driving objects per frame via the spline bridge — one rAF clock, poses from elapsed time f(t), easing + stagger, entrance → idle handoff, recipes, perf budget. The built-in States & Transitions feature is OPT-IN only (load state-transitions when the user explicitly asks).
- state-transitions: The built-in States & Transitions animation feature — load ONLY when the user explicitly asks for it (names states, transitions, the timeline, or the States panel), or for physics-coupled kinematic motion (moving platforms — the one motion that must be state-driven): the all-in-one animate() helper plus the low-level addState/addEvent/addAction/updateTween flow, easings, duration, delay, loop and pingpong. Code-driven motion (the default) is the `animation` skill.
- interactivity: The built-in Events & Actions machinery — for EDITING interactivity a scene already has, for features only events provide (Scroll/Collision/Trigger/DragDrop/LookAt/Follow, variables + property bindings), for sensor events bridging clicks/hovers into code, and for explicit user asks. NEW interactive behavior is code-driven by default (the `animation` skill + the spline bridge). Covers event/action types, creating and editing them (updateEvent/updateAction/updateTween/remove*), states, variables (basic + dynamic), and inspecting existing interactivity via get_objects.
- html-content: HTML content over the 3D canvas (set_html_content) — the DEFAULT home of motion and behavior code (animation loops, interaction logic, game loops; headless script-only documents are fine) as well as web UI. The full injected `spline` bridge API: direct object control (updateObject), runtime creation (createObject/spawnObject/setInstanceTransforms), imported-model animation clips (getAnimations/playAnimation/pauseAnimation/stopAnimation), custom three.js/TSL shader materials (createCustomMaterial), queries, variables/events, console — plus the transparent-background + pointer-passthrough rules and Play-mode caveats. Load BEFORE writing any HTML document.
- games: DEFAULT recipe for playable games and game-like scenes: plain JS code logic in the HTML layer (set_html_content + the spline bridge) — start-screen gate, HUD, keyboard input, a rAF game loop, a glitch-free chase camera, JS collision checks — with the scene built by run_code and sound recipes in game-audio. The built-in Game Controls feature is OPT-IN only (load game-controls when the user explicitly asks for it).
- game-example: The complete worked example for the games skill: a drive-&-collect game end to end — the run_code scene call and the full HTML game document (start gate, input, fixed-timestep loop, chase camera with exact aim math, JS collisions, HUD, restart-from-snapshots, sound hooks). Load it when building a NEW game or game-like scene; edits to an existing game usually only need the games skill itself.
- game-audio: Procedural WebAudio sound effects for games and interactive scenes (no audio assets): the shared synth helpers, AudioContext resume-on-gesture wiring, and per-effect recipes — engine hum, weapons, footsteps, pickups, win/lose stingers. Load alongside the games skill when writing the sound code.
- game-controls: The built-in Game Controls feature — load ONLY when the user explicitly asks for it (says 'game controls', wants the editor's built-in character controller, touch joysticks, or a navmesh): the GameControl event (keyAssignments key mapping, walk/fly, collider, follow camera, idle/move/jump/run action containers), pairing it with physics() so the character stands on and pushes the decor, and Collision/Trigger events for pickups, obstacles and goal zones. Code-driven games (the default) are the `games` skill.
- physics: The physics simulation itself (no character needed): page Simulation switch + gravity, physics() in depth (positioned colliders vs dynamic bodies, friction/bounce/density/gravityScale/damping, convex vs trimesh colliders, fused vs separate group bodies, axis locks), kinematic movers (animated/dragged colliders that push dynamic bodies), spawning dynamic objects with the Create action, and falling/stacking/bouncing/floating recipes.
- materials-and-look: Material layer stacks (color, shading/light category, gradient, fresnel, glass/transmission, depth, texture, displace terrain relief), decal stickers/splashes/impact marks stamped onto surfaces, flatShading/side, animated material tweens, layer/addLayer/updateLayer/removeLayer, opacity, lighting for good looks, fog/AO atmosphere, and backgrounds.
- texture-drawing: The generateTexture contract and recipes: draw seamless repeating textures locally with canvas 2D (brick/stone walls, wood planks, roof tiles, ceramic/checker floors, pavement) — the seam-wrap rules (rng-only randomness, save/restore transforms, opaque base, one draw per feature), sizing/repeat math, and worked per-material drawing recipes. Load BEFORE writing any generateTexture call.
- particles: Particle emitters: creating and tuning them with particles() (emission, motion, sprite look, emitter shapes, timing), recipes (snow, rain, fire, smoke, confetti, auras), and runtime control via the Particles action (start/stop/burst on events). Load for prompts like "particles", "snow", "rain", "fire", "sparks", "smoke", "confetti", "fireworks", "magic dust".
- hair: Hair Systems: simulated strands (hair, fur, grass, fibers) via hair() — growing strands from an object's surface or a built-in scalp, strand shape (length, width, kink/curl, clumping), physics (gravity, wind, stiffness), root/mid/tip coloring or inheriting the base object's surface color, and recipes (character hair, fur, grass). Load for prompts like "hair", "fur", "furry", "fluffy", "grass", "beard", "mustache", "hairy".
- scene-optimization: Scene performance optimization: reading analyze_scene reports, reducing polygons, decimate(), merge(), bakeBoolean(), consolidating materials, taming lights/shadows/effects/textures, removing unused content — the measure→fix→verify workflow and visual-parity rules. Load for "optimize my scene", "reduce the file size", "make it run faster", "improve FPS", "slow/laggy", "too many polygons", and every fix requested from the Performance panel.

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

---

**⚠️ Part 3 is REQUIRED before you author** — the rest of the DSL reference (environment & atmosphere, camera, selection, structure, animation/interactivity, aesthetic helpers, worked examples). Call `load_skill("authoring-guide-3")` now.