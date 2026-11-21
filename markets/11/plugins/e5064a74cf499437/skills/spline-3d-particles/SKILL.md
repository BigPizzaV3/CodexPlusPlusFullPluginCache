---
name: spline-3d-particles
description: "Particle emitters: creating and tuning them with particles() (emission, motion, sprite look, emitter shapes, timing), recipes (snow, rain, fire, smoke, confetti, auras), and runtime control via the Particles action (start/stop/burst on events). Load for prompts like \"particles\", \"snow\", \"rain\", \"fire\", \"sparks\", \"smoke\", \"confetti\", \"fireworks\", \"magic dust\"."
---

# Particles (emitters & runtime control)

A particle emitter is its OWN object type (`'Particle'` in the scene tree),
not a material layer. It continuously spawns short-lived billboard sprites —
the tool for snow, rain, fire, smoke, sparks, confetti, dust, magic.

## Create & edit

```
particles('new', { birthRatePerSec: 120, life: 2 });  // create + configure
rename('Sparks');
```
- `particles('new', props?)` creates an emitter (returns it like `mesh` does);
  `add('Particle')` is the bare equivalent.
- `particles(props)` (no 'new') MERGES props over the SELECTED emitter —
  partial props edit it in place, other selected object types are skipped.
  `select(o => o.type === 'Particle')` or by name first when editing later.
- `get_objects([id])` returns a `particles` block in exactly this prop shape —
  read, tweak, pass back.
- The emitter is a normal object: `position`/`rotation`/`rename`/`group`/
  `hide` all work. Rotating the emitter reorients its emission — often easier
  than direction math.

The default emitter is a decorative pink→amber fountain (50/sec, 1s life,
drifting up from a 100-unit plane, auto-playing forever). Treat every recipe
below as overrides of that.

## The mental model

