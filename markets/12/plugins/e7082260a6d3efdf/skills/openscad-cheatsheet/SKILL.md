---
name: openscad-cheatsheet
description: Look up OpenSCAD syntax, built-in shapes, transforms, boolean operations, extrusion, modules and functions while writing or debugging SCAD source for Print Ready.
---

# OpenSCAD language reference

Read the [downloaded official cheatsheet](references/cheatsheet.md) for syntax and follow its original manual links for details. The [HTML snapshot](references/cheatsheet.html) preserves the original sheet and resolves its relative assets against the source website. Attribution and source links remain in both references.

Use millimetres for Print Ready, while OpenSCAD itself is unitless. The sheet is labeled v2021.01 upstream; query `get_capabilities` for the actual compiler and limits. `include <BOSL2/std.scad>` loads BOSL2 rather than a built-in language feature. Use the separate BOSL2 cheatsheet for its additional modules. Compile source and inspect actual previews before handing off geometry.

MCP-only clients can call `get_openscad_cheatsheet` to read this skill and its linked Markdown reference. Reading documentation does not open the welcome guide.
