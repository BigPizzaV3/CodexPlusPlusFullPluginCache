---
name: spline-3d-game-controls
description: "The built-in Game Controls feature — load ONLY when the user explicitly asks for it (says 'game controls', wants the editor's built-in character controller, touch joysticks, or a navmesh): the GameControl event (keyAssignments key mapping, walk/fly, collider, follow camera, idle/move/jump/run action containers), pairing it with physics() so the character stands on and pushes the decor, and Collision/Trigger events for pickups, obstacles and goal zones. Code-driven games (the default) are the `games` skill."
---

# Game Controls (the built-in GameControl event)

OPT-IN ONLY: games are code-driven by default (the `games` skill — a JS
game loop + HTML UI). Use the built-in Game Controls feature ONLY when the
user explicitly asks for it — they say "game controls", want the editor's
built-in character controller, touch joysticks, or navmesh-constrained
walking. Never put both movement systems on one player. Scene/hero building
guidance (generating the character with the AI mesh tool, budgets) is in
the `games` skill and applies here too.

A GameControl-based scene is four ingredients wired together:

1. a **player** carrying a `'GameControl'` event (keyboard/touch movement,
   jumping, follow camera); normally create one controller per page;
2. a **solid world** — `physics(...)` on every floor, platform, wall and prop
   so the character can stand on them and bump into them;
3. **gameplay reactions** — `'Collision'` events (physical touch) and
   `'Trigger'` events (entering a zone) running actions on contact;
4. **game state** — variables for score/lives, Conditional actions for win/lose.

Everything uses the standard event/action API (`addEvent` / `updateEvent` /
`addAction` / `updateAction`) — load the `interactivity` skill for that
machinery; this skill covers the game-specific parts.

## The GameControl event — making an object playable

Select the player object, then `const gc = addEvent('GameControl');`. The
alias special-cases it and seeds a complete third-person setup. Multiple objects
may carry GameControl events, but one page-level PRIMARY object supplies desktop
and touch controls. The first valid controller remains primary; merely adding
another event does not transfer control. Normally create one. In an existing
multi-controller scene inspect first—`addEvent` cannot choose a different primary:

- WASD to move, arrow keys to rotate, Space to jump, Shift to run;
- `moveMode: 'walk'` — gravity, landing on physics objects, jumping;
- a roughly auto-fitted capsule collider (replace it — see Collider below);
- the play camera following the character with a soft delay.

