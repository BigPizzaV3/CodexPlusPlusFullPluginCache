---
name: spline-3d-games
description: "DEFAULT recipe for playable games and game-like scenes: plain JS code logic in the HTML layer (set_html_content + the spline bridge) — start-screen gate, HUD, keyboard input, a rAF game loop, a glitch-free chase camera, JS collision checks — with the scene built by run_code and sound recipes in game-audio. The built-in Game Controls feature is OPT-IN only (load game-controls when the user explicitly asks for it)."
---

# Games (JS game loop + HTML UI)

Games and game-like scenes are CODE-DRIVEN BY DEFAULT: the world is authored
with `run_code`, and ALL gameplay — input, movement, camera, collisions,
score, win/lose — is plain JavaScript living in the file's HTML layer
(`set_html_content`), driving objects through the `spline` bridge at 60fps.

Do NOT reach for the engine's game machinery unless asked:

- The built-in Game Controls feature (the `GameControl` event) is OPT-IN:
  use it ONLY when the user explicitly asks for it (says "game controls",
  wants the editor's built-in character controller, touch joysticks, or a
  navmesh). Then load the `game-controls` skill and follow it instead of
  the loop recipe here. Never mix both movement systems on one player.
- Engine physics (`physics()` + Collision/Trigger events) is for
  physics-driven scenes, not for the core loop of a code-driven game: the
  bridge's per-frame writes are transform teleports the simulation cannot
  see. Do the gameplay collision math in JS (below). Decorative physics on
  objects the code never moves is fine.
- No engine KeyDown/Start events for game logic either — the HTML document
  handles its own input and boot.

Why this is the default: a JS loop gives conventional game feel (proper
chase camera, smooth steering, instant restart), real UI (start screen,
HUD, game-over), procedural sound (WebAudio synthesis — no audio assets),
and one debuggable place for all the rules — and the same document ships
with exports (public URLs, viewer embeds, runtime code exports), where the
identical `spline` bridge is injected.

Load the `html-content` skill alongside this one for the full bridge API
(`updateObject`, snapshots, transparent-background and passthrough rules).

## Layer 1 — the scene (run_code)

Build the world exactly like any scene (`buildingScenes` conventions),
plus these game rules:

- **Game actors live at the page ROOT, not inside groups — the play camera
  included.** The bridge reads/writes LOCAL transforms; at the root,
  local == world and the math below just works. (A generated character
  wrapped in a facing-fix group is fine — the GROUP is then the root-level
  actor the code drives.)
- **Stable, unique names** — `'Player'`, `'CamRig'`, `'ChaseCam'`,
  `'Coin 1'`… The game code finds objects by these names at boot, then
  drives them BY ID (name lookup traverses the whole scene).
- **The player's visual front faces its +Z side** (where Spline meshes and
  imports face when created). The movement recipes assume heading θ ⇒
  forward = (sin θ, 0, cos θ) with `rotation.y = θ`. If a generated model
  leads with another side, nest the mesh in a group, pre-rotate the MESH
  inside so the GROUP's +Z is the front, keep the group at the root, and
  drive the group (the full recipe: "When the generated model lands"
  below).
- **Ground EVERY actor at its contact patch — player, rivals, props.**
  Cars that spawn inside the floor are the top game-breaker, and it hits
  the whole grid, not just the hero. Two rules make it impossible:
  1. Every actor group's origin IS its contact patch: offset the meshes
     inside so wheels/feet sit at group-local y = 0. Generated models
     need this explicitly — they arrive with ARBITRARY pivots (a
     centered pivot sinks half the car); primitive rivals need their
     wheels/body built above local 0, not centered on it.
  2. ONE shared height constant, used everywhere:
     `const SURFACE_Y = 4;` (the TOP of the asphalt per the height
     layering below — never 0, which is the ground plane). The build
     places every car at `y: SURFACE_Y`; the drive loops either never
     write y or write exactly `SURFACE_Y` — never a recomputed value.
  Verify with a low, close screenshot of the START GRID: every car's
  wheels touching, none buried, none floating.
