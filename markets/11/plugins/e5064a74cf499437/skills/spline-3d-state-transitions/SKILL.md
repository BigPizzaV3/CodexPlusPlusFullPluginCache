---
name: spline-3d-state-transitions
description: "The built-in States & Transitions animation feature — load ONLY when the user explicitly asks for it (names states, transitions, the timeline, or the States panel), or for physics-coupled kinematic motion (moving platforms — the one motion that must be state-driven): the all-in-one animate() helper plus the low-level addState/addEvent/addAction/updateTween flow, easings, duration, delay, loop and pingpong. Code-driven motion (the default) is the `animation` skill."
---

# States & Transitions (the built-in animation feature)

OPT-IN ONLY: motion is code-driven by default (the `animation` skill —
poses computed from time in the HTML layer, written through the `spline`
bridge). Use the built-in States & Transitions feature ONLY when the user
explicitly asks for it — they name states, transitions, the timeline, or
the States panel — or for PHYSICS-COUPLED kinematic motion (a positioned
body pushes dynamic bodies only when a STATE animates its transform;
per-frame bridge writes are teleports the simulation cannot see — see the
`physics` skill). Editing state-based interactivity a scene ALREADY has
also belongs here (with the `interactivity` skill for the full
event/action machinery).

State-based animation: an object has a Base State (its current look) and one
or more named States. A *transition* tweens the object from one state to
another when an *event* fires.

## The fast path: `animate(stateProps, transitionProps?)`
`animate` does the whole thing in one call on the selected object: it creates a
new state, writes the target properties into it, adds an event, adds a
Transition action, and configures the tween.

```
// pulse bigger on start, forever, smoothly
mesh('Sphere', { width: 200 });
animate(
  { scale: { x: 1.4, y: 1.4, z: 1.4 } },
  { duration: 800, easing: 'ease-in-out', loop: true, direction: 'alternate' }
);
```

`stateProps` (the target look) accepts any of:
- `position`, `rotation` (DEGREES), `scale` — each `{x?,y?,z?}`
- `color` — hex/CSS string
- `width`, `height`, `depth` — numbers
- `geometry` — a partial geometry change (e.g. `{ radius: 50 }`)
- `material` — a partial material layer, must include `type`
  (e.g. `{ type: 'fresnel', alpha: 0.5 }`)

`transitionProps` accepts:
- `duration` — milliseconds (default 1000)
- `delay` — milliseconds before starting
- `easing` — one of the string names below
- `loop: true` — repeat forever (sets internal `repeat = -1`)
- `direction: 'alternate'` — ping-pong back and forth (maps to `'pingpong'`)
- `trigger` — the event that starts it; an `INTERACTION_EVENT` string, default
  `'Start'` (i.e. plays on scene load). Use `'MouseDown'`, `'MouseHover'`, etc.
  for interactive transitions.
- spring tuning: `mass`, `stiffness`, `damping`, `velocity` (used when
  `easing: 'spring'`).

### Easing string names accepted by `animate`
`'linear'`, `'ease'`, `'ease-in'`, `'ease-out'`, `'ease-in-out'` (default),
`'cubic'`, `'spring'`. (`'ease-in-out-bounce'` also maps to spring.)

```
// click-to-flip an object 180deg with a springy feel
animate(
  { rotation: { y: 180 } },
  { trigger: 'MouseDown', easing: 'spring', stiffness: 120, damping: 12 }
);
```

## The low-level flow (when you need precise control)
Use this when `animate` is too coarse — e.g. multiple tweens, custom tween
ordering, or wiring an event you already created. All calls operate on the
currently selected object.

1. `addState()` — adds a new state and makes it the active edit target.
2. Write the target look with normal transform/color/material calls; while a
   state is active these write *into the state*, not the base:
   `position({x:300})`, `rotation({z:90})`, `scale({x:2,y:2,z:2})`,
   `color('#ff3366')`.
3. `addEvent(type)` — returns the new event id as its result; the alias also
   exposes the resolved `type`. `type` is an `INTERACTION_EVENT` string,
   default `'Start'`.
4. `addAction(eventId, eventType, 'Transition')` — returns
   `{ actionId, tweenId, initialTweenId }`. The Transition action is created
   with two tweens: `initialTweenId` (base, frame ~10) and `tweenId` (your new
   state, frame ~11).
5. `updateTween(eventId, actionId, tweenId, props)` — set the tween's
   timing/easing.

Because `run_code` is straight-line code, you can capture the returned ids in
variables within a single code block:
```
addState();
position({ y: 300 });
const e = addEvent('Start');
const a = addAction(e, 'Start', 'Transition');
updateTween(e, a.actionId, a.tweenId, {
  duration: 1200,
  easing: 'ease-in-out',
  loop: true,            // repeat forever
  direction: 'alternate' // ping-pong back and forth
});
```

## Tween properties (`updateTween` / `addTween`)
`updateTween` accepts the SAME friendly vocabulary as `animate`:
- `duration`: number — milliseconds.
- `delay`: number — milliseconds before the tween starts.
- `easing`: a string name from the list above (an unknown string is dropped).
- `loop: true` — infinite repeat.
- `direction: 'alternate'` — ping-pong back and forth.
- spring tuning: `mass`, `stiffness`, `damping`, `velocity` (defaults:
  mass 1, stiffness 80, damping 10, velocity 0) with `easing: 'spring'`.

Raw TweenState values also pass through if you're mirroring what
`get_objects` reports: `repeat` (extra iterations after the first, `-1` =
infinite), `direction: 'normal' | 'pingpong' | 'pingpong-rewind'`, and
numeric `easing` enums (`LINEAR = 0`, `EASE = 1`, `EASE_IN = 2`,
`EASE_OUT = 3`, `EASE_IN_OUT = 4`, `CUBIC = 5`, `SPRING = 6`, `ARC = 7`,
`NONE = 8`). Prefer the friendly names.

## Common patterns
```
// gentle infinite bob
animate({ position: { y: 60 } },
        { duration: 1500, easing: 'ease-in-out', loop: true, direction: 'alternate' });

// spin once on load
animate({ rotation: { y: 360 } }, { duration: 4000, easing: 'linear', loop: true });

// fade/scale-in on start
scale({ x: 0.01, y: 0.01, z: 0.01 });        // start small (base state)
animate({ scale: { x: 1, y: 1, z: 1 } },     // grow to full
        { duration: 600, easing: 'spring' });
```

### Phase-offset ambient motion (states-world version)
The DEFAULT scene-life pattern is the code version — the `animation`
skill's "Ambient life (phase offsets)". When the user has explicitly asked
for states, the same idea holds: one looping bob on a whole group reads as
mechanical, so give each drifting element its OWN loop with a different
duration/delay. `iterate` visits every selected object; vary the timing
per index:
```
select(o => o.name.startsWith('Cloud'));
let i = 0;
iterate((o) => {
  animate({ position: { y: 30 + rand() * 30 } },
          { duration: 2200 + i * 700, delay: i * 400,
            easing: 'ease-in-out', loop: true, direction: 'alternate' });
  i = i + 1;
});
```

Notes:
- Rotations are always in DEGREES.
- Set the *starting* look on the base state (before `animate`), and the
  *ending* look inside `stateProps`.
- For click/hover/scroll-driven transitions, set `trigger` (or use the
  low-level event flow) — see the `interactivity` skill for the full event and
  action catalog.
- Verify motion by entering play with `play()` and/or `take_screenshot()`.