The player is a normal object — a mesh, an imported character, or a group
(attach the event to the top group so the whole character moves as one and its
skeletal clips are available to the action containers below). For a GENERATED
model, put the event on it directly or on its wrapping group, set the
`collider` EXPLICITLY (the auto-fit is even rougher on generated/imported
meshes, and their pivot often sits at the feet — `position: [0, height / 2,
0]`), give it `physics(...)` like any player, and confirm its facing (a
generated character may not lead with its `+z` side — watch for the "every
key inverted" symptom and flip `forwardDirection`, see Facing).

### Tuning — `updateEvent(gc, { ... })`

Movement:
- `moveMode`: `'walk'` (gravity + jump) or `'fly'` (free 3D flight; the
  moveNegY/movePosY assignments become usable).
- `speedTranslate` (default 1000), `runMultiplier` (default 2, applied while
  the run key is held), `speedRotate` (default 100).
- `delayPos` / `delayRot` — `[in, out]` smoothing for start/stop of
  translation/rotation (0 = instant, 0.3 = soft).
- `jumpPower` (default 100). Jumping requires walk mode, `collisionEnabled:
  true`, and the character standing on something.
- `resetYPosition` (default 3000) — how far the character may fall below its
  starting height before auto-resetting to the start ("fell off the level").
- `forwardDirection: '+z' | '-z'` — which LOCAL axis is the character's
  front. It MUST match the side of the object that actually leads: `'+z'`
  (default) is the side meshes and imports face when created (toward the
  default camera); `'-z'` is a front that points INTO the screen — set it
  for behind-the-back setups (a paddle facing the net, a runner heading away
  from the camera). Wrong value = every movement key inverted (see Key
  mapping). Movement slots stay character-relative either way (`moveNegZ`
  is always "walk forward").
- `autoOrientMove: true` — the character turns its front toward its movement
  direction while moving (`orientWith: 'camera' | 'axis'`, `orientMode:
  'radial' | 'cartesian'`); `false` — the character keeps a fixed heading
  and strafes (set the heading yourself — see Facing).
- `rotBy`: `'keys' | 'mouse' | 'both'` — mouse-look disables the rotation
  key assignments.
- `collisionEnabled` (default true) — false ghosts through everything.

Collider — SET IT EXPLICITLY. The auto-fit is approximate (bounding-box
based; often off-center or mis-sized, especially on groups and imported
models), so right after `addEvent` pass a complete collider matching the
visible mesh:

```
updateEvent(gc, { collider: { type: 'capsule', height: 180, radius: 50,
	position: [0, 0, 0], rotation: [0, 0, 0] } });
```

- `position` is relative to the object's origin — usually `[0, 0, 0]`
  (all primitives are centered on their pivot); an import with its pivot at
  the feet needs `[0, height / 2, 0]`.
- `type: 'capsule'` (height, radius — height includes the end caps, so keep
  `height >= 2 * radius`), `'box'` (width/height/depth), `'sphere'`
  (radius). Sizes are world units; `rotation` is RADIANS.
- Keep `colliderHelperVisible: true` while building and check a screenshot:
  the green helper must wrap the mesh snugly, centered on it.

Camera:
- `camera`: a camera object id — that camera follows the character
  (`delayPosCamera` / `delayRotCamera` smooth the follow). It keeps the
  angle it has when play starts, so frame the shot first. The follow camera and
  page Play Camera must be the same: `updateEvent(gc, { camera: playCam.id });`
  then `setPlayCamera(playCam);`. `activateCamera` changes only the editor
  viewport and is not a substitute. The first GameControl is seeded from the
  current Play Camera when available.
- `cameraXAxis` / `cameraYAxis`: `'Locked' | 'Limit' | 'Free'` — how much
  the user can orbit around the character. Lock BOTH for a fixed-angle game
  (side-scroller, top-down). `cameraRotXLimits` / `cameraRotYLimits`
  (radians) bound the 'Limit' mode.

Touch:
- `touchControl: true` (default) shows joysticks + a jump button on touch
  devices automatically; `joystickPosLoc` / `joystickRotLoc` /
  `jumpTouchButtonLoc` pick their screen slots.

Navmesh (optional): `navmesh: { enabled: true, zones: 'all' | 'custom',
objects: [...], ... }` bakes a navigation mesh and constrains walking to it —
a way to fence the walkable area without invisible walls.

IMPORTANT: `updateEvent` shallow-merges top-level props. Nested values —
`keyAssignments`, `collider`, `navmesh` — are replaced WHOLE, so always
pass every field of the nested object (read the current one with
`get_objects` first when editing).

### Key mapping — `keyAssignments`

The complete mapping is a list of `[movement, key]` pairs. This is the
canonical default layout and order:

```
[['moveNegZ', 'W'], ['moveNegX', 'A'], ['movePosZ', 'S'], ['movePosX', 'D'],
 ['rotPosX', '▲'], ['rotPosY', '◀'], ['rotNegX', '▼'], ['rotNegY', '▶'],
 ['jump', 'Space'], ['run', '⇧'], ['none', 'Ctrl']]
```

For generated standard layouts, preserve all existing entries/order and change
only action codes unless the user explicitly requests different keys. The
product supports re-keying: first read `keyAssignments` with `get_objects`,
replace the desired key string, and send the ENTIRE array because updates replace
it whole. `'▲' '◀' '▼' '▶'` conventionally represent arrow keys and `'⇧'`
Shift, but other key strings are valid. Movements: `moveNegZ`
(forward) / `movePosZ` (backward) / `moveNegX` (strafe left) /
`movePosX` (strafe right), `moveNegY` / `movePosY` (fly-mode
descend/climb), `rotPosX` / `rotNegX` (look up/down), `rotPosY` /
`rotNegY` (turn left/right), `jump`, `run`, and `'none'` (key does
nothing). Several slots may share one movement (e.g. both 'D' and '▶' →
forward). To restrict a control scheme, set every unused slot to `'none'`.

THE MOVEMENTS ARE CHARACTER-RELATIVE, NOT WORLD AXES. `moveNegZ` always
means "walk the way the character's front points" — it is the seeded 'W' —
regardless of the object's rotation or `forwardDirection` (which only picks
which local mesh axis counts as the front). So to send the character in a
world/screen direction, do NOT hunt for the matching X/Z slot: rotate the
CHARACTER to face that direction (see Facing) and bind the
forward/backward slots. A side-scroller whose goal is to the right =
character rotated to face +X, then `moveNegZ` (forward) on ▶ and
`movePosZ` (backward) on ◀. The strafe slots (`moveNegX`/`movePosX`)
are for sidestepping in free-roam schemes, not for picking world directions.
After wiring, `play()` and have the user confirm the directions.