- **When the hero replaces a placeholder, the placeholder DIES.**
  `remove()` it, then give the hero's wrapper the placeholder's exact
  name — the scene must end with exactly ONE object of that name. Two
  objects sharing 'Player' means `findObjectByName` picks one
  arbitrarily: the loop drives the hidden/leftover one while the visible
  car sits still at the grid.
- **Generate the hero with the AI mesh tool.** Grey primitives make a game
  look like a prototype, so reach for `generate_3d_model` PROACTIVELY for
  the thing the scene is about — the car, the runner, the ship — starting
  with the player. 1 generation is the target, 2 when a secondary subject
  earns it, 3 is the hard maximum (do NOT generate more than 3 unless the
  user explicitly asks). Kick the hero generation off FIRST — it returns
  immediately and bakes in the background — then build ground, props,
  camera and UI while it bakes. The finished model arrives selected, at the
  build anchor: in the app it is handed back to you before the request ends,
  while over MCP the call returns a `job_id` and you collect the result by
  polling `get_generation` (it will not arrive on its own). That's when
  you rename it, fix its facing, and wire it into the loop. Everything
  else — ground, track, walls, pickups — is primitives via `run_code`.

### When the generated model lands — the swap procedure

The completion report ("finished and inserted") is the START of the swap, not
the end: generated meshes arrive at the build anchor with ARBITRARY authored
facing, scale, and pivot. Dropped in raw, the car rides sideways down the
straight, sits buried or afloat, and is scaled to nothing the track was
derived from. And the one place a facing fix must NOT go is the driven
object itself: the loop's `updateObject` writes ABSOLUTE rotations every
frame, so a yaw correction on the driven root is erased on the first tick
— it has to be baked one level DOWN. In order:

1. **Measure it**: `get_scene` → the inserted object's `size`
   [w, h, d] (world bbox — fresh inserts are unrotated, so this is the
   authored box).
2. **Scale to the anchor size, uniformly**: for a car
   `scale({ x: k, y: k, z: k })` with
   `k = CAR.length / Math.max(w, d)` — the long edge must match the
   length the world was sized from, never whatever the generator chose.
3. **Wrap it**: `group()` the mesh — the GROUP is the actor the loop
   drives. Then set the mesh's LOCAL transform inside DELIBERATELY
   (`position({ x: 0, y: h/2, z: 0 })` — scaled h; a centered pivot is
   the common case and h/2 rests the wheels at group-local 0). Never
   trust whatever offsets the wrap left behind.
4. **Yaw the MESH so the group's +Z is the nose.** The measured bbox
   names the long AXIS (length on x ⇒ start with
   `rotation({ y: 90 })`), but a bbox cannot tell nose from tail:
   `take_screenshot`, look at the nose, add 180 if it points backwards.
   90° multiples only — anything else drives skewed forever.
5. **Place the group at the placeholder's slot**: rotation { 0, 0, 0 },
   position { grid x, y: SURFACE_Y, z: grid z }.
6. **The placeholder DIES and the group takes its exact name**:
   `remove()` the placeholder, then `rename()` the group — exactly one
   'Player' in the scene (the loop's boot lookup must have one answer).
7. **Prove it with a screenshot** — low, close, from behind the grid:
   nose pointing along the group's +Z, wheels touching the asphalt, car
   about a third of the track width. Fix it HERE, before play — not
   after the user watches it drive sideways.

Rivals cloned from the hero inherit the calibration with the wrapper —
`clone` the GROUP, never the bare mesh inside.

### World scale & trackside props (every prop, every game)

- **Anchor every size to the player.** Pick the player's size first (a
  stylized car ~340–450 units long, a character ~180–220 tall; 200 units
  = 1 m), then derive the rest: a racing track 3–4 car widths across,
  curbs ~40 wide, barriers ~60 tall, a tire ~110 across. A decorative
  prop bigger than the player is almost always a bug.
