# SVG & 3D Design

Create editable SVG illustrations, custom icons, Blender scenes and parametric CAD from a brief or visual reference. The plugin packages the SVG & 3D Design skill and its supporting guides and validation helpers.

Install it when you want these workflows. Installation does not add an MCP server, lifecycle hook or background service. Once installed, the skill can be selected for relevant requests or invoked explicitly.

## Requirements

Use a desktop session with local execution and tools appropriate to your chosen output:

- SVG checks: Python 3 and Pillow, plus a renderer capable of exporting the SVG to PNG.
- Blender scenes and rendered icons: Blender.
- Functional CAD: a compatible CAD environment such as CadQuery.
- New image references: image generation in the host. You can also provide an existing reference image.

The plugin does not install these dependencies or supply image-generation access. Its Python helpers use only the standard library and Pillow. Use a Python environment with Pillow already installed, or install Pillow into your project's environment before running them.

## Example requests

- Create an editable SVG app icon for a birdwatching journal, with a matching PNG preview.
- Rebuild this illustration as an editable SVG and compare the result with the reference.
- Create an editable Blender scene for a ceramic desk lamp, with a rendered preview.
- Make a parametric CAD mounting plate from these dimensions and export STEP and STL.

## Validation helpers

Paths below are relative to this plugin's root. Replace the example paths and dimensions with those of your actual exports.

```sh
python3 skills/svg-3d-design/scripts/check_svg_budget.py /path/to/final.svg /path/to/final.png --width 512 --height 512
python3 skills/svg-3d-design/scripts/review_alpha.py /path/to/final.png
python3 -m unittest discover -s skills/svg-3d-design/tests
```

The SVG budget helper checks dimensions, PNG integrity and relative file size; it does not prove that the PNG depicts the SVG. The alpha helper flags enclosed transparent regions for visual review, not automatic removal.

Inspect final exports at their intended size and try a representative edit in the saved source. Complex artwork may need iteration. Valid CAD geometry and a rendered preview do not establish physical fit or manufacturing suitability.
