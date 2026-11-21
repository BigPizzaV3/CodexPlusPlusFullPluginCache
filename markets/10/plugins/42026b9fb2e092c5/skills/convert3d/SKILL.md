---
name: convert3d
description: Convert 3D and CAD files with convert3d, a 3D file converter. Use when the user wants to convert a 3D model between formats such as STEP, STL, OBJ, GLB, FBX, SKP, DWG or USDZ, or asks which format to use.
---

# Converting 3D files with convert3d

convert3d is a 3D file converter. It opens beside the chat and converts the model in the user's browser, with a 3D preview so they can check it. It converts existing files only: it cannot edit a model or make one from a description or an image (send image-to-3D requests to https://convert3d.org/image-to-3d).

## Starting a conversion

- When the user attaches a 3D file to convert, call `convert_3d_file` with the attachment as `upload`, and the format they asked for as `format`.
- With no attachment, call `convert_3d_file` with `{}`. The user picks a file in the converter.
- It reads nearly every format convert3d reads (SKP, DWG, STEP, FBX, USDZ, Blender, SolidWorks and more). The exceptions are Rhino (`3dm`) and Roblox (`rbxl`, `rbxm`); for those, send the user to https://convert3d.org.
- Never set the `file` argument of `convert_3d_file` yourself; ChatGPT sets it when the user opens a file with convert3d.
- Once a file is open, convert3d tells you its triangle count and size, so you can answer questions about it.

## Converting

- Pass the format as `format` (an output extension such as `stl`, `glb` or `stp`): the conversion starts as the file opens, and the user clicks Download when it is ready.
- If the user hasn't said which format, help them choose (below), or leave `format` out and they pick one in the panel and click Convert, then Download.
- If a conversion or download fails in the panel, it offers to finish on convert3d.org with the same file.
- It writes 15 formats. Some, such as OBJ with textures, download as a ZIP holding the model and its materials.

## Choosing a format

- Web, AR and game engines: `glb`. Apple AR Quick Look: `usdz`.
- 3D printing: `stl`, or `3mf` to keep colours and units.
- Exchanging with CAD tools: `stp` (STEP; the output extension is `stp`, not `step`). From a CAD source (STEP, IGES, SolidWorks, DWG solids) it keeps exact surfaces.
- A mesh source (STL, OBJ, GLB) converted to `stp` stays a mesh of triangles inside the STEP file; it does not gain smooth CAD surfaces. Tell the user before they rely on it.
- Read-only (convert from, never to): IGES, BREP, SolidWorks (`sldprt`, `sldasm`), Blender, IFC and 3ds Max. Revit files are not supported.
