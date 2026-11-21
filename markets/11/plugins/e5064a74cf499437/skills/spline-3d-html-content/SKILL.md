---
name: spline-3d-html-content
description: "HTML content over the 3D canvas (set_html_content) — the DEFAULT home of motion and behavior code (animation loops, interaction logic, game loops; headless script-only documents are fine) as well as web UI. The full injected `spline` bridge API: direct object control (updateObject), runtime creation (createObject/spawnObject/setInstanceTransforms), imported-model animation clips (getAnimations/playAnimation/pauseAnimation/stopAnimation), custom three.js/TSL shader materials (createCustomMaterial), queries, variables/events, console — plus the transparent-background + pointer-passthrough rules and Play-mode caveats. Load BEFORE writing any HTML document."
---

# HTML content over the 3D canvas

`set_html_content` attaches ONE complete HTML document to the file. The editor
renders it in a sandboxed iframe layered exactly over the 3D canvas — the user
sees your markup composited on top of the live scene (Preview tab) and the
source in the Code tab, with a Console strip capturing your `console.*` output
and errors. The document persists with the file, is undoable, and syncs to
collaborators.

This layer is the DEFAULT home of the file's MOTION and BEHAVIOR code —
animation loops, interaction logic, game loops (# Motion & interactivity;
the `animation` and `games` skills build on the API below). A document may
be HEADLESS — one `<script>` and nothing visible: leave html/body unstyled
so the page stays transparent and every pointer event passes through to the
viewport. Web UI (HUDs, dashboards, panels, forms, controls) is the other
half of its job.

The HTML SHIPS WITH EXPORTS: public URLs, `<spline-viewer>` embeds, and code
exports that run the Spline runtime all present the same HTML + 3D
composition automatically (the same `spline` bridge, with the full event
system live since exports always run in play mode). Only the three.js /
react-three-fiber exports — which don't use the Spline engine — omit it.

## The environment

