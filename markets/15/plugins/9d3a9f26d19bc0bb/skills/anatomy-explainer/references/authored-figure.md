# Authored Anatomy figures in a video project

Use this contract after researching the explanation and authoring its complete object with the bundled upstream kit. The object can contain static SVG, dynamic SVG/HTML, Canvas or WebGL. It does not need to be converted to a limited list of JSON primitives or to a GLB.

## Source and build

Keep, for example, `sources/explainer/build.mjs`, `model.mjs`, geometry modules, research notes and the exported `figure.anatomy.json` in the user's working project. Resolve the pinned kit from the installed plugin root. Original build source stays editable; imported figure assets are immutable snapshots. Do not modify the installed kit or upstream examples to generate a project.

Write a Node build script that uses the original `iso-kit.mjs`, `lathe.mjs`, `tube.mjs` and other modules relevant to the subject. Use upstream `scripts/inline-kit.mjs` helpers when browser logic needs the kit's functions. A static SVG needs only its generated markup and CSS. A dynamic figure packages required functions and model data into its factory string, with no Node APIs or unresolved imports in browser code. Keep a standalone preview page when needed for the upstream capture and audit tools.

The exported JSON has this shape:

```json
{
  "schemaVersion": "1.0",
  "width": 1600,
  "height": 1000,
  "markup": "<div data-anatomy-camera><svg viewBox=\"0 0 1600 1000\"><g data-anatomy-part=\"assembly\">...</g></svg></div><output class=\"model-readout\">...</output>",
  "css": "...embedded upstream and authored styles...",
  "script": "(root) => { /* model and kit functions */ return { renderAt(time, context) { /* draw this exact state */ } }; }",
  "parts": [{"id":"assembly","label":"Functional assembly","group":"mechanism"}],
  "provenance": {
    "sourceCommit": "1482e8469b0a9e0d8cc18ea2740a01423d29ae80",
    "license": "MIT",
    "buildSource": "sources/explainer/build.mjs"
  }
}
```

The abbreviated markup and function above describe the protocol, not a renderable visual template. Supply the complete object. `parts[].id` is required and unique; `label` and `group` are optional semantic notes. Give the corresponding visible elements `data-anatomy-part="assembly"`; a functional assembly can wrap several solids and details. Use meaningful IDs so focus can select an entire subsystem. Avoid overlapping nested focus wrappers that compound dimming; prefer disjoint top-level assembly wrappers. Provenance describes the actual authored work and its dependencies; a kit's MIT license does not override another asset's license.

The script is a self-contained function expression receiving the figure root element. It returns (or resolves to) an object with `renderAt(time, context)` and optionally `ready`, `dispose()` and a `diagnostics` array. The context contains `{sceneTime, modelTime, filmTime, focusPartIds}`; model time is the first argument as well. `sceneTime` is relative to the scene start and `filmTime` is on the full timeline. `renderAt` may return a Promise. `ready` resolves only after the figure's own required resources are usable. Diagnostics use `{code, message, severity: "warning" | "error"}`. Render failures must throw or reject so they cannot silently become blank footage. Use only root-scoped DOM lookups, and keep the object's coordinate system at its declared width/height.

`renderAt` receives explicit **model time in seconds**. Derive all poses, counters, readouts and effects from that time. A useful pattern is a pure `stateAt(time)` which returns positions and derived quantities; use the same result to update the geometry and its readouts. Do not accumulate motion from previous calls, use `Date.now()`, `performance.now()`, `requestAnimationFrame`, timers or unseeded randomness. A call sequence `0 → 3 → 1 → 3` must reproduce the same state at 3 seconds. Reset visibility, styles and effects which are conditional on time. Interactive input may belong in a separate local preview; exports must remain controlled by explicit time.

Keep the figure self-contained: embed images/fonts only when needed, include required browser functions, and do not fetch a CDN, external URL or local absolute path at render time. Network requests are blocked in the authored frame. Put film titles, narration subtitles and long explanatory text in Wandeo's 2D layers so they remain readable during a figure close-up. Readouts attached to the physical object may remain in the figure and move with it. To keep model values or a formula at a fixed corner while zooming into geometry, use the optional camera wrapper below.

## Separate geometry from fixed readouts

Use exactly one **HTML** element marked `data-anatomy-camera` when the figure needs a fixed HUD. Put the SVG/Canvas geometry inside it and put model-linked readouts/formulas as siblings inside the figure root:

```html
<div data-anatomy-camera style="position:absolute;inset:0">
  <svg viewBox="0 0 1600 1000" width="1600" height="1000">
    <g data-anatomy-part="assembly"><!-- complete authored geometry --></g>
  </svg>
</div>
<output class="model-readout" style="position:absolute;right:48px;top:32px">
  <!-- update this from the same stateAt(time) as the geometry -->
</output>
```