Each particle: spawns somewhere on/in the `shape` → flies with `speed` along
`direction` (or the shape's surface normal) → is bent by `gravity` and noise
over its `life` → its sprite blends `color`→`color2` and fades/shrinks by the
two eases → dies. `birthRatePerSec × life` ≈ how many are alive at once; keep
it in the low thousands (hard engine cap 100k).

## Props (units matter)

Emission & motion:
- `birthRatePerSec` — particles per second (UI range 1–2000).
- `life` — seconds each particle lives (max 10).
- `speed` — initial velocity, 0–200.
- `direction: [x,y,z]` — Euler DEGREES rotating the emission axis, which
  starts as +Y (straight up). `[0,0,180]` = down, `[90,0,0]` = toward +Z.
- `directionMode` — `'axis'` (all particles fly parallel to `direction`) or
  `'normals'` (each flies out along the shape's surface normal — radial
  bursts, auras).
- `gravity` — signed Y force, ±50: negative falls (snow `-1`, rain `-20`),
  positive rises (fire `2`). Default is `1` — a gentle updrift.

Turbulence & per-particle variation:
- `noiseType: 'curl' | 'simplex' | 'fbm'` + `noiseStrength` (0–10 is plenty;
  0 = off) + `noiseScale` + `noiseSeed` — bends trajectories; curl gives the
  swirly drift that sells snow and smoke.
- `randomScale` (0–1), `randomRotation` (0–5), `randomMass` (0–1 — varies how
  hard gravity pulls each particle, giving natural arcs).

Sprite look — nested under `material`:
- `color`, `color2` — hex strings fine. `coloring: 'gradient'` blends
  color→color2 over each particle's life; `'random'` picks one of the two per
  particle (confetti).
- `ease` (alpha over life) and `easeSize` (size over life):
  `'linearFadeIn' | 'linearFadeOut' | 'linearInOut' | 'quickFadeInOut' |
  'exponentialInOut' | 'constant'`.
- `size: [start, end]` — sprite size in pixels-ish units (1–256 typical).
  Grow smoke (`[10, 60]`), shrink sparks (`[24, 4]`).
- `spriteRotation: [start, end]` (0–1) — spins the sprite over life.
- The sprite texture is NOT settable from code — the default is a soft round
  dot (fine for almost everything); users can swap the image in the Particles
  panel.

Where particles spawn — nested under `shape`:
- `type: 'Plane' | 'Box' | 'Sphere' | 'Cone' | 'Torus' | 'Mesh'` +
  `size: [x,y,z]` in world units. A wide flat Plane overhead = weather; a
  Sphere + `directionMode: 'normals'` = radial burst.
- `'Mesh'` emits from another object's surface: `shape: { type: 'Mesh',
  fromMeshId: obj.id }` (size acts as a ~[1,1,1] multiplier there). Pair with
  `'normals'` for an aura that hugs the object.

When it emits:
- `autoPlay` — start emitting on load (default true). Set `false` for
  anything an event should trigger.
- `emitTimeCycle` — `'infinity'` (continuous, default), `'one_time'` (emit
  for `emitTimeDuration` seconds then stop — a burst), `'loop'` (emit
  `emitTimeDuration`, wait `emitTimeDelay`, repeat). All in seconds.

Collisions (optional): `add('ParticleCollider')`, position it, then
`particles({ colliderEntityId: collider.id, collisionBounce: 0.75 })` on the
emitter (one collider per emitter; bounce 0–1).

## Recipes

Snow (the library preset's real numbers):
```
particles('new', {
  birthRatePerSec: 400, life: 3, speed: 5, gravity: -1,
  direction: [0, 0, 180],                       // straight down
  noiseType: 'curl', noiseStrength: 0.8,        // the drift
  material: { color: '#ffffff', color2: '#ffffff',
              ease: 'constant', easeSize: 'constant', size: [10, 10] },
  shape: { type: 'Plane', size: [1000, 1, 1000] },
});
position({ y: 400 });                            // sky-wide sheet overhead
rename('Snow');
```
Rain is the same idea, harder: `speed: 120, gravity: -20, life: 1.2,
noiseStrength: 0, material: { size: [3, 3], color: '#9db8d9' }`.

Fire:
```
particles('new', {
  birthRatePerSec: 150, life: 1.2, speed: 30, gravity: 2,
  noiseType: 'curl', noiseStrength: 1.5,
  material: { color: '#ffd166', color2: '#ff3b00', coloring: 'gradient',
              ease: 'quickFadeInOut', easeSize: 'linearFadeOut', size: [26, 6] },
  shape: { type: 'Sphere', size: [40, 10, 40] },
});
rename('Fire');
```
The gradient's hot colors read as fire on their own — add
`fx('bloom', { intensity: 0.8 })` only if the user asks for glow. Smoke above
it: gray-on-gray gradient, `speed: 12, gravity: 1.5, life: 3, noiseType: 'fbm',
noiseStrength: 2, material: { size: [14, 70], ease: 'linearInOut' }`.

Aura hugging an object (emit from its surface):
```
const gem = mesh('Sphere', { width: 120, height: 120, depth: 120 });
const em = particles('new', {
  birthRatePerSec: 60, life: 1.5, speed: 6, directionMode: 'normals',
  material: { color: '#b28dff', color2: '#4dc3ff', size: [10, 2] },
  shape: { type: 'Mesh', fromMeshId: gem.id },
});
```
Position the emitter at the object (or `group` them) so the surface and the
spawn volume line up.

## Controlling emitters with events

The `'Particles'` ACTION drives an emitter from any object's event (allowed on
most events — not Scroll/LookAt/Follow; also usable inside GameControl):

```
// A confetti burst that fires when the button is clicked
const em = particles('new', {
  autoPlay: false,                               // wait for the event
  emitTimeCycle: 'one_time', emitTimeDuration: 0.25,
  birthRatePerSec: 800, life: 2, speed: 70, gravity: -8,
  directionMode: 'normals', randomMass: 0.8, randomRotation: 2,
  material: { coloring: 'random', color: '#ff3b7b', color2: '#33d1ff',
              ease: 'constant', easeSize: 'constant',
              size: [12, 12], spriteRotation: [0, 1] },
  shape: { type: 'Sphere', size: [40, 40, 40] },
});
rename('Confetti');

select(o => o.name === 'Button');                // the emitter's controller
const e = addEvent('MouseDown');
const a = addAction(e, 'Particles');
updateAction(e, a.actionId, { emitterObjectId: em.id, emission: 'start' });
```

`updateAction` props for a Particles action:
- `emitterObjectId` — the emitter's id (from `particles('new')`'s return,
  `select(...)[0].id`, or the `<editor-context>` snapshot).
- `emission`:
  - `'start'` — begin an emission cycle (the burst trigger).
  - `'stop'` — stop emitting; particles already in the air live out.
  - `'pause'` / `'pauseToggle'` — freeze / resume the whole system mid-air.
  - `'emitToggle'` — start/stop on alternate firings (ambient on/off switch).
  - `'reset'` — clear all live particles.
- `delay` — milliseconds before the action runs (same unit as tween delays;
  the inspector displays it in seconds).

Ambient vs triggered, in short: weather/fire = `autoPlay: true` +
`'infinity'` and no wiring needed; bursts = `autoPlay: false` +
`'one_time'` + a `'start'` action; toggleable ambience = `autoPlay` as you
like + `'emitToggle'`.

Stack them like any action — e.g. one MouseDown with a Transition (button
squash) AND a Particles 'start'. Editing existing wiring: `get_objects` shows
each Particles action's `emitterObjectId`/`emission`/`delay` next to its ids.

## Verifying

Static screenshots lie twice here: events don't fire outside play mode, and a
just-started emitter has spawned almost nothing. `play()`, give it a beat,
then `take_screenshot()` — for click-triggered bursts you still see the scene,
not the burst, so trust the wiring check via `get_objects` over pixels. In the
editor, an emitter previews live while it is selected.