- **Prop sizes are named CONSTANTS; loop math is for POSITIONS only.**
  When placing props along a track/curve, the loop computes where each
  one goes — never how big it is. Deriving a size from curve/track
  variables is how circuits end up buried under 5,000-unit cylinders:
  ```
  const TIRE = { radius: 55, height: 40 };           // fixed, up front
  for (let i = 0; i < corner.length; i++) {
    mesh('Cylinder', { radius: TIRE.radius, height: TIRE.height,
      hollow: 0.4 });
    position({ x: corner[i].x, y: TIRE.height / 2, z: corner[i].z });
    rename('TireStack ' + (i + 1));                  // position from the
  }                                                  // loop, size never
  ```
- **`hollow` is a FRACTION, 0..1.** `hollow: 0.4` = a tire with a 40%
  opening; `hollow: 40` is out of range (the classic percent mistake —
  it used to inflate each tire into a scene-swallowing lens; the engine
  now clamps it, but the tire renders wrong). Same rule for every 0..1
  geometry fraction.
- **Keep counts low, grouped, and off the racing line.** A handful of
  tire stacks (1–2 tall) at the OUTSIDE of hard corners, a few dozen
  trees/props total — each family in a named group ('Tire Walls',
  'Trees'). Hundreds of decorative meshes add cost, not looks.
- **Light size covers the play area.** A directional light's shadows
  exist only inside its `size` footprint (default 2000 world units);
  tracks, courts, and arenas span far more, and shadows cut off
  mid-track. Give the key light `size: 4000` or more, matched to the
  ground/track span (e.g. `size: 9000` for a 9000-unit ground).
- **Verify the layout from above before wiring gameplay**: frame a
  top-down screenshot and CHECK — every prop reads smaller than the
  player, nothing overflows the track or the ground plane. A group of
  giant discs/blobs swallowing the scene means a size came from loop
  math: delete that group and rebuild it from the constants.

### Track ribbons — no self-overlap (racing circuits)

The classic circuit failure: a track built from overlapping planks folds
into itself at hairpins — inner edges cross, coplanar faces z-fight (dark
smudges on the asphalt), stray kerb arcs cut across the road. Three rules
prevent all of it:

- **Corner radius ≥ track width, everywhere.** The inner edge's radius is
  `centerRadius - width / 2`; as it nears zero the ribbon folds over
  itself. Keep every corner's CENTERLINE radius at least the track width
  (1.5x reads better) — tighten a hairpin by narrowing the track or
  widening the arc, never by dropping the radius below the width.
- **The asphalt is ONE ribbon mesh, never overlapping segments.** Sample
  a smooth closed centerline, offset each sample left/right by half the
  width, and stitch a single `customMesh` — exact joints, zero overlap:

  ```
  const N = 96, W = 900;                       // samples, track width
  const cx = (t) => Math.sin(t * 2 * Math.PI) * 2600;   // centerline x(t)
  const cz = (t) => Math.cos(t * 2 * Math.PI) * 1700;   // centerline z(t)
  const verts = [], idx = [];
  for (let i = 0; i < N; i++) {
    const t = i / N, e = 1e-3;
    const x = cx(t), z = cz(t);
    const dx = cx(t + e) - x, dz = cz(t + e) - z;        // tangent
    const len = Math.hypot(dx, dz);
    const nx = -dz / len, nz = dx / len;                 // left normal
    verts.push(x + (nx * W) / 2, 0, z + (nz * W) / 2);   // left edge
    verts.push(x - (nx * W) / 2, 0, z - (nz * W) / 2);   // right edge
  }
  for (let i = 0; i < N; i++) {
    const a = i * 2, b = a + 1;
    const c = ((i + 1) % N) * 2, d = c + 1;
    idx.push(a, c, b, b, c, d);   // two up-facing triangles per quad
  }
  customMesh({ vertices: verts, indices: idx });
  position({ y: 2 }); color('#2a2d33'); rename('Track Asphalt');
  // (reversed travel direction? if the ribbon renders dark from above,
  // swap each triangle's last two indices)
  ```

  Kerbs and barriers are the SAME recipe at offset `±(W / 2 + margin)`
  with a narrow width — they follow the track exactly instead of
  overshooting into it. Curve-following geometry comes from this ribbon
  math; boxes are for straights and props only.
