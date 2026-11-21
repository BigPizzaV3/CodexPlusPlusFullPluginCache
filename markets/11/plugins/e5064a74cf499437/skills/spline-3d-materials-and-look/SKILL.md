---
name: spline-3d-materials-and-look
description: "Material layer stacks (color, shading/light category, gradient, fresnel, glass/transmission, depth, texture, displace terrain relief), decal stickers/splashes/impact marks stamped onto surfaces, flatShading/side, animated material tweens, layer/addLayer/updateLayer/removeLayer, opacity, lighting for good looks, fog/AO atmosphere, and backgrounds."
---

# Materials & Look

A Spline material is a **stack of layers**, like layers in an image editor:
higher layers composite over the ones below. The `light` (shading) layer is
the pivot — layers BELOW it are the shaded albedo (the default stack is a
`light` layer with a `color` layer under it); layers ABOVE it composite
UNLIT over the lit result (fresnel rims, outlines, image planes). New layers
from `layer`/`addLayer` go on top of the stack, except `texture`, which
`layer()` slots just below the light layer so it gets shaded. You build looks
by adding/tuning layers.

## The layer helpers
- `layer(type, props?)` — update the TOP layer of `type` on the selection,
  creating it if missing. The DEFAULT way to edit an existing material look —
  re-running it tunes the same layer instead of stacking duplicates.
- `color(value)` — convenience: sets the top color layer (and light color).
  Accepts hex/CSS strings (`'#ff8800'`, `'tomato'`, `'rgb(20,30,40)'`).
- `opacity(alpha)` — sets the color layer's `alpha` (0..1).
- `addLayer(type, props?)` — push a NEW layer of `type` onto the stack, even if
  one of that type already exists. Returns `{ id }`.
- `updateLayer(layerId, props)` — update an existing layer by id.
- `removeLayer(idOrType)` — remove a layer by id, or pass a type to remove the
  top layer of that type.
- `material(materialState)` — replace the whole material (advanced). Must be a COMPLETE material state including its `layers` array (e.g. one read back from the scene) — partial objects are rejected; use `layer()`/`color()` to tweak.
  Never deep-copy a material read from the scene with `JSON.parse(JSON.stringify(…))` or a recursive spread clone: texture image bytes (a `Uint8Array`) come out as a plain `{ 0: 137, … }` object, a multi-MB edit that breaks the texture. To change one layer, use `updateLayer()`/`layer()` instead.
- `shading(props)` — convenience for the light layer (see below).

Getting a layer id when you need one (only for stacked duplicates — otherwise
address by type): capture `addLayer`'s return, or read it off a selected
object — after `select`, a mesh exposes `o.layer(type)` → the layer's props
plus its `id`.
```
layer('gradient', { angle: 45 });               // edit top gradient (or create)
const rim = addLayer('fresnel', { alpha: 0.3 }); // deliberately stack a 2nd one
updateLayer(rim.id, { alpha: 0.6 });
removeLayer('glass');                            // top layer of a type…
removeLayer(rim.id);                             // …or by id
```

## Reusable material assets (shared looks)
THE RULE: the moment two or more objects need the EXACT same material —
window glass, brick walls, metal trim, all the leaves of a forest, any
repeated prop — mint a **material asset** once and link everything to it.
Never rebuild the same layer stack per object: N copies bloat the file,
drift out of sync, and turn "make the windows bluer" into N edits. Linked
objects render from the shared asset, so one `updateMaterial` restyles them
all. (Deliberate VARIATIONS are the exception — an object whose material
should differ gets its own per-object layers, or its own asset if the
variant repeats too, e.g. 'Foliage Light' / 'Foliage Dark'.)

- `createMaterial(name, props?)` — save an asset and link the selection to
  it. Starts from the first selected object's current material (build the
  look on one object first), or the standard default if nothing is selected;
  `props.layers` entries apply on top. Same-name calls update the existing
  asset (never duplicate). Returns `{ id, name }`.
- `applyMaterial(nameOrId)` — link the selection to an existing asset.
- `updateMaterial(nameOrId, { name?, layers? })` — edit the shared asset;
  EVERY linked object updates at once.
- `deleteMaterial(nameOrId)` — remove the asset; still-linked objects keep
  their look (each detaches to an inline copy).
- `listMaterials()` — the overview: `[{ id, name, layers (types only),
  usedBy }]`. The same list rides in every `<editor-context>`/`get_scene`
  snapshot as `materials`, so you usually already know what assets exist.
