---
name: colored-reliefs
description: Use Print Ready for printable artwork that fits a flat, limited-palette image. Signs, nameplates, birthday and milestone placards, logos, badges, magnets, coasters, ornaments, line art and shallow raised decoration. Use this skill when the request implies this workflow, even if the user never mentions reliefs, color swaps or 3MF.
---

# Colored reliefs

Choose a relief when the design reads from the front and a few flat colors can describe the shapes. For an object with measured mating features, model those features with the Print Ready skill and use this workflow for the artwork if needed.

1. Choose the print size and palette, then **call the host's ImageGen tool first for every relief design**. Default to four filament colors including the base. Use the loaded colors when specified and honor requests for more within the tool limit. Pass any user-supplied reference image into that same ImageGen call, even if it already looks flat. Use the prompt below. If ImageGen cannot run or cannot accept the reference, explain the blocker and stop before tracing.
2. Inspect the generated image for the intended subjects, lettering, outline, and assignment of colors. Regenerate with more specific instructions if a feature is wrong or a filled region uses an extra color. Use only the generated illustration as print artwork. Keep the original photo, logo, sketch, or screenshot in the host.
3. Check the selected Print Ready connection with `get_capabilities`. If an explicitly selected connection is unavailable or reports a different environment, stop and explain. Call `prepare_model`, then submit the generated PNG to `create_colored_relief` with the ordered `palette`, `width_mm`, brief, decisions, and `imagegen_used: true`. Put the base first and use `footprint: "silhouette"` for a transparent cutout. Use a host file input for the generated image when available, or its reachable HTTPS URL or PNG data URL. If the host cannot pass the generated file, ask the user to download that specific ImageGen result and attach its PNG. Resume from that result. Keep the same preparation on retry.
4. Poll `get_model` and compare the real top preview and flattened PNG with the generated art. Check the major color regions, lettering, holes and thin details. For a deliberate filament substitution use `refine_artwork` with `palette` and `color_map`, inspect the flattened result for merged features, and pass the ready artwork handle to `create_colored_relief`. Use `trace_artwork` when the outlines need inspection. For an artwork revision, pass the previous generated image and requested changes to ImageGen. For a size or layer change, reuse the generated artwork. Use a new preparation and `previous_model` for revisions.
5. Call `show_model` for the ready relief and offer its separate STL and 3MF downloads. Report planned filament changes and layer heights when relevant. If the host cannot show the viewer, provide the actual preview and both file links from `get_model`.

## ImageGen prompt

Fill in the bracketed fields with the design and chosen palette. Include the reference sentence only when an image is attached to the ImageGen call.

> Create a straight-on, flat 2D print-face illustration of [subject, layout, and aspect ratio] for a [width in mm] wide 3D-printed relief. [Use the attached image as the visual reference. Preserve its recognizable shapes, layout and requested details. Simplify only as needed for the stated palette and printable feature sizes.] Use exactly these [count] solid colors and no others: [color name and #RRGGBB for each color]. Fill the base with [base color], and use [explicit colors for the border, lettering and each main shape]. Use [exact quoted lettering, or no text]. Keep edges crisp and features broad enough for the print size. Use large, contiguous fills. Exclude gradients, shadows, texture, highlights, perspective and mockup scenery. [For a cutout, make everything outside the silhouette transparent. For a full plaque, fill the entire intended face with the base color behind the artwork.]

## How to keep swaps low

Use one continuous Z band per color. Every point on the print face shows its assigned color. That material extends down to the next transition. Each lower band supports the footprints of every band above it. Print Ready checks both ends of each compiled band against the flattened artwork. Four colors take three planned changes, with the first material already loaded. Apply one print profile to the whole relief. The defaults are a 0.20 mm first and regular layer, eight base layers, and four layers per raised color. Honor a supplied printer profile's first and regular layer heights. Each band should contain enough layers to print reliably and hide the filament beneath it.

Use the Bambu Studio format for slot assignments when that slicer is the target. Use standard 3MF with material colors when the slicer is unknown or the user requests it. Both formats use the slicer's printer profile. Set the band heights for that profile and tell the user the matching layer height when it matters. Keep the base and bands together in one object. Create unrelated pieces such as separate milestone tokens as their own objects.

For a design that needs colors at the same height, or parts the user needs to scale independently, use `create_3mf` with named model handles and material colors. Provide a shared `object` name for bodies that need to keep their registration. The independent 3MF tool also works with ordinary CAD models.
