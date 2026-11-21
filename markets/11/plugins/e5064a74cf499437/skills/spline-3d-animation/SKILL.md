---
name: spline-3d-animation
description: "DEFAULT recipe for ALL animation/motion/interactivity asks (\"animate …\", \"make it grow/bloom/orbit/spin\", hover/click behavior, ambient life): scene by run_code with stable names + a pivot at every motion origin; the motion as plain JS in the HTML layer driving objects per frame via the spline bridge — one rAF clock, poses from elapsed time f(t), easing + stagger, entrance → idle handoff, recipes, perf budget. The built-in States & Transitions feature is OPT-IN only (load state-transitions when the user explicitly asks)."
---

# Animation & motion (code-driven)

Motion is CODE-DRIVEN BY DEFAULT: the scene — objects, pivots, materials,
lights — is authored with `run_code`, and ALL motion and behavior —
entrances, growth, orbits, ambient life, reactions to input — is plain
JavaScript in the file's HTML layer (`set_html_content`), computing poses
from elapsed time and writing them through the `spline` bridge
(`spline.updateObject`) every frame. This generalizes the `games` skill's
loop architecture to every moving scene, and the document ships with
exports (public URLs, viewer embeds, runtime code exports), where the same
bridge is injected — the motion IS the file's runtime behavior.

Do NOT reach for the built-in states machinery unless asked:

- States & Transitions (`animate()`, addState/addEvent/addAction/
  updateTween, the timeline) is OPT-IN: use it ONLY when the user
  explicitly asks — they name states, transitions, the timeline, or the
  States panel. Then load `state-transitions` and follow it instead.
