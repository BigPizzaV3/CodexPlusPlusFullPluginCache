# Interactivity Skill

Reference for events, states, actions, and transitions. Load this whenever the user wants the design to *do* something — click, hover, keypress, animate on load, transition between visual states. Static styling is covered in the system prompt; you do not need this skill for non-interactive scenes.

All event/state/action structures are SeqItems: `{ "id": "...", "data": {...}, "children": [] }`. They live on the `states` and `events` arrays of the parent object's data. Sequence order = array order — the server assigns the internal ordering field automatically.

Provide a stable `id` on each SeqItem (states, events, actions, tweens): other SeqItems and transitions reference them by id (e.g. `"state": { "type": "state", "value": "hovered" }`).

## States

States define alternate visual appearances for an object. Each state overrides only the properties that change from the base — unchanged fields fall through.

State data may override: `center`, `rotation`, `opacity`, `fill`, `stroke`, `shape` (including `shape.size` for resizing). It may NOT override structural fields (parent, type, ordering).

```
{
  "id": "hovered",
  "data": {
    "name": "Hovered",
    "fill": { "type": "Color", "color": [0.3, 0.6, 1, 1] }
  },
  "children": []
}
```

**Animate size via `shape.size`, NOT `scale`.** The `scale` property is a low-level transform that doesn't update the object's hit-box, so transitions that rely on it look broken in Play Mode (clicks miss the visibly-shrunk button, hover regions are wrong). For a "pressed" button that shrinks 5%, override `shape.size` to 95% of the base. Same rule for any visible dimension change.

## Events

| Type | Fires on | Notes |
|------|----------|-------|
| `start` | Scene load | Best for entrance animations / on-load reveals |
| `mousePress` | Full click cycle | Optional `mode`: "object" (default) or "canvas" |
| `mouseDown` | Pointer down | Use with `mouseUp` for held-button behavior |
| `mouseUp` | Pointer release | — |
| `mouseHover` | Pointer enter (reverses on leave) | Best paired with `runMode: "toggle"` |
| `keyDown` / `keyUp` / `keyPress` | Keyboard | Optional `key` field; `null` = any key |

```
{
  "id": "click-evt",
  "data": {
    "type": "mousePress",
    "enabled": true,
    "name": "Click",
    "actions": [
      { "id": "act-1", "data": { <ActionData> }, "children": [] }
    ]
  },
  "children": []
}
```

## Actions

### Transition — animate between states

```
{
  "type": "transition",
  // "object" omitted → targets the object this event lives on (self). See below.
  "tweens": [
    { "id": "from", "data": { "state": { "type": "state", "value": null }, "duration": 0 }, "children": [] },
    { "id": "to",   "data": { "state": { "type": "state", "value": "<state-id>" }, "duration": 300 }, "children": [] }
  ],
  "runMode": "toggle"
  // To LOOP instead: add "repeat": -1 (forever) and "direction": "pingpong".
}
```
- **object** (optional): ID of the object whose states to transition. **Omit it (or set `null`) to target the object the event is attached to** — this is the default and is correct for the overwhelmingly common case where the event and the animated object are the same element (hover/press/toggle on one button, accordion header animating its own frame, etc.). Only set `object` to an explicit id when animating a *different* object (e.g. a trigger button that opens a separate modal frame). **Do not guess, copy, or invent an id for self-targeting — leaving the field out is both shorter and more reliable**, especially when adding interactivity to objects that already exist in the scene.
- **state value**: the `value` must be the exact `id` of a state SeqItem in the target object's `states` array — match it character-for-character to the `id` you assigned that state. It is resolved by id, not by the state's `name`. A `value` that doesn't match any existing state id silently does nothing. **Never emit an empty string (`value: ""`) for the target tween** — that is the single most common mistake and the transition just won't play. Define the state in `states` (with its `id`) *before* you reference it, then copy that id verbatim into the tween. Use `null` (not `""`) for the base/resting look.
- **state value `null`**: the object's default (base) appearance — i.e. "go back to neutral".
- **runMode** — how the action behaves when its event fires *again*:
  - `"toggle"` reverses on next trigger. Right for hover (in/out), accordions (open/close), checkboxes.
  - `"once"` plays the chain once and never replays. Right for entrance animations and one-shot reveals.
  - `"repeat"` lets it replay. **`runMode` does NOT make a transition loop** — by itself `"repeat"` still plays exactly once.