- `getMaterial(nameOrId)` — read ONE asset's FULL definition: `{ id, name,
  layers: [{ id, type, …props }], usedBy }`, colors as hex strings
  ('#rrggbbaa' when alpha matters), shared refs resolved, a texture layer's
  `image` as its asset id. The entries are valid `layers` PATCHES: tweak a
  prop and pass a subset straight back to `updateMaterial` (or seed a
  variant via `createMaterial`). An asset minted earlier in the SAME
  run_code call isn't stored yet — read it in the next call.

Both reads echo their data back in the run_code result (a read-only block
is valid and returns the data) — so INSPECT before you INVENT: when the
snapshot shows a suitable asset, `applyMaterial` it, or `getMaterial` it
and derive your variant from the real props instead of guessing them.

`layers` entries are `{ type, …props }` patches with `layer()`'s exact
semantics and props (update the asset's top layer of that type, or add one;
color strings, nested `texture` patches and `image` ids all work).

CAREFUL: `layer()`/`color()`/etc on an object linked to an asset DETACH that
object to a private inline copy first (editing one object never restyles the
others) — to change the shared look, go through `updateMaterial`.
```
select('Window 1'); layer('glass', { ior: 1.5 }); color('#bfe3ff');
createMaterial('Window Glass');                  // save + link Window 1
select((o) => o.name.startsWith('Window'));      // all the windows
applyMaterial('Window Glass');                   // link them
updateMaterial('Window Glass', { layers: [{ type: 'color', color: '#dff1ff' }] }); // restyles all
```

## Layer types (`NodeType`)
`'color'`, `'light'` (shading), `'gradient'`, `'depth'`, `'texture'`,
`'fresnel'`, `'dust'`, `'noise'`, `'normal'`, `'rainbow'`, `'toon'`,
`'outline'`, `'matcap'`, `'displace'`, `'pattern'`, `'transmission'`
(alias `'glass'`),
`'reflection'` (screen-space reflections; WebGPU renderer only),
`'vertexColor'` (the geometry's per-vertex color attribute — imported
vertex-painted meshes; only `alpha`/`mode`, the attribute is the payload),
`'video'`, `'particle'`.

Common layer props:
- All fragment layers: `alpha` (0..1), `mode` (blend mode,
  `FragmentBlendingMode`: `Normal=0`, `Multiply=1`, `Screen=2`,
  `Overlay=3`), and `isMask: true` — turns the layer into a greyscale mask
  for the layer directly below it (white = visible).
- `color`: `color` (hex/CSS string ok).
- `light`: `category` ('phong' | 'toon' | 'lambert' | 'physical'), plus
  category-specific `specular`, `shininess`, `emissive`, `roughness`,
  `metalness`, `reflectivity`; also `bumpMap`, `bumpMapIntensity` (any
  category except `lambert`, which ignores bump maps). Physical adds
  texture-layer map refs — `roughnessMap`, `metalnessMap`, `normalMap`
  (+ `normalScale`), `aoMap` (+ `aoMapIntensity`), `emissiveMap`
  (+ `emissiveIntensity`) — see the PBR maps recipe below — and BRDF
  lobes (plain numbers): `clearcoat` (+ `clearcoatRoughness`), `sheen`
  (+ `sheenColor`, `sheenRoughness`), `ior` (+ `specularIntensity`,
  `specularColor`), `iridescence` (+ `iridescenceIOR`,
  `iridescenceThickness`).
- `gradient`: `colors` (array of hex strings is accepted and converted),
  `angle`, `smooth`. With 3+ colors also pass `steps` (stop positions 0..1,
  e.g. `[0, 0.5, 1]`) — the default steps only place two stops.
- `depth` (3D gradient by distance): `colors` (+ `steps`), `smooth`, and
  `near` / `far` — the world-unit distance range the gradient spans. No
  `angle` here.
- `cavity`: `ridge`, `valley` (0..2 — values clamp at 2, the response
  saturates there) — Blender-style screen-space curvature: brightens convex
  edges (ridge), darkens concave creases (valley). Works on HARD,
  un-beveled edges — low-poly rocks, faceted `customMesh` terrain, crisp
  boxes — as well as bevels. Achromatic, overlay-blended over the stack.
  CAVITY IS OPT-IN: add this layer only when the user explicitly asks for
  it (a cavity layer, worn/eroded edges, curvature/edge-wear shading) —
  never as a default finishing move on rocks, terrain, or buildings. When
  asked: start ridge/valley at 1, alpha 0.6-1; 2 is the strong chiseled
  ceiling, 0.3-0.5 a subtle one.
- `fresnel`: `color`, `scale` (0..1 — 1.0 is the MAX, never exceed it:
  the rim clamps at 1, so a higher scale only blows the rim out into a flat
  wash; for a stronger rim raise `alpha`, for a wider one lower
  `intensity`), `bias`, `intensity` — adds rim light.
- `dust`: `color`, `coverage` (0..1: 0 = bare, 0.5 = everything above
  horizontal, 1 = fully buried), `softness` (0..1 settle-line feather),
  `noiseStrength`/`noiseScale` (breaks the settle line up) — dust/snow
  that accumulates on up-facing surfaces (world space, UV-free; re-settles
  when the object rotates). Warm grey = dust, white + noise = snow.
- `transmission` (glass): `roughness` (blur: 0 = clear, 1 = frosted), `ior`
  (refraction, default 1.5), `thickness`, and tinted absorption —
  `attenuationColor` + `attenuationDistance` (world units; 0 = off): thick
  regions shift toward the color, like real colored glass — see glass
  recipe below.

Color-ish keys auto-convert from hex strings: `color`, `specular`, `emissive`,
`sheenColor`, `specularColor`, `attenuationColor`, `colorA`..`colorD`,
`shadowColor`, `outlineColor`, `contourColor`, and `colors` (an array). Where the stored color carries a meaningful ALPHA channel — toon
`shadowColor` (its `a` is the shadow blend amount), the noise/pattern
`colorA`..`colorD` — a plain hex converts as opaque; use `'rgba(...)'` or an
`{ r, g, b, a }` object (0..1 each) to set the alpha.

## Shading (the light layer)
`shading(props)` sets the shading/lighting model of the selected object:
```
shading({ category: 'physical', roughness: 0.3, metalness: 0.8 }); // PBR metal
shading({ category: 'toon' });                                     // flat cel look
shading({ category: 'lambert' });                                  // soft matte
shading({ category: 'phong', shininess: 30 });                     // classic glossy
shading({ category: 'wireframe' });                                // wireframe (special)
```

`shading` also takes two mesh-level flags:
- `flatShading: true` — per-face normals: the faceted low-poly look. Essential
  for stylized terrain/rocks built with `customMesh` (indexed meshes otherwise
  render smooth).
- `side: 'front' | 'back' | 'double'` — render both faces of open surfaces
  (foliage planes, ribbons, the inside of an open cylinder).

## Recipes

### Matte plastic
```
color('#e0552b');
shading({ category: 'lambert' });
```

### Polished metal (PBR)
```
color('#c9ccd1');
shading({ category: 'physical', roughness: 0.15, metalness: 1 });
```

These recipes use `layer(...)` so they're safe to re-run — tweaking a value
edits the existing layer instead of stacking a duplicate.

### Glass / transmission
```
layer('glass', { alpha: 1, roughness: 0.05 }); // 'glass' -> 'transmission'
opacity(0.4);
```
Glass ONLY reads against contrast: a transmission surface over a white or
same-tone backdrop is invisible — the benchmark's glass-prism scene shipped
as a blank white frame this way. Put a mid/dark backdrop, a visible
refraction subject, or a rim (`fresnel`) behind every glass hero, and check
its silhouette survives in the live capture.
Colored glass (bottles, gems): add absorption instead of tinting the base
color — `attenuationColor` is the hue thick regions shift toward,
`attenuationDistance` the world-unit depth where it fully saturates
(smaller = denser tint; 0 disables):
```
layer('glass', { alpha: 1, roughness: 0.02, thickness: 20,
                 attenuationColor: '#2e8b57', attenuationDistance: 30 });
