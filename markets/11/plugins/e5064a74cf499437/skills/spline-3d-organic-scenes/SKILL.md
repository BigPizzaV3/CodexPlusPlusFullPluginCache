---
name: spline-3d-organic-scenes
description: "Nature & organic scenes, stylized or believable: terrain and islands (displace layer vs customMesh), trees/rocks, water, clouds, graded skies, surface scatter, atmosphere, palettes, and ambient motion. Load for prompts like \"floating island\", \"forest\", \"landscape\", \"ocean\". (Planets/space have their own 'planets' skill.)"
---

# Organic / nature scenes

Recipes for the scenes users actually ask for — islands, forests, landscapes,
oceans. The difference between "3 shapes on a plane" and a scene that
passes design review is: layered silhouette, height-graded color, dense varied
dressing, atmosphere, and out-of-sync motion. All of it is cheap with the
patterns below. (Planet/space scenes are a different setting — load the
`planets` skill for those.)

REGISTER CHECK first (see # Style register): the finishes shown below —
flat-shaded facets, cone pines, bright greens — are the STYLIZED register,
correct when the user asked for low-poly/cute/toy or for an inherently
fantastical diorama (a floating island wears it well). For an UNSTATED style
on a real place ("a forest", "a mountain landscape") keep the same structure
but swap the finishes: skip `flatShading`, keep default segment counts, use
muted natural tones, give the terrain a `layer('texture', { style: 'grassy
ground with dirt patches, seamless' })` + bumpMap (see materials-and-look),
scatter denser and more varied, and prefer `object('tree')` / `object('rock')`
library imports for hero props — detailed models beat cone-pines when realism
is implied.

## Terrain — two paths

**Displace layer (default).** A subdivided flat shape + a noise `displace`
layer gives rolling relief in three lines. Use it whenever the silhouette
doesn't need to be exact:
```
mesh('Plane', { width: 2400, height: 2400, widthSegments: 48, heightSegments: 48 });
rotation({ x: -90 });
position({ y: 0 });
layer('displace', { displacementType: 'noise', intensity: 140, scale: 500, seed: 4 });
shading({ flatShading: true });
color('#5c9e57');
rename('Terrain');
```
`intensity` = relief height, `scale` = feature size (bigger = broader hills).
The mesh MUST have segments to displace.

**customMesh (when the silhouette matters).** Islands, cliffs, specific
landforms: compute a vertex grid (or concentric rings), displace `y` with
summed sines + `rand()`, fade the displacement to zero at the rim so edges
stay clean. Build at REAL world size (vertices are not normalized). WINDING:
on the XZ plane an angle loop `(cos a, ·, sin a)` runs CLOCKWISE seen from
above, so up-facing triangles list the NEXT angle before the CURRENT one —
fan `(center, s+1, s)`, band `(base+s, base+sn, next+s)` +
`(base+sn, next+sn, next+s)` (see building-scenes for the full patterns; a
slip is safety-netted by auto-flip/double-siding, but correct winding gives
cleaner normals). Then `shading({ flatShading: true })` for the low-poly
look. Verify proportions with the `size` [w,h,d] reported by
`run_code`/`get_scene` — don't guess from screenshots.

## A floating island (the full pattern)

1. TOP: a customMesh disc (rings of vertices, sine+rand hills, rim fading to
   the edge), grass green, flat-shaded.
2. UNDERSIDE: a customMesh inverted cone/spike with jittered rings — craggy
   rock tapering to a point. Overlap its top ring INTO the top disc so the
   seam hides; a slightly darker `depth` layer sells the shadowed underside.
   IT SHOULD SHARE SOME VERTICES WITH TOP DISC so the seam is smooth, not a gap, 
   make sure to use them in reverse though to avoid breaking winding order.
4. DRESSING on top: trees + rocks + a pond (below). Scatter, don't hand-place.
5. SATELLITES: a few small `Dodecahedron` rocks floating around the island at
   varied heights — each with its own slow bob/tumble loop.
6. GROUP everything (`select(o => !o.isCamera)` first!), name it, give the
   group ONE slow bob; give clouds/satellites their own offset loops so motion
   is layered, not monolithic.

## Trees, rocks, clouds (loop-scattered, always varied)

```
// pines: trunk + STACKED cone foliage — at least 3 tiers, each smaller and
// overlapping the one below (a single cone reads as a flat party hat).
// Cones default to soft corners (cornerRadius 8) — lower them so tiers
// keep a crisp tip and edge. Compute each tree's offset ONCE and reuse
// it so all parts line up.
for (let i = 0; i < 7; i++) {
  const s = 0.6 + rand() * 0.7;
  const dx = (rand() - 0.5) * 700;
  const dz = (rand() - 0.5) * 700;
  const green = rand() > 0.5 ? '#2e7d4f' : '#35905c';
  mesh('Cylinder', { radius: 7 * s, height: 60 * s });
  color('#6b4a2f');
  position({ y: 30 * s });
  translate({ x: dx, z: dz });
  for (let t = 0; t < 3; t++) {
    mesh('Cone', { radius: 45 * s * (1 - t * 0.25), height: 70 * s,
      radialSegments: 7, cornerRadiusTop: 2, cornerRadiusBottom: 2 });
    color(green);
    position({ y: (75 + t * 38) * s });
    translate({ x: dx, z: dz });
  }
}
```

- Rocks: low-`detail` `Icosahedron`/`Dodecahedron`, random y-rotation + slight
  z-tilt, 2 gray tones, flat-shaded.
- Clouds: 3–5 overlapping `Sphere` puffs per cloud sharing a FLAT BASE —
  biggest puff in the middle, smaller toward the ends. Keep default segments
  and SMOOTH shading: low-segment flat-shaded spheres read as boulders, and a
  loose cluster of random blobs never reads as a cloud. (Rounded `Cube`s
  still work for a toy look.) Place high, spread wide:
```
for (let c = 0; c < 3; c++) {
  const cx = (rand() - 0.5) * 1800;
  const cy = 430 + rand() * 150;
  const cz = (rand() - 0.5) * 1400;
  const puffs = 3 + Math.floor(rand() * 3);
  for (let p = 0; p < puffs; p++) {
    const t = p / (puffs - 1);                    // 0..1 along the cloud
    const d = 60 + 90 * Math.sin(Math.PI * t) + rand() * 15; // big middle, small ends
    mesh('Sphere', { width: d, height: d * 0.8, depth: d });
    color('#ffffff');
    // bottoms all touch the plane y = cy → the classic flat cloud base
    position({ x: cx + (t - 0.5) * puffs * 55, y: cy + d * 0.4, z: cz });
    rename('Puff' + c);
  }
  select(o => o.name === 'Puff' + c);
  group();
  rename('Cloud');
}
```
  Drift the cloud GROUPS out of sync (phase-offset pattern in the animation
  skill) — animating puffs individually tears a cloud apart.
- Alternative to loops — surface scatter. `select` returns an ARRAY of
  matches; `cloneTo` takes a single object, so index it:
```
const terrain = select(o => o.name === 'Terrain')[0];
select(o => o.name === 'Tree');
cloneTo(terrain, { count: 15, spreadType: 'random', seed: 3, hideBase: true });
```
  `clone({ type:'grid', ..., randomness: true, randomnessObject: {...} })`
  jitters a patch instead (see building-scenes for the full randomnessObject
  shape).

## Water

A pond/lake: a flat `Ellipse` nestled slightly ABOVE the terrain low spot
(avoid z-fighting), glassy:
```
mesh('Ellipse', { width: 260, height: 200 });
rotation({ x: -90 });
layer('glass', { alpha: 1, roughness: 0.15 });
color('#3a7bd5');
opacity(0.75);
```
Its shimmer is MOTION, so it rides the scene's motion document (the
`animation` skill) — drive the gradient angle per frame:
`spline.updateObject(id, { material: { layers: [{ type: 'gradient',
angle: 140 + Math.sin(t * 0.7) * 25 }] } })`.
An ocean: the displace-terrain recipe with low `intensity`, blue, with the
`displace` layer's `movement` driven per frame the same way for swell.