- **Nothing lies coplanar with the asphalt.** Stack by a few units:
  ground at y = 0, asphalt at ~y = 2, kerbs a step above the asphalt,
  painted marks (start line, arrows) a step above that. Two faces at the
  SAME height z-fight as flickering smudges at any distance.

## Layer 2 — the chase camera (get this right)

Three hard rules, each one fixing a real failure mode:

1. **The play camera lives at the page ROOT — NEVER inside a group.**
   Parts of the play pipeline treat the camera transform as world-space; a
   play camera nested in a group/rig comes up mis-aimed from the first
   frame (staring at the sky instead of the player).
2. **Turn the play-mode camera controls off: `playControls('none')`.**
   While any of orbit rotate/pan/zoom is enabled (the file default), play
   mode attaches orbit controls to the play camera: they re-aim it at
   their own fixed target on every update and flip its up vector when the
   camera passes over that point — the "camera somersaults / gimbal-locks
   and loses the player" bug. Code driving the play camera must be its
   ONLY driver. Skip this only for a static camera the user SHOULD orbit.
3. **Never hand-write a rotation that both yaws and pitches.** Entity
   Euler order is XYZ, so `{ x: pitch, y: yaw }` tilts sideways and flips
   as the heading turns. Aim cameras through `aimEuler` (below) — exact
   at every heading — and always write ALL THREE axes it returns.

Scene side (run_code): author the camera at the root, aim it with the same
math the loop will use (`aimEuler` is built into run_code — call it
directly), and hand it to Play:

```
// player at (px, py, pz), heading playerYaw degrees (0 = facing +Z)
const cam = add('PerspectiveCamera');
rename('ChaseCam');
const pr = playerYaw * Math.PI / 180;
position({ x: px - Math.sin(pr) * 720,
           y: py + 320,
           z: pz - Math.cos(pr) * 720 }); // above & behind the player
rotation(aimEuler(playerYaw, -12));      // look the way the player faces
setPlayCamera(cam);      // Play + exports render through it
playControls('none');    // the game code is the ONLY camera driver
```

Runtime (in the loop): EASE the camera toward its chase point and AIM it
AT the player every frame. Never bolt it —
`position = player − offset` written verbatim is the #1 cause of the
car "buzzing/trembling in place" at speed: the player and camera are two
separate `updateObject` writes that do not always land in the same
render frame, and a bolted camera turns that one-frame skew into
screen-space vibration (the car's screen position is the DIFFERENCE of
the two). Exponential easing spreads the skew across frames, and aiming
at the player keeps it dead-centre no matter how the writes interleave:

```
// chase point behind the player's heading (px/pz/playerYaw = ON-SCREEN state)
const pr = playerYaw * Math.PI / 180;
const gx = px - Math.sin(pr) * 720, gz = pz - Math.cos(pr) * 720;
cx = damp(cx, gx, 6, dt); cy = damp(cy, py + 320, 6, dt);
cz = damp(cz, gz, 6, dt);
// aim AT the player (a point at roof height), not along a stored heading
const dx = px - cx, dy = (py + 120) - cy, dz = pz - cz;
spline.updateObject(camId, {
  position: { x: cx, y: cy, z: cz },
  rotation: aimEuler(Math.atan2(dx, dz) * 180 / Math.PI,
                     Math.atan2(dy, Math.hypot(dx, dz)) * 180 / Math.PI),
});
```

