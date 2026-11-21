---
name: spline-3d-scene-optimization
description: "Scene performance optimization: reading analyze_scene reports, reducing polygons, decimate(), merge(), bakeBoolean(), consolidating materials, taming lights/shadows/effects/textures, removing unused content — the measure→fix→verify workflow and visual-parity rules. Load for \"optimize my scene\", \"reduce the file size\", \"make it run faster\", \"improve FPS\", \"slow/laggy\", \"too many polygons\", and every fix requested from the Performance panel."
---

# Scene optimization

Optimizing means making the scene CHEAPER — fewer polygons, draw calls,
shader layers, shadow maps and texture bytes — while it keeps LOOKING the
same. Both halves are the job: a fix that visibly changes the scene is a
failure, and so is "optimizing" things that were never the bottleneck.

## What costs what (mental model)

- POLYGONS — export size + memory + every render pass. Cost drivers:
  segment counts, subdivision levels (each level ≈ ×4 polygons), cloners
  (polygons × count), imported/generated meshes. Parametric shapes have
  segment dials; imported/generated/baked meshes don't, and `decimate` is
  the dial for those.
- OBJECTS — draw calls (frame rate) + document size. Hundreds of small
  meshes cost more than one merged mesh with the same triangles.
- MATERIALS & LAYERS — shader work per pixel. Every layer compiles into the
  object's shader; depth/noise/displace/fresnel stacks multiply quickly.
  Duplicated materials also defeat batching and bloat the file.
- TEXTURES (image layers) — download bytes + GPU memory. Expensive to LOAD
  regardless of how small they render.
- LIGHTS & SHADOWS — each shadow-casting light re-renders the scene into a
  shadow map. Light count and shadow resolution are frame-rate dials.
- EFFECTS (postprocessing) — full-screen per-pixel cost; depth of field and
  bloom are the heavy ones.
- LIVE BOOLEANS — CPU recompute whenever an operand changes; NESTED Booleans
  recompute in chains and slow loading.
- AUDIO ASSETS — export bytes.

## Workflow — measure, fix, verify (always in this order)

1. MEASURE: call `analyze_scene`. It returns every metric with a
   good/average/bad mark and thresholds, plus the concrete offenders by id
   and name: the heaviest meshes (with polygon counts and clone
   multipliers), high-subdivision meshes, nested Booleans, all lights with
   shadow flags, layer-heavy materials, duplicated material assets, and
   unused-asset counts. Do NOT guess at problems the report doesn't show.
2. SNAPSHOT THE LOOK: `set_view` on the scene's content + `take_screenshot`
   once, BEFORE touching anything — this is the parity reference.
3. PLAN by impact: fix the 'bad' marks first, then 'average'. The usual
   impact order: heavy meshes / subdivisions / cloner counts →
   `decimate` for the ones with no segment dials → merge candidates →
   nested Booleans → materials & layers → lights & shadows →
   textures & effects → unused content. Tell the user the plan in one short
   paragraph before editing.
4. FIX with the recipes below — one category per `run_code` call, so a
   failure stays isolated and undo stays meaningful.
5. VERIFY: re-run `analyze_scene` and compare numbers; `take_screenshot`
   from the SAME view and compare against the reference. Finish by
   reporting the before → after numbers for what you changed (e.g.
   "polygons 2.1M → 340k, lights 6 → 3") — never claim an improvement you
   did not re-measure.

## Safety rules (hard)

- VISUAL PARITY: the scene must look the same afterwards. If a screenshot
  shows a visible change (popped silhouette, lost detail, changed shading),
  undo-fix it: restore the parameter toward its original value until parity
  returns.