```

### Rim light (fresnel)
```
layer('fresnel', { alpha: 0.4, scale: 1 }); // scale caps at 1
```

### Gradient fill (2D — flat shapes ONLY)
```
layer('gradient', { colors: ['#ff0080', '#7928ca'], angle: 90 });
```
`gradient` paints a FLAT 2D ramp across the surface — on anything with
volume it reads as a STICKER slapped on the shape. Reserve it for
genuinely flat geometry (planes, unextruded vector shapes, UI cards,
backgrounds). ANY extruded or volumetric shape blends color with
`depth` instead — the 3D gradient through the object.

### Depth-faded color (3D gradient — the volumetric default)
```
layer('depth', { colors: ['#0b132b', '#3a506b'] });
```
`depth` grades color through SPACE, so a volumetric shape shifts hue
across its body and reads as lit from within — tune `near`/`far` until
the full blend spans the object (screenshot-check: if the shape shows
one flat color, the range is off; if it shows a hard 2D ramp, you used
`gradient` where `depth` belonged).

### Glassy gradient icons ("luminous from within")
The premium translucent-icon stack — glossy resin/glass shapes whose
color glows from inside rather than being painted on:
```
layer('depth', { colors: ['#ffb54d', '#ff5d8f'] }); // volume blend, tune near/far
layer('glass', { alpha: 1, roughness: 0.08 });      // gloss + refraction
layer('fresnel', { color: '#ffffff', alpha: 0.3, scale: 0.8 }); // soft rim catch
opacity(0.88);                                      // subtle translucency
```
Vary the `depth` color pair per icon (warm ↔ hot, cool ↔ acid) and keep
one soft key + AO so the curvature carries the highlights.

### Screens & displays (readable on-screen text)
A dark panel with a dim or default-size label is the recurring failure —
a lit screen is BUILT, in two parts, both mandatory:
```
// 1. The panel: near-black in the phosphor family, faintly self-lit.
color('#0a1a10');
shading({ category: 'phong', emissive: '#102a1a' });
// 2. The content: its own Text object, parented to the monitor and
//    floated ~2 units off the glass toward the viewer.
mesh('Text', { text: 'C:\\> LOAD "WORLD",8,1\nSEARCHING…\nREADY.', fontSize: 18 });
color('#39ff6a');                                // bright phosphor green
shading({ category: 'phong', emissive: '#39ff6a' }); // SELF-LIT: readable from
                                                 // any angle, lit or dark room