- The document is standalone: your own CSS/JS goes inline, in the document.
- EXTERNAL LIBRARIES from a CDN DO work — the frame is sandboxed
  (`allow-scripts`, opaque origin, no access to the editor's DOM or cookies)
  but not cut off from the network, so `<script src="https://…">` and remote
  stylesheets load normally. Reach for a chart/animation/UI library when it
  genuinely helps; prefer inline code for small things, since every remote
  script is another thing that can fail to load at export time.
- The scene is NOT a three.js scene your script can reach into and traverse.
  Scene-level work — fracturing, physics, geometry, particles — is BUILT
  natively (CSG/booleans, particles, events) and DRIVEN through `spline.*`.
  The one three.js seam is `createCustomMaterial` (below), and it takes
  Spline's OWN bundled three namespace — a three.js you loaded from a CDN
  cannot compile there. So never tell the user external libraries are
  impossible; explain this split instead.
- KEEP THE PAGE BACKGROUND TRANSPARENT (don't set a background on html/body)
  — the 3D scene shows through everywhere you don't paint. Style your own
  panels/cards, not the page.
- Pointer events that hit the page background (html/body, or any element
  inside one marked `data-spline-passthrough`) pass through to the 3D
  viewport automatically — orbiting, selecting, and scene interactions keep
  working between your UI elements. Events on your own elements stay yours.
- A `spline` object is injected before your scripts run (also
  `window.spline`). All methods return Promises; `await spline.ready` first.

## The `spline` API

Reads:
- `spline.getVariable(name)` / `spline.getVariables()` — current values.
- `spline.findObjectByName(name)` / `spline.findObjectById(id)` /
  `spline.getAllObjects()` — snapshots: `{id, name, type, visible,
  position:{x,y,z}, rotation:{x,y,z} (degrees), scale:{x,y,z}}`. Snapshots
  carry NO geometry — vertex data reads through `getGeometry` below.
- `spline.getGeometry(nameOrId, {space?})` — a mesh's LIVE geometry, the
  read mirror of the vertex write channel: resolves `{id, name, geometry?,
  space, vertexCount, triangleCount, indexed, bounds: {min, max, size},
  vertices: Float32Array, indices?: Uint32Array, normals?: Float32Array,
  uvs?: Float32Array}` (or undefined + a console warning when the object
  is missing or has no geometry — only meshes do). Works on every mesh
  kind: parametric primitives (their real tessellation), custom meshes,
  Text glyphs, Boolean results, generated models, and spawned copies
  (their template's geometry). `space: 'local'` (default) is the mesh's
  own frame — exactly what the vertex write channel takes back, so read →
  modify → `updateObject` round-trips (fetch the base topology ONCE, keep
  it, rewrite per frame); `space: 'world'` runs vertices (and normals)
  through the world matrix — e.g. sample a terrain's surface heights to
  place or move things along the ground.

Writes:
- `spline.updateObject(nameOrId, {position?, rotation?, scale?, visible?,
  geometry?, material?})` — DIRECT object control; THIS IS THE DEFAULT
  INTEGRATION POINT. Transforms in degrees, partial axes ok. `geometry`
  overrides any parametric-geometry parameter by schema name and regenerates
  the mesh live: `{geometry: {cornerRadius: 20}}`, `{geometry: {radius: 80,
  segments: 12}}`, and on Text objects `{geometry: {text: 'Score: 42'}}`.
  CUSTOM MESHES additionally take raw data — the VERTEX CHANNEL:
  `{geometry: {vertices, normals?, uvs?, indices?}}` (flat arrays; pass
  `Float32Array` for per-frame writes). Matching topology updates the live
  GPU buffers in place, so rewriting a custom mesh's vertices every frame
  is cheap — keep vertex/index counts fixed across frames (grow by MOVING
  vertices, not adding them); ≤60k vertices. The base topology doesn't
  need recomputing in script: `getGeometry` (Reads above) returns it.
  `material` writes the mesh's material live: `{material: {color:
  '#ff4040'}}` (the color layer — CSS hex/name or {r,g,b,a?} 0..1),
  `{material: {alpha: 60}}` (material alpha 0..100), and
  `{material: {layers: [{type: 'fresnel', intensity: 2}]}}` for any layer's
  numeric/vector/color properties, addressed by `type`, `index`, or `id`
  (layer `alpha` is 0..100; shader-structural props like `noiseType` are
  skipped). Works in edit AND play mode, at 60fps (requestAnimationFrame) or
  from input handlers. Transient/runtime-only: never saved, never touches
  undo history, resets on reload — for persistent scene changes use
  run_code.
- `spline.spawnObject(templateNameOrId, {name?, position?, rotation?,
  scale?, visible?})` — create a RUNTIME-ONLY copy of a template object
  (projectiles, dynamic props, growing counts). The copy renders through
  its template (same geometry/material — restyle the TEMPLATE to restyle
  every copy), is never saved, and cannot be selected or raycast. TRS
  defaults to the template's (rotation in degrees); `visible` defaults
  true even when the template is hidden, so a hidden template works as a
  mold. Resolves to the copy's snapshot — drive it by `id` with
  `updateObject` (transforms + visible only). Budget: 500 live copies.
- `spline.destroyObject(idOrName)` — remove a spawned copy (frees its
  budget slot). Spawned copies only; hide document objects with
  `updateObject(..., {visible: false})` instead.
- `spline.setInstanceTransforms(nameOrId, transforms | null)` — per-copy
  transform writes on a CLONER, indexed by copy: each entry
  `{position?, rotation?, scale?}` (partial axes, degrees), `null` entry =
  hand that copy back to the layout, `null` instead of the array = clear
  all. One call moves every copy — THE channel for swarms, crowds, leaves,
  debris; overrides survive the cloner's own re-layouts until cleared.
  Resolves to the copy count (-1: not a cloner). `getAllObjects`/
  `findObjectByName` snapshots report a cloner's `instanceCount`.
- `spline.createObject(type, options?)` — spawn a NEW object at runtime;
  resolves to its snapshot. `type`: a shape name ('Cube', 'Sphere',
  'Torus', …, 'Text' — 'Geometry' suffix optional), 'CustomMesh' (raw
  vertex geometry — see below), 'Group', or a light ('PointLight',
  'SpotLight', 'DirectionalLight'). Options are one flat bag:
  placement (`position`/`rotation` (degrees)/`scale`, `parent`,
  `name`, `visible`), `material` (a shared material NAME from the file,
  a css color, `{color, roughness, metalness, reflectivity, alpha}`, or a
  custom shader material from `createCustomMaterial` — see below),
  `color` shorthand, and type-specific parameters (`width`,
  `cornerRadius`, `text`, `fontSize`, `intensity`, …). Anything else
  (paths, vectors, booleans, particles…) is rejected with a clear error —
  clone an existing object instead. Transient/runtime-only: never saved; in
  the editor these are Play-mode spawns removed on reset.
- `spline.createObject('CustomMesh', {vertices, indices?, normals?, uvs?,
  …options})` — build a mesh from raw geometry data, the runtime twin of
  run_code's `customMesh`: `vertices` is a flat `[x,y,z, x,y,z, …]`
  array (number[] or Float32Array, max 60000 vertices, used at REAL
  world-unit size), `indices` are triangle vertex indices (omit for a
  non-indexed, faceted-look mesh — there is no flatShading switch at
  runtime), `normals`/`uvs` optional (normals computed when omitted).
  The same winding safety net as run_code applies — inverted closed solids
  are flipped, open surfaces render double-sided — and the same
  counter-clockwise-from-outside winding rules (incl. the XZ-plane gotcha)
  from the core guidance apply. COMPUTE the arrays in script loops; this is
  how a runtime generator makes terrain, rocks, and organic shapes the
  primitives can't. After creation, MORPH it per frame through
  `updateObject`'s vertex channel (same topology — see above): create
  once, then rewrite `vertices` each frame for waves, breathing surfaces,
  melting forms.
- `spline.createCustomMaterial(factory)` — build a CUSTOM three.js/TSL
  shader material and use it via `createObject`'s `material` option. NOT
  the same thing as run_code's `createMaterial('Name')` (that saves a
  Spline layered material as a shared asset) — this one escapes the layer
  system entirely for looks the layers can't express (procedural shader
  patterns, custom lighting response, animated surface math). The factory
  receives Spline's bundled three namespace — build ONLY from it, never
  from an imported/CDN three (a separate three cannot compile here):
  ```js
  const lava = await spline.createCustomMaterial((three) => {
    const { tsl } = three; // Fn, uniform, vec3, texture, wgslFn, time, uv, positionLocal, …
    const m = new three.MeshStandardNodeMaterial();
    m.colorNode = tsl.mix(tsl.vec3(0.8, 0.1, 0), tsl.vec3(1, 0.8, 0),
      tsl.sin(tsl.time.mul(2)).mul(0.5).add(0.5));
    return m;
  });
  await spline.createObject('Sphere', { material: lava });     // reusable —
  await spline.createObject('Torus',  { material: lava, position: [200,0,0] });
  ```
  To sample an image the SCENE ALREADY SHOWS, do NOT try to load it —
  the namespace ships no `TextureLoader`, and a document image has no URL
  (one embedded on a material layer is not even a shared asset). Ask the
  scene for the live texture instead:
  ```js
  const src = await spline.getTexture('Wall');   // { texture, width, height, layer }
  const mat = await spline.createCustomMaterial((three) => {
    const m = new three.MeshStandardNodeMaterial();
    m.colorNode = three.tsl.texture(src.texture, three.tsl.uv());
    return m;
  });
  ```
  `getTexture` takes the first texture/matcap layer, or `{ layer }` to pick
  one by type/uuid, and returns null when the object has none. Same
  inline-only constraint as `createCustomMaterial`.
  Namespace: `tsl` (the full TSL function object), the NodeMaterial
  classes (`MeshStandardNodeMaterial`, `MeshPhysicalNodeMaterial`,
  `MeshBasicNodeMaterial`, …), and `Color`/vectors/texture classes/side
  + blending constants. Drive live changes through `tsl.uniform(...)`
  handles (`u.value = x` — no per-frame bridge calls) or shader-side
  `tsl.time` (zero JS per frame). Scene lights and shadows apply; Spline's
  environment reflections don't. WebGPU only (the default backend), and
  INLINE HTML-content mode only: works in the editor Preview/Play and web
  exports; SANDBOXED surfaces — `<spline-viewer>` embeds and the editor's
  legacy in-canvas play overlay — REJECT the call (their transport cannot
  carry functions or materials). That rejection is EXPECTED there, not a
  bug in your code — but unhandled it lands as a Console-strip error, so
  `try/catch` the call and fall back to a layered material (createObject's
  normal `material` bag / `updateObject`'s material channel) so the
  scene still reads; don't hang a scene's core look on it if the user
  targets viewer embeds. Prefer Spline layered materials (createObject's
  normal `material` bag / shared material names) whenever they can express
  the look — custom shaders are for what layers can't do.
- `spline.setMaterial(nameOrId, materialOrFactory)` — replace an EXISTING
  mesh's material with a custom three.js material: a `createCustomMaterial`
  result (reusable across meshes), a built-in three instance, or the factory
  itself (`spline.setMaterial('Cube', (three) => …)`). The replacement is
  pinned (states/transitions no longer restyle the mesh) and permanent for
  the session (no unset); resolves to the applied material. Same constraints
  AND rejection-handling rule as createCustomMaterial: WebGPU + inline mode
  only — sandboxed surfaces reject it, so `try/catch` with a layered
  fallback. For ordinary layered tweaks (color, alpha, layer props) keep
  using `updateObject`'s `material` channel — setMaterial is for swapping
  to shader looks the layers can't express.
- `spline.cloneObject(nameOrId, options?)` — deep-clone an EXISTING object
  (subtree included, any type — imported models too); resolves to the
  clone's snapshot. Options: `name`, `parent`, `position`,
  `rotation` (degrees), `scale`, `visible`.
- `spline.removeObject(nameOrId)` — remove an object; resolves false when
  none matched. In the editor preview only code-created objects can be
  removed (file objects throw); exported scenes can remove anything.
- `spline.setVariable(name, value)` / `spline.setVariables({...})` — set
  file variables by NAME. ONLY for scenes that already use variables (or
  when the user asks for them): values update live bindings immediately, in
  edit and play mode, without touching undo history. The variable must
  already exist (create with run_code `setVariable(...)` first). Don't
  create variables + bindings just to wire an HTML control to an object —
  `spline.updateObject` does that directly with no scene changes.
- IMPORTED MODEL ANIMATIONS — a GLB/FBX's own clips (skeletal or node
  animations; `clips:N` in the scene digest, ids/names under `clips` in
  `get_objects`) play straight from code, no events or trigger objects:
  - `spline.getAnimations(nameOrId?)` — resolves to
    `[{id, name, duration, object: {id, name}}]` (`duration` in seconds):
    the named object's clips (naming the model's group finds the animated
    object inside it), or every clip in the scene when omitted.
  - `spline.playAnimation(nameOrId, clip?, {loop?, pingpong?, fade?,
    speed?})` — play one clip by name or id (the first when omitted; the
    importer prefixes names with the file name, '<file>_<clip>', and the
    clip's own name works too). It replaces whatever that object was
    playing: `fade: 0.3` cross-fades over 0.3 s, else it cuts. `loop`:
    `true` (default) forever, `false` once — then it HOLDS the last
    frame — or a play count. Resolves to the clip; time a one-shot's
    follow-up from its `duration / speed` (e.g. a one-shot, then back to
    the loop).
  - `spline.pauseAnimation(nameOrId?, clip?)` holds clips where they are
    (`playAnimation` resumes them); `spline.stopAnimation(nameOrId?,
    clip?)` stops them on their first frame. Omit both to pause/stop every
    animated object.
  Clips play where the scene runs — Play mode, the Preview tab, exports.
  An import's own `Start` event plays the first clip a beat after the
  document boots — remove it (`removeEvent`) when code owns the clips.
  Don't ALSO drive the model's bones/parts with `updateObject` while a
  clip plays — the clip owns them.
- `spline.emitEvent(eventName, objectNameOrId)` /
  `spline.emitEventReverse(...)` — trigger events the scene ALREADY has
  authored ('mouseDown', 'keyDown', 'start', …). Interactions only RUN in
  Play mode; in edit mode the call warns in the console instead. Don't
  author new events/states just for HTML wiring.
- `spline.requestRender()` — force a redraw (rarely needed; writes do it).

Events:
- `spline.addEventListener('variableChange', ({name, value}) => {...})` —
  fires in every mode when any variable changes (your writes, the Variables
  panel, SetVariable actions...). Poll-based (~100ms).
- `spline.addEventListener('mouseDown'|'mouseUp'|'mouseHover'|'keyDown'|
  'keyUp'|'start'|'scroll'|'collision', (e) => {...})` — authored scene
  events as they fire; `e.target` is `{id, name}`. Play mode only (the
  interaction system is off while editing). This is how object-targeted
  pointer input reaches code: author the event on the object as a SENSOR
  (it needs no actions — the bridge relays the firing itself) and put the
  response here (`animation` skill's triggered-phase pattern).
- `spline.removeEventListener(name, cb)` to detach.

## Patterns that work well

- **HTML → 3D (default: direct)**: call `spline.updateObject` straight from
  input handlers or requestAnimationFrame —
  `spline.updateObject('Globe', {rotation: {y: t}})`,
  `spline.updateObject('Card', {geometry: {cornerRadius: v}})`,
  `spline.updateObject('Cube', {material: {color: picker.value}})`,
  `spline.updateObject('Score', {geometry: {text: String(points)}})`. No
  variables, no bindings, no states — the scene stays exactly as authored.
- **Truly procedural content (ship the generator, not one output)**: a
  "procedural"/"generative"/"different every time" ask means the user
  wants objects CREATED BY CODE AT RUNTIME. Write the generation algorithm
  here, built on `spline.createObject` / `spline.cloneObject`, and it
  re-runs on every load, Preview, and export — a script-only document with
  no visible UI is valid; the generator IS the app. Seed an rng (vary the
  seed per load for fresh results, fix it for stable ones), expose the
  knobs as consts — or wire them to UI controls with a Regenerate button
  (`spline.removeObject` the last batch, rebuild). A run_code loop would
  bake ONE frozen output into the tree — that's authoring, not procedural
  behavior. The same verbs cover one-object-per-datum live data and any
  DISTINCT generated object; repeated copies of ONE template (bullets,
  obstacles, collectibles) are `spawnObject`'s job instead — cheaper,
  they render through the template. Cap live counts and remove what
  leaves play so long sessions don't accumulate
  objects. `createObject` builds primitives/Text/Group/lights with full
  geometry params AND raw vertex meshes ('CustomMesh' — compute
  vertices/indices in script; runtime terrain, rocks, and organic shapes
  are fully possible); for complex looks (imported models, tuned material
  stacks, particles) author ONE template in the scene with run_code and
  `cloneObject` it with per-instance variation. What stays authored with
  run_code: the tuned DSL generators (`terrain()`/`ocean()`/`tree()`
  algorithms aren't callable from the bridge — hand-roll the vertex math
  or clone an authored result), decals, particles, paths/vectors.
- **HTML → 3D (only when asked / already wired)**: if the user wants
  variables (persistence across the file's logic, Variables panel control,
  scene actions reading the value) or the scene already binds properties to
  variables, drive those with `spline.setVariable` — creating them with
  run_code `setVariable(...)` + `bindVariable(...)` first (see the
  interactivity skill). Don't introduce this layer on your own initiative.
- **3D → HTML**: poll object snapshots (`findObjectByName`) or — in scenes
  that use variables — `spline.addEventListener('variableChange', ...)` to
  mirror scene state into your UI; object click/hover reactions via the
  spline event listeners in Play mode.
- **Layout**: position UI with fixed/absolute CSS against the full viewport —
  the iframe covers the canvas exactly. Keep interactive HTML compact so the
  3D stays reachable; large decorative regions should carry
  `data-spline-passthrough` so they don't swallow scene input.
- **Motion & animation**: THE default home of every animation — a headless
  rAF loop computing poses from elapsed time and writing them with
  `updateObject` (growth, orbits, ambient life, triggered reactions). The
  `animation` skill carries the recipes (clock, easing, stagger,
  entrance → idle) — load it for any motion work.
- **Games**: this layer is the DEFAULT home of a game's loop, keyboard input,
  procedural WebAudio sound and start/HUD/game-over UI — the `games` skill
  builds on the API above (load it for the game shell, chase-camera,
  movement and sound recipes).
- **Anything driven per-frame must move SMOOTHLY** — the `games` skill's
  smooth-motion rules apply to every interactive scene, not just games:
  integrate with a fixed timestep (never the raw frame delta) and write
  low-passed values; never bolt a camera to a moving object
  (`position = target − offset` buzzes — separate updateObject writes can
  land a frame apart; ease toward the target and aim AT it); throttle
  continuously-updating DOM text to ~10 Hz.
- Debug with `console.log` — the user sees it in the Console strip.

## Rules

- DEFAULT TO DIRECT CONTROL: wire HTML to the scene with
  `spline.updateObject` (and reads). Do NOT create variables, bindings,
  states, or events just to connect an HTML control — that adds scene
  complexity the user didn't ask for. Reach for variables/events only when
  the user requests them, the scene already uses them, or something outside
  the HTML (actions, states, exports reading variables) must see the value.
  (The one authored-event exception: an action-less SENSOR event that
  bridges object clicks/hovers into code — see the listener note above.)
- ONE document per file. `set_html_content` creates or fully rewrites it;
  to CHANGE an existing document, `get_html_content` to read the current
  source, then use `edit_html_content` with ONE `edits` batch carrying
  every change you can already spell out (exact `old_str` → `new_str`
  find-and-replace each, `replace_all` for repeated strings) instead of
  resending the whole document — or one call per edit.
- Empty string to `set_html_content` removes the HTML content entirely.
- Don't duplicate the 3D scene in HTML (no WebGL canvases of your own) — the
  scene is behind you; you're the UI layer.
- If you do use variables, they must exist in the file: create/verify them
  with run_code in the same response before shipping HTML that uses them.
- `updateObject` is transient (runtime state, not saved). That's right for
  interactive controls; if the user wants a control that permanently edits
  the file, say so and apply the final value with run_code instead.
- Test-drive interactions mentally against edit mode (updateObject +
  variables work; authored events need Play) and say so to the user when a
  piece of the HTML app only comes alive in Play mode.

## Minimal example (direct control — no variables)

```html
<!doctype html>
<html>
<head>
<style>
  /* page background stays transparent */
  .hud { position: fixed; top: 16px; left: 16px; padding: 12px 16px;
         background: rgba(20,20,24,.85); color: #fff; border-radius: 12px;
         font: 13px/1.4 system-ui; }
  input[type=range] { width: 160px; }
</style>
</head>
<body>
  <div class="hud">
    <div>Spin: <span id="sv">20</span>°/s &nbsp; Rounding: <span id="rv">0</span></div>
    <input id="s" type="range" min="0" max="180" step="1" value="20">
    <input id="r" type="range" min="0" max="45" step="1" value="0">
  </div>
  <script>
    (async () => {
      await spline.ready;
      const s = document.getElementById('s'), r = document.getElementById('r');
      // Continuous motion: drive the transform directly every frame.
      let angle = 0, last = performance.now();
      (function tick(now) {
        angle += ((now - last) / 1000) * Number(s.value); last = now;
        spline.updateObject('Cube', { rotation: { y: angle } });
        requestAnimationFrame(tick);
      })(last);
      s.addEventListener('input', () => { sv.textContent = s.value; });
      // Shape control: geometry parameters regenerate the mesh live.
      r.addEventListener('input', () => {
        rv.textContent = r.value;
        spline.updateObject('Cube', { geometry: { cornerRadius: Number(r.value) } });
      });
    })();
  </script>
</body>
</html>
```
