---
name: spline-3d-physics
description: "The physics simulation itself (no character needed): page Simulation switch + gravity, physics() in depth (positioned colliders vs dynamic bodies, friction/bounce/density/gravityScale/damping, convex vs trimesh colliders, fused vs separate group bodies, axis locks), kinematic movers (animated/dragged colliders that push dynamic bodies), spawning dynamic objects with the Create action, and falling/stacking/bouncing/floating recipes."
---

# Physics (rigid-body simulation)

Spline runs a rigid-body physics engine (Rapier) while the scene PLAYS —
in play mode and in exports, never while editing. Objects fall, stack,
slide, bounce and knock each other over; nothing simulated is written back
to the scene (`stop()` returns everything to its authored layout).

This skill is the simulation reference. For a PLAYABLE CHARACTER standing
on and pushing this world with the built-in Game Controls feature
(`GameControl`, colliders, key mapping, Collision/Trigger gameplay —
only when the user asked for it), load the `game-controls` skill; the
DEFAULT game recipe (JS game loop + HTML UI, no engine physics) is the
`games` skill; for the generic event/action machinery, load
`interactivity`.

## The simulation model

- **Page switch** — physics is off per page until enabled. The first
  `physics(...)` call flips it on automatically; there is no DSL call to
  turn it back off (Simulation panel in the page settings).
- **Gravity** — a page-wide setting (default `-10` m/s², UI slider -20..20;
  POSITIVE values invert gravity so dynamic bodies fall UP). It is NOT
  settable from the DSL — if a scene needs different global gravity, ask the
  user to change it in the Simulation panel. Your per-object lever is
  `gravityScale` (below).
