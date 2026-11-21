---
name: cutaway
description: Explain how machines and hardware work by creating educational cutaways as interactive HTML, isometric SVG, or editable React figures. Use for requests such as "explain how this machine works" with a photo or model number, and for engines, wings, pumps, appliances, and other physical mechanisms. Identify the machine and research its internals before drawing it. Also supports requested software analogies. Doesn't cover medical anatomy or ordinary flowcharts.
---

# Cutaway

Build a cutaway that explains how the requested machine works. For a jet engine, separate core and bypass flow; for an espresso machine, follow water through the pump, boiler, and group head; for a piston engine, connect crank position to piston and valve motion.

When the user invokes Cutaway with a machine photo and asks how it works, deliver a visual explanation by default: identify it, research the mechanism, then create and attach the interactive cutaway. Identification and a written explanation are intermediate work. Honor requests for identification only, text only, or a different output.

Draw the actual mechanism when the user asks about a physical object, and use an analogy when requested. Every visible number and moving part must agree with the same model.

Name the hardware layout and explain its simplifications, such as illustrative dimensions in an engine or uncalculated airflow over a wing. When arrangement or timing affects the explanation, check an authoritative diagram or technical reference and cite it. Name each part, describe its job, and show what changes when the user operates a control.

Cutaway adapts Ryan's MIT-licensed Anatomy toolkit for ChatGPT. Its optional 2D glow layer adapts April Zhu's iso-glow, based on Tolga Cohce's iso-figure, with their MIT notices preserved.

User instructions take precedence over these defaults. Resolve the paths below relative to this skill directory.

## From a photo or model number

Use this workflow when the user asks how their particular machine works. A photo can establish its appearance and help identify it; hidden parts need other evidence. Use the host's image, search, and file tools. Keep the photo in the conversation and deliver the drawing there; this workflow doesn't upload it to Cutaway's hosted service.

1. Identify the brand and model from visible markings, controls, and the user's information. Separate a likely match from a confirmed identification. Ask for a model label only when the missing detail changes the operating principle being explained, or the user requires an exact internal layout. An unknown SKU or revision doesn't block a drawing of a documented shared mechanism. A supplied model number or manual can be enough; don't require a photo. Search by model, without serial numbers or unrelated personal details from the image.
2. Open references for that model and relevant revision. Prefer manufacturer manuals, service documents, and exploded parts diagrams; use a documented teardown when needed. Check that each source actually supports the claim. A search snippet, marketing specification, or similar-looking model doesn't establish internal placement or connections.
3. Establish the parts and connections needed to explain the requested operation. For an espresso machine, check the pump, heating system, brew path, valves, and any steam circuit being shown. Resolve conflicting references or state the uncertainty. Gather only specifications that affect the explanation; an unknown dimension can stay illustrative.
4. Choose the drawing's scope from the evidence. When references document the operating principle but not the exact internal layout, build a simplified mechanism cutaway in the same turn. Match recognizable exterior features from the photo, label internal placement and routing as illustrative, and keep unverified specifications out. A source describing the principle can support this teaching model without proving the product's construction. If the mechanism itself is unresolved, ask the specific question needed to choose it. If the user explicitly requires an exact service layout, explain the missing evidence before substituting a simplified view.
5. Build and deliver the artifact using the workflow below. Keep the identification, sources, supported claims, assumptions, and unknowns in the template's research record; the page and exports carry that context. Include labels, part selection, and controls that explain the operation. Finish with the generated HTML or supported inline preview, plus a short explanation of its scope. Don't stop at a research summary or an offer to draw when the available evidence supports the teaching model.

If browsing is unavailable, use supplied documents and state that limitation. Ask for the relevant manual when needed to establish the mechanism; don't claim to have researched sources you couldn't open. Keep source images and manuals as references, rather than embedding them in the output without permission.

## Deliver in ChatGPT

For an existing GE9X, wing, espresso, or boxer model, use the connected `open_ge9x`, `open_wing`, `open_espresso`, or `open_boxer` tool when it fits the request. The espresso, wing, and boxer views illustrate generic mechanisms. A request about a particular machine needs the identification and research above; don't present a generic hosted view as that exact model. Supply the requested component or control settings. These tools return the interactive view, source links, limitations, and downloads; don't rebuild the same model merely to display it. `list_cutaways` describes the available controls.

Use the drawing workflow below for other machines, changes to a model's geometry or styling, or when the hosted tools aren't available. Keep the hosted models' illustrative dimensions and omitted systems clear when explaining them.