If EVERY direction key feels inverted while the assignments read correctly,
the `forwardDirection` doesn't match the character's real front (the event
keeps the seeded `'+z'` while the object actually leads with its −Z side,
or vice versa). Flip `forwardDirection` — don't rewire the keys.

### Facing — which way the character looks

A character's front is its local `forwardDirection` axis — `'+z'` by
default, the side that faces the camera when a mesh or import is created. Do
NOT assume the controller will turn a camera-facing model toward its movement:

- Fixed-heading games (side-scroller, top-down): set `autoOrientMove: false`
  and rotate the PLAYER OBJECT once so it faces the travel direction — e.g.
  `rotation({ y: 90 })` turns a camera-facing model to face +X (screen right
  on a front camera). The movement basis rotates WITH the heading: after this,
  `moveNegZ` (forward) walks +X — which is exactly why you aim the character
  first and then just bind forward/backward.
- Behind-the-back games (camera behind the player, looking into the scene —
  a ping-pong paddle facing the net, a runner heading into the screen): the
  playable object's front is its local −Z, so set
  `forwardDirection: '-z'`. Do NOT fix this by rotating the object 180°
  (that would visually turn it around) and do NOT rewire the keys — leaving
  `'+z'` here inverts EVERY movement key even though the keyAssignments
  read correctly, which is the telltale symptom.
- Free-roam third-person: keep `autoOrientMove: true` (the default) — the
  character turns toward where it walks. Verify in play mode that the model
  doesn't walk backwards or sideways; if it does, its geometry front doesn't
  match `forwardDirection` — nest the mesh in a group (put the event on the
  group) and pre-rotate the mesh inside, or flip `forwardDirection`.

### The gameActions containers — idle / move / jump / run

GameControl actions live in four containers keyed to what the character is
doing — pass the container name as `addAction`'s 3rd argument (default:
`'move'`):

- `'idle'` — on the ground, not moving;
- `'move'` — moving on the ground;
- `'run'` — moving with the run key held (replaces 'move' while held);
- `'jump'` — from takeoff until landing.

Allowed action types: Transition / Animation / TimelineAnimation / Audio /
Particles / Create / Conditional. Lifecycle differs by action: Transition stops
and returns its target to Base State; TimelineAnimation, Audio, and Particles
stop; Create receives start/stop lifecycle. Skeletal Animation starts on entry
but GameControl does NOT explicitly stop it on exit, so do not rely on exit to
stop imported clips—test them in Play mode. Conditional gates its nested actions
and is not visible feedback itself. Use these for a walk cycle in 'move', a
stretched pose or whoosh in 'jump', or dust particles in 'run':

