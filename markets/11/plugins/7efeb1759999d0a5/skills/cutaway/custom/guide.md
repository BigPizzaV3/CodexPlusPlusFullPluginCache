# Custom cutaways

Initialize with `--example custom`. The project builds `cutaway.html`, `cutaway.fragment.html`, and `cutaway.svg` with Bun, without installing dependencies. Edit the copied files in `custom/`; keep the installed skill intact.

| File | What to change |
| --- | --- |
| `research.json` | Identification, reference URLs, supported claims, assumptions, and unknowns. |
| `model.mjs` | Title, explanation, selectable parts, cycle duration, reduced-motion steps, initial view, and the pure `frame(progress)` function. |
| `drawing.mjs` | Original SVG geometry. `drawing(initialFrame)` returns `{ diagram, view }`; `view` holds projection or other data the browser needs. |
| `runtime.mjs` | The render function passed to `mountCutaway`. Update SVG attributes from the supplied frame. |

The shared page, controls, and builder usually need no changes. Use the existing SVG kit for geometry. Read the kit and craft references linked from the skill when choosing primitives and arranging parts.

## Materials and depth

Use `solid(shape, material)` from `materials.mjs` to render kit solids. It keeps the side-shading paths, top, creases, and outline. Drawing only `shape.fill` and `shape.top` discards the lighting that gives cylinders and housings their volume.

```js
import { materials, solid } from "./materials.mjs";

const motor = solid(cylinder(x, y, radius, z, height, projection), materials.steel);
const housing = solid(slabOf(plan, z, height, projection), materials.black);
```

The built-in materials include black, steel, ceramic, brass, and coffee. A custom material supplies `fill`, `top`, `edge`, and four `shades` from dark to light. These colors live on the SVG paths, so the drawing doesn't depend on page CSS. Use material and edge detail to distinguish parts; reserve saturated color for the operation being explained. Keep recognizable housing features, mounts, and fittings when simplifying the geometry.

## Research record

`identification` has a `name`, `status` (`confirmed`, `likely`, `unknown`, or `generic`), and a `detail` explaining the evidence or uncertainty. A family resemblance in a photo can support a likely match; it doesn't establish a revision or internal layout.

`sources` maps short IDs to `{ label, url, note }`. Use public HTTPS URLs and make `note` explain the source's scope. A patent may establish a mechanism's principle without documenting the photographed product. A product page may establish features without establishing component placement.

`claims` is an array of `{ text, sources: [sourceId] }`. Include only claims supported by references you actually opened. `assumptions` and `unknowns` are arrays of short statements. An illustrative model with no documented product claims can leave `sources` and `claims` empty; don't fabricate citations to satisfy the template.

An unknown production layout can stay in `unknowns` while a documented operating principle supplies the drawing. For example, a source may establish central water entry and centrifugal extraction without locating the pump inside a particular housing. Draw that supported flow with illustrative placement unless the user requires an exact service layout. Complete the artifact rather than ending with the research record.

The page shows these distinctions and links. SVG downloads include a visible identification and model note, plus the full research record and licenses in their metadata. Keep the model's `note` explicit about any uncertain layout. Do not add source photos, personal details, serial numbers, or file metadata to the record.

## Model and drawing contract

- Progress is normalized from 0 to 1. `frame(progress)` returns `title`, `description`, and the mechanism-specific values needed to draw that instant. Keep motion and readouts derived from that state. Clamp boundaries and avoid non-finite values.
- `cycleSeconds` controls illustrative playback duration. `steps` is an increasing array from 0 to 1 for reduced-motion navigation. Neither implies measured machine timing.
- `parts` contains `{ id, title, description, sources: [sourceId] }`. Each ID must appear in the SVG as `data-part="id"`. Repeated groups can represent the same part. The page supplies keyboard-accessible selection buttons.
- `state` supplies `{ progress, part, exterior }`. Draw that initial state so the built SVG and the page before JavaScript runs are accurate. Downloads from the running page preserve the current view and reopen paused.
- `render({ root, diagram, state, view })` updates the drawing. Write changing appearance into SVG attributes, including flow opacity and transforms, so the SVG export preserves it. Avoid CSS rules that depend on HTML ancestors; those ancestors aren't present in a standalone SVG.
- Add an SVG group with `id="exterior"` to enable the exterior toggle. The controller owns its opacity. Keep it clear of pointer events so underlying part selection still works.
- The static geometry needs a finite `viewBox` and accessible description. Keep SVG styles and resources inside the SVG. Use original vector geometry; the validator rejects embedded media and external resource references.
- Keep build helpers in `build.mjs`, `drawing.mjs`, or `page.mjs`. The browser entry point is `runtime.mjs`; only import runtime code there. Importing a whole page helper can reproduce the inline-preview failure.

## Video export

Keep **Download video** and the bundled `video.mjs` when adapting the template. The exporter drives `frame(progress)` through a complete cycle, rasterizes the same SVG, and records a silent 1080 × 1080 H.264 MP4 at a target of 30 fps. The clip includes the title, identification status, stage captions, and scope note. It has no microphone, screen capture, uploads, or source-photo metadata. Browser encoding may add technical container metadata.

Export duration is limited to 4–30 seconds, followed by a short final hold. This changes playback speed for cycles outside that range; timing remains illustrative. Keep animation derived from the supplied frame, including flow positions and rotation. CSS-only animation and page-dependent SVG styles won't reliably survive rasterization.

The controls restore the previous view after success, cancellation, or failure. Hiding the tab cancels the export. The browser must support MP4/H.264 recording; WebM is never renamed as MP4. If a preview cannot export video, use the downloadable HTML in a current Chrome or Safari browser. A completed export keeps a **Save MP4** link for downloads that need another click.

Test the actual MP4 in the target browser and ChatGPT preview. Check the complete cycle, readable captions, no audio, cancellation, and restored controls. Before describing the file as ready for X, test an upload. Existing generated files need regeneration to acquire this control.

## Check and deliver

Run `bun build.mjs`, then `bun custom/validate.mjs cutaway.html cutaway.svg` from the generated project. The validator also accepts `node`. It parses inline JavaScript without executing it, checks the research references and template controls, catches non-finite SVG attributes, and inspects static resource references. It is a build check, not a security sandbox or proof of runtime behavior.

Open the generated HTML with the host's browser tools when available. Scrub to meaningful states and both boundaries; select parts, play, pause, reset, and test reduced motion. Download both formats: reopen the HTML paused at the selected state and inspect the static SVG, its scope note, and sources. Check narrow and desktop layouts. A mechanism-specific check should assert an observable relationship, such as water stopping at the end of brewing, rather than just finding the controls.

For a host that accepts an HTML fragment, read and submit the generated `cutaway.fragment.html`. It contains the same SVG, styles, research, and runtime as the standalone page, without document-level markup. Its styles and controls are scoped to `.cutaway-root`; the root sets its own light background and text colors. Use one cutaway per preview.

Preserve that generated artwork and runtime when adapting to a preview tool's documented requirements. Rewriting the drawing or controls creates a second version that the standalone checks don't cover. If the host rejects the payload or changes its styling, keep the standalone download and state the preview limitation. Save any adapted preview source alongside the editable project so it can be compared with the download.

Provide the HTML, static SVG when useful, and editable project. Inspect the actual preview when tools allow it, and report unavailable browser or ChatGPT checks plainly.
