# Editable deck specification and complete build

Use the installed presentation skill's runtime, operation marker and finalization requirements. This plugin runs in a file-authoring environment with Node.js and `@oai/artifact-tool`; it has no hosted renderer. Design/image generation happens through the agent's available ChatGPT tools before this local builder runs. Do not claim that a script calls ImageGen.

## Build command

Before the first build in a task, run the current presentation operation marker once. If delivering a PDF, also follow the PDF skill's marker before PDF creation. Then run:

```bash
"$CODEX_PRIMARY_RUNTIME_NODE" /absolute/skill/scripts/build_deck.mjs \
  /absolute/project/spec.json /absolute/project/output/deck.pptx \
  --expect /absolute/project/expectations.json \
  --workspace /absolute/project --work-dir /absolute/project/build/run-1 \
  --compatibility required --pdf
```

Choose a new output and private work directory for each revision. Omit `--pdf` when no PDF deliverable is needed. `--compatibility required` is the default: it requires the bundled LibreOffice runtime, saves a native PPTX through it, and renders the final deck independently with LibreOffice. `auto` permits an unavailable compatibility runtime with a recorded limitation. `off` is only for a explicitly requested narrow build and never proves phone compatibility. Conversion and audit failures fail the build rather than silently returning the raw draft.

The builder uses `CODEX_PRIMARY_RUNTIME_NODE`, `CODEX_PRIMARY_RUNTIME_PYTHON`, `CODEX_PRIMARY_RUNTIME_NODE_MODULES`, and `CODEX_PRIMARY_RUNTIME_ROOT` (or `CODEX_PRIMARY_RUNTIME`). Use `--presentation-skill-dir` only when the current presentation skill has a different installed path.

The final JSON identifies the PPTX, optional PDF, two preview sets and compatibility checks. `phoneRenderingVerified` remains false. Inspect all final slide PNGs and the `office-slide-*.png` previews before saving/delivering. Private evidence stays in the work directory. Fonts are preserved but not embedded; explain required fonts when they affect the user's display.

## Input specification

```json
{
  "slideSize": {"width":1280,"height":720},
  "fontFamily":"Arial",
  "fontFamilies":["Arial"],
  "slides":[{"background":"#ffffff","notes":"Sources and useful speaker notes","elements":[
    {"kind":"text","role":"title","name":"Slide title","x":64,"y":48,"w":820,"h":80,"text":"Example heading","size":42,"bold":true,"color":"#14243C"},
    {"kind":"text","role":"thesis","name":"Main thesis","x":64,"y":180,"w":640,"h":160,"text":"Substantive body text","size":32,"color":"#14243C"},
    {"kind":"image","role":"logo","name":"Original logo","path":"./assets/logo.png","x":1070,"y":24,"w":80,"h":80,"fit":"contain","alt":"Supplied logo"},
    {"kind":"image","role":"photo","name":"Photograph","path":"./assets/photo.jpg","x":740,"y":160,"w":440,"h":480,"fit":"cover","alt":"Photograph"}
  ]}]
}
```

`x,y,w,h,size` are CSS pixels at 96 DPI. Derive template dimensions from their exact EMU dimensions divided by 9525. List all authored and retained template fonts in `fontFamilies`. Relative image paths resolve against the specification directory. Obtain image bytes from supplied files, sourced photos or ImageGen, and inspect them before authoring.

Exactly one authored text element on each slide must have `role: "title"`. Other text roles describe content and do not create styling. Set sizes, fonts and emphasis explicitly so the title and thesis read differently. Text supports `font`, `italic`, `align`, `valign`, `wrap`, `insets` and `lineSpacing`; authored text always disables autofit. Use current native APIs for rich inline runs, connectors or focused edits.

For every authored slide, provide one unique audit rule with `nativeText: true`, `noAutofit: true` and every authored text block in `requiredTexts`. Cover each authored table/chart in the corresponding minimum count. The builder rejects incomplete audit coverage before rendering. Use unique zero-based existing-slide targets; absent or null `targetIndex` means an appended slide.

Logos are optional. Omit the example logo element entirely when the user supplies or requests no logo; no placeholder, institutional header or source deck is required. Mark any supplied original logos `role: "logo"`. The pipeline records their input hash and expected frame and checks the exported image bytes at that placement before and after compatibility conversion. A logo that is substituted, rasterized into the background, lost or enlarged fails that check. Keep logos independent from ImageGen artwork.

Use `{"kind":"table","config":<current Artifact Tool table config>}` for native tables and `{"kind":"chart","chartType":"bar","config":<current chart config>}` for native charts. Use native shapes only for meaningful editable diagrams, not decorative artwork.

## Existing decks

Set `baseDeck` to import a PPTX. To reconstruct a source slide, use zero-based `targetIndex` and `replaceContents: true`. The renderer removes owned shapes/images/tables/charts before adding the new composition and resets that slide's background; it retains unrelated slides. Reuse required source content and branding in the new specification. A mere blank template slide can still contain a picture or background; do not assume it is empty.

Omit `targetIndex` to append a slide. `expectations.slideCount` must describe the full resulting deck, including retained slides. For a small focused edit, use the native API instead of clearing the source slide, then run package normalization, compatibility conversion, audit and current finalization on its exported draft.

## Expectations

```json
{"slideCount":1,"slides":[{"slide":1,"nativeText":true,"noAutofit":true,"requiredTexts":["Example heading","Substantive body text"],"nativeTables":0,"nativeCharts":0}]}
```

Include substantive body text and requested exact labels. Apply `noAutofit` to authored slides; do not silently change an unrelated cover's original fitting. Request native charts/tables when relevant. The audit checks the ZIP, native content, required text and fitting; the finalizer checks structure, canvas, fonts and layout geometry. Neither replaces visual review nor actual inspection in a user's application.

## Lower-level helpers

- `render_deck.mjs SPEC NEW-DRAFT.pptx`: build native objects, draft previews/layouts and inspection evidence.
- `prepare_package.py DRAFT --output NEW-CANDIDATE [--size CX,CY] [--contracts CONTRACTS]`: normalize media names, restore known exact dimensions and check original-image contracts. Never alter dimensions merely to silence a mismatch without grounding them in the reference.
- `audit_pptx.py PPTX --expect EXPECTATIONS`: inspect native content and text editability.

Use the full builder by default. Do not repeat manual export/rename/office-conversion steps that it already performs.