Seed `cx/cy/cz` at the chase point on reset (snap, don't ease, or the
camera swoops in from wherever it last was).

Camera variants:
- **Racing / third-person chase**: the recipe above — distance 600–900,
  height 250–400 (the aim pitch lands around −10…−16° by construction).
  Position ease rate 5–8: the camera trails the chase point by roughly
  speed/rate units at full speed — tighten the rate, never bolt.
- **First-person**: position = player position + eye height (~160),
  rotation = `aimEuler(playerYaw, pitch)`, no easing. Hide the player
  mesh (`visible: false`) or mount the camera just ahead of its face.
  Mouse-look: accumulate yaw/pitch from `movementX/Y` after
  `stage.requestPointerLock()` on click (the iframe sandbox allows it);
  clamp pitch to about ±80°.
- **Fixed-angle (side-scroller, top-down, isometric)**: author the
  orientation once with `rotation(...)`; at runtime only LERP the
  position after the player — never rotate it. `playControls('none')`
  still applies whenever the code moves the camera.

## Layer 3 — the game shell (set_html_content)

ONE complete HTML document over the canvas. Non-negotiables:

- **The game waits for the user.** Boot into a start screen — title, one
  line of controls, a Start button — and run gameplay only after the user
  clicks Start (state machine `'menu' → 'playing' → 'over'`). NEVER
  auto-start on load: the scene must stay still until asked. The click is
  also what puts keyboard focus inside the HTML document AND
  creates/unlocks the AudioContext (see Procedural sound effects).
- **A full-viewport input layer**: `<div id="stage" style="position:fixed;
  inset:0"></div>` as the bottom layer, WITHOUT
  `data-spline-passthrough`. Pointer/wheel events that land on it stay in
  the document — keyboard focus stays here too — instead of forwarding to
  the 3D canvas. (Camera safety itself comes from `playControls('none')`
  in Layer 2; the layer keeps stray drags/scrolls from poking the scene,
  and is where pointer-lock mouse-look attaches.) Omit it only when the
  game deliberately lets the user orbit a static play camera.
- **Keyboard state, not keydown bursts**: track held keys in a Set from
  `keydown`/`keyup` (`e.code`), `preventDefault()` the game keys, and
  read the Set inside the loop. Ignore `e.repeat` for one-shot actions
  (jump, restart).
- **Pause when focus leaves the document.** Keys only reach the game
  while ITS document has focus — and entering Play from the toolbar (or
  tabbing away, or clicking editor chrome) moves focus OUTSIDE it,
  leaving a 'playing' game deaf to every key ("the car won't move"). On
  window `blur`: clear the held-keys set (or keys stick down forever)
  and drop to a `'paused'` overlay; its Resume click returns focus and
  input in one gesture.
- **One requestAnimationFrame loop, FIXED sim timestep.** Start it once
  at boot and never stop it; integrate only while `state === 'playing'`.
  Never integrate physics with the raw frame delta — every hitch changes
  the step size and the car lurches. Accumulate the (clamped) delta and
  step the sim in fixed slices, then write the scene a LOW-PASSED copy
  of the sim state so a dropped frame cannot produce a jump:
  ```
  const STEP = 1 / 120; let acc = 0;
  // per frame: dt = Math.min((now - last) / 1000, 0.05)
  acc += dt;
  while (acc >= STEP) { simulate(STEP); acc -= STEP; }
  vx = damp(vx, x, 25, dt); vz = damp(vz, z, 25, dt);   // visual state
  vyaw = dampAngle(vyaw, yaw, 25, dt);                  // what gets WRITTEN
  ```
  Transforms go out as fire-and-forget `spline.updateObject(id, …)` (no
  await in the loop), ONE write per actor per frame, built from the
  visual (`v*`) state — the camera chases and aims at that same visual
  state, so everything on screen agrees.