## Sky & atmosphere (never skip)

- The REAL sky option first: `sky({ timeOfDay: 15, weather: 'partlyCloudy' })`
  — a physically-based atmosphere + volumetric clouds behind the scene, with
  a sun that follows `timeOfDay` (0-24; ~6 sunrise, 12 noon, ~18 sunset) and
  moods from `weather` 'clear' → 'storm'. Reach for it whenever the prompt
  names a time of day, weather, or an open outdoor sky. Its `lighting`
  (default on) lights the scene with the sun + a sky dome IN PLACE of the
  ambient fill — so skip the ambient tint below, keep at most one soft fill
  light, and dial `lightingIntensity`/`exposure` rather than stacking suns.
- Stylized/diorama scenes can stay on the flat color instead:
  `background('#a8d4ff')` — pick a sky tone from the palette.
- `fog({ useBackgroundColor: true, near: 900, far: 4500 })` — distant content
  melts into the sky. THE one-call depth upgrade (with `sky()` on, give fog
  an explicit horizon-ish `color` instead — there's no flat bg to match).
- `environment({ ao: true, ambient: { color: '#bcd4ff', intensity: 0.7 } })`
  — grounding contact-darkening + cool sky fill (ambient matters when the
  sky's own lighting is off or the sky is off).
- Key light: `light('Directional', { intensity: 0.9, color: '#fff3df',
  shadowRadius: 3 })`, moved up and to one side. Warm key + cool ambient is
  the classic outdoor mix. Keep it at or below 1 (up to 2 only if the live
  shot still reads flat after repositioning) — it stacks on the ambient
  fill, and a hotter key washes the daylight out.
  Terrain outgrows the default shadow footprint: a directional light's
  shadows only cover its `size` (default 2000 world units), and a
  landscape/mountain scene spans far more — give the key `size: 4000` or
  more, matched to the terrain's span, so shadows reach the whole area.
  Outdoors there is ONE sun: with `sky()` lighting on, the sky IS the sun —
  otherwise reuse an existing directional light
  (`select(o => o.isLight)` + `updateLight`) rather than adding a second,
  and don't scatter extra point lights for "sunlight".
- For a graded horizon without the simulated sky, a big `Backdrop` behind the
  scene with a `gradient` layer (see materials-and-look).
- No `fx` finishing pass: fog + AO + the key light ARE the finish. Post
  effects are opt-in — add bloom/vignette only when the user asks.

## Palette

Pick 4–5 colors with VALUE contrast and repeat them: e.g. grass '#5c9e57' /
'#35905c', dirt '#8a5a2b', rock '#75757c', sky '#a8d4ff', accent '#e0552b'.
Two greens beat one (alternate them per tree). `style([...])` recolors
everything at the end if the mix drifted.

## Motion (code-driven, layered, out of sync)

Scene life is CODE — one motion document drives everything per frame (see
# Motion & interactivity; load the `animation` skill):

- The hero group: ONE slow bob, `y = base + Math.sin(t * 0.4) * 8`.
- Clouds/satellites: per-element frequency + phase so nothing syncs —
  see the phase-offset pattern in the animation skill.
- Water: material layer writes (above). Cloner scatters stay STATIC —
  `randomnessObject.movement` is a noise phase offset, not motion; drive the
  objects themselves (or their group pivots) for drift.
- Cameras stay OUT of animated groups, and the states machinery stays
  opt-in (`state-transitions` — explicit asks only).

## Order of work

Terrain → hero landform → dressing scatter → water → sky/atmosphere → lights →
motion → frame your check with `set_view({ objects: [...] })` → screenshot →
fix the worst thing → screenshot → finish with
`lookFrom({ azimuth: -35, elevation: 12 })` so the user lands on the hero
angle (`lookFrom` moves THEIR viewport; `set_view` only aims your private
screenshot camera). Procedural scenes earn 3–4 screenshots; use them at
milestones, not per tweak.