```
Size `fontSize` from the PANEL, never the default: read the panel's real
width from the run_code report / `get_scene()` `size` and pick fontSize ≈
panelWidth × 1.4 / longest-line-chars, so the longest line spans ~70% of
the panel. 3-5 short terminal lines beat one long one. Then LOOK: if the
next screenshot's text isn't readable and filling the panel, resize and
recolor NOW — bright emissive text is the era-correct hero look. The same
two-part stack does signage, neon, and appliance displays.
The texture layer's image comes from ONE of these sources — pick what fits:
```
layer('texture', { image: assetId });             // reuse an EXISTING asset — e.g.
                                                    // an id generate_image or
                                                    // generateTexture returned.
                                                    // Applies immediately.
layer('texture', { style: 'weathered copper' });   // OR generate a NEW image from a
                                                    // text prompt (async, see below).
```
If both are given, `image` wins and `style` is ignored — don't pass both.
The third source is drawing the image YOURSELF — `generateTexture` (next
section) returns an asset id for the `image` key.
### generateTexture — draw seamless patterns locally (canvas 2D)

THE way to give real-world surfaces crisp repeating detail (brick, planks,
tiles, pavement) — local and instant, no image service. Its draw callback
has strict seam-wrap rules (rng-only randomness, save/restore transforms,
opaque base fill, each feature drawn once): load the `texture-drawing`
skill for the contract and the per-material recipes BEFORE writing one.

### Texture layers on real-world surfaces (mapping & restraint)

A texture layer must NEVER be the object's only look: always set a `color()`
base in the same family first and keep the texture layer's `alpha` below 1
(0.6–0.8) so it tints the base. Generation is async and can fail — while the
image is unresolved the layer samples opaque black, so a texture-only
material renders the object BLACK until (or unless) the image arrives; a
color base keeps it looking intentional the whole time.

Reach for surface detail ON YOUR OWN INITIATIVE whenever the requested look
needs more than flat colors — "realistic"/"photoreal" asks, natural
materials, recognizable surfaces — and, because an UNSTATED style defaults
to the believable register, on the big surfaces of any real-world subject
the user didn't style ("a house" → brick/stucco walls and shingle roof, "a
table" → wood grain). Route by the look: REPEATING/GEOMETRIC pattern →
`generateTexture` (bricks, tiles, planks — crisp, instant, local);
photographic/organic → `style` (bark, marble, rust, lava, an earth-like
planet). Don't wait for the user to say "generate a texture":
```
mesh('Sphere', { width: 400, height: 400, depth: 400 });
layer('texture', { style: 'earth-like planet surface, oceans and continents, seamless' });
layer('fresnel', { color: '#9ec5ff', alpha: 0.45, scale: 1 }); // atmosphere rim
```

Projection & mapping (get these right or the texture will look broken):
- `projection`: `'uv'` (default — follows the mesh's own UV unwrap) |
  `'planar'` | `'spherical'` | `'cylindrical'` | `'triplanar'`. Friendly
  names are accepted and converted for you.
- The `uv` default DISTORTS on anything whose unwrap isn't a clean quad:
  extruded flat shapes (a Triangle-prism roof smears the image along the
  slope), elongated boxes (a tall chimney stretches it vertically), and
  most customMesh geometry. For box-like, extruded, or procedural surfaces
  pass `projection: 'triplanar'` — it maps per axis from object space with
  no stretching. Keep `uv` for cleanly-unwrapped primitives (Sphere, Plane,
  an unstretched Cube face) and `spherical`/`cylindrical` for their shapes.
- TILING: `texture: { repeat: [x, y] }` (the UI's "Scale") tiles the image so
  features read at real size — without it ONE image spans the whole surface
  (stones the size of windows). `texture: { offset: [x, y] }` shifts it;
  `texture: { rotation: r }` turns it.
- REPEAT IS ALSO RESOLUTION: a tile only has `size` px (512 default), so one
  tile stretched across a whole wall magnifies into blur that NO Sharpness
  setting can fix. Pick repeat from the surface's world size — decide what one
  tile should span (its feature scale: a 4-brick row ≈ 120–160 units, a few
  planks ≈ 150) and set `repeat: [round(surfaceW / span), round(surfaceH /
  span)]` (a 600×450 wall with ~150-unit tiles → `repeat: [4, 3]`). When a
  SINGLE un-tiled image must cover a large hero surface (full-bleed art, a
  planet), generate it at 1024 instead. Per-axis repeat also fixes ASPECT
  smear: `uv` stretches a square texture over the whole face, so on an
  elongated one (a 140×30 sign) features smear ~5× along the long axis —
  `repeat: [5, 1]` (≈ faceW / faceH) restores square features and density.
- SUBTLETY on real-world surfaces: blend the texture over a base `color()`
  in the same family with `alpha: 0.6–0.8` instead of full-strength, put
  'subtle', 'fine grain', 'low contrast' in the `style` prompt, and keep
  `bumpMapIntensity` low (1–2). Full-alpha photographic texture + heavy bump
  reads noisy and toy-like in the opposite direction.
- `axis`: `'x'` | `'y'` | `'z'` — the `planar` projection direction (planar only).
- `projectionAxis`: `'x'` | `'y'` | `'z'` — the pole axis for `spherical` and
  `cylindrical` (omitted = the legacy `'y'` behavior).

Important caveats for `style` (generation, not `image`):
- ONE GENERATION PER STYLE STRING: identical `style` strings reuse the SAME
  generated image (in-block and across the whole session) — near-instant
  after the first, and visually coherent. Spell the style IDENTICALLY on
  every surface that shares a material ("weathered white stucco, seamless"
  on all six stucco houses) and vary the per-surface look with
  `texture: { repeat }`, `alpha`, and the base `color()` underneath, not
  with reworded styles. Distinct styles each cost a full generation
  (seconds, and quota): a whole scene wants ~3-6 distinct styles, not 15.
  Generate the hero-surface textures in your FIRST material pass so the
  round-trips overlap with the rest of the build.
- Image generation is **asynchronous and best-effort** (it already retries
  once internally — never hand-retry). Until the image resolves — or if the
  image backend is unavailable — the layer renders a **checkerboard
  placeholder**. A checkerboard is NOT a bug to fight: either
  re-`take_screenshot()` on a later turn to let it resolve, or, if it persists,
  the backend isn't available — swap that surface to a `generateTexture`
  drawing (patterns need no image service) or build the look procedurally
  (below) instead of retrying the same texture. If `layer('texture')` THROWS
  a "returned no image" error, that surface's generation degraded (the error
  says why — quota, moderation, outage): same recovery — `generateTexture`
  first for anything pattern-like, procedural layers otherwise; identical
  styles that already resolved stay reusable.
- Use concrete, photographic `style` prompts ('cracked desert mud', 'brushed
  steel', 'mossy bark'); very short generic words may match a preset image.
  The image wraps the mesh's UVs — add 'seamless'/'tileable' to the prompt for
  surfaces that wrap around (spheres, cylinders).

### Decals — stamp an image ONTO another object's surface

A `Decal` (`mesh('Decal', { width, height, depth })`) is a projector box
that stamps its OWN material onto every mesh surface inside it — the way to
put a localized image on someone else's surface WITHOUT touching that
object's material or UVs: stickers/labels/logos on products, racing numbers
and livery on vehicle bodywork, paint/ink splashes, bullet impacts and
scorch marks, graffiti and posters on walls, dirt/wear patches. The stamped
skin hugs curved surfaces (it clips the real triangles under the box) and
lifts itself off them (`offset`, default 1), so it cannot z-fight.

The cutout-sticker recipe — both extra steps are MANDATORY for anything
that isn't a full rectangle (splashes, logos, numbers):
```
mesh('Decal', { width: 170, height: 170, depth: 300 }); // box through the surface
removeLayer('color');            // else the default gray fills the cutout
const splat = generateTexture('Paint Splat', (ctx, { size, rng }) => {
  // NO opaque base fill — on a decal, transparent pixels ARE the cutout.
  // (This inverts the usual generateTexture rule; only for decals.)
  ctx.fillStyle = '#ffd400';
  ctx.beginPath(); ctx.arc(size / 2, size / 2, size * 0.26, 0, Math.PI * 2); ctx.fill();
  for (let i = 0; i < 30; i++) {                  // rng()-scattered droplets
    const a = rng() * Math.PI * 2, r = size * (0.28 + rng() * 0.2);
    ctx.beginPath();
    ctx.arc(size / 2 + Math.cos(a) * r, size / 2 + Math.sin(a) * r,
      size * (0.012 + rng() * 0.045), 0, Math.PI * 2);
    ctx.fill();
  }
});
layer('texture', { image: splat.id });
```
- PLACEMENT: the box must INTERSECT the receiving surface — center it on or
  just in front of the surface with a generous `depth`. Only surfaces facing
  the decal receive the stamp; aim it exactly like the flat Rectangle it
  replaces (`rotation({ x: -90 })` floor/tabletop, `{ y: 90 }` +X side
  panel, `{ y: 180 }` far side). Draw-order for text/numbers: the canvas is
  y-down but the stamp reads upright — draw as you would for a screen.
- `layer('texture', { style: '…' })` (generated) works on decals too, but
  generated images are OPAQUE rectangles — fine for posters, labels, screens
  and full-bleed art; for cutout shapes draw with `generateTexture`.
- A decal stamps EVERYTHING inside its box: if a tank sticker also hits the
  seat behind it, shrink the box or pull it forward. One decal per detail —
  three bullet holes are three small decals, not one big one.
- The decal has a full material of its own: `shading` tunes how the stamp is
  lit; a `fresnel` above the light layer, `opacity`-style layer alphas, etc.
  all work. Keep the stack minimal — texture + light is the standard sticker.
- Ambient occlusion behaves correctly by construction: a decal RECEIVES the
  occlusion of the surface it sits on (it darkens in corners with it) but
  GENERATES none — no AO halo pressed around the sticker. Nothing to tune.

### PBR maps from the texture (physical)
The physical light layer can reuse a texture layer as its PBR maps. Pass the
shorthand `'texture'` — it resolves to the material's TOP texture layer, so
create the texture layer FIRST. Available map slots: `bumpMap`,
`roughnessMap`, `metalnessMap`, `normalMap`, `aoMap`, `emissiveMap`.
```
layer('texture', { style: 'weathered rusty metal, seamless' });
shading({ category: 'physical', roughness: 0.85, metalness: 0,
          bumpMap: 'texture', roughnessMap: 'texture', bumpMapIntensity: 6 });
