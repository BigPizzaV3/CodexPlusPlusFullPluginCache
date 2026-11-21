# Anatomy explanatory scenes

Use anatomy for readable structure, spatial routes, sections, assembly and cause/effect. Science and how-it-works videos start with [Anatomy explainer](../../anatomy-explainer/SKILL.md), which applies the original upstream object-authoring workflow before editing. Authored figures can use the full upstream SVG kit, their own deterministic model and optional WebGL/3D; the existing part adapter uses the pinned `turning`, `TURN.mount`, material painter, `audit` and `turn-audit` APIs. Use Three.js for imported GLB/GLTF and perspective materials. Choose from the explanation, not its subject: mechanisms, products, science and processes share the same interface.

Before authoring each spatial shot, record the target object, camera/projection target, main action and observable result in the director plan. Establish spatial and causal relationships before adding decoration. Keep long text, evidence, numbers and narration in existing 2D layers. Use cutaways, color and a short label to make the relevant part unmistakable. Do not add 3D to ordinary subtitles or simple UI merely for style.

## Supported contract

`scene.spatial` retains `camera` and `models`. Use `backend: "anatomy"` and `models: []` for anatomy, or `backend: "auto"` with both `anatomy` and `models` for a mixed scene. An optional normalized `modelViewport: {x,y,width,height}` places the Three.js overlay. The two runtimes are separately observed in the render report. `spatial.annotations` attach to Three models in mixed scenes; `anatomy.annotations` attach to anatomy parts. Existing 2D visual/motion layers and captions retain their stacking order.

## Reusable authored figures: preferred for explainers

Build the complete subject in the user's project with the original kit, keeping its source and research evidence. Follow [the authored figure contract](../../anatomy-explainer/references/authored-figure.md) to export self-contained SVG/HTML, CSS and a deterministic `renderAt` factory as `figure.anatomy.json`. `anatomy import` registers it as an `anatomy-figure` asset. A project-level `anatomyFigures` entry maps a stable figure ID to that asset ID; scenes reference `anatomy.figureId` and control `anatomy.view` instead of rebuilding an unrelated object per scene.

The view supports explicit model-time offsets/rates and normalized crop keyframes, plus `focusPartIds` and `dimOpacity` to retain surrounding context. Author meaningful `data-anatomy-part` elements and derive all motion/readouts from the same `stateAt(time)` function. The browser runs the self-contained author factory without a remote CDN. Changing an imported figure requires a new import so the content hash and render evidence follow the actual source.

The plugin bundles the pinned upstream source tree under `third_party/anatomy/`, including its original `SKILL.md`, craft/kit/motion/verify references and executable examples. Use the closest example's construction method, then author the subject required by the brief. A real GLB/GLTF is an alternative when it suits the subject; it is not a prerequisite for a detailed Anatomy figure. Keep generated source and media in the user's project, and preserve upstream license attribution.

`anatomy.nativeExample: "turning-dial"` remains available as a fixed upstream reference with 88 parts and three layers. It demonstrates that particular dial and hand, not a generic model library or a watch asset. The JSON `parts` adapter below remains useful for declarative scenes and legacy projects. Neither an installed runtime nor a list of primitive names establishes that the complete subject has been authored.

## Existing declarative parts adapter

Anatomy uses **Z-up**, scene units and **degrees**. Three.js uses its documented Y-up coordinates and radians. Do not copy angles or positions between them unchanged.

