---
name: spline-2d
description: "The Hana 2D authoring guides: how to design websites and app screens with 2d_write_html (the supported HTML and CSS, layout, interaction, typography, worked examples) and the effect guides for glass, 3D layers, layer noise, mobile app screens and interactivity. The same text 2d_load_skill returns. Read the authoring contract before your first 2d_write_html."
---

# Hana 2D authoring guides

These are the guides the `2d_load_skill` tool serves, bundled here so they can be read without a tool call. Each `references/<name>.md` is the guide text `2d_load_skill("<name>")` returns: wherever a guide says `load_skill("<name>")`, reading `references/<name>.md` is the same.

Before your first `2d_write_html`, read the authoring contract, in order:

- [references/authoring-guide.md](references/authoring-guide.md): Part 1 of 2 of the HTML+CSS authoring contract — how authoring works, frame sizing & workflow, the supported tags, and the visual styling rules (layout, color, borders, shadows, hover/pressed states, links). Load this AND authoring-guide-2 once before authoring.
- [references/authoring-guide-2.md](references/authoring-guide-2.md): Part 2 of 2 of the HTML+CSS authoring contract — interaction (click / hover / key actions, <details>), entrance & cursor motion, typography + the font catalog, the authoring-discipline checklist, worked examples, self-review via review_frame, and the code↔canvas round-trip (export_html for propagating design changes back to source code; upload_assets + CSS-art fidelity when reproducing a design from a codebase). Load this AND authoring-guide once before authoring.

Read a topic guide when the task needs it:

- [references/3d.md](references/3d.md): Hana's two 3D layer effects, authored as `filter` functions: `hana-3d(...)` (turns a flat shape into a real lit PBR mesh — extruded silhouette, glossy sphere, or torus; for orbs, metal knobs, glass blobs, extruded 3D headlines/logos, donuts/rings) and `hana-projection(...)` (wraps the element's own picture around a 3D sphere/cylinder — can/mug/bottle labels, globes/planets, curved banners). Load before authoring anything that should look three-dimensional, physically lit, or wrapped onto a curved surface.
- [references/glass.md](references/glass.md): Hana's two real glass backdrop effects, authored as `backdrop-filter` functions: `hana-liquid-glass(...)` (a refractive lens that bends, lenses, and magnifies the backdrop — Apple-style 'liquid glass') and `hana-noise-glass(...)` (a procedural-noise distortion — rippled / textured / frosted-organic glass, water, heat-haze). Load before authoring any glassy lens, refractive panel, magnifying chip, textured/rippled glass, or warping translucent overlay. Neither is the flat `backdrop-filter: blur` frosted look.
- [references/layer-noise.md](references/layer-noise.md): Hana's Layer Noise effect, authored as the `filter: hana-layer-noise(...)` function — a procedural-noise distortion of the element's *own* content (its fill, text, or image), for wavy / rippled / melting / heat-haze / organic-warped looks. Load before warping a shape, text, or image with noise. It's the *layer* sibling of `hana-noise-glass` (which distorts the backdrop instead) — don't confuse the two, and it's not the flat `filter: blur`.
- [references/mobile-app.md](references/mobile-app.md): How to design a proper native mobile app screen (iOS / iPhone, and Android) — the two non-negotiable foundations: a **rounded root frame** (device-screen corner radius + `overflow: hidden`) and a **standard status bar pinned at the top** (time + signal/wifi/battery). Includes ready-to-paste status-bar markup. Load this the moment the task is a phone-app UI (390–430px wide), before authoring the screen.
- [references/interactivity.md](references/interactivity.md): Make objects respond to clicks, hovers, keypresses, or page load — state machines, transitions, show/hide, link out. Load whenever the user wants something to animate, react, toggle, or behave like a prototype.