```
const walk = addAction(gc, 'Animation', 'move');
updateAction(gc, walk.actionId, { clipId: '<clip id>' }); // only if the object has imported clips
```

## Physics — making the world solid

The character only collides with objects that are IN the physics world.
`physics(props)` on the SELECTED object(s) puts them there (and switches
physics on for the page the first time):

- `physics({ type: 'positioned' })` — immovable collider: floors, platforms,
  walls, ramps, obstacles. This is the default type.
- `physics({ type: 'dynamic' })` — fully simulated: falls under gravity, gets
  pushed by the character, can be knocked off ledges (crates, balls, dominoes).
- Extras: `friction` (0..1), `bounce` (0..1), `density`, `gravityScale`
  (0 = floats), `damping`, `colliderType: 'convex' (default) | 'trimesh'` —
  use `'trimesh'` for concave shapes the character walks inside or through
  (bowls, arches, tunnels); a convex hull seals openings shut.

Give the PLAYER physics too — `physics({ friction: 0.5 })` is enough. An
object without physics does not exist to the physics world, including the
character itself. The character's body is kinematic: the GameControl event
moves it directly, it pushes 'dynamic' bodies around but is never pushed back,
and its shape comes from the event's `collider`, not the mesh.

Anything the character must stand on needs physics — a ground without it means
the character falls at play start until `resetYPosition` respawns it.

This is the game-facing summary. The full simulation reference — axis locks,
fused vs separate group bodies, moving platforms/sweepers (kinematic movers),
spawning dynamic bodies with the Create action, page gravity, units — is the
`physics` skill.

## Collision events — reacting to touch

A `'Collision'` event goes on the DECOR object (the coin, the spike, the
crate) — NOT on the player. It fires once each time a contact STARTS (it
re-arms after separation), and needs the object to have physics enabled:

- `target: 'character'` (default) — fires when the game-controlled character
  touches this object.
- `target: 'scene'` — fires when any OTHER physics body collides with it
  (a dynamic crate landing on a pressure plate).

Pickup recipe — "touching the coin collects it":

```
const scoreId = setVariable('score', 0);
select(o => o.name === 'Coin');
physics({ type: 'positioned' });
const hit = addEvent('Collision'); // target defaults to 'character'
const s = addAction(hit, 'SetVariable');
updateAction(hit, s.actionId, {
	variableId: scoreId,
	expression: 'score + 1', // the new value — score = score + 1
});
const d = addAction(hit, 'Destroy');
// coinId must be the real id read from get_scene/get_objects in this edit call.
updateAction(hit, d.actionId, { objects: [coinId] }); // the coin removes itself
```

Add an `'Audio'` action for a pickup sound, or a `'Transition'` on the hit
object (flash red on damage, squash a bumper). Collision events are suppressed
for the first ~80ms of play so resting contacts (character already standing on
the floor) don't all fire at start.

## Trigger events — invisible zones

`addEvent('Trigger')` on an object defines an invisible box/sphere sensor
positioned RELATIVE to that object. It fires when something ENTERS the zone —
no physical contact needed, and the SENSOR never blocks movement. A mesh host
with ordinary positioned physics still has its own solid collider, however; keep
that collider outside the path:

- `triggerZone: 'box' | 'sphere'`, `size: [w,h,d]` or `radius`,
  `position`, `rotation` (degrees in this DSL), `helperVisible`.
- `target: 'all'` (any object) or `'custom'` +
  `triggeringObjects: ['<player id>']` — restrict to the player so a stray
  crate can't finish the level.
- When page physics is on, the object HOSTING the trigger needs physics
  enabled too (the sensor is created as part of its physics body), and only
  objects with physics colliders are detected entering it.

