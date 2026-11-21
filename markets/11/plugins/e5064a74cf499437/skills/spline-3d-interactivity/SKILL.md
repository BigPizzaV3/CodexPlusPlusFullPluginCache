---
name: spline-3d-interactivity
description: "The built-in Events & Actions machinery — for EDITING interactivity a scene already has, for features only events provide (Scroll/Collision/Trigger/DragDrop/LookAt/Follow, variables + property bindings), for sensor events bridging clicks/hovers into code, and for explicit user asks. NEW interactive behavior is code-driven by default (the `animation` skill + the spline bridge). Covers event/action types, creating and editing them (updateEvent/updateAction/updateTween/remove*), states, variables (basic + dynamic), and inspecting existing interactivity via get_objects."
---

# Interactivity (Events & Actions)

NEW interactive BEHAVIOR is code-driven by default — logic and motion live
in the HTML layer, driving objects through the `spline` bridge (see
# Motion & interactivity and the `animation` skill; games have their own
skill). This machinery is what you load when:

- the user EXPLICITLY asks for events, actions, states, or variables;
- you are EDITING interactivity a scene ALREADY has (fixes and small
  additions stay in kind — never migrate working content to code unasked);
- a feature only events provide is genuinely needed: Scroll-driven
  narratives, physics `Collision`/`Trigger` reactions, `DragDrop`,
  `LookAt`/`Follow` trackers, `API`/`Webhook`, variables that other scene
  machinery must read;
- you need a SENSOR event: object-targeted pointer input (click/hover on a
  specific mesh) authored on the object — with no actions — so code can
  react via `spline.addEventListener('mouseDown' | 'mouseHover', …)` in
  Play mode; the response stays in the document.

An object reacts to the world through **events**. Each event holds one or more
**actions** that run when the event fires. The most common action is a
`Transition` (tween to a state), but there are many more.

Everything is wired on the currently selected object, so `select(...)` (or
create) the object first.

## Inspect before you edit