- **Boot reads, then cached ids**: `await spline.ready`, snapshot the
  actors once (`findObjectByName` / `getAllObjects` — positions in world
  units, rotations in DEGREES), keep their ids and initial transforms in
  JS. The loop never reads the scene back — JS state is the source of
  truth. If a required lookup comes back null (an object renamed or
  missing), say so on the start screen and stop — a silent null throws
  in the first tick and freezes every car.
- **Restart rebuilds from the snapshots**: restore every actor's initial
  transform and visibility with `updateObject`, reset score/timers, back
  to `'playing'` (bind it to the game-over button and the R key). Bridge
  writes are transient (never saved, gone on reload), so restoring
  snapshots is all a restart takes.
- **HUD is HTML — and throttled.** Score, lap, speed, time live in styled
  fixed-position elements. Event-driven values (score, lap) update when
  they change; continuously-changing readouts (speed, timers) update at
  ~10 Hz, never every frame — writing DOM text 60×/s adds main-thread
  hitches that read as scene jitter. Don't build 3D text scoreboards
  unless asked. Keep the page background TRANSPARENT (style your panels,
  never html/body) so the scene shows through.

## Movement + camera math (drop-in helpers)

Framerate-independent smoothing, and the SHORTEST-ARC angle damp — easing
yaw with a plain lerp is what makes cameras spin the long way around and
glitch when steering flips the sign (the classic 350°→10° bug):

```
const wrap = (d) => ((d + 540) % 360) - 180;  // any delta → [-180, 180]
const damp = (a, b, rate, dt) => a + (b - a) * (1 - Math.exp(-rate * dt));
const dampAngle = (a, b, rate, dt) => a + wrap(b - a) * (1 - Math.exp(-rate * dt));
```

`aimEuler` — THE way to point a camera. It converts "look along world
heading `yawDeg`, tilted by `pitchDeg`" (same heading convention as the
player: 0° looks toward +Z; pitch < 0 looks down) into the XYZ-order Euler
the bridge expects. Smooth yaw/pitch BEFORE converting; never smooth,
partially write, or hand-edit its outputs. It is BUILT INTO run_code; in
browser game-loop code (which runs outside run_code) define this exact
copy inline:

```
function aimEuler(yawDeg, pitchDeg) {
  const y = (yawDeg + 180) * Math.PI / 180; // camera bodies look down -Z
  const p = pitchDeg * Math.PI / 180;
  const cy = Math.cos(y), sy = Math.sin(y);
  const cp = Math.cos(p), sp = Math.sin(p);
  const r2d = 180 / Math.PI;
  // R = Ry(yaw) * Rx(pitch), decomposed into the entity's XYZ order
  return {
    x: Math.atan2(sp, cy * cp) * r2d,
    y: Math.asin(sy * cp) * r2d,
    z: Math.atan2(-sy * sp, cy) * r2d,
  };
}
```

Keep chase cameras tilted (−8° or steeper): it frames the road ahead, and
a perfectly level camera looking exactly along ±X sits on the conversion's
branch point (harmless — the values stay correct — but the tilt keeps the
numbers tame).

Heading convention (matches the scene rules above): `yaw` in degrees,
`rotation.y = yaw`, forward = `(sin yaw°, 0, cos yaw°)` — so
`x += Math.sin(rad) * speed * dt; z += Math.cos(rad) * speed * dt`.

- **Car**: throttle/brake accelerate `speed`, exponential drag
  (`speed *= Math.exp(-DRAG * dt)`), clamp to top speeds, and scale
  steering BY SPEED — `yaw += steer * STEER_DEG * (speed / TOP) * dt` — so
  the car can't pivot in place and reversing counter-steers naturally
  (steer: A/← = +1, D/→ = −1; positive yaw turns left on screen).