Collision vs Trigger: a collision is a physical touch of the object's real
collider (it blocks the character); a trigger is a volume passed through. Use
triggers for goal/finish lines, checkpoints, kill zones under the level, doors
that open on approach; use collisions for pickups, obstacles and damage.

## Game state — initialization, score, win, lose, restart

`setVariable` declares authoring-time state. Use a Start event when runtime
initialization must run when the played/exported scene loads (and after a full
scene restart):
```
const scoreId = setVariable('score', 0);
const start = addEvent('Start');
const initScore = addAction(start, 'SetVariable');
updateAction(start, initScore.actionId, {
  variableId: scoreId,
  expression: '0',
});
```
Start also supports current schema-approved intro actions such as Transition,
Animation, TimelineAnimation, Audio, Particles, Video, Create, Destroy,
SwitchCamera, SceneTransition, Reset, SetVariable, DynamicVariablePlay,
Conditional, ClearLocalStorage, and UserAPI.

After a Collision increments score, put VariableChange on a stable controller or
UI object and gate the win behavior:
```
const changed = addEvent('VariableChange');
updateEvent(changed, { variableId: scoreId });
const gate = addAction(changed, 'Conditional');
updateAction(changed, gate.actionId, { condition: 'score >= 3' });
const reveal = addAction(changed, 'Transition', {
  parentActionId: gate.actionId,
  branch: 'if',
});
updateAction(changed, reveal.actionId, { object: winUiId });
// Configure reveal.tweenId with the real target state id from get_objects.
```
VariableChange may fire after every increment; disable/destroy remaining pickups
or guard with a `won`/phase variable if the win branch must run once.

For a live score/timer READOUT, skip events entirely: make a Text object and
bind its content — `select('ScoreText'); bindVariable('text', 'score');` (a
countdown is a `dynamicVariable('timeLeft', 'timer', …)` bound the same way,
with a VariableChange + Conditional on it for the time-up branch).

Keep three lose/restart patterns distinct:
- Fall recovery: `resetYPosition` restores only the controlled character's
  initial transform; score and world state persist.
- Full restart: Reset means Reset Scene—the whole runtime restarts after an
  optional delay: `const r = addAction(keyEvent, 'Reset');
  updateAction(keyEvent, r.actionId, { delay: 1 });` (seconds).
- Lives: decrement `lives` on Collision/Trigger, then VariableChange +
  Conditional reveals lose UI; a separate KeyDown/MouseDown Reset restarts.
A selective checkpoint teleport needs scene-specific transitions/state and is
not provided by generic Reset.

## Worked example — platform side-scroller

Fixed side-on camera, platforms along X, ◀/▶ to move back/forward along the
platforms ONLY (all other movement unmapped), Space to jump, one collectible,
one goal zone:

```
// --- world: long ground + a floating platform ---
mesh('Cube', { width: 6000, height: 100, depth: 400 });
position({ y: -50 }); rename('Ground');
physics({ type: 'positioned', friction: 0.8 });
mesh('Cube', { width: 800, height: 60, depth: 400 });
position({ x: 900, y: 250 }); rename('Platform');
physics({ type: 'positioned', friction: 0.8 });

// --- camera: create/frame it, then use the returned reference below ---
const playCam = add('PerspectiveCamera');
position({ x: 0, y: 900, z: 3000 });

// --- player ---
mesh('Cube', { width: 100, height: 180, depth: 100 });
position({ x: -2000, y: 90 }); color('#e0552b'); rename('Player');
rotation({ y: 90 }); // face +X (screen right) — the travel direction
physics({ friction: 0.5 }); // register the player with the physics world
const gc = addEvent('GameControl');
updateEvent(gc, {
	keyAssignments: [
		// Standard generated layout: preserve keys/order; change action codes.
		// The character faces +X (rotation above), so 'forward' (moveNegZ)
		// walks toward the goal on the right. Forward/backward only.
		['none', 'W'],
		['movePosZ', 'A'], // A = go back (screen left)
		['none', 'S'],
		['moveNegZ', 'D'], // D = go forward (screen right)
		['none', '▲'],
		['movePosZ', '◀'], // left arrow  = go back
		['none', '▼'],
		['moveNegZ', '▶'], // right arrow = go forward
		['jump', 'Space'],
		['run', '⇧'],
		['none', 'Ctrl'],
	],
	collider: {
		// explicit — centered on the mesh, same size as it (see Collider)
		type: 'capsule', height: 180, radius: 50,
		position: [0, 0, 0], rotation: [0, 0, 0],
	},
	autoOrientMove: false, // hold the fixed heading set with rotation() above
	jumpPower: 150,
	cameraXAxis: 'Locked', // keep the follow camera fixed side-on
	cameraYAxis: 'Locked',
	camera: playCam.id,
});
setPlayCamera(playCam); // same camera for follow and initial Play/export view
```