`get_scene` only shows per-object COUNTS of states/events. To edit existing
interactivity you need real ids: call `get_objects([objectId])` — it returns
each object's states (`{id, name, selected}`), events (`{id, type, key/steps/
target/…, containers}`), every action (`{id, type, url/variableId/object/
runMode/…}`) and every Transition tween (`{id, state, duration, delay, easing,
repeat, direction}`). Then select the object and update by id.

## Event types (`INTERACTION_EVENT` string values)
Pass these strings to `addEvent(type)` or to `animate`'s `trigger`:

- `'Start'` — fires once when the scene loads (default).
- `'MouseDown'`, `'MouseUp'`, `'MousePress'` — pointer on the object.
- `'MouseHover'` — pointer enters/leaves the object.
- `'KeyDown'`, `'KeyUp'`, `'KeyPress'` — keyboard.
- `'Scroll'` — scroll-driven.
- `'Collision'` — physics collision (needs physics on — see the `physics`
  skill for the simulation itself, `game-controls` for gameplay wiring).
- `'Trigger'` — object enters a trigger zone.
- `'LookAt'`, `'Follow'` — object tracks cursor/target.
- `'DragDrop'` — draggable object.
- `'GameControl'` — WASD / third-person controller (special-cased by the
  alias). OPT-IN: add one ONLY when the user explicitly asks for the built-in
  Game Controls feature — then load `game-controls` (key mapping, physics
  pairing, collision/trigger gameplay). Building a game otherwise? The
  DEFAULT is a JS game loop + HTML UI — load the `games` skill.
- `'Conditional'` — fires while a condition (distance / state / comparison) holds.
- `'Resize'` — responsive breakpoints.
- `'VariableChange'` — a variable changed.
- `'API'`, `'WEBHOOK'` — external triggers.
- `'AIAssistantTrigger'` — the AI voice assistant matched this event's
  `description`; `'AIAssistantListener'` — tracks the assistant's audio
  spectrum (takes ONLY `'SetVariable'` actions).

The UI/docs use different names for some of these DSL strings: Trigger Area =
`Trigger`, Game Controls = `GameControl`, Distance / State Change =
`Conditional`.

`addEvent` returns the new event id — capture it for the action call.

### Per-event props (set with `updateEvent(eventId, props)`)
- Key events: `key` — a KeyboardEvent.key value; friendly `'Space'` works,
  single letters are lowercased. E.g. `updateEvent(e, { key: 'ArrowLeft' });`
- Mouse events: `mode: 'Object' | 'Canvas' | 'Window'`.
- Scroll: `steps`, `trigger: 'load'|'scroll'`, `startFrom: 'enter'|'page'`,
  `enterAnchor: 'top'|'center'|'bottom'`, `startOffset`, `endAfter`.
- Collision: `target: 'character' | 'scene'`.
- Trigger: `triggerZone: 'box'|'sphere'`, `size`, `position`, `radius`
  (rotation is given in degrees); `target: 'all' | 'custom'` +
  `triggeringObjects: [id, …]` restrict what sets it off.
- AIAssistantTrigger: `description` — a natural-language description of when
  the assistant should fire it.
- LookAt / Follow: `target` (object id or `'cursor'`), damping/limit props.
- VariableChange: `variableId`, `objectId`, `property` (e.g. 'Position X').
- Conditional: `condition` (Distance / State / Comparison object).
- Any event: `name`, `enabled: false` (disable without deleting).
- `updateEvent` cannot change an event's TYPE — `removeEvent` + `addEvent`.

## Action types (`ActionStateType` string values)
Pass to `addAction(eventId, actionType, container?)` (the event's type is
resolved automatically; the legacy `addAction(eventId, eventType, actionType)`
form also still works):

- `'Transition'` — tween the object to one of its states (the workhorse). Comes
  pre-seeded with two tweens (base + latest state); tune with `updateTween`.
- `'Animation'` — play a baked timeline/skeletal animation clip (only set its
  `object`/`clipId` when the object actually has imported animations:
  `clips:N` in the digest marks that object, and `get_objects` lists its
  clips' ids under `clips` — give every clip its own action, never reuse one
  clipId for several). Code that switches clips itself (UI buttons, a game
  loop) needs no actions at all: `spline.playAnimation` (`animation`
  skill).
  Accepts `updateAction(e, a, { interaction: 'play' | 'pause' | 'stop' })`:
  pause holds the clip where it is (the next play resumes it), stop rewinds
  it to its first frame. A pause/stop action targets `object` (omit for
  every animated object) and optionally one `clipId` of it.
- `'TimelineAnimation'` — play a shared timeline animation.
- `'Link'` — open a URL: `updateAction(e, a, { url: 'https://…',
  context: 'tab' | 'window' })`.
- `'SwitchCamera'` — cut/animate to another camera
  (`{ targetCamera: cameraId }` — NOT `camera`; plus `animate: false` for a
  hard cut, `duration`, `delay`).
- `'SceneTransition'` — go to another page (`{ target: pageId }`).
- `'Create'` — instantiate an object/component (`{ object: objectId }`).
- `'Destroy'` — remove objects (`{ objects: [id, …] }`).
- `'Reset'` — Reset Scene: restart the whole runtime scene after its delay.
  It is not a selective object reset or checkpoint teleport.
- `'SetVariable'` — write a variable: `updateAction(e, a, { variableId,
  expression: 'clicks + 1' })` (see "Expressions" below).
- `'DynamicVariablePlay'` — play/pause a DYNAMIC variable (Counter/Timer/…;
  "Variable Control" in the UI): `updateAction(e, a, { variableId, mode:
  'Play' | 'Pause' | 'Stop' | 'PlayPause' | 'Restart' | 'Toggle' })`. It does
  not move objects by itself — motion comes from binding that variable to a
  property or reacting to it with a `VariableChange` event.
- `'Audio'`, `'Video'` — media. Accept
  `updateAction(e, a, { interaction: 'play' | 'pause' | 'stop' })`.
- `'Particles'` — control a particle emitter: `updateAction(e, a,
  { emitterObjectId: '<emitter id>', emission: 'start' | 'stop' | 'pause' |
  'reset' | 'emitToggle' | 'pauseToggle', delay: 0 })` (delay in ms).
  Emitter setup + recipes live in the `particles` skill.
- `'Conditional'` — branch into if/else sub-actions.
- `'ClearLocalStorage'`, `'UserAPI'` — utility / external.

UI/docs names → DSL strings: Sound = `Audio`, Particles Control =
`Particles`, Variable Control = `DynamicVariablePlay`, Open Link = `Link`,
API Request = `UserAPI`.

### Which actions are allowed where
`Transition`/`Create`/`SetVariable`/`Conditional` are allowed almost
everywhere. Notable exceptions: `'LookAt'` takes NO actions; `'Follow'`
only `'Create'`; `'AIAssistantListener'` only `'SetVariable'`;
`'Trigger'` disallows `'Animation'`/`'TimelineAnimation'`;
`'MouseHover'`/`'Scroll'`/`'DragDrop'` disallow `'Link'`;
`'MousePress'`/`'KeyPress'` disallow `'Destroy'`;
`'GameControl'` only Transition/Animation/TimelineAnimation/Audio/Particles/
Create/Conditional. An invalid combo throws an error naming the allowed list —
read it and pick another action or event.

### Action containers
Most events keep actions in a single list — no container argument needed.
Exceptions (pass as `addAction`'s 3rd argument): `'Conditional'` events have
`'in'` (condition becomes true, the default) and `'out'` (becomes false);
`'DragDrop'` has `'drag'` (default) and `'drop'`; `'API'` has `'success'`
(default) and `'error'`; `'GameControl'` has
`'idle'`/`'move'`/`'jump'`/`'run'` (default `'move'` — see the
`game-controls` skill). Edits and deletes by
actionId find the container automatically. (Adding to a specific Resize
breakpoint isn't supported — its existing actions are still editable by id.)

A `'Conditional'` ACTION has nested branches. Create and configure the gate,
then add children explicitly:
```
const gate = addAction(eventId, 'Conditional');
updateAction(eventId, gate.actionId, { condition: 'score >= 3' });
const win = addAction(eventId, 'Transition', {
  parentActionId: gate.actionId,
  branch: 'if',
});
```
`if` runs when true and `else` when false. Nested Conditional creation is
unsupported; nested child edits/deletes are located automatically by action id.

## Wiring "on click, transition to a state"
The cleanest way is `animate` with a `trigger`:
```
mesh('Cube', { width: 160, height: 160, depth: 160 });
animate(
  { rotation: { y: 90 }, color: '#22d3ee' },
  { trigger: 'MouseDown', duration: 500, easing: 'ease-in-out' }
);
```

The equivalent low-level flow (when you need more control):
```
addState('Rotated');                     // new target state, now active
rotation({ y: 90 });                     // its look
color('#22d3ee');
const e = addEvent('MouseDown');         // event id
const a = addAction(e, 'Transition');
updateTween(e, a.actionId, a.tweenId, { duration: 500, easing: 'ease-in-out' });
```

## Editing an EXISTING interaction (worked example)
"Make the hover animation slower":
1. Find the object's id in the message's `<editor-context>` snapshot (or via
   `get_scene()` if the snapshot was omitted); `get_objects([id])` → find the
   MouseHover event, its Transition action and tween ids.
2. ```
   select(o => o.name === 'Button');
   updateTween('<eventId>', '<actionId>', '<tweenId>', { duration: 600, easing: 'ease-out' });
   ```
3. `play()` + `take_screenshot()` to verify.

Deleting: `removeTween(e, a, t)`, `removeAction(e, a)`, `removeEvent(e)`,
`removeState('Hovered')`. A wrong id is a silent no-op — verify with
`get_objects` afterwards if unsure.

## Tweens (Transition actions)
A Transition's tweens run in order; each tween's `state` is a state **id** of
the action's target object (`null` = Base State). `updateAction(e, a,
{ object: otherId })` retargets the action and re-points its tweens at that
object's latest state. Add/remove steps with
`addTween(e, a, { duration: 300, easing: 'ease-out' })` → tweenId and
`removeTween(e, a, t)`. Tween props: `duration`(ms), `delay`(ms), `easing`
('linear'|'ease'|'ease-in'|'ease-out'|'ease-in-out'|'cubic'|'spring' + spring
`mass`/`stiffness`/`damping`), `loop: true`, `direction: 'alternate'`.

## Hover example
```
animate(
  { scale: { x: 1.15, y: 1.15, z: 1.15 } },
  { trigger: 'MouseHover', duration: 200, easing: 'ease-out' }
);
```
On hover/press/drag events the Transition action defaults to `runMode: 'Toggle'`
(state on enter, back on leave), which is usually what you want.

## Multiple actions on one event
`addAction` adds another action to an existing event; call it again with the
same `eventId` to stack actions (e.g. a Transition plus a SetVariable). Each
returns its own `actionId`.

## States
`addState(name?)` creates a new state (and selects it, so following transform/
color calls define its look). `selectState(nameOrId)` re-activates an existing
state to restyle it; `selectState(null)` returns to the Base State — do this
before making live (non-state) edits. `renameState` / `removeState` accept a
name or id.

## Variables
Variables are scene-level values; `get_scene()` lists them with ids (dynamic
ones carry a `kind`).
- `setVariable('score', 0)` — create-or-update a BASIC variable (number,
  string, or boolean); returns its id.
- `dynamicVariable(name, type, props?)` — create-or-update a SELF-UPDATING
  variable; returns its id. Types + their settings:
  - `'counter'`: `value`, `increment` (per step), `updateInterval` (ms per
    step), `hasEnd` + `endValue`, `repeat` (restart at end), `autoStart`.
    E.g. `dynamicVariable('spin', 'counter', { updateInterval: 16,
    increment: 1, hasEnd: false })` ≈ a value rising ~60/s.
  - `'random'`: `min`, `max`, `decimals`, `updateInterval`, `isStatic`
    (one value instead of re-rolling), `autoStart`.
  - `'time'` (clock): `format` ('HH:mm:ss'|'HH:mm'|'HH'|'mm'|'ss'|'year'|
    'month'|'dayOfYear'|'dayOfMonth'|'secondOfDay'), `format12h24h`
    ('12'|'12ampm'|'24'), `timeZone` (IANA name or null = local).
  - `'timer'` (counts down) / `'stopwatch'` (counts up): `value`,
    `endValue`, `hasEnd`, `repeat`, `format` ('HH:mm:ss'|'mm:ss'|'number'|
    'number3decimal'). With the default 'number' format value/endValue are
    plain seconds; the clock formats store them as `{ textValue: [h, m, s] }`
    / `{ textValue: [m, s] }` arrays — set `format` in the SAME call and the
    shapes are seeded for you, then your explicit value/endValue override.
  - All types also accept `persistent: true` (value survives reloads).
- `renameVariable(nameOrId, newName)`, `removeVariable(nameOrId)`. Removing
  does NOT clean up references — actions/bindings that pointed at it read as
  0/empty.
To change a variable in response to an event, add a `'SetVariable'` action and
give it the target and the new value's expression:
`updateAction(e, a, { variableId, expression: 'clicks + 1' })`. To react to
one changing, use a `'VariableChange'` event (`updateEvent(e, { variableId })`).
Start/stop a dynamic variable from an event with a `DynamicVariablePlay` action.

## Expressions
A SetVariable's `expression` (the "To" field) and a Conditional action's
`condition` (the "If" field) take a source string:
- Variables by NAME (`score`, or `{player hp}` / `{<id>}` in braces for
  names with symbols, or to force a name that is also a keyword); numbers;
  `+ - * / % ^ ( )`; comparisons `== != > < >= <=`; `and` / `or` / `not`
  (or `&& || !`); `true` / `false`; functions `sin cos tan asin acos atan
  atan2 sqrt abs log exp floor ceil round min max random` (`random(1, 6)`).
- The expression is only the NEW VALUE: `'score + 1'`, never
  `'score = score + 1'` (a lone `=` is an error — compare with `==`).
- It is evaluated as the target variable's type. For a text variable only
  quoted literals, variables and `+` apply: `'"Score: " + score'`. For a
  boolean one: `'not isOpen'`, `'lives > 0'`. Conditions are boolean;
  compare text with a quoted literal: `'mode == "hard"'`.
- Set `variableId` in the same (or an earlier) call — the target's type
  decides how the expression is checked. Names resolve when the call applies,
  so variables created earlier in the same run_code block are fine. Unknown
  names or expressions that don't evaluate throw.
- A raw token array (`[{ id: scoreId }, { name: '+' }, { name: '1' }]`) is
  still accepted. `get_objects` reads back `expression` / `condition` as
  tokens: variables are `{ id, name }`, everything else `{ name }`.

## Binding variables to properties
`bindVariable(property, variableNameOrId)` makes a property of the SELECTED
object(s) follow a variable's live value — continuous, data-driven motion
within the variables system (for plain continuous motion the default is the
code loop — `animation` skill; reach for bindings when variables are already
in play or other scene machinery must read the value). Bindable properties:
`'position.x/y/z'`, `'rotation.x/y/z'`, `'scale.x/y/z'`, `'text'` (Text
objects display the value — scores, countdowns, clocks), and ANY numeric
parametric-geometry parameter by its schema name — `'width'`/`'height'`/
`'depth'`, `'cornerRadius'`, `'cornerSides'`, `'radius'`, `'sides'`,
`'segments'`, `'innerRadius'`, `'tube'`, `'arc'`, `'hollow'`, … (the mesh
regenerates live as the variable changes; Vector/Path geometries are
excluded — their shape derives from points). Numeric properties need a
number-valued variable; `'text'` takes any. `unbindVariable(property)`
freezes the property back to the variable's current value. `get_objects`
reports each object's `bindings` (property → variable id).
```
// A cube that spins forever + a live countdown readout:
const spin = dynamicVariable('spin', 'counter', {
  updateInterval: 16, increment: 2, hasEnd: false,
});
const left = dynamicVariable('timeLeft', 'timer', { value: 30, endValue: 0 });
select('Cube');
bindVariable('rotation.y', 'spin');
select('CountdownText');
bindVariable('text', 'timeLeft');
```

## Verifying interactions
Static screenshots won't show interaction. Call `play()` to enter play mode so
events fire, then `take_screenshot()`. Remember `play()` is not undoable.