- **Boundary flags get hysteresis.** Any boolean derived from a
  continuous quantity — off-track/on-grass, inside a boost zone,
  grounded — flips on and off EVERY frame while the car rides its edge,
  and whatever is keyed to it (a top-speed cap, extra friction) snaps
  with it: visible stutter at the track border. Use two thresholds (go
  off beyond edge + 25, come back inside edge − 25) or require the state
  to hold for ~0.1 s before it takes effect — never a single `>=` test.
  While the flag is on, apply its effect as a RATE (extra drag), not an
  instant clamp to a lower cap.
- **Third-person character**: camera-relative input —
  `wx = iz * sin(camRad) - ix * cos(camRad)`,
  `wz = iz * cos(camRad) + ix * sin(camRad)` (ix: D=+1/A=−1, iz: W=+1/S=−1),
  then face the travel direction `yaw = dampAngle(yaw,
  atan2(wx, wz) * 180 / Math.PI, 12, dt)` and move along (wx, wz).
- **Jumping**: keep `vy`; `vy -= G * dt; y += vy * dt`; land when
  `y <= groundY` (reset y, vy, grounded). ~200 units = 1 m, so G ≈ 4000
  u/s² and jump velocity ≈ 1300 u/s feel right; only jump when grounded
  and `!e.repeat`.
- **Collisions are plain JS — 2D tests, depenetrating responses.**
  Pickups/enemies by distance — `Math.hypot(o.x - x, o.z - z) < r`;
  walls/barriers as AABBs; a goal as a distance or box test → `'over'`.
  Collect the lists ONCE at boot from `getAllObjects()` by name prefix.
  Three rules keep collision code from freezing (or shaking) the game:
  - Tests compare **x/z only — never y**. Ground games play in 2D; a
    height mistake anywhere must not register as "inside a wall".
  - Responses **depenetrate, never veto**: on overlap, push the car out
    along the shallowest axis (or slide it along the wall) and keep
    going. Code shaped as "if the next position overlaps, cancel the
    move" turns ANY overlap — a bad spawn, a deep hit, a car inside the
    floor — into a permanently frozen car: every attempted move is
    rejected, forever. A car that starts intersecting geometry must
    drive out of it, not lock up.
  - **Push path-driven actors through their STATE, never their x/z.** A
    rival that recomputes its position from a racing line every frame
    snaps back the same tick you move it — so the push-apart repeats
    forever and both cars shake. Give every path follower a persistent
    lateral offset it ADDS to the line each frame (decaying back to 0
    over ~a second), and write the push into that offset — the rival
    then actually gives way.

## Procedural sound effects (WebAudio — on by default)

Games ship with sound ON BY DEFAULT — procedural WebAudio synthesis, no
audio assets. Load the `game-audio` skill for the synth helpers and the
per-effect recipes (engine, weapons, footsteps, pickups, win/lose) before
writing the sound code; the shell recipe above already reserves the mute
button and the AudioContext resume-on-first-command wiring it teaches.

## Worked example

Building a NEW game (or your first in this session)? Load the
`game-example` skill: a complete drive-&-collect game — scene call, full
HTML document (input, loop, chase camera, collisions, HUD, restart) — that
instantiates every rule above. Editing an existing game usually doesn't
need it; the layer contracts and math above are the reference.

## Verify

- `play()` then a screenshot shows the INITIAL framing through the play
  camera — the player seen from behind, above, both in frame, and EVERY
  car on the grid resting ON the surface. Any car sunk into the floor or
  floating = wrong contact-patch offset or resting height — fix the mesh's
  local y inside that car's group and the shared `SURFACE_Y`, before
  wiring anything else. Screenshots capture the 3D canvas ONLY: the
  HTML start screen/HUD is never in them, so verify the document through
  the Console strip (`console.log` + errors surface there) and by
  telling the user what they should see.