Because only forward/backward along the character's +X heading are mapped, it
can only run along the platforms and jump — depth is unreachable, which IS the
side-scroller. Frame the play camera front-on (looking down -Z) before testing
so "right" on screen is +X.

```
// Call 1 may create a visible Goal arch/flags OUTSIDE the travel lane and a
// Coin at { x: 900, y: 330 }. Then inspect get_scene/get_objects for playerId,
// coinId, groundId, winUiId and the Win UI state's id before Call 2.

// Call 2: wire the Coin with the Collision recipe above using real coinId.
// Put the non-blocking goal sensor on existing positioned Ground, not a cube
// collider across the finish line. Ground's sensor position is host-relative.
select(o => o.id === groundId);
const win = addEvent('Trigger');
updateEvent(win, {
	target: 'custom',
	triggeringObjects: [playerId],
	triggerZone: 'box',
	size: [300, 600, 600],
	position: [2600, 300, 0],
	rotation: [0, 0, 0],
	helperVisible: true,
});
const goalReveal = addAction(win, 'Transition');
updateAction(win, goalReveal.actionId, { object: winUiId });
updateTween(win, goalReveal.actionId, goalReveal.tweenId, {
	state: winUiStateId, duration: 300, easing: 'ease-out',
});
```

## Verify

`play()` starts the game (not undoable; `stop()` returns to editing). A
screenshot after `play()` shows the initial framing, the character's facing,
and whether it is standing (not sunk into or fallen through the ground) — but
you cannot press keys, so for actual movement, jumping and pickups, tell the
user the controls and ask them to confirm, ESPECIALLY that the directions
aren't inverted and the character faces its travel direction (the two most
common mistakes — see Key mapping and Facing).

Gotchas:
- Multiple GameControl events may exist, but only the page-level primary gets
  desktop/touch input; adding another does not transfer primary control.
- Movement slots are character-relative, not world axes: `moveNegZ` =
  forward along the character's heading. Aim the character at the goal, then
  bind forward/backward — never pick X/Z slots by world direction.
- Every key inverted despite a correct-looking mapping = wrong
  `forwardDirection`. `'-z'` for objects that face into the screen
  (paddle, behind-the-back camera); flip it instead of rewiring keys.
- Never keep the auto-fitted collider — set `collider` explicitly, centered
  on the mesh (`position: [0,0,0]`) and sized like it.
- `keyAssignments` / `collider` / `navmesh` are replaced whole; send every
  field. For a standard generated layout preserve all 11 entries/order/keys;
  intentionally re-key only after reading the complete current array.
- GameControl collider rotation and camera rot limits are radians; a Trigger
  zone's `rotation` is degrees (the DSL converts it).
- Collision and Trigger events only see objects that are in the physics world
  (physics enabled — and visible, when `enabled: 'visibility'`).
- The character pushes 'dynamic' props but stands on 'positioned' ones; a
  'dynamic' platform sinks under the character unless that's the point.
