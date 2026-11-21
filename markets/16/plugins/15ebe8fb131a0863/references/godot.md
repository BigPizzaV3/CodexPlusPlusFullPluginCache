# Godot development reference

Official stable docs: https://docs.godotengine.org/en/stable/ and command-line guide https://docs.godotengine.org/en/stable/tutorials/editor/command_line_tutorial.html

Use an installed editor version, not an assumed one. For 4.x use correct CharacterBody2D/3D APIs and scene/node signal wiring. For web targets verify current GDScript/C# and export constraints, required templates and browser support.

Potential CI commands only when installed and matching version:
- `godot --headless --path /path/to/project --editor --quit` for import and script parse checks.
- `godot --headless --path /path/to/project --quit-after 30` for a limited scene smoke run (may require main scene).
- `godot --headless --path /path/to/project --export-release "Preset name" /path/to/output` if export templates and preset are present.

Headless success does not prove gameplay input, graphics, audio or user experience. Test interactively where possible.