```
As a `bumpMap` the texture's light/dark detail catches the light as surface
relief (`bumpMapIntensity` scales it, default 5); as a `roughnessMap` it
varies the gloss across the surface (darker areas render glossier). A texture
layer id also works in place of the shorthand. The other slots follow the
same pattern: `normalMap` treats the texture as a tangent-space normal map
(`normalScale` dials it), `aoMap` darkens crevices (`aoMapIntensity`),
`emissiveMap` makes the mapped areas glow — the map MULTIPLIES `emissive`,
which defaults to black, so ALWAYS pass `emissive` (usually `'#ffffff'`)
with it, and drive brightness with `emissiveIntensity`. `metalnessMap`
varies metalness.
Packed ORM textures work via per-map channel selects —
`roughnessMapChannel` / `metalnessMapChannel` / `aoMapChannel`, each
`'luminance' | 'r' | 'g' | 'b' | 'a'` (defaults: roughness luminance,
metalness `b`, AO `r` — the glTF ORM layout). Only wire slots the texture
actually contains — a photo texture into `normalMap` or `metalnessMap`
produces garbage shading.

ROUGHNESSMAP IS A LUMINANCE MULTIPLIER — misuse turns walls into mirrors:
the sampled luminance multiplies your `roughness` value, so a DARK texture
(slate roof, asphalt, charcoal brick, dark wood) drags roughness toward 0
and the surface renders as mirror-glass — it visually reads as TRANSPARENT
(it reflects the sky/ground in front of it). Only pass `roughnessMap` for
mid-to-light textures with real gloss variation (rusty metal, wet stone);
for dark surfaces keep a flat `roughness` number and use `bumpMap` alone.
If a screenshot shows a glassy/see-through wall or roof you textured, remove
the `roughnessMap` (`shading({ roughnessMap: undefined })`) or raise
`roughness`.

### Stylized surfaces without an image (procedural, always renders)
When a texture won't resolve, or the scene is STYLIZED (low-poly, toon, flat
color palettes — where a photo texture would clash), fake material richness
with procedural layers + PBR shading + lighting — these never fall back to a
checkerboard:
```
shading({ category: 'physical', roughness: 0.7, metalness: 0 }); // PBR base
layer('depth', { colors: ['#0b2a4a', '#3a7bd5'] });              // tonal depth
layer('noise', { alpha: 0.5 });                                  // surface variation
layer('fresnel', { color: '#9ec5ff', alpha: 0.4, scale: 1 });    // rim / atmosphere
```
A stylized planet, for instance, reads well as: an ocean `color` base, a
`noise` layer for continents, a `fresnel` rim for atmosphere, `physical`
shading, and a key light. A REALISTIC planet should get the texture layer
above instead.

### Displace layer — procedural surface relief (terrain without customMesh)
The `displace` layer moves the mesh's VERTICES with procedural noise — real
geometric relief, not just shading. A subdivided flat shape + displace is the
lightweight terrain/water path (reach for `customMesh` only when you need a
specific silhouette):
```
mesh('Plane', { width: 2000, height: 2000, widthSegments: 48, heightSegments: 48 });
rotation({ x: -90 });
position({ y: 0 });
layer('displace', { displacementType: 'noise', intensity: 120, scale: 5, seed: 4 });
shading({ flatShading: true });
color('#5c9e57');
```
Higher `intensity` = taller relief. `scale` is a noise FREQUENCY, not a
feature size: features span roughly `1000/scale` world units, so LOWER scale
= broader hills (default 10 ≈ 100-unit features). Keep features several times
wider than the mesh's segment spacing, or the relief aliases into random
spikes. The mesh needs segments to displace — an unsubdivided plane won't move.

### Animated material looks (flow, shimmer, pulse)
Material motion is code-driven like all motion (# Motion & interactivity):
the motion document writes layer props per frame through the bridge —
`spline.updateObject(id, { material: { layers: [{ type: <layerType>,
...props }] } })` — addressed by `type`, `index`, or `id` (load the
`animation` skill; hero surfaces only):
```js
// a "flowing" waterfall: swing the gradient angle
spline.updateObject(falls.id, { material: {
  layers: [{ type: 'gradient', angle: 120 + Math.sin(t * 0.8) * 30 }] } });