The camera wrapper occupies the whole original `width × height` canvas. The runtime owns its `transform` and `transform-origin`; do not set or overwrite those properties in authored CSS or script. Transform moving objects inside the wrapper instead. More than one camera wrapper, a non-HTML camera wrapper or an author-supplied wrapper transform is an error.

With this wrapper, `view.frame` transforms only the geometry. Sibling HUD/readouts retain their full-canvas position and scale, including during local zoom. `root.querySelector(...)` can still update both geometry and readouts from the same model state. Keep HUD elements outside `data-anatomy-part` wrappers when they should remain fully readable during emphasis, and inspect that focused geometry does not visually collide with them. Put narration subtitles and long text in Wandeo's 2D layers.

Without a camera wrapper, the entire authored figure continues to follow `view.frame`, including any readouts. Use this legacy behavior deliberately for an object whose labels should move with it.

## Import once, reference many times

```text
wandeo anatomy import --project <work> --input <work>/sources/explainer/figure.anatomy.json --license MIT
```

Use the returned asset's `id` (`result.id` in the CLI JSON envelope). Add optional `--url` only for a real source URL. Import validates and copies the JSON; it does not execute the author's build script. If the source changes, rebuild and import a new snapshot, then update the project mapping. Do not edit the registered asset in place.

At the top level of `project.json`:

```json
"anatomyFigures": {
  "device": {"assetId":"IMPORTED_FIGURE_ASSET_ID"}
}
```

Each relevant scene uses the same figure:

```json
"spatial": {
  "backend":"anatomy",
  "camera":{"projection":"orthographic","position":[4,3,6],"target":[0,0,0]},
  "models":[],
  "anatomy":{
    "figureId":"device",
    "view":{
      "timeOffsetSeconds":0,
      "timeScale":1,
      "keyframes":[
        {"atSeconds":0,"frame":{"x":0,"y":0,"width":1,"height":1},"focusPartIds":["assembly"],"dimOpacity":1},
        {"atSeconds":2,"frame":{"x":0.3,"y":0.2,"width":0.45,"height":0.45},"focusPartIds":["assembly"],"dimOpacity":0.2}
      ]
    }
  }
}
```

The camera remains in the spatial schema for compatibility; the authored figure owns its geometric projection. `view.frame` is a normalized crop of the authored canvas, not a Three.js camera. With `data-anatomy-camera`, it affects the geometry wrapper while sibling HUD/readouts stay fixed; otherwise it frames the whole figure. Choose a crop using inspected geometry and keep the causal connection or enough surrounding structure visible. `frame` interpolates smoothly between keyframes and fits the selected region while preserving aspect ratio. `focusPartIds` refers to IDs in the imported figure's `parts` list and switches at the corresponding keyframe; an empty focus list clears emphasis. `dimOpacity` is in `[0,1]`, interpolates between keyframes and controls the surrounding context, not the caption opacity. To fade toward a new focus smoothly, establish its focus IDs at an earlier keyframe with `dimOpacity: 1`, then lower that opacity at the next keyframe. The author must retain valid hidden/cut-away states when emphasis changes.

View `atSeconds` values are relative to the scene start. Model time is:

```text
modelTime = timeOffsetSeconds + sceneLocalTime × timeScale
```

For a second shot that continues the same object after a four-second first shot, use an offset of 4 when the first shot's rate is 1. At another rate, compute the end model time rather than copying the film timestamp. A zero rate is a deliberate freeze. A reset is allowed when the explanation calls for a replay, and should be visually clear. A fast-forward demonstration needs a stated multiplier when it would otherwise misrepresent speed.

The compiler binds `authoredFigure` from the registered asset. Never write this internal field, `assetPath`, raw script or file paths into the scene. Figures remain reusable by stable IDs; their frozen data and hashes travel with the render context.

## Acceptance and delivery

First inspect the complete object without film decorations. Run the upstream checks appropriate to the chosen SVG/WebGL/3D path and keep their reports with the source. Then test a short film segment with an overview, a focused assembly and an observable result. Compare full-size, important 4× junction crops and a 390 px-wide image. Check stable assembly positions, correct occlusion, connections, tone hierarchy and that dimming preserves context. Confirm every displayed number has the same source model as the movement it describes.

Use `project validate`, `render preview` and `review`. Inspect runtime diagnostics and figure-source evidence as well as pixels. Imported authored figures report backend `anatomy-authored` and engine `project-authored anatomy`, along with their figure ID and source identity. They are not necessarily `TURN.mount` and must not be reported as that engine unless they use it. A repeated timestamp must produce the same image, and a meaningful action must change the relevant pixels. Finish with the final MP4, applicable subtitles, editable project, figure source and review findings. Do not describe a render or a simulation as verified until the corresponding check has actually run.
