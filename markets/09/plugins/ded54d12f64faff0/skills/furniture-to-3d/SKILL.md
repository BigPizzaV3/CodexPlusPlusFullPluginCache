---
name: furniture-to-3d
description: Turn a photo of a single furniture piece into a textured 3D model (GLB) with MeltFlex. Use when the user wants a 3D model, an AR preview, or an asset for Blender, SketchUp, Unity or a web viewer.
---

# Furniture to 3D

## Steps

1. Ask for a photo of one item, ideally on a plain background and seen from a three-quarter angle.
2. Call `create_3d_furniture` with the photo as `image` (75 credits).
3. The card shows progress and offers the GLB download when the model is ready, usually in 2 to 3 minutes. If it does not update, call `check_job` with the `jobId` every 10 to 15 seconds.

## Tips

- Crop out other furniture; the model is built from the whole image.
- Set `textured: false` only when the user needs clean geometry for their own materials.