Default to a light-theme, self-contained interactive HTML file with inline SVG, CSS, and JavaScript. Honor a request for static SVG, React, a different theme, or a simpler figure. Use the host's available file and execution tools. Once the necessary references are available, drawing the figure requires no MCP server, external model API, or network request.

For a custom interactive cutaway, read the [template guide](custom/guide.md). Create a writable project outside the installed plugin:

```sh
bun <skill-dir>/scripts/create-project.mjs <output-directory> --example custom
bun <output-directory>/build.mjs
bun <output-directory>/custom/validate.mjs <output-directory>/cutaway.html <output-directory>/cutaway.svg
```

Replace the template's illustrative plunger with the requested mechanism. Keep its page and controls; edit the research record, model, drawing, and render function. Use its material renderer to retain the kit's side shading and creases. The shared controls handle selection, playback, scrubbing, reduced motion, and HTML/SVG downloads of the selected view. The build also produces `cutaway.fragment.html` from the same artwork and runtime for inline previews. This template needs Bun for bundling; its validator also runs with Node.js and requires no installed dependencies.

Keep the template's **Download video** control. It exports a full cycle as a silent MP4 when the browser supports H.264 recording. It renders the same SVG from the model's frame function; don't add a separate animation or screen recorder. If export is unavailable in the preview, direct the user to the downloaded HTML. Check playback before claiming the video works; the static validator cannot verify encoding. See the [video export notes](custom/guide.md#video-export).

The validator checks script syntax, inline-preview hazards, resource references, and required structure. It doesn't execute the controls, verify sources, or establish that ChatGPT can render the file. Exercise the generated model and downloads with the host's browser tools when available; report those checks separately.

For a smaller kit example that can also build with Node.js, use:

```sh
bun <skill-dir>/scripts/create-project.mjs <output-directory>
bun <output-directory>/examples/dial-indicator/build.mjs --light
```

The initializer copies the kit, its MIT license, and a working example while preserving relative imports.

Start from that example, replace its model and geometry with the requested mechanism, and return the generated file and editable source. Don't deliver the sample unchanged for an unrelated request.

For software behavior, the initializer also accepts `--example token-bucket`, `lru-cache`, `connection-pool`, or `circuit-breaker`. These examples use Bun and emit interactive HTML and a styled static SVG snapshot:

```sh
bun <output-directory>/build.mjs --light
```

Their [models](examples/models.mjs), [drawing code](examples/drawings.mjs), and [experiment prompts](examples/catalog.mjs) are starting points for related requests.

If the host has an interactive HTML preview or Canvas tool, present the generated artifact there as well as providing the file. Use the tool's actual documented interface; don't assume arbitrary HTML in a chat message executes or invent a preview URL.

If previews are unavailable, provide the downloadable HTML. If execution is unavailable, write a self-contained artifact with the available file tools and state that it hasn’t been run. If file tools are also unavailable, provide complete source and state the limitation.

Don't install tools on the user's computer, publish a website, or create external records merely to deliver a figure. Those are separate user requests. Keep generated standalone files free of network dependencies.

Preserve Cutaway's [MIT notice](examples/LICENSE) and the applicable upstream notices when distributing source.

Keep build-time page helpers out of the inline runtime. Use `kitScript()` or a bundle containing only the runtime imports; don't paste all of `iso-kit.mjs` into a script. An unused `pageHtml()` helper embeds full-document markup inside its JavaScript and has caused inline fragment validation to fail.

When a host requests an HTML fragment, submit the generated `cutaway.fragment.html` through its documented interface. Preserve its geometry, material colors, and controls instead of drawing a separate preview. Retain the complete document as the download and include any adapted preview source in the editable project. Check the final serialized preview payload as well as the standalone file; a successful build doesn't prove the preview ran.

## Design and build