- Two things must stay on the engine's machinery: PHYSICS-COUPLED
  kinematic motion (a positioned body pushes dynamic bodies only when a
  STATE animates it — bridge writes are teleports the simulation cannot
  see; `physics` skill), and SCROLL-DRIVEN sequences (the bridge never
  relays scroll — that is the Scroll event's job; `interactivity` skill).
  Decorative physics on objects the code never moves is fine.
- Interactivity a scene ALREADY runs on states/events gets its fixes and
  small additions in kind (`get_objects` → update by id — `interactivity`
  skill); NEW motion beside it is still code.

Load `html-content` alongside this skill for the full bridge API and
document rules (transparent background, passthrough, one document per
file).

Why this is the default: code motion is PROCEDURAL. Every pose derives
from time, so it is eased and staggered per element, channels compose
(grow + sway + drift on one object), a replay is one reset of the clock,
and all the rules live in one debuggable place. A pair of hand-authored
states with a tween between them reads as mechanical next to it.

## Layer 1 — build the scene FOR animation (run_code)

Motion quality is decided at build time, before any code runs:

- **Stable, unique names** for everything code will drive ('Part 0'…,
  'Wing L', 'Moon 1'…). The document looks names up ONCE at
  boot and drives objects BY ID thereafter.
- **STRUCTURE IS GENERATED — a part per moving element.** Whatever the
  subject, decompose it by what MOVES and generate that decomposition in
  code (see # Structure is generated below). The procedural generators
  (`tree()`, `rock()`) are baked wholes — right for scenery, wrong for a
  subject that must articulate or grow.
- **A pivot at every moving part's motion origin.** Objects rotate and
  scale around their own origin, so put the origin where the motion
  starts: a tree grows from its BASE, a door swings on its HINGE, a wheel
  spins on its AXLE, a petal opens from its STEM end. Two ways:
  - the procedural generators already do it — `tree()`/`rock()`/
    `building()` bases sit at y = 0 of their position, so scaling the
    handle's group from ~0 grows it out of the ground;
  - for assemblies, `add('Empty')` positioned AT the motion origin,
    build the parts in place, then `moveInto` them (NEXT call — the
    selection rule) and drive the EMPTY. One pivot per moving part —
    the same rule as procedural-generation's creature rigs.
  - a single center-origin primitive can grow from its base without a
    pivot by compensating in code: write `scale.y = s` AND
    `position.y = baseY + (height * s) / 2` in the same frame.
- **Bridge transforms are ABSOLUTE and LOCAL** (rotations in DEGREES).
  `updateObject` SETS values — its `scale` is not the DSL's multiply —
  and reads/writes are in the parent's frame, so snapshot each driven
  object's initial transform at boot and compute against that.
- **One writer per property.** An object the document drives must not
  ALSO carry states/bindings writing the same property — they fight.
  Compose all of a frame's channels in JS and write once.

## Layer 2 — the motion document (set_html_content)

ONE complete HTML document per file. For pure animation it is HEADLESS —
a `<script>` and nothing visible: leave html/body unstyled and
transparent; with no UI elements every pointer event passes through to
the viewport, so the user can still orbit. Add UI only when the request
calls for it (controls, a replay button, a HUD). If the file may already
HAVE a document (`get_html_content` to check), MERGE your motion in with
`edit_html_content` — never clobber a game or HUD with a full rewrite.

Non-negotiables, shared with the `games` loop:

- **One rAF loop, one clock.** Start it once at boot; every pose derives
  from a single elapsed time.
- **STATE FROM TIME — `pose = f(t)`, never `pose += delta`.** Compute
  each frame's pose from elapsed seconds: deterministic, staggerable per
  element, hitch-proof, and replayable (restart = reset the clock).
  Accumulate (+=) only when integrating INPUT or a simulation — that is
  the games skill's fixed-timestep territory, not an animation's.
- **Boot reads, then cached ids**: `await spline.ready`, look each name
  up ONCE, keep `{ id, p: initial position }`. A null lookup logs to the
  console and aborts cleanly — a throw inside the tick silently freezes
  ALL motion.
- **Easing + progress helpers** — inline these; motion is always eased:

```js
const clamp01 = (x) => Math.min(1, Math.max(0, x));
// phase progress: 0..1 over dur seconds, starting at delay
const prog = (t, delay, dur) => clamp01((t - delay) / dur);
const easeOutCubic = (p) => 1 - Math.pow(1 - p, 3);
const easeInOutSine = (p) => 0.5 - Math.cos(Math.PI * p) / 2;
// overshoot ("pop") — the organic entrance
const easeOutBack = (p) => {
  const c = 1.70158; const q = p - 1;
  return 1 + (c + 1) * q * q * q + c * q * q;
};
```

- **Stagger per element.** Element i gets its own delay (`i * 0.18`) and
  its own phase/duration jitter — simultaneous identical motion is the
  mechanical look the code path exists to avoid.
- **Entrance → idle handoff.** A growth/entrance settles into gentle
  perpetual life (sway, breathe, drift), never a hard stop: ramp the idle
  amplitude in with its own `prog(...)` as the entrance ends.

## Structure is generated (a part per moving element)

An animated subject is DECOMPOSED BY MOTION: one named object per element
that moves independently. The part list comes from asking "when THIS
subject moves / grows / reacts, what moves separately?" — never from a
fixed recipe; different subjects decompose differently. Generate that
decomposition in code (bounded loops/queues/recursion in `run_code`,
seeded randomness for organic variation) at the fidelity the ask implies,
and create every part at its authored FINAL pose — Edit mode shows the
finished subject; the document takes it through its motion.

- The driver must KNOW the structure — each part's role, geometry and
  timing. Two general techniques:
  - DETERMINISTIC REGENERATION: derive the part list from one seeded
    routine and run the IDENTICAL routine in both places (same seed, same
    call order ⇒ the same arrays; any edit edits both copies). Right when
    parts carry rich data the scene snapshot can't express — directions,
    lengths, per-part timing.
  - BOOT READS: name parts by convention ('Part 0'…), read their authored
    transforms at boot (`getAllObjects` + prefix filter) and derive the
    motion from those. Right when the authored pose is all the driver
    needs.
- TIMING IS PART OF THE STRUCTURE: give each part its own window or phase
  on ONE normalized timeline (`t = clamp01(elapsed / DURATION)`).
  Entrances run in structural order — supporting parts before the parts
  that depend on them, dependents opening BEFORE their support fully
  finishes: the overlap is what reads organic; a strict one-after-another
  sequence reads mechanical.
- DIRECTIONAL PARTS: a +Y-built part is aimed along a unit direction `d`
  with XYZ Euler degrees —
  `{ x: Math.atan2(d.z, d.y) * 180 / Math.PI, y: 0,
  z: Math.asin(-d.x) * 180 / Math.PI }` — the tool for any structure
  whose parts point somewhere (limbs, spokes, streams, rays). A part
  grows along its own axis by scaling while re-centering:
  `scale.y = g` plus `position = start + dir * (len * g / 2)`.
- GRANULARITY = MOTION, NOT GEOMETRY. A part is an independently MOVING
  element, not a geometric segment: a hero subject usually decomposes
  into ~5–20 parts, and each part's BODY is ONE rich procedural
  `customMesh` — compute the whole limb/blade/petal cluster, offshoots
  and detail included, into a single mesh (up to 60k vertices), pivoted
  at its motion origin. The object list should read like the subject's
  ANATOMY, never like its polygons — one object per geometric segment
  floods the scene tree the user has to live in. When even the anatomy
  parts would multiply (per-branch growth, a crowd, a wave field), drop
  a LEVEL instead of adding objects: the vertex channel and the
  instancing channel below animate arbitrary internal detail through ONE
  scene object. Write only what CHANGED each frame: zero a part once
  before its window opens, stop writing it once it settles, rotate slow
  ambient writes across frames.
- THE CHANNEL MAP — every level of motion through one object or less:
  - WHOLE-OBJECT: transforms/visibility (`updateObject`) — pivots,
    orbits, travel; numeric geometry params; `displace`/`noise` layer
    `movement` per frame = shader-space wobble/sway/shimmer for free.
  - INSIDE ONE MESH — the VERTEX CHANNEL: a `customMesh` accepts
    `updateObject(id, { geometry: { vertices, normals?, uvs?,
    indices? } })` per frame (flat arrays; pass `Float32Array` —
    matching topology updates the live GPU buffers in place). THE way to
    grow/deform structure without objects: keep the generator in the
    document, rebuild the vertex array at progress t, write it — a whole
    branching tree growing per limb is ONE mesh (≤60k vertices). Keep
    the topology (vertex/index counts) FIXED across frames — grow by
    moving vertices (collapsed→extended), not by adding them — so every
    frame takes the cheap in-place path.
  - MANY COPIES — the INSTANCING CHANNEL: make the template a cloner
    (`clone({...})`), then `spline.setInstanceTransforms(name,
    [{position, rotation, scale}, …])` writes every copy's transform in
    ONE call, indexed by copy (partial axes; degrees; a null entry — or
    null instead of the array — hands copies back to the layout;
    overrides survive re-layouts). THE way to drive swarms, crowds,
    leaves, debris: hundreds of moving copies, one scene object.
  - DYNAMIC COUNTS — RUNTIME SPAWNING: `spline.spawnObject(template,
    { name?, position?, rotation?, scale?, visible? })` creates a
    runtime-only copy (never saved, not selectable/raycastable; renders
    through its template) and resolves to its snapshot — drive it by id,
    remove with `spline.destroyObject(id)`. THE way to emit objects the
    scene can't pre-place (projectiles, spawned pickups, growing counts);
    budget 500 live copies — reuse or destroy, and hide the template
    with `visible: false` when it is only a mold. Copies restyle
    through their TEMPLATE (shared look), never individually.

The generic wiring, whatever the subject:

```js
await spline.ready;
const parts = [];                       // { id, …per-part data }
for (let i = 0; i < COUNT; i++) {       // from regeneration or boot reads
  const o = await spline.findObjectByName('Part ' + i);
  if (!o) { console.warn('missing Part ' + i); return; }
  parts.push({ id: o.id, p: o.position });
}
const t0 = performance.now();
(function tick(now) {
  const t = Math.min(1, (now - t0) / 1000 / DURATION);
  for (let i = 0; i < parts.length; i++) {
    // eased progress of part i's own window; skip when unchanged;
    // ONE composed updateObject(parts[i].id, …) from t, i and part data
  }
  requestAnimationFrame(tick);
})(t0);
```

## Ambient life (phase offsets)

Scenes that should just FEEL alive (drifting clouds, bobbing boats,
flickering fireflies) get the same loop with no entrance: per element i,
combine small channels with per-element frequency and phase —
`y = p.y + Math.sin(t * (0.5 + i * 0.13) + i * 2.4) * 12`, a slow drift
on x/z, a fraction of a degree of roll. Never one synchronized bob on a
whole group, and keep amplitudes SMALL (a few units, 1–4°) — ambient means
felt, not watched. Collect the elements at boot by name prefix
(`getAllObjects()` then filter) so a scatter of 20 clouds is one array.

## Orbits, spins & travel

- Endless spin: `rotation.y = (t * 24) % 360` (absolute; % keeps numbers
  finite).
- A REAL orbit is position math, not a spin:
  `x = cx + Math.cos(t * w + phase) * r; z = cz + Math.sin(t * w + phase) * r`
  — with per-body radius/speed/phase (moons, electrons, drones). Add
  `rotation.y = -(t * w + phase) * 180 / Math.PI` to keep a face inward.
- Travel along a route: precompute waypoints in JS, index by
  `u = (t / lapSeconds) % 1`, and interpolate — same shape as the games
  skill's racing line (steady speed needs arc-length-ish spacing:
  keep waypoints roughly evenly spaced).

## Triggered phases & input (code-driven interactivity)

A one-shot reaction is STILL f(t): record when it started, then compute
from that moment.

```js
let burstAt = -1;                       // set on input
const b = burstAt < 0 ? 0 : prog(t, burstAt, 0.6);   // in the tick
```

- Page-level input (keyboard, pointer anywhere, UI controls): plain DOM
  handlers in the document — buttons/sliders drive parameters directly
  (`html-content` skill). Games-grade input (held-key sets, focus/pause)
  is the `games` skill.
- Click/hover on a SPECIFIC OBJECT: author that event on the object as a
  SENSOR — it needs NO actions — and respond in code. run_code:
  `select('Bloom'); addEvent('MouseDown');` — document:
  `spline.addEventListener('mouseDown', (e) => { if (e.target.name === 'Bloom') burstAt = t; })`.
  Sensor events fire in Play mode (and exports) — say so to the user.
- Replay/restart when asked: `t0 = performance.now()` (and re-zero any
  trigger timestamps) wired to a button or key.

## Imported model animations (baked clips)

An IMPORTED model (GLB/FBX) may carry its own authored clips — skeletal or
node animations baked into the file. Those are already eased and
hand-keyed: PLAY them, never rebuild them with pose writes.
`clips:N` in the scene digest flags the object carrying them;
`get_objects` lists each clip's `id`, `name` and `duration`. The
document drives them through the bridge (`html-content` skill):

```js
await spline.ready;
const MODEL = '<model name or id>';
const clips = await spline.getAnimations(MODEL);  // the real names: never guess
const base = clips[0].name;
await spline.playAnimation(MODEL, base);          // loops by default
document.querySelector('#next').onclick = () =>
  spline.playAnimation(MODEL, clips[1].name, { fade: 0.3 });   // cross-fade
document.querySelector('#once').onclick = async () => {
  const clip = await spline.playAnimation(MODEL, clips[2].name, { loop: false, fade: 0.15 });
  if (clip) setTimeout(() => spline.playAnimation(MODEL, base, { fade: 0.3 }),
    clip.duration * 1000);                        // one-shot, then back
};
// spline.pauseAnimation(MODEL) holds the pose (play resumes);
// spline.stopAnimation(MODEL) rests it on the first frame.
```

- An import ships a `Start` event whose Animation action plays the
  model's first clip. When the document drives the clips, REMOVE that event
  first (`get_objects` for its id → `removeEvent` in run_code) — it
  fires a beat after the document boots and overrides its first
  `playAnimation`. One owner per model's clips.
- One clip per object at a time: playing another replaces it (`fade`
  blends the two). Clip names come prefixed with the file name
  ('<file>_<clip>'); the clip's own name resolves too.
- Moving the model AROUND (travel, turning to face a direction) is still
  the loop's job — drive its top-level group with `updateObject` while
  the clip animates the limbs, never the clip's own bones.
- Use an Animation ACTION (`interactivity` skill) instead only when the
  user asks for it on an event in the States/Events panel.

## Material & geometry motion

- Material motion rides the same loop: `spline.updateObject(id,
  { material: { layers: [{ type: 'gradient', angle: 120 + Math.sin(t * 0.7) * 40 }] } })`
  — flowing water, shimmer, pulsing emissive color. Hero surfaces only.
- Geometry parameters animate too (`{ geometry: { cornerRadius: v } }`,
  a Text object's `{ geometry: { text: label } }`) — each write
  REGENERATES the mesh, so keep it to one or two hero objects, and
  throttle text to ~10 Hz. Note a Lathe's size does not respond to
  geometry tweens (profile-driven) — scale it instead.

## Performance budget

- ONE `updateObject` per animated object per frame, fire-and-forget (no
  await in the tick). A few dozen writes per frame is comfortable (brief
  peaks near sixty are fine); hundreds is not — past a few dozen movers,
  switch channel: `setInstanceTransforms` moves every cloner copy in ONE
  message, and the vertex channel moves a whole mesh's structure in one.
  Otherwise write only what CHANGED
  this frame (track per-part zeroed/settled flags), drive GROUP
  pivots instead of leaves, thin the animated set, or update the slow
  layer every 3rd frame.
- Never write DOM text every frame (~10 Hz for readouts — games rule).
- Bridge writes are transient (never saved, reset on reload) — exactly
  right for motion; the authored scene stays clean.

## Verify

- `play()`, screenshot, then screenshot AGAIN — the two captures land a
  beat apart, so poses MUST differ between them; identical frames mean
  the loop isn't running (Console strip shows the error — read it).
  `stop()` when done so the user isn't left in play mode.
- Screenshots capture the 3D canvas only — HTML UI never appears in
  them; verify documents through the Console strip and by telling the
  user what they should see.
- Tell the user where the motion runs: Play mode, the Preview tab, and
  every export. The Edit tab unmounts the document so the scene stays
  editable — the still scene there is expected, not a bug.
- Entrance pacing: a whole entrance inside ~2–4 s unless asked otherwise;
  idle amplitudes small. If the screenshotted mid-growth pose looks like
  scenery collapsing (parts at odd scales), the pivots/compensation are
  wrong — fix Layer 1, don't mask it with timing.

Gotchas:
- `updateObject` transforms are ABSOLUTE, LOCAL, and in DEGREES — read
  the boot snapshot, write computed values; a DSL-style "multiply" scale
  assumption doubles the object every frame.
- A thrown error inside the tick freezes ALL motion silently — guard
  lookups, read the Console strip.
- Exact scale 0 can degenerate — clamp to 0.001.
- Two writers on one property (a state/binding + the loop) fight —
  one owner per property, channels composed in JS.
- Don't drive objects a physics simulation owns (dynamic bodies), and
  don't expect driven motion to push them — kinematic pushing is the
  states carve-out (`physics` skill).
- One document per file: merge into an existing document with
  `edit_html_content`; `set_html_content` replaces the whole thing.