- You cannot press keys, click Start, or hear audio yourself: tell the
  user the controls and ask them to confirm — ESPECIALLY that steering
  isn't inverted, the camera stays smoothly behind the player while
  turning (no long-way spins), the player holds steady on screen at TOP
  speed (buzzing/trembling in place = a bolted camera or raw-dt
  integration — the smooth-motion rules above), the game waits on the
  start screen until they click Start, and the sound effects play after
  Start.
- The document also runs on the stage's Preview tab, but through the
  EDITOR camera — the chase camera is only the view in Play mode and
  exports. The Edit tab unmounts it so the scene stays editable.
- `stop()` when you're done testing. The preview reload chip (and a fresh
  Play) restores every transient bridge write.

Gotchas:
- The play camera: at the page ROOT (never inside a group) and with
  `playControls('none')` whenever code drives it. A grouped play camera
  comes up mis-aimed; live play orbit controls re-aim and up-flip a driven
  camera (the somersault/gimbal-lock bug).
- Hand-written yaw+pitch rotations tilt sideways as the heading turns (XYZ
  Euler order): aim cameras with `aimEuler`, write all three axes it
  returns, and smooth the yaw/pitch INPUTS — never its outputs.
- The player buzzing/trembling IN PLACE at speed = a camera bolted to
  `player − offset`: the two writes land a frame apart and the skew
  shows as vibration. Ease the camera toward the chase point and aim it
  AT the player every frame (Layer 2).
- The car lurching on frame hitches = integrating with the raw frame
  delta. Fixed `STEP` with an accumulator; the scene gets a low-passed
  copy of the sim.
- Speed (or friction) snapping at the track edge = a boundary flag
  flipping every frame. Hysteresis: two thresholds or a hold time, and
  rate-based effects instead of instant caps.
- Two AI cars (or you and a rival) shoving each other forever = the
  push-apart wrote the rival's x/z while its path-follower recomputed
  them the same frame. Push into the follower's lateral-offset state.
- HUD text written every frame (60×/s DOM writes) = main-thread hitches
  that LOOK like scene jitter. Event-driven values update on change;
  continuous readouts at ~10 Hz.
- Smoothing angles with a plain lerp = the long-way-around spin. Wrap the
  delta to [-180, 180] first (`dampAngle`).
- Bridge transforms are LOCAL and rotations are DEGREES, both ways. Keep
  driven actors at the page root.
- Keep the #stage input layer even with play controls off — it holds
  keyboard focus in the document and keeps stray drags from raycasting
  the scene.
- `set_html_content` writes the whole document; to tweak an existing one,
  `get_html_content` then `edit_html_content` (find-and-replace) instead
  of resending it. `updateObject` by cached id, not by name, in the loop.
- `spline.addEventListener('mouseDown'…)` fires only for events the SCENE
  authors and only in Play — a code-driven game doesn't need it; handle
  input in the document.
- Audio before a user gesture is blocked: create/resume the AudioContext
  in the Start click, never at boot — and never try to fetch sound files
  (the sandbox has no guaranteed network; synthesize instead).
- Two objects named 'Player' (a kept placeholder + the generated hero) =
  the loop drives one arbitrarily while the other sits at the grid.
  `remove()` the placeholder the moment the hero replaces it.
- A generated hero that drives SIDEWAYS = the facing fix went on the
  driven root, where the loop's absolute rotation writes erase it every
  frame. Bake the yaw on the mesh INSIDE the group (swap procedure), and
  verify the nose with a screenshot — the bbox can't tell front from
  back.
- ANY car inside the floor (or floating) = wrong pivot or wrong resting
  height: contact patch at group-local y = 0 and one shared SURFACE_Y
  for the whole grid. Sunk cars also jam veto-style collision checks —
  the buried-AND-frozen combo. Depenetrate; never cancel moves on
  overlap.
- A thrown error inside the rAF tick kills the whole game silently —
  every car frozen. Guard optional lookups and read the Console strip.
- The user asked for the built-in controller/joysticks/navmesh? That's the
  `game-controls` skill (GameControl event) — not this loop, never both
  on one player.