// shimmering water: evolve a displace layer's noise
spline.updateObject(sea.id, { material: {
  layers: [{ type: 'displace', movement: 20 + Math.sin(t * 0.5) * 20 }] } });
```
For RUNTIME-CREATED objects (`spline.createObject`), a custom TSL shader
material can animate entirely shader-side — `spline.createCustomMaterial`
with `tsl.time` in the graph costs zero JS per frame (html-content skill;
looks the layer system can't express only — layered materials stay the
default, and NOTE: that bridge call is unrelated to this skill's
`createMaterial('Name')` shared-asset DSL).

(When the user has explicitly asked for STATES, the same props can be
tweened instead — `animate({ material: { type: 'gradient', angle: 120 } },
{ duration: 2600, loop: true, direction: 'alternate' })` — see
`state-transitions`.)

## Lighting for good looks
Material shading only reads well with scene lights — but reuse what's there:
if the scene already has lights, `select(o => o.isLight)` and `updateLight` /
reposition them instead of adding more (1 key is usually enough; 3 lights is
the daylight ceiling — night/interior scenes may run more local pools). For a
scene with none:
- A key `light('Directional', { intensity: 0.9 })` placed up and to one side.
- Optionally a softer fill `light('Point', { intensity: 0.4 })` opposite it.
- DAYLIGHT: keep the key at or below 1 (up to 2 only if the live shot still
  reads flat) — lights stack on the page's ambient fill (default 0.75), and a
  hotter key blows out the very highlights that show off a material.
  NIGHT/INTERIOR: dim the ambient and light with local Points/Spots at 2–8
  shaped by `distance`/`decay` — under-lit PBR reads as grey mud.
- `physical`/PBR materials especially need decent lighting to show roughness
  and metalness; `toon` and `lambert` are more forgiving.

## Backgrounds & atmosphere
`background(value)` sets the page background color (hex/CSS string). A soft,
slightly tinted background flatters most subjects:
```
background('#dfe3e8');
```
To ground a subject on a plain background WITHOUT a visible floor slab,
combine it with a shadow-catcher floor: a Rectangle/Plane with
`visibility({ shadowCatcher: true })` renders only the shadows cast onto it
— the background shows through everywhere else (see building-scenes'
Grounding section). The catcher's material panel is ignored while enabled.
The background is flat. For an OUTDOOR scene that wants a real sky, use the
atmospheric `sky()` instead — a physically-based atmosphere with volumetric
clouds and a sun that also lights the scene:
```
sky({ timeOfDay: 17.5, weather: 'partlyCloudy' }); // golden hour
```
`timeOfDay` (0-24) sets the sun (~6 sunrise, 12 noon, ~18 sunset); `weather`
runs 'clear' → 'storm'. While its `lighting` is on (default) the sky's sun +
dome REPLACE the ambient fill — don't fight it with extra suns; tune
`lightingIntensity`/`exposure` instead. `sky({ hdri: { image } })` maps an
equirect environment instead — `image` takes an image asset id, a built-in
env preset name ('Forest', 'Neon city', 'Sunset fairway', …), or a URL;
`sky('none')` returns to the flat color.
For a merely GRADED backdrop (stylized/abstract scenes where a simulated sky
is too literal), put a big `Backdrop` (or a large vertical `Plane`) behind
the content and give it a `gradient` layer:
```
mesh('Backdrop', { width: 8000, height: 4000 });
layer('gradient', { colors: ['#a8d4ff', '#f6ead9'], angle: 90 });
shading({ category: 'lambert' });
```
Pair the background with the page environment for depth and grounding:
- `fog({ useBackgroundColor: true, near: 800, far: 4000 })` — distance fog
  toward the background color; distant objects melt into the sky.
- `environment({ ao: true, ambient: { color: '#bcd4ff', intensity: 0.7 } })` —
  ambient occlusion (contact darkening that grounds objects) + a tinted
  hemisphere-style ambient fill.
A scene with zero atmosphere reads as a tech demo — one `fog` call is usually
the single highest-impact look upgrade.

## Global look passes
- `prettify()` — auto-harmonizes all material colors (no args). Good finisher.
- `style(['#hex', ...], seed?)` — recolors all materials + the background from a
  supplied palette.
- `studio()` / `stage('studio')` — instant neutral studio: gray ground, key
  light, and two studio materials assigned to the selection.
- `fx(type, props?)` — page-wide post-processing effects (see below).

## Post-processing effects (`fx`)
POST EFFECTS ARE OPT-IN — never part of a default look pass. Enable one ONLY
when the user asks for it, by name or by a look that names it ("glowing
neon" → bloom, "film grain" → noise, "retro pixel look" → pixelation). The
single exception is `depthOfField`: you may enable it unprompted when it
genuinely serves the shot (a close-up hero subject against a distant
background) — skip it otherwise. Do NOT finish scenes with a habitual
bloom + vignette pass: mood and depth come from fog, lighting, AO, and
palette (above), not from post effects.

`fx(type, props?)` enables and tunes a page post effect in one call. Pass
`'none'` (or `null`) as the props to switch one OFF (`fx('vignette', 'none')`),
or `fx('none')` to clear all post-processing. Every effect also accepts a shared
`opacity`. The effects and their key props:
- `'depthOfField'` — camera lens blur: `focusDistance`, `focalLength`,
  `bokehScale`.
- `'bloom'` — glow bleeding off bright areas: `intensity`, `luminanceThreshold`,
  `luminanceSmoothing`, `blurScale`. The tool for an asked-for neon/emissive glow.
- `'vignette'` — darkened frame edges: `darkness`, `offset`.
- `'chromaticAberration'` — RGB colour fringing: `offset` (an `[x, y]` pair).
- `'hueSaturation'` — `hue`, `saturation`; `'brightnessContrast'` —
  `brightness`, `contrast` (global colour grade).
- `'noise'` — film grain (tune with `opacity`); `'pixelation'` — `granularity`
  (retro / low-res block look).

```
fx('depthOfField', { focusDistance: 600, bokehScale: 3 });
```

Shading is hard to predict from code alone — verify material work with a
`take_screenshot()`, but at MILESTONES (after the whole material + lighting
pass, framed with `set_view`), not after every tweak; the usual budget is one
or two screenshots per request.
