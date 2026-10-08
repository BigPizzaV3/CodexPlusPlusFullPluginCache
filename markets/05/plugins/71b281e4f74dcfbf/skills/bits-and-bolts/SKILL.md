---
name: bits-and-bolts
description: Browse, inspect, and pick reusable CAD parts with Bits & Bolts Remote.
---

# Bits & Bolts Remote

Use the tools from this plugin's connected app.

Use the Parts Library to browse CAD models and the registered file viewer to inspect them. Call `cad.pickFile` only when the user explicitly asks to pick, choose, or select a CAD file.

## Inspect a part together

Keep the conversation centered on the user's part and intended use. Open the library to find a component, or open a supplied CAD file. Viewer resources prefer the expanded view when the host supports it. Open one library surface: use `cad.tray` when the user asks for the side panel, otherwise `cad.library`; do not call both for the same request. Read the mounted viewer before changing its camera or display, and preserve the user's part, note, and geometry unless they ask to change them.

Treat a selected surface point and its view as a concern to discuss, not a measurement. Report displayed dimensions as overall bounds. State when the source has no units and millimeters are assumed. Do not infer fit, tolerances, or manufacturing readiness from sample geometry.

When the user asks to compare against other parts or drawings, use `cad.pickReferences` and read the returned resources that are available. When they ask to review requirements, use `cad.reviewForm` with the current catalog `partId` when known. Use accepted answers to discuss the requested tolerance and priority against the available evidence. A canceled form changes nothing; accepted answers are conversation input, not a saved review or manufacturing approval.

Keep inspection notes and views attached to their originating conversation. Offer a separate discussion only when the user wants one. Link back to the same part when referring to it, and use file opening, saving, and export only when the host supports them. Exporting STL preserves mesh geometry, not a parametric feature history.