- **Scale** — 200 world units = 1 meter. A 200-unit cube behaves like a
  1 m crate; a 2000-unit-tall scene is a 10 m drop, so very large scenes
  look like they fall in slow motion (they're big, not slow). Keep play
  scenes roughly real-world sized when the motion should feel snappy.
- **Body roles**:
  - `'positioned'` (the default) — an immovable collider: floors, walls,
    ramps, furniture. Ignores gravity, blocks and is never pushed.
  - `'dynamic'` — fully simulated: falls, rolls, gets pushed, knocks
    other dynamic bodies around.
  - **kinematic movers** — a positioned body that ANIMATES (see below)
    follows its animation exactly and shoves dynamic bodies out of its way.
    (The GameControl character is kinematic too — `game-controls` skill.)

## `physics(props)` — the DSL call

Applies to the SELECTED object(s), like other aliases. Unlike
`updateEvent`'s nested objects, `physics()` MERGES: pass only the fields
you change; repeated calls tweak incrementally. (The axis-lock triples are
the exception — each is replaced whole.)

- `type`: `'positioned'` (default) | `'dynamic'`.
- `friction` (0..1, default 0.5) — surface grip. The engine AVERAGES the
  friction of the two touching surfaces, so an icy floor still slides a
  grippy crate somewhat.
- `bounce` (0..1, default 0.2) — restitution, also AVERAGED between the
  two surfaces: a `bounce: 1` ball on a `bounce: 0.2` floor bounces at
  ~0.6. For a properly bouncy ball, raise the floor's bounce too.
- `density` (default 1; the UI calls it "Weight") — mass comes from
  density x volume. It decides who pushes whom in contacts (a dense crate
  plows through light ones); it does NOT change free-fall speed.
- `gravityScale` (default 1) — per-object gravity multiplier: `0` floats
  in place (still collidable — good for zero-g props), `0.2` feels
  moon-like, a small negative value slowly RISES (balloon).
- `damping` (default 0) — air resistance on movement AND spin: higher
  values fall slower, stop rolling sooner, kill drift. The usual fix for
  "it slides/rolls forever".
- `colliderType`: `'convex'` (default — fast; wraps the mesh in a convex
  hull, sealing any concavity shut) | `'trimesh'` (exact triangles —
  required for bowls, arches, tunnels, ramps with holes; slower). Use
  trimesh on positioned decor; keep dynamic bodies convex.
- `fusedBody` (default true; UI "Children: Fused/Separate") — a group with
  `fusedBody: true` is ONE rigid body built from all child meshes (a table
  falls as a table). With `false` each child simulates independently —
  select the children and give them their own physics props (a stack of
  crates you grouped for tidiness but want to topple crate by crate).
- `enabledTranslation` / `enabledRotation`: `[x, y, z]` booleans
  (dynamic bodies only) — axis locks, replaced WHOLE. Lock what shouldn't
  move: `enabledRotation: [false, false, false]` makes a crate slide
  without tumbling; `enabledTranslation: [true, true, false]` +
  `enabledRotation: [false, false, true]` confines a body to the XY plane
  for 2D-style physics.
- You may also pass the raw schema names `rigidBody` / `restitution`
  (`type` / `bounce` are their friendly spellings).
- `pointMass` exists in the schema but the runtime ignores it — don't use.

Enable/disable semantics: an object's physics `enabled` defaults to
`'visibility'`, so once the page simulation is on, every VISIBLE object
already participates as a positioned collider — and HIDING an object removes
it from the simulation. Still call `physics()` explicitly on the objects
that matter so their type/friction/bounce are deliberate. The DSL can only
enable and tune: `physics(null)` / `physics({ enabled: false })` do NOT
remove physics from an object — to keep something out of the simulation,
hide it, or ask the user to set Enabled: No in its Physics panel.

## Kinematic movers — animated colliders that push things

This is THE carve-out from code-driven motion (# Motion & interactivity):
per-frame bridge writes are teleports the simulation cannot see, so a mover
that must PUSH dynamic bodies is state-driven — the one motion that stays
on `animate()`. A POSITIONED object becomes a kinematic body when it has
any state that
animates its transform (e.g. created with `animate()`), a `Follow` event,
or a `DragDrop` event. It follows its animation exactly (never pushed
back) and bulldozes dynamic bodies — the way to build moving platforms,
sweepers, flippers and crushers without any force API:

```
// conveyor platform sliding back and forth, carrying/pushing dynamic props
mesh('Cube', { width: 800, height: 60, depth: 400 });
position({ y: 200 }); rename('Mover');
physics({ type: 'positioned', friction: 0.9 });
animate({ position: { x: 1000 } },
        { duration: 2500, easing: 'ease-in-out', loop: true, direction: 'alternate' });
```

A spinning sweeper is the same recipe with `rotation: { y: 360 }` and
`easing: 'linear'`. A `DragDrop` event on a positioned object makes a
hand-controlled shover — the user drags it around to knock dynamic bodies
over (wire the event via the `interactivity` skill).

## Spawning dynamic bodies — the Create action

The `'Create'` action instantiates copies of a template object at runtime,
optionally as dynamic bodies with an initial velocity — the only way to
launch something (there is no force/impulse API):

```
// Space bar fires a ball from above the scene at the stack
const e = addEvent('KeyDown');
updateEvent(e, { key: 'Space' });
const c = addAction(e, 'Create');
// ballId: real id from get_scene/get_objects; velocity is world units/sec
updateAction(e, c.actionId, {
	object: ballId,
	dynamic: true,
	position: [-2000, 600, 0],
	velocity: [3000, 200, 0],
	destroy: 'Time', lifetime: 4,
});
```

- `dynamic: true` (the default) spawns a simulated body (the template's
  physics props apply — give the template `physics({ type: 'dynamic',
  ... })` first); `false` spawns a prop that just glides along
  `velocity`.
- `position` / `rotation` — spawn transform; `coordinateSystem:
  'world'` (default) or an object id to spawn relative to it (a moving
  cannon's muzzle).
- `destroy`: `'No'` | `'Time'` (+ `lifetime` seconds) | `'Collision'`
  (vanish on first contact) | `'Quantity'` (+ `destroyAfterQuantity` — only
  the N newest survive). Always bound continuous spawners — thousands of live
  bodies will tank the frame rate.
- `hideBase: 'Yes'` hides the template object during play — the RIGHT way
  to keep the original out of sight: its copies still simulate. Do NOT
  `hide()` the template instead — an authored-invisible template (with the
  default `'visibility'` enabling) spawns copies WITHOUT physics bodies.
- On press-and-hold events `creationSpeed` (default 10/sec) throttles the
  stream — a confetti or ball-pit hose.

## Reacting to contacts

`'Collision'` events fire when the host object's collider touches another
body: `target: 'scene'` reacts to ANY physics body (a dynamic crate landing
on a pressure plate), `target: 'character'` (the default) to the
game-controlled character only. `'Trigger'` events fire on entering an
invisible zone without physical contact. Both need physics enabled on the
page and the objects involved. The full wiring (actions, pickup recipe,
80 ms start suppression, zone props) is in the `games` skill; the generic
event/action API is in `interactivity`.

## Recipes

Falling stack (dominoes / tower knock-over):
```
mesh('Plane', { width: 4000, height: 4000 });
rotation({ x: -90 }); rename('Floor');
physics({ type: 'positioned', friction: 0.8 });
for (let i = 0; i < 5; i++) {
	mesh('Cube', { width: 200, height: 200, depth: 200 });
	// stack with a 10-unit air gap so colliders don't start overlapping
	position({ y: 110 + i * 210, x: (i % 2) * 20 });
	physics({ type: 'dynamic', friction: 0.6 });
}
// play(): the tower settles, a spawned ball (Create recipe) topples it
```

Bouncy ball: `physics({ type: 'dynamic', bounce: 0.9 })` on the ball AND
`bounce: 0.8` on the floor (remember: averaged), drop it from height.

Balloon: `physics({ type: 'dynamic', gravityScale: -0.05, damping: 0.9 })`
— rises slowly, drifts to a stop against the ceiling. `gravityScale: 0`
+ `damping: 0` is zero-g billiards instead.

Non-tumbling slider (2.5D feel): `physics({ type: 'dynamic',
enabledRotation: [false, false, false], enabledTranslation: [true, true,
false] })` — moves only in the XY plane and never falls over.

## Verify

`play()` starts the simulation (not undoable; `stop()` resets to the
authored layout). A screenshot right after `play()` catches bodies
mid-fall; for settled results, describe what should happen and have the
user confirm. Common failures:

- **Jumps/explodes at start** — colliders overlap in the authored layout.
  Leave small air gaps between stacked dynamic bodies and the floor; also
  remember a convex hull is FATTER than a concave mesh looks.
- **Falls through the floor** — the floor is hidden (`'visibility'`
  enabling), or paper-thin while the body moves fast (tunneling): give
  floors real thickness (≥ 50–100 units).
- **Rests tilted / rolls off flat ground** — convex hull on a concave
  mesh; use `colliderType: 'trimesh'` on the positioned decor.
- **Slides or spins forever** — raise `friction` on both surfaces and/or
  `damping` on the body.
- **Won't move at all** — it's still `'positioned'`; only `type:
  'dynamic'` bodies are simulated.