- **repeat + direction — THIS is how you loop.** Set `"repeat": -1` on the transition action to loop the whole tween sequence forever (a positive N loops N extra times; `0`, the default, plays once). Combine with `"direction"`:
  - `"pingpong"` reverses each iteration, so the animation eases to the target state and smoothly *back* every cycle — the natural choice for a pulse, breathe, or float loop.
  - `"normal"` hard-cuts back to the start each loop — right for a continuous spinner (`rotation: 360`, where the jump back to 0 is invisible since they're identical).
  - `"pingpongRewind"` is a rewind variant of pingpong.
- **duration**: milliseconds per tween.

To **stagger** entrances, add a leading 0-duration tween that holds at the hidden state for the desired delay before tweening to visible.

### Link — open a URL
```
{ "type": "link", "url": "https://example.com", "target": "Tab" }
```

### Show/Hide — toggle visibility
```
{ "type": "show", "object": "<target-id>", "show": true, "toggle": false }
```
- `show`: set visibility explicitly to true/false.
- `toggle: true` flips visibility on each trigger and overrides `show`.

## eventsPassthrough

Set `eventsPassthrough: true` on any object to make it transparent to pointer/keyboard input — events pass through to objects behind it (like CSS `pointer-events: none`).

Use for:
- Decorative overlays (glows, gradients, highlights painted on top of an interactive button).
- Visible container Frames that should not swallow clicks meant for objects underneath.
- Animated layers that react visually but should not block interaction.

## Animation timing

Match duration to the kind of motion — wrong durations are the most common reason a prototype feels off:
- **Hover / micro-interaction**: 100–200ms. Anything slower feels laggy on hover.
- **Click / press feedback**: 80–120ms in, 150–250ms out. Quick depress, slower release.
- **Modal open / sheet expand**: 250–400ms.
- **Page transition / large reveal**: 400–600ms.
- **Ambient loop** (pulse, rotate): 1500–3000ms full cycle so it doesn't feel frantic.

Stagger sibling entrances by 50–120ms each — synchronous reveals look robotic.

## Common patterns

### Hover + press button
A button that brightens on hover and shrinks slightly on press. Both transitions animate the button itself, so the `object` field is omitted — the transition self-targets the object the event lives on. (Never reach for the button's own id here.)
```json
{
  "data": {
    "type": "Shape", "name": "Button", "center": [0, 0],
    "shape": { "type": "Rectangle", "size": [120, 44], "cornerRadius": [8, 8, 8, 8] },
    "fill": { "type": "Color", "color": [0.2, 0.5, 1, 1] },
    "states": [
      { "id": "hover-state", "data": { "name": "Hovered", "fill": { "type": "Color", "color": [0.35, 0.6, 1, 1] } }, "children": [] },
      { "id": "press-state", "data": { "name": "Pressed", "shape": { "type": "Rectangle", "size": [114, 41.8], "cornerRadius": [8, 8, 8, 8] } }, "children": [] }
    ],
    "events": [
      {
        "id": "hover-evt",
        "data": {
          "type": "mouseHover", "enabled": true, "name": "Hover",
          "actions": [
            { "id": "hover-act", "data": { "type": "transition", "tweens": [
              { "id": "from", "data": { "state": { "type": "state", "value": null }, "duration": 0 }, "children": [] },
              { "id": "to",   "data": { "state": { "type": "state", "value": "hover-state" }, "duration": 150 }, "children": [] }
            ], "runMode": "toggle" }, "children": [] }
          ]
        },
        "children": []
      },
      {
        "id": "press-evt",
        "data": {
          "type": "mousePress", "enabled": true, "name": "Press",
          "actions": [
            { "id": "press-act", "data": { "type": "transition", "tweens": [
              { "id": "from", "data": { "state": { "type": "state", "value": null }, "duration": 0 }, "children": [] },
              { "id": "to",   "data": { "state": { "type": "state", "value": "press-state" }, "duration": 100 }, "children": [] }
            ], "runMode": "toggle" }, "children": [] }
          ]
        },
        "children": []
      }
    ]
  },
  "children": []
}
```

### Entrance animation (fade + rise on load)
Add a `start` event that transitions FROM a "hidden" state (opacity 0, `center` offset 16–24px down) TO the default. Use `runMode: "once"`. Stagger sibling entrances by adding a leading 0-duration tween that holds at the hidden state for the delay (50–120ms per element).

### Modal open / close
- Modal Frame has two states: "open" (opacity 1, scale 1, `center` at the parent's center) and base (opacity 0, scale 0.95). Default is hidden — start with `opacity: 0` and `visible: false`, or hide via `show` action.
- Trigger button: `mousePress` event with `runMode: "toggle"` — first click opens, second closes.
- Backdrop: full-bleed Rectangle behind the modal with the same toggle event so backdrop clicks dismiss.
- Set `eventsPassthrough: true` on decorative overlays so only the modal/backdrop captures input.

### Accordion / expandable section
- Section Frame has two states: "collapsed" (`shape.size` height = header height, e.g. 56) and "expanded" (full height including body).
- Header has `mousePress` with `runMode: "toggle"` switching between the two states.
- Set `clipContent: true` on the Frame so collapsed body content is hidden.
- For the chevron, add a state on the chevron itself with `rotation: 180` and trigger it from the same event (one transition per object).

### Tab switching
- Each tab body is its own Frame, all overlapping at the same `center`.
- Default: every body except the first has `visible: false`.
- Each tab button has a `mousePress` event with N `show` actions: show its own body, hide every sibling body. Use `runMode: "once"`.
- For the active-tab indicator (underline / pill), give it a state per tab `center` and transition into the right one from the same event.

### Toggle switch
- Knob Shape inside a track Frame. Knob has two states: "off" (knob `center` at the left) and "on" (knob `center` at the right + accent fill).
- Track has a "on" state with accent background.
- Track's `mousePress` event triggers a transition on both the track AND the knob (two actions in the same event), `runMode: "toggle"`.

### Ambient loop (pulsing dot, breathing glow, rotating loader)
- Give the object ONE alternate state — e.g. larger `shape.size` / higher `opacity` for a pulse, or `rotation: 360` for a spinner.
- Add a `start` event whose transition has a single tween to that state plus **`"repeat": -1`** to loop forever. **`repeat: -1` is what makes it loop — `runMode: "repeat"` alone plays exactly once.**
- Set `"direction"`: `"pingpong"` for anything that should ease out and back (pulse, breathe, float — it returns to base smoothly each cycle, so you only need the one to-alt tween); `"normal"` for a continuous spinner (`rotation: 360`, where the cut back to 0 is seamless since the two are identical).