- `projection`: azimuth/elevation in degrees, dimensionless scale (default 1), optional pixel origin. Projection is isometric; use Three.js for a perspective camera.
- `layers`: back-to-front layer names. Within each layer the upstream painter recomputes depth ordering.
- `parts`: stable `id`, `kind`, optional position, groupId, parentId, layer, material, color, opacity, visibility. `parentId` adds the parent's rest position and inherits its group unless overridden. Group pivots and geometry are in world rest coordinates.
- Solid kinds: `box`/`plane` with size; `round` with radius/height/axis; `sphere`; `prism` with a **convex** polygon; `lathe` with a convex body's profile `[axialPosition,radius][]`. Non-convex profiles must be split into separate bodies.
- `gear`: radius, teeth, height, optional innerRadius; extruded convex teeth surround a solid or hollow hub. This is explanatory geometry, not involute gear design or a physics simulation. Derive gear ratios/phases from the intended explanation.
- `ring`: radius, innerRadius, height, segments; the hole is real geometry, not a background-colored mask.
- `tube`/`line`/`arrow`: points relative to position; strokeWidth in output pixels. `freeEnds` explicitly indicates intentionally open ends; set false for endpoints that must connect, then inspect upstream audit findings.
- `spring`: helix radius, height, turns, axis. Its route is real 3D geometry.
- `label`: text/fontSize at a 3D location. Prefer a 2D heading for a sentence.
- `fixed`: an authored upstream SVG decal backed by sampled solid geometry; use for dials, screens, gauges and dense static art. `item`: a sampled point cloud for a complex moving object; set `fullClouds: true` when every authored point must be retained instead of the upstream display thinning pass. `plane`/`billboard` attach SVG marks to 3D geometry and follow its group.
- `details`: forward upstream seams, ribs, dots, bolts, rings and rules to the painter. Use these to make a part read as a manufactured assembly instead of a bare primitive. `route` forwards tube gaps, breaks, caps, rims, bundles and touch relationships.
- Material names: gold, chrome, steel, gunmetal, rubber, brass, copper. Optional custom color/secondaryColor applies when no material is selected.
- Groups: `turn` about Z at pivot; `hinge` about a declared nonzero axis at pivot; `slide` along a normalized direction; `free` translation and XYZ Euler rotation. Parent groups compose transforms.
- Keyframes are **scene-relative**: `{atSeconds, values, parts?, easing?}`. Turn/hinge use numbers in degrees; slide uses distance. Free uses a translation Vec3 or `{translation,rotation}`. `parts` may animate opacity, visible and removedOpacity. Sparse tracks are evaluated from rest on every seek, including reverse seeks. Easing: linear/none, power1/power2 in/out/inOut, sine.inOut.
- Sections use `mode: "clip" | "slice"`, `plane`, `offset`. Keep the half satisfying `dot(plane, point) <= offset`. Slice displays the removed half faintly (`opacity`); clip hides it. `parts.removedOpacity` can reveal the cut over time. The plane is fixed in the rest geometry and moves with its group. Upstream supports prism cuts along/across its extrusion axis and round cuts across the axis. Unsupported cuts fail explicitly; change the geometry or choose Three.js. Do not silently hide the entire part.
- Annotations: `{id,text,anchor:{partId,offset?}|Vec3,labelOffset?,fontSize?,range?}`. Their ranges are scene-relative and leaders follow transformed anchors. Labels stay on top of geometry; inspect overlap and viewing-size readability.
- Optional `effect: {fragment, uniforms?, required?}` calls upstream WebGL `glLayer.draw` using explicit local time. The geometry itself needs no WebGL. A required shader failure blocks export. No shader or runtime is downloaded from a CDN.
- `effects`: an ordered array of `{id,order:"back"|"front",fragment,uniforms?,required?,opacity?}`. Back effects render under the SVG, front effects over it; every layer receives explicit scene time and calls upstream `glLayer.draw`. Use this for light, water, steam, caustics, glow and flow. Keep the SVG readable when WebGL is unavailable unless the effect is marked required.
- `readouts`: deterministic values or group-linked values rendered in the figure. `controls` add pointer, keyboard or button state for local preview; export still comes from explicit keyframes and remains random-access deterministic. `presentation` can add the upstream-style title, subtitle and hint card.
- `audit` may be `true` or an object with `allow`, `crowd`, `cover`, `ground`, `frames`, `apart` and `quick`. Leave it enabled for authored figures. An audit-disabled scene must be an intentional, documented exception.

Example of an axis-correct opening action:

```json
{
  "backend": "anatomy",
  "camera": {"projection":"orthographic","position":[4,3,6],"target":[0,0,0]},
  "models": [],
  "anatomy": {
    "groups": [{"id":"lid","type":"hinge","pivot":[0,1,0],"axis":[1,0,0],"range":[0,90]}],
    "parts": [{"id":"cover","kind":"box","size":[3,2,0.15],"groupId":"lid","material":"steel"}],
    "keyframes": [{"atSeconds":0,"values":{"lid":0}},{"atSeconds":2,"values":{"lid":90},"easing":"power1.inOut"}],
    "annotations": [{"id":"pivot-note","text":"绕轴打开","anchor":{"partId":"cover"},"labelOffset":[110,-70]}]
  }
}
```

## Review the actual implementation

Run `project validate`, resolve geometry errors, then render a short affected preview. `review` returns full-size/viewing-size frames, `sourceUsage` and `spatialRuntime.observed`. For imported authored figures, confirm backend `anatomy-authored`, engine `project-authored anatomy`, the figure ID and source hash. For the declarative/native TURN adapter, confirm an observed `anatomy-svg` or `anatomy-canvas2d` entry with `engine: upstream TURN.mount/turning` and the pinned source commit. Confirm imported models have `three-webgl`, loaded children and no model failures. A capability declaration or installed Skill version is not evidence of backend use.

Inspect before/action/result frames, section interiors, hinge direction, layer order and labels. Upstream audit warnings can include intentional touching/overlap; judge them against the intended structure and record the decision. Technical checks cannot establish physical correctness or explanatory clarity.

For revisions, follow [the render-review upgrade contract](render-review.md). Never call a rerender an anatomy upgrade if the timeline still only references old MP4s. A progress indicator baked into old footage requires regenerating its source or replacing it. **Do not add horizontal playback progress bars.** Keep `presentation.showTimelineProgress` omitted/false; chapter steps are a separate semantic overlay.