1. Identify the mechanism, quantities, states, controls, and desired output. Use supplied values and label illustrative assumptions; ask only when a missing fact changes what the figure teaches. Explain the mechanism choice in 1 sentence and proceed.
2. Read [craft](upstream/references/craft.md) for the drawing language and [kit API](upstream/references/kit.md) for the primitives you need. Inspect 1 bundled example: [dial indicator](upstream/examples/dial-indicator/build.mjs) for a moving mechanism or [desk computer](upstream/examples/desk-computer/build.mjs) for keyboard input. The latter includes upstream Anthropic artwork; replace that motif when creating a new figure unless the user requests it.
3. Define the state model before the geometry: clamp values at real boundaries, preserve quantities, and compute readouts and motion from the same state. Keep simulated time separate from rendering. For hardware, distinguish the teaching model from measured or validated performance.
4. Choose a recognizable object and plan its supports, structure, mechanism, controls, fasteners, and surface details. Use details that explain the construction: bushings support shafts, clamps hold pipes, feet support bases. Scale complexity to the request; don't impose a part quota or invent a time estimate.
5. Lay out the object in world coordinates, with z up, using the shared camera and `fitProjection` to include every extreme point. Build static geometry once and let the kit shade solids. Draw nearer parts over farther ones, splitting wrapping parts into front and back portions when necessary.
6. Compose a framed figure with a concise title, interaction hint, live readout, and an explanatory caption outside the drawing. Keep text readable at phone width. Include an accessible description and keyboard equivalents for pointer controls.
7. Read [motion](upstream/references/motion.md) when adding interaction; use time-based easing or springs and stop animation offscreen. Under reduced motion, disable the idle tour and transition directly to user-selected states. Don't put render-loop state through a React rerender every frame.
8. Open the artifact with the available tools, exercise its controls and boundary states, and check console errors. Inspect desktop and narrow layouts, both themes when delivered, and close-ups of joints and overlaps. Report which checks ran and which were unavailable.

## Drawing constraints

- Draw filled solids with thickness, correct occlusion, a common camera, and consistent lighting. Avoid floating labeled boxes when a physical mechanism can carry the explanation.
- Use subdued colors for the base and structure so the moving parts stand out. Use 1 primary accent unless color itself teaches the concept.
- Terminate lines at surfaces, edges, connections, or printed marks. Place detail on actual geometry. Texture must meet an edge or fade.
- Give pipes real endpoints and clearance. Place fittings against their mounts. For dense pipework, use the recorder and geometry audit in `upstream/kit/audit.mjs`; resolve interlocks in geometry rather than hiding them with arbitrary draw-order offsets.
- Keep moving geometry, displayed values, captions, and control labels consistent. Never hardcode a readout that disagrees with the simulation.
- Escape user-provided text in HTML, SVG, and JavaScript contexts. Don't interpolate untrusted strings directly into markup or inline scripts.

## Optional modes

Read only the references needed by the requested output:

- **Static SVG:** use `figureSvg({ standalone: "light" })` or `"dark"` to embed its styles. Provide meaningful accessible text. A static export must not depend on JavaScript for its resting state.
- **2D glow and palettes:** read [glow](glow/guide.md) when the user requests illuminated active parts or the iso-glow look. Use the bundled filters and palettes with the existing model and geometry; the examples include native style, theme, and palette selectors. Keep light mode flat, retain technical mode, and include the full [iso-glow MIT notice](glow/LICENSE) with adapted output source.
- **WebGL:** read [WebGL](upstream/references/webgl.md). Use shaders for light, water, fire, or another effect that SVG can't express well; register the canvas to the SVG camera and keep transitions smooth and effects bounded. Keep a readable SVG fallback when WebGL is unavailable, and test the light theme separately.
- **3D:** read [3D](upstream/references/3d.md). The bundled `turn.mjs`, `turn-build.mjs`, and `turn-audit.mjs` support moving groups. Keep this optional, explain that it's upstream's beta mode, and verify performance in the target host before promising smooth animation.
- **React/Next.js:** read [React integration](upstream/references/react.md). Copy the TypeScript kit and React adapters into the target project, compute static art outside the live component, and preserve the server/client split. React is supplied by the destination project.
- **Detailed visual review:** read [verification](upstream/references/verify.md) for visual failure modes. Only the dial-indicator and desk-computer examples are bundled; use the host's browser and screenshot tools for the other checks. Report which checks you couldn't run, and never claim an audit or screenshot passed without running and inspecting it.

The inlining helper provides `kitScript()`, `glScript()`, and `turnScript()`. `kitScript()` includes geometry and SVG-part helpers through `groupSvg()`. Import `figureSvg()`, `plateHtml()`, `pageHtml()`, and page styles in the build script when composing the document; they're excluded from the inline runtime.

Advanced upstream fixed-canvas and shared-context helpers aren't included. Don't call absent APIs or fetch missing code during ordinary use.

Finish with the artifact, a short explanation of the controls, the model's assumptions, and any material verification limits. Keep build details out of the figure's controls and explanations.
