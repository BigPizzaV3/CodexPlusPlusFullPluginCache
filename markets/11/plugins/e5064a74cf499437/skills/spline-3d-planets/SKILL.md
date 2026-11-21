---
name: spline-3d-planets
description: "Planet & space scenes: realistic textured planets (AI texture layer — take the initiative), stylized procedural planets, atmosphere rims, rings, moons, space lighting and backdrop. Load for prompts like \"planet\", \"earth\", \"mars\", \"moon\", \"solar system\", \"space scene\"."
---

# Planets & space

A planet is a texture-and-light job, not a geometry job. The user saying
"a realistic planet" IS the ask — generate the surface texture on your own
initiative; don't wait for the word "texture".

## Realistic planet (the default read of "planet")

```
background('#05060f');                                    // deep space
mesh('Sphere', { width: 400, height: 400, depth: 400 });
layer('texture', { style: 'earth-like planet surface, oceans and continents, seamless' });
layer('fresnel', { color: '#9ec5ff', alpha: 0.45, scale: 1 }); // atmosphere rim
shading({ category: 'physical', roughness: 0.9, metalness: 0,
          bumpMap: 'texture', roughnessMap: 'texture', bumpMapIntensity: 6 });
rename('Planet');
light('Directional', { intensity: 1.1, color: '#fff3df' });      // the sun
```
- The planet's slow spin is MOTION, so it lives in the file's motion
  document (# Motion & interactivity; `animation` skill):
  `spline.updateObject(planetId, { rotation: { y: (t * 15) % 360 } })`
  per frame. The moons below ride the same loop.
- Space is a ONE-light setting: move the sun key up and to one side and let
  the night side fall dark — no fill. Two defaults fight this: a fresh scene
  usually already has a Directional Light — reuse it as the sun (or `remove`
  it) instead of adding a second one — and the page's always-on ambient fill
  washes the dark side: kill it with `environment({ ambient: false })`, or if
  the dark side must stay readable keep it dim instead,
  `environment({ ambient: { color: '#1b2340', intensity: 0.3 } })`. A sun
  slightly above intensity 1 is OK here ONLY because the ambient fill is
  disabled — with the ambient on, that same key overexposes.
- `bumpMap`/`roughnessMap: 'texture'` reuse the surface texture as relief and
  gloss maps: continents and craters catch the sun, darker oceans read
  glossier. The shorthand resolves to the material's top texture layer, so
  keep the `shading` call AFTER `layer('texture', …)`. There is no metalness
  map — `metalness` stays a plain number.
- Match the fresnel color to the planet: blue for earth-like, '#e8b28a' dust
  haze for mars, none for an airless moon.
- Texture `style` prompts that work — always append 'seamless' (the image
  wraps the sphere's UVs): 'earth-like planet surface, oceans and continents,
  seamless'; 'red rocky mars surface, craters and dust, seamless'; 'banded gas
  giant clouds, beige and rust, seamless'; 'gray cratered moon rock, seamless'.
- The texture resolves ASYNCHRONOUSLY — a checkerboard placeholder until then.
  Don't fight it: re-`take_screenshot()` on a later turn. Generation is also a
  PAID feature — on plans without the AI-texture entitlement the call can fail
  outright. Either way (error, or a checkerboard that never resolves), fall
  back to the stylized recipe below (full caveats in materials-and-look).

## Stylized planet (toy / low-poly scenes)

Skip the image; build the surface procedurally — always renders:
```
mesh('Sphere', { width: 400, height: 400, depth: 400 });
color('#2f6fb0');                                                // ocean base
layer('noise', { alpha: 0.55 });                                 // continents
layer('fresnel', { color: '#9ec5ff', alpha: 0.4, scale: 1 });    // atmosphere
shading({ category: 'physical', roughness: 0.8, metalness: 0 });
```

## Rings (Saturn look)

A `Torus` flattened on y, tilted, and slightly translucent:
```
mesh('Torus', { width: 900, height: 900, depth: 900, tubularSegments: 64 });
scale({ y: 0.04 });
rotation({ x: 12, z: 8 });
color('#d8c9a8');
opacity(0.8);
rename('Rings');
```
Match the planet's tilt on the planet itself (`rotation({ z: 8 })`) so the
rings read as equatorial.

## Moons & satellites

Small spheres at varied distances:
```
for (let i = 0; i < 2; i++) {
  const d = 90 - i * 30;
  mesh('Sphere', { width: d, height: d, depth: d });
  layer('texture', { style: 'gray cratered moon rock, seamless' });
  shading({ category: 'physical', roughness: 1, metalness: 0,
            bumpMap: 'texture', bumpMapIntensity: 8 });
  position({ x: 420 + i * 260, y: 60 + i * 90, z: -120 * i });
  rename('Moon ' + (i + 1));
}
```
Their motion is code — the `animation` skill's "Orbits, spins & travel":
each moon gets its OWN orbit radius/speed/phase around the planet
(`x = px + Math.cos(t * w + phase) * r; z = pz + Math.sin(t * w + phase) * r`
— a REAL orbit, which states never gave you) plus a slow spin
(`rotation.y = (t * 20 + i * 40) % 360`), every body out of sync so the
system reads layered, never synchronized.

## Finishing

- `group` the planet, rings, and moons and name the group so the scene tree
  stays readable. Select them with a name FILTER over the names you set —
  `select(o => o.name === 'Planet' || o.name === 'Rings' || o.name.startsWith('Moon'))`
  — NEVER a bare string: `select('Planet')` is the select-ALL wildcard and
  would sweep the camera and sun into the group. Do the grouping in a LATER
  `run_code` call than the one that created the objects (filters only see the
  scene as of the call's start).
- Frame with `set_view` and screenshot ONCE the texture has had a turn to
  resolve — judging the look against a checkerboard wastes a screenshot.
- No post-effects finishing pass: the mood comes from the texture, the
  fresnel rim, and the lighting. `fx` effects are opt-in — add
  bloom/vignette only when the user asks for them.
