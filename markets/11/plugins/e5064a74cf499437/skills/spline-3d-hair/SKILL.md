---
name: spline-3d-hair
description: "Hair Systems: simulated strands (hair, fur, grass, fibers) via hair() — growing strands from an object's surface or a built-in scalp, strand shape (length, width, kink/curl, clumping), physics (gravity, wind, stiffness), root/mid/tip coloring or inheriting the base object's surface color, and recipes (character hair, fur, grass). Load for prompts like \"hair\", \"fur\", \"furry\", \"fluffy\", \"grass\", \"beard\", \"mustache\", \"hairy\"."
---

# Hair Systems (simulated strands)

A Hair System is its OWN object type (`'Hair'` in the scene tree): a
TressFX-style strand simulation with physics, wind, clumping, and root-to-tip
coloring — THE tool for hair, fur, grass, and fibers. NEVER model hair as
custom geometry (tubes/cones): it reads rigid and fake, and it can't move.
Strands render on the WebGPU backend (the default); the WebGL fallback does
not draw them.

## Create & edit

```
hair('new', { on: 'Head', hairLength: 1.2 });  // create + configure
rename('Hair');
```
- `hair('new', props?)` creates a hair system (returns it like `mesh` does);
  `add('Hair')` is the bare equivalent.
- `hair(props)` (no 'new') MERGES props over the SELECTED hair system(s) —
  partial props edit it in place, other selected object types are skipped
  (same edit contract as `particles`). `select(o => o.type === 'Hair')` or
  by name first when editing later.
- The system is a normal object: `position`/`rotation`/`scale`/`rename`/
  `group`/`hide` all work.

The default system is a shoulder-length auburn head of hair on a built-in
sphere scalp — gentle gravity, a little wind, simulating while you edit.
Treat the recipes below as overrides of that.

## Where the strands grow

- `on: 'Head'` (a name, id, or object handle) — grow the strands from that
  object's surface. THE common ask. Resolved when the commands run, so an
  object created earlier in the SAME block is a valid base. A group or
  imported model works too — every visible mesh in its subtree sprouts. An
  unknown name is silently skipped (the strands keep their current base), so
  spell it from the scene snapshot. `on: null` detaches back to the
  built-in sphere.
- `headShape: 'sphere' | 'torus' | 'cylinder'` — built-in scalp shapes
  (the scalp is part of the hair object; `headColor` tints it). Passing
  `on` sets `headShape: 'object'` for you.

## Strand shape

- `hairLength` (0.01–3, default 0.75) — length relative to the base's size.
- `hairWidth` (0.1–20, default 1.75) — ribbon width; thick = chunky/stylized.
- `guideStrands` (64–16384, default 8192) — simulated strand count; lower it
  for wispy coverage or performance, raise for density.
- `kink` (0–1) + `kinkFrequency` (0–10) — waviness/curl: amplitude and how
  many waves along each strand. Both 0 (the default) = straight.
- `clumpStrength` (0–1) + `clumpSize` (4–256 strands) + `clumpTipScale`
  (0.5–4) — pull neighboring strands into locks; the classic "styled hair"
  cue (0 = loose and uniform).
- `spreadRadius`, `tipSeparation` — root spread / tip fan-out dials; leave
  them at their defaults unless a screenshot says otherwise.

## Physics

- `gravity` (−30–30, default 10) — droop. 0 for grass that stands up;
  negative lifts the strands (floaty / underwater looks).
- `windStrength` (0–100, default 0) — ambient wind sway. Off by default:
  windless hair settles and lets the viewport idle; any wind keeps the sim
  (and its shadow updates) running every frame.
- `localStiffness` (0–1, default 0.67) — hold each strand's rest shape;
  high = brush-stiff, low = silky.
- `globalStiffness` (0–1, default 0.5) + `globalRange` (0–1) — pin strands
  toward their rest pose over the first fraction of their length (keeps a
  hairdo from collapsing).
- `damping`, `elasticity`, `stiffnessFalloff`, `vspCoefficient` — motion
  fine-tuning; the defaults are well tuned, adjust from a screenshot.
- `autoPlay` (default true) — keep simulating while editing. Play mode and
  exports always simulate regardless.

## Color

Two sources, switched by `hairColorSource`:
- `'custom'` (default) — a root→mid→tip gradient: `hairRootColor`/
  `hairMidColor`/`hairTipColor` (hex/CSS strings fine), plus `headColor`
  for the built-in scalp.
- `'object'` — each strand samples the BASE OBJECT's surface color at its
  root (vertex colors, else the material's color/gradient layers, else its
  flat color) — fur that matches the creature's own patterning.
  `hairShadeRoot`/`hairShadeTip` (default 0.6/1.15) ramp the inherited
  color's brightness root→tip (1/1 = verbatim).

Extras: `noiseEnabled: true` mixes a 3D-noise tint over hair + scalp
(`noiseColorA`–`noiseColorD`, `noiseScale`, `noiseMixHair`/`noiseMixHead`) —
punk/fantasy multicolor looks. Sheen dials: `specularPower`/
`specularIntensity`/`diffuseIntensity`/`ambientIntensity`, `opacity`,
`tipFade` (fade tips to transparent, default 0.4). `castShadow`/
`receiveShadow` default true.

## Recipes (starting points — screenshot and tune)

Character hair on a modeled head:
```
hair('new', { on: 'Head', hairLength: 1.4, kink: 0.25, kinkFrequency: 3,
  clumpStrength: 0.4, clumpSize: 48,
  hairRootColor: '#2c1a0e', hairMidColor: '#4a2f1a', hairTipColor: '#6b4a2c' });
rename('Hair');
```

Fur that inherits the creature's surface colors:
```
hair('new', { on: 'Fox', hairLength: 0.25, hairWidth: 1.2,
  hairColorSource: 'object', localStiffness: 0.85, gravity: 2,
  windStrength: 6 });
rename('Fur');
```

Grass on a ground patch (stiff, upright, wind-swayed):
```
hair('new', { on: 'Lawn', hairLength: 0.35, hairWidth: 3, gravity: 0,
  localStiffness: 0.9, windStrength: 10, clumpStrength: 0.15,
  hairRootColor: '#3f5233', hairMidColor: '#5d7a4d', hairTipColor: '#79975f' });
rename('Grass');
```
(Believable-register greens: olive families, never mint/lime — see # Style
register. For a whole lawn, one system on the ground plane beats many small
ones.)

## Gotchas & verifying

- Changing `hairLength`/`spreadRadius`/`guideStrands`/`headShape`/`on`
  REGROWS the strands from scratch (the sim snaps to the new rest pose);
  the other props update live.
- The strands are simulated, so a screenshot taken the instant after a big
  change may catch them mid-settle — give it a beat, then
  `take_screenshot()`. `autoPlay` keeps the sim running while editing;
  `play()` always simulates.
- Scale the BASE object rather than the hair object to resize a furry thing —
  strand length follows the base.