- DESTRUCTIVE fixes — `decimate`, `merge`, `bakeBoolean`, deleting objects —
  cannot be re-edited the way the originals could. Use them on static dressing
  freely when asked to optimize; when a target has states, events, or
  animations (check `get_scene`'s flags / `get_objects`), SKIP it and tell
  the user why.
- NEVER delete a visible object to hit a number. Deleting is only for
  objects that are invisible, fully buried inside others, or explicitly
  approved by the user.
- Do not "optimize" what is already marked good — leave healthy metrics
  alone.

## Recipes

### Heavy meshes — reduce segments
`analyze_scene` lists the heaviest meshes with their polygon counts. Select
each by id and lower its tessellation with `geometry(...)`:
```
select(o => o.id === '<id from the report>');
geometry({ widthSegments: 24, heightSegments: 16 });   // Sphere/Plane
```
- `radialSegments` (Cylinder / Cone / Pyramid), `radialSegments` +
  `tubularSegments` (Torus), `detail` (Dodecahedron / Icosahedron),
  `segments`/`verticalSegments` (Lathe), `cornerSegments` (rounded corners).
- Halving a segment count roughly quarters a lat/long shape's polygons; a
  24-segment sphere is visually identical to a 64-segment one at most sizes.
- For procedural meshes (terrain/ocean/tree/rock), lower their resolution/
  detail props instead (`get_objects` shows the current values).

### Meshes with no segments to lower — `decimate`
Imported models, AI-generated meshes, baked booleans, merged dressing and
sculpted subdivs have no tessellation params: their polygons live in vertex
data. `decimate(target, ratio)` reduces that vertex data directly. The
target LEADS and is required — the edit is destructive, so it never inherits
the selection — and `ratio` is the fraction of the TRIANGLES to keep, so a
70k-triangle mesh at 0.5 comes back at 35k:
```
decimate('Statue', 0.5);              // half the triangles
decimate(['Rock A', 'Rock B'], 0.25);
decimate(get('selection'), 0.5);      // what the user has selected
decimate('all', 0.5);                 // every mesh in the scene
```
- It preserves the LOOK, not just the shape: uvs, textures, materials,
  normals and vertex colors survive intact — surviving vertices keep their
  original values and nothing is interpolated, so a textured model comes back
  textured. uv seams and hard edges shorten along themselves with every
  corner moving together, so islands stay watertight; material borders are
  pinned. Multi-material meshes keep their per-triangle material assignment.
- It is a READ alias: the result reports `from`/`to` vertex and triangle
  counts per mesh. Report the reduction from THOSE numbers.
- DESTRUCTIVE: the mesh becomes a plain non-parametric mesh. A decimated
  Sphere can't have its `widthSegments` raised again and a decimated subdiv
  has no cage left — so on a PARAMETRIC shape prefer the segment dials
  above, and use `decimate` where they don't exist.
- Same TWO-CALL RULE as `boolean`: the mesh must exist before the
  `run_code` call that decimates it.
- Screenshot after: 0.5 is usually invisible, 0.25 is safe on organic
  shapes, below ~0.1 silhouettes start to facet. Step down and check rather
  than jumping straight to a big cut.
- `reachedTarget: false` is NOT a failure to retry — it means that mesh's
  floor has been reached, and `stoppedBecause` says which of three floors:
  the shape budget (the next collapse would have moved the surface further
  than ~1% of the mesh's size, so it stopped instead of flattening it),
  vertices pinned on material borders or non-manifold junctions, or the mesh
  running out of legal collapses because its uv islands are already at their
  minimum triangle count. Report the reduction it DID get and move on;
  only pass `{ errorLimit: 0.05 }` to push past the shape budget if the
  user explicitly wants a smaller mesh at the cost of the silhouette, and
  screenshot the result. Options ride in a third argument:
  `decimate('Statue', 0.3, { errorLimit: 0.05 })`.
- Do NOT tell the user a mesh needs retopology or texture rebaking in an
  external tool because `decimate` stopped short. Report the floor the
  `stoppedBecause` field actually names, and what you already achieved.
- It reduces up to 2M triangles per mesh (a generated Spline model arrives at
  375k, so that is 5.3x headroom) and runs OFF the main thread, so a dense
  mesh takes seconds without freezing the editor. Past 2M it refuses: split
  the mesh and reduce the parts, or re-import it lighter.
- Live Booleans (`bakeBoolean` first), Shape Blends (lower
  `resolutionLevel`) and text (its own segment dials) can't be decimated;
  the error says which to use.

### High subdivisions
The report's `highSubdivisionMeshes` are SubdivGeometry meshes at level 2+.
Each level is ≈ ×4 polygons — drop one level at a time and re-check the look:
```
select(o => o.id === '<id>');
geometry({ subdivisions: 1 });
```

### Cloner counts
Cloned polygons = source polygons × count, so a heavy CLONE row in the
report has two dials: reduce the SOURCE mesh's segments (above), or lower
the cloner's count with a partial `clone(...)` edit on the selected cloner
(`get_objects` shows its current type and settings):
```
select(o => o.id === '<cloner id>');
clone({ grid: { count: { x: 6, y: 1, z: 6 } } });
```
Lowering the source's polygons is usually the better first move — it keeps
the composition identical.

### Too many objects — merge static dressing
`merge(target?)` collapses meshes into ONE editable mesh (fewer draw calls
and objects; same triangles). The extra meshes are DELETED and the result
uses a single material (the LAST target's), so only merge STATIC,
SAME-MATERIAL dressing — scattered rocks, a fence run, greeble. Targets
must exist before the call (the `boolean` two-call rule):
```
merge(['Rock 1', 'Rock 2', 'Rock 3']);
rename('Rocks (merged)');
```
- Do NOT merge: objects with events/states/animations (they die with the
  merge), objects that need separate materials, or anything the user still
  edits individually. Do NOT merge cloners — reduce their counts instead.

### Booleans — bake what no longer needs to be live
Live Booleans recompute on every operand change; NESTED ones (the report's
`nestedBooleans`) also chain at load time. `bakeBoolean` applies the CSG
result in place ("Apply & Edit"): the Boolean becomes a plain mesh, its
operand children are deleted, nothing recomputes again:
```
bakeBoolean('Wall with windows');
```
- Bake innermost nested Booleans first, then the outer ones if needed.
- The cut becomes permanent — skip Booleans whose operands are animated
  (an animated hole needs to stay live) and say so.
- Keep operand segment counts modest BEFORE baking: baked polygons are
  forever.

### Materials & layers
- Duplicated assets: the report lists them; `listMaterials()` shows usage.
  Repoint objects at one shared asset with `applyMaterial('Name')`, then
  delete the leftovers with `deleteMaterial('Name 2')`.
- Layer-heavy materials: every layer is shader cost. The report's
  `layerTypeHotspots` name the abused layer TYPE and the owning material
  (objectId / assetId). For an object's material: select the object, then
  `removeLayer(idOrType)` — a TYPE string removes the top layer of that
  type (`removeLayer('noise')`), an id removes that exact layer. For shared
  assets, `getMaterial(nameOrId)` lists the layers with ids and
  `updateMaterial('Name', { layers: [...] })` rewrites them. The usual fat:
  stacked noise/depth layers doing one gradient's job, displace layers on
  meshes too coarse to show them, duplicate color layers at full opacity.
  Screenshot after layer removals — layers are look-defining.
- Many one-off materials on similar objects → converge them onto one shared
  asset (`createMaterial` from the best one, `applyMaterial` on the rest).

### Textures
Image layers cost load time regardless of display size. Where a texture is
decorative (soft gradient, grain, simple pattern), swap it for a
color/gradient/noise LAYER — same look, zero download. Textures that must
stay (logos, photos, baked art) are fine — just don't stack several on one
material.

### Lights & shadows
The report lists every light with its shadow flag. Frame cost scales with
shadow-CASTING lights:
```
select(o => o.id === '<fill light id>');
updateLight({ shadows: false });
```
- One shadow-casting key light is enough for most scenes; fills and rims
  rarely need shadows.
- Delete lights that visibly change nothing (verify with a screenshot).
- `shadowResolution` above 1024 is rarely visible — lower it on lights that
  have it raised.
- For glow, emissive materials beat extra point lights.

### Effects
`fx('depthOfField', 'none')` kills the heaviest effect; bloom is next.
Only touch effects the user can spare — they're look-defining. Suggest
rather than remove when unsure.

### Hidden & unused content
- `select(o => !o.visible)` finds hidden objects; `remove(...)` the ones
  that are clearly abandoned (verify names/content first — hidden ≠ junk;
  states/events may toggle visibility at runtime, so check
  `get_objects` before deleting anything hidden).
- Unused material assets: `deleteMaterial('Name')` per asset. Unused
  image/color/audio assets can't be deleted from the DSL — point the user
  at the Performance panel's "Remove Unused Assets" buttons for those.

## What you cannot do (be honest about it)

- Export byte size and image/audio compression live in the export pipeline —
  `analyze_scene` doesn't measure bytes, and exports already compress and
  strip unused assets automatically. Don't promise byte numbers; report the
  metric improvements you measured.
- You can't change export settings or the user's renderer; the Performance
  panel's "Optimization mode" toggle is the user's own preview of the scene
  with shadows/AO/effects reduced — you don't control it.

## Reporting

End with a compact before → after summary of the metrics you improved, what
each fix was, and anything you deliberately skipped (with the reason —
"skipped merging the doors: they carry open/close events"). If the report
still has bad marks you could not fix safely, say what the user could do
manually.
